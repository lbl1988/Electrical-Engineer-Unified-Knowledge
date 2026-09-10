---
id: TH-033
title: 异步电机变频调速控制策略
domain: 基础理论
subdomain: 电机控制
voltage_levels: [LV, MV]
lifecycle: [设计, 运维]
standards:
  - { code: GB/T 12668.1-2023, clause: "4", note: "调速电气传动系统（idt IEC 61800-1），含控制策略分类" }
  - { code: GB 18613-2020, clause: "4", note: "电动机能效限定值及能效等级，变频电机与工频电机差异" }
  - { code: GB/T 21413.1-2018, clause: "4", note: "铁路应用 电力电子变流器，含牵引变频控制" }
  - { code: IEC 60034-2-1:2014, clause: "4", note: "旋转电机损耗与效率试验方法，含变频供电损耗修正" }
status: draft
reviewers: []
version: 0.1
updated: 2026-09-09
---

# 异步电机变频调速控制策略

## 1. 定义

**异步电机变频调速**指通过改变供电频率 $f_1$ 以改变同步转速 $n_s=60f_1/p$（$p$ 为极对数），从而调节转子转速 $n$ 的方法。相比降压调速、变极调速、转子串电阻调速，变频调速是唯一能**同时保持转矩性能与高效**的方案，是当前风机/水泵/压缩机节能改造的主流。

| 控制策略 | 核心思想 | 转矩响应 | 复杂度 | 应用 |
|---|---|---|---|---|
| V/f 控制（标量） | 保持 $U_1/f_1$ 恒定 | 慢（秒级） | 低 | 风机/水泵 |
| 矢量控制（FOC） | dq 解耦磁通与转矩 | 快（ms 级） | 中 | 电梯/起重 |
| 直接转矩控制（DTC） | 滞环控制磁通与转矩 | 极快（μs 级） | 中 | 轧机/牵引 |
| 无速度传感器 FOC | 估算转速替代编码器 | 快 | 高 | 通用变频器 |

## 2. 物理图像

### 2.1 V/f 控制与恒磁通

异步电机稳态等效电路中，气隙磁通 $\Phi\propto E_1/f_1$（$E_1$ 为反电势）。若忽略定子漏抗压降（低速不忽略），则 $\Phi\propto U_1/f_1$。

```
转速指令 ─→ 频率 f₁ ─→ U/f 发生器 ─→ SPWM 调制 ─→ 逆变桥 ─→ 电机

低频补偿：f₁ < 15 Hz 时提升 U₁（补偿 R_s 压降）维持磁通
```

V/f 控制保持磁通恒定 → 转矩近似正比于转差 $\Delta n$，转矩响应随频率变化自然平滑。

### 2.2 矢量控制（FOC）——磁场定向

将三相电流经 Park 变换到与转子磁通同步旋转的 dq 坐标系（详见 [TH-015 Park 方程](TH-015-synchronous-machine-park-equations.md) 同款变换）。在转子磁通定向（$\psi_q=0$）下：

- $i_d$ 控制磁通（类似直流电机励磁绕组）
- $i_q$ 控制转矩（类似直流电机电枢电流）

**转矩与电流解耦**——这是异步电机能获得直流电机级动态性能的物理基础。

```
转速指令 ─→ 速度环 ─→ i_q*（转矩电流参考）
          ─→ 磁通环 ─→ i_d*（励磁电流参考）
                           ↓
              Park 逆变换 ─→ SPWM ─→ 逆变桥 ─→ 电机
                  ↑
              磁通观测器（电压模型/电流模型）
```

## 3. 推导

### 3.1 V/f 控制的转矩-转速特性

异步电机转矩（简化 T 形等效电路，忽略励磁支路）：

$$
T_e=\frac{3p}{\omega_1}\cdot\frac{U_1^2\,R_2'/s}{(R_1+R_2'/s)^2+(X_1+X_2')^2}
$$

保持 $U_1/f_1=const$ 时，$U_1^2\propto f_1^2$、$X_1+X_2'\propto f_1$，$s$ 不变时 $R_2'/s$ 不变，故：

$$
T_e\propto\frac{f_1^2}{\omega_1}\propto\frac{f_1^2}{f_1}=f_1
$$

但实际上 $U_1/f_1$ 恒定时磁通恒定，转矩只取决于转差——**转矩-转速曲线"平移"**，不同频率下机械特性是一族平行的曲线。

| 频率 $f_1$ | 同步转速 $n_s$ | 堵转转矩 $T_{st}$ | 最大转矩 $T_{max}$ |
|---|---|---|---|
| 50 Hz | 1500 r/min | $T_N$ | $2.5\,T_N$ |
| 25 Hz | 750 r/min | $0.9\,T_N$ | $2.4\,T_N$ |
| 10 Hz | 300 r/min | $0.8\,T_N$（低频补偿） | $2.2\,T_N$ |
| 3 Hz | 90 r/min | $0.6\,T_N$（无补偿会骤降） | $1.8\,T_N$ |

低频下 $R_s$ 压降占 $U_1$ 比例上升，磁通减小 → 转矩下降，须 **电压提升补偿**（$U_1=U_{1,rated}\cdot f_1/f_N + \Delta U$）。

### 3.2 矢量控制转矩方程

转子磁通定向（$\psi_r$ 对齐 d 轴）下，转矩：

$$
T_e=\frac{3}{2}p\cdot\frac{L_m}{L_r}\,\psi_r\,i_q
$$

磁通：

$$
\psi_r=\frac{L_m}{1+s\tau_r}\,i_d\quad \tau_r=L_r/R_2'
$$

稳态 $\psi_r\approx L_m i_d$（因 $\tau_r$ 较大），故 $i_d$ 控磁通、$i_q$ 控转矩——**完全解耦**。

### 3.3 节能估算（风机/水泵）

风机/水泵负载转矩 $T\propto n^2$、功率 $P\propto n^3$。工频运行用挡板/阀门调节流量，变频直接调转速：

| 流量需求 | 工频+阀门 $P$ | 变频调速 $P$ | 节能率 |
|---|---|---|---|
| 100% | 100% | 100% | 0% |
| 80% | 90%（阀门节流） | 51% | 43% |
| 60% | 75% | 22% | 71% |
| 40% | 60% | 6% | 90% |

$$
P_{VFD}=\left(\frac{Q}{Q_N}\right)^3 P_N\quad P_{valve}\approx\text{线性}
$$

年运行 6000 h、流量 70% 工况下，变频较工频节能约 50%~60%。

## 4. 与工程实践的联系

- **支撑条目 1**：[TH-024 电力电子变换器与 PWM](TH-024-power-electronic-converters-and-pwm.md) 与 [TH-018 瞬时功率 p-q 理论](TH-018-instantaneous-power-pq-theory.md)——变频器硬件是 VSC+SPWM/SVPWM，矢量控制基于 Park/dq 变换。
- **支撑条目 2**：[TH-007 感应电机启动](TH-007-induction-motor-starting.md) 与 [CASE-017 电机启动压降](../50-case/CASE-017-exam-motor-starting-voltage-drop.md)——变频软启动替代直接/星三角启动，启动电流可限制在额定内。
- **支撑条目 3**：[PR-PQ-001 电能质量治理](../30-practice/PR-PQ-001-pq-compensation-design.md)——变频器是谐波源，须配套输入滤波器或选择低谐波型变频（详见 [TH-008 谐波产生机理](TH-008-harmonic-generation.md)）。
- **失效边界**：① V/f 控制在低速（$<5$ Hz）时磁通补偿不足，转矩波动大，不适合位势负载（起重、电梯）；② 矢量控制依赖转子参数（$R_2', L_r$），温升使 $R_2'$ 变化导致磁通观测偏差，须参数辨识；③ 变频器输出 $du/dt$ 高（IGBT 开关 ns 级），长电缆（>50 m）端电压反射放大可达 2 倍，须加输出电抗器或 dv/dt 滤波器；④ 变频电机轴承电流（共模电压感应）可能损坏轴承，须绝缘轴承或接地碳刷；⑤ 变频器谐波对电机引起附加铜损/铁损，IEC 60034-2-1 规定变频供电效率修正，不可用工频效率直接代入。
- **下游案例**：[CASE-017 电机启动压降](../50-case/CASE-017-exam-motor-starting-voltage-drop.md)、[CASE-035 电机保护整定](../50-case/CASE-035-exam-motor-protection-setting.md)、[CASE-053 轨道交通牵引](../50-case/CASE-053-composite-rail-transit-traction-rectifier.md)

## 5. 关联条目与变更记录

- 关联：[TH-024 电力电子变换器与 PWM](TH-024-power-electronic-converters-and-pwm.md)（VSC 与 SVPWM）、[TH-015 Park 方程](TH-015-synchronous-machine-park-equations.md)（dq 变换）、[TH-018 瞬时功率 p-q 理论](TH-018-instantaneous-power-pq-theory.md)（瞬时电流控制）、[TH-007 感应电机启动](TH-007-induction-motor-starting.md)（软启动与启动电流）、[TH-008 谐波产生机理](TH-008-harmonic-generation.md)（变频器谐波）、[TH-014 磁路饱和](TH-014-magnetic-circuit-saturation.md)（磁通恒定与饱和）、[PR-PQ-001 电能质量治理](../30-practice/PR-PQ-001-pq-compensation-design.md)
- 下游案例：见 §4 列表。

| 版本 | 日期 | 修改内容 | 修改人 |
|---|---|---|---|
| 0.1 | 2026-09-09 | 创建；含 V/f 恒磁通、矢量控制 dq 解耦转矩方程、风机水泵节能估算、$du/dt$ 与轴承电流失效边界 | KB 管理员 |
