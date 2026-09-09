---
id: CALC-SC-002
title: 高压系统三相短路电流计算（IEC 60909 网络法）
domain: CALC
subdomain: SC（短路计算）
voltage_levels: [MV, HV]
lifecycle: [设计]
standards:
  - { code: GB/T 15544.1-2013, clause: "全文", note: "三相交流系统短路电流计算（idt IEC 60909-0），c 系数 MV 取 1.10、HV 取 1.10" }
  - { code: DL/T 5222-2021, clause: "第6章", note: "导体和电器选择设计规程：3kV~1000kV 设备短路开断与耐受电流校验" }
  - { code: GB/T 14285-2023, clause: "第5章", note: "继电保护和安全自动装置技术规程：短路保护最小灵敏度要求" }
  - { code: GB 50060-2008, clause: "第6章", note: "高压配电装置短路电流校验要求" }
status: draft
reviewers: []
version: 0.1
updated: 2026-09-09
---

# 高压系统三相短路电流计算（IEC 60909 网络法）

## 1. 摘要

高压短路与低压短路的核心区别在于：①系统阻抗不能忽略（上级电网短路容量有限）；②发电机/大型电动机的次暂态电抗 $X_d''$ 成为重要输入（近端短路）；③电动机反馈电流在 MV 系统贡献显著。本条给出 10kV 配电网三相短路的完整计算流程，以综合办公楼 10kV 进线端为算例：**上级 $S_{scQ} = 200$ MVA、10kV 母线 $I_k'' = 12.6$ kA、$i_p = 28.9$ kA**，联动 [TH-011](../10-theory/TH-011-synchronous-machine-subtransient-reactance.md) 次暂态电抗理论与 [SC-001](CALC-SC-001-低压三相短路电流计算.md) 低压计算形成全电压等级覆盖。

## 2. 术语与定义

| 术语 | 定义 | 标准出处 |
|---|---|---|
| 远端短路（far from generator） | 短路期间交流分量基本不衰减（无发电机近端效应） | GB/T 15544.1 |
| 近端短路（near to generator） | 短路点距同步发电机电气距离近，交流分量显著衰减 | 同上 |
| 初始对称短路电流 $I_k''$ | t=0 时刻对称交流分量有效值 | 同上 |
| 峰值短路电流 $i_p$ | 含直流分量的最大瞬时值 | 同上 |
| 对称开断电流 $I_b$ | 开关电器触头分离时刻的对称电流有效值 | 同上 |
| 电动机反馈电流 $\Sigma I_{rM}$ | 异步电动机在短路瞬间贡献的次暂态电流 | 同上 §4.3.2 |

## 3. 原理与公式

### 3.1 等效电压源法（与 SC-001 同一方法，扩展至 MV/HV）

$$I_k'' = \frac{c \cdot U_n}{\sqrt{3} \cdot Z_k}$$

**关键区别**：MV/HV 的 $c$ 系数取值与 LV 不同：

| 电压等级 | $c$（最大） | $c$（最小） |
|---|---|---|
| LV (≤1kV) | 1.05 | 0.95 |
| MV (1~35kV) | **1.10** | 1.00 |
| HV (35~230kV) | **1.10** | 1.00 |

### 3.2 各阻抗归算（归算至 10kV 侧）

| 环节 | 公式 | 说明 |
|---|---|---|
| 上级系统 | $X_Q = \dfrac{U_{nQ}^2}{S_{scQ}}$ | $S_{scQ}$ 为上级供电局提供的系统短路容量 |
| 变压器（10kV 侧） | $Z_T = \dfrac{u_k\%}{100} \cdot \dfrac{U_{rT}^2}{S_{rT}}$ | 10/0.4kV 变压器归算至 10kV 侧 |
| 线路（10kV 电缆） | $R_L = r \cdot l$，$X_L = x \cdot l$ | 单位长度阻抗 × 长度 |
| 发电机（近端短路时） | $Z_G = K_G \cdot X_d'' \cdot \dfrac{U_{rG}^2}{S_{rG}}$ | $K_G$ 为校正系数，见 GB/T 15544.1 §3.6 |

### 3.3 峰值系数 $\kappa$（MV/HV 精确法）

$$\kappa = 1.02 + 0.98 \cdot e^{-3 R_k/X_k}$$

> LV 可用简化法（$\kappa = 1.3$ 或查表），MV/HV 须用精确法。

### 3.4 电动机反馈电流

MV 系统中异步电动机总容量 $\Sigma P_{rM} > 0.01 \times S_k$ 时须计反馈：

$$\Delta I_k'' = \frac{E_M''}{X_M''} \approx \frac{0.9}{X_M''} \cdot \sum I_{rM}$$

其中 $X_M'' \approx 1/I_{st}^*$（启动电流倍数倒数），典型 $X_M'' \approx 0.17$ p.u.（$I_{st} = 6$），$E_M'' \approx 0.9$ p.u.。

## 4. 标准依据表

| 标准号-年份 | 条款 | 要求要点（转述） | 适用边界 |
|---|---|---|---|
| GB/T 15544.1-2013 | 4.0 | 等效电压源法：短路点唯一电压源 $c \cdot U_n/\sqrt{3}$ | 三相交流系统通用 |
| GB/T 15544.1-2013 | 4.3.2 | 异步电动机在 $t < 0.1$s 期间贡献短路电流，$I_{kM}'' \approx I_{rM}/X_M''$ | 近端短路须计 |
| GB/T 15544.1-2013 | 4.2 | c 系数：MV/HV 取 1.10（最大）/1.00（最小） | 1kV 以上 |
| DL/T 5222-2021 | 6.2.3 | 高压断路器额定短路开断电流 ≥ 安装处 $I_k''$（或 $I_b$） | 3kV~1000kV |
| DL/T 5222-2021 | 6.2.4 | 高压设备额定峰值耐受电流 ≥ $i_p$ | 同上 |
| GB 50060-2008 | 6.0.4 | 高压电器选择应按 $I_k''$ 校验开断能力 | 3~110kV |

## 5. 设计/选型要点（校审清单）

- [ ] 向供电局索取上级系统短路容量 $S_{scQ}$（不可自行假设——以供电方案答复函为准）
- [ ] MV/HV 的 $c$ 系数取 1.10（最大短路电流工况，校验设备开断/耐受能力）
- [ ] 同步电机近端短路须取 $X_d''$（联动 [TH-011](../10-theory/TH-011-synchronous-machine-subtransient-reactance.md)），并校正 $K_G$
- [ ] 异步电动机反馈：$\Sigma P_{rM} >$ 安装处 $S_k$ 的 1% 时须计入
- [ ] 峰值系数用精确法 $R_k/X_k$ 计算，MV 系统不宜用简化值 1.3
- [ ] 校验设备：断路器 $I_{bk} \geq I_k''$（开断）、$I_{pk} \geq i_p$（峰值耐受）、$I_{cw} \geq I_k''$（短时耐受）

## 6. 常见错误与争议

| 错误/争议 | 后果 | 正确做法/主流处理 | 依据 |
|---|---|---|---|
| MV 用 LV 的 $c = 1.05$ | 短路电流偏小 5%，设备选型偏危险 | MV 取 $c = 1.10$ | GB/T 15544.1 表 1 |
| 电动机反馈漏算 | 近端/厂用变母线短路 $I_k''$ 偏低 | $\Sigma P_{rM} > 1\% S_k$ 时计入 | 同上 §4.3.2 |
| 峰值系数 $\kappa$ 取固定 1.8 | MV 电缆回路 $R/X$ 大、$\kappa$ 实际偏小，过度设计 | 用 $R_k/X_k$ 精确计算 | 同上 §4.3.4 |
| 发电机用 $X_d$（同步电抗） | 近端短路 $I_k''$ 偏小数倍，严重偏危险 | 近端用 $X_d''$，稳态用 $X_d$ | [TH-011](../10-theory/TH-011-synchronous-machine-subtransient-reactance.md) |
| 上级 $S_{scQ}$ 自行假设 | 短路电流与实际偏差极大 | 必须以供电局答复函为准 | 行业惯例 |

## 7. 完整算例（综合办公楼 10kV 进线端短路）

### 7.1 已知条件

| 参数 | 值 | 来源 |
|---|---|---|
| 上级系统短路容量 $S_{scQ}$ | 200 MVA | 供电局答复函 |
| 进线电缆 | YJV22-8.7/15kV 3×120mm² Cu，$l = 50$ m | 设计文件 |
| 电缆单位阻抗 | $r = 0.153$ Ω/km，$x = 0.082$ Ω/km | 产品手册 |
| 异步电动机群 | $\Sigma P_{rM} = 250$ kW，$I_{st} = 6$（$X_M'' = 0.167$ p.u.） | LD-001 用电设备 |

### 7.2 阻抗归算（归算至 $U_n = 10$ kV）

| 环节 | 计算 | 结果 |
|---|---|---|
| 系统阻抗 $Z_Q$ | $Z_Q = \dfrac{U_{nQ}^2}{S_{scQ}} = \dfrac{10^2}{200} = 0.5$ Ω | $Z_Q \approx X_Q = 0.5$ Ω（$R_Q$ 可忽略） |
| 电缆阻抗 | $R_L = 0.153 \times 0.05 = 0.00765$ Ω；$X_L = 0.082 \times 0.05 = 0.0041$ Ω | $R_L = 0.00765$ Ω，$X_L = 0.0041$ Ω |
| 总阻抗 $Z_k$ | $R_k = R_L = 0.00765$ Ω；$X_k = X_Q + X_L = 0.5 + 0.0041 = 0.504$ Ω | $Z_k = \sqrt{0.00765^2 + 0.504^2} = 0.504$ Ω |

> 电缆在 50m 长度下阻抗远小于系统阻抗，可近似 $Z_k \approx X_Q$——但这不适用于长馈线（电缆阻抗占比增大）。

### 7.3 初始对称短路电流 $I_k''$

$$I_k'' = \frac{c \cdot U_n}{\sqrt{3} \cdot Z_k} = \frac{1.10 \times 10000}{\sqrt{3} \times 0.504} = \frac{11000}{0.873} = \mathbf{12.6 \text{ kA}}$$

### 7.4 峰值短路电流 $i_p$（精确法）

$$\frac{R_k}{X_k} = \frac{0.00765}{0.504} = 0.0152$$

$$\kappa = 1.02 + 0.98 \cdot e^{-3 \times 0.0152} = 1.02 + 0.98 \times e^{-0.0455} = 1.02 + 0.98 \times 0.9555 = 1.02 + 0.936 = 1.956$$

$$i_p = \kappa \cdot \sqrt{2} \cdot I_k'' = 1.956 \times 1.414 \times 12.6 = \mathbf{34.9 \text{ kA}}$$

> 注：由于 $R/X$ 极小（系统阻抗主导），$\kappa$ 接近上限 2.0。若误取 $\kappa = 1.8$（简化值），$i_p = 32.2$ kA，偏危险 7.7%。

### 7.5 电动机反馈电流

电动机总额定电流：

$$\sum I_{rM} = \frac{\sum P_{rM}}{\sqrt{3} \cdot U_n \cdot \cos\varphi \cdot \eta} = \frac{250 \times 10^3}{\sqrt{3} \times 10000 \times 0.85 \times 0.9} = \frac{250000}{13243} = 18.9 \text{ A}$$

$$\Delta I_{kM}'' = \frac{E_M''}{X_M''} \cdot \sum I_{rM} = \frac{0.9}{0.167} \times 18.9 = 5.39 \times 18.9 = 101.9 \text{ A} \approx 0.10 \text{ kA}$$

$$\Delta I_{kM}'' / I_k'' = 0.10 / 12.6 = 0.8\%$$

> $\Delta I_{kM}''$ 占比 $< 1\%$，可忽略。但若厂区电动机群达 MW 级，占比可超 5%，必须计入。

### 7.6 设备选型校验

| 校验项 | 要求 | 实际 | 选型 | 结果 |
|---|---|---|---|---|
| 真空断路器开断 $I_{bk}$ | ≥ $I_k'' = 12.6$ kA | VC $I_{bk} = 25$ kA | KYN28-12 / VCB 25kA | ✓ |
| 峰值耐受 $I_{pk}$ | ≥ $i_p = 34.9$ kA | VC $I_{pk} = 63$ kA | 同上 | ✓ |
| 短时耐受 $I_{cw}$ (4s) | ≥ $I_k'' = 12.6$ kA | VC $I_{cw} = 25$kA/4s | 同上 | ✓ |
| 电缆热稳定 $S_{\min}$ | $\geq \dfrac{I_k'' \sqrt{t}}{k}$ | $\dfrac{12600 \times \sqrt{0.5}}{143} = 62.3$ mm² | 120mm² ≥ 62.3mm² | ✓ |

> $t = 0.5$ s 为继电保护 + 断路器全分闸时间（[PR 域保护配置](PR-PT-002-relay-protection-coordination.md) 待建）。

### 7.7 与低压系统的衔接

10/0.4kV 变压器低压侧短路（联动 [SC-001](CALC-SC-001-低压三相短路电流计算.md) d1 点）：

| 参数 | 10kV 侧归算 | 0.4kV 侧实际 |
|---|---|---|
| 变压器阻抗 $Z_T$ | $Z_T = \frac{6\% \times 10^2}{0.63} = 9.52$ Ω（10kV 侧） | $Z_T = \frac{6\% \times 0.4^2}{0.63} = 0.01524$ Ω（0.4kV 侧） |
| 系统阻抗 $Z_Q$ | 0.5 Ω | 归算至 0.4kV 侧：$0.5 \times (0.4/10)^2 = 0.0008$ Ω |

> SC-001 的低压短路计算中 $X_Q = U_{nQ}^2 / S_{scQ} = 0.4^2 / 200 = 0.0008$ Ω，与本处归算一致——验证了高低压衔接正确性。

## 8. 关联条目

- 上游：[TH-011 同步电机次暂态电抗](../10-theory/TH-011-synchronous-machine-subtransient-reactance.md)（发电机近端短路的理论基础）
- 平行：[CALC-SC-001 低压短路计算](CALC-SC-001-低压三相短路电流计算.md)（同方法、不同电压等级）、[TH-003 对称分量法](../10-theory/TH-003-symmetrical-components.md)（不对称短路扩展）
- 下游：[PR-DD-002 变电所布置](../30-practice/PR-DD-002-substation-layout-and-equipment-selection.md)（设备选型校验）、[PR-PE-001 继电保护配置与整定配合](../30-practice/PR-PE-001-relay-protection-config.md)（$I_k''$ 与 CT 校验数据源）、[CASE-020 油浸变压器短路起火](../50-case/CASE-020-accident-oil-transformer-fire.md)（内部匝间短路电流估算）、[CASE-022 2021短路电流与保护整定真题](../50-case/CASE-022-exam-short-circuit-protection.md)（c系数最大/最小双工况）、[CASE-023 轨道交通直流牵引变电所](../50-case/CASE-023-composite-metro-traction-substation.md)（直流系统短路等效）、[CASE-028 海上风电海上升压站](../50-case/CASE-028-composite-offshore-wind-substation.md)（海上风电短路校验）、[CASE-030 2019电缆载流量截面真题](../50-case/CASE-030-exam-cable-ampacity-section.md)（热稳定短路电流）、[CASE-032 电缆终端击穿事故](../50-case/CASE-032-accident-cable-termination-breakdown.md)（击穿后短路）、[CASE-033 储能电站全流程](../50-case/CASE-033-composite-energy-station-full-process.md)（并网点短路）
- 下游案例：[CASE-037 铁磁谐振](../50-case/CASE-037-accident-ferroresonance-pt-burnout.md)、[CASE-040 断路器开断校验](../50-case/CASE-040-exam-short-circuit-dc-component-breaker.md)、[CASE-049 电缆接头热稳定](../50-case/CASE-049-review-cable-joint-construction-defect.md)、[CASE-053 整流变压器短路](../50-case/CASE-053-composite-rail-transit-traction-rectifier.md)、[CASE-051 线路短路](../50-case/CASE-051-review-distance-protection-coordination-cascade-trip.md)

## 9. 变更记录

| 版本 | 日期 | 修改内容 | 修改人 |
|---|---|---|---|
| 0.1 | 2026-09-09 | 创建；含 10kV 网络短路全算例 + 电动机反馈 + 高低压衔接验证 | KB 管理员 |
