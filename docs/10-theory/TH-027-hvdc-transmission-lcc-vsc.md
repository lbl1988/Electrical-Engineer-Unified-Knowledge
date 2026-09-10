---
id: TH-027
title: 高压直流输电（LCC/VSC-HVDC）
domain: 基础理论
subdomain: 直流输电
voltage_levels: [HV, EHV, UHV]
lifecycle: [设计, 运维]
standards:
  - { code: GB/T 35214-2017, clause: "4", note: "高压直流输电系统技术规范，含 LCC/VSC 主接线与基本参数" }
  - { code: GB/T 30553-2014, clause: "4", note: "高压直流换流站绝缘配合（idt IEC 60700）" }
  - { code: GB/T 37017-2018, clause: "4", note: "柔性直流输电换流站技术规范，规定 MMC 拓扑与控制" }
  - { code: DL/T 1897-2018, clause: "4", note: "柔性直流输电系统运行检修规程" }
status: draft
reviewers: []
version: 0.1
updated: 2026-09-09
---

# 高压直流输电（LCC/VSC-HVDC）

## 1. 定义

**高压直流输电（HVDC）**指将三相交流经换流站整流为直流、经直流线路（电缆或架空线）传输、对端换流站逆变回交流的输电方式。按换流器拓扑分两类：

| 类型 | 换流器件 | 拓扑 | 典型工程 |
|---|---|---|---|
| **LCC（电网换相）** | 半控型晶闸管 | 6 脉波/12 脉波桥 | 葛洲坝—上海 ±500 kV、哈密—郑州 ±800 kV 特高压 |
| **VSC（电压源）** | 全控型 IGBT | 两电平/三电平 NPC/MMC | 舟山 ±200 kV、张北 ±500 kV 柔性直流 |

HVDC 相对 HVAC 的核心优势：① 无功充电电流、距离不受功角稳定限制，适合远距离大容量（>800 km）；② 不需同步运行，可互联非同步电网（如 50 Hz/60 Hz）；③ 海底电缆传输（如跨海互联）经济性优于交流。

## 2. 物理图像

### 2.1 LCC 换流站（典型双极两端系统）

```
整流站(AC→DC)                      逆变站(DC→AC)
AC母线 ─ 换流变 ─ 12脉波桥 ─ 平波电抗 ── ±U_d ── 架空线/电缆 ── ±U_d ─ 平波电抗 ─ 12脉波桥 ─ 换流变 ─ AC母线
       │           │                                │           │
       交流滤波器   DC滤波器                         DC滤波器     交流滤波器
       无功补偿                                     无功补偿
```

LCC 换流阀由晶闸管串联组成，**只能导通不能自关断**，换相依赖交流电网电压过零，故称"电网换相"。整流侧触发角 $\alpha$、逆变侧关断角 $\gamma$，需消耗大量无功（约为有功的 50%~60%），须配套 FC/TCR/SVC 无功补偿。

### 2.2 VSC 换流站（典型 MMC 单极系统）

```
整流站(VSC)                         逆变站(VSC)
AC母线 ─ 联络变 ─ MMC ─ 平波电抗 ── ±U_d ── 直流电缆 ── ±U_d ─ 平波电抗 ─ MMC ─ 联络变 ─ AC母线
                    │                                    │
                  子模块                              子模块
                  (半桥+电容)                          (半桥+电容)
```

VSC-MMC 每相由上百子模块串联，IGBT 自关断可输出任意波形，**不依赖电网换相**，故称"自换相"。可在无源网络中独立建压（黑启动）、有功无功独立解耦控制、谐波低无须大容量滤波器，是当前海上风电送出与城市柔性互联主流。

## 3. 推导

### 3.1 LCC 直流电压与功率

整流侧直流电压（6 脉波桥，理想情况）：

$$
U_{dR}=\frac{3\sqrt2}{\pi}U_{LL}\cos\alpha-\frac{3}{\pi}X_c I_d
$$

逆变侧（从逆变站看入）：

$$
U_{dI}=\frac{3\sqrt2}{\pi}U_{LL}\cos\gamma+\frac{3}{\pi}X_c I_d
$$

直流功率 $P_d=U_d I_d$，$I_d=(U_{dR}-U_{dI})/R_{line}$。LCC 控制：整流侧调 $\alpha$（正常 $15^\circ\sim20^\circ$）、逆变侧调 $\gamma$（关断角须保证 $\gamma\ge \omega_0 t_{off}$，否则换相失败）。

### 3.2 LCC 换相失败判据

晶闸管关断后须承受反向电压的时间（关断角 $\gamma$）大于器件关断恢复时间对应的电角度（典型 $7^\circ$~$10^\circ$）。若交流电压跌落使 $\gamma<\gamma_{min}$，导通阀未恢复阻断即承受正向电压，形成**换相失败**——直流短路、功率骤降，是最常见故障。换相失败概率：

$$
P_{CF}\propto \frac{1}{\text{SCR}_{AC}^2}\quad \text{SCR 为交流侧短路比}
$$

SCR<2.5 的弱交流系统换相失败风险极高，是 LCC 在弱电网应用受限的根本原因。

### 3.3 VSC-MMC 输出电压与有功无功解耦

MMC 子模块电容平均电压 $U_c$，每相投入 $N_{on}$ 个子模块，输出端对中性点电压：

$$
u_{ph}=\frac{N_{on}}{N_{total}}U_{dc}
$$

通过 dq 旋转坐标系下电流解耦控制：

$$
P=\frac{3}{2}U_s i_d,\quad Q=\frac{3}{2}U_s i_q
$$

$i_d$ 控有功、$i_q$ 控无功——**独立解耦**，这是 VSC 相对 LCC 的核心优势（LCC 有功无功强耦合，无功只能滞后）。

### 3.4 两种 HVDC 容量与损耗对比

| 指标 | LCC | VSC-MMC |
|---|---|---|
| 单极容量 | 1.5~6 GW | 0.3~1.5 GW（递增中） |
| 直流电压 | ±500~±1100 kV | ±200~±800 kV |
| 换流站损耗 | 0.5%~0.7% | 0.8%~1.2%（含子模块开关损耗） |
| 无功补偿 | 需大容量 FC/SVC | 自身可发无功，无须补偿 |
| 黑启动 | 不支持 | 支持 |
| 弱电网适应 | 差（SCR>3） | 强（可接入无源网络） |

## 4. 与工程实践的联系

- **支撑条目 1**：[PR-ES-001 储能接入](../30-practice/PR-ES-001-energy-storage-integration.md) 与 [TH-024 电力电子变换器与 PWM](TH-024-power-electronic-converters-and-pwm.md)——MMC 拓扑源自 TH-024 的子模块化扩展，构网型 VSC-HVDC 与储能 PCS 共享控制基础。
- **支撑条目 2**：[PR-PQ-001 电能质量治理](../30-practice/PR-PQ-001-pq-compensation-design.md) 与 [TH-020 电力系统稳定性分类](TH-020-power-system-stability-classification.md)——HVDC 换相失败引发交流侧电压跌落与低频振荡，是电能质量与系统稳定的重要扰动源。
- **支撑条目 3**：[CASE-028 海上风电升压站](../50-case/CASE-028-composite-offshore-wind-substation.md)——海上风电送出主流采用 VSC-HVDC（柔性直流），本条给出拓扑与控制物理基础。
- **失效边界**：① LCC 直流电压公式略去换相重叠角，实际换相重叠角 $\mu$ 取决于 $X_c I_d$，大电流时 $\mu$ 增大须修正；② LCC 最小滤波/无功须按额定容量的 50%~60% 配置，否则谐波与电压偏差超标；③ VSC-MMC 子模块电容电压均衡须均压算法，子模块数 $N<50$ 时均压误差大、谐波升高；④ 直流侧单极接地故障与双极短路属不同工况，LCC 可清除单极故障但 VSC 须闭锁全停（这是 LCC 在架空线长距离输电仍占主流原因之一）；⑤ HVDC 输电不能像交流那样中途 T 接分支，须点对点或多端专用接线。
- **下游案例**：[CASE-028 海上风电升压站](../50-case/CASE-028-composite-offshore-wind-substation.md)、[CASE-048 新能源汇集站继保](../50-case/CASE-048-composite-renewable-collector-station-protection.md)

## 5. 关联条目与变更记录

- 关联：[TH-024 电力电子变换器与 PWM](TH-024-power-electronic-converters-and-pwm.md)（MMC 拓扑与 SVPWM）、[TH-020 电力系统稳定性分类](TH-020-power-system-stability-classification.md)（换相失败与低频振荡）、[TH-019 输电线路参数](TH-019-transmission-line-parameters-long-line.md)（直流线路电阻与电压降）、[PR-ES-001 储能接入](../30-practice/PR-ES-001-energy-storage-integration.md)、[PR-PQ-001 电能质量治理](../30-practice/PR-PQ-001-pq-compensation-design.md)
- 下游案例：见 §4 列表。

| 版本 | 日期 | 修改内容 | 修改人 |
|---|---|---|---|
| 0.1 | 2026-09-09 | 创建；含 LCC/VSC 双拓扑、LCC 换相失败判据与 SCR 关系、VSC 有功无功解耦 dq 控制、弱电网失效边界 | KB 管理员 |
