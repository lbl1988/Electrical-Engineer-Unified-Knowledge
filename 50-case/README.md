# L4 工程案例库（50-case）

> 定位：真实/脱敏工程案例与校审问题复盘，采用 [案例类九段式变体](../00-meta/06-模板-案例类.md)（摘要→背景→方案→计算→审查意见→整改→经验教训→关联→变更）。**每个案例必须完成标准溯源与脱敏处理**。

## 三期第一批成果（4 条）

| ID | 主题 | 主要标准依据 | 案例类型 | 支撑条目 |
|---|---|---|---|---|
| [CASE-001](CASE-001-exam-load-classification.md) | 2026供配电真题拆解：综合楼负荷分级与需要系数法 | GB 50052-2009, GB 51348-2019, GB 55024-2022 | EX 真题 | [CALC-LD-001](../40-calc/CALC-LD-001-demand-factor-method.md)·[PR-PS-001](../30-practice/PR-PS-001-load-classification.md)·[CALC-RC-001](../40-calc/CALC-RC-001-reactive-compensation.md)·[60-exam](../60-exam/2026-供配电考纲初始化.md) |
| [CASE-002](CASE-002-review-emergency-lighting.md) | 校审驳回：应急照明仅配双电源未设蓄电池 | GB 51309-2018, GB 55037-2022, GB 50016-2014 | DR 校审 | [PR-BE-001](../30-practice/PR-BE-001-emergency-lighting.md)·[CALC-BT-001](../40-calc/CALC-BT-001-battery-capacity.md)·[PR-PS-001](../30-practice/PR-PS-001-load-classification.md)·[PR-CM-001](../30-practice/PR-CM-001-fire-protection-interlocking.md)·[CALC-DG-001](../40-calc/CALC-DG-001-diesel-generator-capacity.md) |
| [CASE-003](CASE-003-accident-transformer-inrush.md) | 事故复盘：10kV变压器空投涌流致差动保护误动 | GB/T 14285-2006, DL/T 587-2016, GB/T 20840-2014 | AC 事故 | [TH-014](../10-theory/TH-014-magnetic-circuit-saturation.md)·[TH-006](../10-theory/TH-006-transformer-leakage-impedance.md)·[TH-012](../10-theory/TH-012-protection-four-properties.md)·[PR-PE-001](../30-practice/PR-PE-001-relay-protection-config.md)·[CALC-SC-002](../40-calc/CALC-SC-002-hv-short-circuit-iec60909.md) |
| [CASE-004](CASE-004-composite-energy-storage.md) | 综合案例：1MW/2MWh用户侧储能接入多专业协同 | GB/T 51048-2025, GB/T 36547-2024, GB 44240-2024, GB/T 42288-2022, GB 38755-2019 | CP 综合 | [PR-ES-001](../30-practice/PR-ES-001-energy-storage-integration.md)·[PR-PQ-001](../30-practice/PR-PQ-001-pq-compensation-design.md)·[PR-CM-001](../30-practice/PR-CM-001-fire-protection-interlocking.md)·[PR-PE-001](../30-practice/PR-PE-001-relay-protection-config.md)·[TH-008](../10-theory/TH-008-harmonic-generation.md)·[TH-014](../10-theory/TH-014-magnetic-circuit-saturation.md) |

## 三期第二批成果（5 条）

| ID | 主题 | 主要标准依据 | 案例类型 | 支撑条目 |
|---|---|---|---|---|
| [CASE-005](CASE-005-review-transformer-harmonic-derating.md) | 校审驳回：整流负荷变压器未按K因子降容 | GB/T 6451-2015, GB/T 14549-1993, GB/T 51348-2019 | DR 校审 | [TH-008](../10-theory/TH-008-harmonic-generation.md)·[CALC-HM-001](../40-calc/CALC-HM-001-harmonic-power-flow.md)·[PR-PQ-001](../30-practice/PR-PQ-001-pq-compensation-design.md)·[CALC-RC-001](../40-calc/CALC-RC-001-reactive-compensation.md) |
| [CASE-006](CASE-006-accident-cable-joint-fire.md) | 事故复盘：10kV电缆中间接头过热引发火灾 | GB 50217-2018, GB 51348-2019, GB/T 14285-2006, GB 50016-2014 | AC 事故 | [TH-011](../10-theory/TH-011-switching-arc-physics.md)·[CALC-SC-002](../40-calc/CALC-SC-002-hv-short-circuit-iec60909.md)·[CALC-PT-001](../40-calc/CALC-PT-001-protection-setting.md)·[PR-PE-001](../30-practice/PR-PE-001-relay-protection-config.md) |
| [CASE-007](CASE-007-exam-lightning-grounding.md) | 2024供配电真题拆解：独立避雷针接地与跨步电压校验 | GB/T 50065-2011, GB 50057-2010, IEEE Std 80-2013 | EX 真题 | [TH-009](../10-theory/TH-009-lightning-physics.md)·[TH-005](../10-theory/TH-005-touch-step-voltage.md)·[CALC-GR-001](../40-calc/CALC-GR-001-grounding-grid-design.md)·[PR-GR-001](../30-practice/PR-GR-001-lightning-protection-design.md)·[PR-GR-002](../30-practice/PR-GR-002-earthing-arrangement.md) |
| [CASE-008](CASE-008-composite-data-center.md) | 综合案例：A级数据中心2N供配电多专业协同 | GB 50174-2017, GB 50016-2014, GB/T 14549-1993, GB 51348-2019 | CP 综合 | [TH-008](../10-theory/TH-008-harmonic-generation.md)·[TH-012](../10-theory/TH-012-protection-four-properties.md)·[CALC-BT-002](../40-calc/CALC-BT-002-ups-battery-autonomy.md)·[CALC-HM-001](../40-calc/CALC-HM-001-harmonic-power-flow.md)·[CALC-RC-001](../40-calc/CALC-RC-001-reactive-compensation.md)·[CALC-DG-001](../40-calc/CALC-DG-001-diesel-generator-capacity.md)·[PR-BE-001](../30-practice/PR-BE-001-emergency-lighting.md) |
| [CASE-009](CASE-009-review-neutral-grounding.md) | 校审驳回：医疗2类场所误选TN-S未设IT系统 | GB 16895.24-2005, GB 51348-2019, GB/T 16895.3-2024, GB 50054-2011 | DR 校审 | [TH-005](../10-theory/TH-005-touch-step-voltage.md)·[TH-004](../10-theory/TH-004-current-effects-human-body.md)·[PR-GR-002](../30-practice/PR-GR-002-earthing-arrangement.md)·[PR-DD-001](../30-practice/PR-DD-001-lv-breaker-selection.md)·[CALC-GR-001](../40-calc/CALC-GR-001-grounding-grid-design.md) |

## 三期第三批成果（5 条）

| ID | 主题 | 主要标准依据 | 案例类型 | 支撑条目 |
|---|---|---|---|---|
| [CASE-010](CASE-010-review-pe-conductor-size.md) | 校审驳回：低压柜PE线截面未按相线截面匹配 | GB 50054-2011, GB/T 16895.3-2024, GB 51348-2019, GB 55038-2025 | DR 校审 | [TH-013](../10-theory/TH-013-switching-arc-physics.md)·[TH-005](../10-theory/TH-005-touch-step-voltage.md)·[CALC-PT-001](../40-calc/CALC-PT-001-protection-setting.md)·[CALC-SC-001](../40-calc/CALC-SC-001-低压三相短路电流计算.md)·[PR-GR-002](../30-practice/PR-GR-002-earthing-arrangement.md)·[PR-DD-001](../30-practice/PR-DD-001-lv-breaker-selection.md) |
| [CASE-011](CASE-011-accident-dc-ground-fault.md) | 事故复盘：变电站直流系统一点接地致保护误动 | DL/T 5044-2014, GB/T 14285-2006, DL/T 724-2000, DL/T 587-2016 | AC 事故 | [TH-012](../10-theory/TH-012-protection-four-properties.md)·[TH-013](../10-theory/TH-013-switching-arc-physics.md)·[CALC-PT-001](../40-calc/CALC-PT-001-protection-setting.md)·[CALC-BT-001](../40-calc/CALC-BT-001-battery-capacity.md)·[PR-PE-001](../30-practice/PR-PE-001-relay-protection-config.md) |
| [CASE-012](CASE-012-exam-cable-voltage-drop.md) | 2022供配电真题拆解：电缆截面选择与电压降校验 | GB/T 16895.6-2014, GB 50052-2009, GB/T 12325-2008, GB 51348-2019 | EX 真题 | [TH-002](../10-theory/TH-002-phasor-analysis.md)·[TH-013](../10-theory/TH-013-switching-arc-physics.md)·[CALC-CD-001](../40-calc/CALC-CD-001-cable-ampacity-correction.md)·[CALC-SC-001](../40-calc/CALC-SC-001-低压三相短路电流计算.md)·[CALC-VL-001](../40-calc/CALC-VL-001-voltage-deviation-and-loss.md)·[CALC-LD-001](../40-calc/CALC-LD-001-demand-factor-method.md) |
| [CASE-013](CASE-013-composite-pv-es-eva-microgrid.md) | 综合案例：工业园区光储充微电网协同设计 | GB 50797-2012, GB/T 51048-2025, GB/T 50966-2024, GB/T 19964-2024, GB/T 36547-2024 | CP 综合 | [TH-008](../10-theory/TH-008-harmonic-generation.md)·[TH-012](../10-theory/TH-012-protection-four-properties.md)·[TH-011](../10-theory/TH-011-synchronous-machine-subtransient-reactance.md)·[PR-ES-001](../30-practice/PR-ES-001-energy-storage-integration.md)·[PR-EV-001](../30-practice/PR-EV-001-ev-charging-infrastructure.md)·[PR-PQ-001](../30-practice/PR-PQ-001-pq-compensation-design.md)·[PR-CM-001](../30-practice/PR-CM-001-fire-protection-interlocking.md)·[PR-PS-001](../30-practice/PR-PS-001-load-classification.md) |
| [CASE-014](CASE-014-review-fire-pump-end-transfer.md) | 校审驳回：消防泵房未设末端双电源自动切换 | GB 50016-2014(2018), GB 50052-2009, GB 55024-2022, GB 51348-2019, GB 50055-2011 | DR 校审 | [TH-007](../10-theory/TH-007-induction-motor-starting.md)·[TH-012](../10-theory/TH-012-protection-four-properties.md)·[PR-PS-001](../30-practice/PR-PS-001-load-classification.md)·[CALC-DG-001](../40-calc/CALC-DG-001-diesel-generator-capacity.md)·[PR-DD-001](../30-practice/PR-DD-001-lv-breaker-selection.md)·[CALC-VL-001](../40-calc/CALC-VL-001-voltage-deviation-and-loss.md)·[PR-CM-001](../30-practice/PR-CM-001-fire-protection-interlocking.md) |

## 三期第四批成果（5 条）

| ID | 主题 | 主要标准依据 | 案例类型 | 支撑条目 |
|---|---|---|---|---|
| [CASE-015](CASE-015-review-substation-location-voltage.md) | 校审驳回：变配电所未深入负荷中心致电压降超标 | GB 50053-2013, GB 51348-2019, GB 50052-2009, GB/T 12325-2008, GB 50217-2018 | DR 校审 | [CALC-VL-001](../40-calc/CALC-VL-001-voltage-deviation-and-loss.md)·[PR-DD-002](../30-practice/PR-DD-002-substation-layout-and-equipment-selection.md) |
| [CASE-016](CASE-016-accident-arc-flash-burn.md) | 事故复盘：0.4kV低压柜带电作业电弧光短路烧伤 | GB 26859-2011, GB/T 16176-2014, GB 50054-2011, GB/T 13869-2017, IEEE 1584-2018 | AC 事故 | [TH-013](../10-theory/TH-013-switching-arc-physics.md)·[TH-004](../10-theory/TH-004-current-effects-human-body.md)·[TH-005](../10-theory/TH-005-touch-step-voltage.md)·[CALC-SC-001](../40-calc/CALC-SC-001-低压三相短路电流计算.md)·[CALC-PT-001](../40-calc/CALC-PT-001-protection-setting.md)·[PR-DD-001](../30-practice/PR-DD-001-lv-breaker-selection.md) |
| [CASE-017](CASE-017-exam-motor-starting-voltage-drop.md) | 2020供配电真题拆解：电动机启动压降校验与启动方式选择 | GB 50055-2011, GB 51348-2019, GB/T 12325-2008, GB 50052-2009, GB/T 1032-2012 | EX 真题 | [TH-007](../10-theory/TH-007-induction-motor-starting.md)·[CALC-MS-001](../40-calc/CALC-MS-001-motor-starting-voltage-drop.md)·[CALC-VL-001](../40-calc/CALC-VL-001-voltage-deviation-and-loss.md)·[CALC-SC-001](../40-calc/CALC-SC-001-低压三相短路电流计算.md)·[PR-DD-002](../30-practice/PR-DD-002-substation-layout-and-equipment-selection.md) |
| [CASE-018](CASE-018-composite-industrial-substation.md) | 综合案例：工业园区10/0.4kV变电所多专业协同设计 | GB 50053-2013, GB 50016-2014, GB 50019-2015, GB 50058-2014, GB 50217-2018, GB 50116-2013 | CP 综合 | [PR-DD-002](../30-practice/PR-DD-002-substation-layout-and-equipment-selection.md)·[PR-DD-001](../30-practice/PR-DD-001-lv-breaker-selection.md)·[CALC-LD-001](../40-calc/CALC-LD-001-demand-factor-method.md)·[CALC-DG-001](../40-calc/CALC-DG-001-diesel-generator-capacity.md)·[CALC-GR-001](../40-calc/CALC-GR-001-grounding-grid-design.md) |
| [CASE-019](CASE-019-review-cable-fire-compartmentation.md) | 校审驳回：电缆敷设跨越防火分区未做防火封堵 | GB 50016-2014(2018), GB 51348-2019, GB 50217-2018, GB 51309-2018, GB 55037-2022, GB/T 19216.21-2017 | DR 校审 | [PR-DD-001](../30-practice/PR-DD-001-lv-breaker-selection.md)·[PR-DD-002](../30-practice/PR-DD-002-substation-layout-and-equipment-selection.md)·[CALC-CD-001](../40-calc/CALC-CD-001-cable-ampacity-correction.md)·[CALC-BT-001](../40-calc/CALC-BT-001-battery-capacity.md)·[CALC-BT-002](../40-calc/CALC-BT-002-ups-battery-autonomy.md) |

## 三期第五批成果（5 条）

| ID | 主题 | 主要标准依据 | 案例类型 | 支撑条目 |
|---|---|---|---|---|
| [CASE-020](CASE-020-accident-oil-transformer-fire.md) | 事故复盘：35/10kV油浸变压器内部短路起火爆炸 | GB 50053-2013, GB 50016-2014, GB 50116-2013, GB/T 6451-2023, GB/T 7552-2017, DL/T 572-2010, GB 50229-2019 | AC 事故 | [TH-006](../10-theory/TH-006-transformer-leakage-impedance.md)·[TH-003](../10-theory/TH-003-symmetrical-components.md)·[CALC-SC-002](../40-calc/CALC-SC-002-hv-short-circuit-iec60909.md)·[PR-DD-002](../30-practice/PR-DD-002-substation-layout-and-equipment-selection.md)·[PR-CM-001](../30-practice/PR-CM-001-fire-protection-interlocking.md)·[PR-PE-001](../30-practice/PR-PE-001-relay-protection-config.md) |
| [CASE-021](CASE-021-accident-step-voltage-electrocution.md) | 事故复盘：施工现场重复接地缺失致跨步电压致死 | GB 50194-2014, JGJ 46-2024, GB 50054-2011, GB/T 50065-2011, GB/T 13869-2017, GB 26859-2011 | AC 事故 | [TH-005](../10-theory/TH-005-touch-step-voltage.md)·[TH-004](../10-theory/TH-004-current-effects-human-body.md)·[CALC-GR-001](../40-calc/CALC-GR-001-grounding-grid-design.md)·[CALC-SC-001](../40-calc/CALC-SC-001-低压三相短路电流计算.md)·[PR-PE-001](../30-practice/PR-PE-001-relay-protection-config.md) |
| [CASE-022](CASE-022-exam-short-circuit-protection.md) | 2021供配电真题拆解：短路电流计算与继电保护整定 | GB/T 15544.1-2013, DL/T 5222-2021, GB/T 14285-2023, GB 50062-2008, GB 50060-2008 | EX 真题 | [TH-011](../10-theory/TH-011-synchronous-machine-subtransient-reactance.md)·[TH-003](../10-theory/TH-003-symmetrical-components.md)·[TH-012](../10-theory/TH-012-protection-four-properties.md)·[CALC-SC-002](../40-calc/CALC-SC-002-hv-short-circuit-iec60909.md)·[CALC-PT-001](../40-calc/CALC-PT-001-protection-setting.md)·[PR-PE-001](../30-practice/PR-PE-001-relay-protection-config.md) |
| [CASE-023](CASE-023-composite-metro-traction-substation.md) | 综合案例：轨道交通直流牵引变电所多专业协同设计 | GB 50157-2013, GB/T 10411-2007, GB 51151-2016, GB 50313-2013, GB 51298-2018, IEC 62128-1-2017 | CP 综合 | [PR-DD-002](../30-practice/PR-DD-002-substation-layout-and-equipment-selection.md)·[PR-ES-001](../30-practice/PR-ES-001-energy-storage-integration.md)·[CALC-LD-001](../40-calc/CALC-LD-001-demand-factor-method.md)·[CALC-SC-002](../40-calc/CALC-SC-002-hv-short-circuit-iec60909.md)·[CALC-GR-001](../40-calc/CALC-GR-001-grounding-grid-design.md) |
| [CASE-024](CASE-024-review-lightning-grounding-spd.md) | 校审驳回：防雷接地电阻不达标与SPD配合不当 | GB 50057-2010, GB/T 21413-2015, GB/T 21414-2015, GB/T 50065-2011, GB 50343-2012, GB 51348-2019 | DR 校审 | [PR-GR-001](../30-practice/PR-GR-001-lightning-protection-design.md)·[TH-009](../10-theory/TH-009-lightning-physics.md)·[CALC-GR-001](../40-calc/CALC-GR-001-grounding-grid-design.md)·[PR-GR-002](../30-practice/PR-GR-002-earthing-arrangement.md)·[PR-CM-001](../30-practice/PR-CM-001-fire-protection-interlocking.md) |

## 三期第六批成果（5 条）

| ID | 主题 | 主要标准依据 | 案例类型 | 支撑条目 |
|---|---|---|---|---|
| [CASE-025](CASE-025-exam-reactive-compensation-harmonic-resonance.md) | 2023供配电真题拆解：并联电容器无功补偿与谐波谐振校验 | GB 50227-2017, GB/T 14549-1993, GB 51348-2019, GB 50052-2009 | EX 真题 | [CALC-RC-001](../40-calc/CALC-RC-001-reactive-compensation.md)·[TH-008](../10-theory/TH-008-harmonic-generation.md)·[CALC-HM-001](../40-calc/CALC-HM-001-harmonic-power-flow.md)·[PR-PQ-001](../30-practice/PR-PQ-001-pq-compensation-design.md) |
| [CASE-026](CASE-026-review-ups-bypass-battery-autonomy.md) | 校审驳回：A级数据中心UPS蓄电池自主时间不足与维护旁路缺失 | GB 50174-2017, GB/T 7260.3-2016, GB 51348-2019, GB 50016-2014, GB/T 19638.1-2014 | DR 校审 | [CALC-BT-002](../40-calc/CALC-BT-002-ups-battery-autonomy.md)·[CALC-BT-001](../40-calc/CALC-BT-001-battery-capacity.md)·[TH-012](../10-theory/TH-012-protection-four-properties.md)·[PR-BE-001](../30-practice/PR-BE-001-emergency-lighting.md)·[CALC-DG-001](../40-calc/CALC-DG-001-diesel-generator-capacity.md) |
| [CASE-027](CASE-027-accident-vacuum-chopping-overvoltage.md) | 事故复盘：真空断路器截流过电压致高压电动机绕组击穿 | GB 50053-2013, GB/T 18481.1-2002, DL/T 596-2021, GB 755-2019, GB/T 11024.1-2019 | AC 事故 | [TH-013](../10-theory/TH-013-switching-arc-physics.md)·[TH-007](../10-theory/TH-007-induction-motor-starting.md)·[CALC-PT-001](../40-calc/CALC-PT-001-protection-setting.md)·[PR-PE-001](../30-practice/PR-PE-001-relay-protection-config.md) |
| [CASE-028](CASE-028-composite-offshore-wind-substation.md) | 综合案例：海上风电场升压站电气-结构-海工多专业协同设计 | GB/T 19963.1-2021, NB/T 31003-2011, GB 50053-2013, GB 50229-2019, GB/T 14285-2023, GB/T 22516-2017 | CP 综合 | [TH-011](../10-theory/TH-011-synchronous-machine-subtransient-reactance.md)·[CALC-SC-002](../40-calc/CALC-SC-002-hv-short-circuit-iec60909.md)·[CALC-GR-001](../40-calc/CALC-GR-001-grounding-grid-design.md)·[PR-DD-002](../30-practice/PR-DD-002-substation-layout-and-equipment-selection.md)·[PR-PE-001](../30-practice/PR-PE-001-relay-protection-config.md)·[PR-CM-001](../30-practice/PR-CM-001-fire-protection-interlocking.md)·[PR-GR-001](../30-practice/PR-GR-001-lightning-protection-design.md) |
| [CASE-029](CASE-029-review-diesel-generator-room-ventilation.md) | 校审驳回：柴油发电机房通风散热不足与排烟系统设计不当 | GB 50053-2013, GB 50016-2014, GB 50019-2015, GB 50229-2019, GB/T 2820.5-2009, GB 50067-2014 | DR 校审 | [CALC-DG-001](../40-calc/CALC-DG-001-diesel-generator-capacity.md)·[TH-007](../10-theory/TH-007-induction-motor-starting.md)·[PR-DD-002](../30-practice/PR-DD-002-substation-layout-and-equipment-selection.md)·[PR-CM-001](../30-practice/PR-CM-001-fire-protection-interlocking.md) |

## 三期第七批成果（5 条）

| ID | 主题 | 主要标准依据 | 案例类型 | 支撑条目 |
|---|---|---|---|---|
| [CASE-030](CASE-030-exam-cable-ampacity-section.md) | 2019供配电真题拆解：10kV电缆载流量温度修正与截面选择 | GB 50217-2018, GB/T 16895.6-2014, GB/T 12706.2-2020, GB/T 15544.1-2013, GB 50052-2009 | EX 真题 | [CALC-CD-001](../40-calc/CALC-CD-001-cable-ampacity-correction.md)·[CALC-SC-002](../40-calc/CALC-SC-002-hv-short-circuit-iec60909.md)·[CALC-VL-001](../40-calc/CALC-VL-001-voltage-deviation-and-loss.md)·[PR-DD-001](../30-practice/PR-DD-001-lv-breaker-selection.md) |
| [CASE-031](CASE-031-review-dc-insulation-monitoring.md) | 校审驳回：变电所直流操作电源系统未设绝缘监测装置 | DL/T 5044-2014, GB/T 14285-2023, DL/T 724-2000, GB 50053-2013, GB/T 50065-2011 | DR 校审 | [CALC-BT-001](../40-calc/CALC-BT-001-battery-capacity.md)·[TH-012](../10-theory/TH-012-protection-four-properties.md)·[PR-PE-001](../30-practice/PR-PE-001-relay-protection-config.md) |
| [CASE-032](CASE-032-accident-cable-termination-breakdown.md) | 事故复盘：10kV交联电缆终端应力锥安装不良致击穿爆炸 | GB 50168-2018, GB 50217-2018, GB/T 12706.2-2020, DL/T 596-2021 | AC 事故 | [TH-013](../10-theory/TH-013-switching-arc-physics.md)·[CALC-SC-002](../40-calc/CALC-SC-002-hv-short-circuit-iec60909.md)·[CALC-CD-001](../40-calc/CALC-CD-001-cable-ampacity-correction.md)·[PR-PE-001](../30-practice/PR-PE-001-relay-protection-config.md) |
| [CASE-033](CASE-033-composite-energy-station-full-process.md) | 综合案例：5MW/10MWh工商业储能电站全流程设计（消防+EMS+并网保护） | GB/T 51048-2025, GB/T 36547-2024, GB 44240-2024, GB/T 42288-2022, NB/T 10988-2022, GB/T 14285-2023 | CP 综合 | [PR-ES-001](../30-practice/PR-ES-001-energy-storage-integration.md)·[CALC-SC-002](../40-calc/CALC-SC-002-hv-short-circuit-iec60909.md)·[TH-012](../10-theory/TH-012-protection-four-properties.md)·[PR-PE-001](../30-practice/PR-PE-001-relay-protection-config.md)·[PR-CM-001](../30-practice/PR-CM-001-fire-protection-interlocking.md)·[PR-PQ-001](../30-practice/PR-PQ-001-pq-compensation-design.md) |
| [CASE-034](CASE-034-review-neutral-resistor-grounding.md) | 校审驳回：10kV系统中性点经小电阻接地电阻器选型不当 | GB/T 50065-2011, GB 50052-2009, GB/T 14285-2023, DL/T 5222-2021, IEEE C62.92.2-1995 | DR 校审 | [TH-005](../10-theory/TH-005-touch-step-voltage.md)·[TH-012](../10-theory/TH-012-protection-four-properties.md)·[CALC-GR-001](../40-calc/CALC-GR-001-grounding-grid-design.md)·[PR-GR-002](../30-practice/PR-GR-002-earthing-arrangement.md)·[PR-PE-001](../30-practice/PR-PE-001-relay-protection-config.md) |

## 三期第八批成果（5 条）

| ID | 主题 | 主要标准依据 | 案例类型 | 支撑条目 |
|---|---|---|---|---|
| [CASE-035](CASE-035-exam-motor-protection-setting.md) | 2018供配电真题拆解：高压电动机保护整定与热稳定校验 | GB 50055-2011, GB/T 14285-2023, DL/T 5222-2021, GB 50062-2008 | EX 真题 | [TH-007](../10-theory/TH-007-induction-motor-starting.md)·[TH-012](../10-theory/TH-012-protection-four-properties.md)·[CALC-PT-001](../40-calc/CALC-PT-001-protection-setting.md)·[CALC-MS-002](../40-calc/CALC-MS-002-motor-temperature-rise.md)·[PR-PE-001](../30-practice/PR-PE-001-relay-protection-config.md) |
| [CASE-036](CASE-036-review-ct-polarity-differential-malfunction.md) | 校审驳回：变压器差动保护低压侧CT极性接反致空投误动 | GB/T 14285-2023, GB 50062-2008, GB 50150-2016, DL/T 587-2016 | DR 校审 | [TH-012](../10-theory/TH-012-protection-four-properties.md)·[TH-003](../10-theory/TH-003-symmetrical-components.md)·[TH-014](../10-theory/TH-014-magnetic-circuit-saturation.md)·[PR-PE-001](../30-practice/PR-PE-001-relay-protection-config.md) |
| [CASE-037](CASE-037-accident-ferroresonance-pt-burnout.md) | 事故复盘：10kV不接地系统铁磁谐振过电压致电压互感器烧毁 | GB/T 50065-2011, GB 50053-2013, GB/T 14549-1993, DL/T 620-1997 | AC 事故 | [TH-009](../10-theory/TH-009-lightning-physics.md)·[TH-013](../10-theory/TH-013-switching-arc-physics.md)·[TH-014](../10-theory/TH-014-magnetic-circuit-saturation.md)·[PR-GR-002](../30-practice/PR-GR-002-earthing-arrangement.md)·[CALC-SC-002](../40-calc/CALC-SC-002-hv-short-circuit-iec60909.md) |
| [CASE-038](CASE-038-composite-data-center-cooling-collaboration.md) | 综合案例：A级数据中心冷却系统电气-暖通-消防多专业协同设计 | GB 50174-2017, GB 50019-2015, GB 50016-2014, GB 50116-2013, GB 51348-2019 | CP 综合 | [CALC-LD-001](../40-calc/CALC-LD-001-demand-factor-method.md)·[CALC-DG-001](../40-calc/CALC-DG-001-diesel-generator-capacity.md)·[PR-PS-001](../30-practice/PR-PS-001-load-classification.md)·[PR-CM-001](../30-practice/PR-CM-001-fire-protection-interlocking.md)·[PR-DD-002](../30-practice/PR-DD-002-substation-layout-and-equipment-selection.md)·[PR-BE-001](../30-practice/PR-BE-001-emergency-lighting.md) |
| [CASE-039](CASE-039-review-ats-switching-time-mismatch.md) | 校审驳回：应急电源ATS切换时间与UPS备电时序不匹配 | GB 50052-2009, GB 51348-2019, GB 50016-2014, GB 51309-2018, GB/T 21436-2008 | DR 校审 | [CALC-BT-001](../40-calc/CALC-BT-001-battery-capacity.md)·[CALC-DG-001](../40-calc/CALC-DG-001-diesel-generator-capacity.md)·[PR-PS-001](../30-practice/PR-PS-001-load-classification.md)·[PR-BE-001](../30-practice/PR-BE-001-emergency-lighting.md)·[PR-CM-001](../30-practice/PR-CM-001-fire-protection-interlocking.md) |

## 三期第九批成果（5 条）

| ID | 主题 | 主要标准依据 | 案例类型 | 支撑条目 |
|---|---|---|---|---|
| [CASE-040](CASE-040-exam-short-circuit-dc-component-breaker.md) | 2019发输变电真题拆解：短路电流非周期分量衰减与断路器开断能力校验 | GB/T 15544.1-2013, GB 50060-2008, IEC 60909-0, DL/T 5222-2021, GB/T 11022-2020 | EX 真题 | [TH-011](../10-theory/TH-011-synchronous-machine-subtransient-reactance.md)·[CALC-SC-002](../40-calc/CALC-SC-002-hv-short-circuit-iec60909.md)·[TH-002](../10-theory/TH-002-phasor-analysis.md)·[PR-DD-001](../30-practice/PR-DD-001-lv-breaker-selection.md) |
| [CASE-041](CASE-041-review-passive-filter-detuning-harmonic-amplification.md) | 校审驳回：低压无源滤波器支路失谐致5次谐波电流放大 | GB/T 14549-1993, GB 50227-2017, GB/T 51348-2019, IEEE 519-2022, GB/T 12325-2008 | DR 校审 | [TH-008](../10-theory/TH-008-harmonic-generation.md)·[CALC-HM-001](../40-calc/CALC-HM-001-harmonic-power-flow.md)·[CALC-RC-001](../40-calc/CALC-RC-001-reactive-compensation.md)·[PR-PQ-001](../30-practice/PR-PQ-001-pq-compensation-design.md) |
| [CASE-042](CASE-042-accident-capacitor-inrush-fuse-burst.md) | 事故复盘：10kV并联电容器组合闸涌流与操作过电压致熔断器群爆 | GB 50227-2017, GB 50060-2008, GB/T 11024.1-2019, DL/T 604-2019, DL/T 5222-2021 | AC 事故 | [TH-013](../10-theory/TH-013-switching-arc-physics.md)·[TH-014](../10-theory/TH-014-magnetic-circuit-saturation.md)·[CALC-RC-001](../40-calc/CALC-RC-001-reactive-compensation.md)·[PR-PQ-001](../30-practice/PR-PQ-001-pq-compensation-design.md)·[PR-DD-002](../30-practice/PR-DD-002-substation-layout-and-equipment-selection.md) |
| [CASE-043](CASE-043-composite-pv-storage-diesel-microgrid.md) | 综合案例：光储柴微电网并离网切换多专业协同设计 | GB/T 36547-2024, GB/T 51048-2025, GB/T 50966-2024, NB/T 10988-2022, GB/T 29319-2012, GB 50016-2014 | CP 综合 | [PR-ES-001](../30-practice/PR-ES-001-energy-storage-integration.md)·[CALC-DG-001](../40-calc/CALC-DG-001-diesel-generator-capacity.md)·[CALC-LD-001](../40-calc/CALC-LD-001-demand-factor-method.md)·[TH-002](../10-theory/TH-002-phasor-analysis.md)·[TH-011](../10-theory/TH-011-synchronous-machine-subtransient-reactance.md)·[PR-CM-001](../30-practice/PR-CM-001-fire-protection-interlocking.md) |
| [CASE-044](CASE-044-review-capacitor-overvoltage-spd-coordination.md) | 校审驳回：10kV并联电容器组过电压保护与避雷器参数配合不当 | GB 50227-2017, GB/T 11032-2020, DL/T 620-1997, GB 50060-2008, GB/T 14285-2023 | DR 校审 | [TH-013](../10-theory/TH-013-switching-arc-physics.md)·[TH-009](../10-theory/TH-009-lightning-physics.md)·[CALC-RC-001](../40-calc/CALC-RC-001-reactive-compensation.md)·[PR-PQ-001](../30-practice/PR-PQ-001-pq-compensation-design.md)·[PR-DD-002](../30-practice/PR-DD-002-substation-layout-and-equipment-selection.md)·[PR-GR-001](../30-practice/PR-GR-001-lightning-protection-design.md) |

## 三期第十批成果（5 条）

| ID | 主题 | 主要标准依据 | 案例类型 | 支撑条目 |
|---|---|---|---|---|
| [CASE-045](CASE-045-exam-emergency-lighting-battery-capacity.md) | 2017供配电真题拆解：应急照明蓄电池容量与持续时间校验 | GB 51309-2018, GB 50016-2014, GB 51348-2019, GB 55037-2022, DL/T 5044-2014 | EX 真题 | [CALC-BT-001](../40-calc/CALC-BT-001-battery-capacity.md)·[PR-BE-001](../30-practice/PR-BE-001-emergency-lighting.md)·[PR-PS-001](../30-practice/PR-PS-001-load-classification.md)·[CALC-BT-002](../40-calc/CALC-BT-002-ups-battery-autonomy.md) |
| [CASE-046](CASE-046-review-dc-insurance-monitoring-capacitance-mismatch.md) | 校审驳回：变电所直流操作电源绝缘监测装置与系统对地电容不匹配致误告警 | DL/T 5044-2014, DL/T 724-2000, GB/T 14285-2023, GB 50053-2013, DL/T 1396-2014 | DR 校审 | [TH-005](../10-theory/TH-005-touch-step-voltage.md)·[TH-012](../10-theory/TH-012-protection-four-properties.md)·[CALC-BT-001](../40-calc/CALC-BT-001-battery-capacity.md)·[PR-PE-001](../30-practice/PR-PE-001-relay-protection-config.md) |
| [CASE-047](CASE-047-accident-arc-flash-protection-missing-burn.md) | 事故复盘：低压配电柜内部短路电弧光持续燃烧致检修人员严重烧伤（电弧光保护缺失） | GB 26859-2011, GB/T 13869-2017, IEEE 1584-2018, GB 50054-2011, DL/T 1507-2016 | AC 事故 | [TH-013](../10-theory/TH-013-switching-arc-physics.md)·[TH-004](../10-theory/TH-004-current-effects-human-body.md)·[CALC-SC-001](../40-calc/CALC-SC-001-低压三相短路电流计算.md)·[PR-DD-001](../30-practice/PR-DD-001-lv-breaker-selection.md)·[PR-DD-002](../30-practice/PR-DD-002-substation-layout-and-equipment-selection.md) |
| [CASE-048](CASE-048-composite-renewable-collector-station-protection.md) | 综合案例：新能源汇集站光伏+风电并网保护与电能质量多专业协同 | GB/T 19964-2024, GB/T 19963.1-2021, GB/T 14285-2023, GB/T 14549-1993, GB/T 24337-2009, GB/T 36129-2018 | CP 综合 | [TH-008](../10-theory/TH-008-harmonic-generation.md)·[TH-011](../10-theory/TH-011-synchronous-machine-subtransient-reactance.md)·[TH-012](../10-theory/TH-012-protection-four-properties.md)·[CALC-RC-001](../40-calc/CALC-RC-001-reactive-compensation.md)·[CALC-PT-001](../40-calc/CALC-PT-001-protection-setting.md)·[PR-PE-001](../30-practice/PR-PE-001-relay-protection-config.md)·[PR-PQ-001](../30-practice/PR-PQ-001-pq-compensation-design.md)·[PR-ES-001](../30-practice/PR-ES-001-energy-storage-integration.md) |
| [CASE-049](CASE-049-review-cable-joint-construction-defect.md) | 校审驳回：10kV交联电缆中间接头施工工艺缺陷致电场集中与绝缘击穿 | GB 50168-2018, GB 50217-2018, GB/T 12706.2-2020, DL/T 596-2021 | DR 校审 | [TH-013](../10-theory/TH-013-switching-arc-physics.md)·[CALC-CD-001](../40-calc/CALC-CD-001-cable-ampacity-correction.md)·[CALC-SC-002](../40-calc/CALC-SC-002-hv-short-circuit-iec60909.md)·[PR-DD-002](../30-practice/PR-DD-002-substation-layout-and-equipment-selection.md) |

## 案例间引用网（数据贯通闭环）

```
CALC-LD-001 综合楼负荷（P30=395.1kW） ─→ CASE-001 真题拆解 ─→ CASE-004 储能接入（同园区数据链）
PR-BE-001 应急照明（蓄电池标配）    ─→ CASE-002 校审驳回    ─→ CASE-004 消防联动协同 ─→ CASE-008 数据中心 ─→ CASE-014 消防泵末端切换
TH-014 磁路饱和（励磁涌流）          ─→ CASE-003 事故复盘    ─→ CASE-004 PCS保护协同
PR-ES-001 储能接入（1MW/2MWh）       ─→ CASE-004 综合案例    ─→ CASE-013 光储充微电网
TH-008 谐波机理（K因子法）            ─→ CASE-005 变压器降容 ─→ CASE-008 数据中心PCC校核 ─→ CASE-013 充电桩谐波
TH-011 开关电弧（接触电阻）            ─→ CASE-006 电缆接头事故 ─→ CASE-009 接地制式校审
TH-009 雷电物理（跨步电压）            ─→ CASE-007 避雷针真题 ─→ IEEE 80 系数法
CALC-BT-002 UPS备电（功率法）         ─→ CASE-008 数据中心2N ─→ 多专业协同
TH-005 接触/跨步（IT系统）            ─→ CASE-009 医疗2类场所 ─→ PR-GR-002 接地制式 ─→ CASE-010 PE截面
TH-013 开关电弧（短路热效应）          ─→ CASE-010 PE截面校审 ─→ CASE-012 电缆截面真题
TH-012 继保四性（直流电源波动）        ─→ CASE-011 直流接地事故 ─→ CASE-013 微电网离网切换
TH-002 相量分析（电压损失）           ─→ CASE-012 电缆电压降 ─→ CASE-014 消防泵启动电压降
CALC-DG-001 柴发容量（持续+启动）      ─→ CASE-014 消防泵柴发 ─→ CASE-008 数据中心 ─→ CASE-013 微电网 ─→ CASE-018 工业变电所
PR-DD-002 变电所布置（所址-油坑-通风） ─→ CASE-015 变电所未深入负荷中心 ─→ CASE-017 电机启动压降 ─→ CASE-018 多专业协同
TH-013 开关电弧（弧光能量）            ─→ CASE-016 低压柜电弧光短路烧伤 ─→ CASE-006 电缆接头火灾（同源电弧机理）
CALC-MS-001 电机启动压降（短路容量法） ─→ CASE-017 2020启动压降真题 ─→ CASE-014 消防泵启动压降
CALC-CD-001 电缆载流量（同桥架分隔）   ─→ CASE-019 电缆敷设防火分区 ─→ CASE-012 电缆截面真题（载流量三重校验）
GB 51309/50016 消防电缆完整性          ─→ CASE-019 防火分区校审 ─→ CASE-002 应急照明蓄电池 ─→ CASE-014 消防泵末端切换 ─→ CASE-020 油浸变压器水喷雾 ─→ CASE-023 地下变电所气体灭火
TH-006 变压器漏抗（内部短路电流）      ─→ CASE-020 油浸变压器短路起火 ─→ CASE-022 2021短路电流真题（同源阻抗归算）
TH-005/004 跨步电压+人体效应            ─→ CASE-021 施工现场跨步电压致死 ─→ CASE-016 电弧光烧伤（同源人体伤害机理）
CALC-SC-002 高压短路（c系数最大/最小） ─→ CASE-022 2021真题（双工况短路） ─→ CASE-020 变压器内部短路 ─→ CASE-023 直流牵引等效
CALC-GR-001 接地网（共用+杂散）        ─→ CASE-021 跨步电压致死 ─→ CASE-023 杂散电流防护 ─→ CASE-024 防雷共用接地
PR-GR-001 防雷分类（SPD三级配合）      ─→ CASE-024 防雷接地校审 ─→ CASE-007 避雷针接地真题（同源 IEEE 80）
PR-ES-001 储能接入（再生制动）         ─→ CASE-023 轨道交通牵引变电所 ─→ CASE-013 光储充微电网（同源再生能量回馈）
CALC-RC-001 无功补偿（功率因数法）     ─→ CASE-025 2023无功补偿真题（谐振校验） ─→ CASE-005 变压器谐波降容（同源谐波治理）
CALC-BT-002 UPS蓄电池（功率法）        ─→ CASE-026 UPS自主时间校审（Kt系数） ─→ CASE-008 数据中心2N（同源UPS备电）
TH-013 开关电弧（真空截流+重燃）       ─→ CASE-027 截流过电压致电机击穿 ─→ CASE-016 电弧光短路（同源开关瞬态）
TH-011 同步机暂态（风机变流器贡献）    ─→ CASE-028 海上风电升压站 ─→ CASE-022 2021短路真题（同源短路计算）
CALC-DG-001 柴发容量（通风散热）       ─→ CASE-029 柴发房通风排烟校审 ─→ CASE-014 消防泵柴发（同源柴发容量）
CALC-CD-001 电缆载流量（温度×并列×热阻） ─→ CASE-030 2019电缆截面真题 ─→ CASE-012 电缆电压降真题（同源电缆选型）
TH-012 继保四性（直流绝缘=可靠性基础） ─→ CASE-031 直流绝缘监测校审 ─→ CASE-011 直流接地事故（同源直流系统）
TH-013 开关电弧（电树枝+场强集中）     ─→ CASE-032 电缆终端击穿事故 ─→ CASE-006 电缆接头火灾（同源电缆附件）
PR-ES-001 储能接入（PACK级消防+EMS）    ─→ CASE-033 储能电站全流程 ─→ CASE-004 用户侧储能（同源储能扩展）
TH-005 接触/跨步（中性点接地方式）      ─→ CASE-034 小电阻接地校审 ─→ CASE-009 医疗接地制式（同源中性点接地）
CALC-PT-001 保护整定（电机速断+过负荷）  ─→ CASE-035 2018电机保护真题 ─→ CASE-017 电机启动压降真题（同源电机保护）
TH-012 继保四性（差动CT极性）            ─→ CASE-036 CT极性接反误动校审 ─→ CASE-022 差动整定真题（同源差动保护）
TH-014 磁路饱和（铁磁谐振）              ─→ CASE-037 铁磁谐振PT烧毁 ─→ CASE-003 空投涌流（同源PT/变压器非线性）
CALC-LD-001 负荷计算（冷却负荷）          ─→ CASE-038 数据中心冷却协同 ─→ CASE-008 数据中心2N（同源数据中心）
CALC-BT-001 蓄电池容量（UPS分级）        ─→ CASE-039 ATS切换时序校审 ─→ CASE-026 UPS自主时间（同源应急电源）
TH-011 同步机暂态（短路分量衰减）        ─→ CASE-040 发输变电断路器开断校验 ─→ CASE-022 2021短路真题（同源短路计算）
TH-008 谐波机理（无源滤波器调谐）        ─→ CASE-041 无源滤波器失谐校审 ─→ CASE-025 无功补偿谐振（同源谐振）
TH-013 开关电弧（电容器合闸涌流）        ─→ CASE-042 电容器组合闸涌流事故 ─→ CASE-027 真空截流过电压（同源操作过电压）
PR-ES-001 储能接入（构网型PCS）          ─→ CASE-043 光储柴微电网并离网切换 ─→ CASE-013 光储充微电网（同源微电网）
CALC-RC-001 无功补偿（电容器过电压）      ─→ CASE-044 电容器组避雷器配合校审 ─→ CASE-042 电容器涌流事故（同源电容器组）
CALC-BT-001 蓄电池容量（应急照明）        ─→ CASE-045 2017应急照明蓄电池真题 ─→ CASE-002 应急照明校审（同源应急照明）
TH-012 继保四性（直流绝缘监测）          ─→ CASE-046 直流绝缘监测误告警校审 ─→ CASE-031 直流绝缘监测（同源直流系统）
TH-013 开关电弧（电弧光能量）            ─→ CASE-047 电弧光保护缺失烧伤 ─→ CASE-016 电弧光烧伤（同源电弧光）
TH-008 谐波机理（新能源并网）            ─→ CASE-048 新能源汇集站并网保护 ─→ CASE-028 海上风电（同源新能源）
TH-013 开关电弧（电缆接头电场）          ─→ CASE-049 电缆中间接头工艺校审 ─→ CASE-032 电缆终端击穿（同源电缆附件）
```

## 案例子域代码（front matter `subdomain` 字段）

| 代码 | 子域 | case_type 值 | 说明 |
|---|---|---|---|
| EX | 真题拆解 | exam | 注册电气工程师历年真题，按知识单元×年份 |
| DR | 校审问题 | review | 典型设计错误与审查意见，按域分类 |
| AC | 事故复盘 | accident | 基于公开调查报告的电气事故分析 |
| CP | 综合协同 | composite | 多专业协同综合案例 |

> 子域代码仅入 front matter `subdomain`，**不嵌入文件名**（遵守 `CASE-{三位序号}-{英文短名}.md` 格式）。

## 累计统计（十批共 49 条）

| 子域 | 第一批 | 第二批 | 第三批 | 第四批 | 第五批 | 第六批 | 第七批 | 第八批 | 第九批 | 第十批 | 累计 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EX 真题 | 1（CASE-001） | 1（CASE-007） | 1（CASE-012） | 1（CASE-017） | 1（CASE-022） | 1（CASE-025） | 1（CASE-030） | 1（CASE-035） | 1（CASE-040） | 1（CASE-045） | 10 |
| DR 校审 | 1（CASE-002） | 2（CASE-005/009） | 2（CASE-010/014） | 2（CASE-015/019） | 1（CASE-024） | 2（CASE-026/029） | 2（CASE-031/034） | 2（CASE-036/039） | 2（CASE-041/044） | 2（CASE-046/049） | 18 |
| AC 事故 | 1（CASE-003） | 1（CASE-006） | 1（CASE-011） | 1（CASE-016） | 2（CASE-020/021） | 1（CASE-027） | 1（CASE-032） | 1（CASE-037） | 1（CASE-042） | 1（CASE-047） | 11 |
| CP 综合 | 1（CASE-004） | 1（CASE-008） | 1（CASE-013） | 1（CASE-018） | 1（CASE-023） | 1（CASE-028） | 1（CASE-033） | 1（CASE-038） | 1（CASE-043） | 1（CASE-048） | 10 |
| **合计** | **4** | **5** | **5** | **5** | **5** | **5** | **5** | **5** | **5** | **5** | **49** |

## 后续规划（三期续）

案例库累计 34 条已跨过 30 条里程碑。后续扩展方向：考试真题年份覆盖 2018/2025 含发输变电方向（短路分量衰减、派克方程、弧光过电压）、校审问题库扩电缆防火封堵/继电保护误动/应急电源切换各域、事故案例扩充铁磁谐振过电压/电容器组爆炸/直流系统短路、综合案例数据中心冷却协同/光储柴微电网/新能源汇集站。
