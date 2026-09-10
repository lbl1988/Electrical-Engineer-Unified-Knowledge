## 三期续成果（5 条）

| ID | 主题 | 核心公式/方法 | 主要标准依据 | 下游应用条目 |
|---|---|---|---|---|
| [CALC-SC-003](CALC-SC-003-dc-component-decay-and-breaker-dc-rating.md) | 短路电流直流分量衰减与断路器直流分量耐受 | $I_{dc}(t) = I_{dc,0} e^{-t/T_a}$；$T_a = X_\Sigma / (\omega R_\Sigma)$；直流分量% = $\sin\alpha e^{-t/T_a}/\sqrt{2}$ | GB/T 15544.1-2013, GB 1984-2014, IEC 60909-0 | CALC-SC-002（高压短路）·PR-DD-002（断路器选型）·TH-034（涌流） |
| [CALC-GR-002](CALC-GR-002-ground-fault-current-with-zero-sequence.md | 接地故障电流精确计算（含零序网络） | 单相接地 $I_f = E_a/(Z_1+Z_2+Z_0+3Z_f)$；零序阻抗归算；变压器接地方式影响 | GB/T 15544.1-2013, GB 51348-2019, GB/T 1094.11-2022 | TH-021（中性点接地）·CALC-PT-001（零序保护整定）·CALC-SC-001（低压短路） |
| [CALC-FT-001](CALC-FT-001-arc-ground-overvoltage-and-suppression.md) | 弧光接地过电压计算（IT 系统抑制选型） | 弧光重燃 $k = 3.0\sim3.5$；消弧线圈 $L = 1/(3\omega^2(1+\nu)C_\Sigma)$；小电阻 $R_N = U_{ph}/I_f$ | GB/T 18488.1-2023, GB 50055-2011, CIGRE TB 510 | TH-022（过电压）·TH-021（中性点接地）·PR-PQ-001（无功） |
| [CALC-MS-003](CALC-MS-003-motor-soft-starter-selection.md) | 电动机软启动器选型计算（变频/固态/自耦） | VFD $I_{st} \approx 1.0\sim1.5 I_N$；SSR $I_{st} \approx k I_{DOL}$；自耦 $I_{st} = k^2 I_{DOL}$；$\Delta U\% = S_{st}/S_{sc}$ | GB 50055-2011, GB 755-2019, IEC 60034-12 | TH-007（电机启动）·TH-033（VFD）·CALC-MS-001（启动压降）·PR-DD-002（变压器选型） |
| [CALC-SC-004](CALC-SC-004-transient-emf-iec60909.md) | 高压短路 IEC 60909 暂态电动势计算 | c 系数 $U_f = c \cdot U_n$；发电机 $E_f'' = U_n(1+k_G X_d'' S_b/S_{N,G})$；电动机 $I_{k,M}'' = 3.5 I_{r,M}$；多电源支路代数相加 | GB/T 15544.1-2013, IEC 60909-0:2016, DL/T 5222-2021 | CALC-SC-002（网络法）·PR-DD-002（断路器开断能力） |

**计算层已建成 22 条（含三期续 5 条），完成度 100%。**

剩余可按需扩展方向：

- 直流系统短路电流计算（UPS/储能 DC 侧）
- 有源配电网短路计算（含 PCS 短路贡献）
- 谐波电流在电网中的分配计算
- 防雷接地冲击电阻计算（GDT 选型）
- 变压器励磁涌流与差流计算（整定用）

## 后续规划

计算层已全部建成。如需扩展以上方向或切换到实践层（PR 四期），继续告诉我。

