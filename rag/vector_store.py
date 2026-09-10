"""向量库构建与写入。"""

from __future__ import annotations

from typing import Protocol

from .config import RAGConfig
from .loader import Chunk


class VectorStore(Protocol):
    """向量库最小接口契约。"""

    def add_texts(self, texts: list[str], metadatas: list[dict]) -> list[str]: ...

    def similarity_search_with_score(
        self, query: str, k: int
    ) -> list[tuple[object, float]]: ...


def build_vector_store(cfg: RAGConfig, embeddings) -> VectorStore:
    """根据配置构建向量库实例。"""
    if cfg.vector_store == "chroma":
        import chromadb
        from langchain_community.vectorstores import Chroma

        client = chromadb.PersistentClient(path=cfg.chroma_dir)
        return Chroma(
            client=client,
            collection_name=cfg.milvus_collection,
            embedding_function=embeddings,
        )
    elif cfg.vector_store == "milvus":
        from langchain_milvus import Milvus

        return Milvus(
            embedding_function=embeddings,
            connection_args={"host": cfg.milvus_host, "port": cfg.milvus_port},
            collection_name=cfg.milvus_collection,
            drop_old=cfg.milvus_drop_old,
        )
    else:
        raise ValueError(f"未知向量库: {cfg.vector_store}")


def ingest(cfg: RAGConfig, store: VectorStore, chunks: list[Chunk]) -> list[str]:
    """批量写入向量库，返回写入的 ID 列表。"""
    if not chunks:
        return []
    texts = [c.text for c in chunks]
    metadatas = [
        {
            "entry_id": c.entry_id,
            "layer": c.layer,
            "title": c.title,
            "section": c.section,
            "keywords": ",".join(c.keywords),
            "source_path": c.source_path,
        }
        for c in chunks
    ]
    return store.add_texts(texts=texts, metadatas=metadatas)
