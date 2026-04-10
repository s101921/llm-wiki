---
title: "Hermes Agent — Nous Research 會記憶的 AI"
date: 2026-04-09
updated: 2026-04-09
type: summary
tags: [AI Agent, 記憶系統, 開源, Nous Research, Skills]
sources: 1
status: stable
---

# Hermes Agent — Nous Research 會記憶的 AI

**來源：** [[Clippings/Hermes Agent 是什麼？Nous Research 如何用「會記憶的 AI」改變遊戲規則？.md]]  
**發布：** 2026-04-05｜替代方案有限公司

---

## 核心主張

> 傳統 AI 助理每次對話完就忘記一切；Hermes Agent 是第一個讓開源 AI Agent 具有**持久性（Persistence）與成長能力**的框架。

公式：**「learns your projects, builds its own skills, and reaches you wherever you are.」**

---

## 五大核心特色

### 1. 四層記憶系統（Layered Memory Stack）

| 層 | 名稱 | 功能 | 類比 |
|----|------|------|------|
| 1 | Small Context | 工作記憶，快速讀取當前任務 | 短期記憶 |
| 2 | Searchable History | 所有過往對話與任務，可隨時檢索 | 筆記本 |
| 3 | Optional Modeling | 建立使用者偏好模型，主動預測需求 | 心理模型 |
| 4 | Procedural Memory | 記住「如何做」，可複用的技能記憶 | 肌肉記憶 |

### 2. 內建學習循環（Built-in Learning Loop）

每次完成任務後自動評估：「這次可以更有效率嗎？有可複用的技能嗎？」→ 從每次執行中持續優化。

### 3. Skills 系統

把成功的工作流程**自動封裝成可複用的 Skill**，下次遇到類似任務直接調用，不需要重新解釋。

### 4. 模型無關（Model Agnostic）

支援 400+ 模型：OpenAI、Anthropic、Google、Ollama，以及 Nous Portal 一站式訪問。

### 5. 輕量部署

| 方式 | 成本 |
|------|------|
| Ollama 本地 | $0 |
| $5 VPS | $5/月 |
| Docker | 依主機 |

---

## 與 OpenClaw 的核心差異

| 維度 | Hermes Agent | OpenClaw |
|------|--------------|---------|
| 核心理念 | 把 Agent 當「頭腦」培養 | 把 Agent 當「系統」編排 |
| 主打功能 | 持久性、成長、記憶 | 工作流程、多頻道整合 |
| 記憶系統 | 四層自動記憶 | 對話歷史持久化 |
| 適合場景 | 研究、長期任務、個人化 | 客服、社群管理、商業自動化 |
| 授權 | MIT 開源 | 專有 + 開源元件 |

**結論：** 兩者不互斥。Hermes = 深度理解；OpenClaw = 廣度執行。

---

## 基本資訊

| 項目 | 內容 |
|------|------|
| 開發者 | Nous Research（Jeffrey Quesnelle, Karan Malhotra） |
| 授權 | MIT |
| 版本 | v0.7.0（2026-04-03） |
| GitHub Stars | 25,300+（不到兩個月） |
| Forks | 3,300+ |

---

## 相關頁面

- [[wiki/tools/hermes-agent]] — 工具評估頁
- [[wiki/concepts/ai-agent]] — AI Agent 架構（OpenClaw 為例）
- [[wiki/concepts/ai-memory-approaches]] — 各記憶方案比較
