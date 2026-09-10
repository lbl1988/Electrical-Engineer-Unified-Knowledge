"""graph 模块单元测试。"""

from __future__ import annotations

import networkx as nx
import pytest

from rag.graph import build_graph, find_path, get_neighbors, graph_expand


class TestBuildGraph:
    def test_build_from_adjacency(self, sample_adjacency):
        """从邻接表构建有向图。"""
        G = build_graph(sample_adjacency)
        assert isinstance(G, nx.DiGraph)
        assert G.has_edge("TH-006", "PR-DD-002")
        assert G.has_edge("PR-DD-002", "CALC-SC-001")
        assert G.has_edge("TH-006", "TH-023")

    def test_relation_metadata(self, sample_adjacency):
        """边的 relation 属性正确。"""
        G = build_graph(sample_adjacency)
        assert G["TH-006"]["PR-DD-002"]["relation"] == "上游→"
        assert G["PR-DD-002"]["CALC-SC-001"]["relation"] == "下游→"

    def test_no_self_loop(self, sample_adjacency):
        """不产生自环。"""
        G = build_graph(sample_adjacency)
        assert not G.has_edge("TH-006", "TH-006")

    def test_empty_file(self, tmp_path):
        """空文件返回空图。"""
        p = tmp_path / "empty.md"
        p.write_text("", encoding="utf-8")
        G = build_graph(p)
        assert G.number_of_nodes() == 0
        assert G.number_of_edges() == 0


class TestGraphExpand:
    def test_expand_one_hop(self, sample_adjacency):
        """1 跳扩展包含直接邻居。"""
        G = build_graph(sample_adjacency)
        result = graph_expand(G, ["TH-006"], hops=1)
        assert "TH-006" in result
        assert "PR-DD-002" in result  # 后继
        assert "TH-023" in result  # 后继

    def test_expand_two_hops(self, sample_adjacency):
        """2 跳扩展包含间接邻居。"""
        G = build_graph(sample_adjacency)
        result = graph_expand(G, ["TH-006"], hops=2)
        assert "CALC-SC-001" in result  # TH-006 -> PR-DD-002 -> CALC-SC-001

    def test_expand_zero_hops_returns_seed(self, sample_adjacency):
        """0 跳只返回种子节点（如果在图中）。"""
        G = build_graph(sample_adjacency)
        result = graph_expand(G, ["TH-006"], hops=0)
        assert result == ["TH-006"]

    def test_expand_seed_not_in_graph(self, sample_adjacency):
        """种子不在图中返回空列表。"""
        G = build_graph(sample_adjacency)
        result = graph_expand(G, ["XX-999"], hops=2)
        assert result == []

    def test_expand_multiple_seeds(self, sample_adjacency):
        """多个种子合并扩展。"""
        G = build_graph(sample_adjacency)
        result = graph_expand(G, ["TH-006", "PR-DD-002"], hops=1)
        assert "TH-006" in result
        assert "PR-DD-002" in result
        assert "CALC-SC-001" in result


class TestFindPath:
    def test_find_existing_path(self, sample_adjacency):
        """存在路径时返回节点列表。"""
        G = build_graph(sample_adjacency)
        path = find_path(G, "TH-006", "CALC-SC-001")
        assert path == ["TH-006", "PR-DD-002", "CALC-SC-001"]

    def test_find_no_path(self, sample_adjacency):
        """无路径返回空列表。"""
        G = build_graph(sample_adjacency)
        path = find_path(G, "CALC-SC-001", "TH-006")  # 反向无路径
        assert path == []

    def test_find_node_not_found(self, sample_adjacency):
        """节点不存在返回空列表。"""
        G = build_graph(sample_adjacency)
        assert find_path(G, "XX-001", "TH-006") == []


class TestGetNeighbors:
    def test_get_neighbors_one_hop(self, sample_adjacency):
        """1 跳邻居。"""
        G = build_graph(sample_adjacency)
        neighbors = get_neighbors(G, "TH-006", hops=1)
        assert "PR-DD-002" in neighbors
        assert "TH-023" in neighbors
