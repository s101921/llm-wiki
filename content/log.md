---
title: Log
date: 2026-04-08
updated: 2026-04-08
type: log
---

# LLM Wiki — Log

> **只增不減**。每次操作結尾加一條記錄，格式：`## [YYYY-MM-DD] 操作類型 | 說明`
> 快速查看最近 5 筆：`grep "^## \[" log.md | tail -5`

---

## [2026-04-08] ingest | MemPalace — Milla Jovovich & Ben Sigman

- 來源：[[Clippings/milla-jovovichmempalace...]]（GitHub README，v3.0.0）
- 建立：[[wiki/summaries/mempalace]]
- 建立：[[wiki/tools/mempalace]]
- 建立：[[wiki/concepts/rag]]（補填缺失頁）
- 建立：[[wiki/syntheses/ai-memory-approaches]]（LLM Wiki Pattern vs MemPalace vs RAG）
- 更新：[[wiki/concepts/llm-wiki-pattern]]（補充 MemPalace 對照）
- 更新：index.md（+4 頁面，+1 素材）

## [2026-04-08] lint | 發現 3 個問題（0紅、1黃、2綠）

- 🟡 未 ingest：Clippings/milla-jovovichmempalace（MemPalace 記憶系統）
- 🟢 缺失頁面：[[RAG]]（被 llm-wiki-pattern 引用但未建立）
- 🟢 建議深挖：MemPalace vs LLM Wiki Pattern 比較（syntheses/）

## [2026-04-08] ingest | LLM Wiki — Andrej Karpathy

- 來源：[[Clippings/llm-wiki]]（GitHub Gist）
- 建立：[[wiki/summaries/llm-wiki-karpathy]]
- 建立：[[wiki/concepts/llm-wiki-pattern]]
- 更新：index.md（+2 頁面，+1 素材）

## [2026-04-08] setup | Vault 初始化完成

- 建立完整目錄結構（Clippings/, raw/, wiki/, Templates/）
- 撰寫 CLAUDE.md schema（含 ingest / query / lint 工作流程）
- 建立 index.md 與 log.md
- 建立 5 個 Templates（概念頁、工具頁、人物頁、素材摘要頁、每日筆記）
- 架構基於 LLM Wiki pattern by Andrej Karpathy
