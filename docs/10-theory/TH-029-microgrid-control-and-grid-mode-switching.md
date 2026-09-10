---
id: TH-029
title: 微电网控制与并离网切换
domain: 基础理论
subdomain: 微电网
voltage_levels: [LV, MV]
lifecycle: [设计, 运维]
standards:
  - { code: GB/T 33593-2017, clause: "4", note: "微电网接入电力系统技术规定，含并离网切换与孤岛运行要求" }
  - { code: GB/T 36274-2018, clause: "4", note: "微电网能量管理系统技术规范" }
  - { code: GB/T 36547-2018, clause: "4", note: "电化学储能接入电网技术规定，含构网型 PCS 与微电网应用" }
  - { code: IEC 62898-1:2017, clause: "4", note: "微电网系统规范指南，定义并网/孤岛模式与切换" }
status: draft
reviewers: []
version: 0.1
updated: 2026-09-09
---

# 微电网控制与并离网切换

## 1. 定义

**微电网（Microgrid）**指由分布式电源（光伏、风电、燃气轮机）、储能（电池 PCS）、负荷与监控保护装置组成、可在并网与孤岛两种模式间自主切换、对内自治对外可视作单一可控发用电单元的局部分布式系统。IEC 62898 将其定义为"可独立运行或与主网并联的发用电聚合体"。

| 模式 | 参考源 | 频率/电压调节主体 | 典型场景 |
|---|---|---|---|
| **并网模式** | 主网（电压+频率参考） | 微网内 PCS 跟网型控制（PQ 控制） | 正常态主网稳定 |
| **孤岛模式** | 微网内部参考（构网型 PCS/柴发） | 构网型 VSG（VF 控制） | 主网失电/故障 |
| **切换过渡** | 从主网→内参考（或反向） | 同期控制/无缝切换 | 频率/相位重合时切换 |

## 2. 物理图像

### 2.1 典型微电网拓扑

```
                    PCC（公共连接点）
主网 ──────●──── 并网断路器 ────┬──── 10kV/0.4kV 母线 ──── 负荷
            │                    │
        逆功率/孤岛保护           ├── 光伏 PCS（跟网型）
                                ├── 储能 PCS（构网型，黑启动）
                                ├── 风电 PCS（跟网型）
                                └── 柴发（备黑启动）
```

并网断路器断开即形成孤岛，构网型 PCS 立即转为 VF 控制维持频率/电压。

### 2.2 主从控制 vs 对等控制

| 控制策略 | 参考源 | 优点 | 缺点 |
|---|---|---|---|
| **主从控制（master-slave）** | 单台构网型 PCS 作主 | 结构简单、切换逻辑清晰 | 主机故障全停 |
| **对等控制（droop）** | 多台 VSG 下垂控制 | 无主冗余、可扩展 | 参数设计复杂、环流问题 |
| **分层控制** | 上层 EMS 协调 + 下层 VSG | 兼顾优化与可靠性 | 通信依赖 |

## 3. 推导

### 3.1 并网→孤岛切换判据（GB/T 33593 §4）

主网失电后，孤岛形成条件：① 主网断路器断开；② 微网内有源持续供电。若跟网型 PCS 未切换为构网型，频率/电压因负荷不平衡而漂移，孤岛不可持续。判据：

| 检测方法 | 判据 | 响应时间 |
|---|---|---|
| 电压/频率越限 | $\lvert\Delta U\rvert>10\%$ 或 $\lvert\Delta f\rvert>0.2$ Hz | 100~500 ms |
| 电压相位跳变 | $\lvert\Delta\phi\rvert>\phi_{set}$（典型 10°） | <100 ms |
| 逆功率/低功率 | $P_{PCC} < P_{set}$（判断非计划孤岛） | 100~2000 ms |

非计划孤岛须在 2 s 内识别并切除分布式电源（GB/T 19939 防孤岛要求），但微电网属"计划孤岛"——允许持续运行，但须先确认切换安全（详见 [CASE-054 光伏防孤岛](../50-case/CASE-054-review-pv-anti-islanding-reverse-power.md)）。

### 3.2 下垂控制（Droop）方程

多台构网型 PCS 并联运行（孤岛模式），采用 $P-f$ 与 $Q-V$ 下垂：

$$
f=f_0-k_p(P-P_0),\quad U=U_0-k_q(Q-Q_0)
$$

| 参数 | 典型值 | 含义 |
|---|---|---|
| $k_p$ | 0.5%~2% Hz/p.u. | 有功—频率下垂系数 |
| $k_q$ | 2%~5% V/p.u. | 无功—电压下垂系数 |
| $f_0, U_0$ | 50 Hz, 1.0 p.u. | 空载参考值 |

下垂使多台电源自动分担负荷——$P$ 大者 $f$ 低，$P$ 小者 $f$ 高，自然达到平衡。这是对等控制无主运行的物理基础。

### 3.3 同期并网判据（孤岛→并网）

孤岛转并网须满足同期条件，避免冲击电流：

$$
|\Delta f|<0.1\sim0.2\,\text{Hz},\quad |\Delta U|<10\%,\quad |\Delta\phi|<10^\circ\sim15^\circ
$$

不满足同期时须**主动调频调压**——构网型 PCS 通过调整 $f_0, U_0$ 使微网相位追赶主网。同期合闸冲击电流：

$$
I_{inrush}=\frac{\Delta U}{X_s+X_{grid}}\quad (\Delta U \text{ 由相位差决定})
$$

$\Delta\phi=15^\circ$ 时 $\Delta U\approx 0.26$ p.u.，冲击电流可达额定 2~3 倍——这是同期合闸须严格满足判据的物理原因。

### 3.4 黑启动时序

主网与柴发均失电时，构网型储能 PCS 自带电池可独立建压启动：

```
t=0   主网失电
t=2s  构网型 PCS 检测孤岛 → 切 VF 控制建压（<100ms 稳定）
t=10s 恢复母线电压 → 投入非关键负荷
t=30s 柴发接收启动指令 → 15s 启动 → 同期并网分担负荷
t=60s 投入光伏/风电 → 多源并联运行
```

## 4. 与工程实践的联系

- **支撑条目 1**：[PR-ES-001 储能接入](../30-practice/PR-ES-001-energy-storage-integration.md) 与 [TH-024 电力电子变换器与 PWM](TH-024-power-electronic-converters-and-pwm.md) 与 [TH-020 电力系统稳定性分类](TH-020-power-system-stability-classification.md)——构网型 PCS 是微电网 VF 控制与黑启动的硬件基础。
- **支撑条目 2**：[PR-PS-001 负荷分级](../30-practice/PR-PS-001-load-classification.md)——微电网孤岛容量有限，须按负荷重要性分级投入，特级/一级优先保电。
- **支撑条目 3**：[PR-PE-001 继电保护配置](../30-practice/PR-PE-001-relay-protection-config.md)——微电网并网/孤岛短路电流差异大（并网有主网贡献、孤岛仅 PCS 限流），保护整定须双模式校验。
- **支撑条目 4**：[CASE-043 光储柴微网](../50-case/CASE-043-composite-pv-storage-diesel-microgrid.md) 与 [CASE-054 光伏防孤岛](../50-case/CASE-054-review-pv-anti-islanding-reverse-power.md)——本条给出并离网切换判据与黑启动时序的物理基础。
- **失效边界**：① 下垂控制稳态精度有限（频率存在稳态偏差），对频率敏感负荷需二次调节；② 多台构网型 PCS 并联存在环流（参数不匹配导致无功环流），须均流算法或主从切换；③ 同期合闸判据严格，$\Delta\phi>20^\circ$ 时冲击电流可损坏 PCS，须闭锁合闸；④ 微电网保护整定在孤岛模式（短路电流 1.5~3 倍额定、无直流分量衰减）与并网模式（短路电流 10~20 倍、有衰减）差异巨大，须自适应保护或双套定值；⑤ 微电网容量较小时（<1 MVA）电压质量受负荷波动影响大，须快速储能缓冲。
- **下游案例**：[CASE-043 光储柴微网](../50-case/CASE-043-composite-pv-storage-diesel-microgrid.md)、[CASE-048 新能源汇集站继保](../50-case/CASE-048-composite-renewable-collector-station-protection.md)、[CASE-054 光伏防孤岛](../50-case/CASE-054-review-pv-anti-islanding-reverse-power.md)

## 5. 关联条目与变更记录

- 关联：[TH-024 电力电子变换器与 PWM](TH-024-power-electronic-converters-and-pwm.md)（跟网/构网型 PCS）、[TH-020 电力系统稳定性分类](TH-020-power-system-stability-classification.md)（微电网与主网稳定协调）、[TH-016 功角稳定](TH-016-synchronous-machine-power-angle-stability.md)（VSG 虚拟惯量）、[TH-028 FACTS](TH-028-facts-flexible-ac-transmission.md)（STATCOM 与构网型 PCS 共享 VSG）、[TH-027 HVDC](TH-027-hvdc-transmission-lcc-vsc.md)（VSC 拓扑与 dq 解耦）、[PR-ES-001 储能接入](../30-practice/PR-ES-001-energy-storage-integration.md)、[PR-PS-001 负荷分级](../30-practice/PR-PS-001-load-classification.md)、[PR-PE-001 继电保护配置](../30-practice/PR-PE-001-relay-protection-config.md)
- 下游案例：见 §4 列表。

| 版本 | 日期 | 修改内容 | 修改人 |
|---|---|---|---|
| 0.1 | 2026-09-09 | 创建；含并网/孤岛/切换三模式、下垂控制方程、同期合闸判据、黑启动时序、双模式保护失效边界 | KB 管理员 |
