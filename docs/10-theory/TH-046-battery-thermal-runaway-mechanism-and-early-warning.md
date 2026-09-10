---
id: TH-046
title: 锂离子电池热失控机理与预警（SEI膜分解/正负极反应/产气/热扩散）
domain: 基础理论
subdomain: 储能安全
voltage_levels: [LV, HV]
lifecycle: [设计, 验收, 运维]
standards:
  - { code: GB/T 44240-2024, clause: "第7章 热失控防护", note: "电化学储能系统安全规范：热失控监测与抑制" }
  - { code: GB/T 42288-2022, clause: "§5 热安全", note: "电化学储能系统环境技术条件：热安全要求" }
  - { code: GB 38755-2019, clause: "§5 新能源并网安全", note: "电力系统安全稳定导则：含储能热失控引发的系统风险" }
  - { code: IEC 62660-3:2020, clause: "全文", note: "Secondary batteries for road vehicles - Safety requirements（含热滥用测试）" }
  - { code: NFPA 855-2023, clause: "全文", note: "Standard for the Installation of Stationary Energy Storage Systems" }
status: draft
reviewers: []
version: 0.1
updated: 2026-09-10
---

# 锂离子电池热失控机理与预警

## 1. 定义

热失控（Thermal Runaway, TR）是锂离子电池在**过充、过放、外部短路、内部短路、机械损伤或极端温度**条件下，内部放热反应自加速、温度急剧攀升（通常在数十秒内从 ~250°C 升至 800~1200°C），并伴随**大量可燃气体释放（CO、H₂、烃类）、电解液燃烧甚至爆炸**的过程。

热失控是储能电站、电动汽车和便携式电子设备的首要安全威胁。在电力系统语境下，热失控不仅是消防问题——单体→模组→簇级的蔓延可能引发**直流系统短路、直流母线电压骤降、PCS 保护动作**，进而影响电网稳定（见 TH-040 交直流混联）。

| 阶段 | 温度区间 | 特征反应 | 危害 |
|---|---|---|---|
| **SEI 膜分解** | 90~120°C | 负极表面 SEI（固体电解质界面）膜受热分解，重新暴露的锂与电解液反应 | 起始放热，若散热充分可自愈 |
| **电解质分解** | 150~200°C | 电解液（碳酸酯类）开始分解，释放 CO、H₂、C₂H₄ | 产气导致内部压力上升 |
| **正极热解 / 隔膜熔化** | 200~250°C | NCM/NCA 正极释放 O₂，PP/PE 隔膜熔化，正负极直接接触 → **大规模内部短路** | 放热速率指数增长（kW/kg 级） |
| **热失控喷发** | 250°C+ | 温度骤升，电解液蒸气→液态金属锂（~180°C 熔化）燃点 ~1340°C 但在纳米颗粒状态 300°C 即可自燃 | 喷溅、爆炸、火灾 |

## 2. 物理图像

锂离子电池热失控的链式反应与产热/产气过程：

```
触发事件（过充/短路/撞击/热滥用）
    │
    ▼
内部温度 T ↑
    │
    ├── SEI 膜分解（90~120°C）
    │       Q ≈ 100~300 J/g 电解液
    │       产 H₂、CO
    │
    ├── 电解质分解（150~200°C）
    │       Q ≈ 200~500 J/g 电解液
    │       产 CO、H₂、C₂H₄
    │
    ├── 正极热解放 O₂（200~230°C，NCM）
    │       Q ≈ 300~800 J/g 正极
    │       产 O₂ → 助燃
    │
    ├── 隔膜熔化 + 内部短路（200~250°C）
    │       Q = I²R · Δt（短路电流可达 C/5~C/2 倍率）
    │       产热功率骤升至 kW/kg 级
    │
    ▼
热失控（T 指数上升，数十秒内超 800°C）
    │
    ├── 电芯膨胀 → 模组挤压 → 相邻电芯机械损伤 → 次级短路
    │
    ├── 可燃气体排放 → 电池舱内爆炸极限（LEL 1~4%）→ 爆燃
    │
    ▼
簇级热蔓延 → 储能舱火灾 → 直流系统短路 → 电网冲击
```

**关键物理量**：

| 量 | 典型值 | 工程意义 |
|---|---|---|
| 起始放热温度 $T_{\mathrm{onset}}$ | 90~130°C | BMS 预警阈值设 $T_{\mathrm{onset}} - 15$°C |
| 峰值温度 $T_{\mathrm{peak}}$ | 800~1200°C | 热设计的温度上限 |
| 自加速指数 $\beta$ | 0.15~0.25 /K | $dQ/dT = \beta \cdot Q$，决定蔓延速度 |
| 产气量 | 200~500 L/Ah | 电池舱通风/防爆设计依据 |
| 放热功率密度 | 10~50 kW/kg（热失控瞬间） | 热管理系统极端工况设计 |

## 3. 推导

### 3.1 热失控判据

热失控的数学定义：**自放热速率 $q_{\mathrm{self}}$ 超过散热能力 $q_{\mathrm{cool}}$，且温度持续上升**。

$$q_{\mathrm{self}} > q_{\mathrm{cool}} \implies \frac{dT}{dt} > 0 \implies \text{热失控}$$

Arrhenius 型放热速率模型（一级近似）：

$$q_{\mathrm{self}}(T) = Q_{\mathrm{init}} \exp\left(\frac{E_a}{R}\left(\frac{1}{T_{\mathrm{onset}}} - \frac{1}{T}\right)\right)$$

其中：
- $Q_{\mathrm{init}}$ = 起始放热功率（mW~W 级/kg）
- $E_a$ = 活化能（SEI 膜分解约 50~80 kJ/mol，电解质分解约 100~150 kJ/mol）
- $R$ = 气体常数 8.314 J/(mol·K)

散热能力（牛顿冷却）：

$$q_{\mathrm{cool}}(T) = h A (T - T_{\mathrm{amb}})$$

热失控发生在平衡点 $(T_{\mathrm{crit}}, q_{\mathrm{crit}})$ 处的不稳定分支：

$$\frac{dq_{\mathrm{self}}}{dT}\bigg|_{T=T_{\mathrm{crit}}} > \frac{dq_{\mathrm{cool}}}{dT}\bigg|_{T=T_{\mathrm{crit}}}$$

### 3.2 热蔓延模型

从单体到模组的热蔓延时间：

$$\Delta t_{\mathrm{spread}} \approx \frac{C_{\mathrm{p}} m \Delta T}{q_{\mathrm{trans}}}$$

其中 $q_{\mathrm{trans}} \approx k A_{\mathrm{contact}} (T_{\mathrm{peak}} - T_{\mathrm{amb}})$ 是相邻电芯间的传导热流。

**关键防护**：热蔓延阻隔层（气凝胶、云母板）可将 $\Delta t_{\mathrm{spread}}$ 从数秒延长至数十秒，为消防争取时间。

### 3.3 预警判据

实用 BMS 热失控预警采用**多判据融合**，避免单点误报：

| 判据 | 阈值 | 优先级 |
|---|---|---|
| 温度 $T > T_{\mathrm{onset}} - 15$°C | 通常 75~95°C | 低 |
| 温度上升速率 $dT/dt > 1$°C/min | 正常 ≤ 0.2°C/min | 中 |
| 电压骤降 $\Delta U > 50$ mV / 5s | 内部短路特征 | 高 |
| 气体浓度（H₂、CO）超 LEL 的 10% | 产气预警 | 高 |
| 声纹识别（机械破裂声） | 40~200 kHz 特征频带 | 高 |

## 4. 与工程实践的联系

### 4.1 应用场景

| 应用 | 依赖条目 |
|---|---|
| 储能电站热管理设计 | PR-ES-001（电化学储能接入）、CALC-LT-001（照度/热计算思路） |
| BMS 预警阈值设置 | TH-038（频率稳定，储能 VSG 中断影响）、PR-CM-001（消防联动） |
| 电池舱防爆通风设计 | PR-CM-001（消防联动） |
| 电池故障诊断与预测 | TH-043（AI 基础，PINN/强化学习用于 SOH 和热失控预测） |

### 4.2 失效边界

| 边界条件 | 后果 | 工程速记 |
|---|---|---|
| 热管理失效（冷却液断流） | 单体温度均匀，热失控后蔓延更快（无局部冷点阻隔） | 冷却液流量低于额定 50% 即触发降额运行 |
| SOC > 90% 时发生内部短路 | 放热功率是 50% SOC 的 2~3 倍（锂含量高） | 紧急工况下先降 SOC 再降功率 |
| 热失控后未能阻止产气 | 舱内气体浓度达 LEL（1~4%）遇电火花即燃爆 | 强制通风 + 惰性气体覆盖 |

### 4.3 工程速记

> **热失控三要素**：温度超 90°C + 升温加速 + 电压骤降。BMS 只要抓到两个，立即切断高压回路并报警。

## 5. 关联与变更

| 关联 | 说明 |
|---|---|
| [TH-038](TH-038-high-renewable-frequency-stability-inertia.md) | 储能热失控导致的 PCS 脱网直接影响系统惯量 |
| [TH-041](TH-041-distribution-grid-high-penetration-dg-hosting-capacity.md) | 储能脱网加剧 DG 承载力不足 |
| [TH-043](TH-043-ai-foundations-in-electrical-engineering.md) | AI 可用于热失控预测（剩余寿命估计） |
| [PR-ES-001](../30-practice/PR-ES-001-energy-storage-integration.md) | 储能接入设计必须包含热管理方案 |
| [PR-CM-001](../30-practice/PR-CM-001-fire-protection-interlocking.md) | 消防联动方案的上游理论基础 |

**变更记录**：
- 2026-09-10：首版草稿
