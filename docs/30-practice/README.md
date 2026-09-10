# L3 工程实践层（30-practice）

> 定位：设计、选型、施工、验收、运维的工程方法条目，采用 [九段式模板](../00-meta/03-模板-实践类九段式.md)（摘要→术语→原理公式→标准依据→要点→常见错误→完整算例→关联→变更）。
> 每条工程结论强制挂"标准号-年份＋条款号"，算例全部手工复算。

## 二期第一批成果（6 条）

| ID | 主题 | 主要标准依据 | 生命周期 | 支撑的计算/理论条目 |
|---|---|---|---|---|
| [PR-PS-001](PR-PS-001-load-classification.md) | 负荷分级与供电电源配置 | GB 51348-2019 §3, GB 50052-2009 | 设计 | [CALC-LD-001](../40-calc/CALC-LD-001-demand-factor-method.md) |
| [PR-GR-001](PR-GR-001-lightning-protection-design.md) | 建筑物防雷分类与接闪器设计 | GB 50057-2010, GB 55024-2022 | 设计 | [TH-009](../10-theory/TH-009-lightning-physics.md) |
| [PR-GR-002](PR-GR-002-earthing-arrangement.md) | 低压接地制式选择与等电位联结 | GB/T 16895.21-2020, GB 51348-2019 | 设计 | [TH-004](../10-theory/TH-004-current-effects-human-body.md)·[TH-005](../10-theory/TH-005-touch-step-voltage.md)·[CALC-SC-001](../40-calc/CALC-SC-001-低压三相短路电流计算.md) |
| [PR-DD-001](PR-DD-001-lv-breaker-selection.md) | 低压断路器选型与级间选择性 | GB/T 14048.2-2020, GB 51348-2019 | 设计, 采购 | [CALC-SC-001](../40-calc/CALC-SC-001-低压三相短路电流计算.md)·[CALC-PT-001](../40-calc/CALC-PT-001-protection-setting.md)·[TH-003](../10-theory/TH-003-symmetrical-components.md) |
| [PR-BE-001](PR-BE-001-emergency-lighting.md) | 消防应急照明和疏散指示系统设计要点 | GB 51309-2018 | 设计, 验收 | [CALC-BT-001](../40-calc/CALC-BT-001-battery-capacity.md)·[CALC-LT-001](../40-calc/CALC-LT-001-lumen-method.md) |
| [PR-PQ-001](PR-PQ-001-pq-compensation-design.md) | 无功补偿与谐波治理设计要点 | GB 51348-2019, GB/T 14549-1993 | 设计, 运维 | [CALC-RC-001](../40-calc/CALC-RC-001-reactive-compensation.md)·[CALC-LD-001](../40-calc/CALC-LD-001-demand-factor-method.md)·[TH-008](../10-theory/TH-008-harmonic-generation.md) |

## 二期第二批成果（3 条）

| ID | 主题 | 主要标准依据 | 生命周期 | 支撑的计算/理论条目 |
|---|---|---|---|---|
| [PR-DD-002](PR-DD-002-substation-layout-and-equipment-selection.md) | 10/0.4kV 变配电所布置与设备选型 | GB 50053-2013, GB 50060-2008, DL/T 5222-2021 | 设计 | [CALC-LD-001](../40-calc/CALC-LD-001-demand-factor-method.md)·[CALC-SC-001](../40-calc/CALC-SC-001-低压三相短路电流计算.md)·[CALC-RC-001](../40-calc/CALC-RC-001-reactive-compensation.md)·[PR-DD-001](PR-DD-001-lv-breaker-selection.md) |
| [PR-PE-001](PR-PE-001-relay-protection-config.md) | 电力线路与变压器继电保护配置与整定配合 | GB/T 14285-2006, DL/T 587-2016, DL/T 5222-2021, DL/T 5137-2019 | 设计, 运维 | [TH-012](../10-theory/TH-012-protection-four-properties.md)·[TH-003](../10-theory/TH-003-symmetrical-components.md)·[CALC-SC-002](../40-calc/CALC-SC-002-hv-short-circuit-iec60909.md)·[CALC-PT-001](../40-calc/CALC-PT-001-protection-setting.md)·[PR-DD-002](PR-DD-002-substation-layout-and-equipment-selection.md) |
| [PR-EV-001](PR-EV-001-ev-charging-infrastructure.md) | 电动汽车充电设施供配电与安全配置 | GB/T 50966-2024, GB/T 51313-2018, GB/T 18487.1-2023, GB 51348-2019 | 规划, 设计, 验收 | [CALC-LD-001](../40-calc/CALC-LD-001-demand-factor-method.md)·[TH-008](../10-theory/TH-008-harmonic-generation.md)·[PR-PS-001](PR-PS-001-load-classification.md)·[PR-DD-001](PR-DD-001-lv-breaker-selection.md)·[PR-GR-002](PR-GR-002-earthing-arrangement.md)·[PR-PQ-001](PR-PQ-001-pq-compensation-design.md) |

## 条目间引用网（示例闭环）

```
TH-003 对称分量 ─→ CALC-PT-001 两相短路灵敏度校验 ─→ PR-DD-001 断路器选型
CALC-LD-001 负荷计算 ─→ CALC-RC-001 无功补偿 ─→ PR-PQ-001 治理设计
TH-009 雷电物理 ─→ PR-GR-001 防雷分类（N=kNgAe 算例）
```

## 二期第三批成果（2 条）

| ID | 主题 | 主要标准依据 | 生命周期 | 支撑的计算/理论条目 |
|---|---|---|---|---|
| [PR-CM-001](PR-CM-001-fire-protection-interlocking.md) | 火灾自动报警与消防联动控制系统设计 | GB 50116-2013, GB 50166-2019, GB 55037-2022, GB 50016-2014 | 设计, 验收, 运维 | [PR-PS-001](PR-PS-001-load-classification.md)·[CALC-DG-001](../40-calc/CALC-DG-001-diesel-generator-capacity.md)·[PR-BE-001](PR-BE-001-emergency-lighting.md)·[CALC-BT-001](../40-calc/CALC-BT-001-battery-capacity.md)·[PR-GR-001](PR-GR-001-lightning-protection-design.md) |
| [PR-ES-001](PR-ES-001-energy-storage-integration.md) | 电化学储能电站接入设计 | GB/T 51048-2025, GB/T 36547-2024, GB 44240-2024, GB/T 42288-2022, GB 38755-2019 | 规划, 设计, 验收 | [cn-04](../20-standards/cn-04-新兴领域标准包.md)·[TH-008](../10-theory/TH-008-harmonic-generation.md)·[TH-014](../10-theory/TH-014-magnetic-circuit-saturation.md)·[PR-PQ-001](PR-PQ-001-pq-compensation-design.md)·[PR-EV-001](PR-EV-001-ev-charging-infrastructure.md)·[PR-PE-001](PR-PE-001-relay-protection-config.md)·[PR-CM-001](PR-CM-001-fire-protection-interlocking.md) |

## 后续规划（三期）

电动机控制与启动方式、光伏并网设计、电动汽车换电站设计、地铁牵引供电、智慧园区能管系统。

条目编号：`PR/DD/MD/PE/BE/ES/PQ/CM-{三位序号}-{英文短名}.md`。计算类条目放 [40-calc/](../40-calc/)。

## 三期第一批成果（5 条）

| ID | 主题 | 主要标准依据 | 生命周期 | 支撑的计算/理论条目 |
|---|---|---|---|---|
| [PR-PS-002](PR-PS-002-motor-control-and-starting.md) | 电动机控制与启动方式选择 | GB 50055-2011, GB 18613-2020, GB/T 15776-2023 | 设计, 采购, 验收 | [TH-033](../10-theory/TH-033-induction-motor-vfd-control-strategy.md)·[CALC-PT-001](../40-calc/CALC-PT-001-protection-setting.md)·[CALC-LD-001](../40-calc/CALC-LD-001-demand-factor-method.md)·[PR-PQ-001](PR-PQ-001-pq-compensation-design.md) |
| [PR-DD-003](PR-DD-003-cable-routing-and-installation.md) | 电缆敷设方式选择与载流量校正 | GB 50217-2018, GB 51348-2019, GB/T 42127-2022 | 设计, 施工, 验收 | [TH-025](../10-theory/TH-025-cable-thermal-field-and-ampacity.md)·[TH-019](../10-theory/TH-019-transmission-line-parameters-long-line.md)·[CALC-SC-001](../40-calc/CALC-SC-001-低压三相短路电流计算.md)·[CALC-LD-001](../40-calc/CALC-LD-001-demand-factor-method.md) |
| [PR-PS-003](PR-PS-003-ups-and-battery-design.md) | UPS 配置与蓄电池组选择 | GB/T 7260-2023, GB/T 42084-2022, GB 50172-2024, GB 50174-2017 | 设计, 采购, 验收 | [TH-010](../10-theory/TH-010-reactive-power.md)·[TH-024](../10-theory/TH-024-power-electronic-converters-and-pwm.md)·[TH-008](../10-theory/TH-008-harmonic-generation.md)·[CALC-LD-001](../40-calc/CALC-LD-001-demand-factor-method.md)·[CALC-DG-001](../40-calc/CALC-DG-001-diesel-generator-capacity.md) |
| [PR-PQ-002](PR-PQ-002-power-quality-monitoring-and-mitigation.md) | 电能质量监测系统设计与治理评估 | GB/T 15945-2008, GB/T 12325-2008, GB/T 14549-1993, GB/T 19862-2016 | 设计, 验收, 运维 | [TH-008](../10-theory/TH-008-harmonic-generation.md)·[TH-010](../10-theory/TH-010-reactive-power.md)·[TH-018](../10-theory/TH-018-instantaneous-power-pq-theory.md)·[CALC-SC-001](../40-calc/CALC-SC-001-低压三相短路电流计算.md)·[PR-PQ-001](PR-PQ-001-pq-compensation-design.md) |
| [PR-GR-003](PR-GR-003-spd-selection-and-coordination.md) | SPD 选型与级间配合设计 | GB/T 18802.1-2023, GB 50057-2010, GB 51348-2019, GB/T 33588-2020 | 设计, 验收, 运维 | [TH-022](../10-theory/TH-022-overvoltage-mechanism-and-insulation-coordination.md)·[TH-005](../10-theory/TH-005-touch-step-voltage.md)·[TH-017](../10-theory/TH-017-cable-wave-process-vfto.md)·[CALC-SC-001](../40-calc/CALC-SC-001-低压三相短路电流计算.md)·[PR-GR-001](PR-GR-001-lightning-protection-design.md)·[PR-GR-002](PR-GR-002-earthing-arrangement.md) |

## 后续规划（三期第二批）

继电保护整定配合深化、分布式电源接入设计、配电网自动化与 SCADA、变电所综合自动化系统。

## 三期第二批成果（4 条）

| ID | 主题 | 主要标准依据 | 生命周期 | 支撑的计算/理论条目 |
|---|---|---|---|---|
| [PR-PE-002](PR-PE-002-relay-protection-coordination-deepening.md) | 继电保护整定配合深化（阶梯时限/零序方向/距离保护与重合闸配合） | GB/T 14285-2006, DL/T 553-2013, DL/T 587-2016 | 设计, 运维 | [TH-012](../10-theory/TH-012-protection-four-properties.md)·[TH-003](../10-theory/TH-003-symmetrical-components.md)·[TH-030](../10-theory/TH-030-distributed-generation-protection-and-islanding-detection.md)·[TH-034](../10-theory/TH-034-transformer-inrush-current-and-differential-protection.md)·[CALC-PT-001](../40-calc/CALC-PT-001-protection-setting.md)·[CALC-SC-002](../40-calc/CALC-SC-002-hv-short-circuit-iec60909.md) |
| [PR-ES-002](PR-ES-002-distributed-generation-grid-connection.md) | 分布式电源接入配电网设计（光伏/风电/微燃机） | GB/T 36121-2018, GB/T 19964-2024, GB/T 19963-2019, GB/T 33593-2017, GB/T 40567-2021 | 规划, 设计, 验收 | [TH-041](../10-theory/TH-041-distribution-grid-high-penetration-dg-hosting-capacity.md)·[TH-030](../10-theory/TH-030-distributed-generation-protection-and-islanding-detection.md)·[TH-024](../10-theory/TH-024-power-electronic-converters-and-pwm.md)·[TH-008](../10-theory/TH-008-harmonic-generation.md)·[CALC-LD-001](../40-calc/CALC-LD-001-demand-factor-method.md)·[CALC-SC-002](../40-calc/CALC-SC-002-hv-short-circuit-iec60909.md) |
| [PR-DD-004](PR-DD-004-distribution-automation-and-scada.md) | 配电网自动化与 SCADA 系统设计 | GB/T 35695-2017, DL/T 814-2020, DL/T 721-2014, GB/T 36572-2018 | 规划, 设计, 运维 | [TH-012](../10-theory/TH-012-protection-four-properties.md)·[TH-030](../10-theory/TH-030-distributed-generation-protection-and-islanding-detection.md)·[TH-043](../10-theory/TH-043-ai-foundations-in-electrical-engineering.md)·[CALC-SC-002](../40-calc/CALC-SC-002-hv-short-circuit-iec60909.md) |
| [PR-DD-005](PR-DD-005-substation-automation-system.md) | 变电所综合自动化系统设计 | DL/T 5149-2020, DL/T 5216-2017, DL/T 860-2015, DL/T 634.5101-2020, GB/T 36049-2018 | 设计, 验收, 运维 | [TH-012](../10-theory/TH-012-protection-four-properties.md)·[TH-024](../10-theory/TH-024-power-electronic-converters-and-pwm.md)·[TH-017](../10-theory/TH-017-cable-wave-process-vfto.md)·[TH-043](../10-theory/TH-043-ai-foundations-in-electrical-engineering.md)·[CALC-SC-002](../40-calc/CALC-SC-002-hv-short-circuit-iec60909.md)·[CALC-PT-001](../40-calc/CALC-PT-001-protection-setting.md) |

## 后续规划（四期）

光伏并网深化、电动汽车换电站、地铁牵引供电、智慧园区能管系统、电力市场参与方案。
