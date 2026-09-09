---
id: CASE-004
title: 综合案例：1MW/2MWh用户侧储能接入多专业协同
domain: CASE
subdomain: CP
case_type: composite
year_source: 综合设计
desensitized: true
voltage_levels: [LV, MV]
lifecycle: [规划, 设计, 验收]
standards:
  - { code: GB/T 51048-2025, clause: "全文", note: "电化学储能电站设计标准：选址、布置、系统配置、消防、安全" }
  - { code: GB/T 36547-2024, clause: "全文", note: "电化学储能电站接入电网技术规定：电能质量、保护、通信" }
  - { code: GB 44240-2024, clause: "全文", note: "电能存储系统用锂蓄电池和电池组安全要求（强制性）" }
  - { code: GB/T 42288-2022, clause: "全文", note: "电化学储能电站安全规程：运行安全、消防、热失控防护" }
  - { code: GB 38755-2019, clause: "全文", note: "电力系统安全稳定导则：三道防线、储能作为灵活性资源" }
status: draft
reviewers: []
version: 0.1
updated: 2026-09-09
---

# 综合案例：1MW/2MWh用户侧储能接入多专业协同

## 1. 摘要

本案例以某工业园区1MW/2MWh用户侧磷酸铁锂储能电站为背景，复盘容量配置→并网点选择→保护配置→电能质量校核→消防与热失控防护的多专业协同设计链路。教训：**储能接入是电力电子+保护+消防+电能质量的交叉节点，单专业设计必漏项，须按GB/T 51048-2025系统化校审。**

## 2. 背景

**工程概况**（脱敏代号：某工业园区，地址隐去）：园区新建1MW/2MWh用户侧储能电站，峰谷套利＋备用电源应用场景。数据链沿用 [PR-ES-001 储能接入设计](../30-practice/PR-ES-001-energy-storage-integration.md) §3.1 虚构综合楼数据链，天然脱敏。本案例要求完成容量配置、并网点选择、保护配置、电能质量校核、消防设计五项协同校审。

## 3. 方案

### 3.1 原设计要点

| 项目 | 设计取值 |
|---|---|
| 应用场景 | 峰谷套利＋备用电源 |
| 额定功率 | 1MW（PCS） |
| 额定容量 | 2MWh（2h放电） |
| 电池类型 | 磷酸铁锂（LFP） |
| 并网点 | 10kV中压（经升压变并网） |
| PCS | 跟网型，效率0.97 |
| 保护 | 孤岛保护＋低/过压频保护＋方向过流 |
| 消防 | 电池舱防火分隔≥2h＋七氟丙烷灭火 |

### 3.2 关键参数

| 参数 | 取值 | 来源 |
|---|---|---|
| $P_{rated}$ | 1000 kW | 设计 |
| $t_{dis}$ | 2 h | 设计 |
| $DoD$ | 0.85 | LFP常规 |
| $\eta_{PCS}$ | 0.97 | PCS参数 |
| $\eta_{bat}$ | 0.93 | 电池效率 |

## 4. 计算

### 4.1 容量配置校算（引自 [PR-ES-001](../30-practice/PR-ES-001-energy-storage-integration.md) §3.1）

$$E_{rated}=\frac{P_{rated}\cdot t_{dis}}{DoD\cdot\eta_{PCS}\cdot\eta_{bat}}=\frac{1000\times2}{0.85\times0.97\times0.93}=\frac{2000}{0.767}=2608\ \text{kWh}$$

选 2.6MWh电池簇（留裕度），放电末端可输出2MWh。

### 4.2 并网点选择

| 选项 | 适用场景 | 本例选择 |
|---|---|---|
| 低压0.4kV | <200kW，接入用户配电变低压母线 | 不适用 |
| 10kV中压 | 200kW~10MW，经升压变并网 | **本例选用** |

PCC（产权分界点）选在升压变高压侧，保护配置在PCC上游。

### 4.3 电能质量校核

PCS谐波按GB/T 14549校核（详见 [TH-008 谐波](../10-theory/TH-008-harmonic-generation.md) 与 [PR-PQ-001 无功补偿](../30-practice/PR-PQ-001-pq-compensation-design.md)）：
- 谐波电流总畸变率THD_i ≤ 3%（PCS出厂限值）
- 单次谐波电流 ≤ GB/T 14549 Table 2 限值
- 三相不平衡度 ≤ GB/T 15543-2008 限值

## 5. 审查意见

| 序号 | 意见/结论 | 不符条款 | 后果 |
|---|---|---|---|
| 1 | 传统过流保护未考虑PCS限流特性 | GB/T 36547-2024 §4 | 故障时拒动 |
| 2 | 电池舱消防须按GB 44240-2024强制校核热失控 | GB 44240-2024 全文 | 热失控蔓延 |
| 3 | 储能须参与系统稳定三道防线 | GB 38755-2019 | 系统稳定破坏 |
| 4 | 并网点PCC选在升压变低压侧（错误） | GB/T 36547-2024 | 计量与保护错位 |
| 5 | 消防联动未与园区火灾系统对接 | GB/T 42288-2022 | 火灾时孤立无援 |

## 6. 整改

### 6.1 整改措施

1. **保护配置**：配方向保护＋低电压穿越闭锁，适配PCS限流特性（[PR-PE-001](../30-practice/PR-PE-001-relay-protection-config.md)）。
2. **热失控防护**：BMS单体温度监测＋可燃气体探测器＋气体灭火＋液冷系统＋电池级注入灭火剂（详见 [PR-ES-001](../30-practice/PR-ES-001-energy-storage-integration.md) §3.3）。
3. **PCC位置**：调整至升压变高压侧，保护配置在PCC上游。
4. **系统稳定**：储能配置低频减载／高频切机参与三道防线。
5. **消防联动**：纳入园区火灾自动报警系统，联动启动灭火与疏散（[PR-CM-001](../30-practice/PR-CM-001-fire-protection-interlocking.md)）。

### 6.2 验收复查

- GB 44240-2024 热失控触发条件试验：单体热失控触发后不蔓延至相邻电池。
- 保护传动试验：PCS限流工况下方向保护正确动作。
- 消防联动模拟：可燃气体探测报警→气体灭火启动→园区消防联动启动。

## 7. 经验教训

- [ ] 储能接入须按GB/T 51048-2025系统化校审，单专业设计必漏项
- [ ] 容量配置须计入DoD/PCS效率/电池效率三重折减（$E_{rated}$ ≠ $P\times t$）
- [ ] 并网点PCC选在产权分界点，保护配置在PCC上游
- [ ] 保护配置须适配PCS限流特性，传统过流保护会拒动
- [ ] 消防与热失控防护须按GB 44240-2024强制校核，并纳入园区消防联动

## 8. 关联条目

- 上游：[PR-ES-001 储能接入设计](../30-practice/PR-ES-001-energy-storage-integration.md)·[PR-PQ-001 无功补偿](../30-practice/PR-PQ-001-pq-compensation-design.md)·[PR-CM-001 消防联动](../30-practice/PR-CM-001-fire-protection-interlocking.md)·[PR-PE-001 继电保护](../30-practice/PR-PE-001-relay-protection-config.md)·[TH-008 谐波](../10-theory/TH-008-harmonic-generation.md)
- 下游：[cn-04 新兴领域标准包](../20-standards/cn-04-新兴领域标准包.md)·[TH-014 磁路饱和](../10-theory/TH-014-magnetic-circuit-saturation.md)
- 平行：[CASE-001 负荷分级真题](CASE-001-exam-load-classification.md)（同一虚构综合楼数据链）·[CASE-003 变压器涌流事故](CASE-003-accident-transformer-inrush.md)（PCS保护与变压器保护协同）

## 9. 变更记录

| 版本 | 日期 | 修改内容 | 修改人 |
|---|---|---|---|
| 0.1 | 2026-09-09 | 创建；综合案例，数据链沿用 PR-ES-001 | KB 管理员 |
