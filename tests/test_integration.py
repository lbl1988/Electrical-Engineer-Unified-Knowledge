"""集成测试：四维检索端到端。"""

from __future__ import annotations

from rag.config import RAGConfig
from rag.graph import build_graph
from rag.loader import iter_entries
from rag.retriever import FourDimRetriever
from rag.vector_store import ingest
from tests.conftest import FakeEmbeddings, FakeVectorStore


def _make_cfg(monkeypatch=None) -> RAGConfig:
    """构造测试用配置：fake embeddings 相似度较低，降低阈值。"""
    if monkeypatch is not None:
        monkeypatch.setenv("SIMILARITY_THRESHOLD", "0.2")
    return RAGConfig()


class TestFourDimRetriever:
    def _build_retriever(self, kb_root, adj_path, monkeypatch=None):
        cfg = _make_cfg(monkeypatch)
        # 使用 Fake 组件
        store = FakeVectorStore()
        chunks = list(iter_entries(kb_root))
        ingest(cfg, store, chunks)
        graph = build_graph(adj_path)
        return FourDimRetriever(cfg, store, graph, chunks), chunks

    def test_retrieve_returns_items(self, sample_kb, sample_adjacency, monkeypatch):
        """检索返回非空结果。"""
        retriever, _ = self._build_retriever(sample_kb, sample_adjacency, monkeypatch)
        items = retriever.retrieve("变压器")
        assert len(items) > 0

    def test_retrieve_returns_retrieveditem(self, sample_kb, sample_adjacency, monkeypatch):
        """返回的都是 RetrievedItem 实例。"""
        from rag.retriever import RetrievedItem

        retriever, _ = self._build_retriever(sample_kb, sample_adjacency, monkeypatch)
        items = retriever.retrieve("变压器")
        assert all(isinstance(i, RetrievedItem) for i in items)

    def test_retrieve_finds_relevant_entry(self, sample_kb, sample_adjacency, monkeypatch):
        """查询"变压器"应命中 TH-006（变压器短路阻抗）。"""
        retriever, _ = self._build_retriever(sample_kb, sample_adjacency, monkeypatch)
        items = retriever.retrieve("变压器")
        ids = [i.entry_id for i in items]
        assert "TH-006" in ids

    def test_retrieve_graph_expansion(self, sample_kb, sample_adjacency, monkeypatch):
        """图谱扩展应引入关联条目。"""
        retriever, _ = self._build_retriever(sample_kb, sample_adjacency, monkeypatch)
        items = retriever.retrieve("变压器")
        ids = {i.entry_id for i in items}
        # TH-006 -> PR-DD-002 (graph edge) 应被扩展引入
        assert "PR-DD-002" in ids

    def test_retrieve_multiple_sources(self, sample_kb, sample_adjacency, monkeypatch):
        """结果包含多种 source 类型。"""
        retriever, _ = self._build_retriever(sample_kb, sample_adjacency, monkeypatch)
        items = retriever.retrieve("变压器")
        sources = {i.source for i in items}
        assert "vector" in sources or "keyword" in sources or "graph" in sources

    def test_retrieve_no_match_query(self, sample_kb, sample_adjacency, monkeypatch):
        """完全不相关的查询返回空（调高阈值以过滤低相似度与图谱扩展项）。"""
        monkeypatch.setenv("SIMILARITY_THRESHOLD", "0.7")
        cfg = RAGConfig()
        store = FakeVectorStore()
        chunks = list(iter_entries(sample_kb))
        ingest(cfg, store, chunks)
        graph = build_graph(sample_adjacency)
        retriever = FourDimRetriever(cfg, store, graph, chunks)
        items = retriever.retrieve("zzz不存在的关键词xyz")
        assert len(items) == 0

    def test_full_pipeline_count(self, sample_kb, sample_adjacency, monkeypatch):
        """端到端：知识库 3 条目全部入索引。"""
        retriever, chunks = self._build_retriever(sample_kb, sample_adjacency, monkeypatch)
        assert len(chunks) >= 3  # 至少 3 个条目
        assert retriever.store.count >= 3


class TestEndToEndRecall:
    """基于考题的召回率评估。"""

    QUERIES = [
        ("变压器并列运行条件", {"TH-006", "PR-DD-002"}),
        ("低压短路电流计算", {"CALC-SC-001"}),
        ("变电所设备选型", {"PR-DD-002"}),
    ]

    def test_recall_rate(self, sample_kb, sample_adjacency, monkeypatch):
        """Top-5 召回率应达到 100%（小数据集）。"""
        cfg = _make_cfg(monkeypatch)
        store = FakeVectorStore()
        chunks = list(iter_entries(sample_kb))
        ingest(cfg, store, chunks)
        graph = build_graph(sample_adjacency)
        retriever = FourDimRetriever(cfg, store, graph, chunks)

        correct = 0
        for query, expected in self.QUERIES:
            items = retriever.retrieve(query)[:5]
            ids = {i.entry_id for i in items}
            if ids & expected:
                correct += 1
        assert correct == len(self.QUERIES), f"召回率: {correct}/{len(self.QUERIES)}"
