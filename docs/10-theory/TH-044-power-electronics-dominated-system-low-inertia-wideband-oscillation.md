---
id: TH-044
title: 电力电子化电力系统低惯量与宽频振荡机理（PLL 耦合/次同步/超同步/控制引发振荡）
domain: 基础理论
subdomain: 电力系统
voltage_levels: [HV, EHV, UHV]
lifecycle: [规划, 设计, 运维]
standards:
  - { code: GB 38755-2019, clause: "全文", note: "电力系统安全稳定导则（强制性）：含新能源并网稳定要求" }
  - { code: GB/T 19963.1-2021, clause: "全文", note: "电力系统网源协调技术规范 第1部分：技术要求（含宽频振荡抑制）" }
  - { code: GB/T 40595-2021, clause: "全文", note: "并网电源一次调频试验技术规定（含电力电子电源惯量支撑）" }
  - { code: GB/T 19964-2024, clause: "全文", note: "光伏发电站接入电力系统技术规定（含宽频阻抗要求）" }
  - { code: IEC 61400-27-1:2020, clause: "全文", note: "Wind turbines - Electrical simulation models（含宽频阻抗模型）" }
status: draft
reviewers: []
version: 0.1
updated: 2026-09-09
---

# 电力电子化电力系统低惯量与宽频振荡机理（PLL 耦合/次同步/超同步/控制引发振荡）

## 1. 定义

本条研究**高比例电力电子设备接入**后电力系统稳定形态的转变——从"功角主导+低频振荡"转向"电压主导+宽频振荡（次同步~数十 kHz）"。

| 现象 | 定义 | 频率范围 |
|---|---|---|
| **低惯量** | 同步发电机被电力电子设备替代，系统等效惯量下降 | 稳态指标 |
| **次同步振荡（SSO）** | 电力电子控制与轴系/电网耦合振荡 | 10~50 Hz（次同步） |
| **超同步振荡** | 控制耦合至高于工频的振荡 | 50~数百 Hz |
| **控制引发振荡（CIO）** | 多换流站 PLL/电流环互相耦合 | 数十 Hz~kHz |
| **谐波谐振** | 电力电子器件开关频率与电网阻抗谐振 | 数百 Hz~kHz |

## 2. 物理图像

电力电子化电力系统振荡的多频段物理图像：

```
0.1~2 Hz       │ 功角/频率振荡（同步机间）       │ 转子机械量
2~10 Hz         │ 区间振荡（同步机区域间）         │ 转子机械量
10~50 Hz        │ 次同步振荡 SSO                  │ 电力电子控制↔轴系
50~数百 Hz       │ 超同步振荡/控制引发振荡 CIO    │ 多换流站 PLL 耦合
数百 Hz~kHz      │ 谐波谐振/开关谐振              │ 器件↔电网阻抗
```

**机理转变**：传统同步机间振荡以转子机械惯量为媒介，时间常数秒级；电力电子化后，振荡通过 PLL/电流环耦合，时间常数毫秒级，振荡频率上移至数十 Hz~kHz。

## 3. 推导

### 3.1 低惯量机理

系统等效惯量（见 TH-038）：

$$H_\Sigma = \frac{\sum_i H_i S_i}{\sum_i S_i}$$

电力电子电源惯量为零（跟网型）或虚拟惯量 $J_{eq}$（构网型，见 TH-038）。

| 新能源占比 | 跟网型占比 | 等效 $H_\Sigma$ | 振荡风险 |
|---|---|---|---|
| 0% | 0% | 8 s | 低频（0.1~2 Hz）主导 |
| 50% | 50% | 4 s | 中频（2~10 Hz）增强 |
| 80% | 80% | 1.6 s | 宽频（10~数百 Hz）风险显著 |
| 100%（跟网型） | 100% | ≈0 | 高频（kHz）+ 电压失稳风险 |

### 3.2 PLL 耦合振荡机理

跟网型换流器锁相环（PLL）传递函数：

$$\theta_{PLL}(s) = \underbrace{\left(K_p + \frac{K_i}{s}\right)}_{PI}\cdot \frac{1}{s}\cdot U_q(s)$$

PLL 输出相位 $\theta_{PLL}$ 反馈至电流环，形成耦合闭环。两换流站间 PLL 耦合传递函数：

$$G_{couple}(s) = \frac{G_{PLL,1}(s)\cdot G_{line}(s)\cdot G_{PLL,2}(s)}{1-G_{PLL,1}(s)\cdot G_{line}(s)\cdot G_{PLL,2}(s)}$$

特征方程：$1-G_{PLL,1}\cdot G_{line}\cdot G_{PLL,2} = 0$

| PLL 参数 | 阻尼比 $\zeta$ | 振荡频率 $\omega_n$ | 失稳判据 |
|---|---|---|---|
| $K_p=0.5$, $K_i=20$ | 0.7 | 4 Hz | 稳定 |
| $K_p=2$, $K_i=100$ | 0.3 | 10 Hz | 边界 |
| $K_p=5$, $K_i=500$ | 0.1 | 25 Hz | **失稳** |

### 3.3 阻抗分析法

换流器在 $dq$ 坐标下的输入阻抗矩阵：

$$Z_{dq}(j\omega) = \begin{bmatrix} Z_{dd} & Z_{dq} \\ Z_{qd} & Z_{qq}\end{bmatrix}$$

广义奈奎斯特判据（GNC）：

$$\rho\big(Z_{source}(j\omega)\cdot Z_{conv}^{-1}(j\omega)\big) < -1$$

其中 $\rho$ 为返回比矩阵特征值。

| 振荡类型 | 源-荷阻抗交点 | 振荡频率 | 负阻尼来源 |
|---|---|---|---|
| 次同步（SSO） | $|Z_s|=|Z_c|$ 在 $f<50$ Hz | 10~50 Hz | 恒功率控制负电阻 |
| 超同步 | $|Z_s|=|Z_c|$ 在 $f>50$ Hz | 50~200 Hz | 电流环带宽不足 |
| 谐波谐振 | 电网谐振点 | 数百 Hz~kHz | LCL 滤波器 + 电网 |

### 3.4 控制引发振荡（CIO）案例

多风电场汇集于同一 PCC，PLL 互相耦合，形成 CIO。振荡频率：

$$f_{CIO} \approx \frac{1}{2\pi}\sqrt{\frac{K_{PLL,1}\cdot K_{PLL,2}}{L_{line}\cdot C_{DC}}}$$

| 场景 | 振荡频率 | 幅值 | 失稳机理 |
|---|---|---|---|
| 单风电场并网 | — | — | 稳定 |
| 两风电场近距离汇集 | 22 Hz | ±15% | PLL 互相耦合 |
| 三风电场集中汇集 | 18 Hz | ±25% | 三方 PLL 耦合 |

## 4. 与工程实践的联系

### 4.1 支撑条目

- [PR-ES-001 储能接入](../30-practice/PR-ES-001-energy-storage-integration.md)：构网型 PCS 与跟网型 PCS 选择，宽频阻抗建模要求。
- [PR-PE-001 继电保护配置](../30-practice/PR-PE-001-relay-protection-config.md)：电力电子化后短路电流特征变化与保护适配。
- [PR-PQ-001 无功补偿与谐波治理](../30-practice/PR-PQ-001-pq-compensation-design.md)：宽频阻抗谐振点识别与有源阻尼。
- [PR-DD-002 变电所布置与设备选型](../30-practice/PR-DD-002-substation-layout-and-equipment-selection.md)：汇集站滤波器配置与宽频谐振校核。

### 4.2 失效边界

| 失效场景 | 原因 | 对策 |
|---|---|---|
| **PLL 参数失稳** | $K_p$/$K_i$ 过大引入负阻尼 | 自适应 PLL + 阻尼重塑控制 |
| **多换流站 CIO** | 集中汇集 + 控制器雷同 | 错频运行（PLL 参数分散）+ 主动阻尼 |
| **谐波谐振放大** | LCL 谐振点与电网阻抗交点重合 | 主动阻尼 + 有源陷波器 |
| **跟网型失稳** | 弱电网 SCR<1.5 | 切换为构网型 + 同步调相机支撑 |
| **次同步控制相互作用（SSCI）** | 风机控制与串补线路耦合 | 调整控制带宽 + 附加阻尼（见 TH-035） |
| **惯量完全缺失**（100% 跟网型） | RoCoF 超保护阈值 | 构网型+储能虚拟惯量 + 同步调相机 |

## 5. 关联条目与变更记录

- 关联：[TH-024 电力电子变换器与 PWM](TH-024-power-electronic-converters-and-pwm.md)（VSC 拓扑与控制基础）、[TH-027 HVDC LCC/VSC](TH-027-hvdc-transmission-lcc-vsc.md)（VSC 控制与弱电网失效）、[TH-035 SSR/SSCI](TH-035-sub-synchronous-resonance-ssr-ssci.md)（次同步振荡分类）、[TH-038 新能源惯量支撑](TH-038-high-renewable-frequency-stability-inertia.md)（VSG 虚拟惯量）、[TH-040 交直流混联](TH-040-hybrid-ac-dc-grid-stability.md)（LCC/VSC 多换流站耦合）、[TH-043 AI 基础](TH-043-ai-foundations-in-electrical-engineering.md)（AI 辅助振荡模式识别）

| 版本 | 日期 | 修改内容 | 修改人 |
|---|---|---|---|
| 0.1 | 2026-09-09 | 创建；含低惯量/PLL 耦合/阻抗分析/CIO 四类机理 | KB 管理员 |
