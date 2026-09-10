---
id: TH-051
title: 电力电子化设备宽频阻抗建模（PCS 阻抗/有源阻尼/PLL 耦合/阻抗稳定判据）
domain: 基础理论
subdomain: 电力系统稳定
voltage_levels: [HV, EHV, UHV]
lifecycle: [设计, 运维]
standards:
  - { code: GB/T 19963.1-2021, clause: "§4 宽频阻抗", note: "电力系统网源协调技术规范 第1部分：并网电源宽频阻抗建模与试验" }
  - { code: GB 38755-2019, clause: "§6 新能源稳定", note: "电力系统安全稳定导则：含电力电子设备引发的振荡" }
  - { code: GB/T 40595-2021, clause: "§5 宽频特性", note: "并网电源一次调频试验技术规定" }
  - { code: CIGRE TB 868, clause: "全文", note: "Harmonics and Wideband Stability in Converter-Based Power Systems（宽频稳定研究）" }
status: draft
reviewers: []
version: 0.1
updated: 2026-09-10
---

# 电力电子化设备宽频阻抗建模

## 1. 定义

电力电子化设备（光伏/风电变流器、储能 PCS、SVG、HVDC 换流站等）的**宽频阻抗建模**是分析**次同步/超同步/谐波振荡**的基础。不同于传统同步机的低频阻抗模型（仅描述 0~10 Hz 特性），电力电子设备的阻抗模型需要覆盖**10 Hz ~ 10 kHz 甚至更高**的宽频带，以正确捕捉 PLL 耦合、电流环带宽、开关谐波等快速动态。

两种核心建模方法：

| 方法 | 输出 | 带宽 | 用途 |
|---|---|---|---|
| **dq 阻抗模型** | $Z_{dd}, Z_{dq}, Z_{qd}, Z_{qq}$（耦合阻抗矩阵） | 0 ~ 控制带宽（kHz 级） | 小信号稳定分析、PLL 耦合研究 |
| **序阻抗模型** | $Z_p, Z_n, Z_0$（正/负/零序） | 0 ~ 开关频率（数十 kHz） | 宽频振荡、谐波谐振、阻抗稳定判据 |

**阻抗稳定判据**（Nyquist 判据的工程等价）：

$$\frac{Z_{\mathrm{grid}}(s)}{Z_{\mathrm{conv}}(s)} \text{ 的 Nyquist 曲线不应包围 } -1 + j0 \text{ 点}$$

等价于：在谐振频率 $f_{\mathrm{res}}$ 处，阻抗幅值比 < 10 dB 且相位差 < 180°。

## 2. 物理图像

电力电子设备宽频阻抗的频率特性：

```
频率         │ 阻抗主导成分          │ 与电网的相互作用
────────────┼──────────────────────┼───────────────────
< 50 Hz      │ 输出滤波器 L + C     │ 工频运行点
50~200 Hz    │ PLL 与同步环耦合     │ 次同步振荡（SSO/SSCI）
200~1 kHz    │ 电流环带宽           │ 超同步振荡（CIO）
1~10 kHz     │ 有源阻尼/虚拟阻抗     │ 宽频阻抗谐振风险
> 10 kHz     │ 开关谐波边带         │ 高频谐波谐振
```

**关键物理量**：

| 量 | 典型值 | 工程意义 |
|---|---|---|
| PLL 带宽 $f_{\mathrm{PLL}}$ | 10~100 Hz | 决定 PLL 与电网耦合的频段 |
| 电流环带宽 $f_{\mathrm{CC}}$ | 200~2000 Hz | 决定电力电子"刚性" |
| 开关频率 $f_{\mathrm{sw}}$ | 2~20 kHz | 谐波源头 |
| 输出滤波器截止频率 | $f_{\mathrm{sw}} / 10 \sim f_{\mathrm{sw}} / 5$ | 谐波抑制能力 |

## 3. 推导

### 3.1 dq 阻抗模型（跟网型 PCS）

跟网型 PCS 的小信号 dq 阻抗矩阵：

$$\begin{pmatrix} \Delta u_d \\ \Delta u_q \end{pmatrix} = \begin{pmatrix} Z_{dd} & Z_{dq} \\ Z_{qd} & Z_{qq} \end{pmatrix} \begin{pmatrix} \Delta i_d \\ \Delta i_q \end{pmatrix}$$

其中非对角项 $Z_{dq}, Z_{qd}$ 反映 dq 轴耦合，**是 PLL 耦合振荡的根源**。

在 PLL 同步旋转坐标系中，PLL 的相位误差 $\Delta\theta$ 会通过 Park 变换引入耦合项：

$$Z_{dq}(s) \approx -\frac{U_q(s) \cdot G_{\mathrm{PLL}}(s)}{1 + G_{\mathrm{PLL}}(s) \cdot G_{\mathrm{LPF}}(s)} \cdot \frac{1}{s C}$$

**结论**：PLL 带宽越高，dq 耦合越强，次同步振荡风险越大。

### 3.2 序阻抗模型

正序阻抗 $Z_p(f)$ 的简化表达式（LCL 滤波器 + PWM + PLL 耦合）：

$$Z_p(j\omega) = j\omega L_1 + \frac{1}{j\omega C_f + Y_{\mathrm{PWM}}(j\omega)} + Z_{\mathrm{PLL}}(j\omega)$$

其中：
- $L_1$ = 逆变器侧电感
- $C_f$ = 滤波电容
- $Y_{\mathrm{PWM}}$ = PWM 等效导纳（非线性，可用采样平均近似）
- $Z_{\mathrm{PLL}}(j\omega)$ = PLL 引入的附加阻抗

### 3.3 阻抗稳定判据（广义 Nyquist）

**MIMO Nyquist 判据**：多换流站系统，定义回比矩阵：

$$\mathbf{L}(s) = \mathbf{Z}_{\mathrm{grid}}(s) \cdot \mathbf{Y}_{\mathrm{conv}}(s) = \mathbf{Z}_{\mathrm{grid}}(s) \cdot \mathbf{Z}_{\mathrm{conv}}(s)^{-1}$$

系统稳定当且仅当 $\mathbf{L}(s)$ 的**所有特征值**在 $s = j\omega$ 上都**不穿过 -1**。

**工程简化**：对单换流站系统，检查 $Z_{\mathrm{grid}}(j\omega)/Z_{\mathrm{conv}}(j\omega)$ 的幅相特性：
- 幅值 |比值| < 0.707（即 < -3 dB）
- 相位差 $\phi_{\mathrm{grid}} - \phi_{\mathrm{conv}} \neq \pm 180°$

### 3.4 有源阻尼设计

宽频阻抗不稳定时常用的抑制手段——**虚拟阻抗法**：

在 PCS 控制环中附加反馈项 $Z_{\mathrm{virt}} = \mathrm{diag}(R_v, j\omega L_v)$，使等效阻抗：

$$Z_{\mathrm{eq}} = Z_{\mathrm{conv}} + Z_{\mathrm{virt}}$$

**关键参数**：

| 参数 | 作用 | 取值原则 |
|---|---|---|
| 虚拟电阻 $R_v$ | 增加阻尼，降低振荡尖峰 | $5 \sim 20$ % $Z_{\mathrm{base}}$ |
| 虚拟电感 $L_v$ | 调整相位特性，避免与电网谐振 | 使 $Z_{\mathrm{eq}}$ 与 $Z_{\mathrm{grid}}$ 相位差 < 120° |

## 4. 与工程实践的联系

### 4.1 应用场景

| 应用 | 依赖条目 | 标准依据 |
|---|---|---|
| 大型风电/光伏集群并网稳定分析 | TH-028（STATCOM）、TH-040（交直流混联）、TH-041（DG 承载力） | GB/T 19963.1-2021 |
| 储能 PCS 宽频特性试验 | TH-046（电池热失控/储能脱网）、PR-ES-001（储能接入） | GB/T 51048-2025 |
| HVDC 换相失败后的阻抗特性 | TH-027（LCC/VSC-HVDC） | GB/T 38755-2019 |
| 多换流站协同抑制振荡 | TH-028（FACTS）、PR-PQ-001（无功补偿） | CIGRE TB 868 |

### 4.2 失效边界

| 边界条件 | 后果 | 工程速记 |
|---|---|---|
| PLL 带宽过高（> 100 Hz）且电网阻抗较大 | 次同步振荡（SSI） | PLL 带宽设计满足 $f_{\mathrm{PLL}} < 5\sqrt{f_{\mathrm{grid}}/H_{\mathrm{eq}}}$ |
| 多换流站 PLL 同频同步 | 集体振荡风险放大 | 各场站 PLL 带宽错开 ±30% |
| 有源阻尼参数设计不当（过强） | 引入新的振荡模态 | 参数扫描 + Nyquist 校验 |

### 4.3 工程速记

> **阻抗稳定口诀**：幅值比 < 0.7，相位差 < 120°。PLL 带宽错开 ±30%，虚拟电阻 5~20% $Z_{\mathrm{base}}$。

## 5. 关联与变更

| 关联 | 说明 |
|---|---|
| [TH-024](TH-024-power-electronic-converters-and-pwm.md) | PWM 调制原理是阻抗模型的源头 |
| [TH-027](TH-027-hvdc-transmission-lcc-vsc.md) | HVDC 换流站是大规模 PCS 阻抗耦合场景 |
| [TH-028](TH-028-facts-flexible-ac-transmission.md) | STATCOM/SVC 作为可控阻抗改变系统特性 |
| [TH-040](TH-040-hybrid-ac-dc-grid-stability.md) | 交直流混联系统阻抗耦合更复杂 |
| [TH-044](TH-044-power-electronics-dominated-system-low-inertia-wideband-oscillation.md) | 宽频振荡的机理延伸 |
| [PR-PQ-001](../30-practice/PR-PQ-001-pq-compensation-design.md) | SVG 阻抗设计直接影响谐波和无功补偿效果 |

**变更记录**：
- 2026-09-10：首版草稿
