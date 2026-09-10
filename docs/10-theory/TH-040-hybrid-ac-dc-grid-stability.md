---
id: TH-040
title: 交直流混联电网稳定机理（LCC/VSC 换流站耦合、多馈入短路比与相互作用）
domain: 基础理论
subdomain: 电力系统
voltage_levels: [HV, EHV, UHV]
lifecycle: [规划, 设计, 运维]
standards:
  - { code: GB/T 38306-2019, clause: "全文", note: "柔性直流输电系统技术规程（VSC-HVDC 工程）" }
  - { code: GB/T 35127-2017, clause: "全文", note: "柔性直流输电系统接入电网技术规定" }
  - { code: GB 38755-2019, clause: "全文", note: "电力系统安全稳定导则（强制性）：交直流混联三道防线" }
  - { code: DL/T 5426-2020, clause: "全文", note: "高压直流输电系统设计规程" }
  - { code: IEC 60919-3:2024, clause: "3", note: "Performance of high-voltage direct current (HVDC) systems - Part 3: Dynamic conditions, 含多馈入场景" }
status: draft
reviewers: []
version: 0.1
updated: 2026-09-09
---

# 交直流混联电网稳定机理（LCC/VSC 换流站耦合、多馈入短路比与相互作用）

## 1. 定义

本条研究**多条直流落点于同一交流电网**时的耦合稳定问题，以及**LCC（电网换相换流器）与 VSC（电压源换流器）共存**下的互补机理。

| 类别 | 定义 | 失效风险 |
|---|---|---|
| **多馈入直流（MIDC）** | 多条直流落点同一交流系统，电气距离近、耦合强 | 换相失败连锁、电压失稳连锁 |
| **多馈入有效短路比（MISCR）** | 计及邻侧直流耦合后的等效短路比 | MISCR<2.5 为极弱系统 |
| **LCC/VSC 互补** | VSC 无换相失败，可补偿 LCC 暂态无功缺口 | 混合拓扑控制协调复杂 |
| **交直流混联** | 直流接入改变交流电网功角/电压/频率稳定形态 | 稳定形态从"功角主导"转向"电压主导" |

## 2. 物理图像

交直流混联电网稳定的物理图像：

```
交流电网                     直流外送
  ┌─── G1 ───┐             ┌──→ 受端电网
  │          │   DC1(LCC)  │
  G2 ── 母线A ──────────────┤
  │          │   DC2(VSC)  │
  └─── G3 ───┘             └──→ 受端电网
     ↓ 换流母线A
     多馈入耦合：DC1 与 DC2 母线电压互相影响
     DC1 换相失败 → 母线A 电压跌落 → DC2 低压穿越压力
```

**耦合核心**：两条直流的电气耦合阻抗 $Z_{12}$ 越小（落点越近），一条直流换相失败时另一条直流承受的电压冲击越大。

## 3. 推导

### 3.1 多馈入有效短路比（MISCR）

传统单馈入短路比：

$$SCR = \frac{S_{sc}}{P_{dc}} = \frac{U_N^2}{Z_{sc}P_{dc}}$$

多馈入有效短路比（第 $i$ 回直流）：

$$MISCR_i = \frac{S_{sc,i} - \sum_{j\ne i} U_i U_j / Z_{ij} \cdot \Delta U_j / \Delta P_i}{P_{dc,i}}$$

工程简化公式（CIGRE B4.52）：

$$MISCR_i = \frac{S_{sc,i}}{P_{dc,i}} - \frac{1}{Z_{eq,ij}} \cdot \frac{P_{dc,j}}{P_{dc,i}}$$

| 换流站间电气距离 $d$ | 耦合阻抗 $Z_{12}$ (p.u.) | $MISCR_1$（$SCR_1$=3） | 耦合强度 |
|---|---|---|---|
| 近距（共母线段） | 0.05 | 2.0 | 强耦合（危险） |
| 中距（邻段母线） | 0.30 | 2.6 | 中耦合 |
| 远距（不同分区） | 1.0 | 2.9 | 弱耦合 |

### 3.2 换相失败连锁传播

LCC 换相失败判据（换相面积）：

$$A_{comm} = \int_{t_0}^{t_0+\gamma/\omega} (i_{comm}(t) - i_{dc})\,dt > 0$$

故障时母线电压跌落 $\Delta U$，导致换相面积不足：

$$A_{comm}' = A_{comm}\left(1 - \frac{\Delta U}{U_0}\right)^{1.5}$$

连锁触发条件（多馈入连锁换相失败）：

$$\Delta U_{bus,i} > 0.2\,U_N \quad \Rightarrow \quad \text{DC}_i \text{ 换相失败概率} > 80\%$$

| 故障场景 | DC1 换相失败 | DC2 换相失败概率 | 连锁延迟 |
|---|---|---|---|
| DC1 单极闭锁 | 是 | <10%（若 MISCR>3） | — |
| DC1 双极闭锁 | 是 | 30~60%（MISCR=2.5） | 3~5 周波 |
| 近区三相短路 | 双回同时失败 | >90% | 同时 |

### 3.3 LCC/VSC 互补无功

LCC 换流站吸收无功 $Q_{LCC} \approx 0.5\,P_{dc}$，故障时骤增：

$$\Delta Q_{LCC}^{fault} = Q_{LCC,0}\left(\frac{U_0}{U_{fault}} - 1\right)$$

VSC 可瞬时输出无功（$<5$ ms）：

$$Q_{VSC} = \sqrt{S_{VSC}^2 - P_{VSC}^2}$$

互补判据（VSC 补偿 LCC 缺口）：

$$Q_{VSC} \ge \Delta Q_{LCC}^{fault} \cdot \frac{1}{MISCR}$$

| LCC 容量 | 故障无功缺口 | VSC 配置（1/3 原则） | 补偿效果 |
|---|---|---|---|
| 3000 MW | 1500 Mvar | 500 Mvar（MISCR=3） | 换相失败概率 ↓40% |
| 8000 MW（多馈入） | 4000 Mvar | 1500 Mvar（MISCR=2.5） | 换相失败概率 ↓25% |

## 4. 与工程实践的联系

### 4.1 支撑条目

- [PR-ES-001 电化学储能接入](../30-practice/PR-ES-001-energy-storage-integration.md)：VSC 换流站与构网型 PCS 共享控制，MIDC 场景下储能参与暂态无功补偿整定。
- [PR-PQ-001 无功补偿与谐波治理](../30-practice/PR-PQ-001-pq-compensation-design.md)：MIDC 受端动态无功配置与 MISCR 校核流程，VSC 调制谐波源背景。
- [PR-PE-001 继电保护配置](../30-practice/PR-PE-001-relay-protection-config.md)：直流闭锁后潮流转移引发交流线路过载保护与系统级解列配合。
- [PR-DD-002 变电所布置与设备选型](../30-practice/PR-DD-002-substation-layout-and-equipment-selection.md)：多馈入受端动态无功补偿容量与 STATCOM/SVG 选型物理源头。
- [CALC-SC-002 高压短路](../40-calc/CALC-SC-002-hv-short-circuit-iec60909.md)：$S_{sc}$ 与 MISCR 计算数据源。

### 4.2 失效边界

| 失效场景 | 原因 | 对策 |
|---|---|---|
| **MISCR<2.0**（极弱受端） | 交流网架薄弱、直流容量过大 | 加强交流网架 / 装 VSC / 储能调频 |
| **多回直流同时换相失败** | 近区三相短路，耦合强 | 直流降功率运行 / 母线分段 / 故障穿越协调控制 |
| **LCC/VSC 控制不协调** | 两类换流站控制器时间常数差异 | 统一广域协调控制（WAMS 主从） |
| **次同步振荡传递**（LCC→AC→VSC） | 直流调制引入 20~40 Hz 振荡分量 | SSDC 抑制 + 交流侧阻尼（见 TH-035） |
| **频率稳定失效**（高纯直流送出） | 直流闭锁瞬间送端频率跳变 | 送端配置同步调相机恢复短路容量 |

## 5. 关联条目与变更记录

- 关联：[TH-020 电力系统稳定性分类](TH-020-power-system-stability-classification.md)、[TH-027 HVDC LCC/VSC](TH-027-hvdc-transmission-lcc-vsc.md)（换相失败/SCR）、[TH-035 SSR/SSCI](TH-035-sub-synchronous-resonance-ssr-ssci.md)（直流调制诱发次同步振荡）、[TH-038 新能源惯量支撑](TH-038-high-renewable-frequency-stability-inertia.md)（直流闭锁频率冲击与调相机容量）、[TH-037 OLTC 与无功协调](TH-037-tap-changer-and-dynamic-reactive-coordination.md)（受端动态无功协调）

| 版本 | 日期 | 修改内容 | 修改人 |
|---|---|---|---|
| 0.1 | 2026-09-09 | 创建；含 MISCR 推导、换相失败连锁、LCC/VSC 互补 | KB 管理员 |
