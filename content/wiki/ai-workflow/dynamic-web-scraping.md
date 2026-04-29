---
title: 動態網站爬蟲 SOP
date: 2026-04-29
updated: 2026-04-29
type: ai-workflow
status: draft
tags: [scraping, playwright, scraperapi, javascript, ajax, dynamic]
sources: 1
private: false
---

# 動態網站爬蟲 SOP

**類型：AI Workflow｜用途：抓取 JavaScript 渲染後才出現的網頁內容｜工具：Playwright / ScraperAPI / 直抓 AJAX 接口**

## 何時使用

- 用 `requests.get()` 只拿到空殼 HTML，但瀏覽器可以看到資料
- 目標網頁在初次載入後靠 JavaScript 或 AJAX 動態拉取資料
- 需要自動化操作網頁（登入、滾動、點擊）

## 快速判斷是否是動態網站

> 在瀏覽器按「查看原始碼」（Cmd+U），找不到你要的資料，但瀏覽器看得到 → 十之八九是動態網站。

## 三條抓取路線

| 路線 | 優點 | 缺點 | 適用場景 |
|------|------|------|----------|
| 直抓 AJAX 接口 | 快、結構化、解析簡單 | 可能有簽名/鑑權/頻控 | API 格式明確的動態頁面 |
| 無頭瀏覽器（Playwright / Selenium）| 還原真實瀏覽器行為 | 資源占用高、部署麻煩 | 需要點擊/登入/滾動 |
| API 服務（ScraperAPI）| IP 輪換/代理/渲染外包，快速上手 | 需付費 | 大批量抓取、需要更換 IP |

**原則：能抓接口就抓接口；必須渲染才用 JS 渲染。**

## 路線 A：直抓 AJAX 接口

1. 開啟 Chrome DevTools → Network 頁籤
2. 重新載入頁面，過濾 XHR/Fetch 請求
3. 找到返回你要資料的接口（通常是 JSON）
4. 直接用 `requests` 呼叫該接口

```python
import requests

url = 'https://example.com/api/data?page=1'
headers = {'User-Agent': 'Mozilla/5.0...'}
response = requests.get(url, headers=headers)
data = response.json()
```

## 路線 B：Playwright 無頭瀏覽器

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://example.com')
    page.wait_for_selector('#content')  # 等待動態內容載入
    content = page.inner_text('#content')
    browser.close()
```

**適用**：需要登入、滾動載入（infinite scroll）、點擊互動。

→ 見 [[wiki/tools/playwright-cli]] 了解 CLI 模式的 token 效率優勢

## 路線 C：ScraperAPI

```python
pip install scraperapi-sdk

from scraperapi_sdk import ScraperAPIClient
client = ScraperAPIClient('YOUR_API_KEY')

result = client.get('https://example.com', render=True)
# render=True 讓 ScraperAPI 完成 JS 渲染後才回傳 HTML
```

分頁批次抓取：
```python
for page in range(1, N+1):
    url = f'https://example.com/products?page={page}'
    result = client.get(url, render=True)
    # 解析每頁內容
```

## 穩定性清單（避免常見陷阱）

- ✅ **合規優先**：先看站點服務條款（robots.txt）
- ✅ **控制頻率**：加隨機間隔（`time.sleep(random.uniform(1, 3))`）
- ✅ **容錯重試**：別讓一個頁面卡死整批任務（用 try/except + retry）
- ✅ **選擇器不要寫死**：用語意化的選擇器，避免因 UI 改版失效
- ✅ **JS 渲染別濫用**：能抓接口就抓接口，Playwright 資源占用高

## 與其他頁面的關係

- `[[wiki/tools/playwright-cli]]` — Playwright CLI 模式的 token 效率與 MCP vs CLI 取捨
- `[[wiki/concepts/web-search-hierarchy]]` — web_fetch 是 AI 的「輕量版爬蟲」，但無法執行 JS

## 相關素材

- [[raw/爬蟲JS的知識.md]]
