---
title: Agentic Engineering vs Vibe Coding
date: 2026-05-01
updated: 2026-05-01
type: concept
status: growing
tags: [Agentic Engineering, Vibe Coding, Software 3.0, 工程紀律, Jagged Intelligence]
sources: 1
---

# Agentic Engineering vs Vibe Coding

**Karpathy 於 2026 年在 Sequoia AI Ascent 提出的框架，解釋當前 AI 工程範式的兩個層次。**

---

## 核心區分

| | Vibe Coding | Agentic Engineering |
|--|------------|---------------------|
| **目標** | 提升底線（floor）——任何人都能做軟體 | 維持上限（ceiling）——專業軟體的品質標準 |
| **使用者** | 非程式人員，快速原型 | 專業工程師，需要品質、安全、可維護性 |
| **心態** | 接受不完美，先跑起來再說 | 不允許因為 vibe coding 引入漏洞 |
| **速度** | 極快，幾分鐘出原型 | 也很快，但帶著工程紀律 |

Karpathy：「10x 工程師的說法已經過時，agentic engineering 做好的人可以遠超 10x。」

---

## Software 3.0 框架

| 版本 | 如何「寫程式」|
|------|-------------|
| Software 1.0 | 寫程式碼（明確規則） |
| Software 2.0 | 標注資料集訓練神經網路（學習權重） |
| Software 3.0 | 撰寫 Prompt / 管理 Context Window（LLM 作為可程式化電腦） |

**實際意義：** 「給 agent 的那段複製貼上文字」就是 3.0 時代的程式碼。  
OpenClaw 的安裝方式 = 複製文字給 agent，比 bash script 更強大，因為 agent 有智慧，能看環境、debug、自適應。

---

## Jagged Intelligence（鋸齒狀智慧）

LLM 能力是不均勻的：

```
數學、程式碼（強 RL 信號） → 超強
↕
常識、空間推理（弱 RL 信號） → 荒謬錯誤
```

**經典例子：** Opus 4.7 能重構 10 萬行 codebase，卻說「洗車店 50 公尺，走路去」。

**為什麼 jagged：**
1. RL 訓練需要可量化的 reward，只在可驗證域（math, code）有效
2. 實驗室選擇放入的訓練資料（chess 資料多 → chess 能力強）

**對開發者的意義：** 你需要主動探索你的應用「在哪個電路」。
- 在 RL 電路裡（有大量訓練資料、可驗證域）→ 飛
- 不在電路裡 → 需要考慮 fine-tuning 或放棄

---

## 人類仍需掌管的三件事

1. **品味（Taste）**：什麼是好設計、好架構，代碼是否優雅
2. **規格（Spec）**：明確定義「要做什麼」，agents 不能獨立設計規格
3. **理解（Understanding）**：「可以外包思考，但不能外包理解」

> Karpathy: "You can outsource your thinking but you can't outsource your understanding."

當前 agents 仍像資深實習生：執行力強，但會做出奇怪的設計決定（如用 email 跨表關聯 Stripe/Google 帳號，而非用 user ID）。

---

## Agent-first 世界的到來

現有一切都為人類設計，正在逐漸重寫：

| 現在的問題 | Agent-first 的未來 |
|-----------|-------------------|
| 文件寫「請去這個 URL 操作」| 文件告訴你「複製這段給 agent」 |
| CLI 用 flags 設定 | CLI 接受 JSON structure（agent 更熟悉）|
| 部署需要人手動設 DNS、配服務 | 給 prompt → agent 完整部署 |

這與 [[wiki/ai-workflow/harnessing-engineering]] 的「Harness 要為 agent 設計」完全呼應。

---

## 如何招募 Agentic Engineers（Karpathy 的建議）

面試方式要改：不再是給算法題，而是：

> 讓應試者建一個完整大型專案（如 Twitter clone），要求：安全、功能完整，然後用 10 個 agents 嘗試攻擊它，看是否能守住。

這測試的是在 agent 工具下的真實工程能力。

---

## 相關 Wiki 頁

- [[wiki/concepts/ai-agent]] — AI Agent 架構基礎
- [[wiki/ai-workflow/harnessing-engineering]] — 如何用 Harness 引導 LLM
- [[wiki/summaries/karpathy-vibe-coding-agentic-engineering]] — 來源素材
- [[wiki/concepts/computer-architecture]] — Software 1.0/2.0/3.0 在七層架構中的位置
