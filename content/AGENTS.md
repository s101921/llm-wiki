# LLM Wiki — Schema & Instructions

> **這份文件是這個 Vault 的核心設定檔（schema）。**
> 每次開啟新對話，請先閱讀此文件，再閱讀 `index.md`，再開始工作。

---

## 關於這個 Vault

Warren 的專業知識第二大腦。身份：**AI 課程講師 + 行銷顧問**。

這個 Wiki 同時服務兩個角色，知識彼此交叉引用：
- 行銷知識強化課程內容；課程案例回饋顧問方法論
- LLM 負責寫作與維護；Warren 負責策展方向與提問

**語言**：所有 wiki 頁面與回應使用**繁體中文**（原始素材保持原文）

---

## 架構總覽（Karpathy Pattern）

```
Phase 1: Ingest   →   Phase 2: Compile   →   Phase 3: Query
    ↑                                              ↓
    └──────────── Phase 4: Lint ←──────────────────┘
                  （持續循環，wiki 不斷成長）
```

---

## 三層知識架構

Wiki 頁面分三個層次，區別在於**用途**，不是主題：

| 層次 | 資料夾 | 寫法 | 目的 |
|------|--------|------|------|
| ① 知識層 | `concepts/` `tools/` `marketing/`（知識類） | **描述性**：這是什麼、為什麼 | 理解、教學、查詢 |
| ② Skill 層 | `ai-workflow/` `marketing/`（SOP 類） | **指令性**：Step 1 做什麼、輸出是什麼 | LLM 執行單一可重複操作 |
| ③ Playbook 層 | `playbooks/` | **指令性**：串聯多個 Skill，有明確輸入輸出 | LLM 執行完整多步驟流程 |

**判斷這一頁屬於哪一層：**
- 在「解釋一個概念/工具/方法是什麼」→ 知識層
- 在「說明如何執行一個操作（Step 1, 2, 3）」→ Skill 層
- 在「串聯多個 Skill 完成一個完整任務」→ Playbook 層

**`concepts/` vs `ai-workflow/` 的邊界：**
- `concepts/`：給學員看的定義與框架，重點是「這個概念是什麼、有什麼意義」
- `ai-workflow/`：給自己用的執行 SOP，重點是「Step 1, 2, 3 怎麼做」
- 同一主題（如 Harnessing Engineering）兩邊都可以有頁面：concepts/ 放定義，ai-workflow/ 放操作 SOP

---

## 目錄結構

```
LLM Wiki/
├── AGENTS.md          ← 本文件（schema）
├── index.md           ← 所有 wiki 頁面的目錄（每次操作後更新）
├── log.md             ← 操作歷史記錄（只增不減）
│
├── inbox/             ← 零摩擦入口：隨手筆記、草稿、未整理想法（LLM 定期分類）
│
├── Clippings/         ← Web Clipper 自動存放（視同 raw/，唯讀）
├── raw/               ← 其他原始素材（唯讀，LLM 不修改）
│   ├── videos/        ← 影片逐字稿
│   ├── podcasts/      ← Podcast 筆記
│   └── assets/        ← 圖片、PDF、截圖
│
├── projects/          ← 專案知識層（只記學到的事，程式碼留在原目錄）
│   └── [project-slug]/
│       ├── overview.md   ← 這個專案是什麼、目標、狀態
│       ├── learnings.md  ← 過程中的發現（知識，不是程式碼）
│       └── extracted.md  ← 已提煉進 wiki 的項目清單（避免重複）
│
├── wiki/              ← LLM 維護的合成知識頁面（蒸餾後才進來）
│   ├── concepts/      ← 知識層：原理、理論、定義（描述性，供理解與教學）
│   ├── tools/         ← 知識層：工具評估（功能、優缺點、適用場景）
│   ├── marketing/     ← 行銷知識（平坦結構；同一 tag 達 5 頁時 Lint 提議分資料夾）
│   ├── ai-workflow/   ← Skill 層：AI 工具輔助的執行 SOP（指令性）
│   ├── courses/       ← 課程 Marp 投影片穩定版（開發草稿放 projects/）
│   ├── playbooks/     ← Playbook 層：多 Skill 串聯的完整執行流程
│   ├── summaries/     ← 素材萃取頁：單一原始素材的重點提取（ingest 完成後可 archived）
│   ├── clients/       ← ⚠️ 私人（已加入 .gitignore）
│   └── cases/         ← ⚠️ 私人：活動覆盤、成功/失敗案例（已加入 .gitignore）
│
└── Templates/         ← 頁面範本（參考用，不修改）
```

**知識成熟度管道（單向流）：**
```
inbox/ → raw/ 或 projects/ → wiki/（蒸餾後）
```

**私人資料夾**（不發布到網站）：`clients/`、`cases/`（已加入 `.gitignore`）

---

## Frontmatter 規範

```yaml
---
title: 頁面標題
date: YYYY-MM-DD
updated: YYYY-MM-DD
type: concept | tool | marketing | workflow | ai-workflow | playbook | course | summary | synthesis | client | case | project
status: inbox | draft | growing | stable | archived
tags: [tag1, tag2]
sources: 0
private: false   # clients/ 和 cases/ 設為 true
---
```

### `type` 補充說明

| type | 放在 | 層次 | 說明 |
|------|------|------|------|
| `concept` | `wiki/concepts/` | 知識層 | 原理、理論、定義（描述性） |
| `tool` | `wiki/tools/` | 知識層 | 工具評估：功能、優缺點、適用場景（描述性） |
| `marketing` | `wiki/marketing/` | 知識層 | 行銷框架、策略、方法論（描述性） |
| `workflow` | `wiki/marketing/` | Skill 層 | 可重複操作的 SOP，工具無關（指令性） |
| `ai-workflow` | `wiki/ai-workflow/` | Skill 層 | AI 工具輔助的執行流程（指令性） |
| `playbook` | `wiki/playbooks/` | Playbook 層 | 多 Skill 串聯的完整流程，有明確輸入輸出（指令性） |
| `synthesis` | `wiki/concepts/` 或 `wiki/marketing/` | 知識層 | 多素材的綜合分析，放在最相關的 domain 下 |
| `summary` | `wiki/summaries/` | 過渡 | 單一素材的萃取記錄（非最終知識，ingest 完成後可 archived） |
| `course` | `wiki/courses/` | 輸出 | 課程 Marp 投影片 |
| `client` | `wiki/clients/` | 私人 | 客戶知識 |
| `case` | `wiki/cases/` | 私人 | 活動覆盤 |
| `project` | `projects/[slug]/` | — | 專案知識頁 |

**Skill 的放法**：工具無關的 SOP 放 `marketing/`（type: workflow）；用到特定 AI 工具，放 `ai-workflow/`（type: ai-workflow）。

---

## 分類決策指引

遇到「這個知識放哪裡？」，先問這個問題：

| 這是什麼 | 放哪裡 |
|---------|--------|
| 未整理的想法、不確定放哪裡 | `inbox/` |
| 外部素材原文（文章、影片、Podcast） | `raw/` 或 `Clippings/` |
| 解釋「某個 AI/技術概念是什麼」 | `wiki/concepts/` |
| 評估「某個工具的優缺點/用法」 | `wiki/tools/` |
| 行銷知識（框架、策略、方法論） | `wiki/marketing/`（type: marketing） |
| 行銷 SOP（可重複執行的操作步驟） | `wiki/marketing/`（type: workflow） |
| AI 工具輔助的執行流程 | `wiki/ai-workflow/` |
| 多步驟完整執行流程，有明確輸入輸出 | `wiki/playbooks/` |
| 課程投影片（穩定版） | `wiki/courses/` |

**原則：不確定時，先放 `inbox/`，Lint 時再決定。**

### `status` 說明

| status | 含義 | 可信度 |
|--------|------|--------|
| `inbox` | 隨手記，未驗證，可能不準確 | ⚠️ 低 |
| `draft` | 有結構但尚未完整 | 🟡 中 |
| `growing` | 持續有新資訊進來，動態更新 | 🟡 中高 |
| `stable` | 很少變動，高可信度 | ✅ 高 |
| `archived` | 過時但保留參考，不建議直接引用 | 🔴 低 |

---

## Phase 0：Inbox Triage（定期分類）

當 Warren 說「整理 inbox」或 Lint 時，處理 `inbox/` 裡的所有檔案：

**這個 phase 只做分類決定，不做內容豐富。** 目標是快速、低成本地清空 inbox。

1. **丟掉**：明顯過時、重複、沒有知識價值的筆記
2. **移到 raw/**：有價值的原始素材，等待日後正式 Phase 1 Ingest
3. **直接觸發 Phase 1**：內容完整、有知識價值 → 不要只是搬檔案，要完整跑 Phase 1 Ingest 流程（讀相關頁、補資訊、建連結）

> ⚠️ 重要：「直接升級」≠ 把檔案搬進 wiki。沒有跑 Phase 1 的頁面仍然是孤立的。

**分類標準：**
| 狀況 | 判斷 |
|------|------|
| 只是一個詞、一個 URL、一個問句 | 丟掉或移 raw |
| 有描述但缺脈絡、缺驗證 | 移 raw，等素材補足後 Ingest |
| 有清楚的主張、步驟、或框架 | 直接 Phase 1 |
| 與現有 wiki 頁有明顯矛盾 | 直接 Phase 1（優先處理矛盾） |

寫入 `log.md`：`## [YYYY-MM-DD] inbox-triage | 處理 N 筆，觸發 Ingest M 筆，移 raw K 筆`

---

## Phase 1：Ingest（新增素材）

當 Warren 說「處理這個」、「整理這份」時：

1. **閱讀**：讀取 `Clippings/` 或 `raw/` 中的素材
2. **討論**（可選）：確認重點方向
3. **建立素材萃取頁**（若是全新素材）：在 `wiki/summaries/` 建立頁面，記錄這份素材說了什麼，連結回原始檔。這是過渡頁，不是最終知識。
4. **更新或新增知識頁**：根據萃取內容，在 `wiki/concepts/`、`wiki/tools/`、`wiki/marketing/`、`wiki/ai-workflow/` 等對應位置建立或更新頁面：
   - 補充新資訊，標記矛盾（`> ⚠️ 矛盾：...`）
   - 主動建立新的交叉連結（`[[頁面名稱]]`）
5. **更新 `index.md`**
6. **寫入 `log.md`**：`## [YYYY-MM-DD] ingest | 素材標題`

一次 ingest 通常觸及 5–15 個 wiki 頁面。

---

## Phase 2：Compile（編譯輸出）

Query 的好答案**必須存回 wiki**，不能消失在對話記錄裡。

可存回的格式：
- **Markdown 頁面**：比較分析、綜合觀點 → `wiki/*/`
- **Marp 投影片**：可直接在 Obsidian 預覽的簡報 → `wiki/*/`
- **表格**：工具比較、benchmark 對照

存回原則：任何未來會再次用到的答案都應該存回。

---

## Phase 3：Query（查詢知識）

1. 先讀 `index.md` 找相關頁面
2. 讀取相關 wiki 頁面
3. 綜合回答，附引用（`[[頁面名稱]]`）
4. **主動詢問**是否要將答案存回 wiki
5. 寫入 `log.md`：`## [YYYY-MM-DD] query | 問題摘要`

---

## Phase 4：Lint（健康檢查 + 循環回 Phase 2）

當 Warren 說「整理一下」、「lint」時：

逐一檢查並回報：
- 🔴 **矛盾**：頁面間衝突的資訊
- 🔴 **孤立頁面**：沒有任何連結指向的頁面（orphans）
- 🟡 **過時內容**：被新素材推翻的舊觀點
- 🟡 **缺失交叉連結**：應該互相引用但沒有的頁面
- 🟡 **同層橫向缺失連結**：同一 type 或同一主題群的頁面（如兩篇都在談 Compaction 的 summaries），沒有直接互指
- 🟡 **courses/ 反向指向**：concepts/ 或 tools/ 頁面若已被某課程引用，要在該知識頁加上「→ 相關課程」backlink
- 🟢 **缺失頁面**：多次被提及但尚未建立的概念
- 🟢 **建議深挖**：可用網路搜尋補充的資料空缺
- 🟢 **新文章候選**：多個頁面之間發現的潛在連結，值得寫成獨立頁面
- 🟢 **marketing/ 分叉候選**：掃描 `wiki/marketing/` 下所有頁面的 tags，若同一個 tag 出現在 **5 頁以上**，向 Warren 提議建立對應子資料夾，列出建議名稱與要移入的頁面，**等確認後才執行**

Lint 結束後，回到 Phase 2 繼續編譯 —— **這是持續循環，不是一次性操作**。

寫入 `log.md`：`## [YYYY-MM-DD] lint | 發現 N 個問題`

---

## 頁面格式

### 行銷知識頁（wiki/marketing/，type: marketing 或 workflow）
```
# 框架或方法名稱
**類型：[框架/策略/SOP]｜適用場景**

## 核心邏輯（描述性）或 執行步驟（指令性）
## 行銷應用場景 / 實際範例
## 與其他框架的關係
## 常見誤用
## 相關素材
```

### AI 工具頁（wiki/ai-workflow/，type: ai-workflow）
```
# 工具或流程名稱
**類型｜用途｜費用**

## 核心功能
## 執行步驟（Step-by-step）
## Prompt / 設定範例
## 效果評估 / 已知限制
## 相關素材
```

### 客戶頁（wiki/clients/）— 私人
```
# 客戶名稱
**產業｜規模｜合作起始**

## 品牌現況
## 目標受眾
## 歷史決策與脈絡
## 正在進行的專案
```

### 案例頁（wiki/cases/）— 私人
```
# 活動名稱
**客戶｜時間｜平台**

## 目標與策略
## 執行摘要
## 數據結果
## 學到的事
## 下次要改的事
```

---

## 連結規範

- 內部連結：`[[頁面名稱]]`
- 原始素材：`[[Clippings/檔名]]` 或 `[[raw/.../檔名]]`
- 矛盾：`> ⚠️ 矛盾（[[頁面A]] vs [[頁面B]]）：說明`
- 外部連結：保留完整 URL

---

## 頁面格式：Playbook 頁（wiki/playbooks/，type: playbook）

適用：多個 skill 串聯的完整行銷執行流程（marketing plugin）

> ⚠️ Playbook 頁面寫給 LLM 執行用，必須是**指令性**而非描述性。
> 每個 Step 要清楚說明：做什麼、輸入是什麼、輸出是什麼、去讀哪個 skill 頁。

```
# Playbook 名稱
**輸入：[什麼素材或 brief]  →  輸出：[最終交付物]**
**適用場景：[何時跑這個 playbook]**

## 執行前確認
- [ ] 需要的資料／素材
- [ ] 需要的工具權限

## Step 1：[階段名稱]
執行：[[wiki/.../skill頁面]]
輸入：上一步的輸出 或 初始 brief
動作：（具體指令，LLM 可直接照做）
輸出：（明確描述產出格式）

## Step 2：[階段名稱]
...（同上結構）

## 觸發條件
（什麼情況下應該跑這個 playbook）

## 已知限制
（哪些情況這個 playbook 不適用）

## 版本記錄
| 版本 | 日期 | 變更 |
|------|------|------|
| v1 | YYYY-MM-DD | 初版 |

## 相關 Skill 頁
- [[wiki/.../skill1]]
- [[wiki/.../skill2]]
```

**三個層次的關係：**
```
wiki/playbooks/     ← 編排層：串聯多個 skill，有輸入輸出
wiki/*/（workflow） ← Skill 層：單一可重複操作 SOP
wiki/concepts/ tools/ ← 知識層：底層原理與工具
```

---

## 頁面格式：Skill / Workflow 頁（wiki/*/，type: workflow）

適用：圖片生成流程、數據分析 SOP、創意發想框架等可重複操作

```
# Skill 名稱
**類型｜適用場景｜工具（若有）**

## 何時使用
## 執行步驟（Step-by-step SOP）
## Prompt / 設定模板（若有）
## 常見錯誤與修正
## 相關工具頁 / 概念頁
```

---

## 頁面格式：專案知識頁（projects/[slug]/）

### overview.md
```
# 專案名稱
**狀態｜開始日期｜目標**

## 這個專案在做什麼
## 技術棧 / 工具（簡述，細節留程式碼目錄）
## 目前進度
## 相關 wiki 頁面
```

### learnings.md
```
# 專案學習記錄

## [YYYY-MM-DD] 發現事項
（自由格式，隨時 append）

## 已驗證的模式（待提煉）
## 已提煉至 wiki（見 extracted.md）
```

### extracted.md
```
# 已提煉至主 Wiki

| 日期 | 提煉內容 | 目標頁面 |
|------|---------|---------|
| YYYY-MM-DD | 說明 | [[wiki/...]] |
```

---

## 注意事項

- `raw/` 和 `Clippings/` 的檔案**絕對不要修改**
- `inbox/` 的檔案可以由 LLM 移動或刪除（這是唯一例外）
- 每次操作後必定更新 `index.md` 和 `log.md`
- `clients/` 和 `cases/` 標記 `private: true`，不發布到網站，且已加入 `.gitignore`
- 不要建立超過 3 層的巢狀目錄（`projects/[slug]/` 算 2 層，OK）
- Wiki 是持續循環的系統，每次 lint 後回到 compile，不斷成長
- 所有 wiki 頁面的 `status` 欄位必須填寫；新建頁面預設 `draft`
