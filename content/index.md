---
title: Index
date: 2026-04-08
updated: 2026-04-10
type: index
---

# LLM Wiki — Index

> 每次操作後 LLM 必須更新此文件。查詢時先讀這裡找相關頁面，再深入讀取個別頁面。

---

## Inbox（待處理）

> 丟在這裡的筆記尚未分類，Lint 時處理。

_目前無待處理項目_

---

## 進行中專案（projects/）

> 只記知識與學習，程式碼留在原目錄。

_目前無進行中專案_

---

## Playbooks — 多 Skill 組合流程（wiki/playbooks/）

> 串聯多個 skill 的完整行銷執行流程（marketing plugins）。跑任務時讓 LLM 讀這裡。

_尚無 Playbook_

---

## 行銷知識

### 策略（wiki/strategy/）
_尚無頁面_

### 文案（wiki/copy/）
_尚無頁面_

### 廣告投放（wiki/ads/）
_尚無頁面_

### 創意素材（wiki/creative/）
_尚無頁面_

### 內容（wiki/content/）
_尚無頁面_

### 數據分析（wiki/analytics/）
_尚無頁面_

### AI 工作流（wiki/ai-workflow/）

| 頁面 | 摘要 | 素材數 |
|------|------|--------|
| [[wiki/ai-workflow/context-engineering-coding-agents]] | Coding Agent context 管理：Smart Zone、RPI、刻意壓縮、Sub-agent、Mental Alignment | 1 |
| [[wiki/ai-workflow/harnessing-engineering]] | AI 落地六層架構：Agent = Model + Harnessing；工具系統、執行編排、記憶狀態、評估觀測、失敗恢復 | 1 |
| [[wiki/ai-workflow/claude-skills-audit]] | Claude Skills 健檢 SOP：過多 Skill 反而讓模型亂用；四類問題（重複、模糊、衝突、沒用）判斷與刪改邏輯 | 0 |
| [[wiki/ai-workflow/schedule-remote-agent]] | CCR 排程 Remote Agent 設定 SOP：建立 trigger、Prompt 撰寫原則、GitHub/Notion 整合、常見錯誤排查 | 0 |

---

## 課程知識（wiki/courses/）

_尚無頁面_

---

## 方法論與框架（wiki/concepts/）

| 頁面 | 摘要 | 素材數 |
|------|------|--------|
| [[wiki/concepts/llm-wiki-pattern]] | LLM Wiki 方法論，vs RAG 的核心差異，三層架構 | 1 |
| [[wiki/concepts/rag]] | Retrieval-Augmented Generation — 向量檢索，每次查詢重新推導；Agent 記憶底層機制 | 2 |
| [[wiki/concepts/ai-agent]] | AI Agent 架構：工具呼叫、記憶系統、心跳、Cron Job、Context Compaction；以 OpenClaw 為例 | 1 |
| [[wiki/concepts/ai-memory-approaches]] | AI 記憶五方案比較：RAG / AI Agent 記憶 / MemPalace / Hermes Agent / LLM Wiki Pattern（綜合分析）| 4 |

### 工具（wiki/tools/）

| 頁面 | 摘要 | 素材數 |
|------|------|--------|
| [[wiki/tools/mempalace]] | 本地 AI 記憶系統，Palace 結構 + ChromaDB，LongMemEval 96.6%，免費開源 | 1 |
| [[wiki/tools/hermes-agent]] | Nous Research 開源 Agent，四層記憶 + 學習循環 + Skills 自動生成，MIT 免費 | 1 |
| [[wiki/tools/playwright-cli]] | CLI 瀏覽器自動化，token-efficient，coding agent 首選；CLI vs MCP 決策框架；CCR 不可用 | 1 |
| [[wiki/tools/ccr]] | Claude Code Remote 雲端執行環境：能力、硬性限制、資料持久化方式、瀏覽器替代方案 | 0 |

### 行銷執行 Skills（wiki/marketing/）

> 執行層工具，LLM 可直接使用。知識萃取待評估。

| SKILL | 用途 |
|-------|------|
| [[wiki/marketing/brand-visual-architect/SKILL]] | 從品牌設計圖片萃取視覺基因，建立 Brand Visual Guidebook + AI 生圖 Prompt 公式 |
| [[wiki/marketing/image-prompt-generator/SKILL]] | 四維度風格框架（光譜 × 用途 × 情緒 × 平台）→ AI 圖片 Prompt |
| [[wiki/marketing/creative-idea-generator/SKILL]] | 從產品/品牌發展廣告創意概念 → 視覺概念卡（可銜接 image-prompt-generator）|
| [[wiki/marketing/course-brand-customizer/SKILL]] | 為課程客製化品牌提示詞，替換公版筆記並存至 Notion |
| [[wiki/marketing/presentation-architect/SKILL]] | 主題 → 完整簡報規格（YAML + Slidev 程式碼 + AI 圖片 Prompt）|
| [[wiki/marketing/strong-constraint-prompt-optimizer/SKILL]] | 弱 Prompt → 強約束語法（特徵鎖定、環境匹配、隨機抑制）|
| [[wiki/marketing/concept-visualizer/SKILL]] | 知識視覺化：任何概念 → PPTX（5 版型，Warren 品牌色，HTML→WeasyPrint→PPTX 管線）|

---

## 客戶知識（wiki/clients/）— 私人
_尚無頁面_

## 案例覆盤（wiki/cases/）— 私人
_尚無頁面_

---

## 原始素材摘要（wiki/summaries/）

| 頁面 | 來源 | 類型 |
|------|------|------|
| [[wiki/summaries/llm-wiki-karpathy]] | Andrej Karpathy — LLM Wiki | 文章 |
| [[wiki/summaries/mempalace]] | Milla Jovovich & Ben Sigman — MemPalace GitHub README | 文章 |
| [[wiki/summaries/hung-yi-lee-openclaw-agent]] | 李宏毅 — 解剖小龍蝦（YouTube，2026-03-09） | 影片逐字稿 |
| [[wiki/summaries/no-vibes-allowed-dex-horthy]] | Dex Horthy — Context Engineering for Coding Agents（AI Engineer 2025） | 演講逐字稿 |
| [[wiki/summaries/hermes-agent-nous-research]] | 替代方案有限公司 — Hermes Agent 介紹（2026-04-05） | 文章 |
| [[wiki/summaries/harnessing-engineering]] | 歡歡老師 — AI 落地關鍵：什麼是 Harnessing Engineering？ | 影片逐字稿 |
| [[wiki/summaries/playwright-cli]] | microsoft/playwright-cli — CLI vs MCP 取捨、token 效率、session 機制 | GitHub README |

---

## 原始素材（Clippings/ & raw/）

| 檔案 | 說明 |
|------|------|
| [[Clippings/llm-wiki]] | LLM Wiki pattern 原文（Karpathy，GitHub Gist）|
| [[Clippings/milla-jovovichmempalace The highest-scoring AI memory system ever benchmarked. And it's free..md]] | MemPalace README（v3.0.0，2026-04）|
| [[Clippings/解剖小龍蝦 — 以 OpenClaw 為例介紹 AI Agent 的運作原理.md]] | 李宏毅 — AI Agent 運作原理影片逐字稿（2026-03-09）|
| [[Clippings/No Vibes Allowed Solving Hard Problems in Complex Codebases – Dex Horthy, HumanLayer.md]] | Dex Horthy — Context Engineering 演講逐字稿（AI Engineer 2025）|
| [[Clippings/Hermes Agent 是什麼？Nous Research 如何用「會記憶的 AI」改變遊戲規則？.md]] | 替代方案有限公司 — Hermes Agent 介紹（2026-04-05）|
| [[raw/AI 落地關鍵：什麼是 Harnessing Engineering？.md]] | 歡歡老師 — Harnessing Engineering 影片逐字稿 |
| [[Clippings/microsoftplaywright-cli CLI for common Playwright actions. Record and generate Playwright code, inspect selectors and take screenshots..md]] | microsoft/playwright-cli GitHub README |

---

## 統計
- 總 wiki 頁面：17（4 概念、4 工具、7 摘要、4 ai-workflow、0 課程）+ 7 行銷 SKILL
- 已 ingest 素材：7
- 進行中專案：0
- Inbox 待處理：0
- 最後更新：2026-04-15

### 成熟度分布
| status | 數量 | 頁面 |
|--------|------|------|
| stable | 7 | 7 summaries |
| growing | 8 | 4 concepts + 4 tools |
| draft | 2 | 2 ai-workflow（ccr, schedule-remote-agent）|
