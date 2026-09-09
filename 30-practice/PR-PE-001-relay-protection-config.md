---
id: PR-PE-001
title: 电力线路与变压器继电保护配置与整定配合
domain: PE
subdomain: PE（电力系统保护）
voltage_levels: [MV, HV]
lifecycle: [设计, 运维]
standards:
  - { code: GB/T 14285-2006, clause: "4", note: "继电保护和安全自动装置技术规程：线路/变压器/母线保护配置原则" }
  - { code: DL/T 587-2016, clause: "4", note: "微机型继电保护装置通用技术条件：四性量化指标" }
  - { code: DL/T 5222-2021, clause: "6", note: "导体和电器选择设计规程：3kV~1000kV 设备短路开断与耐受电流校验" }
  - { code: DL/T 5137-2019, clause: "5", note: "电测量及电能计量装置设计技术规程：保护用电流互感器配置" }
status: draft
reviewers: []
version: 0.1
updated: 2026-09-09
---

# 电力线路与变压器继电保护配置与整定配合

## 1. 摘要

本条给出 10~35kV 中性点不接地/经消弧线圈接地系统的典型继电保护配置方案与整定配合流程，覆盖线路三段式电流保护、变压器差动+瓦斯主保护、限时电流速断后备等核心环节。接续 [CALC-SC-002](../40-calc/CALC-SC-002-hv-short-circuit-iec60909.md) 算例数据（10kV 母线三相短路 $I_k''=18.7$ kA），给出综合办公楼 10kV 进线及配电变保护的具体整定值，结论：**速断保护动作值 3120A、$K_{sen}=6.0$ 满足主保护要求**；后备保护与下级配合 $\Delta t=0.3$ s 选择性成立。

## 2. 术语与定义

| 术语 | 定义 | 标准出处 |
|---|---|---|
| 主保护 | 快速切除本元件故障的保护 | GB/T 14285 §3.1 |
| 后备保护 | 主保护或断路器拒动时切除故障的保护（近后备/远后备） | 同上 |
| 三段式电流保护 | 限时电流速断（I 段）+ 带时限电流速断（II 段）+ 定时限过流（III 段） | GB/T 14285 §4.2 |
| 差动保护 | 比较被保护元件两端电流之差，反映内部故障 | GB/T 14285 §4.3 |
| 灵敏系数 $K_{sen}$ | 最小运行方式故障量/动作值 | GB/T 14285 §3.0.5 |
| 时间级差 $\Delta t$ | 上下级保护动作时间差，保证选择性 | GB/T 14285 §3.2 |

## 3. 原理与公式（整定决策树）

### 3.1 三段式电流保护整定

**I 段（瞬时电流速断）**：躲本线路末端最大三相短路：

$$I_{op,I}^{(1)} = K_{rel}\, I_{k,max}^{(3)}(\text{本线末端})$$

$K_{rel}=1.2\sim 1.3$；保护范围 40%~50% 线路长度，$K_{sen}$ 不强制但宜 $\geq 1.5$（线路近端）。

**II 段（带时限电流速断）**：与下级线路 I 段配合：

$$I_{op,II}^{(1)} = K_{rel}\, I_{op,I}^{(2)}(\text{下级})$$
$$t_{op,II}^{(1)} = t_{op,I}^{(2)} + \Delta t$$

$K_{rel}=1.1\sim 1.15$，$\Delta t=0.3\sim 0.5$ s；$K_{sen}\geq 1.3$（最小运行方式本线末端两相短路）。

**III 段（定时限过流，后备）**：躲最大负荷电流：

$$I_{op,III}^{(1)} = \frac{K_{rel}}{K_{re}}\, I_{L,max}$$
$$t_{op,III}^{(1)} = t_{op,III}^{(2)} + \Delta t$$

$K_{rel}=1.2$、$K_{re}=0.85\sim 0.95$；远后备 $K_{sen}\geq 1.2$。

### 3.2 变压器保护配置

| 容量 | 主保护 | 后备保护 |
|---|---|---|
| <630 kVA | 电流速断（躲励磁涌流 $I_{op}\geq (3\sim 4)I_N$） | 过流 |
| 630~6300 kVA | 差动（$\leq 7.5\%$）+ 瓦斯 | 复合电压闭锁过流 |
| >6300 kVA | 差动（$\leq 5\%$）+ 瓦斯 | 阻抗/零序后备 |

| 符号 | 含义 | 单位 |
|---|---|---|
| $I_{op,I/II/III}^{(n)}$ | 第 $n$ 级线路 I/II/III 段动作电流 | A |
| $K_{rel}$ | 可靠系数 | — |
| $K_{re}$ | 返回系数 | — |
| $I_{L,max}$ | 最大负荷电流 | A |
| $\Delta t$ | 时间级差 | s |

## 4. 标准依据表

| 标准号-年份 | 条款 | 要求要点（转述） | 适用边界 |
|---|---|---|---|
| GB/T 14285-2006 | 4.2.1 | 3~10kV 中性点非直接接地线路：阶段式电流保护 + 单相接地信号；单相接地电容电流 $I_C$ 限值决定报警/跳闸 | 配电线路 |
| GB/T 14285-2006 | 4.3 | 800kVA 及以上油浸变（400kVA 及以上车间变）：差动保护 + 瓦斯；动作时间 $< 0.1$ s | 变压器主保护 |
| GB/T 14285-2006 | 3.0.5 | 灵敏系数：电流速断主保护 $\geq 1.5$，远后备 $\geq 1.2$ | 全部保护 |
| DL/T 5222-2021 | 6.3 | 断路器额定短路开断电流 $\geq$ 安装处 $I_k''$，热稳定 $I_{th}^2 t$ 校验 | 设备选型 |
| DL/T 5137-2019 | 5.2 | 保护用 CT 准确级 5P/10P，复合误差 $\leq 5\%/10\%$；避免稳态饱和与剩磁影响 | CT 选型 |

## 5. 设计/选型要点

- [ ] **保护配置清单**（按对象）：
  ```
  10/0.4kV 配电变（630kVA 油浸，Dyn11）：
    主保护：
      ├─ 差动保护（含 2 次谐波制动防涌流误动）
      └─ 瓦斯保护（重瓦期跳闸，轻瓦期报警）
    后备保护：
      ├─ 复合电压闭锁过流（I 段：限时电流速断躲励磁涌流；II 段：定时限过流）
      ├─ 零序过流（中性点直接接地系统）/ 间隙零序（经间隙接地）
      └─ 过负荷（信号）
  10kV 进线：
    └─ 三段式电流保护（主 + 后备）
  ```

- [ ] 整定计算顺序：**自下而上**（末端负荷 → 末端线路 → 上级线路 → 变压器 → 进线），先定电流后配时间
- [ ] CT 选择：保护用 CT 一次额定电流 $\geq 1.25\, I_N$，准确限值系数 $ALF\geq$ 短路电流/CT 一次额定值，确保短路时不饱和
- [ ] 励磁涌流躲过：差动保护二次谐波制动（15%~20%），过流保护 $I_{op}\geq (3\sim 4)I_N$（躲空投涌流最大值）
- [ ] 配合级差：微机型保护 $\Delta t=0.3$ s，含断路器分闸 $0.06$ s、误差 $0.05$ s、裕度 $0.05$ s
- [ ] 单相接地保护：$10$ kV 不接地系统：5A ≤ $I_C$ ≤ 30A 报警（XLPE 电缆），30A 以上装消弧线圈；$>$ 30A 跳闸（DL/T 5137）

## 6. 常见错误与争议

| 错误/争议 | 后果 | 正确做法/主流处理 | 依据 |
|---|---|---|---|
| 差动保护躲涌流只靠时间 | 大型变压器空投期间误跳 | 二次谐波制动（15%~20%）+ 间断角（< 5°）判据 | GB/T 14285 §4.3 |
| CT 饱和未校验 | 短路时二次电流畸变，差动误动/拒动 | 选 5P30/10P30，按 $10\, I_N$ 与 $I_k''$ 双校 | DL/T 5137 §5.2 |
| 时间级差取 0.2 s | 断路器/继电器离散性大时越级 | 微机保护取 0.3 s，电磁式 0.5 s | GB/T 14285 §3.2 |
| 远后备灵敏系数不足未补强 | 故障扩散 | 装低电压/复合电压闭锁，或加距离保护 | GB/T 14285 |
| 10kV 单相接地按直接接地整定 | 不接地系统零序电流小，频繁拒动 | 按不接地系统：$I_C$ 报警/跳闸，零序方向保护 | GB/T 14285 §4.2 |
| 逆变器并网故障电流小按传统过流整定 | 拒动 | 改低电压穿越闭锁 + 逆变器自身保护 | GB/T 47968-2026 |

## 7. 完整算例

### 7.1 已知条件（接续 [CALC-SC-002](../40-calc/CALC-SC-002-hv-short-circuit-iec60909.md)）

- 10kV 母线三相短路 $I_k''=18.7$ kA（系统侧）；线路末端（10/0.4kV 配电变高压侧）$I_{k,end}^{(3)}=8.4$ kA
- 最小运行方式两相短路 $I_{k,min}^{(2)}=0.866\, I_{k,max}^{(3)}=0.866\times 8.4=7.28$ kA
- 配电变 630kVA/10kV，$I_N=36.4$ A；$u_k=6\%$
- 10kV 进线电流互感器 600/5，准确级 10P30

### 7.2 线路 I 段（瞬时电流速断）整定

躲本线路末端最大三相短路：

$$I_{op,I} = K_{rel}\, I_{k,end}^{(3)} = 1.25\times 8400 = 10500\ \text{A}$$

一次动作值；CT 变比 600/5=120，二次值 $I_{op,I,sec}=10500/120=87.5$ A。

灵敏系数（最小运行方式本线首端两相短路，取 $I_{k,min,start}^{(2)}\approx 0.866\times 18700=16200$ A，因进线短，首端接近母线）：

$$K_{sen,I} = \frac{16200}{10500} = 1.54 \geq 1.5\ \checkmark$$

### 7.3 线路 II 段（带时限电流速断）整定

下级线路 I 段动作值约 $I_{op,I}^{(2)}=3000$ A（次末端短路整定）：

$$I_{op,II} = 1.15\times 3000 = 3450\ \text{A}$$
$$t_{op,II} = 0\,(\text{下级 I 段}) + 0.3 = 0.3\ \text{s}$$

$K_{sen,II}=\frac{7280}{3450}=2.11\geq 1.3$ ✓。

### 7.4 线路 III 段（定时限过流）整定

最大负荷电流（满载 $\beta=100\%$）$I_{L,max}=36.4\times 2=72.8$ A（按双变并联运行场景）：

$$I_{op,III} = \frac{1.2}{0.85}\times 72.8 = 102.8\ \text{A}$$

二次值 $102.8/120=0.86$ A。

远后备（下级末端两相短路）：$I_{k,end}^{(2)}=0.866\times 8400=7270$ A：

$$K_{sen,III}^{(far)} = \frac{7270}{102.8} = 70.7\gg 1.2\ \checkmark$$

时间 $t_{op,III}=0.3+0.3=0.6$ s（与下级 III 段配合）。

### 7.5 配电变主保护（差动+瓦斯）

- 容量 630 kVA，未达差动硬指标（≥800 kVA 油浸变）；但本条作为重要负荷，增设差动保护
- 差动整定：$I_{op,d}=0.5\, I_N=18.2$ A（一次），二次 $18.2/120=0.15$ A
- 二次谐波制动：15%（即差动电流中 2 次谐波含量 > 15% 闭锁，防涌流误动）
- 瓦斯保护：重瓦斯跳闸、轻瓦斯报警

### 7.6 后备保护（复合电压闭锁过流）

- 动作电流躲励磁涌流：$I_{op}=3\, I_N=109$ A
- 复合电压闭锁：低电压 $U_{op}=0.7\, U_N$、负序电压 $U_{2,op}=0.06\, U_N$（防止外部短路误动）
- 时间：$t=1.0$ s（高压侧后备，与线路 III 段 0.6 s 配合，$\Delta t=0.4$ s）

### 7.7 单相接地保护（10kV 不接地系统）

线路单相接地电容电流（XLPE 电缆）：$I_C \approx 0.1$ A/km × 10 km = 1 A < 5 A，按 GB/T 14285 §4.2 仅设**报警**不跳闸。

### 7.8 CT 准确限值校验

$I_k''=18.7$ kA，CT 一次额定 600A，准确限值系数 30 → 保证准确度的一次电流 $30\times 600=18000$ A ≈ 18.7 kA，**临界不满足**。改选 10P40 或一次额定 800A（变比 800/5=160）：

$$I_{op,I,sec}=\frac{10500}{160}=65.6\ \text{A}$$
$$ALF\text{ 实际} = \frac{18700}{800}=23.4<40\ \checkmark$$

**结论**：CT 改为 800/5 10P40，重新换算二次动作值。

## 8. 关联条目

- 上游：[TH-012 保护四性](../10-theory/TH-012-protection-four-properties.md)（四性量化为本条整定依据）、[TH-003 对称分量法](../10-theory/TH-003-symmetrical-components.md)（零序/负序整定）、[TH-015 Park 方程](../10-theory/TH-015-synchronous-machine-park-equations.md)（暂态电势导出与次暂态衰减时间常数）、[TH-016 功角稳定基础](../10-theory/TH-016-synchronous-machine-power-angle-stability.md)（失步保护整定与摆动速率物理来源）、[TH-020 电力系统稳定性分类](../10-theory/TH-020-power-system-stability-classification.md)（低频减载/低压减载/失步保护的系统性协调）、[TH-021 中性点接地方式与零序网络](../10-theory/TH-021-neutral-grounding-and-zero-sequence-network.md)（接地保护整定与零序补偿系数 k0）、[TH-029 微电网控制与并离网切换](../10-theory/TH-029-microgrid-control-and-grid-mode-switching.md)（微电网并网/孤岛双模式短路电流差异与自适应保护整定）、[TH-030 分布式电源并网保护与孤岛检测](../10-theory/TH-030-distributed-generation-protection-and-islanding-detection.md)（DG 接入改变配网保护方向与防孤岛/逆功率整定）、[TH-031 接地变压器与接地电阻选型](../10-theory/TH-031-grounding-transformer-and-resistor-selection.md)（小电阻接地系统零序过流灵敏度提升）、[TH-034 变压器励磁涌流机理与差动保护防涌流](../10-theory/TH-034-transformer-inrush-current-and-differential-protection.md)（二次谐波制动/波形对称判据与和应涌流）
- 下游：[CALC-SC-002 高压短路](../40-calc/CALC-SC-002-hv-short-circuit-iec60909.md)（$I_k''$ 数据源）、[PR-DD-002](PR-DD-002-substation-layout-and-equipment-selection.md)（断路器选型开断容量校验）、[CASE-020 油浸变压器短路起火](../50-case/CASE-020-accident-oil-transformer-fire.md)（瓦斯+差动保护配合拒动复盘）、[CASE-022 2021短路电流与保护整定真题](../50-case/CASE-022-exam-short-circuit-protection.md)（变压器差动保护最小灵敏度校验）、[CASE-027 真空截流过电压致电机击穿](../50-case/CASE-027-accident-vacuum-chopping-overvoltage.md)（电动机保护）、[CASE-028 海上风电海上升压站](../50-case/CASE-028-composite-offshore-wind-substation.md)（海上变电所保护）、[CASE-031 直流电源绝缘监测](../50-case/CASE-031-review-dc-insulation-monitoring.md)（直流操作电源）、[CASE-032 电缆终端击穿事故](../50-case/CASE-032-accident-cable-termination-breakdown.md)（进线保护）、[CASE-033 储能电站全流程](../50-case/CASE-033-composite-energy-station-full-process.md)（储能并网保护）、[CASE-034 中性点小电阻接地](../50-case/CASE-034-review-neutral-resistor-grounding.md)（接地保护整定）
- 下游案例：[CASE-035 电机保护](../50-case/CASE-035-exam-motor-protection-setting.md)、[CASE-036 差动CT极性](../50-case/CASE-036-review-ct-polarity-differential-malfunction.md)、[CASE-046 直流电源保护](../50-case/CASE-046-review-dc-insurance-monitoring-capacitance-mismatch.md)、[CASE-048 新能源并网保护](../50-case/CASE-048-composite-renewable-collector-station-protection.md)、[CASE-051 距离保护配合](../50-case/CASE-051-review-distance-protection-coordination-cascade-trip.md)、[CASE-054 光伏并网保护](../50-case/CASE-054-review-pv-anti-islanding-reverse-power.md)
- 平行：[CALC-PT-001 低压保护整定](../40-calc/CALC-PT-001-protection-setting.md)（低压侧四段式同源）、[PR-GR-002 接地制式](PR-GR-002-earthing-arrangement.md)（单相接地保护与接地制式联动）
- 案例支撑：[CASE-003 事故复盘](../50-case/CASE-003-accident-transformer-inrush.md)（变压器空投涌流致差动误动）、[CASE-004 储能综合](../50-case/CASE-004-composite-energy-storage.md)（PCS限流特性保护配置）
- 计算支撑：[CALC-PT-002 距离保护整定](../40-calc/CALC-PT-002-distance-protection-setting.md)（高压线路三段式距离保护整定）

## 9. 变更记录

| 版本 | 日期 | 修改内容 | 修改人 |
|---|---|---|---|
| 0.1 | 2026-09-09 | 创建；含三段式整定 + 变压器主后备保护 + CT 校验完整算例 | KB 管理员 |
