---
id: TH-031
title: 接地变压器与接地电阻选型
domain: 基础理论
subdomain: 接地系统
voltage_levels: [MV, HV]
lifecycle: [设计, 选型, 运维]
standards:
  - { code: DL/T 5222-2021, clause: "6", note: "导体和电器选择设计规程，给出接地变压器与接地电阻选型公式" }
  - { code: GB/T 50064-2014, clause: "3", note: "交流电气装置的过电压保护和绝缘配合，中性点接地电阻值" }
  - { code: DL/T 780-2020, clause: "4", note: "配电系统中性点接地电阻器技术规范" }
  - { code: GB/T 17211-1998, clause: "4", note: "干式电力变压器负荷导则（接地变常用干式）" }
status: draft
reviewers: []
version: 0.1
updated: 2026-09-09
---

# 接地变压器与接地电阻选型

## 1. 定义

**接地变压器（Grounding Transformer, 简称接地变）**指为无中性点引出的系统（如 $\triangle$ 接线变压器二次侧或纯电缆网络）提供人为中性点的装置，常见 ZNyn（曲折形）或 ZNd 联结。**中性点接地电阻（NGR, Neutral Grounding Resistor）**指接在人为中性点与地之间、限制单相接地电流的电阻器。两者组合构成 **中性点经小电阻接地系统**。

| 接地方式 | 中性点电阻 $R_N$ | 单相接地电流 | 应用 |
|---|---|---|---|
| 不接地 | $\infty$ | 电容电流 $I_C=\sqrt3\omega C_0 U_n$ | 老旧配网，$I_C<10$ A |
| 经消弧线圈 | $L$ 调谐 | 残流 $<10$ A | 20 kV 以上电缆网络 |
| 经高电阻 | $R_N > 100/I_C$ | $I_C$ 不放大 | 发电机中性点 |
| 经小电阻 | $R_N = U_\phi/I_d$ | $100\sim1000$ A | 城市配网、新能源汇集站 |

## 2. 物理图像

### 2.1 接地变 ZNyn 联结

曲折形（Zigzag）绕组每相分两半，分别绕在两个不同铁芯柱上，使零序磁通相互抵消——**零序阻抗极低**（接近漏抗），正序/负序阻抗较高。这是接地变能提供低阻抗中性点通道的物理基础。

```
          A ────┐
                │  ┌── Z 绕组 ──┐
          B ────┤  │  (分两半)  │
                │  └────────────┘
          C ────┘
                │
               N (中性点) ──── R_N ──── 地
```

正常运行时接地变仅流过励磁电流（空载），几乎不消耗有功；单相接地时中性点电压漂移至 $-\dot U_A$，零序电流 $I_0=U_\phi/Z_0$ 通过 $R_N$ 闭合回路。

### 2.2 小电阻接地系统的单相接地

单相接地时，故障点电流为电容电流与电阻电流的矢量和：

$$
\dot I_d = \dot I_C + \dot I_R = \sqrt{I_C^2+I_R^2}\cdot e^{j\phi}
$$

$R_N$ 的加入使故障电流相位偏移（从纯容性偏向阻性），且当 $R_N\le 1/(3\omega C_0)$ 时 $I_R>I_C$，故障电流主要由电阻分量主导——这使零序过流保护灵敏度大幅提高，且抑制了谐振过电压（详见 [TH-022 过电压机理](TH-022-overvoltage-mechanism-and-insulation-coordination.md)）。

## 3. 推导

### 3.1 接地电阻值选取

根据 DL/T 5222 §6，接地电阻值按限制单相接地电流至目标值 $I_d$ 设计：

$$
R_N = \frac{U_\phi}{I_d} = \frac{U_n}{\sqrt3\,I_d}
$$

| 系统电压 $U_n$ | 目标 $I_d$ | $R_N$ | 典型场景 |
|---|---|---|---|
| 10 kV | 400 A | 14.4 Ω | 城市配网 |
| 10 kV | 100 A | 57.7 Ω | 工业园区 |
| 35 kV | 300 A | 67.4 Ω | 新能源汇集站 |
| 35 kV | 1000 A | 20.2 Ω | 大型变电站 |

### 3.2 接地电阻容量（热稳定）

单相接地持续时间内电阻器须承受的热量：

$$
W_R = I_d^2\,R_N\,t\quad (t=10\sim30\,\text{s})
$$

| $I_d$ | $R_N$ | $t$ | $W_R$ | 散热方式 |
|---|---|---|---|---|
| 400 A | 14.4 Ω | 10 s | 23.0 MJ | 不锈钢栅格风冷 |
| 1000 A | 20.2 Ω | 10 s | 202 MJ | 强制风冷/水冷 |

电阻器材质常用 **铸铁/不锈钢/Cr-Al 合金**，须校核温升 $<760$ ℃（DL/T 780 §4）。

### 3.3 接地变压器容量

接地变额定容量按通过的最大零序电流选取：

$$
S_N = \sqrt3\,U_n\,I_0 = \sqrt3\,U_n\,\frac{U_\phi}{R_N+Z_0} \approx \sqrt3\,U_n\,\frac{U_\phi}{R_N} = U_n\,I_d
$$

（因 $Z_0\ll R_N$，略去 $Z_0$）。典型接地变容量为同系统主变压器容量的 $0.5\%\sim1\%$（详见 [CASE-034 中性点小电阻接地](../50-case/CASE-034-review-neutral-resistor-grounding.md)）。

### 3.4 与消弧线圈并联运行

电缆网络电容电流随线路增长而增大，消弧线圈调谐困难。可采用**消弧线圈+并联小电阻**方案：正常运行消弧线圈补偿电容电流（残流 $<10$ A），单相接地持续时若判定为永久故障则投入并联电阻加速跳闸——兼顾了瞬时故障自熄与永久故障快速隔离。

## 4. 与工程实践的联系

- **支撑条目 1**：[PR-GR-002 接地制式](../30-practice/PR-GR-002-earthing-arrangement.md) 与 [TH-021 中性点接地方式与零序网络](TH-021-neutral-grounding-and-zero-sequence-network.md)——本条给出接地变与 NGR 的选型公式，是 TH-021 "经小电阻接地"分支的工程落地。
- **支撑条目 2**：[PR-PE-001 继电保护配置](../30-practice/PR-PE-001-relay-protection-config.md)——小电阻接地使单相接地电流达数百安，零序过流保护灵敏度大幅提升，可快速选择性跳闸。
- **支撑条目 3**：[PR-DD-002 变配电所布置](../30-practice/PR-DD-002-substation-layout-and-equipment-selection.md)——接地变与 NGR 的布置空间、散热与消防须在设计阶段统筹。
- **失效边界**：① 接地变 ZNyn 联结的正序阻抗较高，不能兼做供电变压器（须另配所用变）；② $R_N$ 选择过小（$I_d>1000$ A）使接地故障近似短路，跨步电压与接触电压增大，须配合接地网设计校核（详见 [TH-005 跨步电压](TH-005-touch-step-voltage.md)）；③ 电阻器温升校核时间须与继保动作时间匹配，若保护延时超过 30 s 电阻器可能损坏；④ 消弧线圈并联电阻方案须注意投切时序，电阻投入过早会破坏消弧补偿效果；⑤ 接地变二次侧若有 yn 绕组带所用负荷，须保证零序磁通不平衡不超过 $5\%$。
- **下游案例**：[CASE-034 10kV 中性点小电阻接地](../50-case/CASE-034-review-neutral-resistor-grounding.md)、[CASE-048 新能源汇集站继保](../50-case/CASE-048-composite-renewable-collector-station-protection.md)

## 5. 关联条目与变更记录

- 关联：[TH-021 中性点接地方式与零序网络](TH-021-neutral-grounding-and-zero-sequence-network.md)（接地方式分类与零序网络）、[TH-022 过电压机理与绝缘配合](TH-022-overvoltage-mechanism-and-insulation-coordination.md)（谐振过电压抑制）、[TH-005 跨步电压与接触电压](TH-005-touch-step-voltage.md)（接地电阻与跨步电压耦合）、[TH-006 变压器漏抗](TH-006-transformer-leakage-impedance.md)（接地变零序阻抗来源）、[PR-GR-002 接地制式](../30-practice/PR-GR-002-earthing-arrangement.md)、[PR-PE-001 继电保护配置](../30-practice/PR-PE-001-relay-protection-config.md)、[PR-DD-002 变配电所布置](../30-practice/PR-DD-002-substation-layout-and-equipment-selection.md)
- 下游案例：见 §4 列表。

| 版本 | 日期 | 修改内容 | 修改人 |
|---|---|---|---|
| 0.1 | 2026-09-09 | 创建；含 ZNyn 联结零序低阻抗机理、接地电阻值选取与热稳定、接地变容量公式、消弧线圈并联电阻方案失效边界 | KB 管理员 |
