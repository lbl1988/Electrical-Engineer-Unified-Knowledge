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

## 二期第二批成果（1 条）

| ID | 主题 | 主要标准依据 | 生命周期 | 支撑的计算/理论条目 |
|---|---|---|---|---|
| [PR-DD-002](PR-DD-002-substation-layout-and-equipment-selection.md) | 10/0.4kV 变配电所布置与设备选型 | GB 50053-2013, GB 50060-2008, DL/T 5222-2021 | 设计 | [CALC-LD-001](../40-calc/CALC-LD-001-demand-factor-method.md)·[CALC-SC-001](../40-calc/CALC-SC-001-低压三相短路电流计算.md)·[CALC-RC-001](../40-calc/CALC-RC-001-reactive-compensation.md)·[PR-DD-001](PR-DD-001-lv-breaker-selection.md) |

## 条目间引用网（示例闭环）

```
TH-003 对称分量 ─→ CALC-PT-001 两相短路灵敏度校验 ─→ PR-DD-001 断路器选型
CALC-LD-001 负荷计算 ─→ CALC-RC-001 无功补偿 ─→ PR-PQ-001 治理设计
TH-009 雷电物理 ─→ PR-GR-001 防雷分类（N=kNgAe 算例）
```

## 后续规划（二期第三批～三期）

继电保护配置与整定配合、电动机控制与启动方式、消防联动设计深化、电动汽车充电设施配置、储能接入设计、光伏并网设计。

条目编号：`PR/DD/MD/PE/BE/ES/PQ/CM-{三位序号}-{英文短名}.md`。计算类条目放 [40-calc/](../40-calc/)。
