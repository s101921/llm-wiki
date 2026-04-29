---
title: 簡報生成七條技術路線
date: 2026-04-29
updated: 2026-04-29
type: concept
status: draft
tags: [presentation, pptx, html, marp, slidev, python-pptx, pptxgenjs, gemini-canvas]
sources: 1
private: false
---

# 簡報生成七條技術路線

**核心問題：AI 生成的簡報，哪些「可編輯」、哪些只是「圖片」？**

## 什麼是「可編輯 PPTX」？

`.pptx` 是改了副檔名的 ZIP 壓縮包，裡面是 **OOXML（Office Open XML）** 格式的 XML。

| 儲存方式 | 在 PowerPoint 的行為 |
|----------|---------------------|
| OOXML 原生標籤 `<p:sp>`, `<a:p>` | 可點擊、可修改文字、可移動 ✅ |
| `<p:pic>` 包著嵌入圖片 | 整張投影片是一張大圖，無法選取文字 ❌ |

**判斷方法**：在 PowerPoint 中能不能點擊文字並修改？

## 七條路線總覽

```
路線A  Markdown/HTML → 截圖(PNG/PDF) → 嵌入 PPTX     ❌ 不可編輯
路線B  Markdown/HTML → 瀏覽器即時渲染                  ❌ 非 PPTX 格式
路線C  AI → JSON 結構 → python-pptx 寫入              ✅ 可編輯（設計受限）
路線D  AI → JSON 結構 → pptxgenjs 精確定位             ✅ 可編輯（設計高自由）
路線E  AI 規格化 HTML → 平台前端工具轉換               ✅ 可編輯（平台綁定）
路線F  Agent 分析參考簡報 → 學習設計語言 → 重新生成     ✅ 可編輯（最高一致性）
路線G  HTML → WeasyPrint 向量 PDF → PDF 轉 PPTX       ✅ 文字可編輯（意外附加）
```

## 路線詳細說明

### 路線A：截圖流（Marp / Slidev）

- **代表工具**：Marp、Slidev、Quarto
- **流程**：Markdown → 瀏覽器截圖 → 嵌入 PPTX
- **結果**：PPTX 裡的每頁都是一張圖片，**完全不可編輯**
- **適用**：只需要「好看的視覺」、不需要後續編輯

### 路線B：HTML 瀏覽器渲染（Reveal.js）

- **代表工具**：Reveal.js
- **特色**：網頁原生格式，有動畫效果
- **限制**：不是 PPTX，無法在 PowerPoint 開啟

### 路線C：python-pptx（Python 直接寫 PPTX）

- **流程**：AI 生成 JSON 結構 → python-pptx 寫入 OOXML
- **優點**：純 Python，可編輯，適合程式自動化
- **缺點**：絕對座標定位，設計自由度有限；複雜排版需大量程式碼

**最佳實務**：先請設計師做好 PPTX 空白模板，再用 `python-pptx` 讀取模板，將圖表填入對應的**佔位符（Placeholder）**。

### 路線D：pptxgenjs（JavaScript 精確定位）

- **流程**：AI 生成 JSON 結構 → pptxgenjs 寫入
- **優點**：Node.js 環境，精確座標控制，設計自由度最高
- **適用**：需要精確視覺設計的自動化簡報

### 路線E：規格化 HTML → 平台前端轉換

- **代表**：Gemini Canvas（HTML → 前端渲染）
- **特色**：在 AI 對話中即時預覽
- **限制**：平台綁定，Single-File Mandate（見 [[wiki/tools/gemini-canvas]]）

### 路線F：PPTAgent（學習參考簡報）

- **流程**：Agent 分析現有精美簡報的設計語言 → 學習版型 → 生成同風格新簡報
- **優點**：最高設計一致性，可沿用企業現有視覺系統
- **技術**：多輪 Agent 推理，理解 XML 結構

### 路線G：WeasyPrint 向量 PDF 中轉

- **流程**：HTML（含 CSS 高級視覺效果）→ WeasyPrint 轉向量 PDF → PDF 轉 PPTX
- **特色**：意外地讓文字保留可編輯性（因為 PDF 是向量格式）
- **限制**：PDF 轉 PPTX 的版面可能跑版

## 工具選擇決策

| 場景 | 推薦路線 |
|------|----------|
| 快速原型 + 即時預覽 | 路線E（Gemini Canvas）|
| 程式自動化 + 可編輯 | 路線C（python-pptx）|
| 高設計自由 + 精確 | 路線D（pptxgenjs）|
| 沿用企業視覺系統 | 路線F（PPTAgent）|
| 投影用、不需編輯 | 路線A（Marp/Slidev）|
| 極致美感 HTML + 可編輯 | 路線G（WeasyPrint）|

## 與其他頁面的關係

- [[wiki/tools/gemini-canvas]] — 路線E 的具體工具：Canvas Block Syntax、Single-File Mandate
- [[wiki/marketing/presentation-architect/SKILL]] — 完整簡報生成 SKILL，使用路線A（Slidev）
- [[wiki/marketing/concept-visualizer/SKILL]] — 使用路線G（HTML → WeasyPrint → PPTX）
- [[wiki/concepts/python-file-ecosystem]] — python-pptx 是 Python 檔案生態中的簡報套件

## 相關素材

- [[raw/簡報生成技術知識庫.md]]
