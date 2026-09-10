---
id: TH-036
title: 发电机励磁系统建模与 AVR/PSS
domain: 基础理论
subdomain: 励磁控制
voltage_levels: [MV, HV, EHV]
lifecycle: [设计, 运维]
standards:
  - { code: GB/T 40595-2021, clause: "4", note: "电力系统网源协调技术规范，含励磁系统参数与 PSS 投退要求" }
  - { code: DL/T 843-2010, clause: "4", note: "大型发电机励磁系统技术条件，含 AVR/PSS 传递函数与整定" }
  - { code: DL/T 1166-2012, clause: "4", note: "同步发电机进相运行试验导则，含励磁限制器" }
  - { code: IEC 60034-16-1:2011, clause: "4", note: "同步电机励磁系统功能特性（idt GB/T 13502）" }
status: draft
reviewers: []
version: 0.1
updated: 2026-09-09
---

# 发电机励磁系统建模与 AVR/PSS

## 1. 定义

**励磁系统（Excitation System）**指向同步发电机转子绕组提供直流励磁电流、并按运行工况自动调节以维持机端电压与无功稳定的装置族。核心由**自动电压调节器（AVR）**与**电力系统稳定器（PSS）**两部分组成。

| 励磁类型 | 励磁电源 | 响应速度 | 典型应用 |
|---|---|---|---|
| 同轴直流励磁机 | 直流发电机 | 慢（0.5~1 s） | 老式中小型机组 |
| 同轴交流励磁机+不可控整流 | 交流发电机+二极管 | 中（0.2~0.5 s） | 200 MW 以下 |
| 同轴交流励磁机+可控整流 | 交流发电机+晶闸管 | 快（0.1~0.2 s） | 300~600 MW |
| 自并励静止励磁 | 机端变压器+晶闸管 | 极快（<0.1 s） | 600 MW 以上主流 |

| 控制器 | 功能 | 作用频带 | 物理目的 |
|---|---|---|---|
| AVR | 端电压闭环调节 | 0.1~5 Hz | 维持 $U_t$ 恒定、无功分配 |
| PSS | 抑制低频振荡 | 0.1~3 Hz | 提供正阻尼力矩，抑制功角振荡 |

## 2. 物理图像

### 2.1 AVR 闭环

AVR 采集机端电压 $U_t$ 与参考 $U_{ref}$ 比较，经 PID 校正输出晶闸管触发角 $\alpha$，控制励磁电压 $E_f$：

```
U_ref ──→(+)──→ PID ──→ α ──→ 晶闸管整流 ──→ E_f ──→ 转子 ──→ E_0 ──→ U_t
          ↑(-)                                                              │
          └──────────────────── U_t 反馈 ←─────────────────────────────────┘
```

AVR 闭环是典型负反馈系统：$U_t$ 升高 → $E_f$ 下降 → $E_0$ 下降 → $U_t$ 回落。但 AVR 本身**提供负阻尼力矩**——故障后功角摇摆期间 $U_t$ 变化使 AVR 反复调节 $E_f$，相位落后于 $\Delta\omega$，等效负阻尼——这是 AVR 可能加剧低频振荡的物理原因，也是 PSS 存在的理由。

### 2.2 PSS 正阻尼力矩

PSS 以 $\Delta\omega$（或 $\Delta P$）为输入，经超前-滞后补偿与清洗环节输出附加信号 $V_s$ 叠加到 AVR 参考电压上，使励磁产生的电磁转矩 $\Delta T_e$ 超前 $\Delta\omega$ 约 $90^\circ$（即与 $\Delta\omega$ 同相）——**正阻尼力矩**。

```
Δω ──→ 清洗环节 ─→ 超前-滞后补偿 ──→ Vs ──→ 叠加到 AVR 输入
                      (相位补偿)
```

## 3. 推导

### 3.1 励磁系统数学模型（IEEE Type ST5A 简化）

自并励静止励磁简化传递函数：

$$
\frac{E_f(s)}{V_{AVR}(s)}=\frac{K_A}{1+sT_A}\cdot\frac{1}{1+sT_{do}'}\quad
```

忽略饱和与限幅，AVR 一阶惯性 $T_A\approx0.01\sim0.05$ s，转子回路时间常数 $T_{do}'\approx5\sim8$ s。

### 3.2 PSS 传递函数

典型 PSS（IEEE PSS1A）：

$$
V_s(s)=K_{PSS}\cdot\underbrace{\frac{sT_w}{1+sT_w}}_{\text{清洗}}\cdot\underbrace{\frac{1+sT_1}{1+sT_2}\cdot\frac{1+sT_3}{1+sT_4}}_{\text{超前-滞后}}\cdot\Delta\omega(s)
$$

| 参数 | 典型值 | 作用 |
|---|---|---|
| $K_{PSS}$ | 5~20 p.u. | 增益 |
| $T_w$ | 5~15 s | 清洗（隔直流） |
| $T_1/T_2$ | 0.1~0.5 / 0.01~0.1 | 第一级超前补偿 |
| $T_3/T_4$ | 0.1~0.5 / 0.01~0.1 | 第二级超前补偿 |

相位补偿目标：使 $\angle G_{PSS}(j\omega)+\angle G_{ex}(j\omega)+\angle G_{G}(j\omega)\approx0^\circ$（与 $\Delta\omega$ 同相），$\omega$ 为低频振荡频率（0.1~3 Hz）。

### 3.3 Heffron-Phillips 模型阻尼力矩分析

发电机小信号模型（Heffron-Phillips）中电磁转矩：

$$
\Delta T_e = K_1\Delta\delta + K_2\Delta E_q'
$$

加入 AVR 后 $K_5<0$（弱联络线工况），AVR 产生的 $\Delta T_e$ 中含与 $\Delta\omega$ 反相的负阻尼分量 $D_{AVR}<0$。PSS 补偿后总阻尼：

$$
D_{total}=D_{mech}+D_{AVR}+D_{PSS}
$$

PSS 参数整定目标：$D_{PSS}>|D_{AVR}|$，使 $D_{total}>0$ 且留有裕度（典型 $D_{total}\ge 3$ p.u.）。

## 4. 与工程实践的联系

- **支撑条目 1**：[TH-016 功角稳定](TH-016-synchronous-machine-power-angle-stability.md) 与 [TH-020 电力系统稳定性分类](TH-020-power-system-stability-classification.md)——PSS 是抑制低频振荡（功角稳定）的关键控制器，本条给出 AVR 负阻尼与 PSS 正阻尼的定量关系。
- **支撑条目 2**：[PR-PE-001 继电保护配置](../30-practice/PR-PE-001-relay-protection-config.md) 与 [TH-012 保护四性](TH-012-protection-four-properties.md)——失步保护与 PSS 动作时序协调，失磁保护与 AVR 低励限制器配合。
- **支撑条目 3**：[TH-032 同步电机进相与调相运行](TH-032-synchronous-machine-leading-and-condensing-operation.md)——进相运行时 AVR 的欠励限制器动作是静态稳定裕度约束的工程实现。
- **失效边界**：① PSS 参数整定针对特定低频振荡频率，全工况（不同负荷、不同联络线）须多模式校验，避免某模式阻尼提升而另一模式变差；② PSS 增益过大会引入控制环振荡（$K_{PSS}$ 上限由励磁系统稳定裕度决定）；③ 自并励在机端三相短路时励磁电压骤降，强励能力不如他励，须按 GB/T 40595 校核强励倍数与持续时间；④ PSS 在次同步频段可能激发 SSR（详见 [TH-035](TH-035-sub-synchronous-resonance-ssr-ssci.md)），须加窄带阻滤波器；⑤ 数字式 AVR 的采样率与算法延迟（ms 级）在次同步频段可能引入相位滞后，须评估。
- **下游案例**：[CASE-020 油浸变压器短路起火](../50-case/CASE-020-accident-oil-transformer-fire.md)、[CASE-048 新能源汇集站继保](../50-case/CASE-048-composite-renewable-collector-station-protection.md)

## 5. 关联条目与变更记录

- 关联：[TH-016 功角稳定](TH-016-synchronous-machine-power-angle-stability.md)（低频振荡与阻尼力矩）、[TH-015 Park 方程](TH-015-synchronous-machine-park-equations.md)（$E_q', T_{do}'$ 物理来源）、[TH-020 电力系统稳定性分类](TH-020-power-system-stability-classification.md)（静态/动态稳定协调）、[TH-035 SSR](TH-035-sub-synchronous-resonance-ssr-ssci.md)（PSS 激发 SSR 风险）、[TH-032 进相调相](TH-032-synchronous-machine-leading-and-condensing-operation.md)（AVR 限制器）、[PR-PE-001 继电保护配置](../30-practice/PR-PE-001-relay-protection-config.md)
- 下游案例：见 §4 列表。

| 版本 | 日期 | 修改内容 | 修改人 |
|---|---|---|---|
| 0.1 | 2026-09-09 | 创建；含 AVR 负反馈闭环与负阻尼机理、PSS 超前-滞后补偿、Heffron-Phillips 阻尼分析、多模式整定与 SSR 激发失效边界 | KB 管理员 |
