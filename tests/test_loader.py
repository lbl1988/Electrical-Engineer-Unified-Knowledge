"""loader 模块单元测试。"""

from __future__ import annotations

from pathlib import Path

import pytest

from rag.loader import (
    CHUNK_OVERLAP,
    CHUNK_SIZE,
    Chunk,
    iter_entries,
    parse_entry,
    split_into_chunks,
)


class TestParseEntry:
    def test_parse_th_entry(self, sample_kb: Path):
        """正确解析 TH 条目的 entry_id/layer/front_matter。"""
        fp = sample_kb / "10-theory" / "TH-006-transformer-leakage-impedance.md"
        entry_id, layer, fm, body = parse_entry(fp)
        assert entry_id == "TH-006"
        assert layer == "TH"
        assert fm["title"] == "变压器短路阻抗的物理来源"
        assert "变压器" in fm["keywords"]
        assert "短路阻抗" in body

    def test_parse_pr_entry(self, sample_kb: Path):
        """正确解析 PR 条目。"""
        fp = sample_kb / "30-practice" / "PR-DD-002-substation-layout.md"
        entry_id, layer, fm, body = parse_entry(fp)
        assert entry_id == "PR-DD-002"
        assert layer == "PR"
        assert fm["title"] == "变电所布置与设备选型"

    def test_parse_calc_entry(self, sample_kb: Path):
        """正确解析 CALC 条目。"""
        fp = sample_kb / "40-calc" / "CALC-SC-001-low-voltage-short-circuit.md"
        entry_id, layer, fm, body = parse_entry(fp)
        assert entry_id == "CALC-SC-001"
        assert layer == "CALC"

    def test_parse_no_front_matter(self, tmp_path: Path):
        """无 front matter 的文件返回空 fm。"""
        fp = tmp_path / "TH-099-test.md"
        fp.write_text("# 无 front matter\n\n正文内容", encoding="utf-8")
        entry_id, layer, fm, body = parse_entry(fp)
        assert entry_id == "TH-099"
        assert fm == {}
        assert "正文内容" in body

    def test_parse_non_entry_file(self, tmp_path: Path):
        """文件名不含条目 ID 时返回空 entry_id。"""
        fp = tmp_path / "README.md"
        fp.write_text("# README", encoding="utf-8")
        entry_id, layer, fm, body = parse_entry(fp)
        assert entry_id == ""
        assert layer == ""


class TestSplitIntoChunks:
    def test_single_section_no_split(self):
        """短章节不二次切分。"""
        chunks = split_into_chunks(
            "TH-001", "TH", {"title": "测试"},
            "## 摘要\n这是一段短文本", "src.md",
        )
        assert len(chunks) == 1
        assert chunks[0].section == "摘要"
        assert "短文本" in chunks[0].text

    def test_long_section_split(self):
        """长章节按 CHUNK_SIZE 切分，带 overlap。"""
        long_text = "字" * (CHUNK_SIZE["TH"] + 100)
        chunks = split_into_chunks(
            "TH-001", "TH", {"title": "测试"},
            f"## 摘要\n{long_text}", "src.md",
        )
        # 至少切成 2 块
        assert len(chunks) >= 2
        # 第一块长度 <= CHUNK_SIZE
        assert len(chunks[0].text) <= CHUNK_SIZE["TH"]
        # overlap 验证：第二块开头应与第一块结尾有重叠
        assert chunks[0].text[-CHUNK_OVERLAP:] in chunks[1].text

    def test_keywords_parsing(self):
        """关键词按中英文逗号分隔。"""
        chunks = split_into_chunks(
            "TH-001", "TH",
            {"title": "测试", "keywords": "变压器, 短路阻抗，漏磁场"},
            "## 摘要\n正文", "src.md",
        )
        assert chunks[0].keywords == ["变压器", "短路阻抗", "漏磁场"]

    def test_layer_specific_chunk_size(self):
        """不同层使用不同分块大小。"""
        # CALC 层 CHUNK_SIZE=300
        long_text = "字" * 350
        chunks = split_into_chunks(
            "CALC-001", "CALC", {"title": "测试"},
            f"## 方法\n{long_text}", "src.md",
        )
        assert len(chunks) >= 2
        assert len(chunks[0].text) <= 300

    def test_empty_body_no_chunks(self):
        """空正文不产生 chunk。"""
        chunks = split_into_chunks(
            "TH-001", "TH", {"title": "测试"},
            "## 摘要\n", "src.md",
        )
        assert chunks == []


class TestIterEntries:
    def test_iter_all_entries(self, sample_kb: Path):
        """遍历所有条目，跳过 README。"""
        chunks = list(iter_entries(sample_kb))
        ids = {c.entry_id for c in chunks}
        assert "TH-006" in ids
        assert "PR-DD-002" in ids
        assert "CALC-SC-001" in ids

    def test_iter_yields_chunk_objects(self, sample_kb: Path):
        """产出的都是 Chunk 实例。"""
        for c in iter_entries(sample_kb):
            assert isinstance(c, Chunk)
            assert c.entry_id
            assert c.layer in ("TH", "PR", "CALC", "CASE")
