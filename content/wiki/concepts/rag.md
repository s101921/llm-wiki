---
title: RAG（Retrieval-Augmented Generation）
date: 2026-04-08
updated: 2026-04-08
type: concept
tags: [RAG, 知識管理, 向量資料庫, LLM]
sources: 2
---

# RAG（Retrieval-Augmented Generation）

**在生成答案前，先從外部知識庫檢索相關片段，再交給 LLM 合成回答。**

---

## 核心原理

LLM 的訓練資料有截止日期，且無法記住對話外的私有資料。RAG 的解法：

1. 將文件切成小段（chunks），用 embedding 向量化後存入向量資料庫
2. 使用者提問時，將問題也向量化，找出語意最接近的 chunks
3. 把這些 chunks 塞入 prompt，讓 LLM 根據它們回答

標準流程：**文件 → 切割 → embedding → 向量庫 → 查詢時檢索 → 注入 context → 生成**

## 優點

- 知識可即時更新，不需重新訓練模型
- 私有資料不需上傳到模型
- 可追溯引用來源

## 根本限制（從 Wiki Pattern 角度）

- **每次重新推導**：每次問問題都從零拼湊，無法累積對知識的理解
- **跨文件合成弱**：檢索返回的是片段，難以處理需整合多份文件的問題
- **無結構**：原始文件沒有交叉引用、矛盾標記、或合成觀點

> 這正是 [[wiki/concepts/llm-wiki-pattern]] 提出的核心動機——用預先合成的 wiki 取代每次查詢的 RAG。

## 在 AI Agent 記憶系統中的應用

AI Agent 的長期記憶本質上就是 RAG：

1. 對話過程中的重要事件被寫入 `.md` 檔
2. 使用者問問題時，Agent 呼叫 memory.search 工具
3. 搜尋關鍵字與 memory chunks 做**字面比對（s1）+ 語意比對（s2）的 weighted sum**
4. 取前 k 個 chunk 塞進 context，LLM 就能「想起」過去的事

限制：今天、昨天的日誌在 System Prompt 中（準確），更早的靠 RAG（不一定可靠）。見 [[wiki/concepts/ai-agent]]。

## 與其他概念的關係

- [[wiki/concepts/llm-wiki-pattern]] — Wiki Pattern 是 RAG 的替代方案（預編譯 vs 即時檢索）
- [[wiki/concepts/ai-agent]] — AI Agent 記憶系統的底層機制就是 RAG
- [[wiki/tools/mempalace]] — MemPalace 是精緻化的 RAG 實作（加上 Palace 結構提升檢索精度）

## 在教學上的應用

RAG 是目前企業 AI 最常見的私有知識整合方式，課程中常作為「讓 AI 讀你的文件」的技術基礎說明。對比 LLM Wiki Pattern 有助於學員理解「檢索」與「合成」的本質差異。

## 相關素材

- [[wiki/summaries/llm-wiki-karpathy]] — Karpathy 對 RAG 限制的批評
- [[wiki/summaries/mempalace]] — 以 RAG 為基礎的高性能記憶系統案例
