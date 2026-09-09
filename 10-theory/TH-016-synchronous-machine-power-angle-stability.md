---
id: TH-016
title: 同步电机功角稳定基础
domain: 基础理论
subdomain: 电力系统
voltage_levels: []
lifecycle: []
standards:
  - { code: GB/T 31464-2015, clause: "5.2", note: "电网运行准则，规定同步稳定裕度与暂态稳定校核口径" }
  - { code: DL/T 1234-2013, clause: "4", note: "电力系统安全稳定计算规范，给出静态/暂态稳定判据与等面积法则应用约定" }
  - { code: GB/T 40595-2021, clause: "4", note: "电力系统网源协调技术规范，规定发电机涉网稳定性参数（含 PSS/AVR）" }
status: draft
reviewers: []
version: 0.1
updated: 2026-09-09
---

# 同步电机功角稳定基础

## 1. 定义

[功角](../00-meta/00-术语表.md#功角) $\delta$（又称功率角、转子角）是发电机内电势 $\dot{E}$ 与系统参考母线电压 $\dot{U}$ 之间的相位角，单位 rad（°）。**功角稳定**指同步电机受到扰动后维持转子间同步运行的能力；按扰动量级与时间尺度分为两类：

| 类型 | 扰动量级 | 时间尺度 | 失稳形态 |
|---|---|---|---|
| 静态稳定（小扰动） | 微小（<1%） | 0~10 s | 非周期失步或低频振荡（0.1~2 Hz） |
| 暂态稳定（大扰动） | 大型故障 | 0~3 s | 第一/多摆周期内非周期失步 |

| 物理量 | 符号 | 单位 |
|---|---|---|
| 发电机内电势（暂态电势） | $E_q'$ | V |
| 系统母线电压 | $U$ | V |
| 总电抗（$X_d'+X_T+X_s$） | $X_\Sigma$ | Ω |
| 电磁功率 | $P_e$ | W |
| 机械功率 | $P_m$ | W |
| 转子惯性常数 | $H$ | s |
| 加速面积（暂态） | $A_{acc}$ | W·rad |
| 减速面积 | $A_{dec}$ | W·rad |

## 2. 物理图像

发电机并网稳态时机械功率 $P_m$ 与电磁功率 $P_e$ 平衡，转子以同步速旋转，$\delta=\delta_0$ 恒定。一旦 $P_m\ne P_e$，转子获得净加速转矩：

$$
\frac{2H}{\omega_0}\frac{\mathrm{d}^2\delta}{\mathrm{d}t^2}=P_m-P_e
$$

> **类比**：单机-无穷大母线等价于一辆"挂载重物"的小车通过弹簧连到墙（无穷大母线）。弹簧拉力即电磁功率 $P_e$，由两端的相对位移 $\delta$ 决定（功角特性）；机械功率 $P_m$ 是稳态推力。故障发生时弹簧力下降（电抗骤增），小车被推力加速、$\delta$ 增大；故障切除后电抗恢复，弹簧力回到正常特性曲线，若减速面积能补足加速面积，小车在若干摆动后回到新平衡点，否则越过 $\delta_{max}=\pi-\delta_0$（弹簧拉力反过来推小车），失步。

```
功角特性 P-δ（凸极机含磁阻功率，本条暂用隐极机经典式 P_e=(EU/X)sinδ）

  P_e↑
   │       ╱─稳态工作点δ0
   │      ╱ ── 故障中曲线 (XΣf↑ → 峰值低)
   │     ╱   ── 故障切除后曲线
   │    ╱
   │   ╱     A_acc (阴影上)
   │  ╱      A_dec (阴影下)
   │ ╱
   │╱________________→ δ
   0   δ0   δc   δmax
```

## 3. 推导

### 3.1 隐极机经典功角方程

不计凸极效应（$X_d=X_q$）、不计定子电阻，用暂态电势 $E_q'$（[TH-015](TH-015-synchronous-machine-park-equations.md) §3.5）：

$$
P_e(\delta)=\frac{E_q' U}{X_\Sigma}\sin\delta
$$

稳态工作点 $P_m=P_e(\delta_0)$，故 $\delta_0=\arcsin(P_m X_\Sigma/(E_q' U))$。

### 3.2 静态稳定判据

小扰动下线性化转子运动方程：

$$
\Delta P_e = \left.\frac{\mathrm{d}P_e}{\mathrm{d}\delta}\right|_{\delta_0}\Delta\delta = \frac{E_q' U}{X_\Sigma}\cos\delta_0 \cdot \Delta\delta
$$

代入运动方程得单自由度二阶系统 $\dfrac{2H}{\omega_0}\Delta\ddot\delta + K_s\Delta\delta=0$，其中 $K_s=\dfrac{E_q' U}{X_\Sigma}\cos\delta_0$。

**静态稳定判据**：$K_s>0$，即 $\cos\delta_0>0$，$\delta_0<90°$。

**比整步功率** $K_s$ 体现单位功角偏差下系统提供的恢复功率——这是静态稳定的本质度量。隐极机理论极限 $\delta_0=90°$（对应 $P_{e,max}=E_q' U/X_\Sigma$），考虑 15%~20% 稳定储备后工程实用工作区 $\delta_0\le 70°$。

### 3.3 暂态稳定的等面积法则

故障过程中 $P_m$ 不变（调速器慢），$P_e$ 因网络电抗增大而骤降，转子加速，$\delta$ 由 $\delta_0$ 推到故障切除角 $\delta_c$：

$$
A_{acc}=\int_{\delta_0}^{\delta_c}(P_m-P_e^{(fault)})\,\mathrm{d}\delta
$$

故障切除后 $P_e$ 跃迁到故障后曲线，若减速转矩能把加速功补足：

$$
A_{dec}=\int_{\delta_c}^{\delta_{max}}(P_e^{(post)}-P_m)\,\mathrm{d}\delta \ge A_{acc}
$$

则系统稳定，否则越过 $\delta_{max}=\pi-\arcsin(P_m X_\Sigma^{post}/(E_q' U))$ 失步。**等面积法则**：$A_{acc}=A_{dec}$，对应临界切除角 $\delta_{cc}$：

$$
\cos\delta_{cc}=\frac{P_m(\delta_{max}^{post}-\delta_0)+P_{e,max}^{post}\cos\delta_{max}^{post}-P_{e,max}^{(fault)}\cos\delta_0}{P_{e,max}^{post}-P_{e,max}^{(fault)}}
$$

由 $\delta_{cc}$ 反推**临界切除时间** $t_{cc}$，是继电保护与断路器开断时间的工程约束（详见 §4）。

### 3.4 多机系统与数值积分

多机系统无闭式解，需对全系统 $2n$ 维摇摆方程数值积分：

$$
\frac{2H_i}{\omega_0}\ddot\delta_i=P_{mi}-\sum_{j\ne i}E_i'E_j'\bigl(B_{ij}\sin\delta_{ij}+G_{ij}\cos\delta_{ij}\bigr),\quad i=1,\dots,n
$$

工程计算软件（PSD-BPA、PSD-PC、PSS/E、PowerFactory）以 0.001~0.005 s 步长龙格-库塔或梯形法积分，依据 DL/T 1234-2013 校核 $t=3$ s 内不出现 $\delta_{ij}>180°$ 的相对角失稳。

## 4. 与工程实践的联系

- **支撑条目 1**：[PR-PE-001 继电保护配置](../30-practice/PR-PE-001-relay-protection-config.md)——失步保护（unstable power swing）依据功角摆动识别失稳，整定门槛须躲过最大稳定摆动；本条给出失稳判据与摆动速率（典型 $|\mathrm{d}\delta/\mathrm{d}t|=1\sim5\,\mathrm{rad/s}$）的物理来源。
- **支撑条目 2**：[CALC-SC-002 高压短路电流计算](../40-calc/CALC-SC-002-hv-short-circuit-iec60909.md) §暂态电势——发电机端近端短路时 $E_q'$ 由 Park 方程给出，是 $I_k''$ 与暂态稳定计算的公共参数。
- **失效边界**：① 等面积法则仅适用**单机-无穷大**与两机系统，多机须数值积分；② 经典模型忽略 AVR 与调速器，实际 AVR 强励动作可显著增大 $E_q'$、扩大 $A_{dec}$，故保守用暂态电势不变算出的 $t_{cc}$ 是工程下限；③ 长过程稳定（>3 s）须考虑锅炉/AGC 动态，超出本条范畴；④ 电压稳定（PV 母线崩溃）与频率稳定（低频减载）属另两类稳定问题，机理不同，见 [PR-PQ-001 电能质量治理](../30-practice/PR-PQ-001-pq-compensation-design.md) §电压频率关联。
- **下游案例**：[CASE-022 短路电流与保护整定](../50-case/CASE-022-exam-short-circuit-protection.md)、[CASE-048 新能源汇集站继保](../50-case/CASE-048-composite-renewable-collector-station-protection.md)、[CASE-051 距离保护越级](../50-case/CASE-051-review-distance-protection-coordination-cascade-trip.md)、[CASE-043 构网型 PCS](../50-case/CASE-043-composite-pv-storage-diesel-microgrid.md)

## 5. 关联条目与变更记录

- 关联：[TH-015 Park 方程与暂态深入](TH-015-synchronous-machine-park-equations.md)（$E_q'$ 来源、小扰动线性化）、[TH-011 同步机次暂态电抗](TH-011-synchronous-machine-subtransient-reactance.md)（短路计算参数交叉）、[PR-PE-001 继电保护配置](../30-practice/PR-PE-001-relay-protection-config.md)（失步保护整定）、[CALC-SC-002 高压短路电流](../40-calc/CALC-SC-002-hv-short-circuit-iec60909.md)
- 下游案例：见 §4 列表。

| 版本 | 日期 | 修改内容 | 修改人 |
|---|---|---|---|
| 0.1 | 2026-09-09 | 创建；含隐极机功角方程、静态稳定判据、等面积法则临界切除角、多机摇摆方程 | KB 管理员 |
