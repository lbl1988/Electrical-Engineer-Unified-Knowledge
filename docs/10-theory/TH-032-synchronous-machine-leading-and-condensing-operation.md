---
id: TH-032
title: 同步电机进相与调相运行
domain: 基础理论
subdomain: 同步电机
voltage_levels: [MV, HV]
lifecycle: [设计, 运维]
standards:
  - { code: GB/T 7064-2017, clause: "4", note: "隐极同步电机技术要求（含进相与调相运行能力）" }
  - { code: DL/T 5810-2020, clause: "4", note: "电力系统电压和无功电力技术导则，规定调相机与发电机进相运行" }
  - { code: GB/T 36547-2018, clause: "4", note: "电化学储能接入电网技术规定，含调相机替代方案" }
  - { code: DL/T 1166-2012, clause: "4", note: "同步发电机进相运行试验导则" }
status: draft
reviewers: []
version: 0.1
updated: 2026-09-09
---

# 同步电机进相与调相运行

## 1. 定义

**进相运行**指同步发电机在欠励磁状态下（励磁电流低于正常值），从电网吸收感性无功（等效发出容性无功）以抑制系统电压过高的运行方式。**调相运行（调相机）**指同步电机不发有功（$P\approx 0$），专门发出或吸收无功以调节电压的运行方式。

| 运行模式 | 励磁 | $P$ | $Q$ | 系统用途 |
|---|---|---|---|---|
| 过励磁（正常发电） | 超前 | $+P$（发出） | $+Q$（发出感性） | 常规发电 |
| 进相运行 | 欠励 | $+P$（发出） | $-Q$（吸收感性） | 夜间低谷降压 |
| 调相运行（过励） | 超前 | $\approx 0$ | $+Q$（大发出） | 电压支撑 |
| 调相运行（进相） | 欠励 | $\approx 0$ | $-Q$（大吸收） | 抑制过电压 |

调相机是电网最早的"STATCOM"，目前在新能源汇集站（如海上风电送出、直流输电换流站）仍有应用。

## 2. 物理图像

### 2.1 功角特性与进相

同步电机稳态运行点由功角方程决定（详见 [TH-016 功角稳定](TH-016-synchronous-machine-power-angle-stability.md)）：

$$
P=\frac{E_0 U}{X_d}\sin\delta
$$

$E_0$ 由励磁决定。减小励磁 $E_0$ 下降 → 维持相同 $P$ 时 $\delta$ 增大 → 功角向稳定极限 $90^\circ$ 逼近——这是进相运行静态稳定裕度下降的物理原因。

### 2.2 V 形曲线

保持有功 $P$ 恒定，励磁电流与定子电流的关系呈"V"形：

```
  I_stator ↑
       │    过励区        进相区
       │     ↘      ↙
       │      ↘  ↙
  I_N ─┤──────×← 正常励磁点
       │     ╱  ╲
       │    ╱    ╲
       └──┴──────────→ I_field
         I_f0
```

过励区定子电流随励磁增加而上升（无功发出增加）；进相区同样随励磁减小而上升（无功吸收增加）。V 形最低点对应 $\cos\varphi=1$（纯有功）。

## 3. 推导

### 3.1 进相运行静态稳定极限

发电机端电压 $\dot U$ 与内电势 $\dot E_0$ 关系：

$$
\dot E_0 = \dot U + j\dot I X_d
$$

进相运行 $\dot I$ 超前 $\dot U$（$\varphi<0$），以 $\dot U$ 为参考：

$$
E_0 = \sqrt{(U + I X_d\sin|\varphi|)^2 + (I X_d\cos|\varphi|)^2}
$$

进相时 $E_0<U$（因 $IX_d\sin|\varphi|$ 项为负）。功角：

$$
\delta = \arctan\frac{I X_d \cos|\varphi|}{U - I X_d\sin|\varphi|}
$$

进相越深 $\varphi$ 越负 → 分母越小 → $\delta$ 增大 → 静态稳定裕度 $K_p=P/P_{max}$ 下降。

| 功率因数 | $\delta$（典型） | 稳定裕度 $K_p$ |
|---|---|---|
| $\cos\varphi=0.95$（滞后） | 30° | 2.0 |
| $\cos\varphi=1.0$ | 40° | 1.56 |
| $\cos\varphi=0.95$（超前） | 55° | 1.22 |
| $\cos\varphi=0.90$（超前） | 65° | 1.10 |

### 3.2 进相运行端部发热限制

进相时定子端部漏磁增加（主磁通减弱，端部合成磁通相对增强），在定子端部铁芯与压指中产生涡流损耗，温升可能超标——这是进相运行的第二重约束。

端部温升近似：

$$
\Delta\theta_{end}\propto B_{end}^2\propto\left(\frac{U}{X_d}\cdot\sin|\varphi|\right)^2
$$

大型隐极发电机进相深度受端部温升限制，通常厂家提供 $P$-$Q$ 包络曲线（进相边界由静态稳定与端部温升两者较小值决定）。

### 3.3 调相机容量

调相机不发有功时全部容量用于无功调节：

$$
Q_{max}^{over}=\frac{E_{0,max}U - U^2}{X_d}\quad(\text{过励发出})
$$

$$
Q_{max}^{under}=\frac{U^2 - E_{0,min}U}{X_d}\quad(\text{进相吸收})
$$

调相机过励容量通常为进相容量的 2~3 倍（因 $E_{0,max}\gg E_{0,min}$）。

## 4. 与工程实践的联系

- **支撑条目 1**：[PR-PQ-001 电能质量治理](../30-practice/PR-PQ-001-pq-compensation-design.md) 与 [TH-028 柔性交流输电 FACTS](TH-028-facts-flexible-ac-transmission.md)——调相机是旋转式 STATCOM，本条给出其无功容量与进相限制。
- **支撑条目 2**：[TH-020 电力系统稳定性分类](TH-020-power-system-stability-classification.md) 与 [TH-016 功角稳定](TH-016-synchronous-machine-power-angle-stability.md)——进相运行静态稳定裕度下降是系统稳定性约束。
- **支撑条目 3**：[PR-ES-001 储能接入](../30-practice/PR-ES-001-energy-storage-integration.md) 与 [TH-027 HVDC](TH-027-hvdc-transmission-lcc-vsc.md)——新能源汇集站与 LCC-HVDC 换流站常配调相机提供无功支撑。
- **失效边界**：① 进相运行静态稳定裕度随深度急剧下降，须保留 $K_p\ge1.1$~$1.3$；② 端部温升限制与机型强相关，须厂家提供 $P$-$Q$ 包络曲线；③ 调相机启动损耗大（须异步启动或变频启动），不适合频繁启停；④ 调相机响应速度（数百 ms~秒级）慢于 STATCOM（ms 级），暂态无功支撑不如 VSC；⑤ 进相运行时机端电压下降可能触发欠励限制器动作。
- **下游案例**：[CASE-028 海上风电升压站](../50-case/CASE-028-composite-offshore-wind-substation.md)、[CASE-048 新能源汇集站继保](../50-case/CASE-048-composite-renewable-collector-station-protection.md)

## 5. 关联条目与变更记录

- 关联：[TH-016 同步电机功角稳定](TH-016-synchronous-machine-power-angle-stability.md)（功角方程与稳定裕度）、[TH-015 Park 方程](TH-015-synchronous-machine-park-equations.md)（暂态电势与 $X_d$）、[TH-020 电力系统稳定性分类](TH-020-power-system-stability-classification.md)（静态稳定约束）、[TH-028 FACTS](TH-028-facts-flexible-ac-transmission.md)（调相机与 STATCOM 对比）、[TH-027 HVDC](TH-027-hvdc-transmission-lcc-vsc.md)（换流站无功支撑）、[PR-PQ-001 电能质量治理](../30-practice/PR-PQ-001-pq-compensation-design.md)
- 下游案例：见 §4 列表。

| 版本 | 日期 | 修改内容 | 修改人 |
|---|---|---|---|
| 0.1 | 2026-09-09 | 创建；含 V 形曲线、进相静态稳定极限推导、端部温升约束、调相机容量公式与 STATCOM 对比失效边界 | KB 管理员 |
