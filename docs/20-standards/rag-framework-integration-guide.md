---
id: REF-RAG-INT
title: RAG 框架接入指南（LangChain/LlamaIndex + Chroma/Milvus 代码级对接）
domain: REF
subdomain: RAG 接入
voltage_levels: [LV, MV, HV, EHV]
lifecycle: [设计, 考试, 运维]
standards:
  - { code: 内部规范, clause: "§8", note: "四维检索：关键词+语义向量+知识图谱+标准溯源" }
status: published
version: 1.0
updated: 2026-09-10
---

# RAG 框架接入指南（LangChain/LlamaIndex + Chroma/Milvus 代码级对接）

> **用途**：提供将本知识库接入 RAG 框架的代码级操作指南。配套 [rag-usage-guide.md](rag-usage-guide.md)（架构与流程）、[rag-metadata-index.md](rag-metadata-index.md)（元数据）、[knowledge-graph-adjacency.md](knowledge-graph-adjacency.md)（图谱）。
> **适用环境**：Windows / Linux，Python 3.10+。

---

## 1. 组件选型决策树

接入前先确定以下三项，避免盲目堆砌依赖：

| 决策点 | 选项 A（轻量/本地） | 选项 B（生产/云端） | 选择依据 |
|---|---|---|---|
| **向量库** | ChromaDB（嵌入式，零配置） | Milvus（分布式，需部署） | 条目数 < 500 → Chroma；> 5000 → Milvus |
| **Embedding** | 本地模型（bge-large-zh-v1.5） | 云端 API（需确认模型名） | 无外网 → 本地；有合规 API → 云端 |
| **编排框架** | LangChain（生态成熟） | LlamaIndex（文档检索专精） | 需图谱/流程编排 → LangChain+LangGraph；纯文档检索 → LlamaIndex |
| **全文索引** | Tantivy/MeiliSearch（Rust） | Elasticsearch | 轻量 → Tantivy；已有 ES → ES |
| **图谱** | NetworkX（内存图） | Neo4j（图数据库） | 边 < 10000 → NetworkX；> 10000 → Neo4j |

> ⚠️ **Embedding 模型名必须以供应商官方文档为准**，切勿从示例代码中猜测模型名。本地模型需提前下载至 `models/` 目录。

---

## 2. 环境准备

### 2.1 依赖安装

```bash
# 核心依赖
pip install langchain langchain-community langchain-core
pip install pyyaml python-dotenv tqdm

# 向量库（二选一）
pip install chromadb                  # 轻量
# pip install pymilvus langchain-milvus  # 生产

# Embedding（二选一）
# 本地：需先 sentence-transformers + 模型下载
pip install sentence-transformers
# 云端：按供应商 SDK
# pip install openai  # OpenAI 兼容接口

# 图谱
pip install networkx

# 全文（可选）
pip install tantivy
```

### 2.2 配置文件 `.env`

所有连接参数通过环境变量注入，**禁止硬编码**：

```env
# === 知识库路径 ===
KB_ROOT=./kb

# === 向量库 ===
VECTOR_STORE=chroma                 # chroma | milvus
CHROMA_DIR=./data/chroma
# MILVUS_HOST=localhost
# MILVUS_PORT=19530
MILVUS_COLLECTION=kb_rag
MILVUS_DROP_OLD=false               # ⚠️ 设为 true 会清空集合，确认后再改

# === Embedding ===
EMBEDDING_PROVIDER=local            # local | openai
# 本地模型
LOCAL_EMBEDDING_MODEL=models/bge-large-zh-v1.5
# 云端（OpenAI 兼容）
# OPENAI_API_BASE=https://api.example.com/v1
# OPENAI_API_KEY=sk-xxx
# OPENAI_EMBEDDING_MODEL=text-embedding-3-large   # 以官方文档为准

# === 检索参数 ===
TOP_K=5
SIMILARITY_THRESHOLD=0.75
GRAPH_HOPS=2                        # 图谱遍历跳数

# === LLM（可选，用于生成回答） ===
# LLM_PROVIDER=openai
# LLM_MODEL=gpt-4
# LLM_API_BASE=https://api.example.com/v1
# LLM_API_KEY=sk-xxx
```

---

## 3. 目录结构映射

知识库 Markdown 文件与 RAG 组件的对应关系：

```
kb/
├── 10-theory/TH-*.md       → 向量化源（五段式分块）
├── 30-practice/PR-*.md     → 向量化源（九段式分块）
├── 40-calc/CALC-*.md       → 向量化源（步骤式分块）
├── 50-case/CASE-*.md       → 向量化源（场景式分块）
├── 20-standards/
│   ├── rag-metadata-index.md    → 元数据提取源
│   ├── knowledge-graph-adjacency.md → 图谱构建源
│   └── cn-02/cn-03-*.md         → 标准溯源源
└── 00-meta/                  → 术语表（同义词扩展）
```

---

## 4. 索引构建

### 4.1 配置类（config.py）

```python
from dataclasses import dataclass, field
from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class RAGConfig:
    kb_root: str = os.getenv("KB_ROOT", "./kb")
    vector_store: str = os.getenv("VECTOR_STORE", "chroma")
    chroma_dir: str = os.getenv("CHROMA_DIR", "./data/chroma")
    milvus_host: str = os.getenv("MILVUS_HOST", "localhost")
    milvus_port: int = int(os.getenv("MILVUS_PORT", "19530"))
    milvus_collection: str = os.getenv("MILVUS_COLLECTION", "kb_rag")
    milvus_drop_old: bool = os.getenv("MILVUS_DROP_OLD", "false").lower() == "true"

    embedding_provider: str = os.getenv("EMBEDDING_PROVIDER", "local")
    local_embedding_model: str = os.getenv("LOCAL_EMBEDDING_MODEL", "models/bge-large-zh-v1.5")
    openai_api_base: Optional[str] = os.getenv("OPENAI_API_BASE")
    openai_api_key: Optional[str] = os.getenv("OPENAI_API_KEY")
    openai_embedding_model: Optional[str] = os.getenv("OPENAI_EMBEDDING_MODEL")

    top_k: int = int(os.getenv("TOP_K", "5"))
    similarity_threshold: float = float(os.getenv("SIMILARITY_THRESHOLD", "0.75"))
    graph_hops: int = int(os.getenv("GRAPH_HOPS", "2"))
```

### 4.2 Markdown 解析与分块（loader.py）

按知识库分层结构定义分块策略：

```python
import re
from pathlib import Path
from typing import Iterator
from dataclasses import dataclass

@dataclass
class Chunk:
    entry_id: str        # 如 TH-001
    layer: str           # TH | PR | CALC | CASE | STD
    title: str
    keywords: list[str]
    section: str         # 所在章节名
    text: str            # 分块文本
    source_path: str     # 相对路径

# 分层分块大小（字符数）
CHUNK_SIZE = {
    "TH":   500,   # 理论层：五段式
    "PR":   400,   # 实践层：九段式
    "CALC": 300,   # 计算层：步骤式
    "CASE": 500,   # 案例层：场景式
    "STD":  200,   # 标准层：条款式
}
CHUNK_OVERLAP = 50

# 从文件名推断层与 ID
_LAYER_RE = re.compile(r"(TH|PR|CALC|CASE)-(\d+)")

def parse_entry(file_path: Path) -> tuple[str, str, dict, str]:
    """解析单个 Markdown，返回 (entry_id, layer, front_matter, body)"""
    text = file_path.read_text(encoding="utf-8")
    # 提取 YAML front matter
    if text.startswith("---"):
        _, fm_text, body = text.split("---", 2)
    else:
        fm_text, body = "", text

    fm: dict = {}
    for line in fm_text.strip().splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"')

    m = _LAYER_RE.search(file_path.name)
    if not m:
        return "", "", fm, body
    layer = m.group(1)
    num = m.group(2)
    entry_id = f"{layer}-{int(num):03d}"
    return entry_id, layer, fm, body

def split_into_chunks(entry_id: str, layer: str, fm: dict,
                      body: str, source_path: str) -> list[Chunk]:
    """按章节标题切分，再对超长章节二次切分"""
    size = CHUNK_SIZE.get(layer, 400)
    # 按 ## 标题分段
    sections = re.split(r"\n## ", body)
    chunks: list[Chunk] = []
    title = fm.get("title", "")
    keywords = [k.strip() for k in fm.get("keywords", "").split(",") if k.strip()]

    for sec in sections:
        sec = sec.strip()
        if not sec:
            continue
        sec_title = sec.splitlines()[0].replace("#", "").strip()
        sec_body = "\n".join(sec.splitlines()[1:])

        # 二次切分（滑动窗口）
        while len(sec_body) > size:
            cut = sec_body[:size]
            chunks.append(Chunk(entry_id, layer, title, keywords, sec_title, cut, source_path))
            sec_body = sec_body[size - CHUNK_OVERLAP:]
        if sec_body:
            chunks.append(Chunk(entry_id, layer, title, keywords, sec_title, sec_body, source_path))
    return chunks

def iter_entries(kb_root: str) -> Iterator[Chunk]:
    """遍历知识库所有条目，产出 Chunk"""
    root = Path(kb_root)
    for pattern in ["10-theory/*.md", "30-practice/*.md", "40-calc/*.md", "50-case/*.md"]:
        for fp in root.glob(pattern):
            if fp.name == "README.md":
                continue
            entry_id, layer, fm, body = parse_entry(fp)
            if not entry_id:
                continue
            rel = fp.relative_to(root).as_posix()
            yield from split_into_chunks(entry_id, layer, fm, body, rel)
```

### 4.3 Embedding 封装（embeddings.py）

**两种 Provider，接口统一**：

```python
from typing import Protocol

class EmbeddingModel(Protocol):
    def embed_documents(self, texts: list[str]) -> list[list[float]]: ...
    def embed_query(self, text: str) -> list[float]: ...

def build_embedding(cfg: RAGConfig) -> EmbeddingModel:
    if cfg.embedding_provider == "local":
        from langchain_community.embeddings import HuggingFaceEmbeddings
        # 需提前下载模型到 cfg.local_embedding_model
        return HuggingFaceEmbeddings(
            model_name=cfg.local_embedding_model,
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": True},
        )
    elif cfg.embedding_provider == "openai":
        from langchain_openai import OpenAIEmbeddings
        # ⚠️ model_name 必须以供应商官方文档为准
        return OpenAIEmbeddings(
            model=cfg.openai_embedding_model,
            openai_api_base=cfg.openai_api_base,
            openai_api_key=cfg.openai_api_key,
        )
    else:
        raise ValueError(f"未知 embedding provider: {cfg.embedding_provider}")
```

### 4.4 向量库构建（vector_store.py）

```python
from typing import Optional
from langchain_core.embeddings import Embeddings
from langchain_core.vectorstores import VectorStore
from .loader import Chunk

def build_vector_store(cfg: RAGConfig, embeddings: Embeddings) -> VectorStore:
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
        # ⚠️ drop_old=true 会清空集合，仅在重建索引时使用
        return Milvus(
            embedding_function=embeddings,
            connection_args={"host": cfg.milvus_host, "port": cfg.milvus_port},
            collection_name=cfg.milvus_collection,
            drop_old=cfg.milvus_drop_old,
        )
    else:
        raise ValueError(f"未知向量库: {cfg.vector_store}")

def ingest(cfg: RAGConfig, store: VectorStore, chunks: list[Chunk]) -> None:
    """批量写入向量库"""
    texts = [c.text for c in chunks]
    metadatas = [{
        "entry_id": c.entry_id,
        "layer": c.layer,
        "title": c.title,
        "section": c.section,
        "keywords": ",".join(c.keywords),
        "source_path": c.source_path,
    } for c in chunks]
    store.add_texts(texts=texts, metadatas=metadatas)
    print(f"已写入 {len(chunks)} 个 chunk")
```

### 4.5 构建入口（build_index.py）

```python
from .config import RAGConfig
from .loader import iter_entries
from .embeddings import build_embedding
from .vector_store import build_vector_store, ingest

def main() -> None:
    cfg = RAGConfig()
    print(f"知识库路径: {cfg.kb_root}")
    print(f"向量库: {cfg.vector_store}")

    chunks = list(iter_entries(cfg.kb_root))
    print(f"共解析 {len(chunks)} 个 chunk")

    embeddings = build_embedding(cfg)
    store = build_vector_store(cfg, embeddings)
    ingest(cfg, store, chunks)
    print("索引构建完成")

if __name__ == "__main__":
    main()
```

---

## 5. 四维检索管道

### 5.1 检索结果统一结构

```python
from dataclasses import dataclass

@dataclass
class RetrievedItem:
    entry_id: str
    layer: str
    title: str
    section: str
    text: str
    score: float          # 相似度 / 关键词匹配分
    source: str           # vector | keyword | graph | standard
    source_path: str
```

### 5.2 维度 1：语义向量检索

```python
from langchain_core.vectorstores import VectorStore

def vector_search(store: VectorStore, query: str, top_k: int) -> list[RetrievedItem]:
    docs = store.similarity_search_with_score(query, k=top_k * 2)
    items: list[RetrievedItem] = []
    for doc, score in docs:
        # Chroma 返回欧氏距离，需归一化；Milvus 直接返回相似度
        items.append(RetrievedItem(
            entry_id=doc.metadata["entry_id"],
            layer=doc.metadata["layer"],
            title=doc.metadata["title"],
            section=doc.metadata["section"],
            text=doc.page_content,
            score=float(score),
            source="vector",
            source_path=doc.metadata["source_path"],
        ))
    return items
```

### 5.3 维度 2：关键词检索（BM25）

```python
from collections import Counter
import math

def bm25_search(query: str, chunks: list[Chunk], top_k: int) -> list[RetrievedItem]:
    terms = query.split()
    df = Counter()
    for c in chunks:
        for t in set(terms):
            if t in c.text:
                df[t] += 1
    N = len(chunks)
    avgdl = sum(len(c.text) for c in chunks) / max(N, 1)
    k1, b = 1.5, 0.75

    scored: list[tuple[float, Chunk]] = []
    for c in chunks:
        score = 0.0
        dl = len(c.text)
        tf = Counter(c.text.split())
        for t in terms:
            if df[t] == 0:
                continue
            idf = math.log((N - df[t] + 0.5) / (df[t] + 0.5) + 1)
            f = tf.get(t, 0)
            score += idf * (f * (k1 + 1)) / (f + k1 * (1 - b + b * dl / avgdl))
        if score > 0:
            scored.append((score, c))
    scored.sort(key=lambda x: x[0], reverse=True)

    return [RetrievedItem(
        entry_id=c.entry_id, layer=c.layer, title=c.title,
        section=c.section, text=c.text, score=s,
        source="keyword", source_path=c.source_path,
    ) for s, c in scored[:top_k]]
```

### 5.4 维度 3：知识图谱遍历

解析 [knowledge-graph-adjacency.md](knowledge-graph-adjacency.md) 构建邻接表，对向量检索 Top-K 结果做 BFS 扩展：

```python
import re
import networkx as nx
from pathlib import Path

def build_graph(adj_path: str) -> nx.DiGraph:
    """从邻接表 Markdown 构建有向图"""
    G = nx.DiGraph()
    text = Path(adj_path).read_text(encoding="utf-8")
    # 匹配 "TH-001 标题 | 关系 | TH-002 标题" 行
    for line in text.splitlines():
        if "|" not in line:
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) < 3:
            continue
        src = _extract_id(parts[0])
        dst = _extract_id(parts[-1])
        rel = parts[1] if len(parts) == 3 else "->".join(parts[1:-1])
        if src and dst:
            G.add_edge(src, dst, relation=rel)
    return G

def _extract_id(text: str) -> str:
    m = re.search(r"(TH|PR|CALC|CASE)-\d{3}", text)
    return m.group(0) if m else ""

def graph_expand(G: nx.DiGraph, seeds: list[str], hops: int) -> list[str]:
    """对种子节点做 BFS，返回扩展节点 ID"""
    expanded = set(seeds)
    frontier = set(seeds)
    for _ in range(hops):
        next_frontier = set()
        for node in frontier:
            if node in G:
                next_frontier.update(G.successors(node))
                next_frontier.update(G.predecessors(node))
        expanded.update(next_frontier)
        frontier = next_frontier
    return list(expanded)
```

### 5.5 维度 4：标准溯源

```python
import re

# 标准号正则：GB 50054、GB/T 14285-2006、DL/T 553 等
STD_RE = re.compile(r"(GB|GB/T|DL/T|NB/T|IEC|IEEE)\s?[\d]+(?:-[\d]{4})?")

def standard_trace(query: str, standard_index_path: str) -> list[dict]:
    """从查询中提取标准号，返回匹配的条款要点"""
    standards = STD_RE.findall(query)
    if not standards:
        return []
    text = Path(standard_index_path).read_text(encoding="utf-8")
    results = []
    for std in set(standards):
        for line in text.splitlines():
            if std in line:
                results.append({"standard": std, "snippet": line.strip()[:200]})
    return results
```

### 5.6 融合排序（Rerank）

```python
from collections import defaultdict

def rerank(items: list[RetrievedItem], threshold: float) -> list[RetrievedItem]:
    """按 entry_id 聚合，多源命中加分"""
    grouped: dict[str, list[RetrievedItem]] = defaultdict(list)
    for it in items:
        if it.score < threshold:
            continue
        grouped[it.entry_id].append(it)

    scored: list[tuple[float, RetrievedItem]] = []
    for entry_id, its in grouped.items():
        # 多源命中加权：vector + keyword + graph 同时命中 → 加分
        sources = {i.source for i in its}
        boost = 1.0 + 0.2 * len(sources)
        best = max(its, key=lambda i: i.score)
        scored.append((best.score * boost, best))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [it for _, it in scored]
```

### 5.7 完整检索管道（retriever.py）

```python
class FourDimRetriever:
    def __init__(self, cfg: RAGConfig, store, graph, all_chunks):
        self.cfg = cfg
        self.store = store
        self.graph = graph
        self.all_chunks = all_chunks

    def retrieve(self, query: str) -> list[RetrievedItem]:
        # 维度1：向量
        v_items = vector_search(self.store, query, self.cfg.top_k)
        seeds = [i.entry_id for i in v_items]

        # 维度3：图谱扩展
        expanded_ids = graph_expand(self.graph, seeds, self.cfg.graph_hops)
        g_items = [self._build_graph_item(eid) for eid in expanded_ids
                   if eid not in seeds]

        # 维度2：关键词
        k_items = bm25_search(query, self.all_chunks, self.cfg.top_k)

        # 维度4：标准溯源
        s_items = standard_trace(query, "kb/20-standards/cn-02-供配电考纲口径索引.md")

        all_items = v_items + g_items + k_items
        return rerank(all_items, self.cfg.similarity_threshold)

    def _build_graph_item(self, entry_id: str) -> RetrievedItem:
        # 从 all_chunks 中找到对应条目最佳 chunk
        for c in self.all_chunks:
            if c.entry_id == entry_id:
                return RetrievedItem(
                    entry_id=c.entry_id, layer=c.layer, title=c.title,
                    section=c.section, text=c.text, score=0.6,
                    source="graph", source_path=c.source_path,
                )
        return RetrievedItem(entry_id, "", "", "", "", 0.0, "graph", "")
```

---

## 6. 查询服务 API

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .retriever import FourDimRetriever

app = FastAPI(title="电气知识库 RAG 服务")
retriever: FourDimRetriever | None = None

class QueryRequest(BaseModel):
    query: str
    top_k: int = 5

class RetrievedItemOut(BaseModel):
    entry_id: str
    title: str
    layer: str
    section: str
    text: str
    score: float
    source: str
    source_path: str

@app.post("/retrieve", response_model=list[RetrievedItemOut])
def retrieve(req: QueryRequest) -> list[RetrievedItemOut]:
    if retriever is None:
        raise HTTPException(503, "检索服务未初始化")
    items = retriever.retrieve(req.query)[:req.top_k]
    return [RetrievedItemOut(**i.__dict__) for i in items]
```

---

## 7. 知识图谱集成细节

### 7.1 邻接表解析规则

[knowledge-graph-adjacency.md](knowledge-graph-adjacency.md) 中表格格式：

```
| 源节点 | 关系 | 目标节点 |
```

- 节点 ID 格式：`TH-\d{3}` / `PR-\d{3}` / `CALC-\d{3}` / `CASE-\d{3}`
- 关系类型：`上游→`、`同级→`、`下游→`、`标准溯源`
- 解析时用正则提取 ID，忽略标题文本

### 7.2 图查询接口

```python
def find_path(G: nx.DiGraph, src: str, dst: str) -> list[str]:
    """查找最短路径（用于"从 A 到 B 的关联链条"）"""
    try:
        return nx.shortest_path(G, src, dst)
    except nx.NetworkXNoPath:
        return []

def get_neighbors(G: nx.DiGraph, node: str, hops: int = 1) -> list[str]:
    """获取指定跳数的邻居"""
    return graph_expand(G, [node], hops)
```

---

## 8. 测试与验证

### 8.1 索引构建验证

```python
def test_index_built(store):
    assert store._collection.count() > 0  # Chroma
    # Milvus: assert store.col.num_entities > 0

def test_query_returns_results(retriever):
    items = retriever.retrieve("变压器并列运行条件")
    assert len(items) > 0
    # 应命中 TH-023 变压器并列运行
    ids = {i.entry_id for i in items}
    assert "TH-023" in ids
```

### 8.2 召回率评估（基于考题）

```python
TEST_QUERIES = [
    ("变压器并列运行条件", {"TH-023", "TH-006"}),
    ("10kV馈线保护整定", {"PR-PE-002", "CALC-PT-001"}),
    ("UPS后备时间计算", {"PR-PS-003", "CALC-BT-002"}),
    ("接地制式选择", {"PR-GR-002", "TH-021"}),
]

def evaluate_recall(retriever):
    correct = 0
    for query, expected in TEST_QUERIES:
        items = retriever.retrieve(query)
        ids = {i.entry_id for i in items[:5]}
        if ids & expected:
            correct += 1
    print(f"Top-5 召回率: {correct}/{len(TEST_QUERIES)}")
```

---

## 9. 维护操作

### 9.1 增量更新（新增条目）

```python
def add_entry(entry_path: str, store, embeddings):
    chunks = list(iter_single_entry(entry_path))
    ingest(RAGConfig(), store, chunks)
    print(f"新增 {len(chunks)} 个 chunk")
```

### 9.2 全量重建

```bash
# 1. 修改 .env 中 MILVUS_DROP_OLD=true（仅全量重建时）
# 2. 运行构建脚本
python -m rag.build_index
# 3. 改回 MILVUS_DROP_OLD=false
```

### 9.3 图谱更新

新增条目后需更新 [knowledge-graph-adjacency.md](knowledge-graph-adjacency.md)，再重建图：

```python
G = build_graph("kb/20-standards/knowledge-graph-adjacency.md")
```

---

## 10. 常见问题

| 问题 | 原因 | 解决 |
|---|---|---|
| Embedding 模型下载失败 | 网络/证书限制 | 改用云端 API Embedding，或手动下载模型到 `models/` |
| Milvus 连接失败 | 服务未启动/端口错误 | 检查 `MILVUS_HOST/PORT`，确认服务运行 |
| 向量检索结果为空 | 索引未构建 / drop_old 误清 | 运行 `build_index`，确认 `drop_old=false` |
| 图谱 BFS 返回过多 | 跳数过大 | 降低 `GRAPH_HOPS` 至 1~2 |
| 中文检索效果差 | Embedding 模型不支持中文 | 换用中文模型（bge-large-zh 等） |
| 分块过长导致召回低 | CHUNK_SIZE 过大 | 按层调整 `CHUNK_SIZE`，增加 `CHUNK_OVERLAP` |

---

## 11. 变更记录

| 版本 | 日期 | 修改内容 | 修改人 |
|---|---|---|---|
| 1.0 | 2026-09-10 | 创建；含组件选型决策树、环境配置、索引构建（4 模块）、四维检索管道、图谱集成、API 服务、测试验证、维护操作 | KB 管理员 |
