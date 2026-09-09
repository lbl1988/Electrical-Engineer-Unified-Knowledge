# L2.5 计算库（40-calc）

> 定位：可直接套用的完整计算方法条目。每条含公式出处（标准/手册页码）、输入输出清单、完整算例（数字全部手工复算）、常见错误表。
> 原则：**一个工况一条链路**——从原始参数到选型结论一步到底，中间值不跳步；与 10-theory（原理）和 30-practice（应用）双向挂接。

## 二期第一批成果（6 条）

| ID | 主题 | 核心公式/方法 | 主要标准依据 | 下游应用条目 |
|---|---|---|---|---|
| [CALC-SC-001](CALC-SC-001-低压三相短路电流计算.md) | 低压三相短路电流计算 | Ik″=c·Un/(√3·Zk)；ip=κ√2·Ik″ | GB/T 15544.1-2013 (IEC 60909) | [PR-DD-001](../30-practice/PR-DD-001-lv-breaker-selection.md)·[PR-GR-002](../30-practice/PR-GR-002-earthing-arrangement.md) |
| [CALC-LD-001](CALC-LD-001-demand-factor-method.md) | 需要系数法负荷计算 | Pjs=Kx·Pe；P30=KΣp·ΣPjs | 《工业与民用供配电设计手册》第四版 | [PR-PS-001](../30-practice/PR-PS-001-load-classification.md)·[PR-PQ-001](../30-practice/PR-PQ-001-pq-compensation-design.md) |
| [CALC-PT-001](CALC-PT-001-protection-setting.md) | 低压断路器保护整定与灵敏度校验 | Ir≥IB；Isd≥1.2Ipk；Ksen=Ik/Iop≥1.3 | GB 50054-2011, GB/T 14048.2-2020 | [PR-DD-001](../30-practice/PR-DD-001-lv-breaker-selection.md) |
| [CALC-BT-001](CALC-BT-001-battery-capacity.md) | 蓄电池容量计算（双体系） | 能量法 Cd=KPt/(Udcη)；换算法 Cc=Kk·Idis/Kc | GB 51309-2018, DL/T 5044-2014 | [PR-BE-001](../30-practice/PR-BE-001-emergency-lighting.md) |
| [CALC-LT-001](CALC-LT-001-lumen-method.md) | 利用系数法照度计算 | N=E·A/(Φ·UF·MF)；LPD 校核 | GB 50034-2024 | [PR-BE-001](../30-practice/PR-BE-001-emergency-lighting.md) |
| [CALC-RC-001](CALC-RC-001-reactive-compensation.md) | 无功补偿容量计算与电抗率选择 | QC=P30(tanφ1−tanφ2)；ν=1/√p | GB 51348-2019, GB/T 15543-2008 | [PR-PQ-001](../30-practice/PR-PQ-001-pq-compensation-design.md) |

## 典型工况链（算例数据贯通）

同一虚构项目（综合办公楼）的数据在条目间贯通流转，形成完整设计链：

```
CALC-LD-001 负荷计算（P30=395.1kW, cosφ=0.797）
   ├─→ CALC-RC-001 无功补偿（QC=107.9kvar→120kvar, cosφ'=0.911）
   ├─→ CALC-PT-001 保护整定（IB=114A→Ir=125A, 卡点工况 250m 需 B 型脱扣）
   │       ↑ CALC-SC-001 短路电流（d1: Ik″=23.3kA, ip=53.6kA）
   └─→ PR-DD-001 断路器选型（ACB 50kA/105kA, 级差 8.5 倍全选择性）
```

## 后续规划（二期第三批～三期）

照度逐点校验法、柴油发电机容量选择、UPS 蓄电池 autonomy 校核、距离保护整定、电动机温升计算。

## 二期第二批成果（5 条）

| ID | 主题 | 核心公式/方法 | 主要标准依据 | 下游应用条目 |
|---|---|---|---|---|
| [CALC-CD-001](CALC-CD-001-cable-ampacity-correction.md) | 电缆载流量计算与校正系数 | $I_z' = I_z \times K_t \times K_g \times K_{soil}$ | GB/T 16895.6-2014 (IEC 60364-5-52), GB 50217-2018 | [PR-DD-001](../30-practice/PR-DD-001-lv-breaker-selection.md)·[CALC-SC-001](CALC-SC-001-低压三相短路电流计算.md)（热稳定） |
| [CALC-SC-002](CALC-SC-002-hv-short-circuit-iec60909.md) | 高压系统三相短路电流计算（IEC 60909 网络法） | $I_k'' = c \cdot U_n / (\sqrt{3} \cdot Z_k)$，MV $c=1.10$ | GB/T 15544.1-2013, DL/T 5222-2021 | [PR-DD-002](../30-practice/PR-DD-002-substation-layout-and-equipment-selection.md)·[PR-PE-001](../30-practice/PR-PE-001-relay-protection-config.md)·[TH-011](../10-theory/TH-011-synchronous-machine-subtransient-reactance.md) |
| [CALC-GR-001](CALC-GR-001-grounding-grid-design.md) | 变电站接地网设计计算（GB/T 50065 / IEEE 80） | $R_g \approx 0.5\rho/\sqrt{A}$；$E_{t,\lim}=(116+0.7\rho_s)/\sqrt{t}$ | GB/T 50065-2011, IEEE 80-2013 | [PR-GR-002](../30-practice/PR-GR-002-earthing-arrangement.md)·[TH-005](../10-theory/TH-005-touch-step-voltage.md) |
| [CALC-VL-001](CALC-VL-001-voltage-deviation-and-loss.md) | 电压偏差与电压损失计算 | $\Delta U\% = (PR+QX)/U_n^2\times 100\%$；$\delta U = \delta U_0 + \Delta U_T - \Delta U_{line}$ | GB/T 12325-2008, GB 50052-2009, GB 51348-2019 | [CALC-MS-001](CALC-MS-001-motor-starting-voltage-drop.md)（启动尖峰叠加）·[PR-DD-002](../30-practice/PR-DD-002-substation-layout-and-equipment-selection.md)（分接头选型）·[CALC-CD-001](CALC-CD-001-cable-ampacity-correction.md)（电缆选型双校） |
| [CALC-MS-001](CALC-MS-001-motor-starting-voltage-drop.md) | 电动机启动压降校验 | $\Delta U_{st}\% \approx K_{st}S_M/(S_{sc}+K_{st}S_M)\times 100\%$ | GB 50055-2011, GB 51348-2019 | [PR-DD-002](../30-practice/PR-DD-002-substation-layout-and-equipment-selection.md)·[CALC-PT-001](CALC-PT-001-protection-setting.md)（躲启动尖峰） |

条目编号：`CALC-{域}-{三位序号}-{英文短名}.md`，域：SC 短路/LD 负荷/PT 保护/BT 蓄电池/LT 照明/RC 无功/HV 高压/CA 电缆/GR 接地/VL 电压/MS 电机启动。
