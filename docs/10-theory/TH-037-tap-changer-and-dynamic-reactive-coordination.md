---
id: TH-037
title: 变压器有载调压与动态无功协调
domain: 基础理论
subdomain: 电压调节
voltage_levels: [LV, MV, HV]
lifecycle: [设计, 运维]
standards:
  - { code: GB/T 6451-2015, clause: "4", note: "油浸式电力变压器技术参数和要求，含 OLTC 结构" }
  - { code: DL/T 5222-2021, clause: "6", note: "导体和电器选择设计规程，有载分接开关选型" }
  - { code: DL/T 5810-2020, clause: "4", note: "电力系统电压和无功电力技术导则，OLTC 与无功补偿协调" }
  - { code: GB/T 31464-2015, clause: "5.2", note: "电网运行准则，电压无功控制策略" }
status: draft
reviewers: []
version: 0.1
updated: 2026-09-09
---

# 变压器有载调压与动态无功协调

## 1. 定义

**有载分接开关（On-Load Tap Changer, OLTC）**指变压器带电状态下切换分接头以改变变比的装置，是电网电压调节的最基础设备。**动态无功协调**指 OLTC 与无功补偿装置（电容器/电抗器/SVC/STATCOM）按预先设定的策略协同调节电压与无功，避免"电压-无功"振荡或调节冲突。

| 调节手段 | 响应速度 | 调节幅度 | 磨损 | 适用频段 |
|---|---|---|---|---|
| OLTC | 慢（30~60 s/级） | 离散（每级 1.25%~2.5%） | 机械磨损大 | 日/小时级慢调节 |
| 机械投切电容器/电抗器（MSC/MSR） | 中（数百 ms~s） | 分级 | 开关电寿命 | 15 min~小时级 |
| SVC | 快（10~20 ms） | 连续 | 低 | 秒级及以下 |
| STATCOM | 极快（ms 级） | 连续 | 低 | 暂态/动态 |

## 2. 物理图像

### 2.1 OLTC 调压机理

变压器变比 $K=U_1/U_2=N_1/N_2$，调节 $N_1$ 改变 $K$ → 二次电压 $U_2=U_1/K$ 变化。OLTC 在高压侧切换分接头，每级典型 1.25%（±8 级 × 1.25% = ±10%），总调节范围 $\pm10\%$。

```
高压侧 ─── 主绕组 ─── 调压绕组(±8 级) ─── 中性点
                              ↑
                      分接切换开关（真空/电阻式过渡）
```

过渡电阻（或真空灭弧）在切换瞬间桥接相邻分接头，限制级间环流。

### 2.2 9 区图控制策略

OLTC 与电容器/电抗器的协调常用**9 区图**——以 $U$ 为纵轴、$\cos\varphi$（或 $Q$）为横轴划分 9 个区域，每区对应不同的调节组合：

```
     U ↑
  3  │  2  │  1
  ───┼─────┼───→ Q
  6  │  0  │  7
  ───┼─────┼───
  5  │  4  │  8
```

0 区为目标区（电压与无功均在合格范围），其余各区按"先调电压后调无功"或"先调无功后调电压"策略动作。

## 3. 推导

### 3.1 OLTC 调压灵敏度

调节一级分接头（变比变化 $\Delta K/K=1.25\%$）引起的二次电压变化：

$$
\Delta U_2 = -\frac{\Delta K}{K}\cdot U_2 \approx 1.25\%\,U_2
$$

对 10 kV 母线每级约 125 V，对 110 kV 每级约 1.375 kV。

### 3.2 OLTC 与无功补偿协调方程

变压器串联阻抗 $Z_T$ 上的电压降：

$$
\Delta U = \frac{P\,R_T+Q\,X_T}{U_2}
$$

$X_T\gg R_T$（大型变压器），故 $\Delta U\approx Q\,X_T/U_2$。无功变化 $\Delta Q$ 引起电压变化：

$$
\Delta U = \frac{X_T}{U_2}\,\Delta Q
$$

| 调节方式 | $\Delta Q$ | $\Delta U$（10 kV 母线，$X_T=0.5$ Ω） | 响应时间 |
|---|---|---|---|
| OLTC 一级 | 0 | 125 V（直接调 $K$） | 30~60 s |
| 投电容器 1 Mvar | +1 Mvar | 50 V | 数百 ms~s |
| SVC 调节 | ±50 Mvar | ±2.5 kV | 10~20 ms |
| STATCOM 调节 | ±100 Mvar | ±5 kV | <5 ms |

### 3.3 动态无功协调策略

**时间尺度解耦**：OLTC 负责慢调节（小时级），补偿"缓慢趋势性"电压偏差；SVC/STATCOM 负责快调节（秒级及以下），应对暂态电压跌落与负荷波动。

**9 区图控制流程**（典型）：

1. 采样 $U_2$ 与 $Q$；
2. 判断所在区域；
3. 若在 0 区：不动；
4. 若在 1/3 区（$U$ 高）：先切电容器，仍高则降分接；
5. 若在 5/8 区（$U$ 低）：先降分接（升 $U$），仍低则投电容器；
6. 若在 2/7 区（$U$ 正常但 $Q$ 越限）：仅投切电容器；
7. 动作后延时确认（5~10 min），避免频繁调节。

### 3.4 OLTC 动作次数限制

分接开关机械寿命典型 $10^5$~$10^6$ 次，每日动作次数限制（DL/T 572）：

$$
N_{daily}\le N_{max}\quad \text{典型}\;N_{max}=20\sim30\;\text{次/日}
$$

频繁动作时须优先用无功补偿替代 OLTC，这是动态无功协调的核心约束之一。

## 4. 与工程实践的联系

- **支撑条目 1**：[PR-PQ-001 电能质量治理](../30-practice/PR-PQ-001-pq-compensation-design.md) 与 [TH-028 柔性交流输电 FACTS](TH-028-facts-flexible-ac-transmission.md)——OLTC 与 STATCOM/SVC 协调是变电站 AVC 系统的核心。
- **支撑条目 2**：[TH-020 电力系统稳定性分类](TH-020-power-system-stability-classification.md) 与 [TH-032 同步电机进相调相](TH-032-synchronous-machine-leading-and-condensing-operation.md)——发电机 AVR、OLTC、无功补偿三层协调构成电网电压-无功控制体系。
- **支撑条目 3**：[PR-DD-002 变配电所布置](../30-practice/PR-DD-002-substation-layout-and-equipment-selection.md)——OLTC 选型与变压器布置空间、分接开关检修平台相关。
- **失效边界**：① OLTC 在大负荷扰动下频繁动作（"调节振荡"），须加延时确认与动作次数闭锁；② OLTC 电压调节灵敏度受 $Z_T$ 限制，短路阻抗大的变压器每级调压效果弱；③ 分接开关故障（过渡电阻烧毁、触头磨损）是变压器事故重要原因，须定期油色谱与机械特性试验；④ OLTC 无法应对暂态电压跌落（响应太慢），须依赖 SVC/STATCOM；⑤ 大型发电机升压变压器 OLTC 一般不参与系统调压（由 AVR 承担），OLTC 主要用于配电网与联络变。
- **下游案例**：[CASE-020 油浸变压器短路起火](../50-case/CASE-020-accident-oil-transformer-fire.md)、[CASE-044 避雷器与电容器配合](../50-case/CASE-044-review-capacitor-overvoltage-spd-coordination.md)

## 5. 关联条目与变更记录

- 关联：[TH-020 电力系统稳定性分类](TH-020-power-system-stability-classification.md)（电压稳定与 PV/QV 曲线）、[TH-032 同步电机进相调相](TH-032-synchronous-machine-leading-and-condensing-operation.md)（AVR-OLTC-无功补偿三层协调）、[TH-028 FACTS](TH-028-facts-flexible-ac-transmission.md)（SVC/STATCOM 与 OLTC 解耦）、[TH-006 变压器漏抗](TH-006-transformer-leakage-impedance.md)（$Z_T$ 与调压灵敏度）、[TH-014 磁路饱和](TH-014-magnetic-circuit-saturation.md)（分接位置与铁芯饱和）、[PR-PQ-001 电能质量治理](../30-practice/PR-PQ-001-pq-compensation-design.md)、[PR-DD-002 变配电所布置](../30-practice/PR-DD-002-substation-layout-and-equipment-selection.md)
- 下游案例：见 §4 列表。

| 版本 | 日期 | 修改内容 | 修改人 |
|---|---|---|---|
| 0.1 | 2026-09-09 | 创建；含 OLTC 调压灵敏度、9 区图协调策略、时间尺度解耦、动作次数限制与调节振荡失效边界 | KB 管理员 |
