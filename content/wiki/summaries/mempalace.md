---
title: "MemPalace — AI 記憶系統"
date: 2026-04-08
updated: 2026-04-08
type: summary
tags: [記憶系統, RAG, 知識管理, MCP, 本地AI]
source_type: article
source_url: https://github.com/milla-jovovich/mempalace
source_file: "[[Clippings/milla-jovovichmempalace The highest-scoring AI memory system ever benchmarked. And it's free..md]]"
sources: 1
status: stable
---

# MemPalace — Milla Jovovich & Ben Sigman

**來源類型：** GitHub README（開源專案）
**作者：** Milla Jovovich & Ben Sigman
**發布日期：** 2026 年 4 月（v3.0.0）
**原始檔案：** [[Clippings/milla-jovovichmempalace The highest-scoring AI memory system ever benchmarked. And it's free..md]]

---

## 核心主張

AI 對話結束後記憶就消失了——MemPalace 的解法是**儲存一切原始對話，再用語意搜尋找回**，而非讓 AI 決定什麼值得記。在 LongMemEval 上達到 96.6% R@5（raw mode，零 API 呼叫）。

## 架構重點（Palace 隱喻）

- **Wing**：每個人或專案一個 wing
- **Room**：wing 內的主題分類（auth、billing…）
- **Hall**：室內走廊 = 記憶類型（facts / events / discoveries / preferences / advice）
- **Tunnel**：不同 wing 之間相同 room 的自動交叉連結
- **Closet**：指向原始內容的摘要索引
- **Drawer**：逐字儲存的原始對話（ChromaDB）

結構帶來的檢索提升：搜全部 60.9% → 加 wing 73.1% → 加 hall 84.8% → 加 room 94.8%（+34%）

## 誠實聲明（2026-04-07 作者更正）

社群在發布後數小時內發現問題，作者主動更正：

- AAAK「30x 無損壓縮」不實 — AAAK 是有損壓縮，小文本反而增加 token
- AAAK 模式在 LongMemEval 得 84.2%，低於 raw 模式的 96.6%
- 96.6% 的標題數字來自 **raw mode（ChromaDB 語意搜尋）**，非 AAAK
- 矛盾偵測（`fact_checker.py`）存在但尚未整合進主流程

## 技術細節

- 儲存：本地 ChromaDB（向量資料庫）
- 知識圖譜：SQLite 時序實體關係（類 Zep/Graphiti，但免費本地）
- MCP：19 個工具，與 Claude、ChatGPT、Cursor、Gemini 整合
- 安裝：`pip install mempalace`，無需 API key，無雲端

## 對 Wiki 的影響

- 建立：[[wiki/tools/mempalace]]
- 建立：[[wiki/concepts/rag]]（補充 RAG 概念頁）
- 建立：[[wiki/concepts/ai-memory-approaches]]（與 LLM Wiki Pattern 比較）
- 更新：[[wiki/concepts/llm-wiki-pattern]]（補充 MemPalace 作為對照案例）
