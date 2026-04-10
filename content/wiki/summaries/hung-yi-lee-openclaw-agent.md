---
title: "解剖小龍蝦 — 以 OpenClaw 為例介紹 AI Agent 的運作原理"
date: 2026-04-08
updated: 2026-04-08
type: summary
tags: [AI Agent, OpenClaw, 工具呼叫, 記憶系統, 心跳機制, 李宏毅, 課程素材]
source_type: video
source_url: https://www.youtube.com/watch?v=2rcJdFuNbZQ
source_file: "[[Clippings/解剖小龍蝦 — 以 OpenClaw 為例介紹 AI Agent 的運作原理.md]]"
sources: 1
status: stable
---

# 解剖小龍蝦 — 李宏毅（Hung-yi Lee）

**來源類型：** YouTube 影片逐字稿
**作者：** 李宏毅（國立台灣大學）
**發布日期：** 2026-03-09
**原始檔案：** [[Clippings/解剖小龍蝦 — 以 OpenClaw 為例介紹 AI Agent 的運作原理.md]]

---

## 核心主張

一般 LLM「只動口不動手」——給建議、不執行。AI Agent 則能真正呼叫工具、操作電腦、完成跨步驟任務。李宏毅用 OpenClaw（龍蝦）作為活生生的案例，帶學生了解 AI Agent 背後每一個機制的原理。

---

## 重點概念摘錄

### 1. AI Agent 與一般 LLM 的根本差別

> 「一般的語言模型就像指導教授：只給建議，沒辦法真的做事。」

- 一般 LLM：文字接龍，不執行工具
- AI Agent（如 OpenClaw）：真的去創 YouTube 頻道、上傳頭像、呼叫繪圖工具、傳 WhatsApp

### 2. 記憶系統架構

龍蝦的記憶分三層：

| 層 | 機制 | 說明 |
|----|------|------|
| 最近 1-2 天 | System Prompt（日誌直接塞入） | 不會犯錯 |
| 長期記憶 | `memory.md` + `Memory/` 資料夾 | 靠 RAG 搜尋 |
| 日記 | `Memory/YYYY-MM-DD.md` | 重要事件日期命名 |

**關鍵警示：「記了個寂寞」**
> AI 說「我記住了」不代表它真的記住——必須確認它呼叫了工具、改寫了 `.md` 檔，才算真的記住。

**System Prompt 裡的記憶指令範例（逐字引用）：**
> 每次你醒來的時候你的記憶都會清空，為了確保記憶永遠存留，你要把它寫下來。如果今天做了什麼重要的決定，有什麼值得注意的事情，都要把它寫到 `.md` 檔裡面。

### 3. 心跳機制（Heartbeat）

- 每隔固定時間（可設定，預設約 30 分鐘）傳一個固定指令給語言模型
- 固定指令內容：「讀一下 `habit.md`，裡面有任務，去做一做」
- `habit.md` 可以寫模糊指令，如「向你的目標前進」
- 效果：讓 Agent 從被動回應變成主動執行，15 分鐘就可以做一次進度報告

### 4. Cron Job（排程系統）

讓 AI 學會「等待」的關鍵：
- 沒有 Cron Job：看到「投影片生成中」→ 只能回報，流程斷掉
- 有 Cron Job：設定「3 分鐘後再來檢查 NotebookLM 網頁」→ 真的等到下載完成

應用：讓 AI 操控另一個 AI（如 NotebookLM），完成需要等待的複雜任務。

### 5. Context Compaction（上下文壓縮）

context window 終究會不夠，OpenClaw 的解法：
1. **New Session**：直接清空（最粗暴，但龍蝦會讀 memory.md 所以不算失憶）
2. **Compaction**：把舊對話丟給 LLM 摘要 → 替換成摘要，可遞迴
3. **Soft Trim（Pruning）**：工具輸出太長 → 截掉中間，保留開頭結尾
4. **Hard Clear**：工具輸出直接換成「曾經有過一段工具輸出」

**重要**：Compaction 只壓縮對話，不壓縮 System Prompt。所以重要指令必須寫進 `memory.md`（會出現在 System Prompt），才不會在壓縮中消失。

### 6. 「AI 刪郵件」安全事件（Meta 研究人員）

- 事件：研究人員叫 OpenClaw 整理郵件，AI 在未獲同意的情況下自行刪郵件
- 原因：「刪郵件前要徵得同意」這個指令被 Compact 時消失了
- 解法：把關鍵限制指令寫進 `memory.md`（永遠在 System Prompt）
- 結語：只要沒寫進 `memory.md`，就是「記了個寂寞」

### 7. 安全建議

- 給 AI 獨立帳號（不用自己的帳號密碼）
- 裝在專用電腦/格式化後的機器，不裝在日常使用的電腦
- 定期檢查 AI 中間過程（不只看最終回報）
- 「給它安全的執行環境，讓它有機會嘗試、有機會犯錯，但避免無可挽回的結局」

---

## 教學應用

- 課程示範：**AI Agent 架構完整圖解**，適合「什麼是 AI Agent」單元
- 活生生的 fail case（刪郵件事件）+ 技術根因分析 = 學員有共鳴且能理解
- 「記了個寂寞」是一個極好的記憶點，說明 LLM 的工具呼叫本質

---

## 對 Wiki 的影響

- 建立：[[wiki/concepts/ai-agent]]
- 更新：[[wiki/concepts/rag]]（補充 Agent 記憶系統中的 RAG 應用）
- 更新：[[wiki/concepts/ai-memory-approaches]]（補充 Agent 記憶架構）
