---
title: 程式碼執行沙盒（Code Execution Sandbox）
date: 2026-04-29
updated: 2026-04-29
type: concept
status: draft
tags: [sandbox, python, execution, gemini, llm-tool]
sources: 1
private: false
---

# 程式碼執行沙盒（Code Execution Sandbox）

**AI 執行程式碼的隔離虛擬環境。LLM 生成程式碼 → 送入沙盒執行 → 結果回傳。**

當 AI 只回傳程式碼卻沒有執行結果時，通常是沙盒在「執行」或「回傳」階段斷鏈了。

## 沙盒的運作流程

```
AI 理解需求
    ↓
寫出 Python 腳本
    ↓
腳本送入沙盒（隔離的 Ubuntu/Linux 容器）中執行
    ↓
生成的檔案 → 轉化為下載連結回傳給使用者
```

## 五大失敗原因

### 1. 依賴庫缺失（Dependencies Missing）

沙盒預裝常用庫（pandas、matplotlib），但特定用途的庫可能未安裝（如 `python-pptx`、`openpyxl`）。

**結果**：`import pptx` 找不到模組 → 執行報錯 → AI 退縮成「給你程式碼請自己執行」模式。

### 2. 檔案系統與 UI 對接失敗（I/O 錯誤）

沙盒是**暫時性環境（Ephemeral Environment）**。程式碼成功執行、檔案也生成了，但在把暫存檔轉換為「下載連結」時超時或路徑讀取錯誤。

### 3. 資源與時間限制（Timeout & OOM）

每個沙盒都有嚴格的記憶體（RAM）和執行時間上限。大量數據、複雜排版 → 執行超時或容器崩潰（Out of Memory）。

### 4. 網路隔離（Air-Gapped）

沙盒通常是**斷網**的。要求「插入外部網址的圖片」或「抓取即時股票資料」→ 網路請求被防火牆擋下 → 執行失敗。

### 5. 意圖判讀錯誤（Intent Misclassification）

LLM 判定「提供程式碼讓使用者客製化」比「直接生成靜態檔案」更好，選擇不執行。

## 提高成功率的 Prompt 策略

- **強化執行指令**：「請**執行**以下需求，並提供最終的 `.pptx` **下載連結**，不要只給我程式碼。」
- **避免外部依賴**：所需文字內容直接包含在對話框內，不要請 AI 去外部網頁抓圖或資料。
- **分段進行**：先確認大綱與數據結構，再下指令「請執行 Python 生成 PPTX 檔案」，降低沙盒運算負擔。

## 不同平台的沙盒特性

| 平台 | 沙盒環境 | 網路 | 持久性 |
|------|----------|------|--------|
| Claude Code | bash_tool（Ubuntu 容器）| 有 | 會話期間 |
| Gemini Canvas | 前端渲染（單一 HTML）| 限制 | 無持久化 |
| ChatGPT | Python sandbox | 無 | 無持久化 |

## 與其他概念的關係

- [[wiki/concepts/ai-agent]] — 沙盒是 Agent 的 tool-use 執行環境
- [[wiki/ai-workflow/llm-interactive-chart]] — bash_tool 是 Claude Code 的具體沙盒實踐
- [[wiki/tools/gemini-canvas]] — Canvas 的前端渲染是一種特殊的「沙盒」模式

## 相關素材

- [[raw/程式碼執行沙盒原理（Code Execution Sandbox）.md]]
