---
title: AI 記憶方案比較：LLM Wiki Pattern vs MemPalace vs RAG
date: 2026-04-08
updated: 2026-04-08
type: synthesis
tags: [記憶系統, 知識管理, RAG, LLM Wiki Pattern, MemPalace]
sources: 2
---

# AI 記憶方案比較：LLM Wiki Pattern vs MemPalace vs RAG

**同樣在解決「AI 沒有長期記憶」的問題，三種方案的策略截然不同。**

---

## 四種方案的核心策略

| | RAG（標準） | AI Agent 記憶 | MemPalace | LLM Wiki Pattern |
|--|------------|--------------|-----------|------------------|
| **記憶方式** | 向量檢索原始文件 | 寫入 `.md`，再 RAG 檢索 | 儲存完整對話，結構化檢索 | LLM 主動合成→寫入 wiki |
| **儲存什麼** | 原始文件切片 | 重要事件、指令、人格 | 逐字對話（Drawers） | 合成知識（頁面） |
| **查詢時做什麼** | 即時語意搜尋 | memory.search + memory.get | 語意搜尋 + Palace 結構過濾 | 直接讀 wiki 頁面 |
| **知識累積方式** | 不累積 | 累積個人事件記憶 | 累積對話歷史 | 累積合成理解 |
| **特殊機制** | — | 心跳 + Cron Job + Compaction | Palace 結構（+34% 檢索）| lint 循環 |
| **適合什麼記憶** | 靜態知識文件 | 個人身份、習慣、決定 | 對話、決策、個人偏好 | 概念、工具、觀點合成 |

---

## 關鍵差異：「儲存什麼」決定「能回答什麼」

**MemPalace** 最強的地方：**事實性回憶**
> *「我上個月決定用 Postgres 的原因是什麼？」*
> → 找到那段對話的逐字記錄，96.6% R@5

**LLM Wiki Pattern** 最強的地方：**合成性理解**
> *「Karpathy 和 MemPalace 對 RAG 的看法有什麼不同？」*
> → wiki 已預先比較，直接讀頁面，不需重新推導

**RAG** 最強的地方：**靜態文件查詢**
> *「這份合約裡的付款條款是什麼？」*
> → 直接從原始文件中找片段

---

## 三者的互補性

三種方案並不衝突，可以同時運作：

- **AI Agent 記憶**（OpenClaw memory.md）：記住「我是誰、有哪些指令限制」
- **MemPalace**：記住「發生了什麼對話」
- **LLM Wiki Pattern**：記住「我們理解了什麼概念」

第一個是**身份證**，第二個是**日記**，第三個是**教科書**。

---

## 教學應用

這個比較適合在課程中討論「AI 的記憶類型」：

1. **情節記憶**（episodic）— MemPalace 擅長：「那次我們說過什麼？」
2. **語意記憶**（semantic）— LLM Wiki Pattern 擅長：「這個概念是什麼？」
3. **工作記憶**（working）— context window：「這次對話說了什麼？」

三種記憶的對比，也是 AI 認知架構的入門教材。

---

## 相關頁面

- [[wiki/concepts/ai-agent]] — AI Agent 完整架構（含心跳、Cron Job、Compaction）
- [[wiki/concepts/llm-wiki-pattern]] — LLM Wiki 方法論
- [[wiki/tools/mempalace]] — MemPalace 工具評估
- [[wiki/concepts/rag]] — RAG 基礎概念
- [[wiki/summaries/hung-yi-lee-openclaw-agent]] — AI Agent 影片摘要（李宏毅）
- [[wiki/summaries/llm-wiki-karpathy]] — LLM Wiki 原始素材
- [[wiki/summaries/mempalace]] — MemPalace 原始素材
