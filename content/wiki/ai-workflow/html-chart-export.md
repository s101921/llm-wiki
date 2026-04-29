---
title: HTML 圖表下載與匯出 SOP
date: 2026-04-29
updated: 2026-04-29
type: ai-workflow
status: draft
tags: [chart.js, echarts, canvas, html, download, export, data-visualization]
sources: 1
private: false
---

# HTML 圖表下載與匯出 SOP

**類型：AI Workflow｜用途：讓網頁動態圖表可以被使用者下載為靜態圖片｜工具：Canvas API / ECharts / html2canvas**

## 何時使用

- HTML 互動圖表需要提供「下載報表」功能
- 需要將數據儀表板的某個區塊截圖匯出
- 使用者需要把圖表插入 Word / 簡報

## 三種技術方案

### A. 套件內建功能（最推薦）

**代表套件**：Apache ECharts

**做法**：在圖表 option 設定中開啟 `toolbox` 的 `saveAsImage`：

```json
{
  "toolbox": {
    "feature": {
      "saveAsImage": {}
    }
  }
}
```

**優點**：零程式碼、支援 PNG/SVG、相容性最好

---

### B. Canvas API 轉換（Chart.js 適用）

**適用**：Chart.js 等以 `<canvas>` 繪製的圖表

**JavaScript 程式碼**：
```javascript
document.getElementById('downloadBtn').addEventListener('click', function() {
  const canvas = document.getElementById('myChart');
  
  // 強制白色背景（避免深色模式透明背景問題）
  const tempCanvas = document.createElement('canvas');
  tempCanvas.width = canvas.width;
  tempCanvas.height = canvas.height;
  const ctx = tempCanvas.getContext('2d');
  ctx.fillStyle = '#FFFFFF';
  ctx.fillRect(0, 0, tempCanvas.width, tempCanvas.height);
  ctx.drawImage(canvas, 0, 0);
  
  const link = document.createElement('a');
  link.download = 'chart.png';
  link.href = tempCanvas.toDataURL('image/png');
  link.click();
});
```

---

### C. DOM 節點截圖（整體報表區塊）

**適用**：需要截取包含文字、KPI 卡、多圖表的整個 `<div>`

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
<script>
document.getElementById('downloadBtn').addEventListener('click', function() {
  html2canvas(document.getElementById('dashboard'), {
    backgroundColor: '#FFFFFF'
  }).then(function(canvas) {
    const link = document.createElement('a');
    link.download = 'dashboard.png';
    link.href = canvas.toDataURL();
    link.click();
  });
});
</script>
```

## 給 LLM 的 Prompt 模板

### 情境一：特定圖表套件

> 「請建立一個包含數據圖表的 HTML 檔案。
> 1. 使用 **Chart.js** 繪製銷售趨勢折線圖。
> 2. 在圖表下方新增按鈕『下載報表圖片』。
> 3. 點擊按鈕時，將 Canvas 圖表轉為 PNG 並觸發瀏覽器下載。
> 4. 確保圖片背景為白色（`#FFFFFF`）。」

### 情境二：完整儀表板（建議）

> 「請分析我提供的數據，產出一個專業數據儀表板網頁。
> 1. 使用 **Apache ECharts** 繪圖。
> 2. 在每一張圖表的 option 中，啟用 toolbox 的 saveAsImage 功能。
> 3. 商務風格排版，上方摘要 3 個重要洞察。
> 
> 數據：[貼上你的數據]」

## 常見問題

### 圖片背景透明
PNG 格式預設透明背景。深色模式下黑色文字看不見。**務必強制設定白色背景** `#FFFFFF`。

### 高解析度印刷需求
調整 `devicePixelRatio`：
```javascript
const ratio = window.devicePixelRatio || 1;
canvas.width = originalWidth * ratio;
canvas.height = originalHeight * ratio;
```

### 跨網域圖片（CORS）
若圖表引用外部圖片，Canvas 會進入「污染（Tainted）」狀態，無法下載。需確保圖片來源開啟 CORS 權限，或改用 base64 嵌入圖片。

## 環境需求

- 瀏覽器：Chrome / Edge / Safari（現代瀏覽器均支援）
- 函式庫：透過 CDN 直接引入，不需 npm install

## 相關工具頁 / 概念頁

- `[[wiki/ai-workflow/llm-interactive-chart]]` — 完整的 Python → Chart.js 流程
- `[[wiki/concepts/python-file-ecosystem]]` — 需要靜態圖片時，可改用 Matplotlib/Seaborn

## 相關素材

- [[raw/HTML數據儀表板：圖表下載與匯出技術手冊.md]]
