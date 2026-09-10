"""retriever 模块单元测试。"""

from __future__ import annotations

from rag.loader import Chunk
from rag.retriever import (
    RetrievedItem,
    bm25_search,
    rerank,
    standard_trace,
    vector_search,
)
from tests.conftest import FakeVectorStore


class TestVectorSearch:
    def test_returns_items(self):
        """向量检索返回 RetrievedItem 列表。"""
        store = FakeVectorStore()
        store.add_texts(
            ["变压器短路阻抗源于漏磁通", "变电所布置原则"],
            [
                {"entry_id": "TH-006", "layer": "TH", "title": "变压器", "section": "摘要", "source_path": "a.md"},
                {"entry_id": "PR-DD-002", "layer": "PR", "title": "变电所", "section": "设计", "source_path": "b.md"},
            ],
        )
        items = vector_search(store, "变压器", top_k=5)
        assert len(items) == 2
        assert all(isinstance(i, RetrievedItem) for i in items)
        assert all(i.source == "vector" for i in items)

    def test_sorted_by_score_desc(self):
        """结果按相似度降序排列。"""
        store = FakeVectorStore()
        store.add_texts(
            ["变压器短路阻抗", "变电所布置"],
            [
                {"entry_id": "TH-006", "layer": "TH", "title": "变压器", "section": "摘要", "source_path": "a.md"},
                {"entry_id": "PR-DD-002", "layer": "PR", "title": "变电所", "section": "设计", "source_path": "b.md"},
            ],
        )
        items = vector_search(store, "变压器", top_k=5)
        scores = [i.score for i in items]
        assert scores == sorted(scores, reverse=True)

    def test_respects_top_k(self):
        """返回数量不超过 top_k。"""
        store = FakeVectorStore()
        store.add_texts(
            ["文本1", "文本2", "文本3"],
            [
                {"entry_id": "A", "layer": "TH", "title": "A", "section": "s", "source_path": "a.md"},
                {"entry_id": "B", "layer": "TH", "title": "B", "section": "s", "source_path": "b.md"},
                {"entry_id": "C", "layer": "TH", "title": "C", "section": "s", "source_path": "c.md"},
            ],
        )
        items = vector_search(store, "查询", top_k=2)
        assert len(items) <= 2


class TestBM25Search:
    def test_match_relevant_chunk(self, sample_chunks):
        """BM25 能匹配含关键词的 chunk。"""
        items = bm25_search("变压器", sample_chunks, top_k=5)
        assert len(items) > 0
        assert all(i.source == "keyword" for i in items)
        # 含"变压器"的 chunk 应排在前面
        assert "变压器" in items[0].text

    def test_no_match(self, sample_chunks):
        """无匹配关键词返回空。"""
        items = bm25_search("xyz不存在", sample_chunks, top_k=5)
        assert items == []

    def test_empty_query(self, sample_chunks):
        """空查询返回空。"""
        items = bm25_search("", sample_chunks, top_k=5)
        assert items == []

    def test_empty_chunks(self):
        """空 chunk 列表返回空。"""
        items = bm25_search("变压器", [], top_k=5)
        assert items == []

    def test_sorted_by_score(self, sample_chunks):
        """结果按 BM25 分数降序。"""
        items = bm25_search("变压器 短路", sample_chunks, top_k=5)
        scores = [i.score for i in items]
        assert scores == sorted(scores, reverse=True)


class TestStandardTrace:
    def test_match_standard(self, sample_standard_index):
        """查询含标准号时返回匹配片段。"""
        results = standard_trace("按 GB 50054 要求设计", sample_standard_index)
        assert len(results) > 0
        assert any("GB 50054" in r["standard"] for r in results)

    def test_no_standard(self, sample_standard_index):
        """查询无标准号返回空。"""
        results = standard_trace("变压器并列运行", sample_standard_index)
        assert results == []

    def test_multiple_standards(self, sample_standard_index):
        """多标准号同时匹配。"""
        results = standard_trace("GB 50054 和 GB/T 14285", sample_standard_index)
        standards = {r["standard"] for r in results}
        assert "GB 50054" in standards
        assert "GB/T 14285" in standards


class TestRerank:
    def _make_item(self, entry_id, score, source):
        return RetrievedItem(
            entry_id=entry_id, layer="TH", title="t", section="s",
            text="x", score=score, source=source,
        )

    def test_filter_below_threshold(self):
        """低于阈值的条目被过滤。"""
        items = [
            self._make_item("TH-001", 0.9, "vector"),
            self._make_item("TH-002", 0.5, "keyword"),
        ]
        result = rerank(items, threshold=0.7)
        ids = {i.entry_id for i in result}
        assert "TH-001" in ids
        assert "TH-002" not in ids

    def test_multi_source_boost(self):
        """多源命中的条目排名提升。"""
        items = [
            self._make_item("TH-001", 0.8, "vector"),
            self._make_item("TH-001", 0.7, "keyword"),  # 同条目双源
            self._make_item("TH-002", 0.85, "vector"),   # 单源高分
        ]
        result = rerank(items, threshold=0.5)
        # TH-001 双源加权: max(0.8,0.7)*1.4 = 1.12 > TH-002: 0.85*1.2 = 1.02
        assert result[0].entry_id == "TH-001"

    def test_sorted_desc(self):
        """结果按加权分降序。"""
        items = [
            self._make_item("TH-001", 0.6, "vector"),
            self._make_item("TH-002", 0.9, "vector"),
        ]
        result = rerank(items, threshold=0.5)
        assert result[0].entry_id == "TH-002"

    def test_empty_input(self):
        """空输入返回空。"""
        assert rerank([], threshold=0.5) == []
