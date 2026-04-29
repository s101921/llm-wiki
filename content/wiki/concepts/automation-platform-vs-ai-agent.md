---
title: Make / n8n vs AI Agent：自動化平台的存亡辯論
date: 2026-04-29
updated: 2026-04-29
type: concept
status: draft
tags: [make, n8n, zapier, automation, ai-agent, mcp, no-code]
sources: 1
private: false
---

# Make / n8n vs AI Agent：自動化平台的存亡辯論

**核心問題：AI 能寫程式後，傳統自動化平台（Make/n8n/Zapier）還有存在意義嗎？**

結論：**「企業缺的不是『寫程式的能力』，而是『管程式的能力』」**

## 攻方論點（AI Agent 會取代傳統平台）

### 1. 入口權轉移
Gartner 預測：70% 客服旅程起止於 AI 助手。使用者不再經過平台，中間層失去流量與商業模式。

### 2. MCP 瓦解連接器護城河
傳統平台靠「8000 個 API 整合數量」建立壁壘。現在服務商主動提供 MCP Server（Model Context Protocol），整合工作從平台轉移到服務商本身，連接器數量的護城河被平權化。

### 3. AI 直接「吃掉」流程
Klarna AI 客服取代 700 人省下 4000 萬美元 → AI 不是在優化流程，而是直接消滅了編排流程的需求。

## 守方論點（平台將進化為基礎設施）

### 1. 整合悖論（Agent 越多越難）
MuleSoft 數據：93% 企業部署 Agent，但 95% 困於數據整合。多 Agent 架構反而更需要穩定的編排與連接層。

### 2. 隱性維運成本陷阱
自建編排器（如 Airbyte/Checkr 的失敗案例）：省了訂閱費，卻背上「重試、超時、定時任務、狀態機」的巨大工程債。

### 3. 可觀測性 vs 責任邊界
AI 只能解決「事後日誌（Log）」；企業需要「事前約束（熔斷、審批、權限）」。
> 「迴紋針最大化器（Paperclip Maximizer）」原理：智能越強，越需要籠頭（控制邊界）。

## 雙方被迫承認的弱點

**攻方（AI Agent）承認：**
- 資料主權合規性不可替代
- 企業級「一鍵重放執行歷史」無法輕易被 AI 程式碼取代

**守方（傳統平台）承認：**
- 入口權確實正在遷移
- 無網路效應的輕平台（小型 Zapier 替代品）必死
- MCP 確實削弱了連接器數量的護城河

## 最終結論

### 什麼死了？
- No-code 的「行銷敘事」（「不用寫程式」這個賣點）
- 定位模糊的中間層平台

### 什麼活了？
- 託管式自動化**基礎設施**（調度 / 重試 / 合規 / 責任邊界打包服務）
- 有深度垂直整合（特定行業 SOP）的平台

### 核心洞察
> 企業真正缺的不是「寫程式的能力」，而是「**管程式的能力**」——監控、重試、審計、版控、熔斷，這些 AI 生成的程式碼本身無法自我管理。

## 與其他概念的關係

- [[wiki/concepts/ai-agent]] — AI Agent 是攻方的核心武器，tool-use 讓 Agent 能執行自動化任務
- [[wiki/ai-workflow/harnessing-engineering]] — Harnessing Engineering 就是「管程式的能力」的工程實踐

## 相關素材

- [[raw/AI 能寫程式了，Make 和 n8n 就該死了？我讓兩個 AI 辯了四輪.md]]
