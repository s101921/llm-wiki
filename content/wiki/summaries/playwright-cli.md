---
title: playwright-cli — Coding Agent 的 Token-Efficient 瀏覽器自動化 CLI
date: 2026-04-10
updated: 2026-04-10
type: summary
status: stable
tags: [playwright, CLI, MCP, coding-agent, browser-automation, token-efficiency]
sources: 1
---

# playwright-cli — Coding Agent 的 Token-Efficient 瀏覽器自動化 CLI

**來源：** [[Clippings/microsoftplaywright-cli CLI for common Playwright actions. Record and generate Playwright code, inspect selectors and take screenshots..md]]  
**類型：** GitHub README（microsoft/playwright-cli）  
**日期：** 2026-04-10

---

## 素材核心主張

`playwright-cli` 是 Microsoft 推出的 CLI 介面，讓 coding agent 用命令列操作 Playwright 瀏覽器——而不是透過 MCP Server。

核心論點：**對 coding agent 來說，CLI 比 MCP 更省 token、更適合大型 codebase 環境。**

---

## 重點提取

### CLI vs MCP 的取捨邏輯

| | CLI（playwright-cli） | MCP（playwright-mcp） |
|--|----------------------|----------------------|
| **Token 效率** | 高。不把 accessibility tree 或工具 schema 載入 context | 低。每次呼叫工具需載入完整 schema |
| **適用場景** | Coding agent，需同時處理 codebase + 瀏覽器自動化 | 探索性自動化、需要持續追蹤頁面狀態的長流程 |
| **狀態管理** | Session-based，可持久化到磁碟 | 持久瀏覽器 context，狀態保持在 MCP Server |
| **互動模式** | 指令逐步執行，每步回傳 snapshot | MCP loop，可持續推理頁面結構 |

> **CLI 最適合**：高吞吐量 coding agent，必須在有限 context window 內同時管理 browser + codebase + 推理。  
> **MCP 最適合**：自愈測試、長時間自主工作流程、需要持續 browser context 的場景。

### 安裝方式

```bash
npm install -g @playwright/cli@latest
playwright-cli install --skills   # 安裝 Skills（讓 Claude Code 等 agent 能讀取）
```

### Skills 整合

`playwright-cli install --skills` 會讓 Claude Code、GitHub Copilot 等 coding agent 的 skill 系統自動識別可用指令。Agent 不需要預先載入 schema，直接從 `--help` 輸出讀指令。

### Sessions 機制

- 預設：瀏覽器 profile 保存在記憶體（關閉即失效）
- `--persistent`：儲存到磁碟，跨 browser restart 保留
- 命名 session：`-s=name`，同時管理多個瀏覽器實例
- `PLAYWRIGHT_CLI_SESSION=name`：環境變數指定預設 session

### Monitoring Dashboard

`playwright-cli show` 開啟視覺化控制台，可即時監控所有 session 的截圖、URL、頁籤，也支援接管滑鼠鍵盤。

### 元素定位方式（三種）

1. **Ref**（快照 ID）：`playwright-cli click e15`
2. **CSS Selector**：`playwright-cli click "#main > button.submit"`
3. **Playwright Locator**：`playwright-cli click "getByRole('button', { name: 'Submit' })"`

---

## 連結至知識層

- [[wiki/tools/playwright-cli]] — 工具評估頁
- [[wiki/ai-workflow/context-engineering-coding-agents]] — CLI 選擇直接回應「太多 MCP 工具 = Dumb Zone」論點
