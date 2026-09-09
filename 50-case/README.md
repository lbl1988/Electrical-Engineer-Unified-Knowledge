# L4 工程案例库（50-case）

> 定位：真实/脱敏工程案例与校审问题复盘，采用 [案例类九段式变体](../00-meta/06-模板-案例类.md)（摘要→背景→方案→计算→审查意见→整改→经验教训→关联→变更）。**每个案例必须完成标准溯源与脱敏处理**。

## 三期第一批成果（4 条）

| ID | 主题 | 主要标准依据 | 案例类型 | 支撑条目 |
|---|---|---|---|---|
| [CASE-001](CASE-001-exam-load-classification.md) | 2026供配电真题拆解：综合楼负荷分级与需要系数法 | GB 50052-2009, GB 51348-2019, GB 55024-2022 | EX 真题 | [CALC-LD-001](../40-calc/CALC-LD-001-demand-factor-method.md)·[PR-PS-001](../30-practice/PR-PS-001-load-classification.md)·[CALC-RC-001](../40-calc/CALC-RC-001-reactive-compensation.md)·[60-exam](../60-exam/2026-供配电考纲初始化.md) |
| [CASE-002](CASE-002-review-emergency-lighting.md) | 校审驳回：应急照明仅配双电源未设蓄电池 | GB 51309-2018, GB 55037-2022, GB 50016-2014 | DR 校审 | [PR-BE-001](../30-practice/PR-BE-001-emergency-lighting.md)·[CALC-BT-001](../40-calc/CALC-BT-001-battery-capacity.md)·[PR-PS-001](../30-practice/PR-PS-001-load-classification.md)·[PR-CM-001](../30-practice/PR-CM-001-fire-protection-interlocking.md)·[CALC-DG-001](../40-calc/CALC-DG-001-diesel-generator-capacity.md) |
| [CASE-003](CASE-003-accident-transformer-inrush.md) | 事故复盘：10kV变压器空投涌流致差动保护误动 | GB/T 14285-2006, DL/T 587-2016, GB/T 20840-2014 | AC 事故 | [TH-014](../10-theory/TH-014-magnetic-circuit-saturation.md)·[TH-006](../10-theory/TH-006-transformer-leakage-impedance.md)·[TH-012](../10-theory/TH-012-protection-four-properties.md)·[PR-PE-001](../30-practice/PR-PE-001-relay-protection-config.md)·[CALC-SC-002](../40-calc/CALC-SC-002-hv-short-circuit-iec60909.md) |
| [CASE-004](CASE-004-composite-energy-storage.md) | 综合案例：1MW/2MWh用户侧储能接入多专业协同 | GB/T 51048-2025, GB/T 36547-2024, GB 44240-2024, GB/T 42288-2022, GB 38755-2019 | CP 综合 | [PR-ES-001](../30-practice/PR-ES-001-energy-storage-integration.md)·[PR-PQ-001](../30-practice/PR-PQ-001-pq-compensation-design.md)·[PR-CM-001](../30-practice/PR-CM-001-fire-protection-interlocking.md)·[PR-PE-001](../30-practice/PR-PE-001-relay-protection-config.md)·[TH-008](../10-theory/TH-008-harmonic-generation.md)·[TH-014](../10-theory/TH-014-magnetic-circuit-saturation.md) |

## 案例间引用网（数据贯通闭环）

```
CALC-LD-001 综合楼负荷（P30=395.1kW） ─→ CASE-001 真题拆解 ─→ CASE-004 储能接入（同园区数据链）
PR-BE-001 应急照明（蓄电池标配）    ─→ CASE-002 校审驳回    ─→ CASE-004 消防联动协同
TH-014 磁路饱和（励磁涌流）          ─→ CASE-003 事故复盘    ─→ CASE-004 PCS保护协同
PR-ES-001 储能接入（1MW/2MWh）       ─→ CASE-004 综合案例    ─→ 多专业协同校审闭环
```

## 案例子域代码（front matter `subdomain` 字段）

| 代码 | 子域 | case_type 值 | 说明 |
|---|---|---|---|
| EX | 真题拆解 | exam | 注册电气工程师历年真题，按知识单元×年份 |
| DR | 校审问题 | review | 典型设计错误与审查意见，按域分类 |
| AC | 事故复盘 | accident | 基于公开调查报告的电气事故分析 |
| CP | 综合协同 | composite | 多专业协同综合案例 |

> 子域代码仅入 front matter `subdomain`，**不嵌入文件名**（遵守 `CASE-{三位序号}-{英文短名}.md` 格式）。

## 后续规划（三期续）

校审问题库扩展（按域分类统计20+条）、事故案例扩充（变电站火灾/电击伤亡/短路爆炸）、考试真题年份覆盖（2020-2026）、综合案例（光储充微电网/数据中心供配电）。
