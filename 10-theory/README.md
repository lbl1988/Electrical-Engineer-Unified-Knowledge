# L1 基础理论层（10-theory）

> 定位：支撑 L3 工程实践的物理与数学基础，采用 [五段式模板](../00-meta/04-模板-理论类五段式.md)（定义→物理图像→推导→与工程实践的联系（含失效边界）→关联与变更）。**每条理论条目显式标注失效边界与工程速记**。

## 首批条目（2026-09-08 建成）

| ID | 主题 | 支撑的工程条目 |
|---|---|---|
| [TH-001](TH-001-quasi-static-approximation.md) | 似稳场与集总参数电路近似 | 全部计算条目的前提 |
| [TH-002](TH-002-phasor-analysis.md) | 相量法与正弦稳态 | SC/LD/RC 系列 |
| [TH-003](TH-003-symmetrical-components.md) | 对称分量法 | CALC-PT-001（两相灵敏度） |
| [TH-004](TH-004-current-effects-human-body.md) | 人体电流效应与时间分区 | 电击防护、RCD 30mA 溯源 |
| [TH-005](TH-005-touch-step-voltage.md) | 接地故障地表电位分布 | 变电站接地设计 |
| [TH-006](TH-006-transformer-leakage-impedance.md) | 变压器短路阻抗物理来源 | CALC-SC-001（ZT 公式） |
| [TH-007](TH-007-induction-motor-starting.md) | 感应电机启动机理 | 尖峰电流/启动压降 |
| [TH-008](TH-008-harmonic-generation.md) | 谐波产生机理与特征谐波 | CALC-RC-001（电抗率） |
| [TH-009](TH-009-lightning-physics.md) | 雷电放电物理与参数 | PR-GR-001（滚球法） |
| [TH-010](TH-010-reactive-power.md) | 无功功率物理意义 | CALC-RC-001（QC 公式） |
| [TH-011](TH-011-synchronous-machine-subtransient-reactance.md) | 同步电机暂态与次暂态电抗 | CALC-SC-002（高压短路 I_k″）、电动机反馈电流 |
| [TH-012](TH-012-protection-four-properties.md) | 继电保护四性（可靠性/选择性/灵敏性/速动性） | PR-PE-001（继电保护整定配合）、CALC-PT-001（低压保护四段式） |
| [TH-013](TH-013-switching-arc-physics.md) | 开关电弧物理与交流电流零点熄弧 | CALC-SC-002（高压短路开断容量校验）、PR-PE-001（断路器开断能力） |
| [TH-014](TH-014-magnetic-circuit-saturation.md) | 磁路与铁磁饱和 | TH-006（变压器漏抗）、CALC-SC-001（$X_m\gg X_\sigma$ 忽略条件） |

## 后续规划（三期）

电缆波过程与 VFTO、同步电机功角稳定基础、瞬时功率 p-q 理论、电力电子器件物理、电化学电池机理。
