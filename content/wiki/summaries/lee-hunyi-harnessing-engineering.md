---
title: "李宏毅 — Harness Engineering：語言模型需要人類引導"
date: 2026-05-01
updated: 2026-05-01
type: summary
tags: [Harnessing Engineering, AI Agent, agents.md, 工具設計, Context Engineering]
sources: 1
status: stable
---

# 李宏毅 — Harness Engineering：語言模型需要人類引導

**來源：** [[Clippings/Harness Engineering：有時候語言模型不是不夠聰明，只是沒有人類好好引導.md]]  
**形式：** 課堂影片逐字稿｜NTU 生成式 AI 導論 2025（2026-04-13）  
**主講：** 李宏毅（台大機器學習課程教授）

> ⚠️ 這是第二份 Harnessing Engineering 素材，第一份見 [[wiki/summaries/harnessing-engineering]]（歡歡老師版本）。本頁著重李宏毅的補充視角，特別是實驗數據與工具設計面向。

---

## 核心主張

> 同樣的模型，多加幾行指令，能力可能天差地遠。  
> 今天語言模型不行，未必是模型不夠聰明，而是 Harness 沒做好。

---

## 核心概念

### Gemma 4 2B 實驗（關鍵案例）

用 2B 小模型修 bug：
- **沒有 Harness**：模型幻想 parser.py 內容，自己編造後說「做完了」
- **加 80 字 Harness 指令**：先 ls 看環境、cat 讀檔、修改、verify 通過，完整完成

結論：模型並不笨，它只是不知道 parser.py 就在腳邊。Harness 提供了人類直覺上的「環境感知」。

### AI Agent = LLM + Harness

```
AI Agent
├── LLM（Claude / GPT / Gemini / 本地模型）
└── Harness（支撐 LLM 完成任務的所有其他程式）
```

**Harness 的前身稱呼演進：**
- Prompt Engineering（改輸入影響輸出）
- Context Engineering（系統化自動建構 context）
- Harness Engineering（控制整個多輪互動過程）

三者有重疊，但 Harness Engineering 強調的是：多輪互動中讓任務被完成。

### 三種控制 Harness 的手段

| 控制目標 | 方式 | 舉例 |
|---------|------|------|
| **認知框架** | 人類語言規則（agents.md / CLAUDE.md） | 告訴模型環境、工作原則、完成標準 |
| **能力邊界** | 限制或開放模型可用工具 | OpenClaw 有 browser，Cowork 沙盒隔離 |
| **工作流程** | 指定模型嚴格遵守的程序 | Step 1 先 ls，Step 2 讀檔，Step 3 修改 |

### agents.md 的實際效果（論文數據）

**2025 年 1 月論文**（有/無 agents.md 比較）：
- agents.md 可縮短完成時間，特別對「邊緣困難任務」有幫助
- 但測量的是速度，非正確率

**2025 年 2 月論文**（正確率比較）：
- 沒有 agents.md：基準線
- 人類寫的 agents.md：不一定有效，在強模型上有時無顯著差異
- LLM 自己寫的 agents.md：多數情況比人類更差，甚至不如沒有

**結論**：我們目前還不太會寫 agents.md。這是研究中的開放問題。

### agents.md 設計原則（OpenAI Blog 引用）

- ❌ 百科全書式（把所有規則都塞進去）→ 佔滿 context，模型表現變差
- ✅ 地圖式（告訴模型「想知道什麼，去哪裡找」）

### CLAUDE.md = agents.md（遷移洞察）

從 OpenClaw 遷移到 Cowork/Claude Code：
```
只需把 agents.md 改名為 CLAUDE.md
```
兩個 harness 讀的啟動檔案不同，但邏輯完全一致。

### 工具設計：人類友善 ≠ Agent 友善

SWE-agent 論文（Agent-Computer Interface，ACI）的實驗結果：

**搜尋工具比較：**
- ❌ 分頁式搜尋（像 Google）：模型一直翻頁，塞滿 context，表現更差
- ✅ 帶摘要的搜尋：告訴模型找到哪些檔案，讓模型自己去開

**編輯工具比較：**
- ❌ 只有 edit 工具（指定行號修改）：模型看不到全貌，容易重複括號
- ✅ edit + linting（語法檢查）：分數從 15 分顯著提升

**Agent-first CLI 設計（Google Workspace 案例）：**
- 人類喜歡 flags（`--verbose`），agent 喜歡 JSON structure
- 未來的 CLI 要從設計起就考慮 agent 如何使用

---

## 相關 Wiki 頁

- [[wiki/ai-workflow/harnessing-engineering]] — 整合自本頁與歡歡老師版本的知識頁
- [[wiki/summaries/harnessing-engineering]] — 第一份素材（歡歡老師版本）
- [[wiki/concepts/ai-agent]] — AI Agent 架構基礎
