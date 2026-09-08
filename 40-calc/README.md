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

## 后续规划（二期第二批～三期）

高压短路电流计算（IEC 60909 远端/近端网络）、电缆载流量计算（GB/T 16895.6 校正系数体系）、接地网设计计算（IEEE 80/GB/T 50065）、电压偏差与电压损失计算、电机启动压降校验、照度点照度校验法、柴油发电机容量选择、UPS 蓄电池 autonomy 校核。

条目编号：`CALC-{域}-{三位序号}-{英文短名}.md`，域：SC 短路/LD 负荷/PT 保护/BT 蓄电池/LT 照明/RC 无功/HV 高压/CA 电缆/GR 接地。
