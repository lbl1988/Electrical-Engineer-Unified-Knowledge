---
id: CASE-050
title: 2016供配电真题拆解：办公建筑照度计算与照明功率密度校验
domain: CASE
subdomain: EX
case_type: exam
year_source: 2016年注册电气工程师（供配电）专业案例
desensitized: true
voltage_levels: [LV]
lifecycle: [设计]
standards:
  - { code: GB 50034-2024, clause: "第4章/第5章", note: "建筑照明设计标准：照度标准与LPD限值" }
  - { code: GB/T 5700-2008, clause: "第5章", note: "照明测量方法：照度计算" }
  - { code: GB 51348-2019, clause: "第21章", note: "民用建筑电气设计标准：照明设计" }
  - { code: CIE 115-2010, clause: "全文", note: "Lighting of roads for pedestrian and low speed areas" }
  - { code: GB/T 26189-2010, clause: "全文", note: "室内照明测量方法" }
status: draft
reviewers: []
version: 0.1
updated: 2026-09-09
---

# 2016供配电真题拆解：办公建筑照度计算与照明功率密度校验

## 1. 摘要

2016 年供配电专业案例题：某办公楼标准层办公区面积 600m²，采用 LED 灯具（单灯功率 36W，光通量 3200lm，利用系数 0.6），要求照度 300lx，校验照明功率密度（LPD）是否满足 GB 50034 限值 9W/m²。结论：所需灯具数 $N=E A/(\Phi U K)=300\times 600/(3200\times 0.6\times 0.8)=117$ 盏，总功率 $P=117\times 36=4212$W，$LPD=4212/600=7.02$ W/m² < 9 W/m² ✓。教训：**照明设计须同时满足照度（利用系数法）和 LPD（功率密度限值）双指标，LED 灯具须核算实际光效与利用系数，不可仅按标称功率选。**

## 2. 背景

### 2.1 真题题干（脱敏重构）

某办公楼标准层开敞办公区：

| 参数 | 数值 | 说明 |
|---|---|---|
| 面积 $A$ | 600 m² | 长30m×宽20m |
| 照度标准 $E$ | 300 lx | GB 50034 办公区 |
| LPD 限值 | 9 W/m² | GB 50034 目标值 |
| LED 灯具功率 | 36 W | 含驱动 |
| 光通量 $\Phi$ | 3200 lm | 灯具标称 |
| 利用系数 $U$ | 0.6 | 查表 |
| 维护系数 $K$ | 0.8 | 办公室 |

**问题**：（1）计算所需灯具数量；（2）校验 LPD 是否满足要求。

### 2.2 关键考点

1. 利用系数法照度计算 $E=N\Phi U K/A$
2. 灯具数量向上取整
3. LPD = 总功率/面积 ≤ 限值
4. 维护系数取值

## 3. 方案（解题链路）

```
1. 照度公式: E = N·Φ·U·K / A
2. 求 N: N = E·A / (Φ·U·K)
3. N 向上取整
4. 总功率 P = N·P_lamp
5. LPD = P / A
6. 与限值 9 W/m² 比较
```

## 4. 计算

### 4.1 利用系数法照度计算（引自 [CALC-LT-001](../40-calc/CALC-LT-001-lumen-method.md) + GB 50034-2024）

$$E=\frac{N\Phi U K}{A}$$

求灯具数量：

$$N=\frac{E A}{\Phi U K}=\frac{300\times 600}{3200\times 0.6\times 0.8}=\frac{180000}{1536}=117.2$$

向上取整：**$N$=118 盏**

### 4.2 照明功率密度 LPD（引自 GB 50034-2024 §5）

$$LPD=\frac{P_{total}}{A}=\frac{N\times P_{lamp}}{A}=\frac{118\times 36}{600}=\frac{4248}{600}=7.08\ \text{W/m}^2$$

**$LPD$=7.08 W/m² < 9 W/m²（限值）✓**

### 4.3 实际照度校核

取 $N$=118 盏时：

$$E=\frac{118\times 3200\times 0.6\times 0.8}{600}=\frac{118\times 1536}{600}=\frac{181248}{600}=302\ \text{lx}>300\ \text{lx ✓}$$

### 4.4 利用系数取值说明（引自 CALC-LT-001）

利用系数 $U$ 取决于：
- 室空间比 RCR：$RCR=5h(L+W)/(L\times W)$
- 顶棚反射比 $\rho_c$：一般 0.7
- 墙面反射比 $\rho_w$：一般 0.5
- 地面反射比 $\rho_f$：一般 0.2

本题取 $U$=0.6（办公空间典型值）。

### 4.5 维护系数取值（引自 GB 50034-2024 表4.1.6）

| 环境特征 | 维护系数 $K$ |
|---|---|
| 清洁（住宅、办公室） | 0.8 |
| 一般（商店、阅览室） | 0.7 |
| 污染多（工厂、厨房） | 0.6 |

办公室取 $K$=0.8 ✓

### 4.6 LED 光效核算

灯具光效：

$$\eta=\frac{\Phi}{P}=\frac{3200}{36}=88.9\ \text{lm/W}$$

GB 50034 要求 LED 灯具光效 ≥90 lm/W（办公），88.9 略低，建议选 4000lm/36W（111 lm/W）。

若改用高光效灯具（$\Phi$=4000lm，$P$=36W）：

$$N=\frac{300\times 600}{4000\times 0.6\times 0.8}=\frac{180000}{1920}=93.75\to 94\ \text{盏}$$

$$LPD=\frac{94\times 36}{600}=5.64\ \text{W/m}^2<9\ \text{W/m}^2\ \text{✓（更优）}$$

## 5. 审查意见（真题考点陷阱）

| 序号 | 常见错误 | 正确做法 |
|---|---|---|
| 1 | 不乘维护系数 $K$ | $K$=0.8（办公室） |
| 2 | 灯具数取四舍五入 | 向上取整 |
| 3 | 用 $N$ 非整数算 LPD | 用取整后的 $N$ |
| 4 | 忽略 LED 光效要求 | 光效 ≥90 lm/W |

## 6. 整改

### 6.1 灯具优化

选用高光效 LED（≥90 lm/W），减少灯具数量，降低 LPD。

### 6.2 智能照明

- 分区控制（靠窗区利用自然光调光）
- 人体感应（无人关灯）
- 可降低实际 LPD 30%~50%

## 7. 经验教训

- [ ] **照度计算用利用系数法**：$E=N\Phi UK/A$
- [ ] **维护系数不可忘**（办公室 0.8）
- [ ] **灯具数量向上取整**后再算 LPD
- [ ] **LPD 须 ≤ GB 50034 限值**
- [ ] LED 灯具光效 ≥90 lm/W（办公）

## 8. 关联条目

- 上游：[CALC-LT-001 照度计算](../40-calc/CALC-LT-001-lumen-method.md)（利用系数法）、[CALC-LT-002 点照度法](../40-calc/CALC-LT-002-point-illuminance-method.md)（点照度校核）、[PR-PS-001 负荷分级](../30-practice/PR-PS-001-load-classification.md)（照明负荷）
- 下游：[PR-DD-002 变电所布置](../30-practice/PR-DD-002-substation-layout-and-equipment-selection.md)（照明配电）
- 平行：[CASE-001 负荷分级真题](CASE-001-exam-load-classification.md)（同源供配电真题——照明负荷）、[CALC-LD-001 需要系数法](../40-calc/CALC-LD-001-demand-factor-method.md)（照明负荷计算）

## 9. 变更记录

| 版本 | 日期 | 修改内容 | 修改人 |
|---|---|---|---|
| 0.1 | 2026-09-09 | 初版创建 | 知识库 |
