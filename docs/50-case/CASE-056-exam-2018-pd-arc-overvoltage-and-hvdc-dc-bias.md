---
id: CASE-056
title: 2018供配电真题拆解：10 kV IT系统弧光接地过电压与HVDC换流站直流偏磁抑制
domain: CASE
subdomain: EX
case_type: exam
year_source: 2018
desensitized: true
voltage_levels: [MV, EHV]
lifecycle: [设计, 运维]
standards:
  - { code: GB 50057-2010, clause: "第3章", note: "建筑物防雷设计规范（过电压配合）" }
  - { code: GB/T 1094.1-2013, clause: "第4章", note: "电力变压器额定值与直流偏磁" }
  - { code: GB 50052-2009, clause: "第6章", note: "供配电系统设计规范（中性点接地）" }
  - { code: CIGRE TB 469, clause: "全文", note: "变压器直流偏磁评估与抑制" }
status: draft
reviewers: []
version: 0.1
updated: 2026-09-10
---

# 2018供配电真题拆解：弧光过电压 + HVDC 直流偏磁

## 1. 摘要

本案例拆解 2018 年度注册电气工程师（供配电）专业考试"10 kV IT 系统弧光接地过电压 + 换流站附近变压器直流偏磁"综合题。某工业园区 10 kV 配电网采用 IT 系统（中性点不接地），同时园区附近有 HVDC 换流站单极运行。考四问：IT 系统电容电流计算、消弧线圈选型、弧光重燃过电压倍数、HVDC 偏磁抑制方案。**教训：消弧线圈过补偿度选 5~10% 而非 0%、HVDC 偏磁抑制优先级从隔离→补偿→屏蔽。**

## 2. 背景

**真题出处**：2018 年度注册电气工程师（供配电）专业考试，知识单元"中性点接地方式"和"高压直流输电"交叉题。

### 2.1 系统概况

- 工业园区 10 kV 配电网：电缆 + 架空混合，总线路长度 200 km
- 电缆 100 km（0.4 μF/km），架空 100 km（0.1 μF/km）
- 采用 IT 系统（中性点不接地，传统设计）
- 园区 500 kV 变压器距 HVDC 换流站 12 km，换流站单极返回电流经大地

### 2.2 问题

1. 10 kV IT 系统对地总电容电流 $I_C$
2. 消弧线圈选型（过补偿度 $\nu = 10\%$）
3. 最恶劣弧光重燃过电压倍数，及抑制后过电压
4. HVDC 偏磁抑制方案对比

## 3. 解答

### 3.1 问题 1：对地电容电流

$$C_{\Sigma} = 3 \times (0.4 \times 100 + 0.1 \times 100) = 3 \times 50 = 150 \mu\text{F}$$

$$I_C = \sqrt{3} \times 314 \times 150 \times 10^{-6} \times 10 = \sqrt{3} \times 0.471 = 0.816 \text{ A}$$

> 注：此处用的是经典公式 $I_C = \sqrt{3} \omega C U$（U 为线电压），与 CALC-GR-001 中的简化公式一致。

### 3.2 问题 2：消弧线圈选型

要求过补偿度 $\nu = 10\%$：

$$I_L = (1 + \nu) I_C = 1.10 \times 0.816 = 0.898 \text{ A}$$

消弧线圈电感：

$$L = \frac{U_{\mathrm{ph}}}{\omega I_L} = \frac{10/\sqrt{3}}{314 \times 0.898} = \frac{5.774}{282} = 20.5 \text{ H}$$

选 **10 kV 级消弧线圈，额定电感 20 H**（可分档调整，适配未来增容）。

### 3.3 问题 3：弧光重燃过电压

**最恶劣弧光重燃倍数**：

$$k_{\max} = 3.0 \sim 3.5$$

取 $k = 3.0$，非故障相过电压：

$$U_{\mathrm{over}} = 3.0 \times \frac{10}{\sqrt{3}} \times \sqrt{2} = 3.0 \times 8.16 = 24.5 \text{ kV（峰值）}$$

10 kV 设备 BIL（雷电冲击）= 75 kV ✓ 远高于 24.5 kV。

**消弧线圈抑制后**：

$$k_{\mathrm{supp}} \leq 1.5$$

$$U_{\mathrm{over, supp}} \leq 1.5 \times 8.16 = 12.2 \text{ kV}$$

### 3.4 问题 4：HVDC 偏磁抑制方案

HVDC 换流站单极返回电流（典型 200 A 直流）经大地流动，园区 500 kV 变压器的接地中性点分流得到直流电流 $I_{dc}$：

$$I_{dc} = I_{\mathrm{return}} \times \frac{Z_{\mathrm{ground, other}}}{Z_{\mathrm{ground, transformer}} + Z_{\mathrm{ground, other}}} \approx 200 \times 0.2 = 40 \text{ A}$$

变压器铁芯面积 $A \approx 0.3 \text{ m}^2$，平均磁路 $l \approx 10$ m，匝数 $N_1 = 2000$：

$$B_{\mathrm{dc}} = \frac{\mu_0 N_1 I_{dc}}{l} = \frac{4\pi \times 10^{-7} \times 2000 \times 40}{10} = 0.010 \text{ T}$$

> 注：实际硅钢片在直流偏磁下 $\mu_r$ 会大幅变化（$\mu_r \approx 1$ 真空），此为简化估算。

**抑制方案对比**：

| 方案 | 原理 | 成本 | 效果 |
|---|---|---|---|
| **中性点串接电容器** | 阻止直流进入变压器 | 低（1~5 万） | 好，但需承受工频电流 |
| **中性点反向电流补偿** | 注入反向直流抵消偏磁 | 中（20~50 万） | 最好，实时动态 |
| **铁芯气隙分段** | 降低偏磁敏感性 | 高（影响空载损耗） | 改造已投运变压器困难 |
| **HVDC 换流站双极运行** | 从根源消除单极返回电流 | 很高（换流站改造） | 最优，但需电网调度 |

**设计推荐**：**中性点串接电容器**（投运变压器首选，改造成本最低）。

## 4. 关联

| 关联 | 说明 |
|---|---|
| [CALC-FT-001](../40-calc/CALC-FT-001-arc-ground-overvoltage-and-suppression.md) | IT 系统弧光过电压 + 消弧线圈完整设计 |
| [CALC-GR-001](../40-calc/CALC-GR-001-ground-fault-current-with-zero-sequence.md) | IT 系统电容电流计算 |
| [TH-021](../10-theory/TH-021-neutral-grounding-and-zero-sequence-network.md) | 中性点接地方式理论 |
| [TH-027](../10-theory/TH-027-hvdc-transmission-lcc-vsc.md) | HVDC 单极运行偏磁源头 |
| [TH-053](../10-theory/TH-053-transformer-dc-magnetization-and-residual-flux.md) | 变压器直流偏磁完整机理 |
