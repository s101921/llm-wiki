---
title: Context Engineering for Coding Agents
date: 2026-04-09
updated: 2026-04-09
type: ai-workflow
tags: [context-engineering, coding-agents, RPI, compaction, smart-zone, brownfield]
sources: 1
status: growing
---

# Context Engineering for Coding Agents

**為 coding agent 管理 context window 的系統性方法——讓模型永遠在 Smart Zone 工作，在複雜 codebase 中也能產出高品質程式碼。**

---

## 核心邏輯

LLM 是無狀態的。每次 token 的輸出只受當前 context window 的內容影響。因此：

> **唯一能提升輸出品質的方法，是放入更好的 tokens。**

Context Engineering 就是系統性地最佳化 context window 的**正確性、完整性、精簡度、與對話軌跡**。

---

## Smart Zone vs Dumb Zone

```
Context Window（~168K tokens，以 Claude Code 為例）
├── 0% ─────────────── 40% ──────────────── 100%
│          Smart Zone        │    Dumb Zone    │
│    高品質推理 / 好工具呼叫  │  品質明顯下滑   │
```

- **40%** 是經驗法則轉折點（依任務複雜度微調）
- 太多 MCP 工具 = 一開始就在 Dumb Zone（每個 MCP 工具的 schema 都佔用 context）
- 讀整份 5M lines 的 monorepo 說明文件 = 把 Smart Zone 全部用在理解，沒空間做事

> **實例：** [[wiki/tools/playwright-cli]] 用 CLI 取代 Playwright MCP，正是為了避免每次呼叫都把 accessibility tree 和工具 schema 載入 context。有 codebase 的 coding agent 應優先選 CLI 介面。

### Context 品質排序（最差 → 最好）

| 狀況 | 影響 |
|------|------|
| 錯誤資訊 | 最糟糕，模型往錯誤方向全速前進 |
| 缺失資訊 | 次糟糕，模型猜測或幻覺 |
| 過多雜訊 | 干擾推理，佔用 Smart Zone |
| 正確 + 完整 + 精簡 + 好軌跡 | 最佳 |

### Trajectory（對話軌跡）的重要性

對話若呈現「做錯 → 被罵 → 做錯 → 被罵」的模式，模型會預測下一步仍是「做錯」。**負向軌跡會自我強化**。與其持續糾正，不如開新 context。

---

## Intentional Compaction（刻意壓縮）

傳統做法：context 滿了才被動壓縮 → 常常品質已下滑。

**刻意壓縮**：在適當時機主動請 agent 把目前進度壓縮成一份精簡的 markdown 檔，再開新 context 繼續。

壓縮的理想內容：
- 確切的相關檔案路徑與行號
- 已知的系統行為與限制
- 排除已探索但無關的路徑
- 下一步的明確方向

這樣新 agent 跳過所有「理解 codebase」的步驟，直接投入工作。

---

## Sub-agents 的正確用途

❌ **錯誤**：前端 agent、後端 agent、QA agent（角色擬人化）

✅ **正確**：用 sub-agent 控制 parent context 的大小

```
Parent Agent（保持 Smart Zone）
    │
    └── 發出任務：「找出 SCM provider 是怎麼整合的」
         │
         Sub-agent（獨立 context，盡情搜尋）
              └── 回傳：「看 /src/scm/github.ts:147」
         │
    Parent 只讀那一個檔案，繼續工作
```

Sub-agent 吸收所有搜尋/閱讀的 context 消耗，parent 只拿結論。

---

## Research-Plan-Implement（RPI）

三階段工作流，全程在 Smart Zone：

### Phase 1：Research（研究）
- 目標：理解系統，找到正確檔案，保持客觀
- 可用 sub-agent 垂直切片 codebase，只收集與任務相關的真實資訊
- 產出：研究文件（含確切檔名 + 行號 + 系統行為）

**靜態文件 vs 按需 Context：**
> Repo 裡的說明文件隨 codebase 演進很快過時，「充滿謊言」。
> 按需 research 產出的是「此刻此任務的真實 context」，更可靠。

### Phase 2：Plan（計畫）
- 目標：壓縮意圖，逐步列出執行步驟
- 計畫品質標準：**讀完這份計畫，最笨的模型也不會搞砸它**
- 計畫應包含：實際 code snippet、確切步驟、每步測試方式
- 可供人類 review，是 **Mental Alignment** 的核心工具

### Phase 3：Implement（實作）
- 按計畫執行，context 保持小
- 不需要重新理解系統（已在前兩階段完成）

**RPI 的本質是 Compaction 的循環應用**，每個階段結束都是一次精簡。

---

## Mental Alignment（心智對齊）

隨著 AI 產出量增加，傳統 code review 難以跟上。計畫文件填補這個缺口：

- 技術負責人讀**計畫**，不必讀每一行 code，仍能理解 codebase 如何演進
- 計畫附在 PR 上（如 Mitchell 的 AMP threads 實踐），讓 reviewer 看到「步驟 + prompt + 結果」
- 早期抓到方向錯誤（計畫層），比事後改 code 成本低得多

> Code review 的真正目的是讓團隊對 codebase 變化保持共同理解，而不只是找 bug。

---

## 不要外包思考

> AI 只能放大你已有的思考，不能替代思考。

- **你必須讀計畫**，否則等於盲目執行
- 沒有完美 prompt，只有好的 context
- 複雜問題（如移除舊依賴）最終仍需要人類回白板重設計
- 人力投入的最高槓桿點：**Review research 和 plan**，而非 review code

```
一行錯誤的 research = 整個計畫方向跑偏 = 幾百行 slop
一段錯誤的計畫 = 幾百行 slop
一行錯誤的 code = 一行 slop
```

---

## 操作校準

| 任務複雜度 | 建議做法 |
|-----------|---------|
| 改按鈕顏色 | 直接跟 agent 說就好 |
| 小功能、單一 repo | 直接實作 |
| 中型功能、可能跨 repo | 做一次 research，再建計畫 |
| 複雜 brownfield 問題 | 完整 RPI + 頻繁 compaction |

沒有固定規則，要靠反覆練習校準自己的判斷。選一個工具練熟，不要在多個工具間來回切換。

---

## 與其他概念的關係

- [[wiki/concepts/ai-agent]] — Context Compaction 機制的底層（Soft Trim / Compaction / Hard Clear / New Session）
- [[wiki/concepts/rag]] — sub-agent research 的底層檢索機制
- [[wiki/ai-workflow/harnessing-engineering]] — 更大的框架：Context Engineering 是 Harnessing 六層之一（層 1）。Harnessing 涵蓋工具系統、執行編排、記憶狀態、評估觀測、失敗恢復，是 Agent 落地的完整系統

## 相關素材

- [[wiki/summaries/no-vibes-allowed-dex-horthy]] — 完整演講摘要
- [[wiki/tools/playwright-cli]] — CLI vs MCP token 效率取捨的具體工具案例
