# 电气工程全域知识库

> 注册电气工程师 · 理论 + 计算 + 实践 + 案例 四维知识体系

**🟢 主站点（GitHub Pages，推荐）**：<https://lbl1988.github.io/Electrical-Engineer-Unified-Knowledge/>

**🟢 镜像站点（Render）**：<https://electrical-engineer-unified-knowledge.onrender.com/>

## 📊 知识库规模

| 层          | 条目数                       | 覆盖范围                             |
| ---------- | ------------------------- | -------------------------------- |
| 基础理论（TH）   | 60                        | 电磁/电路/电机/系统/HVDC/FACTS/微电网/AI 基础 |
| 计算方法（CALC） | 22                        | 短路/谐波/接地/照明/蓄电池/柴油机              |
| 工程实践（PR）   | 29                        | 光伏/储能/换电站/数据中心/医院/航空港/碳中和园区      |
| 工程案例（CASE） | 64                        | 2025/2018 真题、校审意见、事故复盘、综合协同      |
| 元数据        | 523 术语 + 208 标准 + 20 中外对照 | 统一编号、术语索引、标准速查                   |
| **合计**     | **175 条核心条目 + 523 术语 + 208 标准 + 20 中外对照** | <br />                           |

## 🏗 技术栈

- **静态站点生成器**：[MkDocs](https://www.mkdocs.org/)

- **主题**：[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)

- **Markdown 扩展**：Pymdownx（数学公式、代码高亮、任务列表等）

- **部署**：GitHub Actions → GitHub Pages（push 自动构建发布）

## 🛠 本地开发

```bash
# 安装依赖
pip install mkdocs mkdocs-material pymdown-extensions

# 本地预览（热重载）
mkdocs serve

# 构建静态站点
mkdocs build --clean
```

## 📁 目录结构

```
kb/
├── docs/              # MkDocs 源码
│   ├── 00-meta/       # 元数据层（术语/编号规则/标准）
│   ├── 10-theory/     # 基础理论层（60 条）
│   ├── 20-standards/  # 标准规范层
│   ├── 30-practice/   # 工程实践层（29 条）
│   ├── 40-calc/       # 计算方法层（22 条）
│   ├── 50-case/       # 工程案例层（60 条）
│   ├── 60-exam/       # 考纲目录
│   └── 90-governance/ # 治理
├── .github/workflows/ # GitHub Actions 自动部署
├── overrides/         # Material 主题自定义（进度条/数字动画）
├── docs/stylesheets/extra.css  # 自定义样式
└── mkdocs.yml         # MkDocs 配置
```

## ✅ 部署

每次 push 到 `main` 分支，GitHub Actions 自动：

1. 安装 Python + MkDocs 依赖
2. 构建静态站点到 `_site/`
3. 发布到 GitHub Pages

查看 Actions 状态：<https://github.com/lbl1988/Electrical-Engineer-Unified-Knowledge/actions>

## 📅 治理文件更新提醒

| 文件            | 更新频率     | 下次更新           |
| ------------- | -------- | -------------- |
| HANDOVER 交接报告 | 每次大批量开发后 | 2027-03（Q1 盘点） |
| 盘点记录          | 季度       | 2026-12（Q4 盘点） |
| 权威数据源清单       | 月度/季度/半年 | 按白名单监控节奏       |

## 📄 许可证

MIT License
