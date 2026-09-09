---
id: TH-038
title: 新能源高占比系统频率稳定与惯量支撑
domain: 基础理论
subdomain: 系统稳定
voltage_levels: [HV, EHV]
lifecycle: [设计, 运维]
standards:
  - { code: GB/T 40595-2021, clause: "4", note: "电力系统网源协调技术规范，含新能源惯量与调频要求" }
  - { code: GB/T 19963-2024, clause: "4", note: "光伏发电站接入电力系统技术规定（替代 2012 版，强化调频与惯量）" }
  - { code: GB/T 34122-2023, clause: "4", note: "电化学储能 PCS 技术规范，含构网型惯量支撑" }
  - { code: IEC 61400-27-1:2020, clause: "4", note: "风电场电气仿真模型通用要求，含惯量响应模型" }
status: draft
reviewers: []
version: 0.1
updated: 2026-09-09
---

# 新能源高占比系统频率稳定与惯量支撑

## 1. 定义

**惯量（Inertia）**指同步发电机转子旋转动能对频率变化的自然阻尼能力，物理来源是转子机械惯性 $J$。传统电力系统惯量由火电/水电旋转机组提供，频率变化率（RoCoF, Rate of Change of Frequency）与惯量成反比：

$$
\text{RoCoF}=\frac{\mathrm{d}f}{\mathrm{d}t}=\frac{\Delta P}{2H_\Sigma}
$$

新能源（光伏全电力电子、风电经变流器解耦）**不提供惯量**，高占比下系统等效惯量 $H_\Sigma$ 下降，相同功率缺额下频率跌落更快更深——这是新型电力系统频率稳定的核心挑战。

| 惯量来源 | 物理机理 | 响应速度 | 新型系统贡献 |
|---|---|---|---|
| 同步发电机转子 | 动能 $\frac12 J\omega^2$ 自然释放 | 即时（ms 级） | 递减（火电退役） |
| 风电虚拟惯量（VSG） | 控制提取转子动能 | 10~100 ms | 取决于风机容量与控制 |
| 构网型储能 VSG | 电池能量经控制模拟惯量 | 10~50 ms | 新增主力 |
| 负荷惯量（电动机） | 异步电机转差 | 即时 | 负荷侧被动响应 |

## 2. 物理图像

### 2.1 传统系统频率响应

大功率缺额（如大机组跳闸 $\Delta P$）后，全系统等效摇摆方程（详见 [TH-020 电力系统稳定性分类](TH-020-power-system-stability-classification.md) §3.1）：

$$
\frac{2H_\Sigma}{f_0}\frac{\mathrm{d}\Delta f}{\mathrm{d}t}=\Delta P-K_L\Delta f
$$

三个阶段：

```
t=0    大功率缺额 ΔP
       ↓
       惯量响应（H_Σ）→ RoCoF = ΔP/(2H_Σ)
       ↓
t=0.1~5s  一次调频（调速器）→ Δf 稳定至 Δf_st = ΔP/K_L
       ↓
t=10s~min  二次调频（AGC）→ Δf 恢复至 0
```

### 2.2 高新能源占比的"低惯量"困境

火电退役 + 新能源替代后 $H_\Sigma$ 下降。例如某电网原 $H_\Sigma=8$ s，新能源替代至 60% 后 $H_\Sigma'=3.5$ s，相同 $\Delta P=2$ GW 缺额下：

- 原 RoCoF = 2/(2×8) = 0.125 Hz/s
- 新 RoCoF = 2/(2×3.5) = 0.286 Hz/s（**2.3 倍**）

RoCoF 超过 0.5~1 Hz/s 时部分保护（如 RoCoF 继电器）可能误动脱网，加剧功率缺额，形成恶性循环。

## 3. 推导

### 3.1 系统等效惯量

全系统等效惯量常数：

$$
H_\Sigma = \frac{\sum_i H_i S_i}{\sum_i S_i}
$$

| 新能源占比 | 运行火电/水电 | 等效 $H_\Sigma$ | RoCoF（2 GW 缺额） |
|---|---|---|---|
| 0% | 全部旋转 | 8 s | 0.125 Hz/s |
| 30% | 70% 旋转 | 5.6 s | 0.179 Hz/s |
| 60% | 40% 旋转 | 3.2 s | 0.313 Hz/s |
| 80% | 20% 旋转 | 1.6 s | 0.625 Hz/s（超 RoCoF 保护阈值） |

### 3.2 虚拟惯量控制（VSG）

构网型 PCS 模拟同步发电机摇摆方程：

$$
J_{vsg}\frac{\mathrm{d}\omega}{\mathrm{d}t}=T_m-T_e-D_{vsg}(\omega-\omega_0)
$$

$J_{vsg}$ 为虚拟惯量、$D_{vsg}$ 为虚拟阻尼。频率跌落时 VSG"释放"虚拟动能（实际来自电池），等效提供惯量支撑：

$$
H_{vsg}=\frac{J_{vsg}\omega_0^2}{2S_{vsg}}
$$

| VSG 参数 | 典型值 | 效果 |
|---|---|---|
| $H_{vsg}$ | 3~8 s | 等效一台同容量同步机 |
| $D_{vsg}$ | 1~3 p.u. | 附加阻尼 |
| 响应时间 | 10~50 ms | 快于机械调速器 |

### 3.3 频率稳定判据

频率稳定的最低点（nadir）须高于低频减载首轮动作值（典型 49.0 Hz）。最低点估算（简化）：

$$
\Delta f_{nadir}\approx\frac{\Delta P}{K_L+K_{gov}}\left(1-e^{-t_{nadir}/\tau}\right)
$$

$\tau=2H_\Sigma/K_L$，惯量越小 $\tau$ 越短、最低点出现越早且越深。构网型储能提供的虚拟惯量提高 $\tau$，推迟并抬高最低点——这是 VSG 提升频率稳定裕度的物理机理。

## 4. 与工程实践的联系

- **支撑条目 1**：[TH-020 电力系统稳定性分类](TH-020-power-system-stability-classification.md)——本条是频率稳定子类的深入，给出惯量与 RoCoF 的定量关系。
- **支撑条目 2**：[TH-024 电力电子变换器与 PWM](TH-024-power-electronic-converters-and-pwm.md) 与 [TH-029 微电网控制](TH-029-microgrid-control-and-grid-mode-switching.md) 与 [PR-ES-001 储能接入](../30-practice/PR-ES-001-energy-storage-integration.md)——构网型储能 VSG 是惯量支撑的主要设备。
- **支撑条目 3**：[PR-PE-001 继电保护配置](../30-practice/PR-PE-001-relay-protection-config.md) 与 [PR-PS-001 负荷分级](../30-practice/PR-PS-001-load-classification.md)——低频减载与 RoCoF 保护整定须考虑低惯量工况，避免误动或加剧跌落。
- **失效边界**：① VSG 提供的虚拟惯量受电池容量与 SOC 限制，长时间惯量支撑不可持续；② 构网型 PCS 须在弱电网下仍能稳定建压，SCR 过低时 VSG 可能失稳；③ RoCoF 保护整定过低（如 0.125 Hz/s）在高新能源占比下频繁误动，须按系统惯量水平动态调整；④ 大量分布式 VSG 并联可能引入低频振荡（参数不匹配），须均压与协调控制；⑤ 频率最低点估算公式为简化模型，实际多机系统须全状态空间特征值分析或时域仿真。
- **下游案例**：[CASE-043 光储柴微网](../50-case/CASE-043-composite-pv-storage-diesel-microgrid.md)、[CASE-048 新能源汇集站继保](../50-case/CASE-048-composite-renewable-collector-station-protection.md)、[CASE-054 光伏并网](../50-case/CASE-054-review-pv-anti-islanding-reverse-power.md)

## 5. 关联条目与变更记录

- 关联：[TH-020 电力系统稳定性分类](TH-020-power-system-stability-classification.md)（频率稳定与一次调频方程）、[TH-016 功角稳定](TH-016-synchronous-machine-power-angle-stability.md)（转子方程与惯量物理来源）、[TH-024 电力电子变换器](TH-024-power-electronic-converters-and-pwm.md)（构网型 PCS 与 VSG）、[TH-029 微电网控制](TH-029-microgrid-control-and-grid-mode-switching.md)（下垂与 VSG 并联）、[TH-036 AVR/PSS](TH-036-excitation-system-avr-pss.md)（调速器与 PSS 类比的惯量控制）、[PR-ES-001 储能接入](../30-practice/PR-ES-001-energy-storage-integration.md)、[PR-PE-001 继电保护配置](../30-practice/PR-PE-001-relay-protection-config.md)、[PR-PS-001 负荷分级](../30-practice/PR-PS-001-load-classification.md)
- 下游案例：见 §4 列表。

| 版本 | 日期 | 修改内容 | 修改人 |
|---|---|---|---|
| 0.1 | 2026-09-09 | 创建；含惯量-RoCoF 定量关系、VSG 摇摆方程、频率最低点估算、低惯量下 RoCoF 保护误动与电池容量失效边界 | KB 管理员 |
