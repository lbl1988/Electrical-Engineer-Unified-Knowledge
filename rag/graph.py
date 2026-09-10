"""知识图谱：从邻接表 Markdown 构建 NetworkX 图，支持 BFS 扩展与最短路径。"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Iterable

import networkx as nx

_ID_RE = re.compile(r"(TH|PR|CALC|CASE)(?:-[A-Z]+)?-\d{3}")


def _extract_id(text: str) -> str:
    """从文本中提取条目 ID。"""
    m = _ID_RE.search(text)
    return m.group(0) if m else ""


def build_graph(adj_path: str | Path) -> nx.DiGraph:
    """从邻接表 Markdown 构建有向图。"""
    G = nx.DiGraph()
    text = Path(adj_path).read_text(encoding="utf-8")

    for line in text.splitlines():
        if "|" not in line:
            continue
        parts = [p.strip() for p in line.split("|")]
        parts = [p for p in parts if p]  # 去掉首尾空
        if len(parts) < 3:
            continue
        src = _extract_id(parts[0])
        dst = _extract_id(parts[-1])
        rel = "->".join(parts[1:-1]) if len(parts) > 3 else parts[1]
        if src and dst and src != dst:
            G.add_edge(src, dst, relation=rel)
    return G


def graph_expand(
    G: nx.DiGraph, seeds: Iterable[str], hops: int
) -> list[str]:
    """对种子节点做 BFS，返回扩展节点 ID 列表（含种子）。

    hops=0 → 仅种子节点；hops=1 → 种子+直接邻居；hops=2 → 再加间接邻居。
    """
    expanded: set[str] = set()
    frontier: set[str] = set(s for s in seeds if s in G)
    # hops 跳需要 hops+1 轮：第 0 轮加种子，第 1 轮加一跳邻居，...
    for _ in range(max(hops, 0) + 1):
        expanded.update(frontier)
        next_frontier: set[str] = set()
        for node in frontier:
            next_frontier.update(G.successors(node))
            next_frontier.update(G.predecessors(node))
        frontier = next_frontier - expanded
    return list(expanded)


def find_path(G: nx.DiGraph, src: str, dst: str) -> list[str]:
    """查找最短路径，无路径返回空列表。"""
    try:
        return nx.shortest_path(G, src, dst)
    except (nx.NetworkXNoPath, nx.NodeNotFound):
        return []


def get_neighbors(G: nx.DiGraph, node: str, hops: int = 1) -> list[str]:
    """获取指定跳数的邻居。"""
    return graph_expand(G, [node], hops)
