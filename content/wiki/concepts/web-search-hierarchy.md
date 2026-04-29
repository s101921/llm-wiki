---
title: Web Search / Fetch / Deep Research 三層架構
date: 2026-04-29
updated: 2026-04-29
type: concept
status: draft
tags: [web-search, deep-research, web-fetch, geo, seo, scraping]
sources: 3
private: false
---

# Web Search / Fetch / Deep Research 三層架構

**LLM 連網能力的三層演進，不是三個工具，而是資訊處理能力的層級躍遷。**

```
Level 1：web_search  → 資訊發現（找資料入口）
Level 2：web_fetch   → 資訊擷取（讀取單一來源）
Level 3：Deep Search → 知識建構（多步驟自主研究）
```

## 三者定義與比較

| 維度 | web_search | web_fetch | Deep Search |
|------|-----------|-----------|-------------|
| 本質 | 找資料 | 讀資料 | 做研究 |
| 輸入 | Query | URL | Query |
| 輸出 | URL + snippet | 完整內容 | 綜合答案 |
| 深度 | 低 | 高 | 很高 |
| 廣度 | 高 | 低 | 高 |
| 是否多步驟 | ❌ | ❌ | ✅ |
| 是否推理 | ❌ | ❌ | ✅ |
| 偏差來源 | SEO/ranking | 單一來源 | 模型決策 |

## Deep Search 的四核心能力

1. **Query Decomposition**：把複雜問題拆成多個子問題
2. **Multi-hop Retrieval**：找 A → 發現 B → 再找 C（類似人類 research）
3. **Cross-source Validation**：多來源比對，避免單點錯誤
4. **Iterative Reasoning**：搜尋 → 理解 → 再搜尋

## Deep Research 的六大資料限制

1. **權限/登入限制**：私人帳號、雲端硬碟（未授權）、Slack、企業內網、付費牆
2. **robots.txt 控制**：網站可禁止 AI 爬取；`Google-Extended` 只影響 AI 使用，不影響搜尋索引
3. **未被索引內容**：Dark Web、noindex 頁面、孤島頁（無外部連結）
4. **動態內容限制**：CAPTCHA、需要點擊/拖曳的互動 UI
5. **安全與政策過濾**：仇恨言論、違法資訊 → 「不是抓不到，而是不能用」
6. **平台限制**：Facebook / Instagram / Threads / X → robots.txt + API 控制 + 商業政策

### 社群平台可見性評比

| 平台 | 可索引 | AI使用 | 策略價值 |
|------|--------|--------|----------|
| 官網/Blog | 高 | 高 | ⭐⭐⭐⭐⭐ |
| Facebook | 中 | 低 | ⭐⭐ |
| Instagram | 低 | 極低 | ⭐ |
| Threads | 中 | 低（成長中） | ⭐⭐ |

社群內容的三層漏斗：**公開（很多）→ 被索引（少）→ 被AI引用（極少）**

## 動態網站爬蟲的三條路線

| 路線 | 優點 | 缺點 |
|------|------|------|
| 直抓 AJAX 接口 | 快、結構化 | 可能有簽名/鑑權/頻控 |
| 無頭瀏覽器（Playwright/Selenium）| 還原真實瀏覽器行為 | 資源占用高、部署麻煩 |
| API 服務（如 ScraperAPI）| IP 輪換/代理外包，快速上手 | 需付費 |

**原則：能抓接口就抓接口；必須渲染才用 JS 渲染。**

## web_fetch 的技術限制

- 不執行 JavaScript（抓不到動態內容）
- 無法存取需要登入的頁面（Facebook、Instagram、Gmail）
- 抓取整頁但無法做跨來源驗證

## GEO：AI 時代的內容策略轉變

**SEO → GEO（Generative Engine Optimization）**：不再只是競爭排名，而是競爭「被 Deep Search 選中並引用」。

Deep Search 偏好的內容特徵：
- 清楚段落（chunkable）
- 可引用句子
- 有邏輯結構
- 可被壓縮（compressible）

## 與其他概念的關係

- [[wiki/concepts/rag]] — RAG 是 web_fetch 概念的系統化延伸，加入向量索引
- [[wiki/tools/playwright-cli]] — Playwright 是動態網站爬蟲「無頭瀏覽器」路線的具體工具
- [[wiki/concepts/ai-agent]] — Deep Search 是 AI Agent 自主 tool-use 的典型應用

## 相關素材

- [[raw/Web Search vs Web Fetch vs Deep Research.md]]
- [[raw/# Deep Research 資料檢索限制完整指南.md]]
- [[raw/爬蟲JS的知識.md]]
