---
id: TH-003
title: 对称分量法
domain: 基础理论
subdomain: 电路
voltage_levels: [LV, MV, HV, EHV]
lifecycle: [设计]
standards:
  - { code: GB/T 15544.1-2013, clause: "全文", note: "不对称短路计算均建立在对称分量分解之上" }
status: published
reviewers: []
version: 1.0
updated: 2026-09-08
---

# 对称分量法（Fortescue 分解）

## 1. 定义

**对称分量法**：任意一组不对称三相相量 $\dot{F}_a,\dot{F}_b,\dot{F}_c$（电压或电流）可唯一分解为三组对称分量——**正序**（相序 a→b→c）、**负序**（a→c→b）、**零序**（三相同幅值同相位）之和。由 Fortescue（1918）提出，是分析不对称短路、断线与不平衡负荷的基本工具。

## 2. 物理图像

三相不平衡好比"三种节拍混在一起"：正序是正常运转的顺时针旋转磁场；负序是反向旋转的"逆流"；零序是三相手拉手同涨同落，其电流必须经中性线/大地形成回路。对称分量法把混乱的三相拆成三个各自对称的"纯净世界"，每个世界里三相电路解耦为单相等值电路，解完再合回去。

## 3. 推导

引入旋转算子 $a=e^{j120^\circ}=1\angle120^\circ$（$a^3=1$，$1+a+a^2=0$）：

$$\begin{bmatrix}\dot{F}_a\\ \dot{F}_b\\ \dot{F}_c\end{bmatrix} = \begin{bmatrix}1&1&1\\ 1&a^2&a\\ 1&a&a^2\end{bmatrix}\begin{bmatrix}\dot{F}_0\\ \dot{F}_1\\ \dot{F}_2\end{bmatrix},\qquad \begin{bmatrix}\dot{F}_0\\ \dot{F}_1\\ \dot{F}_2\end{bmatrix}=\frac{1}{3}\begin{bmatrix}1&1&1\\ 1&a&a^2\\ 1&a^2&a\end{bmatrix}\begin{bmatrix}\dot{F}_a\\ \dot{F}_b\\ \dot{F}_c\end{bmatrix}$$

**典型不对称故障的序网边界条件**（故障点 a 相为特殊相）：

- **单相接地（a 相，$\dot I_b=\dot I_c=0$）**：三序网络在故障点**串联**，$\dot I_1=\dot I_2=\dot I_0=\dfrac{\dot U_{a|0|}}{Z_1+Z_2+Z_0}$；
- **两相短路（b、c 相）**：正、负序网络**并联**（无零序），$\dot I_1=\dfrac{\dot U_{a|0|}}{Z_1+Z_2}$，故障相电流 $I_k^{(2)}=\sqrt{3}\,|\dot I_1|$；
- **两相接地短路**：三序网络并联接地。

由此得经典结论（远端短路、$Z_1\!\approx\!Z_2$）：

$$I_k^{(2)} = \frac{\sqrt{3}}{2} I_k^{(3)} \approx 0.866\,I_k^{(3)}$$

| 符号 | 含义 | 单位 |
|---|---|---|
| $a$ | 120° 旋转算子 | — |
| $Z_1,Z_2,Z_0$ | 正/负/零序阻抗 | Ω |
| $\dot U_{a|0|}$ | 故障点故障前电压 | V |

## 4. 与工程实践的联系

- 支撑条目：[CALC-PT-001 保护整定与灵敏度校验](../40-calc/CALC-PT-001-protection-setting.md)（灵敏度校验用**末端最小两相短路电流** $I_k^{(2)}=0.866 I_k^{(3)}$ 的来源）、[CALC-SC-001](../40-calc/CALC-SC-001-低压三相短路电流计算.md)（低压单相短路灵敏度分析的相保阻抗法即零序回路的工程简化）
- 失效边界：① 旋转电机暂态中 $Z_2\neq Z_1$ 严格成立（凸极机 $X_d''\neq X_q''$），近似需注意；② 变压器零序阻抗**强烈依赖接线组别**：Dyn 变压器零序电流经 d 侧环流闭合，$Z_0\approx Z_1$；Yyn（三柱铁芯）零序磁通被迫经油箱/空气闭合，$Z_0$ 达数倍 $Z_1$——这就是单相短路电流计算必须区分接线组别的原因；③ 三线制系统无零序通路（$3n$ 次谐波同理消失，见 [TH-008](TH-008-harmonic-generation.md)）。
- 工程速记：**"单相串联、两相并联；Dyn 零序通、Yyn 零序堵"**。

## 5. 关联条目与变更记录

- 关联：[TH-002 相量法](TH-002-phasor-analysis.md)、[TH-006 变压器漏抗](TH-006-transformer-leakage-impedance.md)、[CASE-022 2021短路电流与保护整定](../50-case/CASE-022-exam-short-circuit-protection.md)（两相短路=0.866×三相，灵敏度校验）
- 下游案例：[CASE-036 CT极性接反](../50-case/CASE-036-review-ct-polarity-differential-malfunction.md)

| 版本 | 日期 | 修改内容 | 修改人 |
|---|---|---|---|
| 1.0 | 2026-09-08 | 创建 | KB 管理员 |
