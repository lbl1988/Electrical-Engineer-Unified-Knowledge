"""Embedding 封装：本地模型或云端 API，接口统一。"""

from __future__ import annotations

from typing import Protocol

from .config import RAGConfig


class EmbeddingModel(Protocol):
    """Embedding 模型最小接口契约。"""

    def embed_documents(self, texts: list[str]) -> list[list[float]]: ...

    def embed_query(self, text: str) -> list[float]: ...


def build_embedding(cfg: RAGConfig) -> EmbeddingModel:
    """根据配置构建 Embedding 模型。"""
    if cfg.embedding_provider == "local":
        from langchain_community.embeddings import HuggingFaceEmbeddings

        return HuggingFaceEmbeddings(
            model_name=cfg.local_embedding_model,
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": True},
        )
    elif cfg.embedding_provider == "openai":
        if not cfg.openai_embedding_model:
            raise ValueError("openai_embedding_model 未配置")
        from langchain_openai import OpenAIEmbeddings

        return OpenAIEmbeddings(
            model=cfg.openai_embedding_model,
            openai_api_base=cfg.openai_api_base,
            openai_api_key=cfg.openai_api_key,
        )
    else:
        raise ValueError(f"未知 embedding provider: {cfg.embedding_provider}")
