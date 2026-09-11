## 三期续成果（5 条）

| ID | 主题 | 核心公式/方法 | 主要标准依据 | 下游应用条目 |
|---|---|---|---|---|
| [CALC-SC-003](CALC-SC-003-dc-component-decay-and-breaker-dc-rating.md) | 短路电流直流分量衰减与断路器直流分量耐受 | $I_{dc}(t) = I_{dc,0} e^{-t/T_a}$；$T_a = X_\Sigma / (\omega R_\Sigma)$；直流分量% = $\sin\alpha e^{-t/T_a}/\sqrt{2}$ | GB/T 15544.1-2013, GB 1984-2014, IEC 60909-0 | CALC-SC-002（高压短路）·PR-DD-002（断路器选型）·TH-034（涌流） |
| [CALC-GR-002](CALC-GR-002-ground-fault-current-with-zero-sequence.md | 接地故障电流精确计算（含零序网络） | 单相接地 $I_f = E_a/(Z_1+Z_2+Z_0+3Z_f)$；零序阻抗归算；变压器接地方式影响 | GB/T 15544.1-2013, GB 51348-2019, GB/T 1094.11-2022 | TH-021（中性点接地）·CALC-PT-001（零序保护整定）·CALC-SC-001（低压短路） |
| [CALC-FT-001](CALC-FT-001-arc-ground-overvoltage-and-suppression.md) | 弧光接地过电压计算（IT 系统抑制选型） | 弧光重燃 $k = 3.0\sim3.5$；消弧线圈 $L = 1/(3\omega^2(1+\nu)C_\Sigma)$；小电阻 $R_N = U_{ph}/I_f$ | GB/T 18488.1-2023, GB 50055-2011, CIGRE TB 510 | TH-022（过电压）·TH-021（中性点接地）·PR-PQ-001（无功） |
| [CALC-MS-003](CALC-MS-003-motor-soft-starter-selection.md) | 电动机软启动器选型计算（变频/固态/自耦） | VFD $I_{st} \approx 1.0\sim1.5 I_N$；SSR $I_{st} \approx k I_{DOL}$；自耦 $I_{st} = k^2 I_{DOL}$；$\Delta U\% = S_{st}/S_{sc}$ | GB 50055-2011, GB 755-2019, IEC 60034-12 | TH-007（电机启动）·TH-033（VFD）·CALC-MS-001（启动压降）·PR-DD-002（变压器选型） |
| [CALC-SC-004](CALC-SC-004-transient-emf-iec60909.md) | 高压短路 IEC 60909 暂态电动势计算 | c 系数 $U_f = c \cdot U_n$；发电机 $E_f'' = U_n(1+k_G X_d'' S_b/S_{N,G})$；电动机 $I_{k,M}'' = 3.5 I_{r,M}$；多电源支路代数相加 | GB/T 15544.1-2013, IEC 60909-0:2016, DL/T 5222-2021 | CALC-SC-002（网络法）·PR-DD-002（断路器开断能力） |

## 四期续成果（1 条）

| ID | 主题 | 核心公式/方法 | 主要标准依据 | 下游应用条目 |
|---|---|---|---|---|
| [CALC-SC-005](CALC-SC-005-dc-system-short-circuit.md) | 直流系统短路电流计算（蓄电池/UPS DC 侧/储能 PCS 直流侧） | 稳态 $I_{k,B} = U_{B0}/(R_B + R_L)$；峰值 $i_{p,B} = \kappa_B \cdot I_{k,B}$；$\kappa_B$ 查表（GB/T 22589 §4.2）；多电源代数叠加 | IEC 61660-1:1997, GB/T 22589-2008, DL/T 5044-2014, GB/T 42288-2022, GB/T 14048.2-2020 | PR-PS-003（UPS）·PR-DD-007（数据中心 HVDC）·PR-ES-001（储能）·CASE-052（蓄电池火灾） |

## 五期成果（2 条）

| ID | 主题 | 核心公式/方法 | 主要标准依据 | 下游应用条目 |
|---|---|---|---|---|
| [CALC-SC-006](CALC-SC-006-active-distribution-network-short-circuit.md) | 有源配电网短路电流计算（含 PCS/逆变器短路贡献） | IEC 60909 等效电压源法 + IEEE 1547 修正（PCS 峰值系数 $\kappa_{PCS} = 1.0$）；多源并联叠加；两相短路灵敏度校验 | IEC 60909-0:2016, IEEE 1547-2018, GB/T 19964-2024, GB/T 19963-2019, GB/T 36121-2018, GB/T 40567-2021, GB/T 50065-2011, GB/T 14285-2006 | CALC-PT-001（保护定值）·TH-030（孤岛检测）·PR-ES-001（储能）·PR-ES-003（光伏）·CALC-GR-002（接地） |
| [CALC-HM-002](CALC-HM-002-harmonic-distribution-in-grid.md) | 谐波电流在电网中的分配计算（多母线谐波潮流 + 阻抗分流 + 谐振校验） | 多母线导纳矩阵 $\mathbf{U}_h = \mathbf{Y}_h^{-1} \mathbf{I}_h$；谐振次数 $h_{res} = \sqrt{S_{sc}/Q_{cap}}$；谐波责任分配 $\alpha_i$ | GB/T 14549-1993, IEEE 519-2022, IEC 61000-3-6:2016, GB/T 1094.1-2013, GB/T 12325-2008 | CALC-HM-001（单母线谐波）·TH-008（谐波产生）·PR-PQ-001（无功补偿）·PR-PQ-002（电能质量监测）·PR-EV-001（充电桩） |

**计算层已建成 25 条（含四期续 1 条 + 五期 2 条），完成度 100%。**

剩余可按需扩展方向：

- 防雷接地冲击电阻计算（GDT 选型）
- 变压器励磁涌流与差流计算（整定用）

## 后续规划

计算层已全部建成。如需扩展以上方向，继续告诉我。

