"""RAG 检索器启动期初始化：构建索引、图谱、向量库。

启动时一次性构建（约 1-2 分钟），构建完成后缓存在模块级全局变量。
Render free tier 无持久盘，每次启动从 Markdown 源重建索引（数据在仓库里，可接受）。
"""

from __future__ import annotations

import logging
import os
from pathlib import Path

logger = logging.getLogger("kb.api.startup")

_retriever = None
_build_lock = False


def build_retriever():
    """构建 FourDimRetriever 并缓存到模块全局。

    依赖环境变量：KB_ROOT、VECTOR_STORE、EMBEDDING_PROVIDER、OPENAI_*。
    """
    global _retriever, _build_lock
    if _retriever is not None or _build_lock:
        return
    _build_lock = True
    try:
        # 复用 kb/rag/ 现有模块（kb/ 已通过 uvicorn --app-dir 加入 sys.path）
        from rag.config import RAGConfig
        from rag.loader import iter_entries
        from rag.embeddings import build_embedding
        from rag.vector_store import build_vector_store, ingest
        from rag.graph import build_graph, graph_expand
        from rag.retriever import FourDimRetriever

        cfg = RAGConfig()
        logger.info("开始构建 RAG 索引：kb_root=%s, vector_store=%s", cfg.kb_root, cfg.vector_store)

        chunks = list(iter_entries(cfg.kb_root))
        logger.info("解析到 %d 个 chunk", len(chunks))

        embeddings = build_embedding(cfg)
        store = build_vector_store(cfg, embeddings)
        ids = ingest(cfg, store, chunks)
        logger.info("已写入 %d 个向量", len(ids))

        # 邻接表文件路径：{kb_root}/20-standards/knowledge-graph-adjacency.md
        adj_path = cfg.kb_path / "20-standards" / "knowledge-graph-adjacency.md"
        if adj_path.exists():
            G = build_graph(adj_path)
            logger.info("知识图谱构建完成：节点 %d，边 %d", G.number_of_nodes(), G.number_of_edges())
        else:
            logger.warning("邻接表不存在：%s，使用空图", adj_path)
            import networkx as nx
            G = nx.DiGraph()

        _retriever = FourDimRetriever(cfg, store, G, chunks)
        logger.info("RAG 检索器构建完成")
    finally:
        _build_lock = False


def get_retriever():
    """获取已构建的检索器实例，未构建返回 None。"""
    return _retriever


def get_graph():
    """获取已构建的知识图谱。"""
    return _retriever.graph if _retriever is not None else None


def get_chunk_index():
    """获取 entry_id → Chunk 索引。"""
    return _retriever._chunk_index if _retriever is not None else {}
