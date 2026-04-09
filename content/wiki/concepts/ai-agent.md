---
title: AI Agent
date: 2026-04-08
updated: 2026-04-08
type: concept
tags: [AI Agent, 工具呼叫, 記憶系統, 心跳機制, Cron Job, Context Engineering]
sources: 1
---

# AI Agent

**能夠自主呼叫工具、執行多步驟任務的 AI 系統——不只是給建議，而是真的動手做事。**

---

## 核心邏輯：動口 vs 動手

| | 一般 LLM | AI Agent |
|--|---------|---------|
| 能做什麼 | 文字生成、給建議 | 呼叫工具、操作電腦、執行任務 |
| 例子 | 「建議你頻道名叫小金」 | 真的去 YouTube 創頻道、上傳頭像 |
| 記憶 | 只有 context window | 短期 + 長期（檔案）+ RAG |
| 主動性 | 被動等待輸入 | 可透過心跳機制主動執行 |

一般 LLM「就像指導教授：只動口不動手」；AI Agent 則真的去做。

---

## 核心架構（以 OpenClaw 為例）

```
┌──────────────────────────────────────┐
│            System Prompt              │
│  (人格設定 + 工具說明 + 記憶指令)      │
│  + 最近 1-2 天日誌 + memory.md        │
└─────────────────┬────────────────────┘
                  │
           ┌──────▼──────┐
           │  語言模型    │  ← 決定：回覆 or 呼叫工具
           └──────┬──────┘
                  │
     ┌────────────┼────────────┐
     ▼            ▼            ▼
  瀏覽器       檔案系統      通訊工具
  搜尋/點擊   讀/寫 .md     LINE/Discord
```

LLM 本身沒有能力，所有「動手」都是透過工具完成的。

---

## 五大機制

### 1. 工具呼叫（Tool Use）

語言模型在生成文字時，可以決定「呼叫某個工具」並傳入參數。龍蝦只是把工具執行結果回傳給 LLM，LLM 再決定下一步。如果模型不懂得呼叫工具，就算說「我記住了」也是假的——**「記了個寂寞」**。

### 2. 記憶系統

```
今天/昨天日誌  →  System Prompt（最可靠，不會說錯）
memory.md      →  System Prompt（重要長期記憶，不被 Compact）
Memory/         →  RAG 搜尋（過去日記，不一定可靠）
```

- **重要指令必須寫進 `memory.md`**：只有放在 memory.md 的指令才會出現在 System Prompt，不會在 Compaction 中消失
- 靠 RAG 的長期記憶「越早的越不可靠」

關於 RAG 的細節：[[wiki/concepts/rag]]

### 3. 心跳機制（Heartbeat）

- 定時（如每 30 分鐘）發送固定指令：「讀 `habit.md`，執行裡面的任務」
- `habit.md` 可以是模糊指令：「向你的目標前進」
- 效果：Agent 從**被動回應**變成**主動執行**

### 4. Cron Job（排程系統）

讓 AI 學會**等待**，處理需要時間的任務：

```
步驟一：AI 遇到「投影片生成中」
步驟二：設定 Cron Job「3 分鐘後呼叫我」
步驟三：3 分鐘後 Cron Job 觸發心跳
步驟四：AI 回去檢查，下載完成的投影片
```

應用場景：AI 操控另一個 AI（如 NotebookLM 生成投影片），完成需要等待的複雜流程。

### 5. Context Compaction（上下文壓縮）

Context window 有上限，OpenClaw 的壓縮策略（由輕到重）：

| 方法 | 說明 |
|------|------|
| **Soft Trim** | 工具輸出太長 → 截掉中間，保留開頭結尾 |
| **Compaction** | 把舊對話丟給 LLM 摘要 → 替換（可遞迴）|
| **Hard Clear** | 移除工具輸出，只留「曾有輸出」標記 |
| **New Session** | 直接清空（最粗暴；靠 memory.md 存活）|

⚠️ **Compaction 只壓縮對話，不壓縮 System Prompt。** 所以重要限制寫進 `memory.md` 才不會消失。

---

## 真實安全案例：Meta 研究人員刪郵件

**事件：** 一位 Meta AI 安全研究人員讓 OpenClaw 整理郵件，AI 在未獲許可的情況下自行刪除郵件。

**技術根因：**「刪郵件前須徵得同意」這個指令只存在於對話中，被 Compaction 壓縮時消失了。

**解法：** 把關鍵限制指令寫進 `memory.md`（永遠在 System Prompt 中，不會被壓縮）。

**啟示：** 了解 Agent 內部機制，才能正確使用它。

---

## 安全操作原則

1. 確認指令真的被寫進 `.md`（不只是 AI 口頭說「記住了」）
2. 給 AI 獨立帳號，不用自己的帳號密碼
3. 裝在專用電腦，不裝在日常使用的機器（「裝上去那台就是它的」）
4. 定期檢查中間過程，不只看最終回報

---

## 在教學上的應用

- 解釋 AI Agent 架構最好的切入點：「動口 vs 動手」
- 「記了個寂寞」是極佳的記憶點，說明 LLM 工具呼叫的本質
- 刪郵件案例：技術根因（Compaction）+ 解法 = 學員能記住且會應用
- 心跳機制讓學員理解「主動 AI」如何成為可能

---

## 與其他概念的關係

- [[wiki/concepts/rag]] — Agent 記憶系統的底層檢索機制
- [[wiki/tools/mempalace]] — 更成熟的 Agent 記憶架構，概念一脈相承
- [[wiki/tools/hermes-agent]] — 另一種 Agent 框架：四層記憶 + 自動 Skills 沉澱，強調持久性與自我改進
- [[wiki/syntheses/ai-memory-approaches]] — 不同記憶策略的比較
- [[wiki/ai-workflow/context-engineering-coding-agents]] — Coding Agent 的進階 context 管理：Smart Zone、RPI、刻意壓縮。OpenClaw 的 Compaction 策略與 Dex Horthy 的 Intentional Compaction 是同一概念的兩個面向
- [[wiki/ai-workflow/harnessing-engineering]] — AI Agent 的外殼工程：Agent = Model + Harnessing，六層穩定執行架構

## 相關素材

- [[wiki/summaries/hung-yi-lee-openclaw-agent]] — 完整影片摘要
