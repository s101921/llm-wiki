---
title: Google Sheets API + Gemini API 整合 SOP
date: 2026-04-29
updated: 2026-04-29
type: ai-workflow
status: draft
tags: [google-sheets, gemini, gcp, api, service-account, claude-code]
sources: 2
private: false
---

# Google Sheets API + Gemini API 整合 SOP

**類型：AI Workflow｜用途：讓 AI 讀取 Google 試算表資料並呼叫 Gemini API 進行分析，結果寫回試算表｜工具：GCP + Claude Code 或 IDE/CLI**

## 何時使用

- 需要 AI 自動讀取 Google Sheets 數據並進行摘要或分析
- 想讓 Claude Code 直接操作 Google API
- 需要比較「Claude Code 代理開發」vs「傳統 IDE/CLI 開發」的差異

## 前置設定（三個 GCP 步驟）

### Step 1：建立 GCP 專案與啟用 API

| 步驟 | 動作 | 目的 |
|------|------|------|
| 建立 GCP 專案 | Google Cloud Console → 新增專案 | 資源隔離與計費綁定 |
| 啟用 Sheets API | API 和服務 → 程式庫 → Google Sheets API → 啟用 | 開啟讀取試算表的權限 |
| 啟用 Drive API | 程式庫 → Google Drive API → 啟用（建議） | 讓程式能「尋找」試算表檔案 |

### Step 2：建立服務帳戶（機器人身分）

| 步驟 | 動作 | 目的 |
|------|------|------|
| 建立服務帳戶 | API 和服務 → 憑證 → 建立憑證 → 服務帳戶 | 建立屬於程式的「虛擬信箱」（結尾是 iam.gserviceaccount.com）|
| 下載 JSON 金鑰 | 服務帳戶 → 金鑰 → 新增金鑰 → JSON 格式 → 下載 | 唯一憑證；**絕對不能上傳到公開 GitHub** |
| 授權試算表 | Google 試算表 → 共用 → 貼上服務帳戶 Email → 設為「編輯者」| 讓機器人有檔案存取權限 |

### Step 3：取得 Gemini API Key

| 步驟 | 動作 |
|------|------|
| 登入 Google AI Studio | aistudio.google.com |
| 取得 API Key | Get API key → Create API key（可綁定 GCP 專案）|
| 確認模型名稱 | `gemini-2.5-flash-image-preview`（Nano Banana 實驗版）|

## 執行方案 A：Claude Code 代理開發

### Step 4：Claude Code 環境設定

```bash
# 安裝 Claude Code CLI
npm install -g @anthropic-ai/claude-code

# 建立專案結構
mkdir ai_project
# 將 credentials.json 放入資料夾

# 建立 .env 檔案
GEMINI_API_KEY=你的金鑰
GOOGLE_APPLICATION_CREDENTIALS=./credentials.json
```

### Step 5：啟動 Claude Code 並下達 Prompt

```
claude
```

**Prompt 範本**：
> 「請用 Python 寫一個腳本，讀取 .env 中的金鑰。使用 Google Sheets API 讀取試算表（ID: xxx）的資料，並將資料餵給 Gemini API（使用模型 gemini-2.5-flash-image-preview）進行摘要，最後將結果寫回試算表。」

**Claude Code 會自動**：生成程式碼 → 安裝必要套件（google-api-python-client, google-genai）→ 執行 → 自動 Debug

## 執行方案 B：傳統 IDE/CLI 開發

### Step 4：手動安裝環境

```bash
# 安裝 VS Code + Python
# 在 CLI 安裝套件
pip install google-api-python-client google-genai python-dotenv
```

### Step 5：撰寫 Python 核心邏輯（`main.py`）

```python
from dotenv import load_dotenv
import os, gspread, json
from google.oauth2.service_account import Credentials
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# GCP 憑證
creds = Credentials.from_service_account_file(
    os.getenv('GOOGLE_APPLICATION_CREDENTIALS'),
    scopes=['https://spreadsheets.google.com/feeds']
)
client = gspread.authorize(creds)

# 讀取 Sheets
sheet = client.open_by_key('試算表ID').sheet1
data = sheet.get_all_records()

# Gemini 分析
model = genai.GenerativeModel('gemini-2.5-flash-image-preview')
response = model.generate_content(f"分析這份銷售數據：{json.dumps(data)}")

# 寫回 Sheets
sheet.update('A1', [[response.text]])
```

### Step 6：執行

```bash
python main.py
```

## 兩種開發方式比較

| 比較維度 | 傳統 IDE + CLI | Claude Code 代理 |
|----------|---------------|-----------------|
| 套件安裝 | 手動（pip install...）| 自動（AI 自己安裝）|
| 程式碼撰寫 | 手動打字或複製貼上 | AI 直接修改實體檔案 |
| 除錯流程 | 手動看 CLI 報錯 → Google → 改 Code → 重跑 | AI 自動讀報錯 → 自動改 Code → 自動重跑 |
| 學習曲線 | 較陡峭（需了解語法與報錯訊息）| 較平緩（只需清楚定義需求）|

## 安全注意事項

- `credentials.json` 和 `.env` 都不能提交到 Git（加入 `.gitignore`）
- 服務帳戶 Email 要記得在試算表「共用」，否則會出現 `403 Permission Denied`
- Gemini API Key 不要 hardcode 在程式碼裡

## 相關工具頁 / 概念頁

- `[[wiki/concepts/code-execution-sandbox]]` — Claude Code 的 bash_tool 是一種沙盒執行環境
- `[[wiki/ai-workflow/llm-interactive-chart]]` — 類似模式：Python 計算 + LLM 推理

## 相關素材

- [[raw/使用 Claude Code 存取 Google Sheets API 與 Gemini API.md]]
- [[raw/使用 IDE_CLI 存取 Google Sheets API 與 Gemini API.md]]
