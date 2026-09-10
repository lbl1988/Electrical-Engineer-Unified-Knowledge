---
id: TH-043
title: 人工智能在电气工程应用基础（机器学习/深度学习/物理信息神经网络 PINN）
domain: 基础理论
subdomain: 人工智能
voltage_levels: [LV, MV, HV, EHV]
lifecycle: [规划, 设计, 运维]
standards:
  - { code: GB/T 42018-2022, clause: "全文", note: "人工智能 服务能力成熟度评估参考框架" }
  - { code: GB/T 41773-2022, clause: "全文", note: "人工智能 面向机器学习的系统架构规范" }
  - { code: GB/T 41307-2022, clause: "全文", note: "人工智能 可信赖评估规范（含安全性/鲁棒性）" }
  - { code: DL/T 2547-2022, clause: "全文", note: "人工智能 电力应用技术规范（电力行业 AI 应用导则）" }
  - { code: IEC 62332:2024, clause: "全文", note: "AI in power systems - trustworthiness and governance（草案阶段）" }
status: draft
reviewers: []
version: 0.1
updated: 2026-09-09
---

# 人工智能在电气工程应用基础（机器学习/深度学习/物理信息神经网络 PINN）

## 1. 定义

本条研究**人工智能在电气工程中应用的数学原理与失效边界**，聚焦机器学习（ML）、深度学习（DL）、物理信息神经网络（PINN）与电力数字孪生。

| AI 类别 | 定义 | 电气工程映射 |
|---|---|---|
| **监督学习** | 从标注数据学习映射 $f:X\to Y$ | 故障诊断、负荷预测、设备状态评估 |
| **强化学习（RL）** | 序列决策优化回报 | 电网调度、拓扑优化、储能策略 |
| **物理信息神经网络（PINN）** | 在损失函数中嵌入物理方程约束 | 潮流求解、暂态稳定评估、参数辨识 |
| **数字孪生** | 物理实体映射的实时数字模型 | 设备状态预测、运维决策 |

## 2. 物理图像

AI 在电气工程中的"数据-模型-物理"三层耦合：

```
┌─────────────────────────────────────────────┐
│  物理层（真实电网）                          │
│  潮流方程/微分方程/电磁方程                   │
└─────────┬───────────────┬───────────────────┘
          │ 观测数据       │ 物理约束
          ↓               ↑
┌─────────────────┐   ┌─────────────────────────┐
│  数据驱动层     │   │  物理信息层             │
│  监督/RL 学习   │←──│  PINN: L = L_data + λ L_phys │
└─────────┬───────┘   └─────────────────────────┘
          │
          ↓
┌─────────────────┐
│  决策层          │
│  调度/控制/诊断  │
└─────────────────┘
```

**核心机理**：纯数据驱动模型在罕见工况下泛化失效，PINN 通过将物理方程作为软约束嵌入损失函数，保证预测满足基本物理规律。

## 3. 推导

### 3.1 监督学习（负荷预测为例）

神经网络拟合负荷映射：

$$\hat{P}(t+1) = f_\theta\big(P(t), T(t), \text{day\_type}, \dots\big)$$

损失函数：

$$\mathcal{L}(\theta) = \frac{1}{N}\sum_i \big(P_i - \hat{P}_i\big)^2 + \lambda\|\theta\|^2$$

| 算法 | 输入 | 输出 | 误差（MAPE） | 失效场景 |
|---|---|---|---|---|
| ARIMA | 历史 P | P(t+1) | 3~5% | 节假日/极端天气 |
| LSTM | P+T+日类型 | P(t+1~24h) | 1.5~3% | 罕见节日（无训练样本） |
| Transformer | 多变量长序列 | P(t+1~168h) | 1~2% | 长期分布漂移 |
| PINN-LSTM | 上述+潮流约束 | P(t+1~24h) | 1.5~2.5% | 约束松弛/边界误设 |

### 3.2 强化学习（电网调度为例）

马尔可夫决策过程（MDP）：

- 状态 $s_t$：当前负荷/发电/拓扑/电价
- 动作 $a_t$：机组启停/储能充放/线路投切
- 回报 $r_t$：$-\text{Cost}_{gen}-\text{Cost}_{carbon}-\text{Penalty}_{violation}$
- 转移 $P(s_{t+1}|s_t,a_t)$：电网物理转移概率

目标：

$$\max_\pi\, \mathbb{E}_\pi \left[\sum_t \gamma^t r_t\right]$$

| 算法 | 决策周期 | 适用规模 | 失效边界 |
|---|---|---|---|
| Q-learning | 秒级 | 小系统（<50 节点） | 维数灾难 |
| DDPG/SAC | 秒级 | 中系统（<500 节点） | 安全约束不可硬保证 |
| MARL（多智能体） | 分钟级 | 大系统（解耦分区） | 协调失效/非收敛 |
| 安全 RL（含约束） | 分钟级 | 中-大系统 | 计算复杂度高 |

### 3.3 物理信息神经网络（PINN）

PINN 求解偏微分方程（以潮流方程为例）：

$$F(x, u, \nabla u, \nabla^2 u, \dots) = 0$$

网络输出 $u_\theta(x)$，损失函数：

$$\mathcal{L}(\theta) = \underbrace{\frac{1}{N_d}\sum_i |u_\theta(x_i)-u_i^{data}|^2}_{\text{数据残差}} + \lambda\underbrace{\frac{1}{N_r}\sum_j |F(x_j, u_\theta, \nabla u_\theta)|^2}_{\text{物理残差}}$$

对潮流方程（极坐标）：

$$F = P_i - V_i\sum_j V_j(G_{ij}\cos\theta_{ij}+B_{ij}\sin\theta_{ij})$$

$$\mathcal{L}_{PF} = \frac{1}{N}\sum_i \big|\Delta P_i\big|^2 + \big|\Delta Q_i\big|^2$$

| 应用 | 物理方程 | 优势 | 失效边界 |
|---|---|---|---|
| 潮流求解 | 功率平衡方程 | 无雅可比矩阵奇异问题 | 不收敛于病态系统 |
| 暂态稳定 | 同步机摇摆方程 | 端到端参数辨识 | 故障冲击下泛化弱 |
| 电磁暂态 | Maxwell 方程 | 高频场求解 | 计算量极大 |
| 设备寿命 | Arrhenius/热模型 | 融合监测数据+物理 | 老化机理未建模 |

### 3.4 数字孪生

数字孪生 = 物理模型 + 实时数据 + AI 预测 + 决策反馈：

$$\text{DT}(t) = \underbrace{M_{physics}}_{\text{机理模型}} + \underbrace{\hat M_{AI}(\text{sensor data})}_{\text{AI 状态估计}} + \underbrace{\Delta u(t)}_{\text{决策反馈}}$$

| 数字孪生类别 | 物理模型 | 数据频率 | 决策延迟 |
|---|---|---|---|
| 变压器 DGA 孪生 | 热-氢气生成模型 | 1 h | 1 day |
| 输电线路动态增容 | 热平衡方程 | 1 min | 5 min |
| 储能电池 SOH | 电化学-热模型 | 1 s | 1 h |
| 系统级调度孪生 | 潮流/暂态稳定 | 4 s（PMU） | 15 min |

## 4. 与工程实践的联系

### 4.1 支撑条目

- [PR-ES-001 储能接入](../30-practice/PR-ES-001-energy-storage-integration.md)：储能 SOH 估计与策略优化（RL+PINN）。
- [PR-PQ-001 无功补偿与谐波治理](../30-practice/PR-PQ-001-pq-compensation-design.md)：负荷预测与 SVG/APF 自适应控制。
- [PR-PE-001 继电保护配置](../30-practice/PR-PE-001-relay-protection-config.md)：故障智能诊断与保护自适应整定。
- [PR-PS-001 负荷分级](../30-practice/PR-PS-001-load-classification.md)：负荷预测精度与分级保电策略。
- [PR-CM-001 消防联动](../30-practice/PR-CM-001-fire-protection-interlocking.md)：电池热失控早期预警（PINN+Arrhenius）。

### 4.2 失效边界

| 失效场景 | 原因 | 对策 |
|---|---|---|
| **数据驱动模型泛化失效** | 训练集覆盖不全（罕见工况） | PINN 嵌入物理 + 主动学习补样本 |
| **黑盒模型不可解释** | 深度网络决策不透明 | 可解释 AI（SHAP/LIME）+ 决策树代理 |
| **对抗样本攻击** | 输入扰动致误分类 | 对抗训练 + 输入校验 + 物理一致性检查 |
| **RL 安全约束违反** | 探索阶段违规动作 | 安全 RL + 屏障函数 + 人在回路 |
| **数字孪生同步漂移** | 物理实体老化/改造未同步 | 定期参数辨识 + 模型版本管理 |
| **AI 误诊致保护误动** | 训练样本不平衡 | 保护层级冗余（AI 辅助 + 传统主后备） |

## 5. 关联条目与变更记录

- 关联：[TH-015 Park 方程](TH-015-synchronous-machine-park-equations.md)（PINN 暂态参数辨识）、[TH-035 SSR/SSCI](TH-035-sub-synchronous-resonance-ssr-ssci.md)（AI 辅助振荡模式识别）、[TH-038 新能源惯量支撑](TH-038-high-renewable-frequency-stability-inertia.md)（RL 调频策略）、[TH-042 电力市场与碳交易](TH-042-electricity-market-and-carbon-trading-engineering-mapping.md)（RL 调度+碳成本）

| 版本 | 日期 | 修改内容 | 修改人 |
|---|---|---|---|
| 0.1 | 2026-09-09 | 创建；含监督/RL/PINN/数字孪生四类 AI 基础机理 | KB 管理员 |
