---
title: "Karpathy — From Vibe Coding to Agentic Engineering"
date: 2026-05-01
updated: 2026-05-01
type: summary
tags: [Agentic Engineering, Vibe Coding, Software 3.0, LLM, 知識管理]
sources: 1
status: stable
---

# Karpathy — From Vibe Coding to Agentic Engineering

**來源：** [[Clippings/Andrej Karpathy From Vibe Coding to Agentic Engineering.md]]  
**形式：** 演講逐字稿｜Sequoia Capital AI Ascent 2025（2026-04-29）  
**主講：** Andrej Karpathy（OpenAI 共同創辦人、Tesla AI 前負責人、Eureka Labs 創辦人）

---

## 核心主張

> Vibe Coding 提升了「門檻」讓所有人都能做軟體；  
> Agentic Engineering 則是在新工具下維持「品質上限」的工程紀律。

---

## 關鍵洞察

### Software 1.0 / 2.0 / 3.0 範式

| 版本 | 程式設計方式 | 本質 |
|------|------------|------|
| 1.0 | 寫程式碼 | 明確規則 |
| 2.0 | 標注資料集訓練神經網路 | 學習權重 |
| 3.0 | 撰寫 Prompt / 管理 Context Window | LLM 作為可程式化電腦 |

軟體 3.0 的「程式設計」是：**你給 LLM 的 context 就是你對它的指令**。複製貼上給 agent 的那段文字，就是 3.0 時代的程式碼。

### Vibe Coding vs Agentic Engineering

- **Vibe Coding**：提升底線，任何人都能快速做軟體；接受品質不完美
- **Agentic Engineering**：在 agent 工具下，仍然維持專業軟體的品質標準、安全性、可維護性

這是兩個不同的問題：一個在擴大「能做什麼」，另一個在維持「做得多好」。

### Jagged Intelligence（鋸齒狀智慧）

LLM 在可驗證域（數學、程式）表現驚人，在常識域卻出現荒謬錯誤（走路去洗車）。  
原因：
1. RL 訓練只在有明確 reward 的域有效（可驗證 = 飛快進步）
2. 實驗室選擇放進訓練資料的內容（chess 資料多 → chess 能力強）

結論：你必須主動探索你的應用「在哪個電路」——在 RL 電路裡你飛，不在就陷入泥淖。

### 人類仍需掌管的事

> "You can outsource your thinking but you can't outsource your understanding."

Agent 現在像資深實習生：執行力強，但會犯奇怪錯誤（如用 email 跨表關聯 Stripe/Google 帳號）。人類仍需掌管：
- **品味（Taste）**：什麼是好設計、好架構
- **規格（Spec）**：明確告訴 agent 要做什麼
- **理解（Understanding）**：不能外包的底層認知

### LLM Wiki 的背書

Karpathy 自己維護 LLM wiki，用它處理文章並提問。他的觀點：

> 每次看到對同一資料的不同投影，都能產生新洞察。這是增強理解的工具，不是取代理解。

這直接呼應 [[wiki/concepts/llm-wiki-pattern]] 的核心價值。

### Agent-first 基礎設施

他的抱怨：所有文件、服務、API 仍為人類設計，不是為 agent。他對未來的期待：
- 安裝說明 = 複製貼上給 agent 的文字
- CLI 工具 = agent-first（JSON structure 比 flags 更友善）
- 最終願景：給 prompt → agent 部署整個服務，人類不需要觸碰任何設定

---

## 相關 Wiki 頁

- [[wiki/concepts/agentic-engineering]] — 本次 ingest 衍生的新概念頁
- [[wiki/concepts/llm-wiki-pattern]] — Karpathy 直接背書
- [[wiki/concepts/ai-agent]] — agent 架構基礎
- [[wiki/ai-workflow/harnessing-engineering]] — 人類如何引導 LLM
