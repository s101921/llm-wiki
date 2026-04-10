---
title: playwright-cli
date: 2026-04-10
updated: 2026-04-10
type: tool
status: growing
tags: [playwright, CLI, MCP, coding-agent, browser-automation, token-efficiency]
sources: 1
---

# playwright-cli

**CLI 介面｜瀏覽器自動化｜[github.com/microsoft/playwright-cli](https://github.com/microsoft/playwright-cli)｜免費開源**

---

## 核心功能

`playwright-cli` 把 Playwright 瀏覽器自動化包裝成命令列介面，讓 coding agent 以**極低 token 成本**操作真實瀏覽器。

**與 Playwright MCP 的關鍵差異：**

> CLI 不把 accessibility tree 或工具 schema 載入 LLM context，因此在需要同時處理 codebase + 瀏覽器的 coding agent 場景中，context 消耗大幅降低。

---

## CLI vs MCP 決策框架

| 條件 | 選 CLI | 選 MCP |
|------|--------|--------|
| **Agent 任務** | Coding agent（同時有大型 codebase） | 專屬瀏覽器自動化 loop |
| **Context 壓力** | 高（需省 token） | 低（可接受大 schema） |
| **自動化性質** | 明確步驟，目標確定 | 探索性、自愈測試 |
| **狀態需求** | Session + 可選持久化即可 | 需要持續推理頁面結構 |
| **長期執行** | 不需要 | 需要（長時間 autonomous workflow） |

**一句話原則：**  
> 有 codebase 就選 CLI；純瀏覽器探索選 MCP。

---

## 安裝與設定

```bash
# 安裝
npm install -g @playwright/cli@latest

# 安裝 Skills（讓 Claude Code、Copilot 等自動識別）
playwright-cli install --skills
```

安裝 skills 後，agent 不需要預先載入工具 schema，直接從 `playwright-cli --help` 輸出讀取可用指令。

---

## 核心指令

### 基本操作

```bash
playwright-cli open [url]         # 開啟瀏覽器
playwright-cli goto <url>         # 導航
playwright-cli snapshot           # 取得頁面快照（含元素 ref）
playwright-cli click <ref>        # 點擊元素
playwright-cli fill <ref> <text>  # 填入文字
playwright-cli screenshot         # 截圖
```

### 元素定位（三種方式）

```bash
playwright-cli click e15                          # Ref（快照 ID，最常用）
playwright-cli click "#main > button.submit"      # CSS Selector
playwright-cli click "getByRole('button', { name: 'Submit' })"  # Locator
```

### Session 管理

```bash
playwright-cli list               # 列出所有 session
playwright-cli -s=myapp open URL  # 在命名 session 操作
playwright-cli close-all          # 關閉所有瀏覽器
PLAYWRIGHT_CLI_SESSION=myapp claude .  # 環境變數指定 session
```

### Monitoring

```bash
playwright-cli show   # 開啟視覺化 dashboard，可即時監控所有 session
```

---

## 效果評估

**優點：**
- **Token 效率最高**：不載入 schema 或 accessibility tree，是 coding agent 的最佳選擇
- **Skills 整合**：與 Claude Code、GitHub Copilot 原生整合
- **Session 機制**：可命名、可持久化、可同時跑多個瀏覽器
- **監控友好**：`playwright-cli show` 讓人類隨時接管或觀察
- **功能完整**：涵蓋截圖、PDF、錄影、網路 mock、Cookie/Storage 管理

**限制：**
- 不適合需要持續推理頁面結構的複雜探索性任務（這類用 MCP）
- headless 預設，需加 `--headed` 才能看到瀏覽器
- Session 預設只存記憶體，關閉即失效（需 `--persistent` 才能跨 restart）

---

## 已知限制與注意事項

- CLI 的 snapshot 是每個指令後的靜態快照，不是即時 DOM；如果頁面動態更新，需再次 `snapshot`
- 命名 session 中的 `--persistent` profile 存放在 `.playwright-cli/` 目錄，要注意版控是否排除
- ⚠️ **CCR 環境不可用**：playwright-cli 只能在本機 Claude Code 使用。Claude Code Schedule Remote Agent（CCR）的網路限制導致 Chromium 下載失敗，playwright 安裝會報錯。CCR 中需要瀏覽器的任務請改用 RSS Feed、Firecrawl MCP 或 Browserless 等雲端方案。詳見 [[wiki/tools/ccr]]

---

## 與其他工具比較

| | playwright-cli | playwright-mcp | Puppeteer |
|--|---------------|----------------|-----------|
| **Token 效率** | ✅ 高 | ❌ 低 | ❌ 無 CLI skills |
| **Coding agent 整合** | ✅ Skills 原生 | 🟡 需設定 MCP | ❌ 需自行包裝 |
| **探索性自動化** | 🟡 尚可 | ✅ 最佳 | 🟡 尚可 |
| **狀態持久化** | ✅ Session + persistent | ✅ 持續 context | ❌ 無 |
| **費用** | 免費 | 免費 | 免費 |

---

## 相關頁面

- [[wiki/summaries/playwright-cli]] — 完整 README 摘要
- [[wiki/ai-workflow/context-engineering-coding-agents]] — CLI 選擇直接回應「太多 MCP 工具 = Dumb Zone」，是 context 管理的實際工具選型
