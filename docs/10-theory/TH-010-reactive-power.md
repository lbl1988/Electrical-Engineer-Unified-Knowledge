---
id: TH-010
title: 无功功率的物理意义与现代扩展
domain: 基础理论
subdomain: 电路/电能质量
voltage_levels: [LV, MV, HV, EHV]
lifecycle: [设计, 运维]
standards:
  - { code: GB/T 40427-2021, clause: "", note: "电力系统电压和无功电力技术导则（无功分层分区就地平衡原则）" }
  - { code: IEEE Std 1459-2010, clause: "", note: "非正弦条件下的功率定义（有效视在功率）" }
status: published
reviewers: []
version: 1.0
updated: 2026-09-08
---

# 无功功率的物理意义与现代扩展

## 1. 定义

正弦稳态下，**无功功率 $Q=UI\sin\varphi$**（单位 var）度量电路中**往返振荡、不做净功**的功率幅值：电感磁场储能与电容电场储能每 1/4 工频周期在元件与电源之间往返一次。它是**视在功率 $S=UI$ 的正交分量**（$S^2=P^2+Q^2$），占用输配电容量却不消耗能量（理想 L/C 元件）。

## 2. 物理图像

电感充电如同"向磁场这个水库抽水"，放电时水又倒回来——一个周期里抽过去多少、倒回来多少，**净用水量（有功）为零，但管径（电流）被实实在在占用**。同理电容是"电场水库"。发电机、变压器、线路的容量以电流（kVA）计价，于是"搬运不消费"的无功把宝贵的输送能力白白占走；更糟的是无功电流在线路电阻上照样发热（$\Delta P=3I^2R$）。**并联电容补偿的本质**：在负荷旁边再放一个"电场水库"，让磁场水库的水就近与电场水库对倒，不再劳烦远端电源——这就是"无功就地平衡"。

## 3. 推导

**（1）瞬时功率分解**：$u=\sqrt2U\cos\omega t$，$i=\sqrt2I\cos(\omega t-\varphi)$：

$$p(t)=UI\big[\cos\varphi+\cos(2\omega t-\varphi)\big] = \underbrace{UI\cos\varphi}_{\text{平均}=P} + \underbrace{UI\cos(2\omega t-\varphi)}_{\text{往返振荡}}$$

振荡项幅值即 $Q=UI\sin\varphi$（将 $\cos(2\omega t-\varphi)$ 展开，正交分量系数为 $UI\sin\varphi$）。

**（2）补偿容量公式**（工程核心）：负荷 $P$、$\tan\varphi_1$ 补偿至 $\tan\varphi_2$：

$$Q_C = P\,(\tan\varphi_1-\tan\varphi_2)$$

**（3）线损对功率因数的敏感性**：$I=P/(\sqrt3 U\cos\varphi)$，故

$$\Delta P = 3I^2R \propto \frac{1}{\cos^2\varphi}\quad\Rightarrow\quad \cos\varphi:0.7\to0.9,\ \ \Delta P\ 降至\ (0.7/0.9)^2\approx60\%$$

| 符号 | 含义 | 单位 |
|---|---|---|
| $Q,\ P,\ S$ | 无功/有功/视在功率 | var, W, VA |
| $\varphi$ | 功率因数角 | rad |
| $Q_C$ | 补偿容量 | kvar |

## 4. 与工程实践的联系

- 支撑条目：[CALC-RC-001 无功补偿容量计算](../40-calc/CALC-RC-001-reactive-compensation.md)（$Q_C$ 公式的完整算例＋电抗率选择）、[CALC-LD-001 负荷计算](../40-calc/CALC-LD-001-demand-factor-method.md)（功率因数从计算负荷直接推导）；[PR-PQ-001 无功补偿与谐波治理设计](../30-practice/PR-PQ-001-pq-compensation-design.md)
- 失效边界：① 传统 $Q=UI\sin\varphi$ **仅对正弦线性电路严格成立**；非正弦下出现"畸变功率 $D$"（$S^2=P^2+Q_{Budeanu}^2+D^2$，Budeanu 定义存在争议），IEEE 1459 改用**有效视在功率 $S_e$ 与非有功功率 $N$**，量化谐波造成的容量损失——APF/SVG 容量选型应采用 1459 口径；② 瞬时无功理论（赤木 p-q）支撑三相瞬时补偿的实时控制（APF/SVG 的 DSP 内核），与工频稳态无功是两个数学层次；③ 长线路/电缆的**充电功率**（对地电容发出无功，轻载抬升电压——法拉第效应/费兰蒂效应）使"补偿"方向反转：电缆网轻载时需投电抗器吸收无功；④ 电压稳定问题（$\mathrm{d}Q/\mathrm{d}V$）中无功与电压强耦合（GB/T 40427 分层分区平衡原则的系统级理由），超出本条元件级讨论。
- 工程速记：**"无功是搬运、电容就地还；功率因数每降一档、线损平方涨一档"**。

## 5. 关联条目与变更记录

- 关联：[TH-002 相量法](TH-002-phasor-analysis.md)（功率三角形的相量来源）、[TH-008 谐波机理](TH-008-harmonic-generation.md)（非正弦功率扩展的扰动源）

| 版本 | 日期 | 修改内容 | 修改人 |
|---|---|---|---|
| 1.0 | 2026-09-08 | 创建 | KB 管理员 |
