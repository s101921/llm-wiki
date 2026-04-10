---
title: "Harnessing Engineering — AI 落地關鍵"
date: 2026-04-09
updated: 2026-04-09
type: summary
tags: [Harnessing Engineering, AI Agent, Context Engineering, Prompt Engineering, 落地]
sources: 1
status: stable
---

# Harnessing Engineering — AI 落地關鍵

**來源：** [[raw/AI 落地關鍵：什麼是 Harnessing Engineering？.md]]  
**形式：** 影片逐字稿｜歡歡老師，AI 秘密花園

---

## 核心主張

> 真正決定 Agent 能不能落地、能不能穩定交付的，不是模型本身，而是**模型外面那套運行的系統——Harnessing**。

案例：同樣的模型 + 同樣的提示詞，改進任務拆法、狀態管理、步驟驗證、失敗恢復後，任務成功率從 70% 提升至 95%+。

---

## 三代 AI 工程演進

| | Prompt Engineering | Context Engineering | Harnessing Engineering |
|--|-------------------|---------------------|------------------------|
| **解決的問題** | 模型有沒有聽懂你說什麼？ | 模型有沒有拿到足夠正確的訊息？ | 模型在真實執行裡能不能持續做對？ |
| **工程對象** | 指令表達 | 輸入環境 | 整個運行系統 |
| **適合場景** | 單輪問答 | 需要外部知識的 Agent | 長鏈路、低容錯的真實任務 |

**包含關係（不是替代）：** Harnessing ⊇ Context Engineering ⊇ Prompt Engineering

---

## 核心公式

> **Agent = Model + Harnessing**  
> Harnessing = Agent − Model（除了模型以外，幾乎所有決定穩定交付的東西）

---

## Harnessing 六層架構

| 層 | 名稱 | 核心職責 |
|----|------|---------|
| 1 | **Context 管理** | 角色目標定義、訊息選擇、結構化組織 |
| 2 | **工具系統** | 給什麼工具、何時調用、結果怎麼重新餵回模型 |
| 3 | **執行編排** | 任務步驟的串接：理解→補足訊息→分析→生成→驗證→修正 |
| 4 | **記憶與狀態** | 當前任務狀態 / 對話中間結果 / 長期記憶與用戶偏好（三類不能混） |
| 5 | **評估與觀測** | 輸出驗收、環境驗證、自動測試、日誌、錯誤歸因 |
| 6 | **約束、驗教、失敗恢復** | 哪些不能做（約束）、輸出前先檢查（教驗）、失敗後重試/切路徑/回滾（恢復）|

---

## 比喻：派人去客戶拜訪

| 工程類型 | 對應動作 |
|---------|---------|
| Prompt Engineering | 把任務講清楚（先問候、再提方案、再問需求…） |
| Context Engineering | 資料要齊全（客戶背景、過往記錄、報價、競品情況…） |
| Harnessing Engineering | Check List + 關鍵節點匯報 + 會後錄音 + 偏差即糾正 + 明確驗收標準 |

---

## 相關頁面

- [[wiki/ai-workflow/harnessing-engineering]] — 完整概念頁（含六層詳解）
- [[wiki/ai-workflow/context-engineering-coding-agents]] — Context Engineering 的 Coding Agent 實踐
- [[wiki/concepts/ai-agent]] — AI Agent 完整架構
