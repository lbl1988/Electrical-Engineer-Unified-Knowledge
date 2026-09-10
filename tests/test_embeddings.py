"""embeddings 模块单元测试。"""

from __future__ import annotations

import pytest

from rag.config import RAGConfig
from rag.embeddings import build_embedding
from tests.conftest import FakeEmbeddings


class TestFakeEmbeddings:
    def test_embed_documents_returns_vectors(self):
        """embed_documents 返回与输入等长的向量列表。"""
        emb = FakeEmbeddings()
        vectors = emb.embed_documents(["变压器", "变电所", "短路电流"])
        assert len(vectors) == 3
        assert all(len(v) == FakeEmbeddings.DIM for v in vectors)

    def test_embed_query_returns_vector(self):
        """embed_query 返回单个向量。"""
        emb = FakeEmbeddings()
        v = emb.embed_query("变压器")
        assert len(v) == FakeEmbeddings.DIM

    def test_deterministic(self):
        """相同输入产生相同向量。"""
        emb = FakeEmbeddings()
        v1 = emb.embed_query("变压器")
        v2 = emb.embed_query("变压器")
        assert v1 == v2

    def test_different_inputs_different_vectors(self):
        """不同输入产生不同向量。"""
        emb = FakeEmbeddings()
        v1 = emb.embed_query("变压器")
        v2 = emb.embed_query("变电所")
        assert v1 != v2

    def test_normalized(self):
        """向量归一化（L2 范数约为 1）。"""
        emb = FakeEmbeddings()
        v = emb.embed_query("变压器")
        norm = sum(x * x for x in v) ** 0.5
        assert abs(norm - 1.0) < 0.01


class TestBuildEmbedding:
    def test_unknown_provider_raises(self, monkeypatch):
        """未知 provider 抛出 ValueError。"""
        monkeypatch.setenv("EMBEDDING_PROVIDER", "unknown")
        cfg = RAGConfig()
        with pytest.raises(ValueError, match="未知 embedding provider"):
            build_embedding(cfg)

    def test_openai_without_model_raises(self, monkeypatch):
        """openai provider 未配置模型名抛出 ValueError。"""
        monkeypatch.setenv("EMBEDDING_PROVIDER", "openai")
        monkeypatch.delenv("OPENAI_EMBEDDING_MODEL", raising=False)
        cfg = RAGConfig()
        with pytest.raises(ValueError, match="openai_embedding_model 未配置"):
            build_embedding(cfg)
