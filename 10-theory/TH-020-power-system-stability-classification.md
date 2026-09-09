---
id: TH-020
title: 电力系统稳定性分类（功角/电压/频率/次同步）
domain: 基础理论
subdomain: 电力系统
voltage_levels: [HV, EHV, UHV]
lifecycle: [设计, 运维]
standards:
  - { code: GB/T 31464-2015, clause: "5.2", note: "电网运行准则，规定静态/暂态稳定裕度与三类稳定校核口径" }
  - { code: DL/T 1234-2013, clause: "4", note: "电力系统安全稳定计算规范，给出静态/暂态/电压/频率稳定判据与时域仿真范围" }
  - { code: DL/T 5810-2020, clause: "4", note: "电力系统电压和无功电力技术导则，定义电压稳定裕度与 PV/QV 曲线" }
  - { code: GB/T 40595-2021, clause: "4", note: "电力系统网源协调技术规范，规定涉网稳定性参数（含低频减载）" }
status: draft
reviewers: []
version: 0.1
updated: 2026-09-09
---

# 电力系统稳定性分类（功角/电压/频率/次同步）

## 1. 定义

**电力系统稳定性**指系统在受到扰动后维持各同步发电机同步运行、各节点电压幅值与频率在允许范围内、并能恢复到新的稳态运行点的能力。IEEE/CIGRE 联合工作组 2020 年报告将稳定性分为四大类，本条以此为基础给出工程口径：

| 大类 | 子类 | 物理量 | 时间尺度 | 失稳形态 |
|---|---|---|---|---|
| **功角稳定**（[TH-016](TH-016-synchronous-machine-power-angle-stability.md)） | 静态/暂态/小扰动 | 转子相对角 $\delta_{ij}$ | 0~3 s | 非周期或低频振荡失步 |
| **电压稳定** | 短期（暂态）/长期 | 母线电压 $U$ | 0~10 s / 1~10 min | PV 鼻尖崩塌 / 缓慢下降 |
| **频率稳定** | 短期/长期 | 系统频率 $f$ | 0~30 s | 频率崩塌 / 频率越限 |
| **次同步振荡** | SSO：扭振/谐振/自励磁 | 轴系扭振角 $\theta_m$、次同步电流 | 10 ms~10 s | 轴系疲劳、电流振荡 |

| 物理量 | 符号 | 单位 |
|---|---|---|
| 系统频率 | $f$ | Hz |
| 频率变化率 | $\mathrm{d}f/\mathrm{d}t$ | Hz/s |
| 负荷有功频率特性系数 | $K_L$ | p.u./Hz |
| 系统等效惯性常数 | $H_\Sigma=\sum H_iS_i/\sum S_i$ | s |
| 母线电压 | $U$ | p.u. |
| 短路比（短路容量/负荷） | SCR | — |
| 阻尼比 | $\zeta$ | — |

## 2. 物理图像

**频率稳定**——有功平衡问题：发电机机械功率 $P_m$ 与负荷有功 $P_L$ 失衡，转子动能释放或吸收：

$$
\frac{2H_\Sigma}{f_0}\frac{\mathrm{d}\Delta f}{\mathrm{d}t}=\Delta P_m-\Delta P_L=\Delta P_m-K_L\Delta f
$$

负荷的"频率自调节" $K_L\Delta f$（电动设备随频率下降吸收功率下降）提供天然负反馈，但 $H_\Sigma$ 越小、$K_L$ 越小，频率变化率越大。低频减载（UFLS）按 $\Delta f<-\!0.4$ Hz 一级动作，是最后的频率稳定防线。

**电压稳定**——无功平衡问题：负荷由高压长线馈电时，末端电压 $U_2$ 与负荷功率 $P_L$ 形成 **PV 鼻型曲线**：

```
U₂↑
 │      ╱──鼻尖前（稳定，dU/dP>0）
 │     ╱ 
 │    ╱
 │- -×- - - - -鼻尖（dU/dP=∞）
 │    ╲
 │     ╲──鼻尖后（不稳定，dU/dP<0）
 │      ╲
 └──────────────→ P_L
```

鼻尖点对应负荷阻抗等于线路戴维南等效阻抗 $Z_{th}$，即 $|Z_L|=|Z_{th}|$（最大功率传输定理）。负荷继续增大越过鼻尖，系统不能提供新的平衡点 → **电压崩塌**。短期暂态电压稳定与发电机暂态电势、感应电动机再加速有关；长期电压稳定与 OLTC 动作、恒温负荷热特性有关。

**次同步振荡**——机-网耦合问题：电网谐振频率 $f_n$ 与发电机轴系自然扭振频率 $f_m$ 满足 $f_n+f_m=f_0$（互补频率关系）时形成次同步谐振 SSR（串补线路典型）；构网型 PCS 控制参数与电网阻抗耦合可能引发 SSO（控制器诱导），是新能源高占比电网新风险。

## 3. 推导

### 3.1 频率稳定一次调频方程

单机或全系统等效摇摆方程加负荷频率特性：

$$
\frac{2H_\Sigma}{f_0}\frac{\mathrm{d}\Delta f}{\mathrm{d}t}=\Delta P_m-K_L\Delta f
$$

稳态时 $\mathrm{d}\Delta f/\mathrm{d}t=0$，得调差率 $\Delta f_{st}=\Delta P_m/K_L$。一台机调差系数 $R_i=\Delta f/\Delta P_i$（典型 4%~5%），多机并联等效调差 $1/R_\Sigma=\sum 1/R_i$，机组容量越大调频责任越大。

### 3.2 电压稳定 PV 鼻尖判据

单机-无穷大母线经阻抗 $Z=R+jX$ 馈电，末端功率方程（极坐标形式）：

$$
P_L=\frac{E^2}{|Z|^2}(R\cos\delta+X\sin\delta)-\frac{EU_2}{|Z|^2}(R\cos\theta+X\sin\theta)
$$

鼻尖处 $\partial P_L/\partial U_2=0$ 给出 $U_2$ 临界值。工程上用 **短路比** $SCR=|Z_{th}|^{-1}\cdot U_n^2/P_L$ 判定：$SCR>3$ 强系统、$1.5<SCR<3$ 弱系统、$SCR<1.5$ 极弱系统（新能源并网关键指标）。

### 3.3 次同步谐振判据

发电机经串联补偿并网时，电网从发电机端看入的等效阻抗含谐振点 $f_n=f_0\sqrt{1/(LC)}$；若 $f_n<f_0$，发电机感受到的电气频率 $f_e=f_0-f_n$ 与转子机械扭振模态 $f_m$ 接近互补 → 形成扭振放大条件。IEEE 次同步谐振判据：

$$
f_m+f_n=f_0 \quad \text{（互补条件，必要非充分）}
$$

### 3.4 静态功角稳定（衔接 [TH-016](TH-016-synchronous-machine-power-angle-stability.md)）

$K_s=\mathrm{d}P_e/\mathrm{d}\delta>0$；本条不重复推导，仅在小扰动稳定分类中引用。

## 4. 与工程实践的联系

- **支撑条目 1**：[PR-PS-001 负荷分级](../30-practice/PR-PS-001-load-classification.md)——一级负荷的供电可靠性约束涵盖频率稳定与电压稳定双重校核；低频减载首级动作阈值与一级负荷解锁时序互为约束（GB 50016 一级负荷不应被低频减载首级切除）。
- **支撑条目 2**：[PR-PE-001 继电保护配置](../30-practice/PR-PE-001-relay-protection-config.md)——低频减载、低压减载（UVLS）、失步保护是系统性安全自动装置，整定须躲过最大暂态偏移；SSO 监测装置（IEEE 1544 监测点）属涉网保护。
- **失效边界**：① 本条分类基于交流同步系统；直流系统（HVDC、直流微电网）只有电压稳定与功率稳定，无频率稳定与功角稳定；② 单机-无穷大模型仅用于阐明概念，实际多机系统须用 DL/T 1234 数值仿真；③ 长过程稳定（>10 min）须考虑负荷热特性、锅炉动态、AGC，超出本条范畴；④ SSO 涉及多刚体扭振模态与电力电子控制耦合，须 PSCAD/EMTDC 电磁暂态仿真，本条仅给物理图像。
- **下游案例**：[CASE-022 短路电流与保护整定](../50-case/CASE-022-exam-short-circuit-protection.md)、[CASE-048 新能源汇集站继保](../50-case/CASE-048-composite-renewable-collector-station-protection.md)、[CASE-051 距离保护越级](../50-case/CASE-051-review-distance-protection-coordination-cascade-trip.md)、[CASE-043 构网型 PCS](../50-case/CASE-043-composite-pv-storage-diesel-microgrid.md)、[CASE-053 轨道交通整流](../50-case/CASE-053-composite-rail-transit-traction-rectifier.md)

## 5. 关联条目与变更记录

- 关联：[TH-016 功角稳定基础](TH-016-synchronous-machine-power-angle-stability.md)（功角稳定子类衔接）、[TH-019 输电线路参数与长线方程](TH-019-transmission-line-parameters-long-line.md)（PV 鼻尖与馈电线路阻抗）、[TH-015 Park 方程](TH-015-synchronous-machine-park-equations.md)（轴系扭振模态）、[PR-PS-001 负荷分级](../30-practice/PR-PS-001-load-classification.md)、[PR-PE-001 继电保护配置](../30-practice/PR-PE-001-relay-protection-config.md)、[CALC-SC-002 高压短路电流](../40-calc/CALC-SC-002-hv-short-circuit-iec60909.md)（短路比 SCR 衍生）
- 下游案例：见 §4 列表。

| 版本 | 日期 | 修改内容 | 修改人 |
|---|---|---|---|
| 0.1 | 2026-09-09 | 创建；含 IEEE/CIGRE 四大分类、频率一次调频方程、PV 鼻尖短路比判据、SSR 互补频率条件 | KB 管理员 |
