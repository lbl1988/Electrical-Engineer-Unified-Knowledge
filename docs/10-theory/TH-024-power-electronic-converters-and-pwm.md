---
id: TH-024
title: 电力电子变换器基础拓扑与 PWM
domain: 基础理论
subdomain: 电力电子
voltage_levels: [LV, MV, HV]
lifecycle: [设计, 验收, 运维]
standards:
  - { code: GB/T 12668.1-2023, clause: "3", note: "调速电气传动系统（idt IEC 61800-1），含变流器一般要求与拓扑定义" }
  - { code: GB/T 21413.1-2018, clause: "4", note: "铁路应用 电力电子变流器（idt IEC 61287-1）" }
  - { code: GB/T 19939-2016, clause: "5", note: "光伏并网逆变器技术要求，含谐波/低电压穿越/反孤岛" }
  - { code: GB/T 34122-2023, clause: "4", note: "电化学储能 PCS 技术规范，含构网型与跟网型控制约定" }
status: draft
reviewers: []
version: 0.1
updated: 2026-09-09
---

# 电力电子变换器基础拓扑与 PWM

## 1. 定义

**电力电子变换器**指以功率半导体器件（IGBT、SiC MOSFET、IGCT 等）为开关，按控制策略周期性通断以实现电能形态（DC/AC/AC/DC）与参数变换的装置。按变换方向分类：

| 类型 | 输入→输出 | 典型拓扑 | 应用 |
|---|---|---|---|
| 整流（AC→DC） | 三相 AC → DC | 二极管不控 / PWM 可控整流 / 12 脉波 | 直流电源、变频器前级 |
| 逆变（DC→AC） | DC → 三相 AC | 三相两电平 / 三电平 NPC / MMC | PV/储能 PCS、变频器后级、HVDC |
| 斩波（DC→DC） | DC → DC | Buck / Boost / Buck-Boost | 直流微网、光伏 MPPT、HVDC |
| 交-交（AC→AC） | AC → AC | 矩阵变换器 / 周波变流器 | 大功率直驱调速 |

**PWM（脉宽调制）**：通过高频通断（开关频率 $f_{sw}$ 远高于基波频率 $f_0$）的占空比变化等效出低频交流或可控直流的方法。

| 物理量 | 符号 | 单位 |
|---|---|---|
| 开关频率 | $f_{sw}$ | kHz~MHz |
| 调制比 | $m_a=A_m/A_c$ | — |
| 载波比（频率比） | $m_f=f_{sw}/f_0$ | — |
| 输出基波电压 | $U_{o,1}$ | V |
| 直流母线电压 | $U_{dc}$ | V |
| 调制度（空间矢量） | $M=|U_{ref}|/(U_{dc}/2)$ | — |
| 总谐波失真 | $THD$ | % |

## 2. 物理图像

**三相两电平电压型逆变桥**（最基础拓扑）由三组 IGBT 上下桥臂组成，输出端接负载。每组桥臂只有两个开关状态（上通下断 / 上断下通），输出端对中性点 N 的电位为 $+U_{dc}/2$ 或 $-U_{dc}/2$ —— **两电平**。

```
              +U_dc ──────────┬─────────┬─────────
                          ┌──┴──┐  ┌──┴──┐  ┌──┴──┐
                          │     │  │     │  │     │
                          T1   T3   T5
                          │     │  │     │  │     │
输出 ──────●a─────────●b─────────●c
                          │     │  │     │  │     │
                          T2   T4   T6
                          │     │  │     │  │     │
                          └──┬──┘  └──┬──┘  └──┬──┘
              -U_dc ──────────┴─────────┴─────────
```

**SPWM（正弦脉宽调制）**：载波 $u_c$ 为高频三角波，调制波 $u_m$ 为低频正弦波，比较得到开关信号。当 $u_m>u_c$ 时上桥臂导通，$u_m<u_c$ 时下桥臂导通。输出端在 $+U_{dc}/2$ 与 $-U_{dc}/2$ 间快速切换，平均值为按 $u_m$ 变化的低频正弦。

**SVPWM（空间矢量 PWM）**：把三相电压合成为旋转电压矢量 $\vec U_s$，通过 6 个有效矢量和 2 个零矢量的时间组合（伏秒平衡）逼近参考矢量轨迹——比 SPWM 直流利用率高 15.5%（$\sqrt{3}/2$ vs $1$）。

**三电平 NPC**：每组桥臂加 2 个钳位二极管，输出端可取 $+U_{dc}/2$、0、$-U_{dc}/2$ 三个电平，输出波形更接近正弦、$du/dt$ 减半、谐波低，适合 MV 与 HV 应用（典型 SVG、HVDC、地铁牵引）。

**MMC（模块化多电平）**：每相由若干子模块（半桥或全桥 + 电容）串联，输出电平数随子模块数线性增加，波形接近正弦、无须高频滤波、可扩展至 UHV HVDC（典型柔性直流 ±320 kV~±800 kV）。

## 3. 推导

### 3.1 SPWM 输出基波

正弦调制波 $u_m(t)=M\sin(\omega_0 t)$ 与高频三角载波 $u_c(t)$（峰峰值 $1$、频率 $f_{sw}$）比较，输出端基波幅值（线性调制区 $M\le 1$）：

$$
U_{o,1}=\frac{U_{dc}}{2}M
$$

| 调制比 $M$ | 输出基波幅值（相对 $U_{dc}$） | 工程意义 |
|---|---|---|
| 0 | 0 | 无输出 |
| 0.5 | 0.25 $U_{dc}$ | 中等调制 |
| 1.0 | 0.5 $U_{dc}$ | 线性区上限 |
| $>1$ | $>0.5U_{dc}$（非线性区） | 过调制，谐波急升 |

### 3.2 SVPWM 直流利用率

SVPWM 隐含注入三次谐波（零序分量），使相电压基波幅值：

$$
U_{o,1}^{SVPWM}=\frac{U_{dc}}{\sqrt{3}}=0.577\,U_{dc}
$$

比 SPWM 线性区（0.5 $U_{dc}$）高 $\sqrt{3}/2/0.5=\sqrt{3}/1\approx 1.155$ 倍，即 **直流利用率高 15.5%**。这是 SVPWM 成为工业主流的物理理由。

### 3.3 三电平 NPC 输出谐波

三电平输出电压谐波次数集中在 $m_f\pm 2$、$2m_f\pm 1$（$m_f=f_{sw}/f_0$），幅值与电平数 $N$ 关系（Bessel 函数展开）：

$$
THD\propto\frac{1}{N-1}
$$

三电平（$N=3$）THD 比两电平（$N=2$）低约一半，开关损耗同 $f_{sw}$ 下降可补偿，是中高压主流方案。

### 3.4 开关损耗

每个 IGBT 每周期开关损耗：

$$
P_{sw}=\frac{1}{2}U_{dc}I_{pk}(t_{on}+t_{off})f_{sw}
$$

开关频率越高，损耗越大；SiC MOSFET 的 $t_{on}+t_{off}$ 比 Si IGBT 小约 50%~70%，可在相同损耗下提高 $f_{sw}$ 至 50~100 kHz，是当前光伏/储能 PCS 升级方向。

### 3.5 跟网型与构网型控制（GB/T 34122-2023 §4）

- **跟网型（grid-following，传统 PCS）**：以电网电压为相位参考，输出电流跟踪给定，等效电流源。失网时不能独立供电，须孤岛保护跳闸（详见 [CASE-054 光伏防孤岛](../50-case/CASE-054-review-pv-anti-islanding-reverse-power.md)）。
- **构网型（grid-forming，新型 PCS）**：内部带电压/频率参考（虚拟同步机 VSG），等效电压源，可独立供电或参与系统调频调压，是新型电力系统稳定性关键设备（详见 [CASE-043 光储柴微网](../50-case/CASE-043-composite-pv-storage-diesel-microgrid.md)）。

## 4. 与工程实践的联系

- **支撑条目 1**：[PR-PQ-001 电能质量治理](../30-practice/PR-PQ-001-pq-compensation-design.md) 与 [TH-018 瞬时功率 p-q 理论](TH-018-instantaneous-power-pq-theory.md)——SVG/APF 的硬件基础是三相两电平或三电平 NPC，本条给出拓扑与 PWM 调制的物理源头。
- **支撑条目 2**：[PR-ES-001 储能接入](../30-practice/PR-ES-001-energy-storage-integration.md) 与 [TH-020 电力系统稳定性分类](TH-020-power-system-stability-classification.md)——PCS 是储能与电网接口，构网型 PCS 是新型电力系统稳定性重要支撑（GB/T 34122 新增）。
- **失效边界**：① 线性调制区 $M\le 1$ 上述公式成立，过调制区非线性化且谐波急升，工程避免长期运行；② 高 $f_{sw}$ 下 EMI/EMC 问题突出，须加 LC 滤波器；③ 功率器件开关频率与死区时间限制最低输出频率（>2 Hz）；④ MMC 子模块电容电压均衡须主动控制，故障子模块旁路是运行可靠性关键；⑤ 器件结温限制过载能力，需热计算与降额曲线（详见 [CALC-MS-002 电机温升](../40-calc/CALC-MS-002-motor-temperature-rise.md) §热模型方法）。
- **下游案例**：[CASE-005 谐波降容](../50-case/CASE-005-review-transformer-harmonic-derating.md)、[CASE-028 海上风电升压站](../50-case/CASE-028-composite-offshore-wind-substation.md)、[CASE-043 构网型 PCS 微网](../50-case/CASE-043-composite-pv-storage-diesel-microgrid.md)、[CASE-048 新能源汇集站继保](../50-case/CASE-048-composite-renewable-collector-station-protection.md)、[CASE-053 轨道交通整流](../50-case/CASE-053-composite-rail-transit-traction-rectifier.md)、[CASE-054 光伏防孤岛](../50-case/CASE-054-review-pv-anti-islanding-reverse-power.md)

## 5. 关联条目与变更记录

- 关联：[TH-018 瞬时功率 p-q 理论](TH-018-instantaneous-power-pq-theory.md)（APF 控制算法）、[TH-008 谐波产生机理](TH-008-harmonic-generation.md)（PWM 谐波源）、[TH-020 电力系统稳定性分类](TH-020-power-system-stability-classification.md)（构网型 PCS 与电网稳定）、[TH-002 相量法](TH-002-phasor-analysis.md)（基波分析）、[PR-PQ-001 电能质量治理](../30-practice/PR-PQ-001-pq-compensation-design.md)、[PR-ES-001 储能接入](../30-practice/PR-ES-001-energy-storage-integration.md)、[CASE-043 构网型微网](../50-case/CASE-043-composite-pv-storage-diesel-microgrid.md)
- 下游案例：见 §4 列表。

| 版本 | 日期 | 修改内容 | 修改人 |
|---|---|---|---|
| 0.1 | 2026-09-09 | 创建；含四类变换器分类、SPWM/SVPWM 直流利用率推导、三电平/MMC 拓扑、跟网/构网型对比 | KB 管理员 |
