"""RAG 检索 FastAPI 应用。

端点：
- GET /health            健康检查，返回 chunks 数
- GET /search?query=...&top_k=5   四维检索
- GET /entry/{entry_id}  条目详情
- GET /graph?entry_id=...&hops=2  图谱扩展
"""

from __future__ import annotations

import logging
import os
from typing import Optional

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware

from .startup import build_retriever, get_retriever, get_chunk_index, get_graph

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
logger = logging.getLogger("kb.api")

app = FastAPI(
    title="电气工程全域知识库 RAG API",
    description="四维检索：关键词 + 语义向量 + 知识图谱 + 标准溯源",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in os.getenv("CORS_ORIGINS", "*").split(",") if o.strip()],
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def _startup():
    """启动时构建索引。Render 默认 60s grace，若不够可在 render.yaml 调 healthCheckGracePeriodSeconds。"""
    build_retriever()


@app.get("/health")
def health():
    r = get_retriever()
    return {
        "status": "ok" if r is not None else "building",
        "chunks": len(r.all_chunks) if r else 0,
    }


@app.get("/search")
def search(query: str = Query(..., description="检索查询"), top_k: int = Query(5, ge=1, le=50)):
    """四维检索：向量 + 关键词 + 图谱 + 标准溯源，融合排序后返回 Top-K。"""
    r = get_retriever()
    if r is None:
        raise HTTPException(status_code=503, detail="检索器仍在构建中，请稍后重试")
    items = r.retrieve(query)
    results = []
    for it in items[:top_k]:
        results.append({
            "entry_id": it.entry_id,
            "layer": it.layer,
            "title": it.title,
            "section": it.section,
            "text": it.text[:500],  # 截断长文本
            "score": round(it.score, 4),
            "source": it.source,
            "source_path": it.source_path,
        })
    return {"query": query, "count": len(results), "results": results}


@app.get("/entry/{entry_id}")
def entry(entry_id: str):
    """按条目 ID 取详情（首个 chunk 的完整文本）。"""
    idx = get_chunk_index()
    c = idx.get(entry_id)
    if c is None:
        raise HTTPException(status_code=404, detail=f"条目 {entry_id} 不存在")
    return {
        "entry_id": c.entry_id,
        "layer": c.layer,
        "title": c.title,
        "section": c.section,
        "keywords": list(c.keywords) if hasattr(c, "keywords") else [],
        "text": c.text,
        "source_path": c.source_path,
    }


@app.get("/graph")
def graph(entry_id: str, hops: int = Query(2, ge=0, le=4)):
    """图谱扩展：从 entry_id 出发做 BFS，返回 hops 跳内的关联节点。"""
    G = get_graph()
    if G is None:
        raise HTTPException(status_code=503, detail="图谱未构建")
    if entry_id not in G:
        raise HTTPException(status_code=404, detail=f"节点 {entry_id} 不在图中")
    from rag.graph import graph_expand
    expanded = graph_expand(G, [entry_id], hops)
    neighbors = [n for n in expanded if n != entry_id]
    edges = []
    for n in neighbors:
        for succ in G.successors(n):
            if succ in expanded:
                edges.append({"source": n, "target": succ, "relation": G.edges[n, succ].get("relation", "")})
        for pred in G.predecessors(n):
            if pred in expanded:
                edges.append({"source": pred, "target": n, "relation": G.edges[pred, n].get("relation", "")})
    return {
        "seed": entry_id,
        "hops": hops,
        "nodes": expanded,
        "neighbors": neighbors,
        "edges": edges,
    }


@app.get("/")
def root():
    return {
        "name": "电气工程全域知识库 RAG API",
        "endpoints": ["/health", "/search", "/entry/{id}", "/graph"],
        "docs": "/docs",
    }
