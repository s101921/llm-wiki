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

## [2026-04-15] lint | 發現 7 個問題，修復 5 個

- 🔴 **消失頁面（移除引用）**：`wiki/courses/harness-engineering-intro` 和 `wiki/courses/ai-lobster-intro` 從未真正寫入磁碟；從 `ai-agent.md`、`harnessing-engineering.md`、`index.md` 移除所有引用
- 🟡 **孤立頁面（已登記）**：`wiki/marketing/concept-visualizer/SKILL.md` 加入 index.md「行銷執行 Skills」區塊
- 🟡 **孤立頁面（Warren 自行處理）**：`wiki/marketing/USER_PREFERENCE_MODEL.md`（無 frontmatter，與 USER_DNA 重疊）
- 🟡 **type 錯誤（修復）**：`wiki/ai-workflow/claude-skills-audit.md` 從 `workflow` 改為 `ai-workflow`
- 🟢 **缺失連結（修復）**：`schedule-remote-agent.md` 和 `ccr.md` 各加入 `[[wiki/concepts/ai-agent]]` 反向連結
- 🟢 **index 統計（更新）**：頁面數 19→17，SKILL 數 6→7，工具數 3→4，移除 courses 區塊，更新成熟度分布

## [2026-04-10] ingest | Claude Code Remote (CCR) + Schedule Remote Agent

- 來源：與 Warren 的對話（測試 CCR 排程設定過程）
- 建立：[[wiki/tools/ccr]] — CCR 環境定義、能力、限制、瀏覽器替代方案
- 建立：[[wiki/ai-workflow/schedule-remote-agent]] — CCR 排程設定 SOP、Prompt 原則、常見錯誤排查
- 更新：[[wiki/tools/playwright-cli]] — 補充 CCR 不可用的限制與替代方案
- 更新：index.md（+2 頁面）

## [2026-04-29] ingest | Gemini Canvas 簡報生成 + LLM 互動式圖表流程

- 來源：inbox/（2 個待處理檔案）
- 建立：[[wiki/tools/gemini-canvas]] — Canvas 工具評估：Single-File Mandate、Canvas Block Syntax、防呆 Prompt 規範、PPTX 匯出相容性
- 建立：[[wiki/ai-workflow/llm-interactive-chart]] — CSV → 互動圖表三步 SOP（bash_tool Python 計算 → LLM 推理設計 → show_widget Chart.js 渲染）
- 更新：index.md（+2 頁面，素材數 7→9）
- inbox/ 已清空（兩個檔案均已 ingest）

## [2026-04-29] lint | 發現 6 個問題，修復 6 個

- 🔴 **連結格式錯誤（修復）**：`llm-interactive-chart.md` 中兩個連結有多餘 `.md` 後綴 → 已移除
- 🔴 **過期路徑（修復）**：`gemini-canvas.md` 和 `llm-interactive-chart.md` 中的 `inbox/` 連結已改為 `raw/`
- 🟡 **缺失交叉連結（修復）**：`gemini-canvas.md` 加入 `presentation-architect/SKILL` 和 `concept-visualizer/SKILL` 連結
- 🟡 **缺失交叉連結（修復）**：`llm-interactive-chart.md` 加入 `context-engineering-coding-agents` 連結
- 🟡 **缺失反向連結（修復）**：`ai-agent.md` 加入 `llm-interactive-chart` 作為 tool-use 實踐案例
- 🟡 **缺失反向連結（修復）**：`presentation-architect/SKILL.md` 加入 `gemini-canvas` 和 `concept-visualizer` 相關工具區塊
- 🟢 **新文章候選（登記）**：AI 視覺化輸出三路徑比較頁（gemini-canvas / presentation-architect / concept-visualizer）

## [2026-04-29] ingest | raw/ 批次處理（14 個檔案）

- 發現 raw/ 中有 15 個未處理檔案；本次處理 14 個（1 個因 Mac 編碼問題待處理）
- 建立 **7 個 concepts 頁面**：
  - [[wiki/concepts/multimodal-llm]] — 三元件架構、CLIP 對比學習、tokenization、直接 Embedding vs 先轉文字
  - [[wiki/concepts/code-execution-sandbox]] — 沙盒五大失敗原因、Prompt 提高成功率策略
  - [[wiki/concepts/web-search-hierarchy]] — 三層搜尋架構、Deep Research 六大限制、GEO 策略、動態爬蟲路線
  - [[wiki/concepts/computer-architecture]] — 七層架構、LLM 作為新 Shell、AI-Native OS 展望
  - [[wiki/concepts/automation-platform-vs-ai-agent]] — Make/n8n vs AI Agent 辯論；「管程式的能力」核心洞察
  - [[wiki/concepts/python-file-ecosystem]] — 六大格式類別與套件對應；膠水語言定位
  - [[wiki/concepts/presentation-generation-routes]] — 七條簡報生成路線；可編輯 PPTX 判斷標準
- 建立 **4 個 ai-workflow 頁面**：
  - [[wiki/ai-workflow/html-chart-export]] — Chart.js / ECharts / html2canvas 圖表下載 SOP
  - [[wiki/ai-workflow/google-api-integration]] — GCP + Google Sheets API + Gemini API 整合 SOP；Claude Code vs IDE/CLI 比較
  - [[wiki/ai-workflow/python-html-data-dashboard]] — Python + HTML 三層數據分析架構；LLM Data Agent 完整流程
  - [[wiki/ai-workflow/dynamic-web-scraping]] — 動態網站爬蟲三條路線 SOP
- 待處理：Mac 用戶 Python 開發環境教學指南.md（檔案編碼問題，無法讀取）
- 更新：index.md（總頁面 19 → 30，素材 9 → 22）

## [2026-04-29] lint | 新批次頁面掃描，發現 6 個孤立頁面，全部修復

- 🔴 **孤立頁面（修復）**：6 個新建頁面缺乏任何 wiki 內部連結
- 補上反向連結：
  - `ai-agent.md` → multimodal-llm, code-execution-sandbox, computer-architecture
  - `playwright-cli.md` → dynamic-web-scraping
  - `rag.md` → web-search-hierarchy
  - `harnessing-engineering.md` → automation-platform-vs-ai-agent, computer-architecture
  - `gemini-canvas.md` → presentation-generation-routes
  - `presentation-architect/SKILL.md` → presentation-generation-routes
  - `concept-visualizer/SKILL.md` → presentation-generation-routes（新增相關工具區塊）
