"""config 模块单元测试。"""

from __future__ import annotations

import os

from rag.config import RAGConfig


class TestRAGConfig:
    def test_default_values(self, monkeypatch):
        """未设置环境变量时使用默认值。"""
        for key in [
            "VECTOR_STORE", "MILVUS_PORT", "MILVUS_DROP_OLD",
            "TOP_K", "SIMILARITY_THRESHOLD", "GRAPH_HOPS",
        ]:
            monkeypatch.delenv(key, raising=False)

        cfg = RAGConfig()
        assert cfg.vector_store == "chroma"
        assert cfg.milvus_port == 19530
        assert cfg.milvus_drop_old is False
        assert cfg.top_k == 5
        assert cfg.similarity_threshold == 0.75
        assert cfg.graph_hops == 2

    def test_env_override(self, monkeypatch):
        """环境变量覆盖默认值。"""
        monkeypatch.setenv("VECTOR_STORE", "milvus")
        monkeypatch.setenv("MILVUS_PORT", "29530")
        monkeypatch.setenv("MILVUS_DROP_OLD", "true")
        monkeypatch.setenv("TOP_K", "10")
        monkeypatch.setenv("SIMILARITY_THRESHOLD", "0.8")
        monkeypatch.setenv("GRAPH_HOPS", "3")

        cfg = RAGConfig()
        assert cfg.vector_store == "milvus"
        assert cfg.milvus_port == 29530
        assert cfg.milvus_drop_old is True
        assert cfg.top_k == 10
        assert cfg.similarity_threshold == 0.8
        assert cfg.graph_hops == 3

    def test_drop_old_false_by_default(self, monkeypatch):
        """drop_old 默认为 false，防止误清库。"""
        monkeypatch.delenv("MILVUS_DROP_OLD", raising=False)
        cfg = RAGConfig()
        assert cfg.milvus_drop_old is False

    def test_optional_openai_fields_none(self, monkeypatch):
        """未配置 OpenAI 参数时为 None。"""
        for key in ["OPENAI_API_BASE", "OPENAI_API_KEY", "OPENAI_EMBEDDING_MODEL"]:
            monkeypatch.delenv(key, raising=False)
        cfg = RAGConfig()
        assert cfg.openai_api_base is None
        assert cfg.openai_api_key is None
        assert cfg.openai_embedding_model is None

    def test_kb_path_returns_path(self):
        """kb_path 返回 Path 对象。"""
        from pathlib import Path

        cfg = RAGConfig()
        assert isinstance(cfg.kb_path, Path)
