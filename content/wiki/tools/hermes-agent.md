---
title: Hermes Agent
date: 2026-04-09
updated: 2026-04-09
type: tool
tags: [AI Agent, 記憶系統, 開源, Nous Research, Skills, 自我改進]
sources: 1
---

# Hermes Agent

**開源自我改進 AI Agent｜[github.com/NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)｜MIT 免費**

---

## 核心功能

Hermes Agent 的定位是「**會成長的 AI 頭腦**」，而非「每次對話完就忘記一切的工具」。

核心差異：**持久性（Persistence）+ 自我改進（Self-improvement）**。

### 四層記憶架構（Layered Memory Stack）

| 層 | 名稱 | 功能 | 類比 |
|----|------|------|------|
| 1 | Small Context | 工作記憶，快速讀取當前任務所需資訊 | 短期記憶 |
| 2 | Searchable History | 所有過往對話與任務的長期儲存，可隨時檢索 | 筆記本 |
| 3 | Optional Modeling | 建立使用者偏好與習慣模型，主動預測需求 | 心理模型 |
| 4 | Procedural Memory | 記住「如何做」而非「做了什麼」的可複用技能 | 肌肉記憶 |

### 內建學習循環（Built-in Learning Loop）

每次任務完成後，Agent 自動評估：
- 這次執行有什麼可以改進？
- 這個工作流程下次可以更有效率嗎？
- 有沒有從這次經驗中生成可複用的 Skill？

### Skills 系統

把成功的工作流程**自動封裝成可複用的 Skill**，下次遇到類似任務直接調用，且持續優化。

---

## 行銷應用場景

- **研究助理**：記住所有文獻回顧進度，跨 session 追蹤研究主題
- **獨立創業者**：了解你產品和客戶的 AI 助理，處理行銷內容、競品分析
- **企業內部知識庫**：本地部署保護商業機密，AI 隨著了解業務越來越有用

不適合：需要多頻道即時自動化（LINE/Discord/Telegram），這類場景選 OpenClaw。

---

## 效果評估

**優點：**
- 跨 session 記憶：完全支援，對話歷史不消失
- 自我改進能力：業界唯一內建學習循環的開源框架
- 模型無關：支援 400+ 模型（OpenAI、Anthropic、Google、Ollama）
- 部署輕量：$0（Ollama 本地）到 $5/月（VPS）

**限制：**
- v0.7.0 仍處快速迭代，API 可能隨版本調整
- 多頻道整合不及 OpenClaw
- 商業自動化功能較基礎

---

## 與其他記憶工具比較

| | Hermes Agent | MemPalace | OpenClaw |
|--|-------------|-----------|---------|
| **記憶類型** | 四層架構（含 Procedural） | Palace 結構（對話記憶） | 對話歷史持久化 |
| **學習能力** | 主動自我優化（Learning Loop） | 被動儲存 | 被動儲存 |
| **Skills 沉澱** | 自動生成 | 無 | 手動配置 |
| **LongMemEval** | 未公布 | 96.6% R@5 | 未公布 |
| **部署成本** | $0 起 | $0（本地） | 需付費方案 |
| **授權** | MIT | MIT | 專有 |

**選擇邏輯：**  
- 需要**深度個人化、會越用越懂你**的助理 → Hermes  
- 需要**逐字對話事實性回憶** → MemPalace  
- 需要**商業流程多頻道自動化** → OpenClaw

---

## 相關素材

- [[wiki/summaries/hermes-agent-nous-research]] — 完整文章摘要
- [[wiki/syntheses/ai-memory-approaches]] — 各記憶方案完整比較
- [[wiki/tools/mempalace]] — MemPalace 工具評估
- [[wiki/concepts/ai-agent]] — AI Agent 底層架構
