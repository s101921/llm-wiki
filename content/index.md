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
| [[wiki/ai-workflow/llm-interactive-chart]] | CSV → 互動圖表三步流程：bash_tool（Python 計算）→ LLM 推理設計 → show_widget（Chart.js 渲染） | 1 |
| [[wiki/ai-workflow/html-chart-export]] | HTML 圖表下載 SOP：Canvas API（Chart.js）/ ECharts toolbox / html2canvas DOM截圖；防透明背景、高解析度、CORS 陷阱 | 1 |
| [[wiki/ai-workflow/google-api-integration]] | Google Sheets API + Gemini API 整合 SOP：GCP 設定、服務帳戶、Claude Code 代理 vs 傳統 IDE/CLI 開發比較 | 2 |
| [[wiki/ai-workflow/python-html-data-dashboard]] | Python + HTML 數據儀表板架構：代碼執行分離模式、三種數據傳遞方案（變數替換/Jinja2/Streamlit）、LLM Data Agent 完整流程 | 2 |
| [[wiki/ai-workflow/dynamic-web-scraping]] | 動態網站爬蟲 SOP：三條路線（AJAX 接口/Playwright/ScraperAPI）、判斷動態網站方法、穩定性清單 | 1 |
| [[wiki/ai-workflow/mac-python-dev-setup]] | Mac Python 開發環境 SOP：venv 虛擬環境三情境、單一腳本/模組化/Jupyter 三種開發流派比較 | 1 |

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
| [[wiki/concepts/multimodal-llm]] | 多模態 LLM 架構：模態編碼器（CLIP 對比學習）+ 投影層（語意對齊）+ LLM 主幹；圖片/音訊 tokenization；直接 Embedding vs 先轉文字 | 1 |
| [[wiki/concepts/code-execution-sandbox]] | 程式碼執行沙盒：五大失敗原因（依賴庫缺失、I/O錯誤、超時、網路隔離、意圖判讀）；提高成功率的 Prompt 策略 | 1 |
| [[wiki/concepts/web-search-hierarchy]] | Web Search / Fetch / Deep Research 三層架構；Deep Research 六大資料限制；社群平台可見性；GEO 內容策略；動態爬蟲三條路線 | 3 |
| [[wiki/concepts/computer-architecture]] | 電腦系統七層架構（電壓→硬體→Firmware→Kernel→System Call→CLI/GUI→App）+ LLM 成為新超級 Shell；AI-Native OS 展望 | 1 |
| [[wiki/concepts/automation-platform-vs-ai-agent]] | Make/n8n vs AI Agent 存亡辯論：MCP 瓦解護城河（攻方）vs 維運盲區（守方）；結論：企業缺的是「管程式的能力」 | 1 |
| [[wiki/concepts/python-file-ecosystem]] | Python 檔案生態系：六大類格式（Office/圖表/數據/影像/音視訊/壓縮）與對應套件；膠水語言定位；二進制寫入 vs 模板渲染 | 1 |
| [[wiki/concepts/presentation-generation-routes]] | 簡報生成七條技術路線：可編輯 PPTX 的判斷標準、路線A-G 完整說明（截圖流/Reveal.js/python-pptx/pptxgenjs/Gemini Canvas/PPTAgent/WeasyPrint）| 1 |
| [[wiki/concepts/agentic-engineering]] | Vibe Coding vs Agentic Engineering；Software 3.0；Jagged Intelligence；「能外包思考，不能外包理解」（Karpathy 2026） | 1 |
| [[wiki/concepts/ai-native-product]] | AI-Native 產品開發：Research Preview 機制、剛剛好的 AGI Pill、PM 角色重定義、Eval 的重要性（Cat Wu / Anthropic） | 1 |

### 工具（wiki/tools/）

| 頁面 | 摘要 | 素材數 |
|------|------|--------|
| [[wiki/tools/mempalace]] | 本地 AI 記憶系統，Palace 結構 + ChromaDB，LongMemEval 96.6%，免費開源 | 1 |
| [[wiki/tools/hermes-agent]] | Nous Research 開源 Agent，四層記憶 + 學習循環 + Skills 自動生成，MIT 免費 | 1 |
| [[wiki/tools/playwright-cli]] | CLI 瀏覽器自動化，token-efficient，coding agent 首選；CLI vs MCP 決策框架；CCR 不可用 | 1 |
| [[wiki/tools/ccr]] | Claude Code Remote 雲端執行環境：能力、硬性限制、資料持久化方式、瀏覽器替代方案 | 0 |
| [[wiki/tools/gemini-canvas]] | Gemini Canvas HTML 簡報生成：Single-File Mandate、Canvas Block Syntax、防呆 Prompt 規範、PPTX 匯出相容性 | 1 |

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
| [[wiki/summaries/karpathy-vibe-coding-agentic-engineering]] | Karpathy — From Vibe Coding to Agentic Engineering（Sequoia AI Ascent 2026-04-29） | 演講逐字稿 |
| [[wiki/summaries/lee-hunyi-harnessing-engineering]] | 李宏毅 — Harness Engineering：語言模型需要人類引導（NTU 2026-04-13） | 課堂影片逐字稿 |
| [[wiki/summaries/cat-wu-ai-product-management]] | Cat Wu — Anthropic 如何比所有人都快（Lenny's Podcast 2026-04-23） | Podcast 逐字稿 |

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
| [[Clippings/Andrej Karpathy From Vibe Coding to Agentic Engineering.md]] | Karpathy — AI Ascent 2026 演講逐字稿 |
| [[Clippings/Harness Engineering：有時候語言模型不是不夠聰明，只是沒有人類好好引導.md]] | 李宏毅 — NTU 課堂影片逐字稿 |
| [[Clippings/How Anthropic's product team moves faster than anyone else  Cat Wu (Head of Product, Claude Code).md]] | Cat Wu — Lenny's Podcast 逐字稿 |

---

## 統計
- 總 wiki 頁面：36（13 概念、5 工具、10 摘要、10 ai-workflow、0 課程）+ 7 行銷 SKILL
- 已 ingest 素材：26（Clippings 全部處理完畢）
- 進行中專案：0
- Inbox 待處理：0
- 最後更新：2026-05-01

### 成熟度分布
| status | 數量 | 頁面 |
|--------|------|------|
| stable | 7 | 7 summaries |
| growing | 8 | 4 concepts（original）+ 4 tools（original）|
| draft | 16 | 7 concepts（new batch）+ 2 tools（ccr, gemini-canvas）+ 7 ai-workflow（llm-interactive-chart + new batch）|
