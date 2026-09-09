---
id: REF-HB-001
title: 设计手册速查索引（常用公式 / 典型值 / 章节映射）
domain: REF
subdomain: 手册速查
voltage_levels: [LV, MV, HV, EHV]
lifecycle: [设计, 考试]
standards:
  - { code: 2026 年度考纲公告, clause: "附件8/9", note: "供配电 4 册 + 发输变电 6 册设计手册目录" }
status: published
version: 1.0
updated: 2026-09-09
---

# 设计手册速查索引（常用公式 / 典型值 / 章节映射）

> **用途**：考试与工程设计中快速定位手册公式、典型值与章节。手册与规范冲突时以规范为准（考纲官方注）。
> **配套**：→ [CALC 计算库](../40-calc/)（完整推导）｜ [TH 理论层](../10-theory/)（物理机理）｜ [PR 实践层](../30-practice/)（设计流程）

## 1. 手册总目录（10 册）

### 1.1 供配电考纲手册（4 册）

| # | 简称 | 全名 | 出版社 | 速查代号 |
|---|---|---|---|---|
| G1 | 供配电手册（第四版） | 工业与民用供配电设计手册（第四版） | 中国电力出版社 | **G4** |
| G2 | 钢铁手册 | 钢铁企业电力设计手册 | 冶金工业出版社 | **GT** |
| G3 | 照明手册（第三版） | 照明设计手册（第三版） | 中国电力出版社 | **LT** |
| G4 | 线路手册 | 电力工程高压送电线路设计手册（第二版） | 中国电力出版社 | **TL** |

### 1.2 发输变电考纲手册（6 册）

| # | 简称 | 全名 | 出版社 | 速查代号 |
|---|---|---|---|---|
| T1 | 一次手册 | 电力工程电气设计手册（电气一次部分） | 中国电力出版社 | **P1** |
| T2 | 二次手册 | 电力工程电气设计手册（电气二次部分） | 中国电力出版社 | **P2** |
| T3 | 系统手册 | 电力系统设计手册 | 中国电力出版社 | **PS** |
| T4 | 水电一次 | 水电站机电设计手册（电气一次分册） | 水利电力出版社 | **H1** |
| T5 | 水电二次 | 水电站机电设计手册（电气二次分册） | 水利电力出版社 | **H2** |
| T6 | 线路手册 | 电力工程高压送电线路设计手册（第二版） | 中国电力出版社 | **TL**（同 G4） |

## 2. 常用公式速查（按主题分类）

### 2.1 短路电流计算

| 公式 | 表达式 | 手册章节 | 本库条目 |
|---|---|---|---|
| 三相短路对称电流 | $I_k''=\frac{cU_n}{\sqrt3\,Z_{sys}}$ | G4 §4.1 / P1 表 4-1 | [CALC-SC-001](../40-calc/CALC-SC-001-低压三相短路电流计算.md) |
| 高压系统短路（IEC 60909） | $I_k''=\frac{cU_n}{\sqrt3\,Z_{k}}$（$c=1.05/1.1$） | P1 §4 / PS §6 | [CALC-SC-002](../40-calc/CALC-SC-002-hv-short-circuit-iec60909.md) |
| 峰值短路电流 | $i_p=\kappa\sqrt2\,I_k''$（$\kappa$ 查系数表） | G4 表 4-6 | CALC-SC-001 §3 |
| 电机反馈电流 | $I_{km}''=\frac{E''}{X_d''}$（衰减 $\sim$3T） | P1 §4.3 | [TH-011](../10-theory/TH-011-synchronous-machine-subtransient-reactance.md) |
| 最小短路电流（相保） | $I_{k1min}=\frac{cU_n}{\sqrt3\,Z_{loop}}$ | G4 §4.5 | CALC-SC-001 §3 |

### 2.2 负荷计算

| 公式 | 表达式 | 手册章节 | 本库条目 |
|---|---|---|---|
| 需要系数法 | $P_{30}=P_e\cdot K_d$；$Q_{30}=P_{30}\tan\varphi$ | G4 §1.2 | [CALC-LD-001](../40-calc/CALC-LD-001-demand-factor-method.md) |
| 需要系数综合系数 | $K_\Sigma=\sum P_{30,i}/\sum(P_{e,i}\cdot K_{d,i})$ | G4 §1.3 | CALC-LD-001 §3 |
| 利用系数法 | $P_{av}=P_e\cdot K_l$（工业用） | GT §1.1 | CALC-LD-001 §5 |
| 视在功率 | $S_{30}=\sqrt{P_{30}^2+Q_{30}^2}$ | G4 §1 | CALC-LD-001 |

### 2.3 保护整定

| 公式 | 表达式 | 手册章节 | 本库条目 |
|---|---|---|---|
| 电流速断（I 段） | $I_{set}^I=K_{rel}\,I_{k,max}^{末端}$ | P2 §6 / G4 §7 | [CALC-PT-001](../40-calc/CALC-PT-001-protection-setting.md) |
| 限时电流速断（II 段） | $I_{set}^{II}=K_{rel}\,I_{k,max}^{下级末端}$ | P2 §6 | CALC-PT-001 §3 |
| 定时限过流（III 段） | $I_{set}^{III}=\frac{K_{rel}K_{ss}}{K_r}\,I_{load,max}$ | P2 §6 | [PR-PE-002](../30-practice/PR-PE-002-relay-protection-coordination-deepening.md) |
| 距离保护 I 段 | $Z_{set}^I=0.85\,Z_{line}$ | P2 §7 | [CALC-PT-002](../40-calc/CALC-PT-002-distance-protection-setting.md) |
| 灵敏系数 | $K_{sen}=I_{k,min}/I_{set}\ge1.3\sim1.5$ | P2 §6 | PR-PE-002 §3 |
| 低压断路器长延时 | $I_{r1}\le I_z$；$I_{r2}=4\sim10\,I_{r1}$（t=2~10s） | G4 §6 | [PR-DD-001](../30-practice/PR-DD-001-lv-breaker-selection.md) |
| 热继电器 | $I_r=(1.05\sim1.2)\,I_N$ | G4 §6 | [PR-PS-002](../30-practice/PR-PS-002-motor-control-and-starting.md) |

### 2.4 无功补偿

| 公式 | 表达式 | 手册章节 | 本库条目 |
|---|---|---|---|
| 补偿容量 | $Q_C=P(tan\varphi_1-tan\varphi_2)$ | G4 §9 / PS §8 | [CALC-RC-001](../40-calc/CALC-RC-001-reactive-compensation.md) |
| 调谐次数 | $\nu=\frac{1}{\sqrt{p}}$（$p$=电抗率） | G4 §9.4 | [PR-PQ-001](../30-practice/PR-PQ-001-pq-compensation-design.md) |
| 谐振容量 | $Q_C\ne n^2\frac{S_{sc}}{100}$ | G4 §9.4 | TH-008 §3 |
| PCC 谐波允许值 | $I_{h,允许}=I_{h,基准}(S_i/S_t)^{1/\alpha}$ | G4 附录 | [PR-PQ-002](../30-practice/PR-PQ-002-power-quality-monitoring-and-mitigation.md) |

### 2.5 接地

| 公式 | 表达式 | 手册章节 | 本库条目 |
|---|---|---|---|
| 接触电压 | $U_t=I_E\,R_E\,K_i\,K_m$ | P1 §14 / G4 §13 | [TH-005](../10-theory/TH-005-touch-step-voltage.md) |
| 接地电阻（自然） | $R\approx0.5\,\rho/\sqrt{A}$ | G4 §13 | [CALC-GR-001](../40-calc/CALC-GR-001-grounding-grid-design.md) |
| 接地电阻（人工） | $R=0.5\,\rho/L$（单根水平极） | P1 §14 | CALC-GR-001 §3 |
| 跨步电压 | $U_s=I_E\,R_E\,K_s$ | P1 §14 | TH-005 §3 |
| PE 截面 | $S\le16$：PE=S；$16<S\le35$：PE=16；$S>35$：PE=S/2 | G4 §13 | [PR-GR-002](../30-practice/PR-GR-002-earthing-arrangement.md) |

### 2.6 电缆与线路

| 公式 | 表达式 | 手册章节 | 本库条目 |
|---|---|---|---|
| 载流量校正 | $I_z'=I_z\,K_T\,K_N\,K_G\,K_P$ | G4 §8 | [PR-DD-003](../30-practice/PR-DD-003-cable-routing-and-installation.md) |
| 热稳定截面 | $S_{min}=\frac{I_k\sqrt{t}}{K}$ | G4 §8 / P1 §5 | [CALC-CD-001](../40-calc/CALC-CD-001-cable-ampacity-correction.md) |
| 电压降（三相） | $\Delta U=\frac{\sqrt3\,I_B\,L(R\cos\varphi+X\sin\varphi)}{U_N}$ | G4 §8 | [CALC-VL-001](../40-calc/CALC-VL-001-voltage-deviation-and-loss.md) |
| 线路参数（长线） | $Z_c=\sqrt{z/y}$；$\gamma=\sqrt{zy}$ | TL §2 / PS §4 | [TH-019](../10-theory/TH-019-transmission-line-parameters-long-line.md) |
| 线路波阻抗 | $Z_c\approx\sqrt{L_0/C_0}$ | TL §2 | TH-017 §3 |

### 2.7 照明

| 公式 | 表达式 | 手册章节 | 本库条目 |
|---|---|---|---|
| 利用系数法 | $E=\frac{N\,\Phi\,U\,K}{A}$ | LT §4 | [CALC-LT-001](../40-calc/CALC-LT-001-lumen-method.md) |
| 逐点法 | $E=\frac{I_\theta\cos^3\theta}{h^2}$ | LT §5 | [CALC-LT-002](../40-calc/CALC-LT-002-point-illuminance-method.md) |
| 室形指数 | $RI=\frac{L\times W}{h(L+W)}$ | LT §4 | CALC-LT-001 §3 |
| LPD 校核 | $LPD=\frac{P_{total}}{A}\le$ GB/T 50034 限值 | LT §4 | [CHG-001](../20-standards/changelog/CHG-001-GBT50034-2024.md) |

### 2.8 电机与传动

| 公式 | 表达式 | 手册章节 | 本库条目 |
|---|---|---|---|
| 电机额定电流 | $I_N=\frac{P}{\sqrt3\,U_N\cos\varphi\,\eta}$ | G4 §12 | [PR-PS-002](../30-practice/PR-PS-002-motor-control-and-starting.md) |
| 启动压降 | $\Delta U_{st}=\frac{\sqrt3\,I_{st}\,Z_{sys}}{U_N}$ | G4 §12 | [CALC-MS-001](../40-calc/CALC-MS-001-motor-starting-voltage-drop.md) |
| 启动转矩倍数 | $T_{st}'=T_{st}(U_{st}/U_N)^2$ | GT §6 | PR-PS-002 §3 |
| V/f 控制 | $E/f\approx常量$（恒磁通） | — | [TH-033](../10-theory/TH-033-induction-motor-vfd-control-strategy.md) |
| 电机温升 | $\Delta T=\frac{P_{loss}}{R_{th}}$（稳态） | GT §6 | [CALC-MS-002](../40-calc/CALC-MS-002-motor-temperature-rise.md) |

### 2.9 防雷与 SPD

| 公式 | 表达式 | 手册章节 | 本库条目 |
|---|---|---|---|
| 雷电流幅值 | $I_0=200\sim300$kA（10/350μs, Type 1） | P1 §15 | [TH-009](../10-theory/TH-009-lightning-physics.md) |
| SPD 电压保护水平 | $U_p\le0.8\,U_w$ | G4 §14 | [PR-GR-003](../30-practice/PR-GR-003-spd-selection-and-coordination.md) |
| 级间退耦距离 | $L\ge(U_{p1}-U_{p2})/(di/dt)$ | G4 §14 | PR-GR-003 §3 |
| 滚球半径 | $R$（一类30m/二类45m/三类60m） | P1 §15 | [PR-GR-001](../30-practice/PR-GR-001-lightning-protection-design.md) |
| 接闪器保护范围 | $r_x=\sqrt{h(2R-h)}\cdot\sqrt{h_x(2R-h_x)}$ | P1 §15 | PR-GR-001 §3 |

### 2.10 蓄电池与直流

| 公式 | 表达式 | 手册章节 | 本库条目 |
|---|---|---|---|
| 蓄电池容量（恒流） | $C=\frac{I\cdot t}{\eta\,K_T}$ | P2 §8 / G4 §10 | [CALC-BT-001](../40-calc/CALC-BT-001-battery-capacity.md) |
| 后备时间 | $t=\frac{C\cdot\eta\,K_T}{I}$ | P2 §8 | [CALC-BT-002](../40-calc/CALC-BT-002-ups-battery-autonomy.md) |
| 恒功率法 | $P_{cell}=\frac{P_{UPS}}{n\cdot U_{end}}$ | P2 §8 | [PR-PS-003](../30-practice/PR-PS-003-ups-and-battery-design.md) |

### 2.11 柴油发电机

| 公式 | 表达式 | 手册章节 | 本库条目 |
|---|---|---|---|
| 发电机容量 | $S_G\ge\frac{P_{load}}{K_{step}\cos\varphi}$（启动压降校核） | G4 §3 | [CALC-DG-001](../40-calc/CALC-DG-001-diesel-generator-capacity.md) |
| 启动容量倍数 | $K_{step}=1.0\sim1.5$（视启动方式） | G4 §3 | CALC-DG-001 §3 |

## 3. 典型值速查表

### 3.1 变压器参数典型值

| 容量 (kVA) | $u_k$ (%) | 空载损耗 (W) | 负载损耗 (W) | 备注 |
|---|---|---|---|---|
| 315 | 4 | 670 | 3650 | 10/0.4kV 干变 |
| 630 | 4.5 | 950 | 6300 | 10/0.4kV 干变 |
| 1000 | 6 | 1500 | 9000 | 10/0.4kV 干变 |
| 1600 | 6 | 2100 | 13000 | 10/0.4kV 干变 |
| 31500 | 10.5 | 28000 | 145000 | 110/10kV 油浸 |
| 63000 | 12.5 | 45000 | 260000 | 220/35kV 油浸 |

> 来源：GB/T 6451（油浸）/ GB/T 10228（干式）；手册 G4 表 5-2 / P1 表 2-8

### 3.2 短路阻抗典型值

| 系统位置 | $Z_{sys}$ (mΩ) | $I_k$ 估算 | 来源 |
|---|---|---|---|
| 变压器二次侧直接 | $Z_T=u_k\%\cdot U_N^2/(100\,S_N)$ | $I_k=S_N/Z_T$ | G4 §4 |
| 1600kVA/0.4kV | 9.5 | ~24kA | G4 表 4-3 |
| 1000kVA/0.4kV | 15.2 | ~15kA | G4 表 4-3 |
| 上游 10kV 母线 | 0.5~5 | 视系统短路容量 | P1 §4 |

### 3.3 需要系数典型值

| 负荷类型 | $K_d$ | $\cos\varphi$ | $\tan\varphi$ | 来源 |
|---|---|---|---|---|
| 照明（办公） | 0.8 | 0.9 | 0.484 | G4 表 1-2 |
| 照明（仓库） | 0.6 | 0.8 | 0.750 | G4 表 1-2 |
| 空调（集中） | 0.7 | 0.8 | 0.750 | G4 表 1-2 |
| 电梯 | 0.6 | 0.7 | 1.020 | G4 表 1-2 |
| 水泵 | 0.75 | 0.8 | 0.750 | G4 表 1-2 |
| 风机 | 0.7 | 0.8 | 0.750 | G4 表 1-2 |
| 电焊机 | 0.35 | 0.5 | 1.732 | G4 表 1-2 |
| 起重机 | 0.2 | 0.5 | 1.732 | G4 表 1-2 |

### 3.4 保护整定系数典型值

| 系数 | 典型值 | 适用场景 | 来源 |
|---|---|---|---|
| $K_{rel}$ | 1.2~1.3 | 电流保护 | P2 §6 |
| $K_{ss}$（自启动） | 1.5（一般）/ 2~3（电机集中） | III 段 | P2 §6 |
| $K_r$（返回系数） | 0.85（电磁）/ 0.95（微机） | III 段 | P2 §6 |
| $\Delta t$ | 0.3s（标准）/ 0.5s（保守）/ 0.2s（GIS） | 阶梯时限 | DL/T 553 |
| $K_{sen}$ | ≥1.3（近）/ ≥1.2（远） | 灵敏度 | DL/T 553 |

### 3.5 电缆 R/X 参数典型值（铜芯 XLPE）

| 截面 (mm²) | R (mΩ/m) | X (mΩ/m) | 载流量 (A, 30°C 桥架) | 来源 |
|---|---|---|---|---|
| 16 | 1.15 | 0.082 | 80 | G4 表 8-3 |
| 35 | 0.529 | 0.080 | 125 | G4 表 8-3 |
| 70 | 0.268 | 0.078 | 180 | G4 表 8-3 |
| 95 | 0.194 | 0.076 | 220 | G4 表 8-3 |
| 120 | 0.153 | 0.075 | 255 | G4 表 8-3 |
| 185 | 0.099 | 0.073 | 320 | G4 表 8-3 |
| 240 | 0.075 | 0.072 | 375 | G4 表 8-3 |

### 3.6 防雷参数典型值

| 防雷等级 | 滚球半径 $R$ (m) | 接闪带高度 | $I_{imp}$ (kA) | 来源 |
|---|---|---|---|---|
| 一类 | 30 | 屋面 $\ge0.3$m | 12.5（Type 1） | GB 50057 |
| 二类 | 45 | 屋面 $\ge0.3$m | 12.5（Type 1） | GB 50057 |
| 三类 | 60 | 屋面 $\ge0.3$m | 8（Type 1 可选） | GB 50057 |
| SPD Type 2 | — | — | $I_n$=20kA, $I_{max}$=40kA | GB/T 18802 |

### 3.7 照度标准速查（GB/T 50034-2024 常用值）

| 场所 | 维持平均照度 $E_m$ (lx) | UGR | U0 | LPD 限值 (W/m²) |
|---|---|---|---|---|
| 办公室（一般） | 300 | 19 | 0.40 | ≤8.0 |
| 会议室 | 300 | 19 | 0.40 | ≤8.0 |
| 设计室 | 500 | 19 | 0.60 | ≤12.0 |
| 走廊 | 100 | 22 | 0.40 | ≤3.5 |
| 楼梯间 | 50~100 | — | 0.40 | ≤2.5 |
| 地下车库 | 50~100 | — | 0.25 | ≤2.5 |
| 商店营业厅 | 300~500 | 22 | 0.40 | ≤10.0 |

> 来源：GB/T 50034-2024 + [CHG-001 变更说明](../20-standards/changelog/CHG-001-GBT50034-2024.md)

## 4. 手册章节与本库条目映射

### 4.1 供配电手册 G4（第四版）章节映射

| 手册章节 | 内容 | 本库条目链接 |
|---|---|---|
| G4 §1 | 负荷计算 | [CALC-LD-001](../40-calc/CALC-LD-001-demand-factor-method.md)·[PR-PS-001](../30-practice/PR-PS-001-load-classification.md) |
| G4 §3 | 柴油发电机 | [CALC-DG-001](../40-calc/CALC-DG-001-diesel-generator-capacity.md) |
| G4 §4 | 短路计算 | [CALC-SC-001](../40-calc/CALC-SC-001-低压三相短路电流计算.md)·[TH-003](../10-theory/TH-003-symmetrical-components.md) |
| G4 §5 | 变压器选择 | [TH-006](../10-theory/TH-006-transformer-leakage-impedance.md)·[TH-023](../10-theory/TH-023-transformer-parallel-operation-and-circulating-current.md) |
| G4 §6 | 低压断路器/保护 | [PR-DD-001](../30-practice/PR-DD-001-lv-breaker-selection.md)·[PR-PS-002](../30-practice/PR-PS-002-motor-control-and-starting.md) |
| G4 §8 | 电缆与线路 | [PR-DD-003](../30-practice/PR-DD-003-cable-routing-and-installation.md)·[CALC-CD-001](../40-calc/CALC-CD-001-cable-ampacity-correction.md) |
| G4 §9 | 无功补偿 | [CALC-RC-001](../40-calc/CALC-RC-001-reactive-compensation.md)·[PR-PQ-001](../30-practice/PR-PQ-001-pq-compensation-design.md) |
| G4 §10 | 蓄电池 | [CALC-BT-001](../40-calc/CALC-BT-001-battery-capacity.md)·[PR-PS-003](../30-practice/PR-PS-003-ups-and-battery-design.md) |
| G4 §12 | 电动机 | [PR-PS-002](../30-practice/PR-PS-002-motor-control-and-starting.md)·[TH-033](../10-theory/TH-033-induction-motor-vfd-control-strategy.md) |
| G4 §13 | 接地 | [PR-GR-002](../30-practice/PR-GR-002-earthing-arrangement.md)·[CALC-GR-001](../40-calc/CALC-GR-001-grounding-grid-design.md) |
| G4 §14 | 防雷与 SPD | [PR-GR-001](../30-practice/PR-GR-001-lightning-protection-design.md)·[PR-GR-003](../30-practice/PR-GR-003-spd-selection-and-coordination.md) |

### 4.2 发输变电一次手册 P1 章节映射

| 手册章节 | 内容 | 本库条目链接 |
|---|---|---|
| P1 §2 | 变压器参数 | [TH-006](../10-theory/TH-006-transformer-leakage-impedance.md) |
| P1 §4 | 短路计算（高压） | [CALC-SC-002](../40-calc/CALC-SC-002-hv-short-circuit-iec60909.md)·[TH-011](../10-theory/TH-011-synchronous-machine-subtransient-reactance.md) |
| P1 §5 | 导体选择 | [TH-019](../10-theory/TH-019-transmission-line-parameters-long-line.md) |
| P1 §6 | 配电装置 | [PR-DD-002](../30-practice/PR-DD-002-substation-layout-and-equipment-selection.md) |
| P1 §14 | 接地 | [TH-005](../10-theory/TH-005-touch-step-voltage.md)·[TH-031](../10-theory/TH-031-grounding-transformer-and-resistor-selection.md) |
| P1 §15 | 防雷 | [TH-009](../10-theory/TH-009-lightning-physics.md)·[TH-022](../10-theory/TH-022-overvoltage-mechanism-and-insulation-coordination.md) |

### 4.3 发输变电二次手册 P2 章节映射

| 手册章节 | 内容 | 本库条目链接 |
|---|---|---|
| P2 §6 | 电流保护 | [CALC-PT-001](../40-calc/CALC-PT-001-protection-setting.md)·[PR-PE-002](../30-practice/PR-PE-002-relay-protection-coordination-deepening.md) |
| P2 §7 | 距离保护 | [CALC-PT-002](../40-calc/CALC-PT-002-distance-protection-setting.md) |
| P2 §8 | 直流系统 | [CALC-BT-001](../40-calc/CALC-BT-001-battery-capacity.md) |
| P2 §9 | 变压器保护 | [TH-034](../10-theory/TH-034-transformer-inrush-current-and-differential-protection.md)·[TH-014](../10-theory/TH-014-magnetic-circuit-saturation.md) |

## 5. 考试速查提示

### 5.1 供配电考试常用页码标记

| 主题 | 手册 | 常查页 | 考试频度 |
|---|---|---|---|
| 负荷 $K_d$ 表 | G4 | 表 1-2 | ★★★ |
| 短路阻抗计算 | G4 | §4.2 | ★★★ |
| 断路器选型 | G4 | §6.3 | ★★★ |
| 电缆载流量 | G4 | 表 8-3~8-7 | ★★★ |
| 无功补偿 | G4 | §9.2 | ★★ |
| 蓄电池 | G4 | §10 | ★★ |
| 照度/利用系数 | LT | §4 表 | ★★★ |
| 接地计算 | G4 | §13 | ★★ |

### 5.2 发输变电考试常用页码标记

| 主题 | 手册 | 常查页 | 考试频度 |
|---|---|---|---|
| 短路计算 | P1 | §4 表 4-1 | ★★★ |
| 导体选择 | P1 | §5 | ★★★ |
| 配电装置 | P1 | §6 | ★★ |
| 电流保护 | P2 | §6 | ★★★ |
| 距离保护 | P2 | §7 | ★★ |
| 接地 | P1 | §14 | ★★★ |
| 防雷 | P1 | §15 | ★★★ |
| 线路力学 | TL | §3~§5 | ★★ |

## 6. 维护规则

- 手册新版发布后（如 G4 第五版）→ 本索引逐表 diff → 标注变动 → 触发 changelog
- 本库 CALC/TH/PR 条目新增后 → 回填本索引 §2~§4 对应行
- 公式编号以手册最新版为准，本索引仅标注章节号

## 7. 变更记录

| 版本 | 日期 | 修改内容 | 修改人 |
|---|---|---|---|
| 1.0 | 2026-09-09 | 创建；含 10 册手册目录、11 主题公式速查、7 类典型值速查表、4 册手册章节映射 | KB 管理员 |
