"""vector_store 模块单元测试（使用 FakeVectorStore）。"""

from __future__ import annotations

import pytest

from rag.loader import Chunk
from rag.vector_store import ingest
from tests.conftest import FakeVectorStore


class TestIngest:
    def test_ingest_writes_chunks(self, sample_chunks):
        """ingest 将 chunks 写入向量库。"""
        store = FakeVectorStore()
        ids = ingest(None, store, sample_chunks)
        assert len(ids) == 3
        assert store.count == 3

    def test_ingest_empty(self):
        """空 chunks 列表返回空 ID 列表。"""
        store = FakeVectorStore()
        ids = ingest(None, store, [])
        assert ids == []
        assert store.count == 0

    def test_ingest_metadata_fields(self, sample_chunks):
        """ingest 写入的 metadata 包含必要字段。"""
        store = FakeVectorStore()
        ingest(None, store, sample_chunks)
        # FakeVectorStore 内部 _metadatas
        for m in store._metadatas:
            assert "entry_id" in m
            assert "layer" in m
            assert "title" in m
            assert "section" in m
            assert "keywords" in m
            assert "source_path" in m

    def test_ingest_preserves_entry_id(self, sample_chunks):
        """metadata 中的 entry_id 与 chunk 一致。"""
        store = FakeVectorStore()
        ingest(None, store, sample_chunks)
        ids = [m["entry_id"] for m in store._metadatas]
        assert "TH-006" in ids
        assert "PR-DD-002" in ids
        assert "CALC-SC-001" in ids


class TestFakeVectorStore:
    def test_add_and_search(self):
        """FakeVectorStore 能写入并检索。"""
        store = FakeVectorStore()
        store.add_texts(
            ["变压器短路阻抗", "变电所布置"],
            [{"entry_id": "TH-006"}, {"entry_id": "PR-DD-002"}],
        )
        docs = store.similarity_search_with_score("变压器", k=2)
        assert len(docs) == 2
        # 第一个应是"变压器短路阻抗"（相似度更高）
        assert "变压器" in docs[0][0].page_content

    def test_count(self):
        """count 属性返回写入数量。"""
        store = FakeVectorStore()
        assert store.count == 0
        store.add_texts(["a", "b"], [{}, {}])
        assert store.count == 2
