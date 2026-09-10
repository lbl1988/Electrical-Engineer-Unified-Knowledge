# L1 基础理论层（10-theory）

> 定位：支撑 L3 工程实践的物理与数学基础，采用 [五段式模板](../00-meta/04-模板-理论类五段式.md)（定义→物理图像→推导→与工程实践的联系（含失效边界）→关联与变更）。**每条理论条目显式标注失效边界与工程速记**。

## 首批条目（2026-09-08 建成）

| ID                                                             | 主题                      | 支撑的工程条目                                             |
| -------------------------------------------------------------- | ----------------------- | --------------------------------------------------- |
| [TH-001](TH-001-quasi-static-approximation.md)                 | 似稳场与集总参数电路近似            | 全部计算条目的前提                                           |
| [TH-002](TH-002-phasor-analysis.md)                            | 相量法与正弦稳态                | SC/LD/RC 系列                                         |
| [TH-003](TH-003-symmetrical-components.md)                     | 对称分量法                   | CALC-PT-001（两相灵敏度）                                  |
| [TH-004](TH-004-current-effects-human-body.md)                 | 人体电流效应与时间分区             | 电击防护、RCD 30mA 溯源                                    |
| [TH-005](TH-005-touch-step-voltage.md)                         | 接地故障地表电位分布              | 变电站接地设计                                             |
| [TH-006](TH-006-transformer-leakage-impedance.md)              | 变压器短路阻抗物理来源             | CALC-SC-001（ZT 公式）                                  |
| [TH-007](TH-007-induction-motor-starting.md)                   | 感应电机启动机理                | 尖峰电流/启动压降                                           |
| [TH-008](TH-008-harmonic-generation.md)                        | 谐波产生机理与特征谐波             | CALC-RC-001（电抗率）                                    |
| [TH-009](TH-009-lightning-physics.md)                          | 雷电放电物理与参数               | PR-GR-001（滚球法）                                      |
| [TH-010](TH-010-reactive-power.md)                             | 无功功率物理意义                | CALC-RC-001（QC 公式）                                  |
| [TH-011](TH-011-synchronous-machine-subtransient-reactance.md) | 同步电机暂态与次暂态电抗            | CALC-SC-002（高压短路 I\_k″）、电动机反馈电流                     |
| [TH-012](TH-012-protection-four-properties.md)                 | 继电保护四性（可靠性/选择性/灵敏性/速动性） | PR-PE-001（继电保护整定配合）、CALC-PT-001（低压保护四段式）            |
| [TH-013](TH-013-switching-arc-physics.md)                      | 开关电弧物理与交流电流零点熄弧         | CALC-SC-002（高压短路开断容量校验）、PR-PE-001（断路器开断能力）          |
| [TH-014](TH-014-magnetic-circuit-saturation.md)                | 磁路与铁磁饱和                 | TH-006（变压器漏抗）、CALC-SC-001（$X\_m\gg X\_\sigma$ 忽略条件） |

## 第二批条目（2026-09-09 增补，理论层 14→19）

| ID                                                            | 主题                | 支撑的工程条目                                      |
| ------------------------------------------------------------- | ----------------- | -------------------------------------------- |
| [TH-015](TH-015-synchronous-machine-park-equations.md)        | 同步电机暂态深入（Park 方程） | CALC-SC-002（次暂态电势与衰减时间常数）、CASE-022/040/051   |
| [TH-016](TH-016-synchronous-machine-power-angle-stability.md) | 同步电机功角稳定基础        | PR-PE-001（失步保护整定）、CASE-043/048/051           |
| [TH-017](TH-017-cable-wave-process-vfto.md)                   | 电缆波过程与 VFTO       | PR-GR-001（GIS 行波保护）、CASE-016/032/049         |
| [TH-018](TH-018-instantaneous-power-pq-theory.md)             | 瞬时功率 p-q 理论（赤木变换） | PR-PQ-001（APF 控制算法）、CALC-HM-001、CASE-005/041 |
| [TH-019](TH-019-transmission-line-parameters-long-line.md)    | 输电线路参数与长线方程       | CALC-PT-002（距离整定）、CALC-SC-002、CASE-028/054   |

## 第三批条目（2026-09-09 增补，理论层 19→24）

| ID                                                                         | 主题                        | 支撑的工程条目                                                                  |
| -------------------------------------------------------------------------- | ------------------------- | ------------------------------------------------------------------------ |
| [TH-020](TH-020-power-system-stability-classification.md)                  | 电力系统稳定性分类（功角/电压/频率/次同步振荡） | PR-PS-001（低频减载与一级负荷解锁时序）、PR-PE-001（失步/低频低压减载协调）、PR-ES-001（构网型 PCS 与电网稳定） |
| [TH-021](TH-021-neutral-grounding-and-zero-sequence-network.md)            | 中性点接地方式与零序网络              | PR-PE-001（接地保护整定与 k0）、PR-GR-002（低压 TN/TT/IT 与一次侧接地协调）                    |
| [TH-022](TH-022-overvoltage-mechanism-and-insulation-coordination.md)      | 过电压机理与绝缘配合                | PR-GR-001（雷电行波与 MOA 保护距离）、PR-DD-002（设备绝缘水平与避雷器配置）                        |
| [TH-023](TH-023-transformer-parallel-operation-and-circulating-current.md) | 变压器并列运行条件与环流              | PR-DD-002（多台变压器并列与负载分配）                                                  |
| [TH-024](TH-024-power-electronic-converters-and-pwm.md)                    | 电力电子变换器基础拓扑与 PWM          | PR-PQ-001（SVG/APF 硬件与 SVPWM）、PR-ES-001（PCS 拓扑与构网/跟网控制）                   |

## 第四批条目（2026-09-09 增补，理论层 24→29）

| ID                                                             | 主题                                    | 支撑的工程条目                                                   |
| -------------------------------------------------------------- | ------------------------------------- | --------------------------------------------------------- |
| [TH-025](TH-025-cable-thermal-field-and-ampacity.md)           | 电缆热场与载流量计算基础（IEC 60287 通解/群集校正/暂态 RC） | CALC-CD-001（截面选取与降容）、PR-DD-002（桥架/排管敷设群集）                 |
| [TH-026](TH-026-switchgear-selection-and-breaking-capacity.md) | 开关电器选型与开断能力物理基础（四额定值/TRV/热稳定）         | PR-DD-002（设备选型）、PR-PE-001（继保动作时间与热稳定耦合）                   |
| [TH-027](TH-027-hvdc-transmission-lcc-vsc.md)                  | 高压直流输电（LCC/VSC-HVDC，换相失败/dq 解耦）       | PR-ES-001（构网型 PCS 与 VSC-MMC）、PR-PQ-001（换相失败扰动）            |
| [TH-028](TH-028-facts-flexible-ac-transmission.md)             | 柔性交流输电（FACTS：SVC/STATCOM/UPFC）        | PR-PQ-001（SVG/STATCOM 无功与暂态稳定）、PR-ES-001（VSG 共享）          |
| [TH-029](TH-029-microgrid-control-and-grid-mode-switching.md)  | 微电网控制与并离网切换（下垂/同期/黑启动）                | PR-ES-001（构网型 PCS 黑启动）、PR-PS-001（孤岛分级保电）、PR-PE-001（双模式保护） |

## 第五批条目（2026-09-09 增补，理论层 29→34，跨过 30 条里程碑）

| ID                                                                            | 主题                                      | 支撑的工程条目                                                   |
| ----------------------------------------------------------------------------- | --------------------------------------- | --------------------------------------------------------- |
| [TH-030](TH-030-distributed-generation-protection-and-islanding-detection.md) | 分布式电源并网保护与孤岛检测（防孤岛盲区/AFD/LVRT/HVRT/逆功率） | PR-PE-001（DG 接入保护方向改变）、PR-ES-001（PCS 防孤岛与 LVRT）           |
| [TH-031](TH-031-grounding-transformer-and-resistor-selection.md)              | 接地变压器与接地电阻选型（ZNyn/NGR 阻值与热稳定）           | PR-GR-002（接地变与 NGR 选型）、PR-PE-001（零序过流灵敏度）、PR-DD-002（布置空间） |
| [TH-032](TH-032-synchronous-machine-leading-and-condensing-operation.md)      | 同步电机进相与调相运行（V 曲线/进相稳定/端部温升/调相机容量）       | PR-PQ-001（调相机作为旋转 STATCOM）、PR-ES-001（调相机替代方案）             |
| [TH-033](TH-033-induction-motor-vfd-control-strategy.md)                      | 异步电机变频调速控制策略（V/f/FOC/DTC/节能估算）          | PR-PQ-001（变频器谐波源与滤波器选型）                                   |
| [TH-034](TH-034-transformer-inrush-current-and-differential-protection.md)    | 变压器励磁涌流机理与差动保护防涌流（暂态磁通/二次谐波制动/和应涌流）     | PR-PE-001（差动防涌流判据）                                        |

## 第六批条目（2026-09-09 增补，理论层 34→39，系统级深化主题）

| ID                                                                | 主题                                                         | 支撑的工程条目                                      |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | -------------------------------------------- |
| [TH-035](TH-035-sub-synchronous-resonance-ssr-ssci.md)            | 电力系统次同步谐振 SSR/SSCI 机理（串联补偿电气谐振/互补频率耦合/TCSC 抑制/SSDC）        | PR-PE-001（机组扭振保护与 SSR 阻尼判据）                  |
| [TH-036](TH-036-excitation-system-avr-pss.md)                     | 发电机励磁系统建模与 AVR/PSS（IEEE 模型/负阻尼机理/超前-滞后补偿/Heffron-Phillips） | PR-PE-001（低励磁限制/过励磁保护/失磁保护整定）                |
| [TH-037](TH-037-tap-changer-and-dynamic-reactive-coordination.md) | 变压器有载调压与动态无功协调（OLTC 灵敏度/9 区图/时间尺度解耦/动作次数限制）                | PR-PQ-001（无功补偿与 OLTC 协调）、PR-DD-002（主变调压方式选型） |
| [TH-038](TH-038-high-renewable-frequency-stability-inertia.md)    | 新能源高占比系统频率稳定与惯量支撑（等效惯量/RoCoF/VSG 虚拟惯量/频率最低点估算）             | PR-ES-001（储能 VSG 调频与 RoCoF 保护）               |
| [TH-039](TH-039-generator-breaker-and-gis-selection.md)           | 高压断路器选型深入（发电机断路器 GCB 直流分量/TRV/GIS 绝缘配合与扩建约束）               | PR-PE-001（GCB 保护配合）、PR-DD-002（GIS 间隔布置与扩建预留） |

## 第七批条目（2026-09-09 增补，理论层 39→44，四期方向扩展）

| ID | 主题 | 支撑的工程条目 |
|---|---|---|
| [TH-040](TH-040-hybrid-ac-dc-grid-stability.md) | 交直流混联电网稳定（多馈入短路比 MISCR/换相失败连锁/LCC-VSC 互补） | PR-ES-001（VSC 与构网型 PCS 共享控制）、PR-PQ-001（MIDC 受端动态无功）、PR-PE-001（直流闭锁潮流转移）、PR-DD-002（STATCOM 选型） |
| [TH-041](TH-041-distribution-grid-high-penetration-dg-hosting-capacity.md) | 配电网高渗透率 DG 承载力（静态/动态承载力/电压灵敏度法/LVRT 约束） | PR-ES-001（储能提升承载力）、PR-PQ-001（DG 谐波叠加）、PR-PE-001（DG 短路方向）、PR-DD-002（馈线选型） |
| [TH-042](TH-042-electricity-market-and-carbon-trading-engineering-mapping.md) | 电力市场与碳交易工程映射（LMP/辅助服务/CCER/储能套利） | PR-ES-001（储能经济性）、PR-PS-001（需求响应）、PR-PQ-001（无功辅服）、PR-EV-001（V2G 套利） |
| [TH-043](TH-043-ai-foundations-in-electrical-engineering.md) | 人工智能在电气工程应用基础（监督学习/RL/PINN/数字孪生） | PR-ES-001（储能 SOH）、PR-PQ-001（负荷预测）、PR-PE-001（故障诊断）、PR-PS-001（负荷预测）、PR-CM-001（热失控预警） |
| [TH-044](TH-044-power-electronics-dominated-system-low-inertia-wideband-oscillation.md) | 电力电子化电力系统低惯量与宽频振荡（PLL 耦合/阻抗分析/CIO） | PR-ES-001（构网型 vs 跟网型）、PR-PE-001（短路特征变化）、PR-PQ-001（宽频阻抗谐振）、PR-DD-002（滤波器配置） |

## 第八批条目（2026-09-10 增补，理论层 44→48，五期方向首批）

| ID | 主题 | 支撑的工程条目 |
|---|---|---|
| [TH-045](TH-045-power-system-dynamic-equivalence-and-model-reduction.md) | 电力系统动态等值与降阶方法（电网等值/机组聚合/模态降阶/时变等值） | PR-PE-002（继保整定深化）、PR-DD-004（配网 SCADA）、PR-DD-005（综自系统）、CALC-SC-002（高压短路） |
| [TH-046](TH-046-battery-thermal-runaway-mechanism-and-early-warning.md) | 锂离子电池热失控机理与预警（SEI 分解/产气/热蔓延/BMS 多判据预警） | PR-ES-001（储能接入）、PR-CM-001（消防联动）、TH-038（频率稳定/储能脱网影响） |
| [TH-047](TH-047-xlpe-cable-water-tree-aging-and-insulation-diagnosis.md) | 中高压 XLPE 电缆水树老化机理与绝缘诊断（介损/TDR/PD/UHF） | PR-DD-003（电缆敷设）、TH-017（VFTO 加速水树转变）、CALC-SC-001（短路校验） |
| [TH-048](TH-048-power-system-restoration-and-black-start-optimization.md) | 电力系统恢复控制与黑启动优化（BSR/恢复路径/过电压抑制/构网型黑启动） | PR-PS-001（负荷分级）、PR-DD-004（配网 SCADA）、TH-029（微电网并离网）、TH-041（DG 承载力） |

## 第九批条目（2026-09-10 增补，理论层 48→52，五期方向第二批）

| ID | 主题 | 支撑的工程条目 |
|---|---|---|
| [TH-049](TH-049-renewable-energy-forecasting-and-uncertainty-modeling.md) | 可再生能源出力预测与不确定性建模（概率预测/场景生成/鲁棒优化） | TH-038（频率稳定）、TH-041（DG 承载力）、TH-042（电力市场）、TH-043（AI 辅助）、PR-ES-001（储能容量配置） |
| [TH-050](TH-050-transformer-capacitive-bushing-failure-and-diagnosis.md) | 变压器电容式套管故障物理与绝缘诊断（电容屏短路/DGA/PD/介损监测） | TH-017（VFTO 加速劣化）、TH-022（过电压/绝缘配合）、TH-043（AI 故障诊断） |
| [TH-051](TH-051-power-electronics-wideband-impedance-modeling.md) | 电力电子化设备宽频阻抗建模（dq 阻抗/序阻抗/阻抗稳定判据/有源阻尼） | TH-027（HVDC）、TH-028（STATCOM）、TH-040（交直流混联）、TH-044（宽频振荡）、PR-PQ-001（SVG 设计） |
| [TH-052](TH-052-mtdc-fault-ride-through-and-recovery.md) | 柔性直流多端 MTDC 故障穿越与恢复（MMC 子模块旁路/DCCB/限流电抗器） | TH-027（VSC-HVDC）、TH-040（交直流混联）、TH-048（黑启动）、PR-DD-002（设备选型） |

## 第十批条目（2026-09-10 增补，理论层 52→56，五期方向第三批）

| ID | 主题 | 支撑的工程条目 |
|---|---|---|
| [TH-053](TH-053-transformer-dc-magnetization-and-residual-flux.md) | 变压器铁芯直流偏磁与剩磁机理（HVDC/GIC/逆变器谐波/空投涌流） | TH-006（变压器漏抗）、TH-034（差动防涌流）、TH-027（HVDC 单极偏磁） |
| [TH-054](TH-054-sf6-decomposition-products-and-eco-friendly-substitutes.md) | SF₆ 分解产物诊断与环保替代（PD/过热/电弧分解/C₄F₇N 替代） | TH-013（开关电弧）、TH-026（高压开关选型）、PR-DD-002（GIS 选型） |
| [TH-055](TH-055-cascading-failure-and-thermal-propagation.md) | 储能系统级联故障与热蔓延动力学（电芯→模组→簇→舱级热/电气/气体传播） | TH-046（单体热失控）、TH-038（储能脱网频率影响）、PR-ES-001（储能热管理）、PR-CM-001（消防联动） |
| [TH-056](TH-056-virtual-synchronous-generator-parameter-design-and-stability.md) | 虚拟同步机（VSG）参数设计与稳定性（惯量/阻尼/下垂系数/自适应整定） | TH-024（PWM）、TH-029（微电网并离网）、TH-038（频率稳定）、TH-048（黑启动）、PR-ES-001（构网型 PCS） |

## 第十一批条目（2026-09-10 增补，理论层 56→60，五期方向第四批）

| ID | 主题 | 支撑的工程条目 |
|---|---|---|
| [TH-057](TH-057-virtual-inertia-coordination-and-dispatch.md) | 虚拟惯量协调控制与惯量调度（多场站共享/集群振荡抑制） | TH-038（频率稳定）、TH-056（VSG 设计）、PR-DD-004（SCADA/惯量调度） |
| [TH-058](TH-058-frequency-response-detailed-modeling-primary-secondary-AGC.md) | 频率响应精细化建模（一次调频/二次调频/AGC 协调） | TH-011（同步机 H）、TH-038（频率稳定）、TH-056（VSG）、DL/T 1055 标准 |
| [TH-059](TH-059-active-distribution-network-fault-location-and-isolation.md) | 主动配电网故障定位与隔离（DG 双向短路/行波定位/多源融合） | TH-003（对称分量）、TH-012（保护四性）、TH-017（行波物理）、TH-030（DG 孤岛）、PR-DD-004（配网自动化） |
| [TH-060](TH-060-frequency-response-testing-method-for-power-electronic-systems.md) | 电力电子化系统频率响应测试（RoCoF 注入/虚拟惯量实测/对比指标） | TH-056（VSG 参数）、TH-057（惯量调度）、TH-058（频率响应）、GB/T 40595 |

**理论层已建成 60 条，完成度 100%。**

剩余可按需扩展方向（不再标"后续规划"，作为备选）：

- 新能源场站惯量容量市场机制设计
- 直流偏磁的在线监测算法（FFT + 小波分解）
- SF₆ 替代气体局部放电特性
- 储能系统级联故障的数字孪生建模
- VSG 参数的 AI 自适应整定（强化学习）
- 主动配电网孤岛运行的频率/电压控制
- 高压直流 MTDC 换相失败连锁抑制策略
