---
id: PR-PQ-001
title: 无功补偿与谐波治理设计要点
domain: PR
subdomain: PQ（电能质量）
voltage_levels: [LV, MV]
lifecycle: [设计, 运维]
standards:
  - { code: GB/T 14549-1993, clause: "全文", note: "公用电网谐波：PCC 处注入谐波电流允许值（按协议容量分配）" }
  - { code: GB/T 12325-2008, clause: "", note: "供电电压偏差限值" }
  - { code: GB 50052-2009 / GB/T 51348-2019, clause: "有关条款", note: "补偿装置装设位置、分组投切要求" }
  - { code: GB/T 40427-2021, clause: "", note: "电压与无功分层分区就地平衡原则" }
status: published
reviewers: []
version: 1.0
updated: 2026-09-08
---

# 无功补偿与谐波治理设计要点

## 1. 摘要

电能质量治理的完整设计链：**负荷建模 → 无功补偿容量（→ [CALC-RC-001](../40-calc/CALC-RC-001-reactive-compensation.md)）→ 谐波评估（GB/T 14549 注入校验）→ 电抗率选择 → 滤波/有源方案 → 投切控制**。本条给出流程决策表、治理手段矩阵（FC 调谐滤波/SVG/APF 的适用边界）、PCC 校验要点与"纯电容挂在 5 次背景电网"等 5 类高频错误；算例延续综合楼案例（120kvar/7% 电抗方案）。

## 2. 术语与定义

| 术语 | 定义 | 标准出处 |
|---|---|---|
| PCC | 公共连接点（用户与电网的产权分界点） | GB/T 14549-1993 |
| TDD | 总谐波畸变率（以**需量基波电流**为基准，IEEE 519 口径） | IEEE 519/见 [MAP-G](../20-standards/mapping-中外对照表.md) |
| 调谐滤波器（FC） | 电感电容调谐于某次谐波（如 4.7 次吸收 5 次）的无源支路 | 手册 |
| SVG | 静止无功发生器（链式/降压型），毫秒级连续无功 | 行业通识 |
| APF | 有源电力滤波器，检测谐波电流并注入反相抵消 | 同上 |

## 3. 原理与公式（设计流程）

```
① 负荷建模：设备谐波谱（样本/GB/T 14549 附录实测）、自然功率因数、波动特性
② 无功补偿：QC=P30(tanφ1−tanφ2) → CALC-RC-001 §7.2
③ 谐波评估：各次注入电流 Ih ≤ GB/T 14549 允许值（按协议容量分配至 PCC）
④ 电抗率：背景 5 次 → 7%；3 次 → 14%（谐振次数 ν=1/√p，判据见 CALC-RC-001 §3）
⑤ 治理升级判据：
   · 仅无功不足、谐波达标 → FC（串抗电容器）
   · 谐波超标且次别集中（5/7/11）→ 调谐滤波支路（兼顾补偿）
   · 波动快/谐波谱杂/不平衡 → SVG（无功）或 APF（谐波），或 FC+SVG 混合
⑥ 投切控制：自动循环/编码、过零投切、防振逻辑（小容量细分组）
```

**GB/T 14549 校验式**（转述框架）：用户注入 PCC 的第 $h$ 次谐波电流 $I_h$ 不超过按协议容量 $S_i$ 分配的允许值 $I_{h,允许}=I_{h,基准}\times(S_i/S_t)^{1/\alpha}$（分配系数 $\alpha$ 按标准表取），基准值查标准表（电压等级×谐波次数）。

## 4. 标准依据表

| 标准号-年份 | 条款 | 要求要点（转述） | 适用边界 |
|---|---|---|---|
| GB/T 14549-1993 | 全文 | PCC 谐波电流允许值与分配、测量方法 | 公用电网 0.38~110kV |
| GB/T 12325-2008 | 全文 | 电压偏差限值（补偿过欠均影响） | 供电质量 |
| GB/T 51348-2019 | 有关条款 | 低压补偿分组、投切与防振 | 民用建筑 |
| GB/T 40427-2021 | 全文 | 分层分区就地平衡（系统侧原则） | 电力系统规划 |

## 5. 设计/选型要点（校审清单）

- [ ] 供电协议取考核点 PCC 与目标 $\cos\varphi$；补偿度避免过补偿（容性倒送/夜间电压抬升）
- [ ] 谐波源设备（变频器/UPS/LED 驱动/充电桩）在负荷表中**单列谐波谱列**（次数×含量）
- [ ] 电容器校验三件事：端电压抬升（$U_C=U_n/(1-p)$ 选高一档）、谐波电流过载（≤1.3 倍额定电流级，按厂家标准）、熔丝/放电器配套
- [ ] APF 容量估算：APF ≥ 谐波电流总量（系数法：变频负荷 0.3~0.4×额定电流经验值，实测优先）
- [ ] 投切器件：频繁波动负荷用晶闸管（TSC）；稳定负荷接触器即可（经济性）
- [ ] 闪变敏感点（电焊机/轧机）按 GB/T 12326 校验 Pst（→ [MAP-I](../20-standards/mapping-中外对照表.md)）
- [ ] 并网分布式电源（光伏/储能）倒送工况下补偿方向反转校验（→ [TH-010 失效边界④](../10-theory/TH-010-reactive-power.md)）

## 6. 常见错误与争议

| 错误/争议 | 后果 | 正确做法/主流处理 | 依据 |
|---|---|---|---|
| 背景有 5 次谐波仍挂纯电容 | 并联谐振放大，电容鼓包/熔丝群爆 | 串 7% 电抗（3 次背景 14%） | GB/T 51348/14549 |
| 电抗器与电容器非成套参数 | 失谐点漂移、放大反而更糟 | 成套采购（p、Uc、K 因子匹配），订货标明 | 厂家成套 |
| 用 THDu 达标推定谐波电流达标 | 电压畸变轻≠注入电流合规 | GB/T 14549 管**注入电流**（分配制），两者都校 | GB/T 14549 |
| APF 按视在功率选型 | 容量口径混淆（谐波补偿能力） | 按谐波电流（A）选型；混合需求分列无功/谐波容量 | 厂家样本 |
| 夜间轻载大组全投 | 电压抬升、容性倒送受罚 | 细分组＋自动切除判据（欠无功/过电压） | GB/T 51348 |

## 7. 完整算例（综合楼，衔接 [CALC-LD-001](../40-calc/CALC-LD-001-demand-factor-method.md)/[CALC-RC-001](../40-calc/CALC-RC-001-reactive-compensation.md)）

### 7.1 无功补偿（结论引用）

$P_{30}$=395.1kW、$\cos\varphi$=0.797 → **装设 120kvar（6×20，串 7%，480V 级电容器），补偿后 0.911**（完整推导 → CALC-RC-001 §7）。

### 7.2 谐波评估与电抗率

负荷：变频电梯（6 脉冲，特征 5/7 次）＋ LED 驱动（3 次+高次）→ 背景 **5 次为主**：
- $\nu(7\%)=3.78<5$ → 5 次呈感性不放大 ✓（3 次轻微，运行后实测复核）；
- 若实测 3 次超预期 → 局部补 14% 支路或小容量 APF（电梯群 5/7 次集中时优先 APF 30~50A 档）。

### 7.3 运行监测

投运后于 PCC 处连续监测一周（GB/T 14549 测量口径）：$I_5/I_7$ 注入值 vs 允许值、$\cos\varphi$ 逐时曲线（夜间防过补）、电容器电流（≤1.3 倍额定）——数据归档至运维记录（CM 域）。

## 8. 关联条目

- 上游：[TH-008 谐波机理](../10-theory/TH-008-harmonic-generation.md)、[TH-010 无功功率](../10-theory/TH-010-reactive-power.md)、[TH-018 瞬时功率 p-q 理论](../10-theory/TH-018-instantaneous-power-pq-theory.md)（APF 控制算法的物理源头，赤木变换推导补偿电流参考值）、[TH-024 电力电子变换器基础拓扑与 PWM](../10-theory/TH-024-power-electronic-converters-and-pwm.md)（SVG/APF 硬件拓扑与 SVPWM 调制物理来源）、[TH-028 柔性交流输电 FACTS](../10-theory/TH-028-facts-flexible-ac-transmission.md)（SVC/STATCOM 无功输出与暂态稳定重塑，SVG 即 STATCOM 别称）、[TH-032 同步电机进相与调相运行](../10-theory/TH-032-synchronous-machine-leading-and-condensing-operation.md)（调相机作为旋转 STATCOM 的容量与进相限制）、[TH-033 异步电机变频调速控制策略](../10-theory/TH-033-induction-motor-vfd-control-strategy.md)（变频器谐波源与配套输入滤波器选型依据）、[TH-037 变压器有载调压与动态无功协调](../10-theory/TH-037-tap-changer-and-dynamic-reactive-coordination.md)（OLTC 调压与无功补偿时间尺度解耦、9 区图协调控制策略）、[TH-040 交直流混联电网稳定](../10-theory/TH-040-hybrid-ac-dc-grid-stability.md)（MIDC 受端动态无功配置与 MISCR 校核）、[TH-043 AI 在电气工程应用基础](../10-theory/TH-043-ai-foundations-in-electrical-engineering.md)（负荷预测与 SVG/APF 自适应控制）、[TH-044 电力电子化电力系统低惯量与宽频振荡](../10-theory/TH-044-power-electronics-dominated-system-low-inertia-wideband-oscillation.md)（宽频阻抗谐振点识别与有源阻尼）
- 下游：[CALC-RC-001 补偿计算](../40-calc/CALC-RC-001-reactive-compensation.md)、APF/SVG 选型（PQ 域规划）、[CASE-025 2023无功补偿与谐波谐振真题](../50-case/CASE-025-exam-reactive-compensation-harmonic-resonance.md)（2023无功补偿与谐波谐振真题）、[CASE-033 储能电站全流程](../50-case/CASE-033-composite-energy-station-full-process.md)（储能PQ控制）
- 下游案例：[CASE-041 无源滤波器](../50-case/CASE-041-review-passive-filter-detuning-harmonic-amplification.md)、[CASE-042 电容器涌流](../50-case/CASE-042-accident-capacitor-inrush-fuse-burst.md)、[CASE-044 电容器过电压保护](../50-case/CASE-044-review-capacitor-overvoltage-spd-coordination.md)、[CASE-048 新能源谐波SVG](../50-case/CASE-048-composite-renewable-collector-station-protection.md)、[CASE-053 牵引整流谐波](../50-case/CASE-053-composite-rail-transit-traction-rectifier.md)、[CASE-054 光伏电能质量](../50-case/CASE-054-review-pv-anti-islanding-reverse-power.md)
- 平行：[mapping MAP-G/H/I](../20-standards/mapping-中外对照表.md)（中外电能质量体系差异）
- 计算支撑：[CALC-HM-001 谐波潮流计算](../40-calc/CALC-HM-001-harmonic-power-flow.md)（谐波电流叠加与电压含有率校核，APF选型依据）

## 9. 变更记录

| 版本 | 日期 | 修改内容 | 修改人 |
|---|---|---|---|
| 1.0 | 2026-09-08 | 创建 | KB 管理员 |
