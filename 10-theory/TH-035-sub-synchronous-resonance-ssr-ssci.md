---
id: TH-035
title: 电力系统次同步谐振（SSR/SSCI）机理
domain: 基础理论
subdomain: 系统稳定
voltage_levels: [HV, EHV]
lifecycle: [设计, 运维]
standards:
  - { code: GB/T 40595-2021, clause: "4", note: "电力系统网源协调技术规范，含次同步振荡监测与抑制" }
  - { code: DL/T 1234-2013, clause: "4", note: "电力系统安全稳定计算规范，含次同步振荡仿真范围" }
  - { code: DL/T 553-2017, clause: "4", note: "电力系统次同步振荡监测与抑制装置技术规范" }
  - { code: IEEE PES Subsynchronous Resonance Task Force 2020, clause: "", note: "SSR/SSCI 定义与分类国际共识报告" }
status: draft
reviewers: []
version: 0.1
updated: 2026-09-09
---

# 电力系统次同步谐振（SSR/SSCI）机理

## 1. 定义

**次同步谐振（Subsynchronous Resonance, SSR）**指串联补偿输电系统的电气谐振频率 $f_{er}$ 与汽轮发电机轴系机械扭振频率 $f_n$ 互补（$f_{er}+f_n\approx f_0$），在特定工况下两者耦合产生能量交换，导致发电机轴系扭振增幅损坏的物理现象。**次同步控制相互作用（Subsynchronous Control Interaction, SSCI）**指风电/光伏逆变器控制带宽与串联补偿电网电气谐振耦合引发的振荡，无轴系参与，属电气振荡。

| 类型 | 耦合对象 | 频率范围 | 典型触发 | 后果 |
|---|---|---|---|---|
| SSR（扭振） | 发电机轴系 ↔ 电气谐振 | 10~45 Hz | 串联补偿 + 故障扰动 | 轴系疲劳损坏 |
| SSCI（电气） | 逆变器控制 ↔ 电气谐振 | 20~50 Hz | 风电经串补送出 | 电压电流振荡 |
| SSTI（扭振互作用） | 轴系 ↔ HVDC/FACTS 控制 | 10~45 Hz | HVDC 控制不当 | 轴系疲劳 |
| 暂态力矩放大 | 轴系 ↔ 串补暂态 | 10~45 Hz | 故障清除时刻 | 一次大扭矩冲击 |

## 2. 物理图像

### 2.1 SSR 的互补频率机理

发电机转子以同步角速度 $\omega_0$ 旋转。串联补偿线路的电气谐振频率：

$$
f_{er} = f_0\sqrt{\frac{X_C}{X_L}}
$$

电气谐振产生的负序电流分量（频率 $f_0-f_{er}$）在发电机转子上感应出频率 $f_{er}$ 的磁通，与转子相对运动产生频率 $f_0-f_{er}$ 的电磁转矩。若 $f_0-f_{er}$ 恰好等于发电机轴系某个扭振固有频率 $f_n$，则能量持续注入轴系——**互补条件** $f_{er}+f_n=f_0$。

```
串补线路 ── 电气谐振 fer ──→ 定子电流 f0-fer ──→ 转子感应转矩 fn'=f0-fer
                                                            ↓
发电机轴系 ── 扭振固有 fn ───← 若 fn'=fn 则能量正反馈 → 扭振增幅
```

### 2.2 SSCI 的控制-电气耦合

风电变流器（特别是双馈感应发电机 DFIG 或直驱永磁 PMSG）的电流内环控制带宽约 10~50 Hz。当风电场经串联补偿线路送出时，串补电气谐振频率落在控制带宽内，变流器控制响应与谐振电流形成正反馈——这是 SSCI 的物理本质（无机械轴系参与，纯电气耦合）。

## 3. 推导

### 3.1 串联补偿电气谐振频率

L-C 串联电路谐振频率：

$$
f_{er} = \frac{1}{2\pi\sqrt{LC}} = f_0\sqrt{\frac{X_C}{X_L}}
$$

| 串补度 $k=X_C/X_L$ | $f_{er}$ (Hz) | 互补频率 $f_0-f_{er}$ (Hz) |
|---|---|---|
| 0.10 | 15.8 | 34.2 |
| 0.30 | 27.4 | 22.6 |
| 0.50 | 35.4 | 14.6 |
| 0.70 | 41.8 | 8.2 |

汽轮发电机组轴系扭振固有频率典型在 13~30 Hz（多段轴系模态），故串补度 20%~50% 范围内互补风险最大。

### 3.2 SSR 稳定性判据（阻尼判据）

发电机组等效阻尼系数 $D_n$ 由机械阻尼 $D_{mech}$ 与电气阻尼 $D_{elec}$ 组成：

$$
D_n = D_{mech}+D_{elec}(f_{er})
$$

SSR 稳定条件：

$$
D_n > 0\quad\text{即}\quad D_{elec}(f_{er}) > -D_{mech}
$$

电气阻尼 $D_{elec}$ 在谐振频率附近变为负值（串补线路能量注入），若负阻尼绝对值超过机械正阻尼，扭振增幅。

### 3.3 SSCI 阻尼判据

SSCI 的等效阻尼由变流器控制传递函数 $G_{ctrl}(s)$ 与电网阻抗 $Z_{grid}(s)$ 共同决定：

$$
D_{SSCI} = \text{Re}\left[\frac{1}{Z_{grid}(j\omega)+G_{ctrl}(j\omega)}\right]
$$

$D_{SSCI}<0$ 时振荡增幅。抑制方法：调整控制带宽使其避开谐振点，或加装**次同步阻尼控制器（SSDC）**。

## 4. 与工程实践的联系

- **支撑条目 1**：[TH-020 电力系统稳定性分类](TH-020-power-system-stability-classification.md)——SSR/SSCI 属于次同步振荡子类，是稳定性理论的重要分支。
- **支撑条目 2**：[TH-028 柔性交流输电 FACTS](TH-028-facts-flexible-ac-transmission.md) 与 [TH-027 HVDC](TH-027-hvdc-transmission-lcc-vsc.md)——FACTS/HVDC 控制不当可能激发 SSTI，但 SSDC 也可兼做抑制装置。
- **支撑条目 3**：[PR-PE-001 继电保护配置](../30-practice/PR-PE-001-relay-protection-config.md)——次同步振荡监测装置（SSR-DS）配置与切机保护整定。
- **失效边界**：① 互补频率条件 $f_{er}+f_n\approx f_0$ 是必要非充分条件，还须负阻尼超过正阻尼；② SSCI 风险随串补度增加而上升，但不同风电机型（DFIF/PMSG）控制带宽差异大，须具体分析；③ SSR 暂态力矩放大在故障清除瞬间产生一次性大冲击，即使稳态不满足互补条件也可能损坏轴系；④ SSDC 参数设计须在多工况下验证，避免在某些串补度下反而激发新振荡；⑤ 可控串联补偿（TCSC，详见 [TH-028](TH-028-facts-flexible-ac-transmission.md)）通过调节 $X_C$ 破坏互补条件，是 SSR 抑制的重要手段。
- **下游案例**：暂无专门案例，可在后续事故类条目中补全（如 2015 新疆哈密 SSCI 事件）

## 5. 关联条目与变更记录

- 关联：[TH-020 电力系统稳定性分类](TH-020-power-system-stability-classification.md)（次同步振荡子类）、[TH-016 功角稳定](TH-016-synchronous-machine-power-angle-stability.md)（发电机轴系与电气耦合）、[TH-028 FACTS](TH-028-facts-flexible-ac-transmission.md)（TCSC 抑制 SSR 与 SSDC）、[TH-027 HVDC](TH-027-hvdc-transmission-lcc-vsc.md)（SSTI 风险）、[TH-024 电力电子变换器](TH-024-power-electronic-converters-and-pwm.md)（逆变器控制带宽与 SSCI）、[PR-PE-001 继电保护配置](../30-practice/PR-PE-001-relay-protection-config.md)
- 下游案例：见 §4 列表。

| 版本 | 日期 | 修改内容 | 修改人 |
|---|---|---|---|
| 0.1 | 2026-09-09 | 创建；含 SSR 互补频率机理、SSCI 控制-电气耦合、阻尼判据、TCSC 抑制与 SSDC 失效边界 | KB 管理员 |
