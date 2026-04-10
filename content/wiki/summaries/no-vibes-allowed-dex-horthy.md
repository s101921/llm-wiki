---
title: "No Vibes Allowed: Solving Hard Problems in Complex Codebases — Dex Horthy, HumanLayer"
date: 2026-04-09
updated: 2026-04-09
type: summary
tags: [context-engineering, coding-agents, research-plan-implement, compaction, brownfield]
sources: 1
status: stable
---

# No Vibes Allowed: Solving Hard Problems in Complex Codebases

**來源：** AI Engineer 2025（2025-12-03）｜講者：Dex Horthy（HumanLayer）
**原始素材：** [[Clippings/No Vibes Allowed Solving Hard Problems in Complex Codebases – Dex Horthy, HumanLayer.md]]

---

## 核心主張

AI coding 工具對 brownfield（既有複雜）程式碼的效果很差，原因不在模型，在於沒有做好 **context engineering**。解法是：管理好你的 context window，讓模型永遠在「Smart Zone」工作。

---

## 問題背景

- Eigor 調查 10 萬名開發者：用 AI 寫程式，大量時間在 rework 上週 AI 生的 slop
- Greenfield（新專案）很好用；Brownfield（舊複雜 codebase）幾乎沒用
- 講者本人第一次用 Claude Code 印象普通，後來團隊研究出方法：生產力 2-3x，整個協作方式都改了

---

## 關鍵概念

### 1. Smart Zone vs Dumb Zone
- Context window 約 168K tokens（以 Claude Code 為例），保留部分給輸出
- **大約 40% 使用率**是轉折點——超過後模型品質明顯下降（Dumb Zone）
- 太多 MCP 工具 = 一直在 Dumb Zone 工作

### 2. Context 品質三軸
最差到最好：
- ❌ Incorrect（錯誤資訊）
- ❌ Missing（遺漏資訊）
- ⚠️ Too much noise（過多雜訊）
- ✅ Correct + Complete + Concise + Good trajectory

**Trajectory** 很關鍵：如果對話的模式是「做錯 → 被罵 → 做錯 → 被罵」，模型會預測下一步仍是「做錯」。

### 3. Intentional Compaction（刻意壓縮）
- 主動請 agent 把目前 context 壓縮成一份 markdown 檔
- 包含：**相關的確切檔名與行號**，而非整個 codebase 概覽
- 新 agent 從這份檔案啟動，跳過所有搜尋/理解步驟，直接工作
- 比 context 滿了才被動壓縮好得多

### 4. Sub-agents 的正確用途
- ❌ 錯誤用法：「前端 agent、後端 agent、QA agent」（角色擬人化）
- ✅ 正確用法：用來**控制 context**
- 例：派一個 sub-agent 去搜尋/理解某功能的運作方式，只回傳「你要看 /src/foo.ts 第 42 行」——parent agent 只讀那一個檔案就夠

### 5. Research-Plan-Implement（RPI）
三階段工作流，全程保持在 Smart Zone：

| 階段 | 目的 | 產出 |
|------|------|------|
| Research | 理解系統，找到正確檔案，保持客觀 | 研究文件（含真實檔名 + 行號）|
| Plan | 壓縮意圖，逐步列出執行步驟 | 計畫檔案（含實際 code snippet）|
| Implement | 按計畫執行，context 保持小 | PR / 修改 |

計畫品質的目標：「讀完這份計畫，世界上最笨的模型也不會搞砸它。」

### 6. Mental Alignment（心智對齊）
- Code review 的真正目的不是找 bug，是讓團隊了解 codebase 如何演進
- 隨著 AI 產出量增加，**計畫文件取代 code review** 成為對齊工具
- 技術負責人可以讀計畫，不必讀每一行 code
- Plan 附在 PR 上（如 AMP threads），比純 diff 更能讓 reviewer 理解脈絡

### 7. 不要外包思考
- AI 只能放大你已有的思考，不能替代思考
- 沒有完美的 prompt
- 你必須讀計畫，不讀計畫等於盲目執行
- Dex 嘗試對 Parquet Java 移除 Hadoop 依賴，最後失敗——最終要回到白板重新設計

### 8. 靜態文件 vs 按需壓縮 Context
- Repo 裡的 CLAUDE.md / 說明文件：隨 codebase 演進很快過時，「充滿謊言」
- 更好的做法：on-demand，由 research prompt 針對當前任務垂直切片 codebase，產出「此任務相關的真實 context」

---

## 實際案例

- **Boundary ML（Rust，30 萬行）**：一個週末 7 小時，交出 3.5 萬行 PR，CTO 隔天看到以為是正常 contributor
- **Parquet Java + Hadoop**：失敗案例；太複雜，必須回白板重設計
- **HumanLayer 自己的團隊**：3 人 8 週，從普通使用到 2-3x 產出，完全改變協作方式

---

## 關於 Semantic Diffusion

Martin Fowler 2006 年提出的概念：一個好詞彙 + 好定義出現，大家各自解讀，詞彙意義擴散、失效。

- 「Agent」已語義擴散：人、microservice、chatbot、workflow
- 「Spec-driven dev」已語義擴散：更長的 prompt、PRD、markdown files、library 文件
- 「RPI」也可能擴散——重要的是概念（compaction + context engineering），不是縮寫

---

## 連結

- [[wiki/ai-workflow/context-engineering-coding-agents]] — 主要概念頁
- [[wiki/concepts/ai-agent]] — Agent 架構基礎，Context Compaction 機制
