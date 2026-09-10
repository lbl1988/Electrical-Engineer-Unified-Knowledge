***

hide:

- navigation

- toc

***

<div class="kb-hero">
  <h1>电气工程全域知识库</h1>
  <p>覆盖国内与国际标准、基础理论与工程实践的全域电气工程知识库。注册电气工程师备考 · 工程设计 · 校审 · 事故分析一站式参考。</p>
  <div class="kb-stats">
    <div><div class="kb-stat-num">60</div><div class="kb-stat-label">基础理论</div></div>
    <div><div class="kb-stat-num">208</div><div class="kb-stat-label">标准索引</div></div>
    <div><div class="kb-stat-num">29</div><div class="kb-stat-label">工程实践</div></div>
    <div><div class="kb-stat-num">22</div><div class="kb-stat-label">计算方法</div></div>
    <div><div class="kb-stat-num">60</div><div class="kb-stat-label">工程案例</div></div>
    <div><div class="kb-stat-num">504</div><div class="kb-stat-label">术语词条</div></div>
  </div>
</div>

## 五层知识模型

```
L4 应用层（考试·校审·案例）   ← 60-exam/、50-case/
L3 工程实践层（设计·选型·运维）← 30-practice/、40-calc/
L2 标准规范层（GB/DL/NB·IEC/IEEE/NFPA）← 20-standards/
L1 基础理论层（电磁·电路·电机·系统）← 10-theory/
L0 元数据层（术语·编号·模板·规范）← 00-meta/
```

> **规则：上层引用下层，禁止反向依赖；每条工程结论必须挂"标准号-年份＋条款号"。**

## 知识导航

<div class="kb-grid">
  <a class="kb-card" href="00-meta/">
    <div class="kb-card-title">📋 元数据层</div>
    <div class="kb-card-desc">术语表、编号规则、写作规范与三套模板，所有条目的上游约束</div>
    <div class="kb-card-count">7 份文档</div>
  </a>
  <a class="kb-card" href="10-theory/">
    <div class="kb-card-title">⚡ 基础理论</div>
    <div class="kb-card-desc">电磁·电路·电机·电力系统·电力电子·接地·保护，60 篇核心理论</div>
    <div class="kb-card-count">60 篇</div>
  </a>
  <a class="kb-card" href="20-standards/">
    <div class="kb-card-title">📖 标准规范</div>
    <div class="kb-card-desc">国内强制规范、行业标准、国际标准及中外对照表，工程结论溯源依据</div>
    <div class="kb-card-count">9 份索引 + 5 changelog</div>
  </a>
  <a class="kb-card" href="30-practice/">
    <div class="kb-card-title">🔧 工程实践</div>
    <div class="kb-card-desc">供配电设计·接地·电缆·继电保护·电能质量·储能·充电桩等 20 篇</div>
    <div class="kb-card-count">29 篇</div>
  </a>
  <a class="kb-card" href="40-calc/">
    <div class="kb-card-title">🧮 计算方法</div>
    <div class="kb-card-desc">短路电流·负荷计算·保护整定·蓄电池·照度·无功补偿·电缆·接地，全部带手工复算算例</div>
    <div class="kb-card-count">22 篇</div>
  </a>
  <a class="kb-card" href="50-case/">
    <div class="kb-card-title">💼 工程案例</div>
    <div class="kb-card-desc">真题·校审·事故·复合四类案例，覆盖防雷/接地/电缆/变配电所/UPS/谐波/消防等域</div>
    <div class="kb-card-count">54 篇</div>
  </a>
  <a class="kb-card" href="60-exam/">
    <div class="kb-card-title">📝 考纲目录</div>
    <div class="kb-card-desc">2026 供配电 74 本 / 发输变电 67 本规范考纲，含年度 diff 与知识单元映射</div>
    <div class="kb-card-count">2 份</div>
  </a>
  <a class="kb-card" href="90-governance/">
    <div class="kb-card-title">⚙️ 治理</div>
    <div class="kb-card-desc">权威数据源清单、季度盘点记录与交接报告，标准版本信息只认白名单</div>
    <div class="kb-card-count">3 份</div>
  </a>
</div>

## 快速入口

- **查标准** → [cn-01 强制规范与主干标准](20-standards/cn-01-强制性通用规范与主干标准.md) ｜ [cn-02 供配电考纲 74 本](20-standards/cn-02-供配电考纲口径索引.md) ｜ [cn-03 发输变电 67 本](20-standards/cn-03-发输变电考纲口径索引.md) ｜ [intl 国际索引](20-standards/intl-国际标准索引.md)

- **查手册速查** → [手册速查索引](20-standards/handbook-quick-reference-index.md)

- **中外差异** → [mapping 中外对照表（20 张）](20-standards/mapping-中外对照表.md)

- **换版动态** → [changelog/](20-standards/changelog/)

- **查术语** → [00-术语表（504 词条）](00-meta/00-术语表.md)

- **看算例** → [CALC-SC-001 低压三相短路计算](40-calc/CALC-SC-001-低压三相短路电流计算.md)

- **备考** → [2026 供配电考纲](60-exam/2026-供配电考纲初始化.md) ｜ [2026 发输变电考纲](60-exam/2026-发输变电考纲初始化.md)

## 验收统计

| KPI 指标       | 目标      | 实际                              | 状态 |
| ------------ | ------- | ------------------------------- | -- |
| 术语表          | ≥500 词条 | **504**（A\~M 13 域）              | ✅  |
| 标准索引         | 200 本   | 约 208（国内 153 去重＋国际 55）          | ✅  |
| 中外对照表        | 20 张    | **20**（MAP-A\~T）                | ✅  |
| 换版 changelog | 5 份     | **5**（4 国内＋1 国际）                | ✅  |
| 计算方法         | —       | **22**（算例全部手工复算自洽）              | ✅  |
| 理论条目         | —       | **60**（TH-001~060，五段式）         | ✅  |
| 实践条目         | —       | **25**（九段式）                     | ✅  |
| 案例条目         | —       | **54**（真题×11/校审×20/事故×12/复合×11） | ✅  |
| 2026 考纲目录    | 2 份     | **2**（含年度 diff）                 | ✅  |
| 治理文档         | —       | 3（数据源清单＋Q3 盘点＋交接报告）             | ✅  |

## 写作与贡献规则

1. 新条目先读 [01-编号规则](00-meta/01-编号规则.md) 与 [02-写作规范](00-meta/02-写作规范.md)，套用 [实践类九段式](00-meta/03-模板-实践类九段式.md)/[理论类五段式](00-meta/04-模板-理论类五段式.md)/[changelog](00-meta/05-模板-标准changelog.md) 模板；
2. 状态机：`draft → review → published`，发布须双人（注册工程师）复核；
3. 标准版本信息只认 [权威数据源清单](90-governance/权威数据源清单.md) 白名单；
4. Git 提交信息：`{条目ID}: {动作} {说明}`。










