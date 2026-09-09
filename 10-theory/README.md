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

## 第二批条目（2026-09-09 增补，理论层 14→19）

| ID | 主题 | 支撑的工程条目 |
|---|---|---|
| [TH-015](TH-015-synchronous-machine-park-equations.md) | 同步电机暂态深入（Park 方程） | CALC-SC-002（次暂态电势与衰减时间常数）、CASE-022/040/051 |
| [TH-016](TH-016-synchronous-machine-power-angle-stability.md) | 同步电机功角稳定基础 | PR-PE-001（失步保护整定）、CASE-043/048/051 |
| [TH-017](TH-017-cable-wave-process-vfto.md) | 电缆波过程与 VFTO | PR-GR-001（GIS 行波保护）、CASE-016/032/049 |
| [TH-018](TH-018-instantaneous-power-pq-theory.md) | 瞬时功率 p-q 理论（赤木变换） | PR-PQ-001（APF 控制算法）、CALC-HM-001、CASE-005/041 |
| [TH-019](TH-019-transmission-line-parameters-long-line.md) | 输电线路参数与长线方程 | CALC-PT-002（距离整定）、CALC-SC-002、CASE-028/054 |

## 第三批条目（2026-09-09 增补，理论层 19→24）

| ID | 主题 | 支撑的工程条目 |
|---|---|---|
| [TH-020](TH-020-power-system-stability-classification.md) | 电力系统稳定性分类（功角/电压/频率/次同步振荡） | PR-PS-001（低频减载与一级负荷解锁时序）、PR-PE-001（失步/低频低压减载协调）、PR-ES-001（构网型 PCS 与电网稳定） |
| [TH-021](TH-021-neutral-grounding-and-zero-sequence-network.md) | 中性点接地方式与零序网络 | PR-PE-001（接地保护整定与 k0）、PR-GR-002（低压 TN/TT/IT 与一次侧接地协调） |
| [TH-022](TH-022-overvoltage-mechanism-and-insulation-coordination.md) | 过电压机理与绝缘配合 | PR-GR-001（雷电行波与 MOA 保护距离）、PR-DD-002（设备绝缘水平与避雷器配置） |
| [TH-023](TH-023-transformer-parallel-operation-and-circulating-current.md) | 变压器并列运行条件与环流 | PR-DD-002（多台变压器并列与负载分配） |
| [TH-024](TH-024-power-electronic-converters-and-pwm.md) | 电力电子变换器基础拓扑与 PWM | PR-PQ-001（SVG/APF 硬件与 SVPWM）、PR-ES-001（PCS 拓扑与构网/跟网控制） |

## 第四批条目（2026-09-09 增补，理论层 24→29）

| ID | 主题 | 支撑的工程条目 |
|---|---|---|
| [TH-025](TH-025-cable-thermal-field-and-ampacity.md) | 电缆热场与载流量计算基础（IEC 60287 通解/群集校正/暂态 RC） | CALC-CD-001（截面选取与降容）、PR-DD-002（桥架/排管敷设群集） |
| [TH-026](TH-026-switchgear-selection-and-breaking-capacity.md) | 开关电器选型与开断能力物理基础（四额定值/TRV/热稳定） | PR-DD-002（设备选型）、PR-PE-001（继保动作时间与热稳定耦合） |
| [TH-027](TH-027-hvdc-transmission-lcc-vsc.md) | 高压直流输电（LCC/VSC-HVDC，换相失败/dq 解耦） | PR-ES-001（构网型 PCS 与 VSC-MMC）、PR-PQ-001（换相失败扰动） |
| [TH-028](TH-028-facts-flexible-ac-transmission.md) | 柔性交流输电（FACTS：SVC/STATCOM/UPFC） | PR-PQ-001（SVG/STATCOM 无功与暂态稳定）、PR-ES-001（VSG 共享） |
| [TH-029](TH-029-microgrid-control-and-grid-mode-switching.md) | 微电网控制与并离网切换（下垂/同期/黑启动） | PR-ES-001（构网型 PCS 黑启动）、PR-PS-001（孤岛分级保电）、PR-PE-001（双模式保护） |

## 第五批条目（2026-09-09 增补，理论层 29→34，跨过 30 条里程碑）

| ID | 主题 | 支撑的工程条目 |
|---|---|---|
| [TH-030](TH-030-distributed-generation-protection-and-islanding-detection.md) | 分布式电源并网保护与孤岛检测（防孤岛盲区/AFD/LVRT/HVRT/逆功率） | PR-PE-001（DG 接入保护方向改变）、PR-ES-001（PCS 防孤岛与 LVRT） |
| [TH-031](TH-031-grounding-transformer-and-resistor-selection.md) | 接地变压器与接地电阻选型（ZNyn/NGR 阻值与热稳定） | PR-GR-002（接地变与 NGR 选型）、PR-PE-001（零序过流灵敏度）、PR-DD-002（布置空间） |
| [TH-032](TH-032-synchronous-machine-leading-and-condensing-operation.md) | 同步电机进相与调相运行（V 曲线/进相稳定/端部温升/调相机容量） | PR-PQ-001（调相机作为旋转 STATCOM）、PR-ES-001（调相机替代方案） |
| [TH-033](TH-033-induction-motor-vfd-control-strategy.md) | 异步电机变频调速控制策略（V/f/FOC/DTC/节能估算） | PR-PQ-001（变频器谐波源与滤波器选型） |
| [TH-034](TH-034-transformer-inrush-current-and-differential-protection.md) | 变压器励磁涌流机理与差动保护防涌流（暂态磁通/二次谐波制动/和应涌流） | PR-PE-001（差动防涌流判据） |

## 后续规划（四期）

理论层 34 条已覆盖电磁/电路/电机/系统/电力电子/接地/保护/直流输电/柔性输电/微电网/分布式电源全主干。后续按需扩展：高压断路器选型深入、电力系统次同步谐振（SSR/SSCI）机理、发电机励磁系统建模与 AVR/PSS、变压器有载调压与动态无功协调、新能源高占比系统频率稳定与惯量支撑。
