"""索引构建入口。"""

from __future__ import annotations

from .config import RAGConfig
from .embeddings import build_embedding
from .loader import iter_entries
from .vector_store import build_vector_store, ingest


def main() -> None:
    cfg = RAGConfig()
    print(f"知识库路径: {cfg.kb_root}")
    print(f"向量库: {cfg.vector_store}")

    chunks = list(iter_entries(cfg.kb_root))
    print(f"共解析 {len(chunks)} 个 chunk")

    embeddings = build_embedding(cfg)
    store = build_vector_store(cfg, embeddings)
    ids = ingest(cfg, store, chunks)
    print(f"已写入 {len(ids)} 个 chunk")
    print("索引构建完成")


if __name__ == "__main__":
    main()
