---
id: TH-023
title: 变压器并列运行条件与环流
domain: 基础理论
subdomain: 电机学
voltage_levels: [LV, MV, HV, EHV]
lifecycle: [设计, 运维]
standards:
  - { code: GB/T 6451-2023, clause: "4", note: "油浸式电力变压器技术参数与要求，规定联结组别与阻抗偏差容差" }
  - { code: GB/T 17468-2019, clause: "6", note: "电力变压器选用导则，含并列运行条件与并联技术要求" }
  - { code: GB/T 13499-2008, clause: "5", note: "电力变压器应用导则（idt IEC 60076-8），含并联运行负载分配与环流推导" }
  - { code: DL/T 572-2021, clause: "5", note: "电力变压器运行规程，规定并列操作与负载分配原则" }
status: draft
reviewers: []
version: 0.1
updated: 2026-09-09
---

# 变压器并列运行条件与环流

## 1. 定义

**变压器并列运行**指两台或多台变压器的一次、二次绕组分别接到同一高压/低压母线，共同承担负荷的运行方式。并列运行的**四个充分条件**：

| 序号 | 条件 | 容差 | 不满足后果 |
|---|---|---|---|
| 1 | 变比（$K=U_1/U_2$）相同 | $\Delta K/K\le 0.5\%$ | 空载环流 $I_{c0}$ |
| 2 | 联结组别（向量组别）相同 | 严格一致 | 巨大相角差环流（不允许并列） |
| 3 | 短路阻抗标幺值相同 | $\Delta Z_k/Z_k\le 10\%$ | 负载分配不均 |
| 4 | 额定容量比合理 | $S_1/S_2\le 3:1$ | 大机欠载、小机过载 |

| 物理量 | 符号 | 单位 |
|---|---|---|
| 变比 | $K=U_1/U_2$ | — |
| 短路阻抗（标幺值） | $z_k=u_k\%$ | p.u. |
| 短路阻抗（实际值） | $Z_k=z_k\cdot U_n^2/S_n$ | Ω |
| 空载环流 | $I_{c0}$ | A |
| 负载分配电流（i 台） | $I_i$ | A |
| 联结组别相位差 | $\Delta\varphi$ | ° |

## 2. 物理图像

两台并列变压器相当于两个戴维南电源（电势 $\dot E_1$、$\dot E_2$，内阻 $Z_{k1}$、$Z_{k2}$）通过低压母线并联：

```
   高压母线 ────┬────────┬────
                │        │
              T1        T2
              Z_k1      Z_k2
              E_1       E_2
                │        │
   低压母线 ────┴────────┴────

环流路径（空载）：E_1 → Z_k1 → 母线 → Z_k2 → E_2 → 高压侧（视为短接）
                  ↑_______________↓
              E_1 与 E_2 不等 → 环流形成
```

**变比不同** → 二次空载电势幅值不同 → **空载环流**（即使负荷为零也存在）。
**联结组别不同** → 二次空载电势相位不同 → **相角差环流**（幅值 = $\sqrt{2}E\sin(\Delta\varphi/2)/Z_k$，几十度相位差即接近三相短路电流）。
**短路阻抗不同** → 负载时各变压器承担电流按 $1/Z_k$ 反比分配 → **负载分配不均**（小阻抗者过载）。

## 3. 推导

### 3.1 空载环流（变比不同）

设 T1 变比 $K_1$、T2 变比 $K_2$，二次空载电压 $E_{21}=U_1/K_1$、$E_{22}=U_1/K_2$，幅值差 $\Delta E=E_{21}-E_{22}$。环流路径仅含两台短路阻抗：

$$
\dot I_{c0}=\frac{\dot E_{21}-\dot E_{22}}{Z_{k1}+Z_{k2}}\approx\frac{\Delta E}{2Z_k}
$$

（若 $Z_{k1}=Z_{k2}=Z_k$ 简化）。例：1000 kVA、$u_k=6\%$、变比差 1%（$\Delta E=400$ V × 1% = 4 V），$Z_k=6\%\times 0.4^2/1=9.6$ mΩ：

$$
I_{c0}=4/(2\times 0.0096)=208\text{ A}
$$

—— 已占额定电流 1443 A 的 14.4%！变比差必须严控 ≤0.5%（GB/T 17468 §6）。

### 3.2 联结组别相位差环流

若两台联结组别对应相位差 $\Delta\varphi$，电势相量夹角 $\Delta\varphi$，环流幅值：

$$
I_{c,\varphi}=\frac{2E\sin(\Delta\varphi/2)}{Z_{k1}+Z_{k2}}
$$

Yd11 与 Yd0 联结组别并列时 $\Delta\varphi=30°$，环流约 $\sin(15°)\times 2E/(2Z_k)=0.259\times E/Z_k$，相当于 0.26 倍短路电流（$E/Z_k$ 即三相短路电流）—— **绝对不允许并列**。

### 3.3 负载分配（短路阻抗不同）

并列运行时总负载 $S_L$，每台承担：

$$
S_i=S_L\cdot\frac{S_{ni}/z_{ki}}{\sum_j S_{nj}/z_{kj}}
$$

其中 $S_{ni}$ 为额定容量、$z_{ki}$ 为短路阻抗标幺值。**只有当 $z_{k1}=z_{k2}$ 且容量比合理时，按额定容量比例分配**。否则小阻抗变压器先达满载（详见 [GB/T 13499-2008 §5](../20-standards/cn-01-强制性通用规范与主干标准.md) §应用导则）。

### 3.4 容量比与阻抗匹配

当容量比 $S_1/S_2=\lambda$，要求 $z_{k1}/z_{k2}\in[\lambda-0.1,\lambda+0.1]$（DL/T 572 §5），否则负载分配比例偏离容量比例 10% 以上。例：1000 kVA + 315 kVA（$\lambda=3.17$）超出 3:1 上限，禁止并列。

### 3.5 不同联结组别的等效相位移

| 联结组别 | 相位移 | 同组并列 |
|---|---|---|
| Yyn0 / Dyn0 / Yzn0 | 0° | ✓ |
| Yd1 / Dyn1 | 30° | ✓ |
| Yd11 / Dyn11 | 330°（=-30°） | ✓ |
| Yd5 / Dyn5 | 150° | ✓ |
| Yd0 与 Yd11 之间 | 30° | ✗（环流巨大） |

> 工程速记：**0 与 0 可并、11 与 11 可并、0 与 11 不可并**；新建工程统一选 Dyn11（与 Yyn0 替代方向，详见 [TH-021](TH-021-neutral-grounding-and-zero-sequence-network.md)）。

## 4. 与工程实践的联系

- **支撑条目 1**：[CALC-LD-001 需要系数法负荷计算](../40-calc/CALC-LD-001-demand-factor-method.md) §变压器选择——综合楼算例选 2×630 kVA（$u_k=6\%$，相同联结组别），并列运行负载分配按容量比例（详见 TH-023 §3.3）。
- **支撑条目 2**：[PR-DD-002 变电所布置](../30-practice/PR-DD-002-substation-layout-and-equipment-selection.md) §设备选型——变压器选型须满足本条四个并列条件；切换并列前须核相、测变比、测 $Z_k$。
- **失效边界**：① 上述推导用线性变压器模型，忽略励磁支路与铁磁饱和（详见 [TH-014 磁路饱和](TH-014-magnetic-circuit-saturation.md)），空投涌流时段不能套用并列分析（涌流衰减后才进入稳态并列）；② 三绕组变压器并列须考虑三侧阻抗矩阵；③ 有载调压变压器分接头不同时变比短暂失配，但分接头自动跟踪调整后即恢复，不计入持续环流；④ 新能源电子式变压器（PCS 中隔离型 DC/DC）并列逻辑由控制器软件实现，本条不适用。
- **下游案例**：[CASE-003 变压器空投涌流致差动误动](../50-case/CASE-003-accident-transformer-inrush.md)、[CASE-020 油浸变压器短路起火](../50-case/CASE-020-accident-oil-transformer-fire.md)、[CASE-028 海上风电升压站](../50-case/CASE-028-composite-offshore-wind-substation.md)、[CASE-039 应急电源 ATS 时序](../50-case/CASE-039-review-ats-switching-time-mismatch.md)、[CASE-053 轨道交通整流](../50-case/CASE-053-composite-rail-transit-traction-rectifier.md)

## 5. 关联条目与变更记录

- 关联：[TH-006 变压器漏抗](TH-006-transformer-leakage-impedance.md)（$Z_k$ 物理来源与本条并列分配应用）、[TH-014 磁路饱和](TH-014-magnetic-circuit-saturation.md)（涌流失效边界）、[TH-021 中性点接地方式](TH-021-neutral-grounding-and-zero-sequence-network.md)（联结组别对零序通路的影响）、[CALC-LD-001 负荷计算](../40-calc/CALC-LD-001-demand-factor-method.md)、[PR-DD-002 变电所布置](../30-practice/PR-DD-002-substation-layout-and-equipment-selection.md)
- 下游案例：见 §4 列表。

| 版本 | 日期 | 修改内容 | 修改人 |
|---|---|---|---|
| 0.1 | 2026-09-09 | 创建；含四条件、空载环流与相角差环流推导、负载分配公式、联结组别相位移表 | KB 管理员 |
