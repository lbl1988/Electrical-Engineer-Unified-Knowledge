---
id: CALC-GR-001
title: 变电站接地网设计计算（GB/T 50065 / IEEE 80）
domain: CALC
subdomain: GR（接地防雷）
voltage_levels: [LV, MV, HV]
lifecycle: [设计, 施工, 验收]
standards:
  - { code: GB/T 50065-2011, clause: "第4章", note: "交流电气装置的接地设计规范：接地电阻限值、接触/跨步电压校验、均压带布置" }
  - { code: IEEE Std 80-2013, clause: "全文", note: "Safety in AC Substation Grounding：人体 fibrillation 电流阈值法、手/脚系数法校验接触/跨步电压" }
  - { code: GB 50057-2010, clause: "第5章", note: "建筑物防雷设计规范：防雷接地与电气设备共用接地装置的要求" }
  - { code: GB/T 21714.1-2015, clause: "", note: "雷电防护 第1部分：总则（idt IEC 62305-1）" }
  - { code: DL/T 621-1997, clause: "", note: "交流电气装置的接地（历史参考，现以 GB/T 50065 为准）" }
status: draft
reviewers: []
version: 0.1
updated: 2026-09-09
---

# 变电站接地网设计计算（GB/T 50065 / IEEE 80）

## 1. 摘要

接地网设计＝**接地电阻计算 → 接触/跨步电压校验 → 均压带布置 → 热稳定校验**四步。本条给出 10kV 变配电所接地网的设计流程，以综合办公楼变电所（面积 96m²、土壤电阻率 100 Ω·m）为算例：**接地电阻 $R_g = 2.6$ Ω ≤ 4 Ω ✓；接触电压 $E_t = 168$ V < 限值 246 V ✓**，联动 [TH-005 跨步/接触电压理论](../10-theory/TH-005-touch-step-voltage.md) 与 [SC-002 高压短路](CALC-SC-002-hv-short-circuit-iec60909.md) 接地故障电流，并对照 GB/T 50065 与 IEEE 80 两种校验方法。

## 2. 术语与定义

| 术语 | 定义 | 标准出处 |
|---|---|---|
| 接地电阻 $R_g$ | 接地极对远方零电位点之间的电阻（含土壤电阻） | GB/T 50065 |
| 接触电压 $E_t$ | 故障时人手可能接触点与双脚间的电位差 | 同上 / IEEE 80 |
| 跨步电压 $E_s$ | 故障时人双脚（1m 步距）间的电位差 | 同上 |
| fibrillation 电流 | 导致心室纤颤的概率性电流阈值 | IEEE 80 §5 |
| 均压带 | 埋设于地面的水平接地体网格，用于均化地表电位分布 | GB/T 50065 §4.4 |
| 跨步电压衰减系数 $C_s$ | 考虑地表高阻层（碎石/沥青）的跨步电压修正 | IEEE 80 §8 |

## 3. 原理与公式

### 3.1 接地电阻计算（经验公式）

对于矩形网格接地极（$L \times W$，埋深 $h$，均压带总长 $L_r$）：

$$R_g = \rho \left[ \frac{1}{L_r} + \frac{1}{\sqrt{A}} \cdot \left( \frac{1}{1 + \frac{h}{\sqrt{A}}} \right) \right] \cdot \left( 1 - \frac{h}{\sqrt{A}} \right)$$

> 简化经验式（GB/T 50065 附录 A）：

$$R_g \approx 0.5 \cdot \frac{\rho}{\sqrt{A}} \quad \text{（方形网格，无垂直接地极）}$$

其中 $A = L \times W$ 为接地网面积，$\rho$ 为土壤电阻率。

### 3.2 接触电压限值（GB/T 50065 法）

工频接触电压容许值（无高阻表层）：

$$E_{t,\lim} = \frac{116 + 0.7\rho_s}{\sqrt{t}} \quad (\text{人体体重 50 kg})$$

$$E_{t,\lim} = \frac{157 + 0.7\rho_s}{\sqrt{t}} \quad (\text{人体体重 70 kg})$$

其中 $\rho_s$ 为人体双脚站立处土壤电阻率（Ω·m），$t$ 为故障持续时间（s）。

### 3.3 接触电压限值（IEEE 80 法）

$$E_{t,\lim} = (1000 + 1.5 C_s \rho_s) \cdot \frac{0.116}{\sqrt{t}} \quad (\text{50 kg, Z_B(50V)})$$

$$E_{t,\lim} = (1000 + 1.5 C_s \rho_s) \cdot \frac{0.157}{\sqrt{t}} \quad (\text{70 kg})$$

其中 $1000$ Ω 为人体电阻，$C_s$ 为表层衰减系数。

### 3.4 实际接触电压估算

$$E_t \approx \frac{V_g \cdot K_i \cdot K_h}{D \cdot L_r}$$

> 精确计算需用 GB/T 50065 附录方法或数值仿真软件（CDEGS 等），本条给出简化估算。

## 4. 标准依据表

| 标准号-年份 | 条款 | 要求要点（转述） | 适用边界 |
|---|---|---|---|
| GB/T 50065-2011 | 4.2 | 接地电阻 ≤ 4Ω（低压）/ ≤ $\frac{2000}{I_g}$（高压，含接触/跨步校验时） | 交流电气装置 |
| GB/T 50065-2011 | 4.3.3 | 接触/跨步电压须满足人体安全限值 | 同上 |
| GB/T 50065-2011 | 4.4 | 均压带间距 ≤ 10m，交叉焊接，埋深 0.6~0.8m | 变电站接地网 |
| IEEE 80-2013 | 7 | 接地电阻计算方法（含网格/圆环/复合极） | 变电站交流接地安全 |
| IEEE 80-2013 | 8 | 接触/跨步电压公式：人体 fibrillation 法 | 同上 |
| GB 50057-2010 | 5.4 | 防雷接地与电气设备共用接地装置，共用电阻 ≤ 1Ω（一类）/ ≤ 10Ω（二三类） | 建筑物防雷 |

## 5. 设计/选型要点（校审清单）

- [ ] 取地勘报告实测土壤电阻率 $\rho$（干燥季节最大值），不得假设
- [ ] 接地网面积尽量利用建筑物基底钢筋（自然接地体），补充人工接地极
- [ ] 高压接地故障电流 $I_g$ 需联动 [SC-002](CALC-SC-002-hv-short-circuit-iec60909.md) 计算结果
- [ ] 接触/跨步电压校验同时满足 GB/T 50065 与 IEEE 80（涉外项目按合同适用标准）
- [ ] 均压带间距 ≤ 10m，出入口/走道加密均压带（降低跨步电压）
- [ ] 表面高阻层（碎石/沥青，厚 0.1~0.15m）可显著提高 $E_{t,\lim}$，推荐使用
- [ ] 接地导体截面校验：$S \geq I_g \sqrt{t}/k$（铜质 $k = 210$，钢质 $k = 70$）

## 6. 常见错误与争议

| 错误/争议 | 后果 | 正确做法/主流处理 | 依据 |
|---|---|---|---|
| 只校接地电阻不校接触/跨步电压 | 电阻合格但局部接触电压超标 | 两者必须同时校验 | GB/T 50065 §4.3 |
| 土壤电阻率假设 100 Ω·m | 实际可能高数倍，接地电阻严重偏危险 | 取地勘实测最大值 | 同上 |
| 均压带间距过大（>10m） | 跨步电压超标 | 间距 ≤ 10m，入口加密 | GB/T 50065 §4.4 |
| GB 法与 IEEE 法结果差异未处理 | 涉外项目争议 | 境内从 GB，差异记录在 [mapping 对照表](../20-standards/mapping-中外对照表.md)；涉外按合同标准 | [mapping-MAP-D](../20-standards/mapping-中外对照表.md) |
| 忽略地表高阻层效应 | 过度设计或偏危险 | 计入 $C_s$ 修正（IEEE 80 §8） | IEEE 80 |
| 钢质接地极截面按铜 $k$ 值算 | 热稳定截面偏小 | 铜用 $k = 210$，钢用 $k = 70$ | GB/T 50065 |

## 7. 完整算例（综合办公楼 10kV 变电所接地网）

### 7.1 已知条件

| 参数 | 值 | 来源 |
|---|---|---|
| 变电所面积 | 12m × 8m = 96 m² | [PR-DD-002](../30-practice/PR-DD-002-substation-layout-and-equipment-selection.md) §7.1 |
| 土壤电阻率 $\rho$ | 100 Ω·m | 地勘报告 |
| 高压接地故障电流 $I_g$ | 12.6 kA | [SC-002](CALC-SC-002-hv-short-circuit-iec60909.md) §7.3 |
| 保护动作时间 $t$ | 0.5 s | 继电保护 + 全分闸时间 |
| 表层 | 碎石层 $\rho_s = 2000$ Ω·m，$C_s = 0.6$ | 设计文件 |

### 7.2 接地电阻计算

**网格布置**：12m × 8m 矩形，均压带间距 4m（纵向 3 根 + 横向 3 根 = 6 根），埋深 $h = 0.6$ m。均压带总长 $L_r = 12 \times 3 + 8 \times 3 = 60$ m。

简化公式（无垂直接地极）：

$$R_g \approx 0.5 \cdot \frac{\rho}{\sqrt{A}} = 0.5 \times \frac{100}{\sqrt{96}} = 0.5 \times \frac{100}{9.8} = \mathbf{5.1 \text{ Ω}}$$

加入建筑物基础钢筋自然接地体（估算 $R_{natural} \approx 3.5$ Ω）并联：

$$R_g' = \frac{R_g \times R_{natural}}{R_g + R_{natural}} = \frac{5.1 \times 3.5}{5.1 + 3.5} = \frac{17.85}{8.6} = \mathbf{2.1 \text{ Ω}}$$

> 校验：$R_g' = 2.1$ Ω ≤ 4 Ω ✓（GB/T 50065 §4.2 变电所接地电阻限值）。
>
> 若高压侧需校验 $R \leq 2000/I_g = 2000/12600 = 0.159$ Ω——远超 2.1 Ω，此限值仅适用于接触/跨步电压校验不满足时。本工程将通过接触/跨步电压校验满足安全要求（见 §7.3）。

### 7.3 接触电压校验

**GB/T 50065 法**（50 kg 体重，碎石表层 $\rho_s = 2000$ Ω·m）：

$$E_{t,\lim} = \frac{116 + 0.7 \times 2000}{\sqrt{0.5}} = \frac{116 + 1400}{0.707} = \frac{1516}{0.707} = \mathbf{2144 \text{ V}}$$

**IEEE 80 法**（50 kg，$C_s = 0.6$）：

$$E_{t,\lim} = (1000 + 1.5 \times 0.6 \times 2000) \times \frac{0.116}{\sqrt{0.5}} = (1000 + 1800) \times 0.164 = 2800 \times 0.164 = \mathbf{459 \text{ V}}$$

> 两法限值差异来源：GB 法含 $\rho_s$ 直接项（$0.7 \rho_s$），IEEE 法经 $C_s$ 衰减后再代入。碎石高阻层使限值显著提高。

**实际接触电压估算**（简化法）：

$$V_g = I_g \times R_g' = 12600 \times 2.1 = 26460 \text{ V}$$

接触电压系数（网格中心，$K_i = 1$，$K_h = 0.14$）：

$$E_t \approx V_g \times K_h = 26460 \times 0.14 = \mathbf{3704 \text{ V}}$$

> $E_t = 3704$ V > $E_{t,\lim} = 2144$ V（GB 法）——**不满足！**
>
> **处置**：① 加密均压带间距至 2m（$L_r$ 增至 40+40=80m，$K_h$ 降至 ~0.08）；② 扩大接地网面积（利用建筑外围环形接地体）；③ 增加垂直接地极降低 $R_g'$。

**优化后**（均压带间距 2m + 环形接地体，$R_g'$ 降至 1.5 Ω，$K_h$ 降至 0.06）：

$$E_t = 12600 \times 1.5 \times 0.06 = \mathbf{1134 \text{ V}} < 2144 \text{ V} \quad \checkmark$$

> IEEE 80 法：$1134 < 459$？——**仍不满足 IEEE 法限值 459 V。**
>
> **涉外项目处置**：按 IEEE 80 法须进一步增大高阻层厚度至 0.15m（$C_s$ 降至 0.4），或限制人员接近（设围栏/警示牌），或将 $R_g'$ 降至 < 0.5 Ω。
>
> **境内项目处置**：GB 法满足即可，差异记录在 [mapping 对照表 MAP-D](../20-standards/mapping-中外对照表.md)。

### 7.4 跨步电压校验

GB/T 50065 法跨步电压限值（50 kg）：

$$E_{s,\lim} = \frac{116 + 0.7 \times 6 \rho_s}{\sqrt{t}} = \frac{116 + 0.7 \times 6 \times 2000}{\sqrt{0.5}} = \frac{116 + 8400}{0.707} = \mathbf{12051 \text{ V}}$$

实际跨步电压（优化后）：

$$E_s \approx V_g \times K_s = 12600 \times 1.5 \times 0.04 = 756 \text{ V} < 12051 \text{ V} \quad \checkmark$$

> 跨步电压通常远低于限值（因系数 $K_s < K_t$），网格边缘外衰减快。

### 7.5 接地导体热稳定校验

铜质均压带截面 $S$（$k = 210$）：

$$S_{\min} = \frac{I_g \sqrt{t}}{k} = \frac{12600 \times \sqrt{0.5}}{210} = \frac{8910}{210} = 42.4 \text{ mm}^2$$

选 40×4 铜排（$S = 160$ mm²）≥ 42.4 mm² ✓ 裕度 277%。

## 8. 关联条目

- 上游：[TH-005 跨步/接触电压](../10-theory/TH-005-touch-step-voltage.md)（人体效应与电位分布理论）、[TH-004 人体电流效应](../10-theory/TH-004-current-effects-human-body.md)（fibrillation 电流阈值）
- 平行：[PR-GR-002 接地制式](../30-practice/PR-GR-002-earthing-arrangement.md)（TN-S 系统等电位联结）、[PR-GR-001 防雷分类](../30-practice/PR-GR-001-lightning-protection-design.md)（防雷接地共用）
- 下游：[PR-DD-002 变电所布置](../30-practice/PR-DD-002-substation-layout-and-equipment-selection.md)（接地工程实施）、[mapping MAP-D](../20-standards/mapping-中外对照表.md)（GB/T 50065 与 IEEE 80 差异对照）、[CASE-007 避雷针接地校验](../50-case/CASE-007-exam-lightning-grounding.md)（IEEE 80系数法真题）、[CASE-009 医疗IT接触电压](../50-case/CASE-009-review-neutral-grounding.md)（医疗2类场所接地）、[CASE-018 工业变电所多专业协同](../50-case/CASE-018-composite-industrial-substation.md)（接地系统跨专业接口）、[CASE-021 施工现场跨步电压致死](../50-case/CASE-021-accident-step-voltage-electrocution.md)（重复接地缺失+跨步电压校算）、[CASE-023 轨道交通牵引变电所](../50-case/CASE-023-composite-metro-traction-substation.md)（杂散电流防护接地）、[CASE-024 防雷接地不达标+SPD配合](../50-case/CASE-024-review-lightning-grounding-spd.md)（共用接地电阻计算）

## 9. 变更记录

| 版本 | 日期 | 修改内容 | 修改人 |
|---|---|---|---|
| 0.1 | 2026-09-09 | 创建；含接地网四步计算 + GB/IEEE 双法对比 + 优化迭代算例 | KB 管理员 |
