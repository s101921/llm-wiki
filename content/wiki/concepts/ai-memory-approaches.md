---
title: AI 記憶方案比較：五種策略全覽
date: 2026-04-08
updated: 2026-04-09
type: synthesis
tags: [記憶系統, 知識管理, RAG, LLM Wiki Pattern, MemPalace, Hermes Agent]
sources: 3
status: growing
---

# AI 記憶方案比較：五種策略全覽

**同樣在解決「AI 沒有長期記憶」的問題，五種方案的策略截然不同。**

---

## 五種方案的核心策略

| | RAG（標準） | AI Agent 記憶 | MemPalace | Hermes Agent | LLM Wiki Pattern |
|--|------------|--------------|-----------|--------------|------------------|
| **記憶方式** | 向量檢索原始文件 | 寫入 `.md`，再 RAG 檢索 | 儲存完整對話，結構化檢索 | 四層自動記憶 + 主動學習 | LLM 主動合成→寫入 wiki |
| **儲存什麼** | 原始文件切片 | 重要事件、指令、人格 | 逐字對話（Drawers） | 對話 + 偏好模型 + 技能 | 合成知識（頁面） |
| **查詢時做什麼** | 即時語意搜尋 | memory.search + memory.get | 語意搜尋 + Palace 結構過濾 | 自動調用適當層級 | 直接讀 wiki 頁面 |
| **知識累積方式** | 不累積 | 累積個人事件記憶 | 累積對話歷史 | 自動生成可複用 Skills | 累積合成理解 |
| **特殊機制** | — | 心跳 + Cron Job + Compaction | Palace 結構（+34% 檢索）| Learning Loop + Skills 封裝 | lint 循環 |
| **適合什麼記憶** | 靜態知識文件 | 個人身份、習慣、決定 | 對話、決策、個人偏好 | 個人化、長期任務、技能沉澱 | 概念、工具、觀點合成 |

---

## 關鍵差異：「儲存什麼」決定「能回答什麼」

**MemPalace** 最強的地方：**事實性回憶**
> *「我上個月決定用 Postgres 的原因是什麼？」*
> → 找到那段對話的逐字記錄，96.6% R@5

**Hermes Agent** 最強的地方：**持久性個人化 + 技能沉澱**
> *「上次我們解決這類 bug 的方法是什麼？」*
> → 調用 Procedural Memory 中封裝好的 Skill，直接應用

**LLM Wiki Pattern** 最強的地方：**合成性理解**
> *「Karpathy 和 MemPalace 對 RAG 的看法有什麼不同？」*
> → wiki 已預先比較，直接讀頁面，不需重新推導

**RAG** 最強的地方：**靜態文件查詢**
> *「這份合約裡的付款條款是什麼？」*
> → 直接從原始文件中找片段

---

## 五種方案的互補性

五種方案並不衝突，可以組合運作：

- **AI Agent 記憶**（OpenClaw memory.md）：記住「我是誰、有哪些指令限制」
- **MemPalace**：記住「發生了什麼對話」
- **Hermes Agent**：記住「如何做事、用戶偏好」並自動沉澱技能
- **LLM Wiki Pattern**：記住「我們理解了什麼概念」

**身份證**（Agent 記憶）× **日記**（MemPalace）× **學習記錄**（Hermes）× **教科書**（Wiki Pattern）

---

## 教學應用

這個比較適合在課程中討論「AI 的記憶類型」：

1. **情節記憶**（episodic）— MemPalace 擅長：「那次我們說過什麼？」
2. **語意記憶**（semantic）— LLM Wiki Pattern 擅長：「這個概念是什麼？」
3. **程序記憶**（procedural）— Hermes Agent 擅長：「這類任務怎麼做？」
4. **工作記憶**（working）— context window：「這次對話說了什麼？」

四種記憶的對比，是 AI 認知架構的完整入門教材。

---

## 相關頁面

- [[wiki/concepts/ai-agent]] — AI Agent 完整架構（含心跳、Cron Job、Compaction）
- [[wiki/concepts/llm-wiki-pattern]] — LLM Wiki 方法論
- [[wiki/tools/mempalace]] — MemPalace 工具評估
- [[wiki/concepts/rag]] — RAG 基礎概念
- [[wiki/summaries/hung-yi-lee-openclaw-agent]] — AI Agent 影片摘要（李宏毅）
- [[wiki/summaries/llm-wiki-karpathy]] — LLM Wiki 原始素材
- [[wiki/summaries/mempalace]] — MemPalace 原始素材
