
**Step 1 — Python 數據分析（bash_tool）**

我在一個 Ubuntu 容器裡執行 Python 腳本，用 `csv` 標準庫讀取三個檔案，然做了以下計算：

- 用 `dict` 建立產品主檔、客戶主檔的 lookup table

- 對每一筆交易 join 產品線、通路類型、區域、客戶分級

- 用 `defaultdict(float)` 分別 aggregate：月度、業務員、產品線、通路、區域、Top產品、Top客戶、客戶分級

輸出是純文字的 summary 數字，印在 stdout 裡回傳給我。

---

**Step 2 — 我（Claude）判斷洞察與圖表設計**

拿到數字之後，我在 context 裡直接推理：

- 哪些維度值得視覺化（月度趨勢 → 折線、佔比 → 甜甜圈、排名 → 水平長條）

- 哪些數字有異常值值得 callout（1月高峰、張家豪落差、A級集中）

- 如何安排版面層次（KPI卡 → 趨勢 → 結構分析 → 洞察卡）
  
這步沒有呼叫任何工具，純粹是 reasoning。


---

  

**Step 3 — 寫 HTML + Chart.js 腳本（show_widget）**

我把所有數字硬編碼進 HTML 字串，直接送給 `visualize:show_widget` 工具渲染。技術棧是：

- 版面：純 HTML + inline CSS，用 CSS variables 自動適配深淺色模式

- 圖表：Chart.js 4.4.1（從 cdnjs 載入 UMD build）

- 數據：我直接把 Python 算好的數字寫進 `data: [738, 378, 573...]`，沒有任何 API call 或資料庫查詢
---

**整個流程的技術架構圖：**

```

你的 CSV 檔案

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