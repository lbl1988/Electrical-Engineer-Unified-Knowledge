---
id: TH-001
title: 似稳场与集总参数电路近似
domain: 基础理论
subdomain: 电磁场
voltage_levels: [LV, MV, HV]
lifecycle: [设计]
standards:
  - { code: GB/T 2900.1, clause: "", note: "电工术语 基本术语" }
status: published
reviewers: []
version: 1.0
updated: 2026-09-08
---

# 似稳场与集总参数电路近似

## 1. 定义

**似稳场（quasi-static field）**：当电磁场随时间变化足够缓慢、且所关心区域的几何尺寸远小于电磁波波长时，位移电流效应可忽略，电磁场在每一瞬间近似满足静态场的分布规律。此时电路可用**集总参数（lumped parameters）**——电阻 $R$、电感 $L$、电容 $C$——描述，基尔霍夫定律 $~$（KCL/KVL）成立。工频 50Hz 时波长 $\lambda = c/f \approx 6000$ km。

## 2. 物理图像

把交变电压施加在一根导线上：电压以光速传播，若导线长 100m，波走过全程仅需 0.33μs，而工频周期是 20ms——**在任意瞬间，全线上各点电压几乎"同涨同落"**，相位差 $2\pi \times 100/6\times10^6 \approx 0.6$ mrad，完全可以忽略。于是"线上处处同时"——这正是集总电路的直觉：一根导线可以画成电路图里一条没有尺寸的线。

## 3. 推导

由 Maxwell 方程组，全电流定律（安培-麦克斯韦定律）：

$$\nabla\times\vec{H} = \vec{J}_c + \frac{\partial\vec{D}}{\partial t}$$

其中传导电流密度 $\vec{J}_c=\sigma\vec{E}$，位移电流密度 $\partial\vec{D}/\partial t=\varepsilon\,\partial\vec{E}/\partial t$。对正弦场，两者幅值之比：

$$\frac{J_d}{J_c} = \frac{\omega\varepsilon}{\sigma} \sim \frac{2\pi f\,\varepsilon_0}{\sigma}$$

以良导体 $\sigma\sim10^7$ S/m 代入：位移电流在 $f \lesssim 10^{15}$ Hz 前均可忽略。但真正的判据来自**几何尺度**：设电路最大尺寸 $d$，场传播时间 $d/c$ 远小于变化时间尺度 $1/\omega$，即

$$d \ll \lambda = \frac{c}{f}$$

此时推迟势退化为瞬时势，场方程退化为稳态形式，KCL（节点电荷不积累）与 KVL（回路感应电势集中于"电感"元件内部）成立。

| 符号 | 含义 | 单位 |
|---|---|---|
| $\lambda$ | 波长 | m |
| $c$ | 真空光速 | m/s |
| $d$ | 电路特征尺寸 | m |
| $\vec{J}_c,\ \vec{J}_d$ | 传导/位移电流密度 | A/m² |

## 4. 与工程实践的联系

- 支撑条目：[CALC-SC-001 低压三相短路计算](../40-calc/CALC-SC-001-低压三相短路电流计算.md)（阻抗串并联叠加的全部代数运算均以似稳近似为前提）、[TH-002 相量法](TH-002-phasor-analysis.md)
- 失效边界：① **长线**：架空线数百 km（如 500km ≈ λ/12）需分布参数模型（贝杰龙法/行波）；② **高频暂态**：VFTO（GIS 隔离开关操作，ns 级）、雷电波（1.2/50μs 波头沿线传播，波阻抗概念不可回避）；③ **开关电源与 EMC**：数十 kHz~MHz 的开关谐波使 PCB/母排的"寄生电感"变成真实电抗——集总模型须扩展寄生参数。
- 工程速记：**"工频装置算电路，快速暂态算波过程"**——短路计算书不需要波阻抗，但防雷计算离不开它。

## 5. 关联条目与变更记录

- 关联：[TH-002 相量法](TH-002-phasor-analysis.md)、[TH-009 雷电物理](TH-009-lightning-physics.md)（雷电波即似稳近似失效的典型场景）

| 版本 | 日期 | 修改内容 | 修改人 |
|---|---|---|---|
| 1.0 | 2026-09-08 | 创建 | KB 管理员 |
