---
id: TH-018
title: 瞬时功率 p-q 理论（赤木变换）
domain: 基础理论
subdomain: 电力电子
voltage_levels: []
lifecycle: []
standards:
  - { code: GB/T 15543-2008, clause: "3", note: "电能质量 电力系统频率偏差与三相不平衡度，瞬时功率分解对应正序/负序分量" }
  - { code: GB/T 14549-1993, clause: "5", note: "电能质量 公用电网谐波，谐波检测方法的物理基础" }
  - { code: IEC 61000-4-30:2015, clause: "5", note: "电能质量测量方法，给出瞬时与半周期功率测量的口径" }
  - { code: IEEE 1459-2010, clause: "3", note: "正弦/非正弦/不平衡条件下功率定义，p-q 理论的 IEEE 标准化延伸" }
status: draft
reviewers: []
version: 0.1
updated: 2026-09-09
---

# 瞬时功率 p-q 理论（赤木变换）

## 1. 定义

[赤木 p-q 理论](../00-meta/00-术语表.md#赤木-p-q-理论)（H. Akagi, 1983）将三相瞬时电压电流变换到静止 **α-β-0 坐标系**（Clarke 变换），定义**三相瞬时实功率 p** 与**三相瞬时虚功率 q**——两者都是**时变量**，可用于任意波形（含谐波、不平衡、暂态）的功率分解，突破了 [TH-002 相量法](TH-002-phasor-analysis.md)仅适用单一频率稳态的限制。

| 物理量 | 符号 | 单位 |
|---|---|---|
| α-β 电压向量 | $u_\alpha, u_\beta$ | V |
| α-β 电流向量 | $i_\alpha, i_\beta$ | A |
| 三相瞬时实功率 | $p$ | W |
| 三相瞬时虚功率 | $q$ | var |
| 零序功率 | $p_0$ | W |
| 直流分量（基波平均） | $\bar p, \bar q$ | W, var |
| 交流分量（振荡） | $\tilde p, \tilde q$ | W, var |

## 2. 物理图像

三相正弦对称系统下，三相瞬时功率之和恒定：

$$
p(t) = u_a i_a + u_b i_b + u_c i_c = \text{const} = 3 U_+ I_+ \cos\varphi
$$

——这是三相系统相对单相系统最核心的优势（**瞬时功率脉动为零**）。但只要三相不对称（含负序）或电流含谐波（含 5、7、11 次），瞬时功率就会脉动。

赤木变换的物理意义：把 abc 三相**空间**正交分解为 α-β 平面（气隙主磁通旋转平面）与 0 轴（零序），瞬时功率分解为：

- $p=u_\alpha i_\alpha + u_\beta i_\beta$：α-β 平面实功率（对应机械/电阻消耗的"真实"能量传递）；
- $q=u_\beta i_\alpha - u_\alpha i_\beta$：α-β 平面虚功率（在三相之间往返交换、净能量传递为零）；
- $p_0=3u_0 i_0$：零序功率（中性线/接地回路消耗，主磁通无贡献）。

```
瞬时功率分解（赤木）：

  p(t) ┬─ p̄ ：基波正序有功（与负荷电阻、机械功率对应）
       ├─ p̃ ：由谐波/不对称产生的实功率振荡（补偿对象1）
       └─ p0 ：零序有功

  q(t) ┬─ q̄ ：基波正序无功（与 cosφ 补偿对应）
       └─ q̃ ：由谐波/不对称产生的虚功率振荡（补偿对象2）

补偿目标：APF 注入 −(p̃+q̃) 与零序分量 → 网侧仅剩 p̄+q̄。
```

## 3. 推导

### 3.1 Clarke 变换（功率不变约定）

$$
\begin{bmatrix} u_\alpha \\ u_\beta \\ u_0 \end{bmatrix}
=\sqrt{\frac{2}{3}}\begin{bmatrix}
1 & -\tfrac{1}{2} & -\tfrac{1}{2} \\
0 & \tfrac{\sqrt{3}}{2} & -\tfrac{\sqrt{3}}{2} \\
\tfrac{1}{\sqrt{2}} & \tfrac{1}{\sqrt{2}} & \tfrac{1}{\sqrt{2}}
\end{bmatrix}
\begin{bmatrix} u_a \\ u_b \\ u_c \end{bmatrix}
$$

满足 $\mathbf{C}^{-1}=\mathbf{C}^T$（正交），功率 $p=u_a i_a+u_b i_b+u_c i_c=u_\alpha i_\alpha+u_\beta i_\beta+3u_0 i_0$（功率不变）。

### 3.2 瞬时功率定义

赤木定义 α-β 平面瞬时功率：

$$
\begin{bmatrix} p \\ q \end{bmatrix}
=\begin{bmatrix} u_\alpha & u_\beta \\ -u_\beta & u_\alpha \end{bmatrix}
\begin{bmatrix} i_\alpha \\ i_\beta \end{bmatrix}
$$

**三相总瞬时功率**（不含零序时） $p_{3\phi}=p+p_0=u_\alpha i_\alpha+u_\beta i_\beta+3u_0 i_0$。

### 3.3 反变换：补偿电流参考值

由 $p,q$ 反解 α-β 电流：

$$
\begin{bmatrix} i_\alpha \\ i_\beta \end{bmatrix}
=\frac{1}{u_\alpha^2+u_\beta^2}\begin{bmatrix} u_\alpha & -u_\beta \\ u_\beta & u_\alpha \end{bmatrix}
\begin{bmatrix} p \\ q \end{bmatrix}
$$

**APF 补偿电流参考值**：剔除基波正序 $\bar p$ 后剩余部分对应的需要补偿的电流——

$$
\begin{bmatrix} i_{\alpha,ref} \\ i_{\beta,ref} \end{bmatrix}
=\frac{1}{u_\alpha^2+u_\beta^2}\begin{bmatrix} u_\alpha & -u_\beta \\ u_\beta & u_\alpha \end{bmatrix}
\begin{bmatrix} -\tilde p - p_0 \\ -q \end{bmatrix}
$$

（典型 APF 控制策略，补偿全部 $q$ 与全部振荡功率 $\tilde p+p_0$，保留网侧仅 $\bar p$。）

| 符号 | 含义 | 单位 |
|---|---|---|
| $\bar p$ | α-β 平面有功直流分量（基波正序平均） | W |
| $\tilde p$ | α-β 平面有功交流分量（谐波/不对称振荡） | W |
| $\bar q$ | α-β 平面虚功率直流分量（基波正序无功） | var |
| $\tilde q$ | α-β 平面虚功率交流分量（不对称振荡虚功率） | var |

### 3.4 与传统相量法的对应

对称三相正弦稳态下，$u_\alpha=\sqrt{3}U\cos\omega t$、$u_\beta=\sqrt{3}U\sin\omega t$、$i_\alpha=\sqrt{3}I\cos(\omega t-\varphi)$、$i_\beta=\sqrt{3}I\sin(\omega t-\varphi)$：

$$
\bar p=3UI\cos\varphi,\quad \bar q=3UI\sin\varphi,\quad \tilde p=\tilde q=p_0=0
$$

即稳态对称下 p-q 理论退化为相量法视在功率 $S=3UI=P+jQ$，验证两套理论的一致性。

### 3.5 局限与扩展

赤木 p-q 理论在 **电压不对称** 时存在缺陷——$u_\alpha^2+u_\beta^2$ 含 2 倍频脉动，使 $\bar p/\bar q$ 分离不再正交。Peng-Lee 的 **改进 p-q 理论**改用正序电压 $u_\alpha^+,u_\beta^+$ 作为参考，是当前 APF 工业主流算法；本条不展开。

## 4. 与工程实践的联系

- **支撑条目 1**：[PR-PQ-001 电能质量治理](../30-practice/PR-PQ-001-pq-compensation-design.md)——APF 控制算法基于 p-q 理论或其改进型，本条给出补偿电流参考值推导的物理源头。
- **支撑条目 2**：[CALC-HM-001 谐波潮流](../40-calc/CALC-HM-001-harmonic-power-flow.md)——谐波源建模、滤波器调谐点选择，瞬时功率分解给出谐波功率的时域定义（区别于频域 FFT 结果）。
- **失效边界**：① p-q 理论无频率分辨率，仅靠低通滤波分离 $\bar p$/$\tilde p$，分离带宽与动态响应相互制约；② 电压不对称下原始 p-q 分解不正交，须改进型 p-q 或 d-q 锁相；③ 三相四线制中零序功率 $p_0$ 的处理需附加中性线电流补偿；④ 对直流系统（HVDC、微电网直流母线），p-q 理论失效，须用直流瞬时功率 $p=UI$ 与电流滞环控制。
- **下游案例**：[CASE-005 变压器谐波降容校审](../50-case/CASE-005-review-transformer-harmonic-derating.md)、[CASE-041 无源滤波器失谐校审](../50-case/CASE-041-review-passive-filter-detuning-harmonic-amplification.md)、[CASE-020 油浸变压器火灾事故](../50-case/CASE-020-accident-oil-transformer-fire.md)、[CASE-042 电容器涌流事故](../50-case/CASE-042-accident-capacitor-inrush-fuse-burst.md)

## 5. 关联条目与变更记录

- 关联：[TH-002 相量法](TH-002-phasor-analysis.md)（稳态对称下两理论一致）、[TH-008 谐波产生机理](TH-008-harmonic-generation.md)（$\tilde p$、$\tilde q$ 的来源）、[TH-010 无功功率](TH-010-reactive-power.md)（瞬时功率分解传统对应）、[PR-PQ-001 电能质量治理](../30-practice/PR-PQ-001-pq-compensation-design.md)、[CALC-HM-001 谐波潮流](../40-calc/CALC-HM-001-harmonic-power-flow.md)
- 下游案例：见 §4 列表。

| 版本 | 日期 | 修改内容 | 修改人 |
|---|---|---|---|
| 0.1 | 2026-09-09 | 创建；含 Clarke 变换、p/q 定义、反变换 APF 补偿电流推导、与传统相量法对应与失效边界 | KB 管理员 |
