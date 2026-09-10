"""RAG 配置管理：所有连接参数通过环境变量注入，禁止硬编码。"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


def _env(key: str, default: str = "") -> str:
    return os.getenv(key, default)


@dataclass(frozen=True)
class RAGConfig:
    """RAG 配置，字段在实例化时从环境变量读取。"""

    kb_root: str = field(default_factory=lambda: _env("KB_ROOT", "./kb"))
    vector_store: str = field(default_factory=lambda: _env("VECTOR_STORE", "chroma"))

    # Chroma
    chroma_dir: str = field(default_factory=lambda: _env("CHROMA_DIR", "./data/chroma"))

    # Milvus
    milvus_host: str = field(default_factory=lambda: _env("MILVUS_HOST", "localhost"))
    milvus_port: int = field(default_factory=lambda: int(_env("MILVUS_PORT", "19530")))
    milvus_collection: str = field(default_factory=lambda: _env("MILVUS_COLLECTION", "kb_rag"))
    milvus_drop_old: bool = field(
        default_factory=lambda: _env("MILVUS_DROP_OLD", "false").lower() == "true"
    )

    # Embedding
    embedding_provider: str = field(default_factory=lambda: _env("EMBEDDING_PROVIDER", "local"))
    local_embedding_model: str = field(
        default_factory=lambda: _env("LOCAL_EMBEDDING_MODEL", "models/bge-large-zh-v1.5")
    )
    openai_api_base: Optional[str] = field(
        default_factory=lambda: _env("OPENAI_API_BASE") or None
    )
    openai_api_key: Optional[str] = field(
        default_factory=lambda: _env("OPENAI_API_KEY") or None
    )
    openai_embedding_model: Optional[str] = field(
        default_factory=lambda: _env("OPENAI_EMBEDDING_MODEL") or None
    )

    # 检索
    top_k: int = field(default_factory=lambda: int(_env("TOP_K", "5")))
    similarity_threshold: float = field(
        default_factory=lambda: float(_env("SIMILARITY_THRESHOLD", "0.75"))
    )
    graph_hops: int = field(default_factory=lambda: int(_env("GRAPH_HOPS", "2")))

    @property
    def kb_path(self) -> Path:
        return Path(self.kb_root)
