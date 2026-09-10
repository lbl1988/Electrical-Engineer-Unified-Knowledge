# 电气工程全域知识库

> 注册电气工程师 · 理论 + 计算 + 实践 + 案例 四维知识体系

**🟢 主站点（GitHub Pages，推荐）**：<https://lbl1988.github.io/Electrical-Engineer-Unified-Knowledge/>

**🟢 镜像站点（Render）**：<https://electrical-engineer-unified-knowledge.onrender.com/>

---

## 📊 知识库规模

| 层 | 条目数 | 覆盖范围 |
|---|---|---|
| 基础理论（TH） | 60 | 电磁/电路/电机/系统/HVDC/FACTS/微电网/AI/VSG/黑启动 |
| 计算方法（CALC） | 22 | 短路/谐波/接地/照明/蓄电池/柴油机/IEC 60909/弧光过电压 |
| 工程实践（PR） | 29 | 光伏/储能/换电站/数据中心/医院/航空港/碳中和园区/EMS/电力市场 |
| 工程案例（CASE） | 64 | 2025/2018 真题、校审意见、事故复盘、综合协同、行业事故 |
| 元数据 | 523 术语 + 208 标准 + 20 中外对照 | 统一编号、术语索引、标准速查 |
| 引用图谱 | 6 张（128 节点） | 核心闭环/新能源储能/数据中心/设备选型/系统稳定/医院IT |
| **合计** | **175 条核心条目 + 523 术语 + 208 标准 + 20 中外对照** | |

**全库统计**：218 个 Markdown 文件 · 31,275 行 · 84 次 Git 提交

---

## 🏗 技术栈

- **静态站点生成器**：[MkDocs](https://www.mkdocs.org/) + [Material 主题](https://squidfunk.github.io/mkdocs-material/)
- **Markdown 扩展**：Pymdownx（数学公式、代码高亮、任务列表、可折叠块）
- **图谱**：Mermaid.js（6 张四层引用闭环图）
- **部署**：GitHub Actions → GitHub Pages（push 自动构建发布）
- **镜像**：Render Static Site
- **CDN**：系统字体栈 + BootCDN（国内访问优化）

---

## 📁 目录结构

```
kb/
├── docs/                    # 218 个 Markdown 文件
│   ├── 00-meta/             # 元数据层（术语表/编号规则/引用图谱 6 张）
│   ├── 10-theory/           # 理论层（TH-001~060，60 条）
│   ├── 20-standards/        # 标准规范层（208 本 + 换版记录）
│   ├── 30-practice/         # 实践层（PR-001~029，29 条）
│   ├── 40-calc/             # 计算层（CALC-001~022，22 条）
│   ├── 50-case/             # 案例层（CASE-001~064，64 条）
│   ├── 60-exam/             # 考纲目录（供配电 74 本 + 发输变电 67 本）
│   └── 90-governance/       # 治理（数据源/盘点/交接/建设总结报告）
├── scripts/export_data.py   # 数据导出脚本（CSV/JSON/Markdown）
├── .github/workflows/       # GitHub Actions 自动部署
├── overrides/               # 主题自定义（阅读进度条/数字动画）
├── docs/stylesheets/extra.css  # 自定义样式（20+ 组件）
└── mkdocs.yml               # MkDocs 配置
```

---

## 🛠 本地开发

```bash
# 安装依赖
pip install mkdocs-material

# 本地预览（热重载）
mkdocs serve

# 构建静态站点
mkdocs build --clean

# 导出数据索引
python scripts/export_data.py --format all
```

---

## ✅ 部署

每次 push 到 `main` 分支，GitHub Actions 自动：

1. 安装 Python + MkDocs Material
2. 构建静态站点到 `_site/`
3. 发布到 GitHub Pages

查看 Actions 状态：<https://github.com/lbl1988/Electrical-Engineer-Unified-Knowledge/actions>

---

## 📑 引用图谱（6 张）

| # | 图谱 | 节点 | 核心主题 |
|---|---|---|---|
| 01 | 核心闭环 | 17 | 四层引用基线（对称分量→短路→断路器→真题） |
| 02 | 新能源 + 储能 | 15 | 微电网/VSG/电池热失控/光伏火灾 |
| 03 | 数据中心 + 工业配电 | 12 | 雷电/柴发/UPS/ATS 切换事故 |
| 04 | 变配电一次设备选型链 | 30 | 断路器/GIS/CT/避雷器/电缆选型闭环 |
| 05 | 电力系统稳定链 | 28 | 功角/频率/AVR-PSS/黑启动四层防线 |
| 06 | 医院 IT 系统链 | 26 | 人体安全/IT 系统/SPD/UPS |

---

## 🔍 质量保证

| 检查项 | 结果 |
|---|---|
| `mkdocs build` WARNING | 0 |
| ID 重复 | 0 |
| front matter 格式错误 | 0 |
| 术语锚点缺失 | 0 |
| 断链（文件不存在） | 0 |
| 统计口径一致性 | ✅ 全部对齐 |

---

## 📅 治理文件更新提醒

| 文件 | 更新频率 | 下次更新 |
|---|---|---|
| HANDOVER 交接报告 | 半年 | 2027-03（Q1 盘点） |
| 盘点记录 | 季度 | 2026-12（Q4 盘点） |
| 权威数据源清单 | 月度/季度/半年 | 按白名单监控节奏 |
| 建设总结报告 | 一次性 | — |

---

## 📄 许可证

MIT License
