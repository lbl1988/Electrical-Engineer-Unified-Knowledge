"""四维检索管道：向量 + 关键词(BM25) + 图谱 + 标准溯源 + Rerank。"""

from __future__ import annotations

import math
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from .config import RAGConfig
from .graph import graph_expand
from .loader import Chunk

_STD_RE = re.compile(r"((?:GB|GB/T|DL/T|NB/T|IEC|IEEE)\s?[\d]+(?:-[\d]{4})?)")


@dataclass
class RetrievedItem:
    """检索结果统一结构。"""

    entry_id: str
    layer: str
    title: str
    section: str
    text: str
    score: float
    source: str  # vector | keyword | graph | standard
    source_path: str = ""


def vector_search(
    store, query: str, top_k: int
) -> list[RetrievedItem]:
    """维度 1：语义向量检索。"""
    docs = store.similarity_search_with_score(query, k=top_k * 2)
    items: list[RetrievedItem] = []
    for doc, score in docs:
        meta = doc.metadata if hasattr(doc, "metadata") else {}
        items.append(
            RetrievedItem(
                entry_id=meta.get("entry_id", ""),
                layer=meta.get("layer", ""),
                title=meta.get("title", ""),
                section=meta.get("section", ""),
                text=doc.page_content if hasattr(doc, "page_content") else "",
                score=float(score),
                source="vector",
                source_path=meta.get("source_path", ""),
            )
        )
    return items[:top_k]


def bm25_search(
    query: str, chunks: Iterable[Chunk], top_k: int
) -> list[RetrievedItem]:
    """维度 2：BM25 关键词检索。"""
    terms = [t for t in re.split(r"\s+", query.strip()) if t]
    if not terms:
        return []

    chunk_list = list(chunks)
    N = len(chunk_list)
    if N == 0:
        return []

    df = Counter()
    for c in chunk_list:
        for t in set(terms):
            if t in c.text:
                df[t] += 1

    avgdl = sum(len(c.text) for c in chunk_list) / N
    k1, b = 1.5, 0.75

    scored: list[tuple[float, Chunk]] = []
    for c in chunk_list:
        score = 0.0
        dl = max(len(c.text), 1)
        # 中文无空格，使用子串出现次数作为词频
        for t in terms:
            if df[t] == 0:
                continue
            idf = math.log((N - df[t] + 0.5) / (df[t] + 0.5) + 1)
            f = c.text.count(t)
            score += idf * (f * (k1 + 1)) / (f + k1 * (1 - b + b * dl / avgdl))
        if score > 0:
            scored.append((score, c))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [
        RetrievedItem(
            entry_id=c.entry_id,
            layer=c.layer,
            title=c.title,
            section=c.section,
            text=c.text,
            score=s,
            source="keyword",
            source_path=c.source_path,
        )
        for s, c in scored[:top_k]
    ]


def standard_trace(query: str, standard_index_path: str | Path) -> list[dict]:
    """维度 4：标准溯源，返回匹配的标准号与片段。"""
    standards = set(_STD_RE.findall(query))
    if not standards:
        return []
    text = Path(standard_index_path).read_text(encoding="utf-8")
    results: list[dict] = []
    for std in standards:
        for line in text.splitlines():
            if std in line:
                results.append({"standard": std, "snippet": line.strip()[:200]})
    return results


def rerank(
    items: list[RetrievedItem], threshold: float
) -> list[RetrievedItem]:
    """融合排序：按 entry_id 聚合，多源命中加权。"""
    grouped: dict[str, list[RetrievedItem]] = defaultdict(list)
    for it in items:
        if it.score < threshold:
            continue
        grouped[it.entry_id].append(it)

    scored: list[tuple[float, RetrievedItem]] = []
    for entry_id, its in grouped.items():
        sources = {i.source for i in its}
        boost = 1.0 + 0.2 * len(sources)
        best = max(its, key=lambda i: i.score)
        scored.append((best.score * boost, best))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [it for _, it in scored]


class FourDimRetriever:
    """四维检索器。"""

    def __init__(
        self,
        cfg: RAGConfig,
        store,
        graph,
        all_chunks: list[Chunk],
    ) -> None:
        self.cfg = cfg
        self.store = store
        self.graph = graph
        self.all_chunks = all_chunks
        self._chunk_index = {c.entry_id: c for c in all_chunks}

    def retrieve(self, query: str) -> list[RetrievedItem]:
        """执行四维检索并融合排序。"""
        # 维度 1：向量
        v_items = vector_search(self.store, query, self.cfg.top_k)
        seeds = [i.entry_id for i in v_items]

        # 维度 3：图谱扩展
        expanded_ids = graph_expand(self.graph, seeds, self.cfg.graph_hops)
        g_items = [
            self._build_graph_item(eid)
            for eid in expanded_ids
            if eid not in seeds
        ]

        # 维度 2：关键词
        k_items = bm25_search(query, self.all_chunks, self.cfg.top_k)

        all_items = v_items + g_items + k_items
        return rerank(all_items, self.cfg.similarity_threshold)

    def _build_graph_item(self, entry_id: str) -> RetrievedItem:
        c = self._chunk_index.get(entry_id)
        if c is None:
            return RetrievedItem(
                entry_id=entry_id,
                layer="",
                title="",
                section="",
                text="",
                score=0.6,
                source="graph",
                source_path="",
            )
        return RetrievedItem(
            entry_id=c.entry_id,
            layer=c.layer,
            title=c.title,
            section=c.section,
            text=c.text,
            score=0.6,
            source="graph",
            source_path=c.source_path,
        )
