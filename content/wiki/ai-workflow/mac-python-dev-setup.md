---
title: Mac Python 開發環境設定 SOP
date: 2026-05-01
updated: 2026-05-01
type: ai-workflow
status: draft
tags: [python, mac, venv, virtualenv, jupyter, development-environment]
sources: 1
private: false
---

# Mac Python 開發環境設定 SOP

**類型：AI Workflow｜用途：在 Mac 本機建立乾淨、可重複的 Python 執行環境｜工具：Terminal + venv + pip**

## 何時使用

- 第一次在 Mac 上執行 Python 腳本
- 需要管理多個有不同套件需求的 Python 專案
- 遇到 `ModuleNotFoundError`，需要排查環境問題

## Step 1：一次性基礎建設

```bash
# 確認 Python 已安裝
python3 --version    # 看到 Python 3.x.x
pip3 --version       # 看到 pip 2x.x
```

若未安裝，至 [python.org](https://www.python.org/downloads/macos/) 下載最新版，按「繼續」到底即可。

## Step 2：三種情境的虛擬環境操作

> 虛擬環境（venv）= 每個專案的獨立工具箱，避免不同專案的套件互相干擾。
> 啟動後，終端機前方會出現 `(venv)` 標誌。

### 情境一：初次執行（從無到有）

```bash
cd /路徑/到/你的/專案資料夾
python3 -m venv venv          # 建立虛擬環境
source venv/bin/activate       # 啟動（看到 (venv) 出現）
pip install pandas matplotlib  # 安裝這專案需要的套件
python3 main.py                # 執行腳本
```

### 情境二：後續執行（明天回來繼續）

```bash
cd /路徑/到/你的/專案資料夾
source venv/bin/activate       # 只要啟動環境即可
python3 main.py                # 套件已在，直接執行
```

### 情境三：新專案（不同資料夾）

每個新專案都要建立自己的虛擬環境，重複情境一的步驟。各專案的 venv 彼此獨立。

```bash
deactivate   # 離開當前虛擬環境（也可直接關閉終端機）
```

## 三種開發流派

### 流派一：單一腳本（快速測試、小型自動化）

所有邏輯在一個 `.py` 檔案中完成。

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
df['processed'] = df['score'] > 90
df.to_csv('result.csv', index=False)
plt.bar(df['name'], df['score'])
plt.savefig('chart.png')
```

### 流派二：模組化開發（大型系統、可重用）

將讀取、分析、視覺化拆成不同檔案，由 `main.py` 串聯：

```
project/
├── venv/
├── data_loader.py    # 讀取工兵
├── analyzer.py       # 分析專家
├── visualizer.py     # 繪圖美工
└── main.py           # 總指揮官（唯一需要手動執行的檔案）
```

```python
# main.py
from data_loader import load_csv_data
from analyzer import perform_analysis
from visualizer import create_chart

raw_data = load_csv_data('source.csv')
analyzed = perform_analysis(raw_data)
create_chart(analyzed)
```

### 流派三：Jupyter Notebook（探索分析、資料科學）

程式碼分格執行，資料停留在記憶體。適合反覆調整視覺化。

```bash
pip install jupyter
jupyter notebook    # 在瀏覽器開啟
```

## 三種流派比較

| 特性 | 單一腳本 | 模組化 | Jupyter |
|------|----------|--------|---------|
| 資料持久性 | 每次重新讀取 | 每次重新讀取 | **資料停在記憶體** |
| 除錯難易度 | 難（從頭跑）| 中 | **極易（修哪格跑哪格）**|
| 自動化潛力 | 極高 | 極高 | 低（通常手動操作）|
| 適合場景 | 排程腳本 | 大型系統 | 探索分析 |

## 常見問題

**`ModuleNotFoundError`**：先確認終端機前面有沒有 `(venv)` 標誌。沒有 → `source venv/bin/activate` 再重試。

**路徑有空格**：用反斜線跳脫（`Gooogle\ CLI`）或引號包覆（`"Gooogle CLI"`）。

**啟動 venv 後不需要 `pip3`**：在 `(venv)` 環境中，`pip` 和 `python` 自動對應到虛擬環境版本。

## 相關工具頁 / 概念頁

- `[[wiki/concepts/python-file-ecosystem]]` — Python 可生成的六大格式類別與套件
- `[[wiki/ai-workflow/python-html-data-dashboard]]` — 本機執行 Python + HTML 數據分析方案
- `[[wiki/ai-workflow/google-api-integration]]` — 本機 Python 環境是 Google API 整合的執行基礎

## 相關素材

- [[raw/Mac 用戶 Python 開發環境教學指南.md]]
