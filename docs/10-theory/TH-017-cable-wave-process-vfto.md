---
id: TH-017
title: 电缆波过程与 VFTO（暂态过电压）
domain: 基础理论
subdomain: 高电压
voltage_levels: [MV, HV, EHV]
lifecycle: [设计, 验收, 运维]
standards:
  - { code: GB/T 311.1-2012, clause: "5", note: "绝缘配合，规定 GIS 内快速暂态过电压 VFTO 的耐受水平与配合方法" }
  - { code: GB/T 11022-2020, clause: "3", note: "高压开关设备和控制设备标准的共用技术要求（idt IEC 62271-1），含 GIS 隔离开关额定参数" }
  - { code: GB 50586-2010, clause: "4.4", note: "气体绝缘金属封闭开关设备（GIS）施工及验收规范，VFTO 测量与绝缘试验要求" }
  - { code: GB/T 16927.1-2008, clause: "6", note: "高电压试验技术，规定操作冲击与快速暂态试验波形" }
status: draft
reviewers: []
version: 0.1
updated: 2026-09-09
---

# 电缆波过程与 VFTO（暂态过电压）

## 1. 定义

**波过程**指当电路特征长度 $d$ 与电磁波长 $\lambda=v/f$ 相比拟时（$d/\lambda \gtrsim 0.1$），电压、电流不再可作集总参数处理，而以**行波**形式在导体上传播、反射、透射的现象（参见 [TH-001 似稳场近似](TH-001-quasi-static-approximation.md) 的失效边界）。

**VFTO（Very Fast Transient Overvoltage，快速暂态过电压）**指 GIS（气体绝缘金属封闭开关设备）内隔离开关分合闸过程中，触头间 SF6 气体击穿在 ns 量级内完成的阶跃扰动，沿 GIS 短母线传播并在波阻抗突变点反射叠加形成的**陡波前、高频（0.3~100 MHz）、高幅值（1.5~3.0 p.u.，极端可达 4 p.u.）**暂态过电压。波前典型上升时间 4~20 ns。

| 物理量 | 符号 | 单位 |
|---|---|---|
| 分布参数波阻抗 | $Z_c$ | Ω |
| 行波传播速度 | $v$ | m/s |
| 单位长度电感 | $L_0$ | H/m |
| 单位长度电容 | $C_0$ | F/m |
| 单位长度电阻 | $R_0$ | Ω/m |
| 单位长度电导 | $G_0$ | S/m |
| 折射系数（电压） | $\alpha_u$ | — |
| 反射系数（电压） | $\beta_u$ | — |
| 时间位置 | $x,\ t$ | m, s |

## 2. 物理图像

**长线行波**：电压 $u(x,t)$、电流 $i(x,t)$ 在单位长度 $L_0,C_0$ 串并联构成的"链型电路"中传播。向前传播的电压波 $u^+$ 与同向电流波 $i^+$ 之比恒为 $Z_c$；遇到特性阻抗不同的节点（电缆终端、变压器入口、母线分支），部分反射、部分透射。

```
行波节点折射-反射：

  入射波 u⁺ →   ┃ 节点A (Zc1 → Zc2)   ┃ → 透射波 uᵗ = αu · u⁺
              ↺ 反射波 u⁻ = βu · u⁺
  其中：
  αu = 2 Zc2 / (Zc1+Zc2)
  βu = (Zc2-Zc1) / (Zc1+Zc2)
```

**VFTO 物理过程**：

```
GIS 隔离开关分合闸：触头间隙击穿（ns 完成）
   │
   ▼ 形成阶跃波（幅值 ≈ 相电压峰值，陡度 du/dt ~ 10¹¹ V/s）
   │
   ▼ 沿 SF6 母线传播，波速 v ≈ 0.27~0.30 m/ns（接近光速的 90%~100%）
   │
   ├─ 在 GIS 弯头/T 接/套管（Zc 突变）反射、透射
   ├─ 在变压器入口（电缆-绕组波阻抗骤降）多次反射
   └─ 在开路终端（βu=+1）形成 2× 入射幅值叠加
   │
   ▼ 反复折射反射叠加 → 0.1~1 μs 内形成 1.5~3.0 p.u. 振荡过电压
```

**关键对比**：相同 1 p.u. 阶跃在 GIS 内（低损耗 SF6、短母线）几乎无阻尼，幅值逼近理论极限；在油纸电缆内因介质损耗较大、波前被拉缓，过电压仅 1.1~1.3 p.u.。

## 3. 推导

### 3.1 电报方程

对均匀分布参数长线，取微元 dx：

$$
\begin{aligned}
-\frac{\partial u}{\partial x} &= R_0 i + L_0 \frac{\partial i}{\partial t} \\
-\frac{\partial i}{\partial x} &= G_0 u + C_0 \frac{\partial u}{\partial t}
\end{aligned}
$$

### 3.2 无损线（$R_0=G_0=0$）的通解

拉氏变换后联立解耦得二阶常系数线性偏微分方程，通解为**前向波 + 反向波叠加**：

$$
\begin{aligned}
u(x,t) &= u^+\!\left(t-\frac{x}{v}\right) + u^-\!\left(t+\frac{x}{v}\right) \\
i(x,t) &= \frac{1}{Z_c}\Bigl[u^+\!\left(t-\frac{x}{v}\right) - u^-\!\left(t+\frac{x}{v}\right)\Bigr]
\end{aligned}
$$

其中：

$$
v=\frac{1}{\sqrt{L_0 C_0}},\quad Z_c=\sqrt{\frac{L_0}{C_0}}
$$

> 工程速记：**同向电压电流比恒为 $Z_c$**；**反向电压电流比为 $-Z_c$**。这是折射、反射系数推导与 Bergeron 法数值求解的根基。

### 3.3 折射反射系数（彼得森法则）

节点两侧 $Z_{c1}, Z_{c2}$ 突变，入射波 $u^+$ 到达节点时：

$$
\beta_u=\frac{Z_{c2}-Z_{c1}}{Z_{c1}+Z_{c2}},\quad \alpha_u=1+\beta_u=\frac{2Z_{c2}}{Z_{c1}+Z_{c2}}
$$

| 节点 | $Z_{c2}/Z_{c1}$ | $\beta_u$ | 现象 |
|---|---|---|---|
| 开路终端（$Z_{c2}\to\infty$） | $\infty$ | $+1$ | 电压加倍 |
| 短路终端（$Z_{c2}=0$） | 0 | $-1$ | 电压归零、电流加倍 |
| 匹配终端（$Z_{c2}=Z_{c1}$） | 1 | 0 | 无反射 |

**彼得森法则**：等效电路中节点对地接入 $2Z_{c1}$ 与 $Z_{c2}$ 并联，入射波等效电压源 $u^+(t)$，节点电压即折射波 $u^t=\alpha_u u^+$——把行波问题化为集总电路问题。

### 3.4 VFTO 估算公式

假设单次击穿在 $t=0$ 形成 1 p.u. 阶跃波，开路终端反射后电压：

$$
u_{VFTO,max}^{(单次)} \approx 2 \Gamma \cdot U_{peak}
$$

其中 $\Gamma=\prod_k |\beta_{u,k}|$ 为多段母线反射系数累乘。多次击穿（隔离开关反复重燃）下，由于残余电荷叠加，工程实测**幅值 1.5~3.0 p.u.，最高可达 4 p.u.**（GB/T 311.1-2012 §5 给出 GIS 设备 VFTO 缓波前 1.6~2.0 p.u.、陡波前 2.5~3.0 p.u. 的耐受校核基线）。

### 3.5 电缆波阻抗与参数

| 电缆类型 | $Z_c$ 典型 | $v$ 典型 |
|---|---|---|
| 油纸（高压充油） | 30~50 Ω | 150~170 m/μs |
| 交联聚乙烯（XLPE） | 30~40 Ω | 160~180 m/μs |
| 同轴 SF6 母线（GIS） | 60~90 Ω | 270~300 m/μs |
| 架空线路（分裂导线） | 250~500 Ω | 295~300 m/μs |

GIS 与电缆波阻抗失配约 2~3 倍，是 VFTO 在 GIS-电缆界面反射幅值显著的物理来源。

## 4. 与工程实践的联系

- **支撑条目 1**：[PR-GR-001 防雷分类](../30-practice/PR-GR-001-lightning-protection-design.md)——GIS 变电站的行波保护与避雷器配置须考虑 VFTO；本条给出波阻抗失配、反射系数作为节点选择依据。
- **支撑条目 2**：[TH-013 开关电弧物理](TH-013-switching-arc-physics.md)——隔离开关 SF6 击穿 ns 级完成、形成 VFTO 源，两者机理衔接。
- **失效边界**：① 波过程成立前提是 $d/\lambda\gtrsim 0.1$，对 50 Hz 工频 $\lambda=6000$ km，常规 35 kV 及以下电缆仍可按集总参数处理（见 [TH-001](TH-001-quasi-static-approximation.md)）；VFTO 频率达 100 MHz，1 m 母线即满足波过程条件；② 无损线近似忽略 $R_0$、$G_0$，对远距离行波须引入衰减频变参数（J. Marti 模型）；③ 变压器绕组内部波过程（梯形波在匝间分布不均，造成首端匝绝缘应力集中）属另一类问题，本条不展开。
- **下游案例**：[CASE-016 弧光烧伤事故](../50-case/CASE-016-accident-arc-flash-burn.md)、[CASE-032 电缆终端击穿事故](../50-case/CASE-032-accident-cable-termination-breakdown.md)、[CASE-049 电缆接头施工缺陷校审](../50-case/CASE-049-review-cable-joint-construction-defect.md)、[CASE-054 光伏孤岛与逆功率校审](../50-case/CASE-054-review-pv-anti-islanding-reverse-power.md)

## 5. 关联条目与变更记录

- 关联：[TH-001 似稳场近似](TH-001-quasi-static-approximation.md)（失效边界来源）、[TH-005 接触/跨步电压](TH-005-touch-step-voltage.md)（接地网暂态电流分布）、[TH-009 雷电物理](TH-009-lightning-physics.md)（同为行波过电压，但波前时间不同）、[TH-013 开关电弧物理](TH-013-switching-arc-physics.md)（VFTO 源机理）、[TH-019 输电线路参数与长线方程](TH-019-transmission-line-parameters-long-line.md)（行波理论的稳态对应）
- 下游案例：见 §4 列表。

| 版本 | 日期 | 修改内容 | 修改人 |
|---|---|---|---|
| 0.1 | 2026-09-09 | 创建；含电报方程通解、折射反射系数、VFTO 多段反射累乘估算、电缆/GIS 波阻抗参数 | KB 管理员 |
