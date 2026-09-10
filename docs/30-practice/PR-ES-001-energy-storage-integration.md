---
id: PR-ES-001
title: 电化学储能电站接入设计
domain: ES
subdomain: ES（电化学储能）
voltage_levels: [LV, MV]
lifecycle: [规划, 设计, 验收]
standards:
  - { code: GB/T 51048-2025, clause: "全文", note: "电化学储能电站设计标准（替代 GB 51048-2015，改推荐性，2026-04-01 实施）：选址、布置、系统配置、消防、安全" }
  - { code: GB/T 36547-2024, clause: "全文", note: "电化学储能电站接入电网技术规定（替代 2018 版）：电能质量、保护、通信、调度" }
  - { code: GB/T 36558-2023, clause: "全文", note: "电力系统电化学储能系统通用技术条件" }
  - { code: GB 44240-2024, clause: "全文", note: "电能存储系统用锂蓄电池和电池组 安全要求（强制性）" }
  - { code: GB/T 42288-2022, clause: "全文", note: "电化学储能电站安全规程：运行安全、消防、热失控防护" }
  - { code: GB 38755-2019, clause: "全文", note: "电力系统安全稳定导则（强制性）：三道防线、储能作为灵活性资源" }
status: draft
reviewers: []
version: 0.1
updated: 2026-09-09
---

# 电化学储能电站接入设计

## 1. 摘要

电化学储能作为新型电力系统的灵活性资源，2026 年起执行 GB/T 51048-2025 设计标准与 GB/T 36547-2024 接入规定。本条给出**容量配置、PCS 选型、并网点选择、保护配置、消防与热失控防护**完整流程，对接 [cn-04 新兴领域标准包](../20-standards/cn-04-新兴领域标准包.md) 中六项国标，结论：**1MW/2MWh 用户侧储能配 2 台 500kW PCS、10kV 并网、锂电安全按 GB 44240-2024 强制校核、热失控按 GB/T 42288-2022 防护**。

## 2. 术语与定义

| 术语 | 定义 | 标准出处 |
|---|---|---|
| PCS | 储能变流器，电池直流 ↔ 电网交流双向变换 | GB/T 36558-2023 |
| 并网点 PCC | 储能系统与电网的连接点 | GB/T 36547-2024 |
| 额定功率/容量 | PCS 额定交流功率 / 电池额定能量 | 同上 |
| 充放电深度 DoD | 单次循环电池容量使用比例 | GB/T 36558 |
| 热失控 | 电池单体温度急剧上升的自加速放热反应 | GB 44240-2024 |
| BMS | 电池管理系统，监视/控制/保护电池 | GB/T 34131-2023 |

## 3. 原理与公式（配置决策树）

### 3.1 容量配置

按应用场景（调峰、备用、调频）确定功率/容量比：

$$E_{rated} = \frac{P_{rated}\cdot t_{dis}}{DoD\cdot\eta_{PCS}\cdot\eta_{bat}}$$

| 符号 | 含义 | 单位 |
|---|---|---|
| $P_{rated}$ | PCS 额定功率 | kW |
| $t_{dis}$ | 设计放电时长（1/2/4h 等） | h |
| $DoD$ | 充放电深度（锂电常 0.8~0.9） | — |
| $\eta_{PCS}$ | PCS 效率（0.97~0.98） | — |
| $\eta_{bat}$ | 电池充放电效率（0.92~0.95） | — |

### 3.2 并网点与保护

用户侧储能优先 0.4kV 低压并网（< 200kW）或 10kV 中压并网（≥ 200kW）。保护配置：

- 孤岛保护（防孤岛运行）：主动/被动双重判据
- 低/过电压、低/过频率保护
- 故障电流保护（PCS 限流特性下传统过流不灵敏，须配置方向/距离保护）
- 防孤岛与电网失压联动跳闸

### 3.3 消防与热失控防护

```
电池舱 ─→ 热失控早期预警（BMS 单体温度监测 + 可燃气体探测器）
     ├─→ 被动防护：电池舱防火分隔（≥ 2h）、泄爆口、独立通风
     ├─→ 主动防护：气体灭火（七氟丙烷/全氟己酮）、液冷系统
     └─→ 热失控抑制：电池级注入灭火剂、防蔓延间距
```

## 4. 标准依据表

| 标准号-年份 | 条款 | 要求要点（转述） | 适用边界 |
|---|---|---|---|
| GB/T 51048-2025 | 全文 | 站址选择、布置、电池/PCS/BMS 选型、消防、安全 | 设计 |
| GB/T 36547-2024 | 全文 | 接入电网：电能质量（谐波/三相不平衡/直流分量）、保护、通信、调度自动化 | 并网 |
| GB/T 36558-2023 | 全文 | 通用技术：功率/容量定义、运行模式、效率 | 通用 |
| GB 44240-2024 | 全文 | 锂电安全强制要求：热失控触发条件、预防、试验 | 强制性 |
| GB/T 42288-2022 | 全文 | 安全规程：运行安全、消防设施、应急处置 | 运行 |
| GB 38755-2019 | 三道防线 | 储能作为灵活性资源参与系统稳定 | 系统级 |

## 5. 设计/选型要点

- [ ] **应用场景定位**：用户侧峰谷套利、调频辅助服务、备用电源、新能源平滑——决定容量配置与运行模式
- [ ] **并网点选择**：低压 0.4kV（< 200kW，接入用户配电变低压母线）；10kV 中压（200kW~10MW，经升压变并网）
- [ ] **PCS 选型**：功率因数、效率、谐波（按 GB/T 14549 校核，详见 [TH-008](../10-theory/TH-008-harmonic-generation.md) 与 [PR-PQ-001](PR-PQ-001-pq-compensation-design.md)）；构网型 vs 跟网型（构网型见 GB/T 47968-2026、GB/T 47655-2026）
- [ ] **电池选型**：磷酸铁锂（LFP，安全优）、三元锂（能量密度高、热失控风险大）、钠离子（新型，安全性好但能量密度低）；按 GB 44240-2024 强制校核
- [ ] **保护配置**：孤岛保护、低/过压频保护、方向过流（适配 PCS 限流特性）、防孤岛联动跳闸
- [ ] **BMS 与 EMS**：BMS 监视单体电压/温度/SOC，EMS 协调 PCS 与电网调度
- [ ] **消防**：站区独立布置、电池舱防火分隔 ≥ 2h、可燃气体探测 + 气体灭火 + 水喷雾
- [ ] **接地**：电池柜、PCS、变流器外壳等电位联结，独立接地装置 $R\le 4$ Ω

## 6. 常见错误与争议

| 错误/争议 | 后果 | 正确做法/主流处理 | 依据 |
|---|---|---|---|
| 用 GB 51048-2015 旧版 | 不符合 2026-04-01 后设计要求 | 用 GB/T 51048-2025 | CHG-002 |
| 并网点 PCC 选错 | 计量与保护错位 | 产权分界点为 PCC，保护配置在 PCC 上游 | GB/T 36547 |
| 传统过流保护未考虑 PCS 限流 | 故障时拒动 | 配方向保护 + 低电压穿越闭锁 | GB/T 36547 §4 |
| 三元锂未按 GB 44240 强制校核 | 热失控事故 | 强制性国标，逐条校核热失控触发与防护 | GB 44240-2024 |
| 电池舱无独立通风与泄爆 | 热失控气体聚集爆炸 | 设可燃气体探测 + 泄爆口 + 独立通风 | GB/T 42288 |
| 站址与建筑物防火间距不足 | 火灾蔓延 | 独立站区，距建筑物 ≥ 10m（具体以 GB/T 51048 为准） | GB/T 51048 |
| 未配置孤岛保护 | 电网失压时储能继续供电危险 | 主动 + 被动双重孤岛保护 | GB/T 36547 |
| 储能与充电桩共用 PCS | 储能直充 vs PCS 交流耦合混淆 | 区分 DC-DC 直充（充电桩在直流侧）与 PCS 交流耦合（详见 [PR-EV-001](PR-EV-001-ev-charging-infrastructure.md)） | 工程惯例 |

## 7. 完整算例（用户侧 1MW/2MWh 储能电站）

### 7.1 已知条件

- 用户场景：工业园区峰谷套利（日两充两放，2h 充/2h 放）
- 峰电价 1.0 元/kWh、谷电价 0.3 元/kWh
- 10kV 中压并网（PCC 在用户 10kV 母线）

### 7.2 容量配置

按 2h 放电、$DoD=0.85$、$\eta_{PCS}=0.97$、$\eta_{bat}=0.95$：

$$E_{bat,rated} = \frac{P_{rated}\cdot t_{dis}}{DoD\cdot\eta_{PCS}\cdot\eta_{bat}} = \frac{1000\times 2}{0.85\times 0.97\times 0.95} = \frac{2000}{0.783} = 2.55\ \text{MWh}$$

电池额定容量选 2.55 MWh，可用容量 2.0 MWh。

### 7.3 PCS 与电池选型

- PCS：2 × 500 kW（N+1 备份，单台故障降额运行），三相 0.4kV 输出，经 0.4/10kV 升压变并网
- 电池：磷酸铁锂（LFP），安全优先；按 GB 44240-2024 强制校核热失控
- BMS：三级架构（单体 → 模组 → 簇），SOC/SOH 实时监测

### 7.4 保护配置

| 保护类型 | 整定 | 依据 |
|---|---|---|
| 孤岛保护（主动） | 频移法 + 阻抗法，跳闸时间 < 2s | GB/T 36547 §4 |
| 孤岛保护（被动） | 电压/频率偏差，$U<85\%$/$U>110\%$、$f<49.5$/$f>50.2$ | 同上 |
| 方向过流 | PCS 限流 1.5 倍，方向元件 + 低压闭锁 | GB/T 36547 |
| 低电压穿越 | $U>20\%$ 持续 150ms 不跳闸 | GB/T 36547 |

### 7.5 谐波校核

PCS 为 PWM 整流，主要 5/7/11/13 次谐波，单次 $\leq 3\%$、THD $\leq 5\%$（GB/T 14549）。短路容量 $S_{sc}=\sqrt3\times 10\times I_k''$，若 $I_k''=18.7$ kA（接续 [CALC-SC-002](../40-calc/CALC-SC-002-hv-short-circuit-iec60909.md)），$S_{sc}=324$ MVA。2 台 PCS 总谐波电流估算 $I_{5}=2\times 500/(\sqrt3\times 0.4)\times 3\%=43$ A，5 次电压畸变率：

$$V_5\% = \frac{5\times 43\times \sqrt3\times 10}{324}\times 100\% = \frac{3724}{324}\times 0.001 \approx 1.15\% \leq 4\%\ \checkmark$$

满足 GB/T 14549 单次谐波 4% 限值。

### 7.6 消防与热失控防护

- 站址：独立布置，距主要建筑物 ≥ 10m
- 电池舱：防火分隔 ≥ 2h、独立通风、可燃气体探测器（H2/CO）、泄爆口
- 灭火：全氟己酮气体灭火（电气火灾适用，详见 [PR-CM-001](PR-CM-001-fire-protection-interlocking.md) 联动）、电池级灭火剂注入接口
- 热失控抑制：电池模组间陶瓷隔板、液冷系统（≤ 35°C 运行）

### 7.7 接地与等电位

- 接地制式：TN-S
- 共用接地装置 $R\le 4$ Ω（含防雷接地、工作接地、保护接地）
- 电池柜、PCS、升压变、BMS 外壳等电位联结到主接地母线

### 7.8 经济性估算

$$\text{日收益} = 2 \text{MWh}\times (1.0-0.3) = 1400\ \text{元/日}$$
$$\text{年收益} = 1400 \times 330 \text{日} = 46.2\ \text{万元}$$

按 1MW/2.55MWh 估算总投资 250 万元（PCS + 电池 + 升压 + 土建），静态回收期约 5.4 年（未计补贴与电池衰减）。

## 8. 关联条目

- 上游：[cn-04 新兴领域储能标准包](../20-standards/cn-04-新兴领域标准包.md)（GB/T 51048-2025 等 6 项）、[TH-008 谐波](../10-theory/TH-008-harmonic-generation.md)（PCS 谐波机理）、[TH-014 磁路饱和](../10-theory/TH-014-magnetic-circuit-saturation.md)（变压器/PCS 铁芯设计）、[TH-024 电力电子变换器基础拓扑与 PWM](../10-theory/TH-024-power-electronic-converters-and-pwm.md)（PCS 拓扑与构网/跟网型控制物理来源）、[TH-020 电力系统稳定性分类](../10-theory/TH-020-power-system-stability-classification.md)（构网型 PCS 与电网稳定协调）、[TH-027 高压直流输电 LCC/VSC-HVDC](../10-theory/TH-027-hvdc-transmission-lcc-vsc.md)（VSC-MMC 拓扑与构网型 PCS 共享控制基础）、[TH-028 柔性交流输电 FACTS](../10-theory/TH-028-facts-flexible-ac-transmission.md)（构网型 PCS 与 STATCOM 共享 VSG 控制）、[TH-029 微电网控制与并离网切换](../10-theory/TH-029-microgrid-control-and-grid-mode-switching.md)（储能 PCS 黑启动与 VF 控制、下垂对等运行）、[TH-030 分布式电源并网保护与孤岛检测](../10-theory/TH-030-distributed-generation-protection-and-islanding-detection.md)（储能 PCS 防孤岛与 LVRT/HVRT）、[TH-032 同步电机进相与调相运行](../10-theory/TH-032-synchronous-machine-leading-and-condensing-operation.md)（调相机替代方案与构网型 PCS 对比）、[TH-038 新能源高占比系统频率稳定与惯量支撑](../10-theory/TH-038-high-renewable-frequency-stability-inertia.md)（储能 VSG 虚拟惯量与一次调频整定，RoCoF 保护与最低频率约束）、[TH-040 交直流混联电网稳定](../10-theory/TH-040-hybrid-ac-dc-grid-stability.md)（VSC 换流站与构网型 PCS 共享控制，MIDC 场景下储能暂态无功补偿）、[TH-041 配电网高渗透率 DG 承载力](../10-theory/TH-041-distribution-grid-high-penetration-dg-hosting-capacity.md)（储能削峰填谷与 LVRT 支撑提升 DG 静态/动态承载力）、[TH-043 AI 在电气工程应用基础](../10-theory/TH-043-ai-foundations-in-electrical-engineering.md)（储能 SOH 估计与策略优化，PINN+RL 应用）、[TH-044 电力电子化电力系统低惯量与宽频振荡](../10-theory/TH-044-power-electronics-dominated-system-low-inertia-wideband-oscillation.md)（构网型 vs 跟网型 PCS 选择与宽频阻抗建模）
- 下游：[PR-PQ-001 无功补偿与谐波治理](PR-PQ-001-pq-compensation-design.md)（PCS 谐波治理）、[PR-EV-001 电动汽车充电](PR-EV-001-ev-charging-infrastructure.md)（光储充一体化场景）、[PR-CM-001 消防联动](PR-CM-001-fire-protection-interlocking.md)（储能舱消防联动）、[CASE-023 轨道交通牵引变电所协同](../50-case/CASE-023-composite-metro-traction-substation.md)（再生制动逆变回馈+超级电容储能方案对比）、[CASE-033 储能电站全流程](../50-case/CASE-033-composite-energy-station-full-process.md)（储能电站全流程）
- 下游案例：[CASE-043 构网型PCS并离网](../50-case/CASE-043-composite-pv-storage-diesel-microgrid.md)、[CASE-048 新能源储能调频](../50-case/CASE-048-composite-renewable-collector-station-protection.md)、[CASE-054 光伏并离网](../50-case/CASE-054-review-pv-anti-islanding-reverse-power.md)
- 平行：[PR-PE-001 继电保护配置](PR-PE-001-relay-protection-config.md)（新型电源对保护的影响）、[GB/T 47968-2026 构网型变流器](../20-standards/cn-04-新兴领域标准包.md)（构网型 PCS 选型）
- 案例支撑：[CASE-004 储能综合案例](../50-case/CASE-004-composite-energy-storage.md)（1MW/2MWh多专业协同，沿用本条数据链）
- 计算支撑：[CALC-HM-001 谐波潮流计算](../40-calc/CALC-HM-001-harmonic-power-flow.md)（PCS谐波电流叠加与电能质量校核）

## 9. 变更记录

| 版本 | 日期 | 修改内容 | 修改人 |
|---|---|---|---|
| 0.1 | 2026-09-09 | 创建；含 1MW/2MWh 用户侧储能完整配置、保护、消防与经济性估算 | KB 管理员 |
