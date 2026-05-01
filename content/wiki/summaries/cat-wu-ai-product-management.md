---
title: "Cat Wu — Anthropic 如何比所有人都快"
date: 2026-05-01
updated: 2026-05-01
type: summary
tags: [AI Product, PM, Claude Code, Cowork, Anthropic, 快速迭代]
sources: 1
status: stable
---

# Cat Wu — Anthropic 如何比所有人都快

**來源：** [[Clippings/How Anthropic's product team moves faster than anyone else  Cat Wu (Head of Product, Claude Code).md]]  
**形式：** Podcast 逐字稿｜Lenny's Podcast（2026-04-23）  
**主講：** Cat Wu（Anthropic Claude Code + Cowork Head of Product）

---

## 核心主張

> 不是因為有最好的模型，而是因為流程極度低摩擦、每個人都有能力從想法直接到產品。

---

## Anthropic 快速 ship 的三個關鍵

### 1. 設定清楚目標

LLM 太通用，導致「我們在為誰建」極度模糊。好 PM 能具體說出：
- 主要使用者是誰（professional developers）
- 要解決的問題是什麼（permission prompt fatigue）
- 定義清楚的 use case（企業開發者安全地達到零 permission prompt）

這個清楚的 goal 會自動排除大量不合適的解法。

### 2. Research Preview 機制

幾乎所有功能先以 **research preview** 發布：
- 明確標示「這是早期產品、可能不長久支援」
- 降低承諾門檻 → 一週內即可 ship
- 快速拿到真實回饋，再決定是否深化

### 3. 跨職能緊密流程

工程師 → Evergreen Launch Room → Docs + PMM + DevRel 隔天完成公告

PM 的核心工作是**建立這套機制**，讓任何工程師的任何想法都有一條清楚的快速通道到用戶手上。

---

## PM 角色的本質轉變

| 過去（slow era）| 現在（AI era）|
|----------------|--------------|
| 協調跨部門多季度 roadmap | 找到最快把想法送到用戶手上的路徑 |
| 強調流程對齊 | 強調移除每一個 ship 的障礙 |
| PRD 驅動 | 清楚 goal + metrics + team principles 驅動 |
| 6 個月 sprint | 有時候一天一個功能 |

PRD 仍然存在，但只用於特別模糊或需要長期基礎設施的功能。

---

## PM 的新核心技能

Cat Wu 列出她在招聘時最看重的能力：

1. **定義一個月後的產品應該長什麼樣**（在模型能力快速變化中設方向）
2. **剛剛好的 AGI pill 劑量**：不過度設計「超強模型版」，也不低估當前模型能力
3. **理解 harness 的問題**：當模型行為意外，問它為什麼 → 找到 prompt / harness 的漏洞
4. **Product taste**：程式碼越來越便宜，「決定要寫什麼」越來越值錢
5. **寫 eval**：即使只有 10 個，也能幫團隊量化目標與進展

---

## Claude Code / Cowork / Desktop 的使用時機

Cat Wu 自己的分法：

| 工具 | 適用場景 |
|------|---------|
| **Claude Code CLI** | 一次性 coding 任務，功能最新最完整 |
| **Claude Code Desktop** | 需要看 UI 即時預覽；給不熟悉 terminal 的人 |
| **Web / Mobile** | 在外出時發起任務（不需要 laptop） |
| **Cowork** | 輸出不是 code 的任務（deck、doc、email、Slack） |

Cowork 的最大優勢：連結 Slack + Gmail + Google Drive 後，能在夜間自動跑幾小時、產出符合 Anthropic 設計系統的投影片草稿。

---

## Anthropic 成功的兩個關鍵

1. **統一使命**（安全 AGI for humanity）：讓跨部門決策極快，每個人都知道優先順序
2. **Focus**：不做 social network，不做資訊 feed——使命過濾掉所有不必要的方向

---

## 人類在 AI 時代仍然不可缺的能力

- **品味（Taste）**：決定什麼值得建、怎麼建
- **常識 EQ**：知道所有 stakeholder 是誰、如何溝通、什麼是正確的 venue
- **優先順序判斷**：合成大量資訊後做出選擇（這個 Cowork 幫你收集，你負責決定）

---

## 相關 Wiki 頁

- [[wiki/concepts/ai-native-product]] — 本次 ingest 衍生的新概念頁
- [[wiki/concepts/ai-agent]] — Agent 架構基礎
- [[wiki/tools/ccr]] — Cowork 相關
