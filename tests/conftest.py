"""pytest 公共夹具与测试桩。"""

from __future__ import annotations

import os
import sys
import textwrap
from pathlib import Path

import pytest

# 将 kb 目录加入 sys.path，使 rag 包可导入
_KB_ROOT = Path(__file__).resolve().parent.parent
if str(_KB_ROOT) not in sys.path:
    sys.path.insert(0, str(_KB_ROOT))

from rag.loader import Chunk  # noqa: E402


# ---------------------------------------------------------------------------
# 测试数据夹具
# ---------------------------------------------------------------------------

@pytest.fixture
def sample_kb(tmp_path: Path) -> Path:
    """构造一个最小知识库，含 TH/PR/CALC 各一条。"""
    (tmp_path / "10-theory").mkdir()
    (tmp_path / "30-practice").mkdir()
    (tmp_path / "40-calc").mkdir()
    (tmp_path / "50-case").mkdir()

    (tmp_path / "10-theory" / "TH-006-transformer-leakage-impedance.md").write_text(
        textwrap.dedent("""\
        ---
        id: TH-006
        title: 变压器短路阻抗的物理来源
        keywords: 变压器, 短路阻抗, 漏磁场, uk%
        ---

        # 变压器短路阻抗的物理来源

        ## 1. 摘要
        变压器短路阻抗源于漏磁通，uk%表征额定电流下漏抗压降标幺值。

        ## 2. 推导
        uk% = (I_N * X_k / U_N) * 100
        漏磁通路径在高低压绕组之间。
        """),
        encoding="utf-8",
    )

    (tmp_path / "30-practice" / "PR-DD-002-substation-layout.md").write_text(
        textwrap.dedent("""\
        ---
        id: PR-DD-002
        title: 变电所布置与设备选型
        keywords: 变电所, 变压器, 开关柜
        ---

        # 变电所布置与设备选型

        ## 1. 摘要
        变电所主接线与设备布置原则。

        ## 2. 设计要点
        变压器并列运行需满足变比相等条件。
        """),
        encoding="utf-8",
    )

    (tmp_path / "40-calc" / "CALC-SC-001-low-voltage-short-circuit.md").write_text(
        textwrap.dedent("""\
        ---
        id: CALC-SC-001
        title: 低压三相短路电流计算
        keywords: 短路电流, 低压, 三相
        ---

        # 低压三相短路电流计算

        ## 1. 方法
        Ik = c * Un / (sqrt(3) * Zsys)

        ## 2. 算例
        变压器阻抗决定短路电流大小。
        """),
        encoding="utf-8",
    )

    return tmp_path


@pytest.fixture
def sample_chunks() -> list[Chunk]:
    """构造测试用 Chunk 列表。"""
    return [
        Chunk(
            entry_id="TH-006",
            layer="TH",
            title="变压器短路阻抗",
            keywords=["变压器", "短路阻抗"],
            section="摘要",
            text="变压器短路阻抗源于漏磁通，uk%表征额定电流下漏抗压降标幺值",
            source_path="10-theory/TH-006.md",
        ),
        Chunk(
            entry_id="PR-DD-002",
            layer="PR",
            title="变电所布置",
            keywords=["变电所", "变压器"],
            section="设计要点",
            text="变压器并列运行需满足变比相等条件",
            source_path="30-practice/PR-DD-002.md",
        ),
        Chunk(
            entry_id="CALC-SC-001",
            layer="CALC",
            title="低压短路计算",
            keywords=["短路电流", "变压器"],
            section="方法",
            text="Ik = c * Un / (sqrt(3) * Zsys)",
            source_path="40-calc/CALC-SC-001.md",
        ),
    ]


@pytest.fixture
def sample_adjacency(tmp_path: Path) -> Path:
    """构造最小邻接表 Markdown。"""
    p = tmp_path / "adj.md"
    p.write_text(
        textwrap.dedent("""\
        | 节点 | 关系 | 目标 |
        |---|---|---|
        | TH-006 变压器漏抗 | 上游→ | PR-DD-002 变电所布置 |
        | PR-DD-002 变电所布置 | 下游→ | CALC-SC-001 短路计算 |
        | TH-006 变压器漏抗 | 同级→ | TH-023 变压器并列 |
        """),
        encoding="utf-8",
    )
    return p


@pytest.fixture
def sample_standard_index(tmp_path: Path) -> Path:
    """构造最小标准索引。"""
    p = tmp_path / "std.md"
    p.write_text(
        textwrap.dedent("""\
        | 标准号 | 要求 |
        |---|---|
        | GB 50054 | 低压配电设计规范 |
        | GB/T 14285 | 继电保护配置原则 |
        """),
        encoding="utf-8",
    )
    return p


# ---------------------------------------------------------------------------
# 测试桩：FakeEmbeddings 与 FakeVectorStore
# ---------------------------------------------------------------------------

class FakeDocument:
    """模拟 langchain Document。"""

    def __init__(self, page_content: str, metadata: dict):
        self.page_content = page_content
        self.metadata = metadata


class FakeEmbeddings:
    """Embedding 测试桩：基于字符频率的向量，语义相似度与字符重叠正相关。"""

    DIM = 64

    def _embed(self, text: str) -> list[float]:
        # 字符频率向量：相同字符越多，余弦相似度越高
        vec = [0.0] * self.DIM
        for ch in text:
            vec[ord(ch) % self.DIM] += 1.0
        norm = math_sqrt(sum(v * v for v in vec)) or 1.0
        return [v / norm for v in vec]

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        return [self._embed(t) for t in texts]

    def embed_query(self, text: str) -> list[float]:
        return self._embed(text)


def math_sqrt(x: float) -> float:
    return x ** 0.5


class FakeVectorStore:
    """向量库测试桩：内存存储，按余弦相似度检索。"""

    def __init__(self):
        self._texts: list[str] = []
        self._metadatas: list[dict] = []
        self._embeddings = FakeEmbeddings()

    def add_texts(self, texts: list[str], metadatas: list[dict]) -> list[str]:
        ids = []
        for i, (t, m) in enumerate(zip(texts, metadatas)):
            self._texts.append(t)
            self._metadatas.append(m)
            ids.append(f"id_{len(self._texts) - 1}")
        return ids

    def similarity_search_with_score(
        self, query: str, k: int
    ) -> list[tuple[FakeDocument, float]]:
        q_vec = self._embeddings.embed_query(query)
        scored: list[tuple[float, int]] = []
        for i, text in enumerate(self._texts):
            d_vec = self._embeddings.embed_query(text)
            sim = sum(a * b for a, b in zip(q_vec, d_vec))
            scored.append((sim, i))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [
            (FakeDocument(self._texts[i], self._metadatas[i]), sim)
            for sim, i in scored[:k]
        ]

    @property
    def count(self) -> int:
        return len(self._texts)
