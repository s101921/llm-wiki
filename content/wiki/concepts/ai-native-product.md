---
title: AI-Native 產品開發
date: 2026-05-01
updated: 2026-05-01
type: concept
status: growing
tags: [AI Product, PM, 快速迭代, Research Preview, Product Taste, Evals]
sources: 1
---

# AI-Native 產品開發

**Anthropic Cat Wu 視角：在 AI 時代如何建產品、如何做 PM、什麼才是真正的快速迭代。**

---

## 核心原則

> 移除每一個 ship 的障礙。讓團隊裡每個人都能把想法在一週內送到用戶手上。

---

## AI-Native 產品的三個 Ship 快的核心機制

### 1. 具體目標替代 Roadmap

LLM 產品因為太通用，缺乏天然的邊界，容易陷入「我們在為誰建」的模糊狀態。

好的 goal 長這樣：
```
用戶：企業專業開發者
問題：permission prompt fatigue
Use case：讓企業開發者安全地達到零 permission prompt
```

這個目標會自動排除 80% 不合適的解法，讓工程師不需要等 PM 就能做決策。

### 2. Research Preview 機制

幾乎所有功能先以 **research preview** 標籤發布：
- 明確告訴用戶「這是早期產品、可能不長久支援」
- 降低承諾門檻 → 工程師週到週半就能 ship 一個想法
- 快速收到真實用戶回饋，再決定是否深化

### 3. 緊密跨職能流程（Evergreen Launch Room）

```
工程師 dogfood 完成
    → 發到 Evergreen Launch Room
    → Docs + PMM + DevRel 隔天完成公告
```

PM 的核心工作：建立這套機制，不是指揮每個功能。

---

## PM 角色的本質重定義

不再是「對齊多季度 roadmap」，而是：

**1. 設定方向**（模型能力不確定下，定義一個月後產品應長什麼樣）  
**2. 理解 harness 問題**（模型行為意外時，問它為什麼，找 prompt/harness 漏洞）  
**3. 找到信任的反饋者**（5 個能精準表達問題的用戶，勝過 500 個模糊回饋）  
**4. 寫 eval**（即使只有 10 個，也能量化目標與進展）

---

## 剛剛好的 AGI Pill 劑量

這是 Cat Wu 最強調的 PM 技能之一：

- ❌ **過度 AGI pilled**：設計「超強模型版」的產品，現在的模型還做不到
- ❌ **AGI 懷疑者**：低估當前模型，設計過多手把手引導
- ✅ **剛剛好**：知道當前模型在哪裡強、在哪裡弱，設計「幫用戶走到 golden path」的產品

做法：大量使用模型，問模型為什麼做了奇怪的決定 → 暴露 harness / prompt 的問題。

---

## 快速 ship 的代價

Cat Wu 誠實說了犧牲的東西：

**產品一致性（Product Consistency）：**  
當你每週都在 ship，不同功能之間的重疊、矛盾無可避免。用戶可能不知道「哪個方式才是最好的」。

解法：更多教育（如 `/powerup` 指令）；讓產品主動教用戶，而不是假設用戶會自己搞懂。

---

## Claude Code vs Desktop vs Cowork 的定位

Cat Wu 自己的分法：

| 工具 | 適合 |
|------|------|
| Claude Code CLI | Coding 任務，功能最新最完整 |
| Claude Code Desktop | 需要 UI 即時預覽；不熟 terminal 的人 |
| Web / Mobile | 外出時發起任務 |
| **Cowork** | **輸出不是 code 的任務**（deck、doc、email、Slack） |

Cowork 的最大價值：連接 Slack + Gmail + Google Drive → 夜間自動生產符合設計系統的投影片草稿。

---

## Anthropic 的成功方程式

1. **統一使命**（安全 AGI for humanity）= 讓跨部門決策極快，人人知道優先順序
2. **Focus** = 使命過濾不必要方向，不做 social、不做 feed
3. **Internal tooling**：Claude Code 降低了公司內部自建工具的門檻，各團隊建自己的 workflow

---

## 相關 Wiki 頁

- [[wiki/summaries/cat-wu-ai-product-management]] — 來源素材
- [[wiki/concepts/agentic-engineering]] — 工程師如何在 agent 時代工作
- [[wiki/concepts/ai-agent]] — Agent 架構基礎
- [[wiki/ai-workflow/harnessing-engineering]] — PM 需要理解 Harness 設計（Cat Wu 明確指出）
- [[wiki/tools/ccr]] — Cowork 的雲端環境
