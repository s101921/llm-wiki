---
title: Python 檔案生態系
date: 2026-04-29
updated: 2026-04-29
type: concept
status: draft
tags: [python, pandas, pptx, pdf, excel, chart, automation]
sources: 1
private: false
---

# Python 檔案生態系

**Python 作為「膠水語言」——幾乎所有有數位定義的檔案格式，都能透過對應的套件生成。**

## 核心類比

- **Python 底層環境** = 穩固的工作桌（基礎語法、標準函式庫）
- **第三方套件** = 針對不同任務的專業電動工具
- **LLM 的角色** = 看需求規格、挑選對應工具的工頭

## 六大檔案類別與對應套件

### 1. 辦公室文檔（Office & Documents）

| 格式 | 套件 | 說明 |
|------|------|------|
| Excel (.xlsx, .xlsm) | `pandas`, `openpyxl`, `XlsxWriter` | 數據處理、格式美化、條件格式化 |
| Word (.docx) | `python-docx` | 生成結構化報告 |
| PowerPoint (.pptx) | `python-pptx` | 自動抓取數據填入簡報模板 |
| PDF (.pdf) | `ReportLab`（從零繪製）, `WeasyPrint`（HTML轉PDF）, `PyPDF2`（合併拆分）| 視需求選擇 |

> **PDF vs PPTX 選擇**：需要極致美感 → PDF（WeasyPrint）；需要後續手動微調 → PPTX（python-pptx）

### 2. 互動式圖表（Data Visualization）

| 套件 | 用途 | 輸出格式 |
|------|------|----------|
| `matplotlib`, `seaborn` | 靜態統計圖 | PNG/SVG |
| `plotly` | 互動式網頁圖表 | HTML |
| `pyecharts` | ECharts Python 封裝 | HTML |

> 使用 Chart.js 時，數據通常從 Python 計算後**硬編碼**進 HTML（見 [[wiki/ai-workflow/llm-interactive-chart]]）

### 3. 數據交換（Data & Serialization）

- JSON / YAML：API 交換格式、設定檔
- Parquet / Feather：大數據高效能壓縮格式
- Pickle：儲存 Python 物件（如訓練好的 AI 模型）
- SQLite：輕量關聯式資料庫

### 4. 影像（Images）

- 點陣圖：`Pillow (PIL)` 或 `OpenCV`
- 向量圖（SVG）：`svgwrite`

### 5. 音訊與視訊

- 音訊：`pydub`, `librosa`
- 視訊：`MoviePy` 或 `FFmpeg`

### 6. 壓縮與封裝

- 壓縮檔：`zipfile`, `shutil`
- 執行檔：`PyInstaller`（.exe / .app）

## Excel 精細格式處理

`openpyxl` 支援的細部操作：
- 儲存格合併與對齊
- 條件格式化（達成率低於 80% 自動標記黃色）
- 公式寫入（在儲存格直接寫入 `=SUM(B2:B10)`）
- 分頁處理（依部門/月份拆分工作表）

**現代新選擇**：Microsoft 365 的 **Python in Excel**，不需離開 Excel 就能在儲存格內撰寫 Python。

## Python 生成檔案的兩種邏輯

1. **二進制寫入**：根據檔案格式的二進制規範直接寫入（圖片、壓縮檔）
2. **模板渲染**：先寫好框架（HTML, LaTeX, Markdown），再填入內容後轉檔

## 與其他頁面的關係

- [[wiki/ai-workflow/llm-interactive-chart]] — Chart.js 數據硬編碼模式的具體 SOP
- [[wiki/ai-workflow/python-html-data-dashboard]] — Python + HTML 完整數據分析方案
- [[wiki/tools/gemini-canvas]] — Canvas 是不依賴 Python 的替代視覺化方案
- [[wiki/concepts/code-execution-sandbox]] — Python 在沙盒中執行的技術背景
- [[wiki/ai-workflow/mac-python-dev-setup]] — Mac 上建立 Python 執行環境的 SOP

## 相關素材

- [[raw/Python支援的檔案格式.md]]
