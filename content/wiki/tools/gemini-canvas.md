---
title: Gemini Canvas — HTML 簡報生成
date: 2026-04-29
updated: 2026-04-29
type: tool
status: draft
tags: [gemini, canvas, presentation, html, prompt]
sources: 1
private: false
---

# Gemini Canvas — HTML 簡報生成

**類型：AI 工具｜用途：在瀏覽器右側 Canvas 畫面即時渲染 HTML 簡報｜費用：Gemini 標準方案**

## 核心功能

Gemini Canvas 是 Google Gemini 內建的「沉浸式 UI」環境，可在對話右側即時渲染完整的 HTML 文件，讓 AI 直接輸出可瀏覽的投影片或互動頁面，無需離開聊天介面。

## 已知失敗模式

### 1. 碎裂的多檔輸出（違反 Single-File Mandate）
Canvas 引擎要求所有結構與樣式必須封裝在**同一個 HTML 檔案**內。若 AI 將投影片拆成多個 `.html` 檔，系統無法提供完整預覽。

### 2. AI 誤判自身權限（退縮成傳統助理模式）
AI 可能誤以為自己「無法在 Canvas 執行渲染」，而退縮成「提供程式碼請你自己執行」的模式。正確行為是直接輸出完整 HTML，讓系統渲染。

## 正確觸發方式

- 將所有投影片的 HTML 結構（`#slide1`, `#slide2`...）與 CSS 全部合併進**同一個 `.html` 檔案**
- 使用正確的程式碼區塊標記語法（Canvas Block Syntax）觸發右側預覽引擎
- 多張投影片用垂直排列（`display: flex; flex-direction: column; gap: 24px;`）

## Prompt 防呆規範（可直接貼入 System Prompt）

```
### ⚠️ 簡報生成與畫布渲染絕對規範 (CRITICAL RULES) ⚠️

1. 單一檔案強制原則：
   - 所有投影片、HTML 結構、CSS 樣式必須全部合併輸出在同一個 .html 檔案中。
   - 禁止將投影片拆成多個獨立 HTML 檔案。

2. 正確觸發預覽 UI：
   - 不要說「請你在本地端執行」或「我沒有匯出權限」。
   - 直接輸出完整 HTML 原始碼，讓系統在右側畫布渲染。

3. CSS 隔離與相容性：
   - 所有版型 CSS 整合進唯一的 <style> 標籤。
   - .slide-container 具備 width: 1280px; height: 720px; flex-shrink: 0;

4. PPTX 匯出相容性（若需匯出成 PowerPoint）：
   - 使用語意化 HTML（div, h1, p, span）+ 標準 Flexbox/Grid
   - 顏色使用標準 HEX 或 RGBA
   - 避免 CSS filter、clip-path、多層疊加背景（這些在轉 PPTX 時會破圖）
```

## 適用場景

- 快速原型：在 Gemini 對話中即時預覽視覺化簡報
- 單次輸出：不需要版本管理的一次性簡報
- 教學示範：讓學員直接看到 AI 生成的可互動頁面

## 已知限制

- Canvas 環境不支援多檔案（每次只能渲染一個 HTML）
- 生成的 HTML 若使用複雜 CSS（clip-path、filter）將無法正常匯出成 PPTX
- 不適合需要多人協作或長期維護的簡報專案

## 相關 Skill 頁

- `[[wiki/concepts/presentation-generation-routes]]` — Canvas 是路線E（規格化 HTML → 平台前端轉換）；了解其他六條路線的可編輯性比較
- `[[wiki/marketing/presentation-architect/SKILL]]` — 完整簡報生產流程（Slidev + AI 圖片）；Canvas 是快速原型替代方案
- `[[wiki/marketing/concept-visualizer/SKILL]]` — 另一種視覺化輸出：PPTX 格式，適合需要匯出的場景

## 相關素材

- `[[raw/Gemini Canvas簡報生成問題.md]]`（原始素材，已 ingest）
