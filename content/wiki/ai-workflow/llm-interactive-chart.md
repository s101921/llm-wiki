---
title: LLM 互動式圖表生成流程
date: 2026-04-29
updated: 2026-04-29
type: ai-workflow
status: draft
tags: [data-visualization, chart.js, python, bash-tool, workflow]
sources: 1
private: false
---

# LLM 互動式圖表生成流程

**類型：AI Workflow｜用途：將 CSV 資料轉成瀏覽器可互動的視覺化圖表｜工具：bash_tool + Chart.js + show_widget**

## 何時使用

- 有原始 CSV 資料需要視覺化分析
- 需要在 AI 對話內直接產出可互動圖表（不依賴外部工具）
- 資料集涉及多維度聚合（月度趨勢、排名、佔比分布）

## 執行步驟

### Step 1 — Python 資料分析（bash_tool）

在 Ubuntu 容器裡執行 Python 腳本，讀取 CSV 並做聚合計算：

```python
import csv
from collections import defaultdict

# 建立 lookup table（產品主檔、客戶主檔）
# 對每筆交易 join 對應欄位（產品線、通路、區域、客戶分級）
# 用 defaultdict(float) 分別 aggregate 各維度
# 輸出純文字 summary 數字到 stdout
```

**輸入：** CSV 檔案路徑  
**輸出：** 純文字數字 summary（印到 stdout，回傳給 Claude context）

### Step 2 — LLM 推理視覺化設計（Context Window）

拿到 Step 1 的數字後，在 context 裡直接推理（不呼叫任何工具）：

- 判斷哪些維度值得視覺化
  - 趨勢 → 折線圖
  - 佔比 → 甜甜圈圖
  - 排名 → 水平長條圖
- 識別異常值值得 callout（如某月高峰、某業務員落差）
- 設計版面層次：KPI 卡 → 趨勢 → 結構分析 → 洞察卡

**輸入：** Step 1 的 stdout 數字  
**輸出：** 圖表設計決策（存在 context 裡，不輸出）

### Step 3 — 寫 HTML + Chart.js 並渲染（show_widget）

把所有數字硬編碼進 HTML 字串，送給 `visualize:show_widget` 渲染：

```html
<!-- 技術棧 -->
<!-- 版面：純 HTML + inline CSS，用 CSS variables 適配深淺色模式 -->
<!-- 圖表：Chart.js 4.4.1（從 cdnjs 載入 UMD build） -->
<!-- 數據：直接硬編碼 data: [738, 378, 573...]，無 API call -->
```

**輸入：** Step 2 的設計決策 + Step 1 的數字  
**輸出：** iframe 渲染的互動圖表（Chart.js 在瀏覽器端執行）

## 技術架構

```
CSV 檔案
  ↓
bash_tool（Ubuntu 容器）
  → Python 腳本執行，stdout 回傳數字 summary
  ↓
Claude context window
  → 推理：選圖表類型、找洞察、設計版面
  → 寫 HTML/JS 字串（數字硬編碼）
  ↓
show_widget tool
  → iframe 渲染，Chart.js 在瀏覽器端執行
```

## 關鍵設計原則

- **數據硬編碼**：Python 只負責算數，HTML 裡的數字直接嵌入，不需要 runtime API
- **Step 2 是純推理**：LLM 不呼叫工具，只在 context 裡思考設計決策
- **關注點分離**：資料處理（Python）→ 設計判斷（LLM）→ 渲染（Chart.js）各司其職

## 已知限制

- 數字硬編碼代表圖表不能動態更新；若原始資料改變需重跑全流程
- bash_tool 需要 Ubuntu 容器權限，在受限環境（如 Gemini Canvas）可能無法使用
- Chart.js 從 cdnjs 載入，離線環境需要改用本地 bundle

## 相關工具頁 / 概念頁

- `[[wiki/concepts/ai-agent]]`（bash_tool 是典型的 tool-use 模式）
- `[[wiki/tools/gemini-canvas]]`（Canvas 環境的 show_widget 替代方案）
- `[[wiki/ai-workflow/context-engineering-coding-agents]]`（進階 tool-use 脈絡：coding agent 的工具呼叫設計）

## 相關素材

- `[[raw/LLM互動式圖表執行流程.md]]`（原始素材，已 ingest）
