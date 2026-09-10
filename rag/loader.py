"""Markdown 解析与分层分块。"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterator

# 分层分块大小（字符数）
CHUNK_SIZE: dict[str, int] = {
    "TH": 500,
    "PR": 400,
    "CALC": 300,
    "CASE": 500,
    "STD": 200,
}
CHUNK_OVERLAP = 50

# 从文件名推断层与 ID（支持子域名，如 PR-DD-002、CALC-SC-001、TH-006）
_LAYER_RE = re.compile(r"(TH|PR|CALC|CASE)(?:-([A-Z]+))?-(\d+)")
_FRONT_MATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


@dataclass
class Chunk:
    """一个文本分块。"""

    entry_id: str
    layer: str
    title: str
    keywords: list[str] = field(default_factory=list)
    section: str = ""
    text: str = ""
    source_path: str = ""


def _parse_front_matter(text: str) -> tuple[dict[str, str], str]:
    """解析 YAML front matter，返回 (fm_dict, body)。"""
    m = _FRONT_MATTER_RE.match(text)
    if not m:
        return {}, text
    fm_text = m.group(1)
    body = text[m.end():]
    fm: dict[str, str] = {}
    for line in fm_text.splitlines():
        if ":" in line and not line.strip().startswith("#"):
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm, body


def parse_entry(file_path: Path) -> tuple[str, str, dict[str, str], str]:
    """解析单个 Markdown 文件，返回 (entry_id, layer, front_matter, body)。"""
    text = file_path.read_text(encoding="utf-8")
    fm, body = _parse_front_matter(text)
    m = _LAYER_RE.search(file_path.name)
    if not m:
        return "", "", fm, body
    layer = m.group(1)
    sub = m.group(2) or ""
    num = int(m.group(3))
    entry_id = f"{layer}-{sub}-{num:03d}" if sub else f"{layer}-{num:03d}"
    return entry_id, layer, fm, body


def split_into_chunks(
    entry_id: str,
    layer: str,
    fm: dict[str, str],
    body: str,
    source_path: str,
) -> list[Chunk]:
    """按章节标题切分，再对超长章节二次切分。"""
    size = CHUNK_SIZE.get(layer, 400)
    title = fm.get("title", "")
    keywords_raw = fm.get("keywords", "")
    keywords = [k.strip() for k in re.split(r"[,，]", keywords_raw) if k.strip()]

    # 按 ## 标题分段
    sections = re.split(r"\n## ", body)
    chunks: list[Chunk] = []

    for sec in sections:
        sec = sec.strip()
        if not sec:
            continue
        lines = sec.splitlines()
        sec_title = lines[0].replace("#", "").strip()
        sec_body = "\n".join(lines[1:]).strip()
        if not sec_body:
            continue

        # 二次切分（滑动窗口）
        while len(sec_body) > size:
            cut = sec_body[:size]
            chunks.append(
                Chunk(
                    entry_id=entry_id,
                    layer=layer,
                    title=title,
                    keywords=keywords,
                    section=sec_title,
                    text=cut,
                    source_path=source_path,
                )
            )
            sec_body = sec_body[size - CHUNK_OVERLAP:]
        if sec_body:
            chunks.append(
                Chunk(
                    entry_id=entry_id,
                    layer=layer,
                    title=title,
                    keywords=keywords,
                    section=sec_title,
                    text=sec_body,
                    source_path=source_path,
                )
            )
    return chunks


def iter_entries(kb_root: str | Path) -> Iterator[Chunk]:
    """遍历知识库所有条目，产出 Chunk。"""
    root = Path(kb_root)
    patterns = [
        "10-theory/*.md",
        "30-practice/*.md",
        "40-calc/*.md",
        "50-case/*.md",
    ]
    for pattern in patterns:
        for fp in sorted(root.glob(pattern)):
            if fp.name == "README.md":
                continue
            entry_id, layer, fm, body = parse_entry(fp)
            if not entry_id:
                continue
            rel = fp.relative_to(root).as_posix()
            yield from split_into_chunks(entry_id, layer, fm, body, rel)
