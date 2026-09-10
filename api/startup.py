"""RAG 检索器启动期初始化：构建索引、图谱、向量库。

启动时一次性构建（约 1-2 分钟），构建完成后缓存在模块级全局变量。
Render free tier 无持久盘，每次启动从 Markdown 源重建索引（数据在仓库里，可接受）。

容错策略：正常流程失败时自动降级到 FakeEmbeddings + FakeVectorStore，
确保服务始终能启动起来（health 端点可用），方便排查环境变量问题。
"""

from __future__ import annotations

import logging
import math
import os
from pathlib import Path

logger = logging.getLogger("kb.api.startup")

_retriever = None
_build_lock = False
_is_fake = False


def _make_fake_embeddings():
    """FakeEmbeddings：基于字符频率的向量，仅在云端 API 不可用时兜底。"""

    class FakeEmbeddings:
        DIM = 64

        def _embed(self, text):
            vec = [0.0] * self.DIM
            for ch in text:
                vec[ord(ch) % self.DIM] += 1.0
            n = math.sqrt(sum(v * v for v in vec)) or 1.0
            return [v / n for v in vec]

        def embed_documents(self, texts):
            return [self._embed(t) for t in texts]

        def embed_query(self, text):
            return self._embed(text)

    return FakeEmbeddings()


def _make_fake_store():
    """FakeVectorStore：纯内存，不依赖 ChromaDB。"""

    class FakeDoc:
        def __init__(self, pc, md):
            self.page_content = pc
            self.metadata = md

    class FakeStore:
        def __init__(self):
            self._texts = []
            self._mds = []
            self._emb = _make_fake_embeddings()

        def add_texts(self, texts, metadatas):
            ids = []
            for t, m in zip(texts, metadatas):
                self._texts.append(t)
                self._mds.append(m)
                ids.append(f"id_{len(self._texts) - 1}")
            return ids

        def similarity_search_with_score(self, query, k):
            q = self._emb.embed_query(query)
            scored = []
            for i, t in enumerate(self._texts):
                d = self._emb.embed_query(t)
                sim = sum(a * b for a, b in zip(q, d))
                scored.append((sim, i))
            scored.sort(key=lambda x: x[0], reverse=True)
            return [
                (FakeDoc(self._texts[i], self._mds[i]), sim)
                for sim, i in scored[:k]
            ]

    return FakeStore()


def build_retriever():
    """构建 FourDimRetriever 并缓存到模块全局。

    优先用真实 Embedding（本地或云端 API）+ ChromaDB；
    任何环节失败则降级到 FakeEmbeddings + FakeVectorStore，确保服务可用。
    """
    global _retriever, _build_lock, _is_fake
    if _retriever is not None or _build_lock:
        return
    _build_lock = True
    try:
        from rag.config import RAGConfig
        from rag.loader import iter_entries
        from rag.graph import build_graph
        from rag.retriever import FourDimRetriever

        cfg = RAGConfig()
        logger.info("开始构建 RAG 索引：kb_root=%s, vector_store=%s", cfg.kb_root, cfg.vector_store)

        chunks = list(iter_entries(cfg.kb_root))
        logger.info("解析到 %d 个 chunk", len(chunks))

        # 优先用真实 Embedding + ChromaDB
        embeddings = None
        store = None
        try:
            from rag.embeddings import build_embedding
            from rag.vector_store import build_vector_store, ingest

            embeddings = build_embedding(cfg)
            store = build_vector_store(cfg, embeddings)
            ids = ingest(cfg, store, chunks)
            logger.info("真实向量库构建完成，写入 %d 个向量", len(ids))
            _is_fake = False
        except Exception as e:
            logger.warning("真实 Embedding/向量库构建失败：%s，降级到 Fake", e)
            embeddings = _make_fake_embeddings()
            store = _make_fake_store()
            ids = store.add_texts(
                texts=[c.text for c in chunks],
                metadatas=[
                    {
                        "entry_id": c.entry_id,
                        "layer": c.layer,
                        "title": c.title,
                        "section": c.section,
                        "keywords": ",".join(c.keywords) if hasattr(c, "keywords") else "",
                        "source_path": c.source_path,
                    }
                    for c in chunks
                ],
            )
            logger.info("Fake 向量库构建完成，写入 %d 个向量", len(ids))
            _is_fake = True

        # 图谱
        import networkx as nx
        adj_path = cfg.kb_path / "20-standards" / "knowledge-graph-adjacency.md"
        if adj_path.exists():
            G = build_graph(adj_path)
            logger.info("知识图谱构建完成：节点 %d，边 %d", G.number_of_nodes(), G.number_of_edges())
        else:
            logger.warning("邻接表不存在：%s，使用空图", adj_path)
            G = nx.DiGraph()

        _retriever = FourDimRetriever(cfg, store, G, chunks)
        if _is_fake:
            logger.warning("RAG 检索器构建完成（FakeEmbeddings 兜底）")
        else:
            logger.info("RAG 检索器构建完成")
    finally:
        _build_lock = False


def get_retriever():
    return _retriever


def get_graph():
    return _retriever.graph if _retriever is not None else None


def get_chunk_index():
    return _retriever._chunk_index if _retriever is not None else {}


def is_fake():
    """当前是否在用 FakeEmbeddings 兜底（用于 /health 端点显示）。"""
    return _is_fake
