---
title: MemPalace
date: 2026-04-08
updated: 2026-04-08
type: tool
tags: [記憶系統, RAG, 本地AI, MCP, ChromaDB, 開源]
sources: 1
---

# MemPalace

**開源記憶系統｜[github.com/milla-jovovich/mempalace](https://github.com/milla-jovovich/mempalace)｜免費（MIT）**

---

## 核心功能

用「宮殿記憶術」的隱喻組織 AI 對話記憶：Wings（人/專案）→ Rooms（主題）→ Closets（摘要索引）→ Drawers（逐字原文）。所有內容儲存在本地 ChromaDB，語意搜尋，零 API 呼叫。

**記憶分層（Memory Stack）：**

| 層 | 內容 | 大小 | 時機 |
|----|------|------|------|
| L0 | AI 身份設定 | ~50 tokens | 永遠載入 |
| L1 | 關鍵事實（AAAK 壓縮） | ~120 tokens | 永遠載入 |
| L2 | Room 回憶（近期對話） | 依需求 | 主題出現時 |
| L3 | 深度語意搜尋 | 依需求 | 明確查詢時 |

---

## 優缺點評估

**優點：**
- 完全本地，免費，無訂閱，資料不離機
- LongMemEval 96.6% R@5（raw mode）— 業界最高之一
- 19 個 MCP 工具，Claude/ChatGPT/Cursor 直接整合
- Palace 結構帶來 +34% 檢索準確率
- 時序知識圖譜（SQLite），可查「某日之前什麼是真的」

**缺點 / 注意事項：**
- AAAK 壓縮仍是實驗性，小文本無法省 token，且 LongMemEval 降至 84.2%
- 矛盾偵測（`fact_checker.py`）尚未整合進主流程
- v3.0.0 仍有已知 bug（macOS ARM64 segfault、ChromaDB 版本鎖定問題）
- 設計偏向對話記憶，不是知識合成

---

## 適合的教學場景

- 示範「AI 如何記住長期對話」——對比 context window 的限制
- 說明向量資料庫（ChromaDB）的實際應用
- 討論 AI 記憶的不同策略：RAG 檢索 vs 知識合成（見 [[wiki/syntheses/ai-memory-approaches]]）
- 討論 AI 產品發布透明度：作者主動公開更正過度聲明，是好案例

---

## 與其他工具比較

| 工具 | LongMemEval R@5 | API 需求 | 費用 |
|------|----------------|---------|------|
| **MemPalace (raw)** | **96.6%** | **無** | **免費** |
| Mastra | 94.87% | 需要（GPT）| API 費用 |
| Mem0 | ~85% | 需要 | $19–249/mo |
| Zep | ~85% | 需要 | $25+/mo |

---

## 相關素材

- [[wiki/summaries/mempalace]] — 完整 README 摘要
- [[wiki/syntheses/ai-memory-approaches]] — vs LLM Wiki Pattern
- [[wiki/concepts/rag]] — MemPalace 的底層檢索機制
