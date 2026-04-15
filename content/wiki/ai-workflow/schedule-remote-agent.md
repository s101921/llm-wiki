---
title: Claude Code Schedule Remote Agent 設定 SOP
date: 2026-04-10
updated: 2026-04-10
type: ai-workflow
status: draft
tags: [ccr, schedule, remote-agent, automation, claude-code, notion, github]
sources: 0
---

# Claude Code Schedule Remote Agent 設定 SOP

**類型：AI 工具 SOP｜用途：設定定期自動執行的雲端 Agent｜費用：包含在 Claude Code 訂閱**

---

## 何時使用

- 需要每天/每週定期自動抓資料、整理報告、推送到 Notion 或 GitHub
- 任務不需要使用者手動觸發
- 任務不依賴本機電腦（使用者電腦可以關機）

> ⚠️ CCR 執行環境不支援瀏覽器自動化，設計任務時優先使用 RSS、公開 API、Firecrawl MCP。
> 詳見 [[wiki/tools/ccr]]

---

## 執行步驟

### Step 1：載入 RemoteTrigger 工具

在 Claude Code 對話中輸入 `/schedule`，或用 ToolSearch 載入：

```
ToolSearch: select:RemoteTrigger,AskUserQuestion
```

---

### Step 2：定義任務內容

設計 Agent Prompt 時，必須包含以下資訊（Agent 從零開始，沒有任何上下文）：

```
✅ 認證資訊（API Key、PAT，直接寫入 prompt）
✅ 目標服務（GitHub repo URL、Notion 頁面 ID）
✅ 完整執行步驟（Step 1, 2, 3...）
✅ 錯誤處理邏輯（各步驟獨立，單一失敗不影響其他）
✅ 完成後的輸出格式
```

---

### Step 3：設定 Cron 排程（UTC）

Cron 永遠是 UTC，台灣時間需減 8 小時：

| 台灣時間 | UTC | Cron |
|---------|-----|------|
| 每天早上 9:00 | 01:00 | `0 1 * * *` |
| 每天下午 5:00 | 09:00 | `0 9 * * *` |
| 每天晚上 9:00 | 13:00 | `0 13 * * *` |

> 最小間隔：1 小時（`*/30 * * * *` 會被拒絕）

---

### Step 4：建立 Trigger

```json
{
  "name": "任務名稱",
  "cron_expression": "0 9 * * *",
  "enabled": true,
  "mcp_connections": [
    {
      "connector_uuid": "MCP connector 的 UUID",
      "name": "Notion",
      "url": "https://mcp.notion.com/mcp"
    }
  ],
  "job_config": {
    "ccr": {
      "environment_id": "env_01Qtq2FEgzgKYqA3sgX3x2zp",
      "session_context": {
        "model": "claude-sonnet-4-6",
        "sources": [],
        "allowed_tools": ["Bash", "Read", "Write", "Edit", "Glob", "Grep"]
      },
      "events": [
        {
          "data": {
            "uuid": "<生成一個小寫 v4 UUID>",
            "session_id": "",
            "type": "user",
            "parent_tool_use_id": null,
            "message": {
              "role": "user",
              "content": "完整的 Agent Prompt"
            }
          }
        }
      ]
    }
  }
}
```

> ⚠️ **`sources` 留空**：如果 GitHub repo 是私有的，不要放在 sources，否則 CCR 啟動時會因無法 clone 而報 `failed to start run`。
> 改法：在 prompt 裡用 PAT 做 `git clone https://x-access-token:PAT@github.com/...`

---

### Step 5：GitHub 整合注意事項

使用 Fine-grained PAT 時，必須確認以下權限開啟：

| 權限 | 需求 |
|------|------|
| `Contents: Read and write` | 必須（用於 git push）|
| `Metadata: Read-only` | 自動帶入 |

Git clone 指令格式：
```bash
git clone https://x-access-token:YOUR_PAT@github.com/username/repo.git /tmp/repo
```

---

### Step 6：Notion MCP 整合

Notion MCP 透過 claude.ai 的 OAuth 連接，不需要 Notion API Token。

在建立 trigger 時，將 Notion connector 加入 `mcp_connections`：
```json
{
  "connector_uuid": "82dc9d27-81a2-44f4-acb5-0e5ff2f68774",
  "name": "Notion",
  "url": "https://mcp.notion.com/mcp"
}
```

在 Agent Prompt 中說明使用 `notion-create-pages` 工具，提供目標頁面 ID（格式：`xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`）。

---

### Step 7：測試與確認

建立後：
1. 前往 `https://claude.ai/code/scheduled/{TRIGGER_ID}` 手動點擊 Run Now
2. 確認執行 log 無錯誤
3. 確認 GitHub repo 有新 commit、Notion 有新頁面

---

## 常見錯誤排查

| 現象 | 原因 | 解法 |
|------|------|------|
| `failed to start run` | `sources` 中有私有 repo | 移除 sources，改用 prompt 中的 PAT clone |
| GitHub push 403 | PAT 缺少 `Contents: Write` | 到 GitHub 編輯 PAT，補齊權限 |
| Playwright 安裝失敗 | CCR 網路限制 | 改用 RSS / Firecrawl / requests |
| Notion MCP 工具找不到 | 沒加 `mcp_connections` | 重新 update trigger 加入 connector |
| Agent 回傳假資料 | WebSearch 估算，不是真實資料 | 改用官方 API 或 RSS |

---

## Prompt 撰寫原則

```
1. 認證資訊放在最前面，清楚標示
2. 用 Step 1, 2, 3 明確分段
3. 每個 Step 說明：做什麼 + 指令範例
4. 各 Step 獨立（一個失敗不影響其他）
5. 最後要求輸出執行摘要（成功/失敗 + 關鍵結果）
6. TODAY_DATE 這類動態值讓 Agent 自己用 bash 取得，不要硬寫
```

---

## 相關頁面

- [[wiki/tools/ccr]] — CCR 環境能力與限制詳解
- [[wiki/tools/playwright-cli]] — 本機瀏覽器自動化（CCR 不可用）
- [[wiki/concepts/ai-agent]] — Cron Job 機制的底層概念（含心跳、排程、Compaction 說明）
