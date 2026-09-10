---
id: TH-028
title: 柔性交流输电（FACTS）
domain: 基础理论
subdomain: 柔性输电
voltage_levels: [HV, EHV]
lifecycle: [设计, 运维]
standards:
  - { code: GB/T 36574-2018, clause: "4", note: "静止无功补偿装置（SVC）技术规范" }
  - { code: GB/T 36547-2018, clause: "4", note: "电化学储能系统接入电网技术规定，含构网型 PCS 与 FACTS 协同" }
  - { code: GB/T 38669-2020, clause: "4", note: "静止同步补偿器（STATCOM）技术规范" }
  - { code: IEC 62932-1:2019, clause: "4", note: "柔性交流输电系统（FACTS）通用术语与定义" }
status: draft
reviewers: []
version: 0.1
updated: 2026-09-09
---

# 柔性交流输电（FACTS）

## 1. 定义

**柔性交流输电系统（FACTS, Flexible AC Transmission System）**指基于电力电子技术，通过快速调节交流输电系统参数（阻抗、电压幅值/相角、有功/无功）以提升传输能力、增强稳定性、改善电能质量的装置族。按接入方式分串联型、并联型与串并联复合型三类。

| 类型 | 代表装置 | 接入方式 | 主要功能 |
|---|---|---|---|
| **并联型** | SVC、STATCOM（SVG） | 并联 | 电压支撑、无功补偿、抑制电压波动 |
| **串联型** | TCSC、SSSC | 串联 | 线路阻抗调节、潮流控制、暂态稳定 |
| **复合型** | UPFC、IPFC | 串并联 | 电压+潮流+阻抗综合控制 |

FACTS 相对机械式补偿（断路器投切电容器）的核心优势：① 响应速度从"秒级"提升到"毫秒级"；② 连续可调而非分级；③ 四象限运行（可发可吸、容性感性）。

## 2. 物理图像

### 2.1 SVC（静止无功补偿器）——晶闸管控制并联型

```
        母线 ─┬── TCR（晶闸管控制电抗器）  → 吸收感性无功（连续可调）
              │
              ├── TSC（晶闸管投切电容器）  → 发出容性无功（分级）
              │
              └── FC（固定滤波器）          → 滤谐波 + 固定容性补偿
```

TCR 通过控制触发角 $\alpha$（$90^\circ\sim180^\circ$）改变电抗器等效电纳，连续吸收 $0\sim Q_{TCR}$ 无功；TSC 按需求分级投入电容器。SVC 输出无功随母线电压下降而平方下降（$Q\propto U^2 B$），这是其与 STATCOM 的根本差异。

### 2.2 STATCOM（静止同步补偿器/SVG）——VSC 电压源并联型

```
        母线 ─── 耦合变压器 ─── VSC三相桥 ─── 直流电容
                                  ↑
                          SVPWM 调制，输出电压 U_c
                          U_c > U_s → 发容性无功
                          U_c < U_s → 吸感性无功
```

STATCOM 本质是电压源（VSC），通过调节输出电压幅值与相位控制与电网交换的无功。输出无功近似与电压成正比（$Q\approx(U_c-U_s)U_s/X$），电压跌落时仍能维持额定电流输出——这是 STATCOM 在故障穿越与暂态电压支撑优于 SVC 的物理基础。

### 2.3 UPFC（统一潮流控制器）——复合型

```
        并联 VSC(1) ─ 母线 ─ 串联变压器 ─ 线路 ── 串联 VSC(2)
                          │                    │
                          └── 共用直流电容 ─────┘
```

并联侧调节母线电压（如 STATCOM），串联侧注入幅值相位均可调的串联电压 $\Delta U$，等效调节线路两端电压差与相角——可同时控制有功潮流与无功分布，是 FACTS 家族功能最全的装置。

## 3. 推导

### 3.1 SVC 无功输出与电纳

TCR 基波等效电纳（触发角 $\alpha$）：

$$
B_{TCR}(\alpha)=\frac{1}{\pi X_L}(2\pi-2\alpha+\sin 2\alpha)
$$

| $\alpha$ | $B_{TCR}/B_{max}$ | 无功吸收 |
|---|---|---|
| 90° | 1.0 | 最大（全导通） |
| 120° | 0.54 | 中等 |
| 150° | 0.16 | 小 |
| 180° | 0 | 0（关断） |

SVC 总无功 $Q_{SVC}=U^2(B_{TSC}+B_{FC}-B_{TCR})$，随 $U^2$ 变化——电压跌落时无功输出能力下降。

### 3.2 STATCOM 无功输出

STATCOM 输出电压 $\dot U_c$ 与系统电压 $\dot U_s$ 经耦合电抗 $X$ 连接，交换无功：

$$
Q=\frac{U_s(U_c\cos\delta-U_s)}{X}
$$

$\delta$ 为 $\dot U_c$ 超前 $\dot U_s$ 的相角（很小，仅平衡损耗所需有功）。当 $U_c>U_s$ 发容性、$U_c<U_s$ 吸感性。STATCOM 输出无功受电流限制 $I_{max}$ 约束：

$$
Q_{max}=U_s I_{max}
$$

与 $U_s$ 成正比（线性），而非 SVC 的平方关系。故障下 $U_s$ 跌落至 0.7 p.u. 时，STATCOM 仍可输出 70% 额定容量，而 SVC 仅剩 49%。

### 3.3 提升暂态稳定极限

长线路传输功率 $P=\dfrac{U_1 U_2}{X_{line}}\sin\delta_{12}$，稳态极限 $P_{max}=\dfrac{U_1 U_2}{X_{line}}$。串联补偿（TCSC）降低等效电抗：

$$
P_{max}'=\frac{U_1 U_2}{X_{line}-X_{TCSC}}>\frac{U_1 U_2}{X_{line}}
$$

并联 STATCOM 提升两端电压幅值 $U_1, U_2$ 同样提升 $P_{max}$。二者均使功角特性曲线上移，等面积加速面积减小、减速面积增大，暂态稳定裕度提高——这是 FACTS 抑制低频振荡与提升传输能力的物理基础。

## 4. 与工程实践的联系

- **支撑条目 1**：[PR-PQ-001 电能质量治理](../30-practice/PR-PQ-001-pq-compensation-design.md) 与 [TH-024 电力电子变换器与 PWM](TH-024-power-electronic-converters-and-pwm.md) 与 [TH-018 瞬时功率 p-q 理论](TH-018-instantaneous-power-pq-theory.md)——STATCOM/SVG 是 APF 的大功率版本，共享 VSC 与 SVPWM 硬件基础。
- **支撑条目 2**：[TH-020 电力系统稳定性分类](TH-020-power-system-stability-classification.md) 与 [TH-016 同步电机功角稳定](TH-016-synchronous-machine-power-angle-stability.md)——FACTS 通过功角特性曲线重塑提升暂态稳定，是抑制低频振荡与电压稳定的关键设备。
- **支撑条目 3**：[PR-ES-001 储能接入](../30-practice/PR-ES-001-energy-storage-integration.md)——构网型 PCS 与 STATCOM 共享 VSG 控制原理，储能可兼做 STATCOM 功能。
- **失效边界**：① SVC 在电压严重跌落（$U<0.6$ p.u.）时无功输出能力急剧下降，故障穿越不如 STATCOM；② STATCOM 直流电容须维持稳定，直流母线电压跌落会触发保护闭锁；③ 串联型 FACTS（TCSC）在短路时串联电容器承受过电压，须配合 MOV 限压与旁路间隙；④ UPFC 串联侧注入电压受耦合变压器绝缘水平限制，不适合 EHV/UHV 直接接入；⑤ FACTS 控制器与电网存在次同步谐振（SSR）风险，须抑制控制策略（详见 [TH-020 次同步振荡](TH-020-power-system-stability-classification.md)）。
- **下游案例**：[CASE-005 谐波降容](../50-case/CASE-005-review-transformer-harmonic-derating.md)、[CASE-041 低压无源滤波失谐](../50-case/CASE-041-review-passive-filter-detuning-harmonic-amplification.md)、[CASE-048 新能源汇集站继保](../50-case/CASE-048-composite-renewable-collector-station-protection.md)

## 5. 关联条目与变更记录

- 关联：[TH-024 电力电子变换器与 PWM](TH-024-power-electronic-converters-and-pwm.md)（VSC 与 SVPWM 硬件）、[TH-018 瞬时功率 p-q 理论](TH-018-instantaneous-power-pq-theory.md)（瞬时无功控制算法）、[TH-020 电力系统稳定性分类](TH-020-power-system-stability-classification.md)（暂态稳定与次同步振荡）、[TH-016 功角稳定](TH-016-synchronous-machine-power-angle-stability.md)（功角特性曲线重塑）、[TH-027 HVDC](TH-027-hvdc-transmission-lcc-vsc.md)（VSC 拓扑共享）、[PR-PQ-001 电能质量治理](../30-practice/PR-PQ-001-pq-compensation-design.md)
- 下游案例：见 §4 列表。

| 版本 | 日期 | 修改内容 | 修改人 |
|---|---|---|---|
| 0.1 | 2026-09-09 | 创建；含 SVC/STATCOM/UPFC 三类、TCR 电纳推导、STATCOM 线性无功输出、暂态稳定重塑失效边界 | KB 管理员 |
