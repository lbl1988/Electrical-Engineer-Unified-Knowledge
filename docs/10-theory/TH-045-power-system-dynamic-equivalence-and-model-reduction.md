***

id: TH-045
title: 电力系统动态等值与降阶方法（电网等值/机组聚合/模态降阶/时变等值）
domain: 基础理论
subdomain: 电力系统分析
voltage\_levels: \[HV, EHV, UHV]
lifecycle: \[规划, 设计, 运维]
standards:

- { code: GB 38755-2019, clause: "§6 稳定计算", note: "电力系统安全稳定导则：等值系统稳定计算要求" }

- { code: GB/T 19963.1-2021, clause: "§4 建模原则", note: "电力系统网源协调技术规范 第1部分：等值与聚合原则" }

- { code: GB/T 40425-2021, clause: "全文", note: "电力系统安全稳定控制技术导则（含动态等值应用）" }
  status: draft
  reviewers: \[]
  version: 0.1
  updated: 2026-09-10

***

# 电力系统动态等值与降阶方法

## 1. 定义

电力系统动态等值与降阶是将**大规模电力系统模型**（数千节点、数百台机组）简化为**小规模等值模型**的数学方法，使稳定计算、实时仿真和控制器设计在计算上可行。

| 方法类别                               | 核心思想                                  | 时间尺度    | 适用场景        |
| ---------------------------------- | ------------------------------------- | ------- | ----------- |
| **动态等值（Dynamic Equivalence）**      | 保留研究区（Study Area）详细模型，外部系统聚合成等值发电机/负荷 | 秒级\~亚秒级 | 稳定计算、故障分析   |
| **机组聚合（Generator Aggregation）**    | 将同调机组（Coherent Generators）合并为一台等值机组   | 秒级\~亚秒级 | 区域等值、新能源聚合  |
| **模态降阶（Model Reduction）**          | 消除快模态（高频特征值），保留主导慢模态                  | 全频段→低频段 | 控制器设计、小干扰稳定 |
| **时变等值（Time-Varying Equivalence）** | 根据运行方式动态更新等值参数                        | 秒级实时    | 在线稳定监测、应急控制 |

**关键原则**：等值系统在\*\*关注模态（Interested Modes）\*\*上的动态响应必须与详细系统一致，非关注模态允许被消除。

## 2. 物理图像

电力系统动态等值的物理图像：

```
        详细系统（N 节点、M 机组）
           │
    ┌──────┴──────┐
    │  关注区       │  外部区（Aggregate）
    │  (Study Area) │  (External System)
    └──────┬──────┘
           │
    动态等值（保留关注区，外部聚合成 G_eq + Z_eq）
           │
    等值系统（n ≪ N 节点、m ≪ M 机组）
           │
    ┌──────┴──────┐
    │  模态降阶      │  机组聚合
    │  (消除快模态)   │  (同调机组合并)
    └──────┬──────┘
           │
    极简模型（适合控制器设计/实时仿真）
```

**时间尺度解耦**：电力系统动态过程覆盖多时间尺度——电磁暂态（μs~~ms）、机电暂态（ms~~s）、中长期稳定（s~~min）、调度级（min~~h）。等值/降阶的本质是**在选定的时间尺度上消除更快或更慢的动态过程**。

## 3. 推导

### 3.1 动态等值的基本方程

详细系统的状态空间模型：

$$\dot{\mathbf{x}} = \mathbf{A}\mathbf{x} + \mathbf{B}\mathbf{u}$$

$$\mathbf{y} = \mathbf{C}\mathbf{x} + \mathbf{D}\mathbf{u}$$

其中 $\mathbf{x} \in \mathbb{R}^{n}$ 是状态向量（典型 $n=10^3\sim10^5$）。

等值的目标是找到降阶变换 $\mathbf{T}$：

$$\mathbf{x} = \mathbf{T}\tilde{\mathbf{x}} + \mathbf{x}\_0$$

使得降阶系统：

$$\dot{\tilde{\mathbf{x}}} = \tilde{\mathbf{A}}\tilde{\mathbf{x}} + \tilde{\mathbf{B}}\mathbf{u}$$

在关注模态上的响应与原系统一致。

### 3.2 模态降阶：平衡截断法（Balanced Truncation）

这是工程上最常用的模态降阶方法：

**步骤 1**：求解 Lyapunov 方程得到可控 Gramian $\mathbf{P}$ 和可观 Gramian $\mathbf{Q}$：

$$\mathbf{A}\mathbf{P} + \mathbf{P}\mathbf{A}^{\mathrm{T}} + \mathbf{B}\mathbf{B}^{\mathrm{T}} = \mathbf{0}$$

$$\mathbf{A}^{\mathrm{T}}\mathbf{Q} + \mathbf{Q}\mathbf{A} + \mathbf{C}^{\mathrm{T}}\mathbf{C} = \mathbf{0}$$

**步骤 2**：对 $\mathbf{P}\mathbf{Q}$ 做特征值分解，得到 Hankel 奇异值 $\sigma\_1 \geq \sigma\_2 \geq \cdots \geq \sigma\_n$。

**步骤 3**：保留前 $r$ 个大奇异值对应的模态，消除后 $n-r$ 个快模态（小奇异值）。

**降阶误差界**：

$$|\mathbf{H}(s) - \tilde{\mathbf{H}}(s)|_\infty \leq 2\sum_{i=r+1}^n \sigma\_i$$

即截断误差的 $H\_\infty$ 范数不超过被截奇异值之和的两倍——这是选择 $r$ 的理论依据。

### 3.3 机组聚合：同调等值法（COI-Based）

同调机组的定义：在外扰下**转子角轨迹相似**的机组可以合并。

常用判据：转子角 COI（Center of Inertia）偏差 $|\delta\_i - \delta\_{\mathrm{COI}}| < \epsilon$。

等值参数计算（合并 $k$ 台同调机组为一台）：

| 参数   | 等值公式                                                              |
| ---- | ----------------------------------------------------------------- |
| 惯量   | $H\_{\mathrm{eq}} = \sum\_{i=1}^k H\_i S\_i / \sum\_{i=1}^k S\_i$ |
| 同步电抗 | $X\_d'_{\mathrm{eq}} = 1 / \sum_{i=1}^k (1/X\_d'\_i)$             |
| 励磁参数 | $K\_{\mathrm{eq}} = \sum\_{i=1}^k K\_i / k$                       |

### 3.4 外部系统等值：发电机聚合 + 负荷等值

外部系统的常规等值（WECC 标准）：

```
外部系统（详细模型）
    │
    ├── 发电机：聚合成 G_eq（电压源 Z_s + R+jX）
    │
    └── 负荷：聚合成 ZIP 负荷等值
          S = P_0 (a + b·f + c·f²)
          其中 f = V/V_n 或 f = f_grid/f_n
```

ZIP 负荷模型（恒定功率 + 恒定电流 + 恒定阻抗）：

$$P = P\_0 \left(a\_P \cdot \left(\frac{V}{V\_n}\right)^0 + b\_P \cdot \left(\frac{V}{V\_n}\right)^1 + c\_P \cdot \left(\frac{V}{V\_n}\right)^2\right)$$

$$Q = Q\_0 \left(a\_Q \cdot \left(\frac{V}{V\_n}\right)^0 + b\_Q \cdot \left(\frac{V}{V\_n}\right)^1 + c\_Q \cdot \left(\frac{V}{V\_n}\right)^2\right)$$

约束：$a\_P + b\_P + c\_P = 1$，$a\_Q + b\_Q + c\_Q = 1$。

## 4. 与工程实践的联系

### 4.1 应用场景

| 应用         | 等值方法        | 规模压缩比 | 依赖条目                                 |
| ---------- | ----------- | ----- | ------------------------------------ |
| 电力系统稳定计算   | 动态等值 + 机组聚合 | 100:1 | PR-PE-002（继保整定深化）、PR-DD-002（变配电选型）   |
| 新能源并网稳定分析  | 模态降阶        | 50:1  | PR-ES-002（DG 接入设计）、TH-038（频率稳定）      |
| HVDC 控制器设计 | 平衡截断法       | 20:1  | TH-027（LCC/VSC-HVDC）、TH-040（交直流混联）   |
| 在线稳定监测     | 时变等值        | 实时更新  | TH-043（AI 基础）、PR-DD-004（配网自动化 SCADA） |

### 4.2 失效边界

| 边界条件            | 后果                         | 工程速记                        |
| --------------- | -------------------------- | --------------------------- |
| 机组非同调却强制聚合      | 等值系统丢失摆动模态，稳定裕度计算偏差可超过 30% | 同调判据 $\epsilon$ 取 5\~10°    |
| 降阶阶数 $r$ 选太小    | 关键模态被消除，控制器在实际系统上性能恶化甚至失稳  | 保留 Hankel 奇异值衰减曲线的第一个"拐点"之前 |
| 外部系统动态特性变化（如故障） | 静态等值（ZIP）失效，需切换到动态等值       | 故障前用静态，故障中用动态               |
| 电力电子设备未被等值      | 快速动态引发的次同步振荡在等值系统中不可见      | 电力电子支路必须作为研究区保留             |

### 4.3 工程速记

> **选等值方法的口诀**：稳定计算→动态等值，控制器设计→模态降阶，实时监测→时变等值。同调判据用 COI 偏差 5\~10°，降阶阶数看奇异值拐点。

## 5. 关联与变更

| 关联                                                                         | 说明                             |
| -------------------------------------------------------------------------- | ------------------------------ |
| [TH-015](TH-015-synchronous-machine-park-equations.md)                     | Park 方程是机组等值的基础                |
| [TH-016](TH-016-synchronous-machine-power-angle-stability.md)              | 功角稳定分析依赖同调机组识别                 |
| [TH-038](TH-038-high-renewable-frequency-stability-inertia.md)             | 惯量聚合需考虑虚拟惯量的等值                 |
| [TH-040](TH-040-hybrid-ac-dc-grid-stability.md)                            | 交直流混联系统等值需考虑换相失败模态             |
| [PR-DD-004](../30-practice/PR-DD-004-distribution-automation-and-scada.md) | 配网 SCADA 的状态估计本质是在线等值          |
| [CALC-SC-002](../40-calc/CALC-SC-002-hv-short-circuit-iec60909.md)         | 高压短路计算中的系统等值 $S\_k''$ 即动态等值的特例 |

**变更记录**：

- 2026-09-10：首版草稿，覆盖动态等值/机组聚合/模态降阶/时变等值四个方向

