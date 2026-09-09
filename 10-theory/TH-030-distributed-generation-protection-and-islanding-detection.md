---
id: TH-030
title: 分布式电源并网保护与孤岛检测
domain: 基础理论
subdomain: 分布式电源
voltage_levels: [LV, MV, HV]
lifecycle: [设计, 运维]
standards:
  - { code: GB/T 19939-2016, clause: "5", note: "光伏并网逆变器技术要求，含防孤岛与低电压穿越" }
  - { code: GB/T 19964-2024, clause: "4", note: "光伏发电站接入电力系统技术规定（替代 2012 版，强化高电压穿越）" }
  - { code: GB/T 40595-2021, clause: "4", note: "电力系统网源协调技术规范，含分布式电源涉网保护" }
  - { code: IEC 62116-2014, clause: "6", note: "光伏逆变器孤岛检测规程，规定测试工况与切除时间" }
status: draft
reviewers: []
version: 0.1
updated: 2026-09-09
---

# 分布式电源并网保护与孤岛检测

## 1. 定义

**分布式电源（Distributed Generation, DG）**指接入配电网（35 kV 及以下）的分散式发电装置，包括光伏、风电、燃气轮机、燃料电池、小型水电等。与集中式大电源不同，DG 改变了配电网"单向辐射受端"格局，带来**双向潮流**与**孤岛**两类新问题，须配置专门并网保护。

**孤岛（Island）**指主网失电后，DG 仍向局部网络持续供电的状态。分为：
- **非计划孤岛**：意外形成，电压/频率不受控，危及检修人员安全，须在 2 s 内切除（GB/T 19939）；
- **计划孤岛**：微电网主动断开并持续运行（详见 [TH-029 微电网控制](TH-029-microgrid-control-and-grid-mode-switching.md)）。

| 保护类型 | 功能 | 标准依据 |
|---|---|---|
| 防孤岛保护 | 主网失电后 2 s 内切除 DG | GB/T 19939 §5、IEC 62116 |
| 低电压穿越（LVRT） | 电网跌落时短时不停机支撑 | GB/T 19964-2024 §4 |
| 高电压穿越（HVRT） | 电网过电压时短时不停机 | GB/T 19964-2024 新增 |
| 频率异常保护 | $f$ 越限（49.5~50.2 Hz）切除 | GB/T 40595 |
| 逆功率保护 | 防止 DG 向上级反送电 | 设计规范/并网协议 |

## 2. 物理图像

### 2.1 防孤岛保护的检测盲区

当 DG 输出功率 $P_{DG}$ 与本地负荷 $P_{load}$ 恰好匹配（$P_{DG}\approx P_{load}, Q_{DG}\approx Q_{load}$）时，主网断开后 PCC 处电压/频率变化极小——这就是**检测盲区（Non-Detection Zone, NDZ）**。被动检测（电压/频率越限）在此工况下无法识别孤岛。

```
主网 ──●── PCC ── 本地网络 ── 负荷 P_load, Q_load
        │                    │
      并网断路器            DG: P_DG, Q_DG

主网断电后，若 P_DG ≈ P_load，PCC 处 ΔU, Δf 几乎为 0 → 被动检测失效
```

### 2.2 LVRT 曲线（GB/T 19964-2024）

光伏电站须在电网电压跌落时按曲线短时不停机：

```
U/U_N (%)
100 │─────┐
 90 │     │────────────────────────────┐
 20 │     │                            │
  0 └─────┴────────────────────────────┴──→ t (s)
     0   0.15          0.625         1.5   2.0
     │←不脱网→│←必须连续运行→│←可脱网→│
```

曲线要求：$U<90\%$ 时须持续运行 0.625 s，$U>20\%$ 时不脱网至 1.5 s。风电 LVRT 曲线类似但参数不同。

## 3. 推导

### 3.1 被动检测判据与盲区

主网失电后 PCC 处电压变化取决于功率失配：

$$
\Delta U \approx \frac{\Delta P \cdot R + \Delta Q \cdot X}{U_0}
$$

频率变化取决于有功失配（转子方程简化）：

$$
\Delta f \approx \frac{\Delta P}{K_{f}\,P_{load}}
$$

$K_f$ 为系统频率调节系数（典型 1%~3%/p.u.）。被动检测判据：

| 判据 | 典型阈值 | 盲区 |
|---|---|---|
| $\lvert\Delta U\rvert$ | 10% | $\lvert\Delta P\rvert<0.1\,P_{load}$ 时无法检出 |
| $\lvert\Delta f\rvert$ | 0.2 Hz | $\lvert\Delta P\rvert<K_f\cdot0.2\cdot P_{load}$ 时无法检出 |
| $\lvert\Delta\phi\rvert$（相位跳变） | 10° | 对纯阻负荷有效，对感性负荷盲区仍存在 |

### 3.2 主动检测——频率偏移法（AFD）

逆变器在并网时主动注入微小频率偏移（在电流参考叠加直流或不对称波形）。并网时频率被主网锁定，偏移无效果；孤岛时频率自由漂移，加速越限检出：

$$
f_{ref} = f_0 + \Delta f_{AFD}\cdot \text{sign}(I_{load})
$$

$\Delta f_{AFD}$ 典型 0.5~1 Hz。AFD 将检测盲区缩小至 $\lvert\Delta P\rvert<0.01\,P_{load}$，但会引入谐波并影响电能质量。

### 3.3 LVRT 有功支撑

LVRT 期间逆变器须注入无功电流支撑电压恢复（GB/T 19964 §4）：

$$
I_Q \ge 1.5\,(1-U/U_N)\,I_N\quad (0.2\le U/U_N \le 0.9)
$$

| $U/U_N$ | $I_Q/I_N$（最小） | 支撑效果 |
|---|---|---|
| 0.9 | 0.15 | 轻跌落 |
| 0.5 | 0.75 | 中度跌落 |
| 0.2 | 1.20 | 严重跌落，满发无功 |

注入无功电流抬升并网点电压，辅助电网恢复——这是构网型 PCS 的雏形（详见 [TH-024 电力电子变换器](TH-024-power-electronic-converters-and-pwm.md)）。

### 3.4 逆功率保护整定

防止 DG 向上级反送电（如自发自用余电不上网模式）：

$$
P_{set} = -k\cdot P_{DG,rated}\quad (k=1\%\sim5\%)
$$

$P_{PCC}<P_{set}$ 持续 0.2~2 s 切除 DG。负号表示反方向（向主网送电）。

## 4. 与工程实践的联系

- **支撑条目 1**：[PR-PE-001 继电保护配置](../30-practice/PR-PE-001-relay-protection-config.md) 与 [TH-012 保护四性](TH-012-protection-four-properties.md)——DG 接入改变了配电网短路电流方向与大小，原有保护可能误动/拒动，须重新整定。
- **支撑条目 2**：[TH-029 微电网控制](TH-029-microgrid-control-and-grid-mode-switching.md) 与 [TH-024 电力电子变换器](TH-024-power-electronic-converters-and-pwm.md)——防孤岛与计划孤岛是同一物理过程的两种处理方式，构网型 PCS 的 LVRT 无功支撑是黑启动的过渡。
- **支撑条目 3**：[PR-ES-001 储能接入](../30-practice/PR-ES-001-energy-storage-integration.md)——储能 PCS 同样须配置防孤岛与 LVRT，储能+光伏组成光储一体系统。
- **失效边界**：① 被动检测存在盲区，$P_{DG}\approx P_{load}$ 时无法检出，须主动检测或组合方案；② AFD 等主动检测会引入谐波，电能质量敏感场所（如医院、数据中心）须慎用；③ LVRT 曲线仅适用于并网点电压跌落，DG 本身故障须由内部保护切除；④ GB/T 19964-2024 新增 HVRT（$U>110\%$~$130\%$ 持续 0.5~2 s 不脱网），老型号逆变器可能不支持；⑤ 逆功率保护灵敏度受 DG 功率波动影响，须设延时避免误动。
- **下游案例**：[CASE-048 新能源汇集站继保](../50-case/CASE-048-composite-renewable-collector-station-protection.md)、[CASE-054 光伏防孤岛](../50-case/CASE-054-review-pv-anti-islanding-reverse-power.md)

## 5. 关联条目与变更记录

- 关联：[TH-029 微电网控制](TH-029-microgrid-control-and-grid-mode-switching.md)（计划孤岛 vs 非计划孤岛）、[TH-024 电力电子变换器与 PWM](TH-024-power-electronic-converters-and-pwm.md)（构网型 PCS 与 LVRT）、[TH-020 电力系统稳定性分类](TH-020-power-system-stability-classification.md)（频率稳定与低频减载协调）、[TH-012 保护四性](TH-012-protection-four-properties.md)、[PR-PE-001 继电保护配置](../30-practice/PR-PE-001-relay-protection-config.md)、[PR-ES-001 储能接入](../30-practice/PR-ES-001-energy-storage-integration.md)
- 下游案例：见 §4 列表。

| 版本 | 日期 | 修改内容 | 修改人 |
|---|---|---|---|
| 0.1 | 2026-09-09 | 创建；含防孤岛检测盲区、AFD 主动检测、LVRT 无功支撑公式、HVRT 新增要求、逆功率整定 | KB 管理员 |
