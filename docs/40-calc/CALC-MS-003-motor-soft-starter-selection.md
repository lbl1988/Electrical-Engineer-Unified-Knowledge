---
id: CALC-MS-003
title: 电动机软启动器选型计算（变频/固态/自耦 三种方案比较）
domain: CALC
subdomain: MS（电机启动）
voltage_levels: [LV, MV]
lifecycle: [设计, 采购]
standards:
  - { code: GB 50055-2011, clause: "第5章", note: "通用用电设备配电设计规范：电动机启动方式选择" }
  - { code: GB 755-2019, clause: "§10 启动", note: "旋转电机 定额和性能：电动机启动电流与转矩要求" }
  - { code: IEC 60034-12:2016, clause: "全文", note: "Motors - Selection of starting methods" }
status: draft
reviewers: []
version: 0.1
updated: 2026-09-10
---

# 电动机软启动器选型计算

## 1. 算例背景

直接启动（DOL）时感应电动机启动电流 $I_{\mathrm{st}} = 6 \sim 8 I_N$，会导致：
- 电网电压跌落（$\Delta U\% > 10\%$，影响其他敏感负荷）
- 电动机绕组过流（热冲击）
- 机械传动系统扭矩冲击

**软启动器**降低启动电流（通常控制在 $1.5 \sim 4 I_N$），有三种主流方案：

| 方案 | 原理 | 启动电流 | 启动转矩 | 适用场景 |
|---|---|---|---|---|
| **变频调速（VFD）** | 改变频率，电机变频启动 | $1.0 \sim 1.5 I_N$ | 额定转矩 | 需要调速、风机水泵 |
| **固态软启动（SSR）** | 晶闸管调压，降低电压启动 | $2.0 \sim 4.0 I_N$ | 降低（$T \propto U^2$） | 不需要调速、鼠笼电机 |
| **自耦变压器** | 降低启动电压 | $1.5 \sim 3.0 I_N$ | 降低 | 高压/大功率电机 |

## 2. 核心公式

### 2.1 启动电流与启动转矩

直接启动：

$$I_{\mathrm{st,DOL}} = 6 \sim 8 I_N$$

$$T_{\mathrm{st,DOL}} = (0.5 \sim 0.7) T_N$$

变频启动（$f_{\mathrm{start}} = 10 \sim 15$ Hz 调频）：

$$I_{\mathrm{st,VFD}} \approx 1.0 \sim 1.5 I_N$$

$$T_{\mathrm{st,VFD}} \approx T_N \cdot f_{\mathrm{start}}/f_N$$

自耦变压器启动（抽头比 $k = U_{\mathrm{start}}/U_N$，典型 $k = 0.5 \sim 0.7$）：

$$I_{\mathrm{st,AT}} = k^2 \cdot I_{\mathrm{st,DOL}}$$

$$T_{\mathrm{st,AT}} = k^2 \cdot T_{\mathrm{st,DOL}}$$

固态软启动（调压 $U_{\mathrm{start}} = k \cdot U_N$，$k = 0.6 \sim 0.8$）：

$$I_{\mathrm{st,SSR}} \approx k \cdot I_{\mathrm{st,DOL}}$$

$$T_{\mathrm{st,SSR}} \approx k^2 \cdot T_{\mathrm{st,DOL}}$$

### 2.2 电网电压跌落校验

启动时系统电压跌落（标幺值）：

$$\Delta U\% = \frac{S_{\mathrm{st}}}{S_{\mathrm{sc}}} \times 100\%$$

其中：
- $S_{\mathrm{st}} = \sqrt{3} U_N I_{\mathrm{st}} / 1000$ kVA（启动容量）
- $S_{\mathrm{sc}} = \sqrt{3} U_N I''_{\mathrm{sc}} / 1000$ kVA（短路容量）

**设计阈值**：$\Delta U\% \leq 10\%$（电网容量足够时），若系统薄弱则要求 $\leq 5\%$。

## 3. 完整算例

### 3.1 已知条件

| 参数 | 值 | 说明 |
|---|---|---|
| 电机 | 132 kW 鼠笼式风机 | $P_N = 132$ kW, $U_N = 380$ V |
| $I_N$ | 238 A | |
| $I_{\mathrm{st,DOL}}$ | 7 $I_N$ = 1666 A | 直接启动 |
| $T_{\mathrm{st,DOL}}$ | 0.6 $T_N$ | |
| $U_{\mathrm{grid}}$ | 10 kV/380 V 变压器 | 1000 kVA |
| 低压侧短路容量 $S_{\mathrm{sc}}$ | 30 MVA | 典型 |

### 3.2 方案 A：直接启动（校核电压跌落）

$$S_{\mathrm{st}} = \sqrt{3} \times 380 \times 1666 / 1000 = 1096 \text{ kVA}$$

$$\Delta U\% = \frac{1096}{30000} \times 100\% = 3.65\% \leq 10\% \quad \checkmark$$

但**机械冲击大**，对风机轴承不利——实际不采用直接启动。

### 3.3 方案 B：变频调速（VFD）选算

**核心参数**：

- 变频器额定功率：$\geq 132$ kW，选 **FRN-160（160 kW）**
- 额定电流：$I_{\mathrm{VFD}} \geq 238$ A，选 **316 A 规格**

**启动参数**：

- 启动频率：$f_{\mathrm{start}} = 10$ Hz
- 启动电流：$I_{\mathrm{st,VFD}} = 1.3 I_N = 309$ A
- 启动转矩：$T_{\mathrm{st,VFD}} = 0.6 \times 10/50 \approx 0.12 T_N$（风机属于平方转矩，低频启动转矩足够）

**电压跌落**：

$$S_{\mathrm{st}} = \sqrt{3} \times 380 \times 309 / 1000 = 203 \text{ kVA}$$

$$\Delta U\% = \frac{203}{30000} \times 100\% = 0.68\% \quad \checkmark$$

**结论**：VFD 启动电流仅直接启动的 19%，电压跌落 0.68%，方案可行。

### 3.4 方案 C：固态软启动（SSR）选算

选 $k = 0.7$（启动电压 70% $U_N$）：

$$I_{\mathrm{st,SSR}} = 0.7 \times 1666 = 1166 \text{ A}$$

$$T_{\mathrm{st,SSR}} = 0.7^2 \times 0.6 T_N = 0.29 T_N$$

**选型**：SSR 额定电流 $\geq 1166$ A，选 **1300 A 规格**。

**电压跌落**：

$$\Delta U\% = \frac{\sqrt{3} \times 380 \times 1166 / 1000}{30000} \times 100\% = 2.55\% \quad \checkmark$$

**缺点**：启动转矩只有额定的 29%——风机在低速段可能转矩不够。

### 3.5 方案对比

| 指标 | DOL | VFD | SSR |
|---|---|---|---|
| 启动电流 | 7× = 1666 A | 1.3× = 309 A | 4.9× = 1166 A |
| 启动转矩 | 0.6 T_N | 0.12 T_N | 0.29 T_N |
| 电压跌落 | 3.65% | 0.68% | 2.55% |
| 机械冲击 | 大 | 小 | 中 |
| 价格（万元） | 0 | 8~15 | 3~5 |
| 后续调速 | ✗ | ✓ | ✗ |

**最终选型**：考虑风机长期需要调速，选 **160 kW VFD（FRN-160）**。

## 4. 下游应用

| 应用 | 依赖条目 |
|---|---|
| 电动机启动压降校核 | CALC-SC-001（低压短路）·CALC-MS-001（启动电压降） |
| 变频器谐波评估 | TH-033（VFD 控制策略）·CALC-HM-001（谐波潮流） |
| 变压器容量选型 | PR-DD-002（变配电选型）·CALC-LD-001（负荷计算） |

## 5. 工程注意点

| 要点 | 说明 |
|---|---|
| 变频启动转矩 | 风机/泵是平方转矩（$T \propto n^2$），低速转矩需求小；空压机/输送机是恒转矩，低频启动需提高 $V/f$ 比 |
| 谐波 | VFD 产生 5/7/11/13 次谐波，选装 LCL 滤波器（THD < 5%） |
| 固态软启动绕线电机 | 绕线电机可从转子侧绕接频敏变阻器，启动电流可降到 1.5× |
| 自耦变压器抽头 | 通常有 60%/65%/70% 三档，启动困难时换高档（电流大但转矩大） |

---

**关联条目**：[TH-007](../10-theory/TH-007-induction-motor-starting.md)（感应电机启动机理）·[TH-033](../10-theory/TH-033-induction-motor-vfd-control-strategy.md)（变频控制策略）·[CALC-MS-001](CALC-MS-001-motor-starting-voltage-drop.md)（启动电压降落）·[CALC-MS-002](CALC-MS-002-motor-temperature-rise.md)（温升计算）
