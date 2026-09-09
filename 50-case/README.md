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

## 案例间引用网（数据贯通闭环）

```
CALC-LD-001 综合楼负荷（P30=395.1kW） ─→ CASE-001 真题拆解 ─→ CASE-004 储能接入（同园区数据链）
PR-BE-001 应急照明（蓄电池标配）    ─→ CASE-002 校审驳回    ─→ CASE-004 消防联动协同 ─→ CASE-008 数据中心
TH-014 磁路饱和（励磁涌流）          ─→ CASE-003 事故复盘    ─→ CASE-004 PCS保护协同
PR-ES-001 储能接入（1MW/2MWh）       ─→ CASE-004 综合案例    ─→ 多专业协同校审闭环
TH-008 谐波机理（K因子法）            ─→ CASE-005 变压器降容 ─→ CASE-008 数据中心PCC校核
TH-011 开关电弧（接触电阻）            ─→ CASE-006 电缆接头事故 ─→ CASE-009 接地制式校审
TH-009 雷电物理（跨步电压）            ─→ CASE-007 避雷针真题 ─→ IEEE 80 系数法
CALC-BT-002 UPS备电（功率法）         ─→ CASE-008 数据中心2N ─→ 多专业协同
TH-005 接触/跨步（IT系统）            ─→ CASE-009 医疗2类场所 ─→ PR-GR-002 接地制式
```

## 案例子域代码（front matter `subdomain` 字段）

| 代码 | 子域 | case_type 值 | 说明 |
|---|---|---|---|
| EX | 真题拆解 | exam | 注册电气工程师历年真题，按知识单元×年份 |
| DR | 校审问题 | review | 典型设计错误与审查意见，按域分类 |
| AC | 事故复盘 | accident | 基于公开调查报告的电气事故分析 |
| CP | 综合协同 | composite | 多专业协同综合案例 |

> 子域代码仅入 front matter `subdomain`，**不嵌入文件名**（遵守 `CASE-{三位序号}-{英文短名}.md` 格式）。

## 累计统计（两批共 9 条）

| 子域 | 第一批 | 第二批 | 累计 |
|---|---|---|---|
| EX 真题 | 1（CASE-001） | 1（CASE-007） | 2 |
| DR 校审 | 1（CASE-002） | 2（CASE-005/009） | 3 |
| AC 事故 | 1（CASE-003） | 1（CASE-006） | 2 |
| CP 综合 | 1（CASE-004） | 1（CASE-008） | 2 |
| **合计** | **4** | **5** | **9** |

## 后续规划（三期续）

校审问题库扩展（按域分类累计20+条，覆盖防雷/接地/电缆/变配电所/UPS/谐波/消防各域）、事故案例扩充（变电站火灾/电击伤亡/短路爆炸/弧光过电压）、考试真题年份覆盖（2020-2026，含发输变电方向）、综合案例（光储充微电网/工业变电所/轨道交通牵引）。
