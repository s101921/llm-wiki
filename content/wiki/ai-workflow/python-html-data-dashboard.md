---
title: Python + HTML 數據儀表板架構
date: 2026-04-29
updated: 2026-04-29
type: ai-workflow
status: draft
tags: [python, html, chart.js, data-analysis, dashboard, pandas, weasyprint]
sources: 2
private: false
---

# Python + HTML 數據儀表板架構

**類型：AI Workflow｜用途：以本地 Python 處理敏感數據，LLM 只接觸資料結構（Schema），最終輸出互動式 HTML 或 PDF/PPTX 簡報｜工具：Python + Chart.js / WeasyPrint / python-pptx**

## 核心設計原則

**「代碼執行分離」模式**：LLM 只接觸「資料結構（Schema）」，不接觸「真實數值」。本地環境是安全沙盒，處理實際業務數據。

## 三層架構

```
邏輯規劃（LLM 端）
  → 你提供欄位名稱（Headers）與分析需求
  → LLM 產出 Python 分析腳本與 HTML 模板

數據加工（本地 Python）
  → 執行腳本處理原始數據（CSV/Excel/SQL）
  → 將結果轉化為 HTML 能理解的格式（JSON）

渲染呈現（本地 Browser）
  → 將數據注入 HTML，生成可視化報告
```

## Python 到 HTML 的數據傳遞方案

### 方案 A：變數替換法（最簡單）

```python
import pandas as pd, json

# 讀取與計算
df = pd.read_csv('sales.csv')
result = df.groupby('month')['revenue'].sum().to_dict()

# 注入 HTML 模板
with open('template.html', 'r') as f:
    html = f.read()

html = html.replace('{{DATA_PLACEHOLDER}}', json.dumps(result))

with open('output.html', 'w') as f:
    f.write(html)
```

**HTML 模板預留位**：
```html
<script>
  var raw_data = {{DATA_PLACEHOLDER}};
</script>
```

### 方案 B：Jinja2 模板引擎（專業做法）

```python
from jinja2 import Template

with open('template.html', 'r') as f:
    template = Template(f.read())

html_content = template.render(
    title="月度行銷分析報告",
    data_list=my_processed_data_json
)
```

### 方案 C：Streamlit（最強烈推薦）

```bash
pip install streamlit
streamlit run app.py
```

- 內建互動式圖表（Plotly, ECharts）
- LLM 對 Streamlit 語法掌握度極高
- 不需處理 HTML/JS 的拋接問題

## 輸出格式選擇

| 格式 | 套件 | 優點 | 缺點 |
|------|------|------|------|
| PDF | WeasyPrint | 極佳美感、CSS全局樣式 | 不可編輯、需 Pango 底層庫 |
| PPTX | python-pptx | 完全可編輯 | 絕對座標定位，排版費工 |
| HTML | Chart.js / Plotly | 互動式、可分享連結 | 需要瀏覽器開啟 |

> **PDF vs PPTX 選擇指引**：提交主管 → PDF；會議前需手動微調 → PPTX。最佳 PPTX 實務：用設計師製作的精美模板 + python-pptx 填入佔位符。

## 給 LLM 的 Prompt 協作策略

| 步驟 | Prompt 策略 |
|------|-------------|
| Step 1: 定義結構 | 「我有 CSV 檔案，欄位包含 date, revenue, campaign。請寫 Python 腳本，計算每日總營收，輸出為 JSON。」|
| Step 2: 建立模板 | 「請寫互動式 HTML 模板，用 Chart.js 呈現折線圖，在 `<script>` 內預留 `const dashboardData` 變數位置。」|
| Step 3: 膠水代碼 | 「請寫 Python 代碼，讀取 HTML 模板，將 JSON 注入 dashboardData 位置，另存為 final_report.html。」|

## 技術注意事項

- **NaN 值處理**：JSON 不支援 `NaN`，確保 Python 先用 `.fillna(0)` 或 `.dropna()` 處理
- **離線資源**：本地端使用時，Chart.js 等 JS 庫確認使用 CDN 連結（需網路）或已下載到本地
- **資料傳遞量**：不能將幾十萬筆資料直接送回 LLM Context Window，讓執行引擎只回傳「統計分析結果」或「前五筆範例」

## 完整 LLM Data Agent 流程

```
使用者上傳數據
    ↓
LLM：分析規劃 + 查詢設計（決定算什麼）
    ↓
工具呼叫：數據計算引擎（Python/pandas，專注清洗、聚合）
    ↓
輸出：結構化資料（JSON / 統計摘要文字）
    ↓
LLM：視覺化規格 + 洞察意圖（根據摘要撰寫分析、規劃圖表類型）
    ↓
工具呼叫：渲染與匯出引擎（根據 LLM 指定的 output_format 選套件）
    ↓
最終分析輸出
```

> 關鍵：步驟 3 的 Python **只做數據計算，不生成最終圖表**；圖表生成在步驟 6 的渲染引擎。

## 相關工具頁 / 概念頁

- `[[wiki/ai-workflow/llm-interactive-chart]]` — 簡化版：三步 SOP（bash_tool → LLM推理 → show_widget）
- `[[wiki/concepts/python-file-ecosystem]]` — 各種輸出格式的套件選擇參考
- `[[wiki/ai-workflow/html-chart-export]]` — HTML 圖表下載功能的實作 SOP
- `[[wiki/concepts/code-execution-sandbox]]` — 為什麼 AI 有時只給程式碼不直接執行

## 相關素材

- [[raw/Python+HTML打造品牌地端數據分析方案.md]]
- [[raw/📖 知識庫：自動化銷售數據分析與簡報生成指南 (Mac 環境).md]]
