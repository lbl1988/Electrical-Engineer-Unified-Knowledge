---
id: CASE-064
title: 事故复盘：数据中心精密空调故障叠加 ATS 切换时序错误，服务器高温停机 45 min
domain: CASE
subdomain: AC
case_type: accident
year_source: 2024
desensitized: true
voltage_levels: [LV, MV]
lifecycle: [运维]
standards:
  - { code: GB 50174-2017, clause: "第8章", note: "数据中心设计规范：供配电与空调" }
  - { code: TIA-942-Tier, clause: "Tier III", note: "Standard for Data Center Centers（等级标准）" }
  - { code: IEEE 446-2018, clause: "第6章", note: "Design Guide for Emergency and Standby Power Systems（ATS 配合）" }
status: draft
reviewers: []
version: 0.1
updated: 2026-09-10
---

# 事故复盘：数据中心精密空调故障 + ATS 切换时序错误 → 服务器高温停机

## 1. 摘要

某 Tier III 数据中心（1500 机柜，IT 负荷 2.4 MW）**2N UPS 之一故障 → ATS 切换到柴发 → 精密空调供电回路未跟随切换（接线错接在故障 UPS 侧）→ 精密空调停机 12 min → 机房 1 温度超过 32°C（阈值 27°C）→ 210 台服务器自动关机保护**，业务中断 45 min，直接经济损失 340 万元。**根因**：精密空调供电未按 2N 冗余设计（只接在一路 UPS）；ATS 切换时序未与精密空调联动（UPS-2 故障后空调回路未自动投柴发）；温度监控阈值设为 35°C（应 30°C 预警 + 27°C 切换预案）。

## 2. 事故时序

| 时间 | 事件 | 关键参数 |
|---|---|---|
| 23:08 | UPS-2 发生可控硅短路故障 | 系统告警 |
| 23:08 | ATS 自动切换到柴发 | 切换时间 18 ms |
| 23:08 | 精密空调（3 台 × 200 kW）失电 | 接在 UPS-2 母线侧 |
| 23:20 | 机房 1 温度升至 31°C | 12 min 温升 4°C（初始 27°C） |
| 23:25 | 温度超阈值 35°C，服务器自动关机 | 210 台（占总数 14%） |
| 23:28 | 运维发现空调失电，手动切柴发侧 | 空调重启延迟 20 min |
| 23:45 | 机房温度降至 26°C，服务器逐步开机 | 业务恢复 45 min |

## 3. 直接损失

| 项目 | 数量 | 说明 |
|---|---|---|
| 业务中断 | 45 min | 金融交易 + 电商后台 |
| 服务器损坏 | 12 台 | 过温击穿 |
| SLA 赔付 | 约 280 万 | 客户协议 |
| 应急供电 | 约 60 万 | 柴油发电车 |
| **合计** | | **约 340 万元** |

## 4. 原因分析

### 4.1 直接原因

精密空调接线错误（接在 UPS-2 母线而非 ATS 后端公共母线）→ UPS-2 故障后空调失电。

### 4.2 间接原因

| 漏洞 | 根因 | 标准要求 |
|---|---|---|
| **空调未按 2N 设计** | 3 台精密空调都接在 UPS-2 侧，未形成双路供电 | GB 50174-2017 Tier III 要求关键负荷双路 |
| **ATS 切换未联动空调** | 只切换了服务器母线，空调回路单独 | IEEE 446 要求 ATS 联动关键辅助设备 |
| **温度阈值过高** | 35°C 关机、32°C 预警（应 27°C 预警 + 26°C 自动切预案） | TIA-942 推荐 27°C 最佳运行温度 |
| **运维巡检盲区** | 夜间仅每 4 小时巡检一次，无视频监控 | 关键机房应 24/7 在线监控 |

### 4.3 引用上游条目

- [PR-DD-007 数据中心配电深化](../30-practice/PR-DD-007-data-center-power-distribution-deepening.md) — Tier III 配电 + 2N UPS
- [PR-PS-003 UPS 配置](../30-practice/PR-PS-003-ups-and-battery-design.md) — UPS 冗余设计
- [CALC-BT-002 UPS 后备时间](../40-calc/CALC-BT-002-ups-battery-autonomy.md) — UPS 容量核算
- [TH-009 雷电物理](../10-theory/TH-009-lightning-physics.md) — UPS 浪涌保护

## 5. 整改措施

| 措施 | 费用 | 工期 |
|---|---|---|
| 精密空调加柴发侧供电回路（改接线 + 加 ATS） | 约 18 万 | 2 天 |
| 空调温度阈值调整：26°C 预警 / 30°C 告警 / 32°C 停机 | 0（参数） | 1 天 |
| 机房温度视频监控系统（3 台红外摄像头） | 约 22 万 | 5 天 |
| UPS-2 返厂维修 + 预防性维护加强 | 约 85 万 | 14 天 |
| **合计** | **约 125 万** | |

## 6. 经验教训

1. **数据中心的辅助设备（空调）比主设备（服务器）更重要**——服务器有 UPS 撑 15~30 min，但机房温度上升 1°C/min，精密空调停 10 min 就超阈值
2. **ATS 切换必须联动关键辅助负荷**——GB 50174 附录 D 明确要求 ATS 切换时同步切换精密空调、照明、消防
3. **温度预警阈值不能等到 35°C**——IT 行业最佳实践是：26°C 发预警、30°C 启动备用空调、32°C 强制切业务，比一般工业标准高

## 7. 关联条目

- 上游：[PR-DD-007 数据中心配电](../30-practice/PR-DD-007-data-center-power-distribution-deepening.md) — Tier III 标准
- 上游：[PR-PS-003 UPS 配置](../30-practice/PR-PS-003-ups-and-battery-design.md) — 2N 设计原则
- 关联：[CASE-063 配电网大面积停电](CASE-063-accident-distribution-grid-large-outage.md) — 本例如果配网停电，柴发切换后空调必须立即跟随

## 8. 变更记录

| 版本 | 日期 | 修改 |
|---|---|---|
| 0.1 | 2026-09-10 | 首批 |
