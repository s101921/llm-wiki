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

## [2026-04-10] lint | 發現 4 個問題，全部修復

- 🔴 **路徑錯誤（修復）**：`wiki/concepts/ai-memory-approaches.md` 被 7 個頁面引用為 `syntheses/`，全部改為 `concepts/`；index.md 移除 syntheses/ 區塊，改納入 concepts/ 下
- 🔴 **孤立頁面（修復）**：6 個 `wiki/marketing/` SKILL 頁面加入 index.md「行銷執行 Skills」區塊
- 🟡 **courses/ backlinks（修復）**：`wiki/concepts/ai-agent` 加入 ai-lobster-intro 反向連結；`wiki/ai-workflow/harnessing-engineering` 加入 harness-engineering-intro 反向連結
- 🟡 **playwright-cli 橫向連結（修復）**：在 `wiki/concepts/ai-agent` 工具相關段落加入 playwright-cli 入口

## [2026-04-10] ingest | playwright-cli — microsoft/playwright-cli GitHub README

- 來源：[[Clippings/microsoftplaywright-cli CLI for common Playwright actions...]]（GitHub README）
- 建立：[[wiki/summaries/playwright-cli]]
- 建立：[[wiki/tools/playwright-cli]]（CLI vs MCP 決策框架、token 效率、session 管理）
- 更新：[[wiki/ai-workflow/context-engineering-coding-agents]]（補充 CLI vs MCP 具體例子 + 反向連結）
- 更新：index.md（+2 頁面，+1 素材）

## [2026-04-10] ingest | Claude Skills 健檢 SOP（來自 inbox 示範）

- 來源：inbox 隨手筆記（Type A：直接觀察 + 可重複 SOP）
- 建立：[[wiki/ai-workflow/claude-skills-audit]]（type: workflow, status: draft）
- 更新：[[wiki/ai-workflow/harnessing-engineering]] — 加入 skills-audit 反向連結（層 2 工具系統）
- 更新：index.md（ai-workflow +1）

## [2026-04-10] schema-upgrade | 新增 playbooks/ 層

- 更新：CLAUDE.md — 新增 wiki/playbooks/ 目錄、type: playbook、Playbook 頁面格式規範
- 建立：wiki/playbooks/（含 README）
- 更新：index.md — 新增 Playbooks 區塊
- 更新：LLM Wiki 使用說明.docx

## [2026-04-10] schema-upgrade | 知識成熟度管道架構更新

- 更新：CLAUDE.md — 新增 `inbox/`、`projects/` 層、`status` frontmatter、Phase 0 Inbox Triage、Skill/Workflow 頁格式、專案知識頁格式
- 新增：`inbox/` 資料夾（零摩擦入口）
- 新增：`projects/` 資料夾（專案知識層）
- 批次更新：16 個 wiki 頁面加入 `status` 欄位（summaries → stable，其餘 → growing）
- 更新：index.md — 加入 inbox、projects 區塊；加入成熟度分布表

## [2026-04-09] course | AI 龍蝦是什麼？（one-pager，行銷人入門）

- 建立：[[wiki/courses/ai-lobster-intro]]（3 張 Marp 投影片）
- 同步存：Course/_outputs/ai-lobster-intro/slides.md
- 更新：index.md（+1 課程）

## [2026-04-09] course | Harness Engineering 行銷人一頁介紹（雙版本）

- 建立：[[wiki/courses/harness-engineering-intro]]（原始版 + 廚房概念版，Marp 格式）
- 同步存：Course/_outputs/harness-engineering-intro-outline.md
- 更新：index.md（新增課程知識分類）

## [2026-04-09] ingest | Harnessing Engineering — 歡歡老師，AI 秘密花園

- 來源：[[raw/AI 落地關鍵：什麼是 Harnessing Engineering？.md]]（影片逐字稿）
- 建立：[[wiki/summaries/harnessing-engineering]]
- 建立：[[wiki/ai-workflow/harnessing-engineering]]（三代演進、六層架構、Agent = Model + Harnessing）
- 更新：[[wiki/ai-workflow/context-engineering-coding-agents]]（補充 Harnessing 為更大框架的連結）
- 更新：[[wiki/concepts/ai-agent]]（補充 Harnessing Engineering 交叉連結）
- 更新：index.md（+2 頁面，+1 素材）

## [2026-04-09] ingest | Hermes Agent — Nous Research（替代方案有限公司）

- 來源：[[Clippings/Hermes Agent 是什麼？Nous Research 如何用「會記憶的 AI」改變遊戲規則？.md]]（文章，2026-04-05）
- 建立：[[wiki/summaries/hermes-agent-nous-research]]
- 建立：[[wiki/tools/hermes-agent]]（四層記憶、學習循環、Skills 系統）
- 更新：[[wiki/syntheses/ai-memory-approaches]]（改為五方案比較，加入程序記憶類型）
- 更新：[[wiki/concepts/ai-agent]]（補充 Hermes Agent 工具連結）
- 更新：[[wiki/tools/mempalace]]（補充 vs Hermes Agent 比較）
- 更新：index.md（+2 頁面，+1 素材）

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
