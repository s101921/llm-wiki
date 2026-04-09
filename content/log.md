---
title: Log
date: 2026-04-08
updated: 2026-04-08
type: log
---

# LLM Wiki — Log

> **只增不減**。格式：`## [YYYY-MM-DD] 操作類型 | 說明`
> 快速查看最近 5 筆：`grep "^## \[" log.md | tail -5`

---

## [2026-04-09] ingest | No Vibes Allowed — Dex Horthy, HumanLayer

- 來源：[[Clippings/No Vibes Allowed Solving Hard Problems in Complex Codebases – Dex Horthy, HumanLayer.md]]（AI Engineer 2025 演講逐字稿）
- 建立：[[wiki/summaries/no-vibes-allowed-dex-horthy]]
- 建立：[[wiki/ai-workflow/context-engineering-coding-agents]]（Smart Zone、RPI、Compaction、Sub-agents、Mental Alignment）
- 更新：[[wiki/concepts/ai-agent]]（補充與 Context Engineering 頁面的交叉連結）
- 更新：index.md（+2 頁面，+1 素材）

## [2026-04-08] ingest | 解剖小龍蝦 — 李宏毅 AI Agent 影片

- 來源：[[Clippings/解剖小龍蝦 — 以 OpenClaw 為例介紹 AI Agent 的運作原理.md]]（YouTube 逐字稿，2026-03-09）
- 建立：[[wiki/summaries/hung-yi-lee-openclaw-agent]]
- 建立：[[wiki/concepts/ai-agent]]（工具呼叫、記憶、心跳、Cron Job、Compaction）
- 更新：[[wiki/concepts/rag]]（補充 Agent 記憶中的 RAG 應用）
- 更新：[[wiki/syntheses/ai-memory-approaches]]（改為四方比較）
- 更新：index.md（+2 頁面，+1 素材）

## [2026-04-08] ingest | MemPalace — Milla Jovovich & Ben Sigman

- 來源：[[Clippings/milla-jovovichmempalace...]]（GitHub README，v3.0.0）
- 建立：[[wiki/summaries/mempalace]]
- 建立：[[wiki/tools/mempalace]]
- 建立：[[wiki/concepts/rag]]（補填缺失頁）
- 建立：[[wiki/syntheses/ai-memory-approaches]]
- 更新：[[wiki/concepts/llm-wiki-pattern]]（補充 MemPalace 對照）
- 更新：index.md（+4 頁面，+1 素材）

## [2026-04-08] lint | 發現 3 個問題（0紅、1黃、2綠）

- 🟡 未 ingest：Clippings/milla-jovovichmempalace（MemPalace 記憶系統）
- 🟢 缺失頁面：[[wiki/concepts/rag]]（被 llm-wiki-pattern 引用但未建立）
- 🟢 建議深挖：MemPalace vs LLM Wiki Pattern 比較（syntheses/）

## [2026-04-08] setup | 完整重構：AI 行銷顧問 + 課程講師架構

- 重寫 CLAUDE.md：對齊 Karpathy 四階段架構（Ingest/Compile/Query/Lint）
- 補齊遺漏概念：Derived Outputs、跨連結生成、Lint 循環、Web 搜尋補缺
- 更新 wiki 次項：strategy / copy / ads / creative / content / analytics / ai-workflow / courses / clients / cases
- 建立 10 個新資料夾
- 更新 index.md 反映新結構

## [2026-04-08] ingest | LLM Wiki — Andrej Karpathy

- 來源：[[Clippings/llm-wiki]]（GitHub Gist）
- 建立：[[wiki/summaries/llm-wiki-karpathy]]
- 建立：[[wiki/concepts/llm-wiki-pattern]]
- 更新：index.md（+2 頁面，+1 素材）

## [2026-04-08] setup | Vault 初始化

- 建立初始目錄結構與 Templates
- 架構基於 LLM Wiki pattern by Andrej Karpathy
