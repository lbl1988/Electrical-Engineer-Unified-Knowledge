---
id: TH-002
title: 相量法与正弦稳态分析
domain: 基础理论
subdomain: 电路
voltage_levels: [LV, MV, HV, EHV]
lifecycle: [设计]
standards: []
status: published
reviewers: []
version: 1.0
updated: 2026-09-08
---

# 相量法与正弦稳态分析

## 1. 定义

**相量（phasor）**：表征正弦量幅值与初相位的复常数。对正弦电压 $u(t)=U_m\cos(\omega t+\varphi_u)$，定义相量 $\dot{U}=U\,e^{j\varphi_u}$（$U$ 为有效值）。相量法将线性时不变电路在正弦激励下的**微分方程特解问题转化为复数代数方程问题**：$\mathrm{d}/\mathrm{d}t \to j\omega$。

## 2. 物理图像

复平面上一个长度为 $U$ 的箭头以角速度 $\omega$ 逆时针旋转，它在实轴上的投影就是正弦电压——**正弦量＝旋转相量的投影**。稳态分析中所有量旋转速度相同，可以"冻结"这张动画只比较初始位置（相位差）。电阻上的电压电流同相位（箭头同向），电感上电压超前电流 90°（电压箭头提前 1/4 圈），电容上落后 90°——复数 $j$ 正是"旋转 90°"的代数化身。

## 3. 推导

由欧拉公式：

$$u(t) = U_m\cos(\omega t+\varphi) = \mathrm{Re}\left[U_m e^{j(\omega t+\varphi)}\right] = \mathrm{Re}\left[\sqrt{2}\,\dot{U}\,e^{j\omega t}\right]$$

对电感 $u_L = L\,\mathrm{d}i/\mathrm{d}t$，代入复数表示：

$$\dot{U}_L = j\omega L\,\dot{I} \quad\Rightarrow\quad X_L=\omega L,\ \angle\dot U_L = \angle\dot I + 90^\circ$$

同理 $\dot{U}_C = \dot{I}/(j\omega C)$，$X_C=1/\omega C$。KVL/KCL 对相量逐项成立（线性和的实部＝实部的和）。定义复阻抗 $Z=R+jX$，全部直流电路的串并联/戴维南定理照搬复数化。

**功率**：$\dot S=\dot U\dot I^*=P+jQ$，$P=UI\cos\varphi$（有功），$Q=UI\sin\varphi$（无功）。

| 符号 | 含义 | 单位 |
|---|---|---|
| $\dot{U},\ \dot{I}$ | 电压/电流相量（有效值） | V, A |
| $X_L,\ X_C$ | 感抗/容抗 | Ω |
| $\varphi$ | 阻抗角（电压超前电流角） | rad |
| $P,\ Q,\ S$ | 有功/无功/视在功率 | W, var, VA |

## 4. 与工程实践的联系

- 支撑条目：[CALC-SC-001 短路计算](../40-calc/CALC-SC-001-低压三相短路电流计算.md)（$Z_k=R_k+jX_k$ 的复数合成）、[CALC-RC-001 无功补偿](../40-calc/CALC-RC-001-reactive-compensation.md)（功率三角形 $\tan\varphi=Q/P$ 直接决定补偿容量）、[CALC-LD-001 负荷计算](../40-calc/CALC-LD-001-demand-factor-method.md)
- 失效边界：① 仅适用于**线性时不变电路的正弦稳态**；非线性元件（整流器、磁饱和变压器励磁电流）产生谐波，须先做傅里叶分解再**逐次谐波**用相量法（见 [TH-008 谐波机理](TH-008-harmonic-generation.md)）；② 暂态过程（短路后最初的直流偏移、电机启动）需要时域或拉普拉斯方法，相量法只描述稳态分量；③ 相量法默认单一频率，间谐波/次同步振荡需多频率叠加分析。
- 工程速记：**"R 同相、L 超前 90°、C 滞后 90°；抄计算书先看 X/R"**。

## 5. 关联条目与变更记录

- 关联：[TH-001 似稳近似](TH-001-quasi-static-approximation.md)（相量法成立的空间前提）、[TH-010 无功功率](TH-010-reactive-power.md)（功率三角形相量来源）
- 下游案例：[CASE-040 断路器同期](../50-case/CASE-040-exam-short-circuit-dc-component-breaker.md)、[CASE-043 微电网同期合闸](../50-case/CASE-043-composite-pv-storage-diesel-microgrid.md)

| 版本 | 日期 | 修改内容 | 修改人 |
|---|---|---|---|
| 1.0 | 2026-09-08 | 创建 | KB 管理员 |
