---
id: TH-058
title: 电力系统频率响应精细化建模（一次调频/二次调频/AGC 协调）
domain: 基础理论
subdomain: 电力系统稳定
voltage_levels: [HV, EHV, UHV]
lifecycle: [运维]
standards:
  - { code: GB 38755-2019, clause: "§6 稳定计算与频率响应", note: "电力系统安全稳定导则：频率响应建模与校核" }
  - { code: GB/T 19963.1-2021, clause: "§4 频率响应", note: "电力系统网源协调技术规范 第1部分：一次调频和虚拟惯量技术要求" }
  - { code: GB/T 40595-2021, clause: "全文", note: "并网电源一次调频试验技术规定" }
  - { code: DL/T 1055-2022, clause: "全文", note: "电力系统二次调频技术规范" }
status: draft
reviewers: []
version: 0.1
updated: 2026-09-10
---

# 电力系统频率响应精细化建模

## 1. 定义

电力系统频率响应（Frequency Response）是指系统在**有功功率不平衡**（如发电机跳闸、负荷突变、新能源出力突降）时的**频率动态过程**。精细化建模的目标是：准确模拟从**毫秒级 RoCoF** 到**分钟级 AGC 恢复**的完整频率动态链，为频率稳定校核和一次调频/虚拟惯量配置提供量化依据。

| 响应层级 | 时间尺度 | 响应源 | 模型 |
|---|---|---|---|
| **惯性响应** | 0~2 s | 同步发电机转子惯量 + 虚拟惯量 | $H_{\mathrm{eq}} \cdot df/dt = -\Delta P$ |
| **一次调频** | 2~30 s | 同步机调速器 + 新能源频率环 | 下垂控制 $f = f_0 - R \cdot \Delta P$ |
| **二次调频** | 30 s ~ 5 min | AGC + 电力电子快速调节 | PI 控制 $\Delta P_{\mathrm{AGC}} = K_P f + K_I \int f$ |

**关键指标**：

| 指标 | 定义 | 阈值 |
|---|---|---|
| RoCoF（频率变化率） | $df/dt \approx -\Delta P/(2H_{\mathrm{eq}} S_{\mathrm{base}})$ | ≤ 0.1 Hz/s |
| 频率最低点 $f_{\min}$ | 故障后频率跌落极值 | ≥ 49.5 Hz（50 Hz 系统） |
| 一次调频响应时间 | 调速器输出有效补偿的时间 | ≤ 3 s |
| 稳态频率偏差 | 一次调频完成后的频率偏差 | ≤ 0.05 Hz |
| AGC 恢复时间 | 频率回到 49.9~50.1 Hz 的时间 | ≤ 5 min |

## 2. 物理图像

频率响应的完整时间动态链：

```
t=0      │ 功率不平衡发生（ΔP = -10% S_base，如 1 GW 机组跳闸）
         │
         │  阶段 1：惯性响应（0~2 s）
         │  ├── RoCoF 峰值：df/dt|_peak = -ΔP/(2H_eq S_base)
         │  │   传统系统 H_eq ≈ 4~6 s → RoCoF ≈ -0.08 ~ -0.12 Hz/s
         │  │   高比例新能源 H_eq ≈ 1~2 s → RoCoF ≈ -0.25 ~ -0.5 Hz/s（超限！）
         │  ├── 同步机惯性 + 虚拟惯量同时作用
         │  └── 频率跌落至 ~49.7 Hz（惯性响应贡献）
         │
         │  阶段 2：一次调频（2~30 s）
         │  ├── 调速器/频率环激活
         │  ├── 下垂控制：P_primary = P_ref - (f - f_n)/R
         │  │   R = 5%（典型）→ Δf = -0.1 Hz → ΔP = 0.02 pu
         │  ├── 频率继续缓慢跌落至最低点 f_min
         │  │   f_min 取决于一次调频响应速率
         │  └── 频率开始回升
         │
         │  阶段 3：二次调频（30 s ~ 5 min）
         │  ├── AGC 激活，PI 控制
         │  ├── ΔP_AGC = K_P (f - f_n) + K_I ∫(f - f_n) dt
         │  └── 频率逐步恢复至 49.9~50.1 Hz
         │
t=5 min  │ 频率恢复完成，进入稳态
```

## 3. 推导

### 3.1 完整频率响应模型

功率不平衡后的频率动态满足（经典模型）：

$$2H_{\mathrm{eq}} S_{\mathrm{base}} \frac{df}{dt} = -\Delta P_{\mathrm{imbalance}} + \Delta P_{\mathrm{primary}} + \Delta P_{\mathrm{secondary}} + \Delta P_{\mathrm{load}}$$

各项贡献：

| 项 | 表达式 | 来源 |
|---|---|---|
| $\Delta P_{\mathrm{imbalance}}$ | $P_{\mathrm{gen}} - P_{\mathrm{load}}$（负值表示发电不足） | 故障触发 |
| $\Delta P_{\mathrm{primary}}$ | $\sum_i (f_0 - f)/R_i$ | 一次调频下垂控制 |
| $\Delta P_{\mathrm{secondary}}$ | $K_P (f_0 - f) + K_I \int_0^t (f_0 - f) dt$ | AGC 二次调频 |
| $\Delta P_{\mathrm{load}}$ | $D_{\mathrm{load}} \cdot (f - f_0)$ | 负荷频率效应（负荷随频率略增略减） |

### 3.2 高比例新能源下的 RoCoF 计算

**关键点**：传统同步机的惯量是物理固有的（转子质量），跟网型新能源的惯量**为零**（除非配置虚拟惯量）。

$$H_{\mathrm{eq}} = \frac{H_{\mathrm{sync}} S_{\mathrm{sync}} + \sum H_{v,i} S_{\mathrm{DG},i}}{S_{\mathrm{total}}}$$

其中：
- $H_{\mathrm{sync}}$ = 同步机平均惯量常数（典型 3~5 s）
- $H_{v,i}$ = 第 $i$ 个 DG 的虚拟惯量（0~2 s）
- $S_{\mathrm{sync}}, S_{\mathrm{DG},i}$ = 同步机和 DG 的额定容量

**RoCoF 预测**：

$$\left|\frac{df}{dt}\right|_{\mathrm{peak}} = \frac{\Delta P_{\mathrm{imbalance}}}{2 H_{\mathrm{eq}} S_{\mathrm{total}}}$$

**算例**：$S_{\mathrm{total}} = 10$ GW，新能源占比 70%，同步机 $H=4$ s，DG 有 50% 配 $H_v=1$ s：
$H_{\mathrm{eq}} = (3 \times 4 + 7 \times 0.5 \times 1) / 10 = (12 + 3.5)/10 = 1.55$ s
ΔP = 1 GW（10%）时：$\mathrm{RoCoF} = 1/(2 \times 1.55 \times 10) = 0.032$ Hz/s ✓

若 DG 不配虚拟惯量：$H_{\mathrm{eq}} = 12/10 = 1.2$ s，RoCoF = 0.042 Hz/s（仍接近阈值）。

### 3.3 一次调频响应时间

一次调频的**响应时间常数** $\tau_{\mathrm{prim}}$：

$$\tau_{\mathrm{prim}} \approx \max(\tau_{\mathrm{governor}}, \tau_{\mathrm{PCS}})$$

| 响应源 | 时间常数 | 优势 |
|---|---|---|
| 同步机调速器（水轮） | 5~10 s | 持续时间长 |
| 同步机调速器（汽轮） | 2~5 s | 响应较快 |
| 电力电子频率环 | 0.1~1 s | **极快**，但持续时间有限（几秒内 PCS 饱和） |

**最佳配置**：同步机提供持续惯量 + 电力电子提供快速一次调频 → 优势互补。

### 3.4 AGC 与虚拟惯量的协调

一个常见误区：AGC（二次调频）和虚拟惯量**作用在不同时间尺度**，不会冲突。虚拟惯量在毫秒~秒级响应 RoCoF，AGC 在分钟级恢复频率——两者天然解耦。

但要注意：**AGC 的积分作用**如果太强，可能抵消虚拟惯量的阻尼效果（积分饱和 + 频率超调）。

**协调原则**：$K_I \leq \omega_{\mathrm{nat}} \cdot D_{\mathrm{total}}$，其中 $\omega_{\mathrm{nat}}$ 是系统固有频率，$D_{\mathrm{total}}$ 是总阻尼。

## 4. 与工程实践的联系

### 4.1 应用场景

| 应用 | 依赖条目 | 标准依据 |
|---|---|---|
| 省级电网频率安全评估 | TH-038（频率稳定/惯量）、TH-057（惯量协调） | GB 38755-2019 |
| 新能源并网一次调频配置 | TH-029（微电网）、TH-056（VSG） | GB/T 40595-2021 |
| AGC 参数整定 | TH-056（VSG 阻尼）、TH-016（功角稳定） | DL/T 1055-2022 |
| RoCoF 注入试验（实测验证） | TH-043（AI/数据处理） | GB/T 40595-2021 |

### 4.2 失效边界

| 边界条件 | 后果 | 工程速记 |
|---|---|---|
| $H_{\mathrm{eq}} < 1.0$ s（高比例新能源） | 任何大扰动 RoCoF > 0.1 Hz/s，触发保护 | 必须配置虚拟惯量，目标 $H_{\mathrm{eq}} \geq 1.5$ s |
| 一次调频响应时间 > 5 s | 频率最低点超过 0.5 Hz 偏差 | 新能源快速频率环 + 同步机调速器配合 |
| AGC $K_I$ 过大 | 二次调频超调 + 与虚拟惯量相互抵消 | $K_I$ 取值使阻尼比 $\zeta \geq 0.5$ |

### 4.3 工程速记

> **频率响应三阶段**：惯性响应（RoCoF ≤ 0.1 Hz/s）→ 一次调频（3 s 内出力）→ 二次调频（5 min 恢复）。$H_{\mathrm{eq}} \geq 1.5$ s 是高比例新能源系统的底线。

## 5. 关联与变更

| 关联 | 说明 |
|---|---|
| [TH-011](TH-011-synchronous-machine-subtransient-reactance.md) | 同步机转子惯量的物理基础 |
| [TH-024](TH-024-power-electronic-converters-and-pwm.md) | PCS 频率环是快速一次调频的硬件基础 |
| [TH-038](TH-038-high-renewable-frequency-stability-inertia.md) | 频率稳定的系统级分析 |
| [TH-048](TH-048-power-system-restoration-and-black-start-optimization.md) | 黑启动过程的频率响应 |
| [TH-056](TH-056-virtual-synchronous-generator-parameter-design-and-stability.md) | VSG 虚拟惯量和阻尼是精细化建模的核心增量 |
| [TH-057](TH-057-virtual-inertia-coordination-and-dispatch.md) | 惯量协调是多场站频率响应的上游 |

**变更记录**：
- 2026-09-10：首版草稿
