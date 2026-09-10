"""RAG 检索模块：四维检索（关键词 + 语义向量 + 知识图谱 + 标准溯源）。"""

from .config import RAGConfig
from .loader import Chunk, iter_entries, parse_entry, split_into_chunks
from .graph import build_graph, graph_expand, find_path, get_neighbors
from .retriever import (
    RetrievedItem,
    vector_search,
    bm25_search,
    standard_trace,
    rerank,
    FourDimRetriever,
)

__all__ = [
    "RAGConfig",
    "Chunk",
    "iter_entries",
    "parse_entry",
    "split_into_chunks",
    "build_graph",
    "graph_expand",
    "find_path",
    "get_neighbors",
    "RetrievedItem",
    "vector_search",
    "bm25_search",
    "standard_trace",
    "rerank",
    "FourDimRetriever",
]
