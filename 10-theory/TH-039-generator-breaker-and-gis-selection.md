---
id: TH-039
title: 高压断路器选型深入（发电机断路器与 GIS）
domain: 基础理论
subdomain: 开关电器
voltage_levels: [MV, HV, EHV]
lifecycle: [设计, 选型, 运维]
standards:
  - { code: GB 1984-2014, clause: "4", note: "高压交流断路器（idt IEC 62271-100），含 TRV 标准值与近区故障" }
  - { code: GB/T 14824-2008, clause: "4", note: "高压交流发电机断路器技术条件（idt IEC 62271-101），机端短路特性" }
  - { code: DL/T 5222-2021, clause: "6", note: "导体和电器选择设计规程，发电机断路器与 GIS 选型" }
  - { code: GB/T 11022-2020, clause: "4", note: "高压开关设备通用规范（idt IEC 62271-1），GIS 结构与额定值" }
status: draft
reviewers: []
version: 0.1
updated: 2026-09-09
---

# 高压断路器选型深入（发电机断路器与 GIS）

## 1. 定义

本条深入两类特殊应用断路器：**发电机断路器（Generator Circuit Breaker, GCB）**与**气体绝缘开关设备（GIS, Gas-Insulated Switchgear）**。

| 特殊应用 | 与常规的差别 | 标准 |
|---|---|---|
| **发电机断路器** | 机端短路直流分量衰减慢、$\kappa>2.7$、TRV 严苛，须专用型 | GB/T 14824 |
| **GIS** | 全部带电部件封闭于 SF₆ 气室，绝缘靠气体、结构紧凑 | DL/T 5222 §6、GB/T 11022 |

## 2. 物理图像

### 2.1 发电机断路器的严苛工况

发电机机端短路时，发电机本身是短路电流源，其 **次暂态电抗 $X_d''$** 决定短路电流。与传统输电短路相比：

- **直流分量衰减慢**：发电机 $X/R$ 大（50~100），直流分量时间常数 $T_a=X/(\omega R)$ 长达 100~300 ms，分闸时直流分量占比可达 50%~75%（常规系统 <30%）。
- **冲击系数 $\kappa$ 超标**：$\kappa$ 可能超过 2.7（常规 $\le2.7$），关合电流校验更严苛。
- **TRV 上升速率高**：机端短路 TRV 标准值比同电压等级常规系统高 2~3 倍。

### 2.2 GIS 的紧凑结构

GIS 将母线、断路器、隔离开关、接地开关、CT/PT、避雷器全部封装于金属外壳内，以 SF₆ 气体（0.4~0.6 MPa）绝缘。

```
           ┌──────── GIS 气室 ────────┐
           │  ┌──DS──┐  ┌──CB──┐      │
  进线 ────┤  │隔离  │──│断路器│──母线│  出线
           │  └──────┘  └──────┘      │
           │  CT  PT  ES  LA          │
           └──────────────────────────┘
```

相比常规空气绝缘（AIS），GIS 占地仅为 AIS 的 10%~15%、不受污秽/海拔影响、运维安全性高，但造价高（2~4 倍）、扩建受限。

## 3. 推导

### 3.1 发电机断路器直流分量校验

发电机机端短路直流分量衰减时间常数：

$$
T_a = \frac{X_d''}{\omega R_a}
$$

| 机组 | $X_d''$ (p.u.) | $R_a$ (p.u.) | $T_a$ (ms) | 分闸时 $I_{dc}/(\sqrt2 I_{ac})$ |
|---|---|---|---|---|
| 300 MW 汽轮 | 0.18 | 0.003 | 190 | 65% |
| 600 MW 汽轮 | 0.20 | 0.002 | 318 | 75% |
| 1000 MW 核电 | 0.21 | 0.002 | 334 | 80% |

GB/T 14824 规定 GCB 须在 $\kappa_{max}=2.7\sim2.9$（直流分量 50%~75%）下开断，常规断路器（GB 1984）在 $\kappa_{max}=2.5$（约 30% 直流）下校验——GCB 要求明显更严苛。

### 3.2 发电机断路器 TRV 标准

GB/T 14824 附录给出的 GCB TRV 标准值（代表性参数）：

| 电压等级 | $u_c$（峰值） | RRRV（kV/μs） | 与常规比 |
|---|---|---|---|
| 24 kV（300 MW 机端） | 44 | 1.5 | 常规 12 kV 仅 0.34 |
| 36 kV（600 MW 机端） | 66 | 2.0 | 常规 40.5 kV 仅 1.0 |

GCB 的 TRV 上升速率约为常规的 4~5 倍——这是 GCB 不能用常规断路器替代的根本原因。

### 3.3 GIS 绝缘配合

GIS 内部采用 SF₆ 气体绝缘，雷电冲击耐受电压（LIWV）与操作冲击耐受电压（SIWV）由 GB/T 11022 规定：

| 电压等级 | 额定 $U_m$ | LIWV (kV) | SIWV (kV) | 工频耐受 (kV) |
|---|---|---|---|---|
| 126 kV GIS | 126 | 550 | — | 230 |
| 252 kV GIS | 252 | 1050 | — | 460 |
| 550 kV GIS | 550 | 1675 | 1175 | 740 |

GIS 绝缘配合须与外部架空线/电缆协调，通常 GIS 首端配置避雷器保护（详见 [TH-022 过电压与绝缘配合](TH-022-overvoltage-mechanism-and-insulation-coordination.md)）。

### 3.4 GIS 间隔与扩建约束

GIS 间隔数固定，扩建须停运相关间隔并打开气室：

$$
N_{bay}=N_{line}+N_{bus}+N_{transformer}+N_{reserve}
$$

扩建约束：① 气室打开后 SF₆ 须回收处理（环保）；② 新旧设备配合面密封性须现场检测；③ 母线停电影响范围大。故 GIS 设计须预留 20%~30% 间隔裕度。

## 4. 与工程实践的联系

- **支撑条目 1**：[TH-026 开关电器选型与开断能力物理基础](TH-026-switchgear-selection-and-breaking-capacity.md)——本条是 TH-026 在发电机机端与 GIS 两类特殊应用场景的深化。
- **支撑条目 2**：[PR-DD-002 变配电所布置](../30-practice/PR-DD-002-substation-layout-and-equipment-selection.md)——GIS 选型直接影响变电所占地面积与布置方案。
- **支撑条目 3**：[TH-015 Park 方程](TH-015-synchronous-machine-park-equations.md) 与 [TH-011 同步电机次暂态电抗](TH-011-synchronous-machine-subtransient-reactance.md)——$X_d''$ 与 $T_a$ 是 GCB 短路电流校验的输入。
- **失效边界**：① GCB 不能用常规断路器替代，直流分量与 TRV 校验须用 GB/T 14824 而非 GB 1984；② GIS 气室泄漏检测灵敏度须 $<10^{-3}$ Pa·m³/s，微小泄漏长期累积会导致绝缘下降；③ GIS 内部故障电弧（母线短路）使气室压力骤增，须有压力释放装置（膜片或阀门），否则外壳破裂；④ GIS 扩建停运时间长（24~72 h），设计阶段须预留间隔；⑤ SF₆ 是强温室气体（GWP=23500），泄漏率须 $<0.5\%$/年，环保法规趋严下逐步向 SF₆-free（如 C4F7N/CO₂ 混合气）发展。
- **下游案例**：[CASE-027 真空截流过电压致电机击穿](../50-case/CASE-027-accident-vacuum-chopping-overvoltage.md)、[CASE-040 2019 非周期分量与开断校验](../50-case/CASE-040-exam-2019-dc-component-breaker-rating.md)、[CASE-047 低压柜电弧光](../50-case/CASE-047-accident-arc-flash-protection-missing-burn.md)

## 5. 关联条目与变更记录

- 关联：[TH-026 开关电器选型与开断能力](TH-026-switchgear-selection-and-breaking-capacity.md)（四额定值与 TRV 基础）、[TH-013 开关电弧物理](TH-013-switching-arc-physics.md)（SF₆ 灭弧机理）、[TH-011 同步电机次暂态电抗](TH-011-synchronous-machine-subtransient-reactance.md)（$X_d''$ 与 $T_a$）、[TH-015 Park 方程](TH-015-synchronous-machine-park-equations.md)（暂态电势与衰减）、[TH-022 过电压与绝缘配合](TH-022-overvoltage-mechanism-and-insulation-coordination.md)（GIS 绝缘配合与避雷器）、[TH-017 电缆波过程与 VFTO](TH-017-cable-wave-process-vfto.md)（GIS 内 VFTO）、[PR-DD-002 变配电所布置](../30-practice/PR-DD-002-substation-layout-and-equipment-selection.md)
- 下游案例：见 §4 列表。

| 版本 | 日期 | 修改内容 | 修改人 |
|---|---|---|---|
| 0.1 | 2026-09-09 | 创建；含 GCB 直流分量与 TRV 标准深化、GIS 结构与绝缘配合、扩建约束、SF₆ 环保失效边界 | KB 管理员 |
