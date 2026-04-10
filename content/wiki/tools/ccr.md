---
title: Claude Code Remote (CCR)
date: 2026-04-10
updated: 2026-04-10
type: tool
status: draft
tags: [ccr, claude-code, remote-agent, schedule, automation, cloud]
sources: 0
---

# Claude Code Remote (CCR)

**雲端執行環境｜Anthropic 管理｜Schedule Remote Agent 的執行容器｜包含在 Claude Code 訂閱**

---

## 核心定義

CCR（Claude Code Remote）是 Anthropic 提供的雲端沙盒容器，是 Claude Code Schedule 排程功能的底層執行環境。每次排程觸發，就會啟動一個全新的、隔離的 CCR 容器，執行完畢後整個環境銷毀。

```
你的電腦（Claude Code）
    ↓ 設定排程
Anthropic 雲端
    └── 每次觸發 → 啟動 CCR 容器 → 執行 Agent Prompt → 環境銷毀
```

---

## CCR 能做什麼

| 能力 | 說明 |
|------|------|
| **Bash / Python / Node.js 執行** | 可以跑腳本、安裝輕量套件 |
| **外部 API 呼叫** | 透過 HTTP 呼叫任何公開 API |
| **MCP 連接器** | 使用 claude.ai 已連接的 MCP（Notion、Firecrawl 等） |
| **Git 操作** | clone（需 PAT 驗證）、commit、push |
| **臨時檔案讀寫** | 在 `/tmp/` 建立、處理檔案（但不持久） |
| **WebSearch / WebFetch** | 若 prompt 中開放這些 tool |

---

## CCR 不能做什麼（硬性限制）

| 限制 | 原因 |
|------|------|
| **瀏覽器自動化（Playwright、Puppeteer）** | 無 GUI 環境，且網路限制導致 Chromium 無法下載 |
| **下載大型 binary** | 網路出口受限，~100MB 以上的套件通常失敗 |
| **連接使用者本機** | 完全隔離，無法寫入 `~/Desktop` 或任何本地路徑 |
| **本機 crontab 設定** | `crontab` 指令只對 CCR 容器有效，容器銷毀後消失 |
| **持久性本地儲存** | `/tmp/` 執行後消失，資料必須推送到外部（GitHub、Notion）|
| **自訂 Docker Image** | CCR 不開放自訂執行環境，固定基礎鏡像 |

---

## 資料持久化的正確方式

因為 CCR 環境執行後銷毀，任何要保留的資料都必須在執行中推送到外部：

```
CCR 執行中
    ├── ✅ git push → GitHub repo（最常用）
    ├── ✅ Notion MCP → 建立/更新 Notion 頁面
    ├── ✅ HTTP POST → 任何支援 API 的服務
    └── ❌ 存到本機 → 不可能
```

---

## 瀏覽器自動化的替代方案

| 方案 | 適用場景 | CCR 可用？ |
|------|---------|-----------|
| **RSS Feed / 公開 API** | 有官方資料端點的服務（如 Google Trends RSS） | ✅ 優先選 |
| **Firecrawl MCP** | 一般公開網頁抓取（不需登入） | ✅ 可用 |
| **requests + BeautifulSoup** | 靜態 HTML 頁面 | ✅ 可用 |
| **Browserless / Browserbase** | 需要 JS 渲染的動態頁面，透過 WebSocket 連接雲端瀏覽器 | ✅ 需付費帳號 |
| **Playwright（直接安裝）** | — | ❌ CCR 網路限制導致失敗 |
| **自製 Docker Image + Playwright** | — | ❌ CCR 不允許自訂環境 |

> **實戰案例**：Google Trends TW 有官方 RSS Feed（`https://trends.google.com.tw/trending/rss?geo=TW`），直接 curl 拿到真實資料，完全不需要瀏覽器。

---

## 已知失敗模式

| 錯誤 | 原因 | 修法 |
|------|------|------|
| `failed to start run` | `sources` 中放了私有 repo，CCR 啟動時無法 clone | 移除 sources 中的 repo，改在 prompt 裡用 PAT 做 `git clone` |
| GitHub push 403 | Fine-grained PAT 缺少 `Contents: Read and write` 權限 | 到 GitHub → Settings → PAT 編輯，補齊 Contents 權限 |
| Playwright 安裝失敗 | CCR 網路限制，Chromium binary 下載被擋 | 改用 RSS / Firecrawl / Browserless |
| Notion MCP 找不到 | trigger 設定中沒有加 `mcp_connections` | 建立 trigger 時加入 Notion MCP connector |

---

## CCR vs 本機 Skill + crontab

當任務需要瀏覽器、本機檔案、或完整工具支援時，可以改用**本機 Skill + Mac crontab**替代 CCR：

| | CCR 排程 | 本機 Skill + crontab |
|--|---------|-----------------|
| **電腦需要開著** | ❌ 不需要（跑在 Anthropic 雲端） | ✅ 需要 |
| **Playwright / 瀏覽器** | ❌ 不可用 | ✅ 完全可用 |
| **本機檔案存取** | ❌ 不行 | ✅ 可存到任意路徑 |
| **設定複雜度** | 中（需設定 trigger） | 低（SKILL.md + crontab 一行）|
| **費用** | 包含在訂閱 | 包含在訂閱 |

### 本機 crontab 說明

crontab 是 Mac 內建排程系統，**設定一次後自動在背景定時執行，不需要手動輸入指令**。

**Crontab 語法：**
```
分 時 日 月 週 指令
0  17 *  *  *  /usr/local/bin/claude --print "/trends"
```

常用範例：
```
0 17 * * *    → 每天 17:00
0 9  * * 1-5  → 平日早上 9:00
*/30 * * * *  → 每 30 分鐘
```

**設定步驟（只做一次）：**

```bash
# 1. 確認 claude 路徑
which claude

# 2. 開啟編輯器
crontab -e

# 3. 加入排程（建議同時記錄 log）
0 17 * * * /usr/local/bin/claude --print "/trends" >> ~/Desktop/trends/cron.log 2>&1
```

**crontab 與 Skill 的關係：**

```
crontab（Mac 系統層）  →  負責「什麼時間執行」
        ↓
claude --print "/trends"
        ↓
/trends skill            →  負責「執行什麼內容」
```

兩者完全獨立。skill 內容怎麼改都不影響 crontab；crontab 也只是一個觸發器，不包含任何業務邏輯。

**crontab 不只能觸發 Skill，也可以跑任何 bash 腳本：**

```bash
# 例如每天早上 9 點同步 Obsidian Vault 到 GitHub
0 9 * * * /Users/warren/Desktop/llm-wiki/sync.sh >> /Users/warren/Desktop/llm-wiki/sync.log 2>&1
```

**查詢與管理：**

| 指令 | 作用 |
|------|------|
| `crontab -l` | 列出所有已設定的排程 |
| `crontab -e` | 編輯排程 |
| `crontab -r` | 刪除全部排程（⚠️ 不可逆） |

crontab 設定沒有獨立的 GUI 或清單介面，永遠透過以上三個指令操作。

**查看執行記錄：**
```bash
cat ~/Desktop/trends/cron.log      # /trends 執行記錄
cat ~/Desktop/llm-wiki/sync.log    # sync.sh 執行記錄
```

**執行條件：**

| 狀況 | 結果 |
|------|------|
| 電腦開著、到了排程時間 | ✅ 自動執行 |
| 電腦關機 | ❌ 跳過，不補跑 |
| 電腦睡眠 | ❌ 預設跳過 |
| 蓋上螢幕但插電（關閉睡眠）| ✅ 可執行 |

> **選擇原則**：Mac 平常都開著 → 用本機 crontab，功能最完整。常關機或需要無人值守 → 用 CCR，但需繞開瀏覽器限制。

---

## 相關頁面

- [[wiki/ai-workflow/schedule-remote-agent]] — 設定 CCR 排程任務的 SOP
- [[wiki/tools/playwright-cli]] — 本機瀏覽器自動化（CCR 不可用，本機 Claude Code 可用）
