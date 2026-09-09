---
id: TH-021
title: 中性点接地方式与零序网络
domain: 基础理论
subdomain: 电力系统
voltage_levels: [LV, MV, HV, EHV]
lifecycle: [设计, 运维]
standards:
  - { code: GB/T 50065-2011, clause: "4", note: "交流电气装置接地设计，含中性点接地方式选择与接地电阻/电抗整定" }
  - { code: GB 50064-2014, clause: "3", note: "交流电气装置过电压保护与绝缘配合设计规范，规定接地方式对过电压的限制要求" }
  - { code: GB 50053-2013, clause: "3.2", note: "20kV 及以下变电所设计，给出低压系统中性点接地制式选择" }
  - { code: GB/T 14285-2006, clause: "4.4", note: "继电保护与安全自动装置技术规程，含接地短路保护配合" }
status: draft
reviewers: []
version: 0.1
updated: 2026-09-09
---

# 中性点接地方式与零序网络

## 1. 定义

**中性点接地方式**指电力系统中变压器/发电机中性点对地的连接方式，按接地阻抗分类：

| 类型 | 接地阻抗 | 系统代表 | 单相接地电流 $I_k^{(1)}$ |
|---|---|---|---|
| 中性点直接接地（SNS） | $Z_N=0$ | 110 kV 及以上、低压 TN | 大，同三相短路量级 |
| 中性点经小电阻接地（NUS） | $R_N\sim$ 几~几十 Ω | 6~35 kV 城网 | 几百~1000 A |
| 中性点经消弧线圈接地 | $L_N\approx 1/(3\omega^2 C_0)$ | 6~66 kV 配网、电缆较短 | 谐振补偿后残流 <10 A |
| 中性点不接地（NUN） | $Z_N=\infty$ | 6~10 kV 配网、农村电网 | 仅电容电流 $I_C$ |
| 中性点经高电阻接地 | $R_N\sim$ 几百~几千 Ω | 发电机中性点 | <10~15 A |

**零序网络**：在 [TH-003 对称分量法](TH-003-symmetrical-components.md) 框架下，把 abc 三相不对称故障分解为正序/负序/零序三套对称网络分别求解。零序电流 $I_0=(\dot I_a+\dot I_b+\dot I_c)/3$ 必须通过中性点接地阻抗或变压器铁芯（Dyn：零序通；Yyn：零序堵）形成闭合回路，$Z_N$ 直接决定 $I_0$ 大小与零序网络拓扑。

| 物理量 | 符号 | 单位 |
|---|---|---|
| 中性点接地阻抗 | $Z_N$ | Ω |
| 单相对地电容（每相） | $C_0$ | F |
| 系统总对地电容电流 | $I_C=3\omega C_0 U_0$ | A |
| 残流（补偿后残余电流） | $I_{res}$ | A |
| 脱谐度 | $v=(I_C-I_L)/I_C$ | — |
| 零序电压 | $U_0$ | V |
| 零序补偿系数 | $k_0=(Z_0-Z_1)/Z_1$ | — |

## 2. 物理图像

中性点不接地系统单相接地后，故障相对地电压降为 0，非故障相对地电压升高至线电压（$U_{b'}=\sqrt{3}U_a$）。接地电流**仅由全系统每相对地电容提供**：

```
中性点不接地系统单相（a 相）接地：

           L1  L2  L3 三相母线
           │   │   │
           ▼   ▼   ▼
          ────┼───┼───
          Ca  Cb  Cc        每相对地电容
          │   │   │
          └─┼─┴─┬─┘
            ▼   ▼
            G  ★ 故障点（a 相接地）
            ↓
            大地

接地电流 Ik=3ωC0·U0 = 3 倍单相电容电流
非故障相电压升高至 √3 倍相电压
```

中性点经消弧线圈接地：在故障点引入感性电流 $\dot I_L=\dot U_0/(j\omega L_N)$，与电容电流 $\dot I_C=j3\omega C_0\dot U_0$ 方向相反，**相量相消**：

$$
\dot I_{res}=\dot I_C+\dot I_L=j\bigl(3\omega C_0-1/(\omega L_N)\bigr)\dot U_0
$$

调谐至 $v=0$（$I_L=I_C$）时残流仅剩高次谐波与有功分量（一般 <10 A），电弧自熄；过补偿 $v=-5\sim-10\%$ 防位移过电压。

> **变压器接线对零序网络的影响**（[TH-006 变压器漏抗](TH-006-transformer-leakage-impedance.md) 关联）：
> - **Dyn**：一次侧 d 形接法零序堵，二次侧 yn 接地形成独立零序回路；从一次看 $Z_0\to\infty$，从二次看 $Z_0=Z_k+Z_N$；
> - **Yyn**：无零序通路，$Z_0$ 受励磁支路限制（中性点电压漂移，易铁磁谐振）；
> - **YNyn**：两侧均接地且通零序，$Z_0=Z_k+Z_N$（一/二次均计入）。

## 3. 推导

### 3.1 中性点不接地系统接地电流

单相接地时，零序等值：电源端中性点电压漂移 $\dot U_0=-\dot U_a$，对地电容 $3C_0$（三相并联）通过故障点闭合：

$$
\dot I_k^{(1)} = \dot I_C = 3\omega C_0 U_\phi = \sqrt{3}\omega C_0 U_n
$$

其中 $U_\phi$ 为相电压、$U_n$ 为线电压。工程速记：**单相接地电流 = 3 倍每相电容电流**；10 kV 架空线 $I_C\approx 0.1$ A/km，电缆 $I_C\approx 1\sim2$ A/km。

### 3.2 中性点经电阻接地（NUS）

中性点接入 $R_N$，故障点零序等值回路：$R_N/3$ 与 $-j/(\omega\cdot 3C_0)$ 并联。当 $R_N=1/(3\omega C_0)$ 时（阻尼全补偿），电弧过电压倍数最低（GB 50064 推荐 $R_N$ 选 1/3 阻尼补偿点）。

故障电流：

$$
I_k^{(1)}\approx\frac{U_\phi}{R_N/3}\quad(\text{当 }R_N\ll 1/(\omega C_0)\text{，忽略电容分量})
$$

典型 10 kV 经 10 Ω 中性点电阻接地，$I_k^{(1)}\approx 577$ A（单相故障电流限定，便于零序保护灵敏动作）。

### 3.3 中性点经消弧线圈接地（谐振接地）

调谐条件（全补偿）：

$$
L_N=\frac{1}{3\omega^2 C_0}\cdot\frac{1}{1-v},\quad v=\frac{I_C-I_L}{I_C}
$$

| 脱谐度 $v$ | 工况 | 残流 | 工程取舍 |
|---|---|---|---|
| 0 | 全补偿 | 仅谐波/有功 (<5 A) | 中性点位移电压高，需并联阻尼电阻 |
| -5%~-10% | 过补偿 | <10 A | 工程首选，防欠补偿在切线路时位移过电压 |
| +5%~+10% | 欠补偿 | 10~20 A | 仅在电容电流波动小的系统 |

### 3.4 零序阻抗与接地保护配合

接地距离保护零序补偿系数 $k_0$：

$$
k_0=\frac{Z_0-Z_1}{Z_1}
$$

零序补偿后测量阻抗 $Z_{meas}=U_\phi/(I_\phi+3k_0 I_0)=z_1\cdot l$，故障相到保护安装处距离 $l$（详见 [CALC-PT-002](../40-calc/CALC-PT-002-distance-protection-setting.md) §接地距离整定）。

### 3.5 零序网络接线规则速记

| 故障类型 | 正序 | 负序 | 零序 | 三序网络 |
|---|---|---|---|---|
| 三相短路 | ✓ | ✗ | ✗ | 仅正序 |
| 两相短路 | ✓ | ✓ | ✗ | 正负串联 |
| 单相接地 | ✓ | ✓ | ✓ | 正负零串联 |
| 两相接地 | ✓ | ✓ | ✓ | 正负零并联（在故障点） |

> 工程速记：**单相接地三序串联**；**两相接地三序并联**；**两相短路无零序**；**三相短路仅正序**。

## 4. 与工程实践的联系

- **支撑条目 1**：[PR-GR-001 防雷分类](../30-practice/PR-GR-001-lightning-protection-design.md) 与 [PR-GR-002 接地制式](../30-practice/PR-GR-002-earthing-arrangement.md)——中性点接地方式决定低压系统接地制式（TN/TT/IT），低压系统接地制式必须与变电所一次侧中性点接地协调。
- **支撑条目 2**：[PR-PE-001 继电保护配置](../30-practice/PR-PE-001-relay-protection-config.md) 与 [CALC-PT-002 距离保护](../40-calc/CALC-PT-002-distance-protection-setting.md)——零序保护整定、零序补偿系数 $k_0$、中性点电阻值都建立在本条中性点接地方式选择之上。
- **失效边界**：① 不接地系统非故障相电压升高至线电压，全系统须按线电压绝缘（设备造价高），10 kV 以上不再使用；② 消弧线圈自动调谐需在线测量 $C_0$，电容电流变化（投切线路）时自动跟踪补偿；③ 经消弧线圈接地系统单相接地后仍可运行 1~2 h（GB 50053 §3.2），但须配接地选线装置；④ 配电网改电缆化后 $I_C$ 急升，原不接地/消弧线圈系统可能需改小电阻接地（城网典型改造方向）。
- **下游案例**：[CASE-034 中性点小电阻接地](../50-case/CASE-034-review-neutral-resistor-grounding.md)、[CASE-046 直流绝缘监测](../50-case/CASE-046-review-dc-insurance-monitoring-capacitance-mismatch.md)、[CASE-054 光伏孤岛与逆功率](../50-case/CASE-054-review-pv-anti-islanding-reverse-power.md)、[CASE-022 短路与保护整定](../50-case/CASE-022-exam-short-circuit-protection.md)、[CASE-053 轨道交通整流](../50-case/CASE-053-composite-rail-transit-traction-rectifier.md)

## 5. 关联条目与变更记录

- 关联：[TH-003 对称分量法](TH-003-symmetrical-components.md)（零序网络理论基础）、[TH-006 变压器漏抗](TH-006-transformer-leakage-impedance.md)（变压器接线对零序通路的影响）、[TH-014 磁路饱和](TH-014-magnetic-circuit-saturation.md)（Yyn 系统铁磁谐振）、[TH-022 过电压机理](TH-022-overvoltage-mechanism-and-insulation-coordination.md)（弧光接地过电压）、[PR-GR-002 接地制式](../30-practice/PR-GR-002-earthing-arrangement.md)、[CALC-PT-002 距离保护](../40-calc/CALC-PT-002-distance-protection-setting.md)
- 下游案例：见 §4 列表。

| 版本 | 日期 | 修改内容 | 修改人 |
|---|---|---|---|
| 0.1 | 2026-09-09 | 创建；含五类接地方式对照、不接地/电阻/消弧线圈接地电流推导、零序网络接线速记、零序补偿系数 k0 | KB 管理员 |
