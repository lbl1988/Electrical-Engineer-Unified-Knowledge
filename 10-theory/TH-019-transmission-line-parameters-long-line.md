---
id: TH-019
title: 输电线路参数与长线方程
domain: 基础理论
subdomain: 电力系统
voltage_levels: [HV, EHV, UHV]
lifecycle: [设计, 验收, 运维]
standards:
  - { code: GB/T 1179-2017, clause: "4", note: "架空导线产品技术条件（含绞线参数、电阻率）" }
  - { code: DL/T 5222-2021, clause: "5", note: "导体和电器选择设计技术规程，给出线路参数选用与电晕校核口径" }
  - { code: GB/T 50065-2011, clause: "4", note: "交流电气装置接地设计，含地线/相线自感互感计算" }
  - { code: DL/T 5233-2018, clause: "3", note: "电力工程架空线路设计规程，含电气参数取值与档距校核" }
status: draft
reviewers: []
version: 0.1
updated: 2026-09-09
---

# 输电线路参数与长线方程

## 1. 定义

**输电线路参数**指单位长度的电阻 $R_0$（Ω/km）、电抗 $X_0=\omega L_0$（Ω/km）、电纳 $B_0=\omega C_0$（S/km）、电导 $G_0$（S/km，主要反映电晕损耗）。**长线方程**指稳态正弦下均匀分布参数线路的电压电流沿线分布方程，给出任意点 $x$ 处电压电流与始末端的关系。

按几何长度 $l$ 与波长 $\lambda$ 的比值划分线路模型（工频 $\lambda=6000$ km）：

| 类别 | 几何长度（参考值） | 工程模型 |
|---|---|---|
| 短线 | $l<50$ km（架空）/ $<5$ km（电缆） | 集中参数：仅串联 $Z=R_0l+jX_0l$ |
| 中长线 | $50\sim 200$ km | 集中 π/T 等效（串联 Z + 两端并联 Y/2） |
| 长线 | $l>200$ km | 分布参数：双曲函数 $U(x),I(x)$ |

| 物理量 | 符号 | 单位 |
|---|---|---|
| 串联阻抗 | $z_0=R_0+j\omega L_0$ | Ω/km |
| 并联导纳 | $y_0=G_0+j\omega C_0$ | S/km |
| 传播常数 | $\gamma=\alpha+j\beta=\sqrt{z_0 y_0}$ | 1/km |
| 特性阻抗（波阻抗） | $Z_c=\sqrt{z_0/y_0}$ | Ω |
| 波长 | $\lambda=2\pi/\beta$ | km |
| 线路自然功率 | $P_n=U_n^2/Z_c$ | W |

## 2. 物理图像

线路串联阻抗 $z_0$ 来自：① **电阻 $R_0$**（趋肤+导线直流电阻）；② **自感 $L_s$**（导线自身磁链）；③ **互感 $M$**（邻相导线耦合）；④ **地线回路**（大地作为返回通路引入卡森级数修正）。

并联导纳 $y_0$ 来自：① **对地电容 $C_0$**（导线-大地/导线-中线/导线-导线三部分，由 Maxwell 系数矩阵求逆得出）；② **对地电导 $G_0$**（电晕损耗 + 介质损耗，晴天可忽略，雨天显著增大）。

> **几何位置感**：分裂导线增大等效半径 $r_{eq}$，使 $L_0$ 减小、$C_0$ 增大、$Z_c$ 降低——这是超高压线路用 4~8 分裂导线的核心物理理由。典型 500 kV 4 分裂：$L_0\approx 0.89$ mH/km、$C_0\approx 12.7$ nF/km、$Z_c\approx 265$ Ω、自然功率 $P_n\approx 940$ MW。

```
双曲长线稳态分布（末端功率 P, Q 已知）：

  U(x) ↑                       Π 等效（中长线）
      │                                         
      │──╲                                       ┌──┐ 
      │  ╱──┐                          Y/2 ───┤  ├─── Y/2
      │─╱   │   串联 Z=z₀l                └──┘
      │                              │      ┌──┐     │
      └────────────────→ x          ───────┤  ├─────
                                       Z  └──┘  Y/2
      双曲分布：U(x)=U₂cosh(γx)+ZcI₂sinh(γx)
```

## 3. 推导

### 3.1 微分方程（工频相量）

取微元 dx，串联 $z_0\,\mathrm{d}x$、并联 $y_0\,\mathrm{d}x$，相量形式：

$$
-\frac{\mathrm{d}\dot U}{\mathrm{d}x}=z_0\dot I,\quad -\frac{\mathrm{d}\dot I}{\mathrm{d}x}=y_0\dot U
$$

### 3.2 二阶常微分方程与通解

对 x 再求导并代入：

$$
\frac{\mathrm{d}^2\dot U}{\mathrm{d}x^2}=\gamma^2 \dot U,\quad \frac{\mathrm{d}^2\dot I}{\mathrm{d}x^2}=\gamma^2 \dot I
$$

通解（末端边界 $x=0$ 处 $\dot U=\dot U_2,\dot I=\dot I_2$）：

$$
\boxed{\;\dot U(x)=\dot U_2\cosh(\gamma x)+Z_c\dot I_2\sinh(\gamma x)\;}
$$

$$
\dot I(x)=\dot I_2\cosh(\gamma x)+\frac{\dot U_2}{Z_c}\sinh(\gamma x)
$$

（x 自末端起算，向电源端为正方向）

| 符号 | 含义 | 单位 |
|---|---|---|
| $\alpha$ | 衰减常数（单位长度行波幅值衰减率） | 1/km |
| $\beta$ | 相位常数（单位长度行波相移） | rad/km |
| $\lambda=2\pi/\beta$ | 工频波长 | km |
| $v=\omega/\beta$ | 相速度（接近光速 295 km/ms） | km/ms |

### 3.3 双曲型 ABCD 参数

整线参数矩阵（始端 $x=l$，末端 $x=0$）：

$$
\begin{bmatrix}\dot U_1\\\dot I_1\end{bmatrix}
=\begin{bmatrix}A&B\\C&D\end{bmatrix}\begin{bmatrix}\dot U_2\\\dot I_2\end{bmatrix}
=\begin{bmatrix}\cosh(\gamma l)&Z_c\sinh(\gamma l)\\\tfrac{1}{Z_c}\sinh(\gamma l)&\cosh(\gamma l)\end{bmatrix}\begin{bmatrix}\dot U_2\\\dot I_2\end{bmatrix}
$$

满足 $AD-BC=1$（互易）、$A=D$（对称）。中长线 $|\gamma l|\ll 1$ 时泰勒展开取一阶：$\cosh(\gamma l)\approx 1$、$\sinh(\gamma l)\approx \gamma l$、$Z_c\gamma l=z_0 l=Z$、$\gamma l/Z_c=y_0 l=Y$，得 π 等效（两端各 $Y/2$、串联 $Z$），与集中参数法一致。

### 3.4 自然功率 $P_n$ 与费兰蒂效应

末端匹配 $Z_{load}=Z_c$ 时沿线无反射、$\dot U$、$\dot I$ 同相、沿线电压幅值恒定。此时传输功率即**自然功率**：

$$
P_n=\frac{U_n^2}{Z_c}
$$

末端空载 $I_2=0$ 时，$\dot U_1=\dot U_2\cosh(\gamma l)$，因 $\cosh(\gamma l)$ 含 $\sin$ 虚部使幅值随长度增大——**费兰蒂效应**：长线空载末端电压高于电源端，500 km 空载线路末端可升 5%~10%，须并联电抗器补偿。

### 3.5 典型线路参数（交流 50 Hz）

| 电压等级 | 导线配置 | $R_0$ | $X_0$ | $B_0$ | $Z_c$ | $P_n$ |
|---|---|---|---|---|---|---|
| 110 kV | LGJ-240 单根 | 0.13 | 0.40 | 2.78 | 380 | 32 MW |
| 220 kV | LGJ-2×300 分裂 | 0.05 | 0.33 | 3.40 | 310 | 156 MW |
| 500 kV | LGJ-4×300 分裂 | 0.025 | 0.28 | 3.95 | 265 | 940 MW |
| 750 kV | LGJ-6×400 分裂 | 0.012 | 0.22 | 4.45 | 222 | 2530 MW |
| 1000 kV | LGJ-8×500 分裂 | 0.008 | 0.20 | 5.00 | 200 | 5000 MW |

> **趋势速记**：电压越高，分裂越多 → $R_0\downarrow$、$X_0\downarrow$、$B_0\uparrow$、$Z_c\downarrow$ → 自然功率近平方级增长（$P_n\propto U_n^2/Z_c$）。

## 4. 与工程实践的联系

- **支撑条目 1**：[CALC-PT-002 距离保护整定](../40-calc/CALC-PT-002-distance-protection-setting.md)——距离 I 段测量阻抗 $Z_{meas}=R+jX$ 反映线路上故障点到保护安装处的距离，本条给出 $z_0$ 与沿线分布是整定计算基础。
- **支撑条目 2**：[CALC-SC-002 高压短路电流](../40-calc/CALC-SC-002-hv-short-circuit-iec60909.md)——远端短路用线路阻抗作系统等效，长线段还须考虑分布参数对短路初始值的修正。
- **失效边界**：① 工频长线方程仅适用于 50 Hz 单一频率稳态，对操作过电压/雷电行波须用 [TH-017 波过程](TH-017-cable-wave-process-vfto.md) 时域电报方程；② 串联补偿电容器与并联电抗器改变沿线电气长度，须修正 ABCD 矩阵后参与潮流/稳定计算；③ 不换位长线三相参数不对称，须用相域模型或序参数加权修正；④ 海缆分布电容极大（$C_0$ 20~50 倍于架空），充电功率主导，5~10 km 即按长线处理。
- **下游案例**：[CASE-022 短路电流与保护整定](../50-case/CASE-022-exam-short-circuit-protection.md)、[CASE-048 新能源汇集站继保](../50-case/CASE-048-composite-renewable-collector-station-protection.md)、[CASE-051 距离保护越级](../50-case/CASE-051-review-distance-protection-coordination-cascade-trip.md)、[CASE-054 光伏孤岛与逆功率校审](../50-case/CASE-054-review-pv-anti-islanding-reverse-power.md)、[CASE-028 海上风电升压站协同](../50-case/CASE-028-composite-offshore-wind-substation.md)

## 5. 关联条目与变更记录

- 关联：[TH-001 似稳场近似](TH-001-quasi-static-approximation.md)（短线模型边界）、[TH-002 相量法](TH-002-phasor-analysis.md)（推导工具）、[TH-017 电缆波过程](TH-017-cable-wave-process-vfto.md)（暂态对应稳态长线）、[CALC-PT-002 距离保护](../40-calc/CALC-PT-002-distance-protection-setting.md)、[CALC-SC-002 高压短路电流](../40-calc/CALC-SC-002-hv-short-circuit-iec60909.md)、[PR-PS-001 负荷分级](../30-practice/PR-PS-001-load-classification.md)
- 下游案例：见 §4 列表。

| 版本 | 日期 | 修改内容 | 修改人 |
|---|---|---|---|
| 0.1 | 2026-09-09 | 创建；含长线二阶方程通解、ABCD 双曲参数、自然功率与费兰蒂效应、典型线路参数表 | KB 管理员 |
