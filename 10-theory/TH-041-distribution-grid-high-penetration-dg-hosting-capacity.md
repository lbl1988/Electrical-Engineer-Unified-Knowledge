---
id: TH-041
title: 配电网高渗透率分布式电源承载力机理（静态/动态承载力与电压约束）
domain: 基础理论
subdomain: 电力系统
voltage_levels: [LV, MV]
lifecycle: [规划, 设计, 运维]
standards:
  - { code: GB/T 36121-2018, clause: "全文", note: "配电网分布式电源接入原则（光伏/风电接入容量上限）" }
  - { code: GB/T 19964-2024, clause: "全文", note: "光伏发电站接入电力系统技术规定（替代 2012 版，含 LVRT/HVRT/电能质量）" }
  - { code: GB/T 19963-2019, clause: "全文", note: "风电场接入电力系统技术规定" }
  - { code: GB/T 40567-2021, clause: "全文", note: "分布式能源接入电网承载力评估方法" }
  - { code: GB/T 51048-2025, clause: "有关条款", note: "电化学储能电站设计标准（DG 承载力提升方案）" }
status: draft
reviewers: []
version: 0.1
updated: 2026-09-09
---

# 配电网高渗透率分布式电源承载力机理（静态/动态承载力与电压约束）

## 1. 定义

本条研究**配电网接入 DG（分布式电源）的容量上限**判定机理，包含静态承载力（稳态约束）与动态承载力（暂态约束）两类。

| 承载力类别 | 定义 | 判据 |
|---|---|---|
| **静态承载力** | 稳态运行下不超约束的最大 DG 容量 | 电压偏差、热稳定、短路容量 |
| **动态承载力** | 故障暂态下 DG 能持续并网的最大容量 | LVRT/HVRT、频率穿越、孤岛检测 |
| **反向潮流承载力** | DG 倒送功率不超过变压器/线路容量 | 逆功率整定、调压方向反转 |
| **渗透率** | DG 容量与配变/区域负荷容量之比 | 0~100%+ |

## 2. 物理图像

配电网高渗透率 DG 承载力的核心机理是**潮流方向反转引发电压分布改变**：

```
传统：        ┌── 电源（变电所）── 馈线 ── 负荷
              电压：U_source > U_end（单调下降）

高渗透率 DG： 电源（变电所）── 馈线 ── [DG 注入] ── 负荷
                                      电压：U_end > U_source（末端抬升，方向反转）
```

**关键机理**：配电网阻抗参数 $R/X$ 比高（低压网 $R\approx X$，中压 $R/X \approx 0.3\sim0.5$），DG 注入功率 $P+jQ$ 导致的电压抬升以 $P$ 项为主（不同于输电网 $X\gg R$ 以 $Q$ 为主）。

## 3. 推导

### 3.1 电压灵敏度法承载力

配电网线路压降简化：

$$\Delta U \approx \frac{P R + Q X}{U_N}$$

DG 注入有功 $P_{DG}$ 引起节点电压变化：

$$\frac{\partial U_i}{\partial P_{DG}} = \frac{R_{i-source}}{U_N}$$

各节点静态电压约束承载力（不考虑无功调节）：

$$P_{DG,max}^{U} = \frac{(U_{max} - U_{i,0})\,U_N}{R_{i-source}}$$

| 节点位置 | $R_{i-source}$ (Ω) | $\partial U/\partial P$ (V/kW) | $P_{DG,max}^U$（$\Delta U_{max}=7\%U_N$） |
|---|---|---|---|
| 馈线首端（近变电所） | 0.05 | 0.13 | 5.4 MW（10kV） |
| 馈线中段 | 0.20 | 0.53 | 1.3 MW |
| 馈线末端 | 0.50 | 1.32 | 0.5 MW |

### 3.2 热稳定承载力

DG 倒送工况下，线路/变压器载流量成为约束：

$$S_{DG,max}^{thermal} = \min(S_{line}, S_{trx}) - P_{load,min}$$

### 3.3 短路容量约束承载力

DG 接入改变短路电流分布，影响开关遮断容量：

$$I_{sc}^{DG} = I_{sc}^{grid} + \frac{S_{DG}}{\sqrt3\,U_N\,Z_{DG}}$$

约束：$I_{sc}^{total} \le I_{break}$

| DG 类型 | 短路电流贡献（p.u. 容量） | 备注 |
|---|---|---|
| 旋转电机（同步） | 4~6 倍 | 改变显著 |
| 双馈感应（DFIG） | 1.5~2 倍 | 改变中等 |
| 直驱风电（VSC） | 1.0~1.3 倍 | 改变小 |
| 光伏（VSC） | 1.0~1.1 倍 | 改变微小 |

### 3.4 动态承载力（LVRT 限制）

故障期间 DG 必须按 GB/T 19964-2024 规定的 LVRT 曲线并网：

| 电压跌落 $U/U_N$ | 最低持续并网时间（GB/T 19964-2024） |
|---|---|
| 0 | 0.15 s（150 ms） |
| 0.2 | 0.65 s |
| 0.5 | 1.5 s |
| 0.9 | 5 s（含恢复） |

动态承载力判据：

$$P_{DG,max}^{dynamic} = P_{DG,max}^{static} \cdot k_{LVRT}$$

$k_{LVRT}$ 取决于：故障率、电网支撑能力、DG 类型（VSC 取 0.8~0.95，旋转电机取 0.9~1.0）。

## 4. 与工程实践的联系

### 4.1 支撑条目

- [PR-ES-001 储能接入](../30-practice/PR-ES-001-energy-storage-integration.md)：储能提升 DG 承载力（削峰填谷、LVRT 期间无功支撑）。
- [PR-PQ-001 无功补偿与谐波治理](../30-practice/PR-PQ-001-pq-compensation-design.md)：DG 谐波源叠加校核与 SVG 电压支撑方案。
- [PR-PE-001 继电保护配置](../30-practice/PR-PE-001-relay-protection-config.md)：DG 改变短路电流方向与保护配合（见 TH-030）。
- [PR-DD-002 变电所布置与设备选型](../30-practice/PR-DD-002-substation-layout-and-equipment-selection.md)：馈线选型与升压变容量校核。

### 4.2 失效边界

| 失效场景 | 原因 | 对策 |
|---|---|---|
| **末端电压越限（>7%）** | DG 集中于馈线末端 | 优化接入位置 + 无功调节（光伏零 VAR 或吸收 VAR） |
| **倒送超载** | 周末/节假日负荷低 + DG 高发 | 储能吸收 + 主变有载调压反调 + DG 限功率 |
| **短路容量超标** | 旋转 DG 占比高 | DG 经电力电子接口 + 限流电抗器 + 母线分段 |
| **孤岛检测失效** | 多 DG 协同掩盖孤岛信号 | 主动+被动双重检测 + 集中广域孤岛保护 |
| **动态电压跌落穿越失败** | LVRT 不达标设备并网 | 设备型式试验强制 + GB/T 19964-2024 复核 |

## 5. 关联条目与变更记录

- 关联：[TH-030 分布式电源并网保护与孤岛检测](TH-030-distributed-generation-protection-and-islanding-detection.md)、[TH-029 微电网控制与并离网切换](TH-029-microgrid-control-and-grid-mode-switching.md)、[TH-038 新能源惯量支撑](TH-038-high-renewable-frequency-stability-inertia.md)、[TH-024 电力电子变换器与 PWM](TH-024-power-electronic-converters-and-pwm.md)（VSC 接口短路贡献低）

| 版本 | 日期 | 修改内容 | 修改人 |
|---|---|---|---|
| 0.1 | 2026-09-09 | 创建；含静态/动态承载力推导、电压灵敏度法、LVRT 约束 | KB 管理员 |
