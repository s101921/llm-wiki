---
title: Harnessing Engineering
date: 2026-04-09
updated: 2026-05-01
type: ai-workflow
tags: [Harnessing Engineering, AI Agent, Context Engineering, Prompt Engineering, 落地, 穩定性, agents.md, 工具設計]
sources: 2
status: growing
---

# Harnessing Engineering

**讓 AI Agent 在真實世界穩定執行的系統工程——關注「如何讓模型別跑偏、跑得穩、出了錯還能拉回來」。**

---

## 核心邏輯

> **Agent = Model + Harnessing**  
> Harnessing = 除了模型本身以外，幾乎所有決定 Agent 能否穩定交付的東西。

Harnessing 的字面意思是「疆繩」「馬具」「約束裝置」——當模型從「回答問題」走向「執行任務」，系統不只要負責餵資訊，還要能**駕馭整個過程**。

---

## 三代 AI 工程演進

三者是**包含關係，不是替代關係**：

```
Harnessing Engineering（整個運行系統的工程化）
    ├── Context Engineering（輸入環境的工程化）
    │       └── Prompt Engineering（指令表達的工程化）
    └── + 工具系統、執行編排、記憶狀態、評估觀測、約束恢復
```

| | 解決的問題 | 適合場景 |
|--|-----------|---------|
| **Prompt Engineering** | 模型有沒有聽懂你說什麼？ | 單輪問答、創意生成 |
| **Context Engineering** | 模型有沒有拿到足夠正確的訊息？ | 需要外部知識的任務 |
| **Harnessing Engineering** | 模型在連續執行中能不能持續做對？ | 長鏈路、低容錯的真實 Agent |

---

## 六層架構

### 層 1：Context 管理

模型能不能穩定發揮，很多時候取決於它**看到了什麼**。

- 角色目標定義：模型要知道自己是誰、任務是什麼、成功標準是什麼
- 訊息拆解與選擇：上下文不是越多越好，而是**越相關越好**
- 結構化組織：固定規則 / 當前任務 / 任務狀態 / 外部證據，分層清楚

⚠️ 訊息一旦亂掉，模型就很容易漏重點、忘約束，甚至自我污染。

### 層 2：工具系統

工具讓模型能接觸真實世界（搜尋、讀文件、寫程式、調 API）。Harnessing 在這裡解決三個問題：

1. **給什麼工具**：工具太少限制能力；工具太多模型會亂用
2. **何時調用**：本來不需要查的時候別亂查；該查證的時候也別硬答
3. **工具結果怎麼餵回**：搜尋回來的幾十條結果，提煉、篩選再給模型，不要原封不動塞回去

### 層 3：執行編排

把任務步驟串起來。完整軌道：

```
理解目標 → 判斷訊息夠不夠（不夠補） → 分析 → 生成輸出 → 驗證輸出 → 不滿足則修正/重試
```

Agent 問題往往不是「某一步不會」，而是「不會把所有步驟串起來」。

### 層 4：記憶與狀態

沒有狀態管理的 Agent 每輪都像失憶：不知道自己做了什麼、哪些結論已確認、哪些問題還沒解決。

需要明確區分三類：

| 類型 | 說明 |
|------|------|
| 當前任務狀態 | 這一次任務執行到哪、有哪些中間結果 |
| 對話中間結果 | 這輪對話中已確認的事實 |
| 長期記憶與用戶偏好 | 跨 session 持久的知識和個人偏好 |

三類混在一起，系統會越來越亂。

### 層 5：評估與觀測

最容易被忽視的層。很多系統不是生成不出來，而是**生成完了不知道自己做得好不好**。

包括：
- 輸出驗收（Output Acceptance Criteria）
- 環境驗證（執行後的外部確認）
- 自動測試、日誌、指標
- 錯誤歸因（出了錯，找到根本原因）

### 層 6：約束、驗教、失敗恢復

真實環境裡，失敗是常態，不是例外（API 超時、文件格式混亂、模型誤解任務…）。

| 機制 | 說明 |
|------|------|
| **約束（Guardrails）** | 哪些能做，哪些不能做 |
| **驗教（Pre-flight Check）** | 輸出之前先檢查 |
| **恢復（Recovery）** | 失敗後：重試 / 切路徑 / 回滾到穩定狀態 |

---

## 比喻：派人去重要客戶拜訪

| 工程類型 | 你做了什麼 |
|---------|---------|
| Prompt Engineering | 把任務講清楚：「先問候、再提方案、再問需求、確認下一步」 |
| Context Engineering | 把資料給齊：客戶背景、過往溝通記錄、報價單、競品情況 |
| Harnessing Engineering | Check List + 關鍵節點實時匯報 + 會後錄音 + 發現偏差立即糾正 + 明確驗收標準 |

---

## 對 AI 落地的意義

> 同樣的模型，在不同系統下的表現差距可以非常大。真正決定能不能上線的可能是模型，但**真正決定能不能穩定交付的，是 Harnessing**。

AI 落地的核心挑戰，正在從「讓模型看起來更聰明」轉向「讓模型在真實世界裡穩定工作」。

---

## 與其他概念的關係

- [[wiki/ai-workflow/context-engineering-coding-agents]] — Harnessing 的子集：Context Engineering 在 Coding Agent 場景的實踐（Smart Zone、RPI、刻意壓縮）
- [[wiki/ai-workflow/claude-skills-audit]] — 層 2「工具系統」的實踐：Skills 過多反而讓模型亂用，定期健檢 SOP
- [[wiki/concepts/ai-agent]] — AI Agent 的底層機制（工具呼叫、記憶系統、心跳、Compaction）
- [[wiki/concepts/rag]] — 工具系統中的資訊檢索機制
- [[wiki/concepts/automation-platform-vs-ai-agent]] — Harnessing Engineering 是「管程式的能力」的工程方法論；Make/n8n vs AI Agent 的存亡辯論
- [[wiki/concepts/computer-architecture]] — 七層架構是理解 Harnessing Engineering 位置的基礎：LLM 正成為新一層 Shell

## 補充視角：李宏毅的 agents.md 實驗數據

（來源：[[wiki/summaries/lee-hunyi-harnessing-engineering]]）

### 核心示範：Gemma 4 2B 修 bug 實驗

同一個 2B 小模型：
- **無 Harness**：幻想 parser.py 內容，編造後說「做完了」
- **加 80 字 Harness 指令**：ls → cat 讀檔 → 修改 → verify 通過

**洞察：** 模型不是不夠聰明，它只是不知道 parser.py 就在腳邊。Harness 補上了「環境感知」。

### agents.md 的論文數據

**2025 年 1 月論文（速度）：**
- agents.md 可縮短任務完成時間，對邊緣困難任務幫助最明顯
- 未量測正確率

**2025 年 2 月論文（正確率）：**
- 人類寫的 agents.md：不穩定，在強模型上有時無顯著效果
- LLM 自己寫的 agents.md：多數情況比人類差，甚至不如沒有

**結論：我們目前還不太會寫 agents.md，是研究中的開放問題。**

### agents.md / CLAUDE.md 設計原則

- ❌ 百科全書式（把所有規則塞進去）→ 佔滿 context，表現反而變差
- ✅ 地圖式（告訴模型「想知道什麼，去哪裡找」）

**遷移洞察：** CLAUDE.md = agents.md  
OpenClaw 遷移到 Cowork 只需把 agents.md 改名 CLAUDE.md，agent 即復活。

### 工具設計：人類友善 ≠ Agent 友善

| 工具類型 | 人類感受 | Agent 表現 |
|---------|---------|----------|
| 分頁式搜尋（如 Google） | 直覺熟悉 | 一直翻頁塞滿 context，表現更差 |
| 帶摘要搜尋（給檔名，讓 agent 自己開） | 不直覺 | 最好 |
| Edit 工具（指定行號修改） | 精確 | 看不到全貌，容易加重複括號 |
| Edit + Linting | 稍複雜 | 分數顯著提升 |

**Agent-first CLI 原則（Google Workspace 案例）：**
- Agent 喜歡 JSON structure，不喜歡 flags
- 未來的工具要從設計起就考慮 agent 使用方式，而非「人能用，agent 剛好也能用」

---

## 相關素材

- [[wiki/summaries/harnessing-engineering]] — 影片摘要（歡歡老師版本）
- [[wiki/summaries/lee-hunyi-harnessing-engineering]] — 李宏毅版本（含論文數據、工具設計、Gemma 4 2B 實驗）
