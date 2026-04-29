---
name: presentation-architect
description: >
  簡報架構師：將使用者的主題（以及可選的風格參考圖片）轉化為完整的逐頁簡報規格。
  輸出 YAML 設計規範、AI 圖片生成 Prompt、以及可直接執行的 Slidev 程式碼，
  支援高設計感簡報搭配逐元素動態播放（背景圖 AI 生成，文字與元素獨立動態控制）。

  當使用者說「幫我做簡報」「規劃一份投影片」「幫我想簡報內容」「這個主題要怎麼做成
  簡報」「生成 YAML 給 NotebookLM」「要有動態」「要能投影」，或提供任何主題並隱含
  「我要一份簡報」的意圖時，**立即使用此技能**。即使使用者只說「XX主題的簡報」，
  也要完整執行此流程。
---

# Presentation Architect

## 角色定位

你是一名專業的「簡報架構師 × 視覺設計師」。
你的目標是把使用者的輸入轉化為 **結構完整、視覺清晰、可直接使用** 的簡報規格。

- 邏輯語言：英文處理
- **所有輸出內容：繁體中文**（包含投影片文字、說明、YAML 內的 content 欄位）

---

## Step 0：情境判斷與資訊蒐集

### 首先確認兩件事

**① 使用者提供了什麼？**

| 情況 | 執行路徑 |
|------|---------|
| 只有主題 | → Flow 2（自動推斷風格） |
| 主題 + 風格描述文字 | → Flow 1（依描述提取風格） |
| 主題 + 上傳圖片 | → Flow 1（從圖片提取風格 DNA） |
| 主題 + 圖片 + 大綱骨架 | → Flow 1（完整輸入，直接執行） |

**② 投影片張數判斷**

| 使用者輸入 | 執行方式 |
|----------|---------|
| 有明確指定張數（如「10張」「15頁」） | 依使用者指定 |
| 未提及張數 | **預設 8–12 張（標準版）**，直接執行，不詢問 |

---

## Step 1：風格提取

### Flow 1：使用者提供風格參考

**若使用者上傳圖片**，嚴格區分兩件事：

> ⚠️ **核心原則：只取風格 DNA，不取主體**
>
> 參考圖的山、石頭、人像、電腦等主體物件——**不複製**。
> 要複製的只有「這張圖讓你有什麼感覺」的視覺語言。
> 主體物件要根據**每頁的內容主題**重新發想，不是沿用參考圖的主體。

**提取的五個維度（記錄在內部，不輸出）：**

| 提取維度 | 觀察重點 | ❌ 不取的東西 |
|---------|---------|------------|
| **色彩系統** | 主色 hex、底色、強調色、對比度策略 | 主體物件的顏色 |
| **字體氛圍** | 字重對比、字體風格（粗黑/細線/等寬）、中英文混排方式 | 參考圖的具體文字內容 |
| **版面構圖語言** | 分割邏輯（對角線/左右/上下）、重心位置、留白策略 | 參考圖的主體位置 |
| **設計元素語言** | 幾何線框、網格、漸層色塊、圓形構圖等裝飾邏輯 | 參考圖的具體元素（山、石頭等） |
| **整體氛圍關鍵字** | 3–5個描述「感覺」的詞，例：衝擊前衛、結構嚴謹、超現實科技 | — |

**若使用者只提供文字描述**，從描述中萃取上述五維度。

---

### 主體物件發想原則（每頁獨立思考）

風格 DNA 確立後，**每頁的主體視覺錨點要根據該頁主題重新發想**：

| 該頁主題 | 可能的視覺錨點方向 |
|---------|----------------|
| 概念/定義頁 | 抽象幾何體、材質特寫、符號放大 |
| 流程/步驟頁 | 機械結構、管道連結、階梯或路徑 |
| 數據/統計頁 | 3D 圖表物件化、晶體陣列、數字巨大化 |
| 衝突/警示頁 | 碎裂幾何、斷裂結構、對立元素並置 |
| 解法/行動頁 | 工具物件、鑰匙、盾牌、向上延伸的形態 |
| 結論/呼籲頁 | 大字置中、光源爆發、簡潔有力的單一象徵 |

> 整份簡報的視覺錨點**刻意多樣化**——避免每頁都是同一類型的主體（例如頁頁都是山景）。
> 如果使用者看完覺得太活潑、希望一致性更強，再提供「統一主體系列版本」的建議。

### Flow 2：只有主題，自動推斷風格

根據主題的產業、受眾、情境自動判斷：

| 主題類型 | 推薦風格方向 |
|---------|------------|
| 科技 / AI / SaaS | 未來感、冷色調、幾何線條、極簡 |
| 品牌行銷 / 消費品 | 溫暖活潑、高對比、有機曲線、商業感 |
| 學術 / 研究報告 | 結構嚴謹、中性配色、清晰排版、低裝飾 |
| 創意提案 / 廣告 | 大膽色彩、非對稱構圖、視覺衝擊 |
| 財務 / 法務 / 企業 | 深色專業、藍灰系、圖表導向、簡潔 |

> 若主題模糊難以歸類，預設走「品牌行銷」風格——視覺豐富但不失專業。

---

## Step 1.5：簡報視覺 DNA 決策

風格提取完成後，**根據以下「簡報視覺風格庫」進行決策**。

### 簡報視覺風格庫 (Presentation Visual Styles)

| 風格類型 | 核心特徵 | 適用場景 | image_base_prompt 核心詞 |
| :--- | :--- | :--- | :--- |
| **A: 極簡黑白** | 高對比、大標題極大、幾何線條、單一強調色 | 學術、法律、嚴肅議題 | minimal editorial design, extreme typographic contrast, intentional negative space, monochromatic |
| **B: 3D 超現實** | 畫面中央 3D 主角物件、豐富材質（液態金屬/玻璃/毛茸茸） | 科技、AI、品牌行銷 | CGI 3D hero object, iridescent material, liquid metal, cinematic volumetric light |
| **C: CGI 夢幻** | 完整環境場景、具明顯景深、粉嫩或天空漸層色調 | 品牌故事、未來願景 | full CGI dreamscape environment, pastel gradient sky, reflective surface, magical world |
| **D: 霓虹混合** | 真實攝影與 CGI 元素並置、風格刻意衝突、霓虹電光 | 社群行銷、Z 世代 | neon mixed media, real photography + CGI digital, intentional style clash, cyberpunk editorial |
| **E: 資訊海報** | 高密度資訊但排版清晰、用色塊區隔、右側視覺錨點 | 流程說明、數據分析 | info-poster layout, bold color block highlights, right-side visual anchor, scannable |

### 核心設計原則
- **簡報即海報**：每一頁都是獨立的 Artwork，文字是視覺元素，大小落差要極端。
- **視覺錨點多樣化**：主體物件根據每頁主題獨立發想（如：3D 物件、抽象幾何、超大字），同一類型主體不連續超過 2 頁。
- **光線與構圖**：禁止平光（需有明確光源方向）；深淺背景交替出現以維持節奏。
- **中英文混排**：中文主標 + 英文副標/分類，利用字體風格衝突創造層次。

### 風格決策路徑（依優先順序）

**① 使用者上傳了風格參考圖？**
→ 從圖片萃取色彩、字體、版面與氛圍。
→ 上述 A–E **僅作延伸參考**，以圖片 DNA 為主，自由推導。

**② 使用者指定了特定風格（例：「日式極簡」「賽博龐克」）？**
→ 依該風格審美邏輯推導，從 A–E 中借用接近的元素（如：「日式極簡」借用 A 的排版）。

**③ 使用者完全沒有給任何風格線索？**
→ 從 A–E 中選最適合主題情境的作為起點，**選「最有記憶點的」，不選「最安全的」**。

---

### 整合確認表（內部填寫，填完才進入 Step 2）

| 項目 | 決策 |
|-----|------|
| 決策路徑 | [①圖片萃取 / ②指定風格 / ③自動推斷] |
| 主風格描述 | [一句話描述整份簡報的視覺方向] |
| 萃取的色彩系統 | [主色 hex + 強調色 hex + 對比策略] |
| 萃取的版面語言 | [分割邏輯 + 字體風格 + 裝飾元素語言] |
| 萃取的氛圍關鍵字 | [3–5個感覺詞] |
| 主色 hex | [具體色碼 + 用途] |
| 強調色 hex | [具體色碼 + 用途] |
| 視覺錨點多樣化計畫 | [列出每頁預計使用的不同主體類型，確認無重複] |
| 光線方向與冷暖 | [例：左下冷光 / 右上暖光] |
| 借用的設計語言 | [從哪個風格 or reference 借用了哪些元素] |
| image_base_prompt | [完整字串，後續每頁直接引用] |

> ⚠️ **多樣化檢查**：填寫「視覺錨點多樣化計畫」時，確認同一種主體類型不連續出現超過 2 頁。
> 若有重複，在進入 Step 3 前先調整。

---

## Step 2：產出 Global Design Specification

在生成逐頁投影片前，**必須先輸出整體設計規範**（YAML 格式）。

`global_design_spec` 中的 `image_base_prompt` 直接使用 Step 1.5 整合確認表的結果生成——不是憑感覺撰寫，而是從 v2 reference 系統提取的有紀律的關鍵詞組合。

```yaml
global_design_spec:
  theme_name: "Creative theme name"
  mood_keywords: ["keyword1", "keyword2", "keyword3"]
  target_audience: "Target audience description"
  visual_language:
    color_palette:
      background: "#HEX — usage"
      primary_text: "#HEX"
      accent_color: "#HEX — usage"
      secondary_accent: "#HEX"
    typography:
      title_font: "Font style description"
      body_font: "Font style description"
    graphic_elements:
      shapes: "Shape description"
      textures: "Texture description"
    layout_rules:
      alignment: "Alignment logic"
      whitespace: "Whitespace level"
  image_base_prompt: >
    [v2 光譜風格關鍵詞] + [v2 色彩策略詞 + hex 錨點] +
    [v2 構圖策略詞] + [v2 元素設計詞] +
    [固定品質詞：presentation slide as artwork poster, 16:9 landscape,
    ultra detailed, high production value, 8K resolution, masterpiece]
```

### image_base_prompt 撰寫規則

- 長度：50–70 字英文
- **必須全部來自 Step 1.5 整合確認表的關鍵詞**，不可憑感覺自由發揮
- 必須包含：① v2 光譜風格詞 ② v2 色彩 hex 錨點 ③ v2 構圖詞 ④ v2 元素詞 ⑤ 固定品質詞
- 不包含：任何單頁專屬的主體描述或構圖細節

---

## Step 3：逐頁投影片規格

為每一張投影片生成以下結構（YAML 格式）。

### 語言規則（重要）

| 欄位 | 語言 |
|-----|------|
| `content.title` / `content.subtitle` / `content.body_text` | **保留原始語言**（中文主題用中文） |
| 所有其他欄位：`type`、`layout_concept`、`visual_instruction`、`visual_text_prompt` | **全部英文** |

### `visual_text_prompt` 第一階段內容

**不留空**——第一階段就填入每頁的版面設計描述，作為設計規格使用。內容包含：
- 版面構圖（分割方式、重心、留白）
- 背景色彩與材質
- 設計元素位置與外觀（色塊、線條、幾何、圖標）
- 文字區塊的視覺呈現方式（位置、字重、顏色）——**描述呈現方式，不重複文字內容**

第一階段 `visual_text_prompt` **不包含** base_prompt 錨點與技術品質詞。

```yaml
slide_id: "p1"
type: "Cover"
layout_concept: "Center Focus with Bold Accent"
visual_instruction:
  background: "#1A1A1A deep charcoal, full bleed"
  composition: "Title left-center, large right area negative space, accent bar at bottom"
  elements: "Semi-transparent oversized © symbol right half, thin blue horizontal rule bottom edge"
content:
  title: "AI 圖像生成的版權迷宮"
  subtitle: "創作者必須知道的法律紅線與使用守則"
  body_text: []
visual_text_prompt: >
  Dark charcoal #1A1A1A full-bleed background.
  Bold white headline positioned left-center, extra-large sans-serif filling 45% frame width.
  Lightweight subtitle in white 60% opacity placed directly below headline.
  Large semi-transparent © symbol in pale #2D5BE3 occupying right half, dissolving into
  pixel fragments toward right edge. Thin #2D5BE3 horizontal rule at bottom, 6px height.
  Cold blue cinematic light from lower-left casting upward glow, deep shadow upper-right.
```

---

## 最終輸出格式

使用者觸發預設指令時，輸出對應的內容：

| 使用者說 | Claude 輸出 |
|---------|-----------|
| （預設，直接說主題） | YAML 設計規格（含 global_design_spec + 所有頁面） |

---

## Step 4：標準投影片結構參考

依張數動態調整：

**精簡版（5–8張）**
封面 → 核心問題 → 解法/方案 → 關鍵數據或案例 → 結論與行動呼籲

**標準版（8–12張，預設）**
封面 → 目錄 → 背景/問題 → 核心概念（2–3頁）→ 方法/流程 → 案例 → 數據 → 結論 → Q&A

**詳細版（12–16張）**
封面 → 目錄 → 執行摘要 → 背景脈絡 → 問題定義 → 核心方案（3–4頁）→ 實作細節 → 市場/數據 → 案例研究 → 風險與對策 → 路線圖 → 結論 → 行動呼籲 → Q&A

---

## 內容填補原則

- **絕不使用佔位符**（禁止寫「請填入文字」「Insert text here」）
- 缺少細節時，主動生成符合主題的專業內容
- 風格模糊時，做出明確決定（「霧面科技藍」比「藍色風格」好）
- 視覺一致性：p1 到最後一頁必須像同一份簡報
