---
id: REF-RAG-GUIDE
title: RAG 检索使用指南（四维检索架构与操作流程）
domain: REF
subdomain: RAG 指南
voltage_levels: [LV, MV, HV, EHV]
lifecycle: [设计, 考试, 运维]
standards:
  - { code: 内部规范, clause: "§8", note: "四维检索：关键词+语义向量+知识图谱+标准溯源" }
status: published
version: 1.0
updated: 2026-09-10
---

# RAG 检索使用指南（四维检索架构与操作流程）

> **用途**：说明知识库四维检索架构的设计、数据流、操作流程与部署指南，配合 [RAG元数据索引](rag-metadata-index.md) 和 [知识图谱邻接表](knowledge-graph-adjacency.md) 使用。
> **代码级接入**：详见 [RAG 框架接入指南](rag-framework-integration-guide.md)（LangChain/LlamaIndex + Chroma/Milvus 完整代码）。

## 1. 四维检索架构

```
用户查询
  │
  ├── 维度 1：关键词检索（全文匹配，快速定位）
  │     ↓
  ├── 维度 2：语义向量检索（Embedding 相似度，概念匹配）
  │     ↓
  ├── 维度 3：知识图谱遍历（邻接表多跳，关联发现）
  │     ↓
  └── 维度 4：标准溯源（规范条款锚定，合规验证）
        ↓
  结果融合排序（Rerank）→ 返回 Top-K 条目
```

| 维度 | 数据源 | 检索方法 | 适用场景 |
|---|---|---|---|
| 关键词 | 全文索引（142 条目） | BM25 / TF-IDF | 精确术语查询（如"星三角启动"） |
| 语义向量 | Embedding 向量库 | 余弦相似度 | 概念查询（如"如何限制启动电流"） |
| 知识图谱 | 邻接表（~400 边） | BFS/DFS 多跳 | 关联发现（如"短路计算涉及哪些条目"） |
| 标准溯源 | 标准条款索引 | 条款号映射 | 合规验证（如"GB 50054 对 PE 的要求"） |

## 2. 数据流与文件依赖

### 2.1 核心文件

| 文件 | 作用 | 更新频率 |
|---|---|---|
| [rag-metadata-index.md](rag-metadata-index.md) | 条目元数据（ID/标题/关键词/主题/摘要） | 新条目时 |
| [knowledge-graph-adjacency.md](knowledge-graph-adjacency.md) | 条目间关系邻接表 | 新条目时 |
| [handbook-quick-reference-index.md](handbook-quick-reference-index.md) | 手册公式/典型值速查 | 手册换版时 |
| 10-theory/TH-*.md | 理论条目原文（向量化源文本） | 批次开发时 |
| 30-practice/PR-*.md | 实践条目原文 | 批次开发时 |
| 40-calc/CALC-*.md | 计算方法原文 | 批次开发时 |

### 2.2 向量化管道

```
源文件（Markdown）
  → YAML front matter 提取（ID/标题/关键词/标准）
  → 正文分块（TH: 五段式, PR: 九段式, CALC: 步骤式）
  → 文本清洗（去标记/去表格/保留公式）
  → Embedding 模型 → 向量库
  → 元数据索引 → 倒排索引（关键词）
  → 邻接表 → 图数据库
```

## 3. 操作流程

### 3.1 查询流程

**步骤 1：关键词检索**
- 输入查询关键词
- BM25 全文匹配，返回 Top-20 候选

**步骤 2：语义向量检索**
- 查询文本 → Embedding → 余弦相似度
- 返回 Top-20 候选

**步骤 3：图谱扩展**
- 从 Top-K 候选中提取节点 ID
- BFS 扩展 1~2 跳邻居（上游理论 + 下游算例）
- 返回关联条目

**步骤 4：标准溯源**
- 提取查询中的标准号（如 GB 50054）
- 映射到 STD-CN-002/003 条款
- 返回标准原文要点

**步骤 5：融合排序**
- 合并四维结果
- Rerank（去重 + 多样性 + 相关性加权）
- 返回 Top-5 最终结果

### 3.2 示例查询

**查询 1**："10kV 馈线保护怎么整定？"

| 维度 | 检索结果 |
|---|---|
| 关键词 | PR-PE-002 整定配合深化（"10kV" + "整定"） |
| 语义 | PR-PE-001 继电保护配置（"保护配置"语义匹配） |
| 图谱 | PR-PE-002 → CALC-PT-001 保护整定 → TH-012 继保四性 → TH-003 对称分量 |
| 溯源 | GB/T 14285-2006（保护配置原则）；DL/T 553-2013（整定导则） |
| **融合** | **PR-PE-002（主）+ CALC-PT-001（算例）+ TH-012（理论）+ GB/T 14285（标准）** |

**查询 2**："UPS 电池后备时间不够怎么办？"

| 维度 | 检索结果 |
|---|---|
| 关键词 | PR-PS-003 UPS配置（"UPS" + "后备时间"） |
| 语义 | CALC-BT-002 UPS后备时间（"后备时间"语义匹配） |
| 图谱 | PR-PS-003 → CALC-BT-002 → CALC-BT-001 蓄电池容量 → TH-024 电力电子 |
| 溯源 | GB/T 7260-2023（UPS技术条件）；GB/T 42084-2022（数据中心UPS） |
| **融合** | **PR-PS-003（主）+ CALC-BT-002（计算）+ CALC-BT-001（电池）+ GB/T 7260（标准）** |

## 4. 部署指南

### 4.1 轻量部署（纯 Markdown + 脚本）

```yaml
向量模型: bge-large-zh-v1.5（本地部署，1024维）
向量库: ChromaDB / FAISS
全文索引: Tantivy / MeiliSearch（Rust）
图谱: NetworkX（Python，内存图）
框架: LangChain / LlamaIndex
```

### 4.2 生产部署（全栈）

```yaml
向量模型: text-embedding-3-large（API，1536维）
向量库: Milvus / Qdrant（分布式）
全文索引: Elasticsearch
图谱: Neo4j（图数据库）
框架: LangChain + LangGraph
LLM: GPT-4 / Claude / GLM
```

### 4.3 索引构建脚本（伪代码）

```python
# 1. 加载元数据索引
metadata = load_markdown("rag-metadata-index.md")
entries = parse_entries(metadata)  # 142 条目

# 2. 分块与向量化
for entry in entries:
    chunks = split_content(entry.file_path, strategy=entry.layer)
    vectors = embedding_model.encode(chunks)
    vector_db.insert(vectors, metadata=entry)

# 3. 构建知识图谱
graph = load_adjacency("knowledge-graph-adjacency.md")
neo4j.import(graph)

# 4. 构建全文索引
for entry in entries:
    es.index(entry.full_text, metadata=entry)

# 5. 构建标准溯源索引
for std in standards:
    es.index(std.clauses, metadata=std)
```

## 5. 索引维护规则

| 触发事件 | 动作 | 更新文件 |
|---|---|---|
| 新增 TH/PR/CALC 条目 | 更新元数据索引 + 邻接表 | rag-metadata-index.md, knowledge-graph-adjacency.md |
| 标准换版 | 更新标准溯源映射 | STD-CN-002/003, changelog |
| 手册新版 | 更新手册速查索引 | handbook-quick-reference-index.md |
| 季度盘点 | 全量重建向量索引 | 向量库 + 图谱 |

## 6. 性能指标

| 指标 | 目标值 | 说明 |
|---|---|---|
| 检索延迟 | <500ms | 关键词+向量+图谱融合 |
| Top-5 召回率 | >90% | 对标准考题查询 |
| 图谱多跳延迟 | <100ms | BFS 2 跳 |
| 索引构建时间 | <5min | 142 条目全量 |

## 7. 变更记录

| 版本 | 日期 | 修改内容 | 修改人 |
|---|---|---|---|
| 1.0 | 2026-09-10 | 创建；含四维检索架构、数据流、操作流程、2 示例查询、部署指南、维护规则 | KB 管理员 |
