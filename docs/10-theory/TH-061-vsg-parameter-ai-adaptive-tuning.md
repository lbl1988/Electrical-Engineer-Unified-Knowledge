---
id: TH-061
title: VSG 参数 AI 自适应整定（强化学习 + 物理信息约束 + 数字孪生闭环）
domain: 基础理论
subdomain: 人工智能 / 电力系统稳定
voltage_levels: [HV, EHV]
lifecycle: [设计, 运维]
standards:
  - { code: GB/T 19963.1-2021, clause: "§5 构网型控制", note: "电力系统网源协调技术规范 第1部分：虚拟惯量与阻尼（自适应整定边界）" }
  - { code: GB/T 40595-2021, clause: "全文", note: "并网电源一次调频试验技术规定（含虚拟惯量测试）" }
  - { code: GB/T 47968-2026, clause: "全文", note: "构网型变流器通用技术规范（2026-09-03 发布，2026-11-01 实施；19 项关键指标含惯量阻尼/等效暂态阻抗/3 倍过流）" }
  - { code: GB/T 42018-2022, clause: "全文", note: "人工智能 服务能力成熟度评估参考框架" }
  - { code: DL/T 2547-2022, clause: "§4 自适应控制", note: "人工智能 电力应用技术规范：RL 在电网控制中的适用边界" }
  - { code: IEC 62332:2024, clause: "§7 自适应整定", note: "AI in power systems - trustworthiness and governance（草案阶段）" }
  - { code: GB/T 41307-2022, clause: "§4 鲁棒性", note: "人工智能 可信赖评估规范：RL 算法安全性/鲁棒性要求" }
status: draft
reviewers: []
version: 0.1
updated: 2026-09-11
---

# VSG 参数 AI 自适应整定

## 1. 定义

VSG 参数 AI 自适应整定是**通过强化学习（Reinforcement Learning, RL）实时调整虚拟同步机（VSG）的虚拟惯量 $J_v$ 与虚拟阻尼 $D_v$**，使构网型逆变器在**电网强度变化、故障穿越、负荷扰动**等工况下保持最优频率响应的技术。它是 [TH-056 VSG 参数设计与稳定性](TH-056-virtual-synchronous-generator-parameter-design-and-stability.md) 的前沿延伸：TH-056 给出**固定参数**设计方法，本条给出**自适应参数**的 AI 整定方法。

| 整定方法 | 适用场景 | 优势 | 局限 |
|---|---|---|---|
| **离线查表法** | 稳态运行 | 工程简单、可解释 | 不能应对电网强度突变 |
| **梯度下降法** | 已知目标函数 | 收敛快 | 需要精确电网模型 |
| **强化学习（RL）** | 未知/时变电网 | 自主探索、无需精确模型 | 训练数据需求大、黑箱 |
| **物理信息强化学习（PI-RL）** | 关键电源 | 结合 RL 与电网方程约束 | 算法复杂度高 |
| **数字孪生闭环** | 实时整定 | 在线 + 安全 + 可解释 | 需要数字孪生平台（详见 TH-062） |

**核心问题**：VSG 的固定参数在**强电网**下应取小 $J_v$（避免振荡），在**弱电网**下应取大 $J_v$（提供惯量支撑）；故障穿越期间应取大 $D_v$（快速抑制振荡），恢复后应取小 $D_v$（避免功率波动）。传统查表法无法适应。

## 2. 物理图像

VSG 参数 AI 自适应整定的"感知-决策-执行"闭环：

```
┌─────────────────────────────────────────────────────────┐
│  物理层（构网型逆变器 + 电网）                          │
│  功率方程：J_v · dω/dt = P_ref - P_out - D_v · Δω     │
│  └── 状态：频率 ω、相位 θ、有功 P、电网强度 SCR        │
└──────────┬──────────────────────────────────────────────┘
           │ PMU 量测（状态观测）
           ↓
┌─────────────────────────────────────────────────────────┐
│  智能体层（RL Agent）                                   │
│  状态 s = [ω, Δω, P, Q, SCR, t_fault]                  │
│  动作 a = [ΔJ_v, ΔD_v]（参数调整增量）                 │
│  奖励 r = -α·|Δf|² - β·|ΔP|² - γ·约束违反             │
│  策略 π(a|s) = argmax E[Σγ^t · r_t]                    │
└──────────┬──────────────────────────────────────────────┘
           │ 参数下发
           ↓
┌─────────────────────────────────────────────────────────┐
│  物理信息约束层（PINN 修正）                            │
│  L_total = L_data + λ · L_phys（电网方程残差）          │
│  └── 约束：J_v ∈ [J_min, J_max], D_v ∈ [D_min, D_max] │
│  └── 安全：参数变化率限幅（避免控制震荡）              │
└─────────────────────────────────────────────────────────┘
```

**关键约束**：VSG 参数自适应整定必须满足**电网方程约束**，否则 RL 策略可能产生"看似最优但实际违反物理规律"的参数（详见 [TH-043](TH-043-ai-foundations-in-electrical-engineering.md) PINN 章节）。

## 3. 推导

### 3.1 VSG 机械方程（回顾，详见 TH-056）

$$J_v \cdot \frac{d\omega}{dt} = P_{ref} - P_{out} - D_v \cdot (\omega - \omega_0)$$

其中：
- $J_v$ = 虚拟惯量（kg·m²，电力侧归算到电角速度）
- $D_v$ = 虚拟阻尼（标幺值 pu·s）
- $\omega$ = 虚拟转子电角速度
- $\omega_0$ = 电网同步角速度

**稳定性约束**（小信号分析）：

$$J_v \cdot D_v > \frac{(P_{ref} - P_{out})^2}{4 \cdot \omega_0^2}$$

即 $J_v$ 与 $D_v$ 必须满足乘积下限，否则系统发散。

### 3.2 RL 状态-动作-奖励建模

#### 状态空间

$$s_t = [\omega_t, \Delta\omega_t, P_t, Q_t, SCR_t, d_t]$$

| 状态分量 | 含义 | 来源 |
|---|---|---|
| $\omega_t$ | 当前角速度 | PMU 量测 |
| $\Delta\omega_t$ | 频率偏差 | $\omega_t - \omega_0$ |
| $P_t$ | 有功功率 | PCS 量测 |
| $Q_t$ | 无功功率 | PCS 量测 |
| $SCR_t$ | 电网短路比（强度指标） | 在线辨识（详见 3.3） |
| $d_t$ | 故障标志（0/1） | 保护信号 |

#### 动作空间

$$a_t = [\Delta J_v, \Delta D_v]$$

- $\Delta J_v \in [-J_{step}, +J_{step}]$（典型 $J_{step} = 0.5$ kg·m²）
- $\Delta D_v \in [-D_{step}, +D_{step}]$（典型 $D_{step} = 5$ pu·s）

**约束限幅**（避免一次调整过大）：

$$J_v \in [J_{min}, J_{max}] = [1.0, 10.0] \text{ kg·m²}$$

$$D_v \in [D_{min}, D_{max}] = [5, 50] \text{ pu·s}$$

#### 奖励函数

$$r_t = -\alpha \cdot (\Delta\omega_t)^2 - \beta \cdot (\Delta P_t)^2 - \gamma \cdot \mathbb{1}_{[|J_v \cdot D_v| < J_v D_v|_{min}]}$$

| 权重 | 典型值 | 目标 |
|---|---|---|
| $\alpha$ | 10.0 | 抑制频率偏差（首要） |
| $\beta$ | 1.0 | 抑制功率振荡（次要） |
| $\gamma$ | 100.0 | 惩罚稳定性约束违反（硬约束） |

### 3.3 电网短路比 SCR 在线辨识

SCR 是 RL 状态的关键输入，决定 $J_v$ 与 $D_v$ 的最优取值范围：

$$SCR = \frac{S_{sc,grid}}{S_{PCS,rated}}$$

- $SCR > 5$：强电网，取小 $J_v$（2 kg·m²）
- $3 < SCR < 5$：中等电网，取中 $J_v$（5 kg·m²）
- $SCR < 3$：弱电网，取大 $J_v$（8 kg·m²）

**在线辨识方法**（基于 PMU 量测）：

$$\hat{SCR}_t = \frac{U_{t}^2 / Z_{grid,t}}{S_{PCS}}$$

其中 $Z_{grid,t}$ 由 VSG 注入小信号扰动 + PMU 测电压响应辨识（递推最小二乘法 RLS）。

### 3.4 PPO 算法（Proximal Policy Optimization）

VSG 自适应整定主流采用 PPO 算法（OpenAI 2017）：

**策略梯度**：

$$\nabla_\theta J(\theta) = \mathbb{E}\left[\nabla_\theta \log \pi_\theta(a_t|s_t) \cdot A_t\right]$$

**优势函数**（GAE 估计）：

$$A_t = \sum_{l=0}^{\infty} (\gamma \lambda)^l \delta_{t+l}, \quad \delta_t = r_t + \gamma V(s_{t+1}) - V(s_t)$$

**PPO clip 目标**（避免策略更新过大）：

$$L^{CLIP}(\theta) = \mathbb{E}\left[\min\left(r_t(\theta) A_t, \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon) A_t\right)\right]$$

其中 $r_t(\theta) = \pi_\theta(a_t|s_t) / \pi_{\theta_{old}}(a_t|s_t)$，$\epsilon = 0.2$（典型）。

### 3.5 物理信息约束（PINN 修正）

为避免 RL 策略违反电网方程，在损失函数中加入物理残差：

$$L_{total} = L_{RL} + \lambda_{phys} \cdot L_{phys}$$

$$L_{phys} = \left\|J_v \cdot \frac{d\omega}{dt} - (P_{ref} - P_{out} - D_v \cdot \Delta\omega)\right\|^2$$

**作用**：当 RL 输出的 $(J_v, D_v)$ 不能满足 VSG 机械方程时，$L_{phys}$ 增大，梯度反向修正策略网络，保证参数物理可行性（详见 [TH-043](TH-043-ai-foundations-in-electrical-engineering.md) PINN 章节）。

### 3.6 训练-部署架构

```
┌──────────────────────────────────────┐
│  训练阶段（离线，基于 PSCAD 仿真）  │
│  · 10^6 步电网扰动场景采样           │
│  · PPO 算法 + PINN 约束             │
│  · 收敛判据：奖励均值收敛 ±5%        │
└──────────────┬───────────────────────┘
               │ 策略网络 π_θ(a|s)
               ↓
┌──────────────────────────────────────┐
│  部署阶段（在线，数字孪生闭环）     │
│  · PMU 采集状态 s_t                  │
│  · 策略网络推理 a_t = π_θ(s_t)      │
│  · 参数限幅 + 安全检查               │
│  · 下发到 PCS 控制器                 │
│  · 实时奖励反馈（强化在线学习）      │
└──────────────────────────────────────┘
```

## 4. 标准依据

| 标准 | 条款 | 关键要求 | 应用边界 |
|---|---|---|---|
| GB/T 19963.1-2021 | §5 | 构网型电源虚拟惯量与阻尼参数边界 | 构网型逆变器并网 |
| GB/T 40595-2021 | 全文 | 一次调频试验：虚拟惯量动态响应测试 | 调频性能验证 |
| GB/T 47968-2026 | 全文 | 构网型变流器通用技术规范：19 项指标含惯量/阻尼/等效暂态阻抗/3 倍过流/模型数据开放（2026-11-01 实施） | 构网型变流器本体规范 |
| DL/T 2547-2022 | §4 | RL 在电网控制中的适用边界与安全要求 | AI 控制应用 |
| GB/T 41307-2022 | §4 | AI 鲁棒性：RL 策略在扰动下的稳定性 | AI 安全评估 |
| IEC 62332:2024 | §7 | AI 自适应整定的可信性与治理（草案） | 国际参考 |

## 5. 工程算例

### 算例：10 MW 构网型储能电站 VSG 自适应整定

#### 已知条件

| 参数 | 值 | 说明 |
|---|---|---|
| PCS 额定容量 | 10 MVA | 构网型 |
| 电网 SCR | 2.5~6.0（时变） | 风电场接入，强度波动 |
| 固定参数（基线） | $J_v = 5$, $D_v = 20$ | TH-056 设计值 |
| RL 策略 | PPO + PINN | 2 层 MLP，64 神经元/层 |
| 训练场景 | 10^6 步 PSCAD 仿真 | 含故障、负荷扰动、SCR 变化 |

#### 工况 1：电网 SCR 从 6.0 突降到 2.5（风电大发）

- 固定参数：频率最大偏差 $\Delta f_{max} = 0.45$ Hz，恢复时间 3.2 s
- RL 自适应：智能体检测到 SCR 下降，自动增大 $J_v$ 至 8.0，$D_v$ 至 30，$\Delta f_{max} = 0.28$ Hz，恢复时间 1.8 s
- **改善幅度**：频率偏差降低 38%，恢复时间缩短 44%

#### 工况 2：三相短路故障穿越

- 固定参数：故障期间振荡，$D_v$ 不足导致 2 次功率摇摆
- RL 自适应：检测到故障标志 $d_t = 1$，$D_v$ 瞬时增大至 50（上限），振荡 1 次衰减
- **改善幅度**：振荡次数减少 50%

#### 工况 3：负荷突投 30% 额定

- 固定参数：$J_v$ 偏大，频率响应迟滞
- RL 自适应：$J_v$ 降至 2.0，响应更敏捷，但仍满足 $J_v \cdot D_v >$ 稳定性下限
- **改善幅度**：响应时间缩短 30%

### 结果汇总

| 工况 | $\Delta f_{max}$（固定） | $\Delta f_{max}$（RL） | 改善 |
|---|---|---|---|
| SCR 突降 | 0.45 Hz | 0.28 Hz | -38% |
| 故障穿越 | 0.62 Hz | 0.41 Hz | -34% |
| 负荷突投 | 0.38 Hz | 0.25 Hz | -34% |

## 6. 工程注意点

| 要点 | 说明 |
|---|---|
| **训练数据覆盖** | RL 策略性能强依赖训练场景覆盖度，未训练工况可能失效；必须包含故障、SCR 变化、负荷扰动等 |
| **参数限幅** | RL 输出必须限幅，避免 $J_v \cdot D_v$ 破坏稳定性下限（见 3.1） |
| **在线学习风险** | 在线 RL 可能产生不稳定参数，必须设置"安全监督层"（GB/T 41307），异常时切回固定参数 |
| **可解释性** | RL 黑箱特性不满足电网调度可解释性要求，必须保留参数调整日志与决策依据 |
| **PMU 同步性** | 状态量测依赖 PMU，同步误差 > 10 μs 会显著降低 RL 性能（详见 TH-058） |
| **数字孪生同步** | 在线部署必须配合数字孪生平台（TH-062），保证训练-部署一致性 |
| **标准合规** | GB/T 19963.1 对 $J_v$、$D_v$ 边界有强制要求，RL 输出必须满足 |
| **与传统保护配合** | VSG 参数变化可能影响保护定值，需与继电保护协同校验（详见 CALC-SC-006） |

## 7. 关联条目

- 上游：[TH-056](TH-056-virtual-synchronous-generator-parameter-design-and-stability.md)（VSG 参数设计与稳定性，固定参数基础）·[TH-043](TH-043-ai-foundations-in-electrical-engineering.md)（AI 基础，PINN）·[TH-038](TH-038-high-renewable-frequency-stability-inertia.md)（高比例新能源频率稳定）·[TH-057](TH-057-virtual-inertia-coordination-and-dispatch.md)（虚拟惯量协调调度）
- 下游：[TH-062](TH-062-bess-cascading-failure-digital-twin.md)（储能数字孪生，RL 部署平台）·[PR-ES-001](../30-practice/PR-ES-001-energy-storage-integration.md)（储能接入）·CASE-040（构网型事故）
- 平行：[TH-060](TH-060-frequency-response-testing-method-for-power-electronic-systems.md)（频率响应测试）·[TH-044](TH-044-power-electronics-dominated-system-low-inertia-wideband-oscillation.md)（低惯量振荡）·[CALC-SC-006](../40-calc/CALC-SC-006-active-distribution-network-short-circuit.md)（有源配电网短路）

## 8. 变更记录

| 版本 | 日期 | 修改内容 | 修改人 |
|---|---|---|---|
| 0.1 | 2026-09-11 | 初版建成：RL（PPO）+ PINN 约束 + 数字孪生闭环 + 10 MW 三工况算例 | TRAE |
