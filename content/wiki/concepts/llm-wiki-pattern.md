---
title: LLM Wiki Pattern
date: 2026-04-08
updated: 2026-04-08
type: concept
tags: [知識管理, LLM, 第二大腦, PKM]
sources: 1
status: growing
---

# LLM Wiki Pattern

**用 LLM 持續撰寫與維護一個結構化的個人 Wiki，讓知識隨每次輸入複利累積，而非每次查詢時重新推導。**

---

## 核心原理

傳統 RAG 的問題：每次問問題，LLM 都從零開始從原始文件中拼湊答案，沒有累積。

LLM Wiki 的做法不同：

1. 每加入一份新素材，LLM 就把知識**編譯**進 wiki
2. Wiki 是一個**持續複利的產物** — 交叉引用已建好、矛盾已標記、綜合觀點已反映最新素材
3. 查詢時直接讀 wiki，不用重新推導

核心比喻：**Obsidian 是 IDE，LLM 是工程師，Wiki 是程式碼**。

## 三層架構

| 層 | 內容 | 誰維護 |
|----|------|--------|
| 原始素材（raw/Clippings） | 文章、影片、PDF，不可修改 | 你 |
| Wiki（wiki/） | 摘要頁、概念頁、工具頁、綜合分析 | LLM |
| Schema（CLAUDE.md） | 結構規範、工作流程 | 你 + LLM 共同演化 |

## 三種操作

- **Ingest**：新素材進來 → LLM 讀取 → 寫摘要 → 更新相關頁面 → 更新 index + log
- **Query**：問問題 → LLM 讀 index → 讀相關頁 → 回答附引用 → 好答案存回 wiki
- **Lint**：定期健康檢查 → 找矛盾、孤立頁、過時內容、缺失頁面

## 為什麼有效

知識庫維護失敗的原因不是「沒時間讀」，而是「沒時間做書目整理」。LLM 不會厭倦更新交叉引用，一次可以觸及 15 個頁面，維護成本趨近於零。

## 與其他模式的差別

- vs [[wiki/concepts/rag|RAG]]：RAG 每次重新檢索；Wiki Pattern 知識預先編譯，查詢更快更深
- vs [[wiki/tools/mempalace|MemPalace]]：同樣解決 AI 記憶問題，但策略相反——MemPalace 儲存完整對話再語意搜尋（擅長事實回憶）；Wiki Pattern 預先合成知識頁面（擅長概念理解）。兩者可互補，見 [[wiki/concepts/ai-memory-approaches]]
- vs Notion/概念圖：手動維護，隨規模擴大人工成本爆炸
- vs NotebookLM：封閉系統，無法自訂結構，知識不累積

## 在教學上的應用

這個 Vault 本身就是 LLM Wiki Pattern 的實踐。可作為課程中示範「AI 如何輔助知識管理」的活生生案例。

## 相關素材

- [[Clippings/llm-wiki]] — Andrej Karpathy 原文（GitHub Gist）
