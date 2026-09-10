---
id: TH-025
title: 电缆热场与载流量计算基础
domain: 基础理论
subdomain: 电缆传输
voltage_levels: [LV, MV, HV]
lifecycle: [设计, 选型, 运维]
standards:
  - { code: GB/T 16895.18-2022, clause: "附录B", note: "建筑物电气装置线缆载流量与热阻计算（idt IEC 60364-5-52）" }
  - { code: GB 50217-2018, clause: "4", note: "电力工程电缆设计标准，给出敷设方式校正与载流量选用" }
  - { code: GB/T 11017-2014, clause: "4", note: "额定电压110kV交联聚乙烯绝缘电缆热学与短时过载曲线" }
  - { code: IEC 60287-1-1:2014, clause: "4", note: "电缆稳态热计算国际标准，给出RAC/热阻/载流量通解" }
status: draft
reviewers: []
version: 0.1
updated: 2026-09-09
---

# 电缆热场与载流量计算基础

## 1. 定义

**电缆载流量（ampacity）**指在给定敷设环境与运行条件下，电缆导体长期允许工作温度不超过绝缘材料最高持续运行温度时所对应的稳态电流。决定载流量的物理本质是**稳态热平衡**：导体损耗（铜损+介质损）经各层热阻传到环境，每层温度梯度由 $q=\Delta T/R_\theta$ 决定。

| 物理量 | 符号 | 单位 | 含义 |
|---|---|---|---|
| 导体工作温度 | $\theta_c$ | ℃ | 长期允许上限（XLPE 90 ℃，EPR 90 ℃，PVC 70 ℃） |
| 环境温度 | $\theta_a$ | ℃ | 空气敷设取最热月日均最高；土壤敷设取常年地温 |
| 热阻 | $R_\theta$ | K·m/W | 单位长度的温度梯度与热流之比 |
| 热流 | $q$ | W/m | 单位长度发热量 |
| 允许载流量 | $I$ | A | 稳态热平衡下导体温度恰好到 $\theta_c$ 对应电流 |

## 2. 物理图像

从内到外的圆柱套筒热路（以单芯交联电缆为例）：

```
铜芯 ─ R_cond(绝缘) ─ R_scr(屏蔽) ─ R_jk(护套) ─ R_env(敷设环境)
 θ_c                                                          θ_a
   ↑            ↑              ↑             ↑            ↑
   └─────────── 每层热阻串联，总热阻决定温度抬升 ────────────┘
```

各层热阻对应圆柱壁导热：$R_\theta=\dfrac{1}{2\pi\lambda}\ln(r_o/r_i)$，其中 $\lambda$ 为材料导热系数（XLPE 约 0.29 W/(m·K)、铜屏蔽 0.18、PVC 护套 0.17、土壤 0.8~1.2、空气 0.026）。

热源有三类：导体铜损 $I^2R_{ac}$、屏蔽涡流损耗 $I_s^2R_s$、介质损耗 $U^2\omega C\tan\delta$。低压电缆以铜损为主；110 kV 及以上电缆介质损耗占比明显上升（XLPE $\tan\delta\approx 0.001$，但电压高，损耗可观）。

## 3. 推导

### 3.1 单回路电缆载流量通解（IEC 60287）

将全部热源与热阻代入稳态热平衡：

$$
\theta_c-\theta_a = I^2R_{ac}(R_{ins}+R_{scr}+R_{jk}+R_{env}) + \frac{1}{2}W_d R_{ins} + W_d(R_{scr}+R_{jk}+R_{env}) + \lambda_1 I^2 R_{ac}(R_{scr}+R_{jk}+R_{env})
$$

整理得载流量：

$$
I = \sqrt{\frac{\theta_c-\theta_a-\Delta\theta_d}{R_{ac}\big[(1+\lambda_1)R_{total}+\lambda_1'(R_{scr}+R_{jk}+R_{env})\big]}}
$$

其中 $\Delta\theta_d$ 为介质损耗引起的温升、$\lambda_1$ 为屏蔽损耗比（屏蔽涡流/铜损）。低压电缆 $W_d\approx 0$、$\lambda_1\approx 0$ 时简化为：

$$
I = \sqrt{\frac{\theta_c-\theta_a}{R_{ac}\,R_{total}}}
$$

### 3.2 多回路并列敷设的群集校正

多根电缆并列时，相邻电缆互为热源，相邻回路温升叠加。IEC 给出群集系数 $k_g$（载流量修正倍数）：

$$
I_{group}=k_g \cdot I_{single}\quad k_g<1
$$

托盘内并列间距 $s=d$（电缆外径）时 $k_g\approx 0.7$；间距 $s=2d$ 时 $k_g\approx 0.85$。详细查表见 [CALC-CD-001](../40-calc/CALC-CD-001-cable-ampacity-correction.md)。

### 3.3 短时过载与应急负荷（GB/T 11017）

短时（一般 0.5~4 h）过载下热平衡尚未建立，可用暂态热路 RC 模型：

$$
\theta_c(t)=\theta_0+\Delta\theta_\infty(1-e^{-t/\tau})
$$

其中 $\tau$ 为电缆热时间常数（中压电缆 $\tau\approx 2\sim 4$ h，随截面增大）。XLPE 电缆允许短时过载至 1.2~1.3 倍额定，时间不超过 4 h；事故应急可到 1.5 倍 ≤ 10 min（具体曲线见 GB/T 11017 §4）。

## 4. 与工程实践的联系

- **支撑条目 1**：[CALC-CD-001 电缆截面与降容](../40-calc/CALC-CD-001-cable-ampacity-correction.md)——本条给出 IEC 60287 通解与群集校正，是截面选取与降容系数查表的物理源头。
- **支撑条目 2**：[PR-DD-002 变配电所布置](../30-practice/PR-DD-002-substation-layout-and-equipment-selection.md)——电缆桥架/排管敷设方式与群集系数直接影响所选截面。
- **支撑条目 3**：CASE-019 电缆载流量温度修正 与 CASE-034 10kV 电缆终端击穿——本条给出温度修正与热失衡致局部过热的物理基础。
- **失效边界**：① 公式假定稳态热平衡，启动初期（<3τ）误差大，须用暂态热路；② 土壤干燥失水时 $\lambda$ 急降（热阻升 2~3 倍），载流量可能下降 30%，须按干燥/潮湿双工况校核；③ 邻近热源（蒸汽管、热水管）会抬升 $\theta_a$，须叠加温升；④ 电缆密集交叉处局部热阻非均匀，须三维场仿真；⑤ 短路热稳定按绝热过程（详见 [CALC-CD-001 §热稳定](../40-calc/CALC-CD-001-cable-ampacity-correction.md)），与本条稳态热平衡属不同物理过程，不可混用。
- **下游案例**：CASE-019 电缆载流量真题、CASE-029 2019 电缆载流量真题、CASE-034 10kV 电缆终端击穿、[CASE-049 10kV 中间接头击穿](../50-case/CASE-049-review-cable-joint-construction-defect.md)

## 5. 关联条目与变更记录

- 关联：[TH-014 磁路饱和](TH-014-magnetic-circuit-saturation.md)（铁损与介质损类比）、[TH-008 谐波产生机理](TH-008-harmonic-generation.md)（谐波附加铜损）、[TH-019 输电线路参数](TH-019-transmission-line-parameters-long-line.md)（长电缆充电电流与分布参数）、[CALC-CD-001](../40-calc/CALC-CD-001-cable-ampacity-correction.md)、[PR-DD-002](../30-practice/PR-DD-002-substation-layout-and-equipment-selection.md)
- 下游案例：见 §4 列表。

| 版本 | 日期 | 修改内容 | 修改人 |
|---|---|---|---|
| 0.1 | 2026-09-09 | 创建；含 IEC 60287 通解、群集校正、短时过载暂态 RC 模型、干燥土壤失效边界 | KB 管理员 |
