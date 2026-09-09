---
id: TH-015
title: 同步电机暂态深入（Park 方程与暂态电磁过程）
domain: 基础理论
subdomain: 电机学
voltage_levels: []
lifecycle: []
standards:
  - { code: GB 755-2017, clause: "3", note: "旋转电机定额和性能（idt IEC 60034-1），定义同步电机基本量、dq0 轴约定与额定值" }
  - { code: GB/T 15544.1-2013, clause: "4.3", note: "等效电压源法用 Xd″/Xd′/X2/X0 作发电机暂态等效参数" }
  - { code: GB/T 7064-2017, clause: "5", note: "同步电机励磁系统分类（隐极/凸极）与暂态模型约定" }
status: draft
reviewers: []
version: 0.1
updated: 2026-09-09
---

# 同步电机暂态深入（Park 方程与暂态电磁过程）

## 1. 定义

[Park 变换](../00-meta/00-术语表.md#park-变换)（1929，R. H. Park）是把定子 abc 三相量映射到与转子同步旋转的 **d（直轴）/q（交轴）/0（零轴）** 上的非功率不变形式；功率不变约定下变换矩阵元素略有差异，但物理本质相同。其作用是把**电感系数随转子位置周期变化**的 abc 坐标电压方程，转化为**电感系数常数化**的 dq0 坐标方程，从而显式求解同步电机暂态过程。

| 物理量 | 符号 | 单位 |
|---|---|---|
| Park 变换矩阵 | $\mathbf{P}$ | — |
| 转子电角位置（d 轴超前 a 相磁轴） | $\theta$ | rad |
| 转子机械角速度 × 极对数 | $\omega_r=\omega=p\theta$ | rad/s |
| 定子 abc 三相电流向量 | $\mathbf{i}_{abc}$ | A |
| dq0 轴电流向量 | $\mathbf{i}_{dq0}$ | A |

## 2. 物理图像

定子三相绕组在空间相差 120°，转子磁场以电角速度 $\omega$ 旋转。**站在定子看**：三相绕组与转子之间的互感是 $\theta$ 的函数（含 $\cos\theta$、$\cos(\theta\pm 2\pi/3)$），导致 abc 方程中 $L_{ij}=L_{ij}(\theta)$ 随时间变化，无法直接积分。

**站在转子看**（Park 变换的几何意义）：把定子三相绕组合成一个与转子同步旋转的"等效定子绕组"，分解为 d 轴分量（与转子主磁通同向）和 q 轴分量（超前 90°）。由于 d、q 轴与转子无相对运动，互感不再随 $\theta$ 变化；零轴对应三相瞬时值之和的 $1/\sqrt{3}$，与转子无关，气隙主磁通中无零轴贡献，故 $L_0=L_{ls}$（定子漏感）。

```
abc 三相（静止，互感随θ变化）
   │  Park 变换 P(θ)
   ▼
dq0 轴（随转子旋转，互感常数化）
   ├─ d 轴：与转子主磁通同向，含励磁+阻尼耦合
   ├─ q 轴：超前 90°，凸极机中仅含阻尼耦合
   └─ 0 轴：与转子无关，仅定子漏感
```

## 3. 推导

### 3.1 功率不变约定下的 Park 变换

采用功率不变约定（变换前后功率不变），$\mathbf{i}_{dq0}=\mathbf{P}\mathbf{i}_{abc}$：

$$
\mathbf{P}=\sqrt{\frac{2}{3}}\begin{bmatrix}
\cos\theta & \cos(\theta-\frac{2\pi}{3}) & \cos(\theta+\frac{2\pi}{3}) \\
-\sin\theta & -\sin(\theta-\frac{2\pi}{3}) & -\sin(\theta+\frac{2\pi}{3}) \\
\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}}
\end{bmatrix}
$$

满足 $\mathbf{P}^{-1}=\mathbf{P}^{T}$（正交矩阵），故功率守恒 $P=\frac{3}{2}(v_d i_d+v_q i_q)+3v_0 i_0$ 简化为 $P=v_d i_d+v_q i_q+2v_0 i_0$。

### 3.2 dq0 轴电压方程（含转速电动势项）

派克方程核心——dq0 轴电压含两项：磁链变化项 + **转速电动势项** $\omega\psi$：

$$
\begin{aligned}
v_d &= -R_s i_d - p\psi_d + \omega\psi_q \\
v_q &= -R_s i_q - p\psi_q - \omega\psi_d \\
v_0 &= -R_s i_0 - p\psi_0
\end{aligned}
$$

其中 $\psi_d=L_d i_d + L_{af}i_f + L_{aD}i_D$，$\psi_q=L_q i_q + L_{aQ}i_Q$，$\psi_0=L_0 i_0$；$p=\mathrm{d}/\mathrm{d}t$。

| 符号 | 含义 | 单位 |
|---|---|---|
| $R_s$ | 定子相电阻 | Ω |
| $L_d,L_q$ | d/q 轴同步电感（含电枢反应） | H |
| $L_{af},L_{aD},L_{aQ}$ | 定子-转子互感（d 轴-励磁 / d 轴-阻尼 / q 轴-阻尼） | H |
| $\psi_d,\psi_q,\psi_0$ | dq0 轴磁链 | Wb |
| $\omega$ | 转子电角速度 | rad/s |

**转速电动势项** $\omega\psi_q$、$\omega\psi_d$ 是机械能↔电能转换的桥梁：稳态时 $p\psi=0$，$v_q=-\omega\psi_d$ 即发电机电势 $E_f=\omega L_{af}i_f/\sqrt{3}$（线值）。

### 3.3 转子侧方程（f/D/Q 三绕组）

$$
\begin{aligned}
v_f &= R_f i_f + p\psi_f,\quad \psi_f=L_{ff}i_f+L_{fD}i_D+\tfrac{3}{2}L_{af}i_d \\
0 &= R_D i_D + p\psi_D,\quad \psi_D=L_{Df}i_f+L_{DD}i_D+\tfrac{3}{2}L_{aD}i_d \\
0 &= R_Q i_Q + p\psi_Q,\quad \psi_Q=L_{QQ}i_Q+\tfrac{3}{2}L_{aQ}i_q
\end{aligned}
$$

阻尼绕组短接（$v_D=v_Q=0$）。系数 $\tfrac{3}{2}$ 来自功率不变约定下 abc→dq0 互感的 $3/2$ 倍标度。

### 3.4 由 Park 方程导出 Xd″/Xd′/Xd

在 TH-011 §3.1 已给出 $X_d''=X_{ls}+\bigl[(1/X_{ad})+(1/X_{lf})+(1/X_{lD})\bigr]^{-1}$。其推导路径恰由 Park 方程提供：

1. **机端三相突然短路 → $v_d=v_q=v_0=0$**；
2. **磁链守恒**（超导闭合绕组 $\psi$ 不突变）给出 $t=0^+$ 时 $\psi_f,\psi_D,\psi_q$ 维持故障前值；
3. 由 Park 方程 d 轴磁链 $\psi_d=\psi_d(0)$ 守恒，反解出 $i_d$ 的强制跳变量——电流从稳态 $i_d=E_f/X_d$ 跃升到 $i_d(0)=E_f/X_d''$；
4. 三个衰减段（阻尼 $T_d''$ → 励磁 $T_d'$ → 稳态）对应阻尼绕组、励磁绕组逐步"释放磁链守恒"。

TH-011 表的"次暂态-暂态-稳态"三段衰减，本条 Park 方程是其**机理性源头**。

### 3.5 暂态电势 $E_q'$ 与功角方程的衔接

定义暂态电势 $E_q'$（凸极机引入 $E_q'$ 后忽略凸极效应的工程近似）：

$$
E_q' = \frac{\omega L_{af}}{\sqrt{3}}i_f - \omega\frac{L_d-L_d'}{\sqrt{3}}i_d
$$

满足磁链守恒 $E_q'(0^+)=E_q'(0^-)$，是单机-无限大母线暂态稳定方程的关键状态变量（详见 [TH-016 同步电机功角稳定基础](TH-016-synchronous-machine-power-angle-stability.md)）。

## 4. 与工程实践的联系

- **支撑条目 1**：[CALC-SC-002 高压短路电流计算](../40-calc/CALC-SC-002-hv-short-circuit-iec60909.md)——发电机近端短路时，初始对称短路电流 $I_k''=cU_n/(\sqrt{3}X_d'')$ 的"次暂态 → 暂态 → 稳态"衰减时段对应 IEC 60909 计算中"开断电流 $I_b$（触头分开瞬时）"与"对称短路开断电流 $I_{knc}$"的取值时刻，本条 Park 方程给出衰减时间常数 $T_d''$、$T_d'$ 的机理源头。
- **支撑条目 2**：[TH-016 同步电机功角稳定基础](TH-016-synchronous-machine-power-angle-stability.md)——派克方程线性化后给出小扰动稳定判据 $\mathrm{d}P_e/\mathrm{d}\delta>0$；暂态电势 $E_q'$ 守恒是单机-无穷大母线等面积法则的物理前提。
- **失效边界**：① Park 方程默认**理想电机假设**——气隙磁通正弦分布、忽略铁磁饱和（饱和时 $L_d$、$X_d''$ 等随电流变化，需引入饱和系数修正，见 [TH-014 磁路饱和](TH-014-magnetic-circuit-saturation.md)）；② 忽略定子瞬变电阻压降 $R_s$ 后方能解析求解大扰动，工程计算软件（PSD-BPA、PSS/E、PSCAD）保留 $R_s$ 并数值积分；③ 磁链守恒只在 $t=0^+$ 严格成立，故障后 $t>T_d''$ 时阻尼绕组已衰减，须以暂态方程重新积分；④ 仅同步电机适用——异步电机无独立励磁绕组，需用笼型等效模型。
- **下游案例**：[CASE-022 2021 短路电流与保护整定](../50-case/CASE-022-exam-short-circuit-protection.md)、[CASE-028 海上风电升压站协同](../50-case/CASE-028-composite-offshore-wind-substation.md)、[CASE-040 短路分量衰减](../50-case/CASE-040-exam-short-circuit-dc-component-breaker.md)、[CASE-048 新能源汇集站继保](../50-case/CASE-048-composite-renewable-collector-station-protection.md)、[CASE-051 距离保护越级](../50-case/CASE-051-review-distance-protection-coordination-cascade-trip.md)

## 5. 关联条目与变更记录

- 关联：[TH-011 同步电机暂态与次暂态电抗](TH-011-synchronous-machine-subtransient-reactance.md)（本条给出 Park 方程机理源头）、[TH-003 对称分量法](TH-003-symmetrical-components.md)（不对称短路时 dq0 与正/负/零序的对应关系）、[TH-014 磁路饱和](TH-014-magnetic-circuit-saturation.md)（失效边界）、[TH-016 同步电机功角稳定基础](TH-016-synchronous-machine-power-angle-stability.md)（暂态电势衔接）
- 下游案例：见 §4 列表。

| 版本 | 日期 | 修改内容 | 修改人 |
|---|---|---|---|
| 0.1 | 2026-09-09 | 创建；含 Park 变换矩阵、dq0 电压方程、转子 f/D/Q 方程、暂态电势衔接 Xd″/Xd′/Xq' 与下游案例引用 | KB 管理员 |
