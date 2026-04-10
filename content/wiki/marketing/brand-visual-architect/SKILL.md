---
name: brand-visual-architect
description: >
  從多張品牌設計圖片中萃取視覺基因，建立可供 AI 生圖使用的完整 Brand Visual Guidebook。
  當使用者說「幫我分析這個品牌的設計風格」、「我要幫客戶建立品牌視覺指南」、「幫我做品牌的 AI 生圖 Prompt 公式」、
  「這些廣告圖怎麼讓 AI 學起來」、「我上傳了一些品牌素材」，或直接上傳多張設計圖片並提到品牌、風格、Prompt、
  Guidebook、視覺規範等關鍵字，都應立即使用此技能。
  即使使用者只上傳 2-3 張圖片說「幫我分析」，也要完整跑此流程，從單批分析開始執行。
  支援輸入格式：直接上傳圖片、PDF 設計稿、圖片 URL、混合方式。
  最終輸出：對話中完整的文字 Guidebook + 可下載的 .md 檔案。
---

# Brand Visual Architect — 品牌視覺矩陣指南建立技能

## 核心設計原則

### 🔑 圖片數量與分批策略（最重要）

LLM 分析圖片有注意力衰退問題：
- **1–6 張**：單批分析，品質最高
- **7–12 張**：分成 2 批（每批 ≤6 張），分別萃取後合併
- **13–20 張**：分成 3–4 批，先各批萃取，再跨批比對 Brand DNA
- **20 張以上**：建議使用者先篩選出最具代表性的 15 張

**分批執行邏輯：**
1. 每批圖片 → 輸出「單批視覺摘要」（不輸出完整報告）
2. 所有批次完成後 → 整合成最終 Guidebook
3. 使用者若分多次上傳，主動詢問「還有更多圖片嗎？」

---

## Step 0：接收圖片與前置確認

### 判斷圖片來源類型
| 來源 | 處理方式 |
|------|---------|
| 直接上傳圖片 | 直接分析，判斷批次數量 |
| 圖片 URL | 使用 web_fetch 抓取後分析 |
| PDF 設計稿 | 視為多頁圖片，每頁視為一張素材 |
| 混合 | 統一整理後按批次處理 |

### 前置問題（若圖片已上傳，只問缺少的資訊）

```
1. 品牌名稱？（若圖片已顯示則自動辨識）
2. 產業/類別？（例：美妝、科技、餐飲、文化藝術）
3. 這些圖片涵蓋哪些用途？（例：社群廣告、包裝、EDM）
   → 若無法確定，告知使用者「將由分析結果自動歸類」
4. 目標輸出語言？（預設：繁體中文報告 + 英文 Prompt）
```

若使用者沒有提供以上資訊且圖片中看不出來，**僅詢問品牌名稱**，其餘由分析自動推斷。

---

## Step 1：分批視覺萃取

> **對每一批圖片（≤6 張）執行此步驟**

每批輸出以下格式的「單批摘要」（**此步驟不輸出給使用者看，只做內部記錄**）：

```
[批次 N 摘要]
- 觀察到的主色系：
- 排版特徵：
- 光影風格：
- 受眾訊號（若有）：
- 產品/服務類別（若有）：
- 本批異常或特殊圖片：
```

---

## Step 2：跨批整合 Brand DNA

若只有一批圖片，直接進入此步驟。
若有多批，比對各批摘要，找出「所有批次共同出現的視覺元素」作為 Brand DNA。

萃取以下項目：
- **品牌總調性**：3–5 個跨越所有批次一致的形容詞
- **全域主色調**：所有圖片共用的色彩（HEX + 色彩心理描述）
- **品牌絕對禁忌**：從圖片中「絕對沒有出現過」的元素推斷禁忌
- **風格群組辨識**：從圖片差異中識別 2–5 個受眾×產品的群組

---

## Step 3：輸出完整 Guidebook

### 輸出語氣與格式
- **繁體中文**撰寫主要說明
- **英文**撰寫所有 Prompt 公式與 Keywords
- 每個群組的視覺解剖必須使用具體設計術語，禁止使用空泛詞彙

### 完整 Guidebook 結構

---

```
# [品牌名稱] AI 品牌視覺矩陣指南
**製作日期**：[日期] ｜ **分析素材數量**：[N] 張

---

## 一、品牌核心基因 The Constant: Brand DNA
*無論哪種受眾或產品，都必須遵守的最高視覺原則*

### 品牌總調性 Global Brand Vibe
[3–5 個貫穿全品牌的精準形容詞，中英對照]

### 全域主色調 Global Color Palette
| 色彩角色 | HEX 碼 | 色彩描述 | 品牌心理暗示 |
|---------|--------|---------|------------|
| 主色     |        |         |            |
| 副色     |        |         |            |
| 強調色   |        |         |            |
| 中性色   |        |         |            |

### 品牌絕對禁忌 Strict Negative Elements
- 視覺元素禁忌：
- 色調禁忌：
- 排版風格禁忌：
- 氛圍禁忌：

---

## 二、視覺風格矩陣概覽 Style Clusters Matrix
*依據「目標受眾 × 產品/服務 × 行銷平台」三維分群*

| 群組 | 代號 | 受眾特徵 | 產品/服務類別 | 主要行銷平台 |
|-----|------|---------|-------------|------------|
| A   |      |         |             |            |
| B   |      |         |             |            |
| C   |      |         |             |            |

---

## 三、分群專屬視覺解剖 Cluster Profiles

### 🎯 群組 A：[群組名稱]

**A. 光影與氛圍 Lighting**
- 主光源：[具體描述，例：overhead soft box diffused light]
- 陰影表現：[例：subtle drop shadow, 15% opacity]
- 色溫與環境光：[例：warm 5500K golden hour ambient]

**B. 專屬色彩計畫 Colors**
- 輔助色：[HEX] | [描述]
- 背景色/環境色：[HEX] | [描述]
- 色彩比例建議：[主色:副色:強調色 = X:X:X]

**C. 材質與紋理 Materials**
- 主體材質：[例：matte ceramic finish, micro-texture surface]
- 環境/背景材質：[例：clean white paper background, subtle grain]

**D. 字體與排版 Typography**

*基礎字型規格*
- 主標題字型：[字族分類 + 字重，例：bold geometric sans-serif, tight tracking]
- 副標題與說明文：[例：light weight, generous line height]
- CTA 邏輯：[例：pill-shape button, high contrast fill]
- 文字位置規則：[例：left-aligned, lower third placement]

*字型設計處理手法（Typography Treatment）*
仔細觀察 Logo、標準字、標題是否存在以下進階設計手法，並精確標記：

| 手法類型 | 術語 | 說明 | 本品牌是否出現 |
|---------|------|------|--------------|
| 圖文結合 | Combination Mark | 圖標與標準字合併為一體 | ✓ / ✗ |
| 文字圖形化 | Illustrative Typography | 筆畫與插圖/符號融合 | ✓ / ✗ |
| 嵌入式設計 | Integrated Icon | 圖示取代某字母或筆畫 | ✓ / ✗ |
| 標準字設計 | Logotype Design | 品牌名稱客製化字體、含筆畫異質化 | ✓ / ✗ |
| 創意字體設計 | Creative Typography | 文字筆畫具藝術聯想性轉化 | ✓ / ✗ |
| 拆字法 | Deconstructed Typography | 拆解中文筆畫並在缺口置入相關元素 | ✓ / ✗ |
| 負空間字體 | Negative Space Typography | 利用留白隱藏圖示或第二層意義 | ✓ / ✗ |

若確認出現，進一步描述：
- **嵌入位置**：哪個字、哪個筆畫被替換或融合（例：「的」字下半部改為貓剪影）
- **圖示語義**：嵌入的圖示與品牌的語義連結為何
- **視覺整合程度**：seamless fusion / subtle hint / standalone combination
- **AI Prompt 還原關鍵字**：[例：`logotype with integrated cat silhouette replacing radical, negative space design, custom chinese typography`]

**E. 攝影與構圖 Camera & Composition**
- 鏡頭焦段：[例：85mm portrait lens equivalent]
- 構圖法則：[例：rule of thirds, product in right frame]
- 景深控制：[例：f/2.0 shallow depth, creamy background bokeh]
- 視角：[例：eye-level, slight downward 15° tilt]

**F. 行銷平台適配 Platform Specs**
- 適合平台：[例：Instagram Feed, Facebook Ad]
- 建議比例：[例：1:1, 4:5]
- 視覺優先區塊：[例：產品置中上方 1/3 以避免 UI 遮擋]

*(每個群組重複以上結構 A–F)*

---

## 四、AI 繪圖矩陣公式庫 Prompt Matrix

### 🔑 Global Keywords（全域品牌關鍵字，每個 Prompt 都必須包含）
`[Brand DNA 的英文關鍵字串]`

### ⛔ Global Negative Prompts（全域負向詞）
`[品牌禁忌的英文關鍵字串]`

---

### 公式 A：[群組名稱]
**使用時機**：當需要生成針對 [受眾] 的 [產品類型] 圖像時

**基礎公式**：
```
[Subject/Action], [Global Keywords], [群組A光影], [群組A色彩], [群組A材質], [群組A鏡頭], --ar [比例] --style raw
```

**進階變體（加入情境）**：
```
[Subject/Action] in [scene context], [Global Keywords], [群組A全參數], --ar [比例]
```

**實戰範例**：
```
[具體可以直接使用的完整 Prompt 範例]
```

*(每個群組提供 1 組基礎公式 + 1 組進階變體 + 1 個實戰範例)*

---

## 五、跨平台應用速查表 Platform Quick Reference
| 群組 | IG Feed | IG Story | FB Ad | EDM Banner | OOH 戶外 |
|-----|---------|----------|-------|------------|---------|
| A   | ✓ 最佳  | ✓        | ✓     | △          | ✗       |
| B   |         |          |       |            |         |

---

## 六、Prompt 使用說明 How to Use
1. **找到對應群組**：依你的受眾與產品類型選擇群組
2. **複製 Global Keywords**：貼到 Prompt 開頭
3. **加入群組公式**：填入你的具體主題
4. **加入 Negative Prompts**：確保品牌一致性
5. **指定平台比例**：依輸出平台調整 --ar 參數
```

---

## Step 4：存檔輸出

Guidebook 全文輸出後，執行以下步驟：

1. 將完整 Guidebook 儲存為 `.md` 檔案：
   - 路徑：`/mnt/user-data/outputs/[品牌名稱]-brand-visual-guidebook.md`
2. 使用 `present_files` 工具提供下載連結
3. 告知使用者：「這份 Guidebook 可直接貼入 Notion、存為 PDF，或作為 Custom Instructions 給其他 AI 工具。」

---

## 特殊情境處理

### 圖片品質不足時
若某張圖片模糊、截圖品質差，在分析中標記「⚠️ 此圖品質有限，以下判斷僅供參考」，不因此略過該圖。

### 品牌圖片混雜多個子品牌時
若分析發現圖片來自明顯不同的子品牌（例：主品牌 vs 副線），主動詢問使用者是否要分開建立 Guidebook，或整合為一份含子品牌章節的版本。

### 只有 1–3 張圖片時
告知使用者：「目前素材較少，分析結果會聚焦在可確認的共同元素，部分推斷可靠度較低，建議日後補充更多素材更新 Guidebook。」然後仍執行完整流程，不足的欄位標記 `[待補充 - 建議增加此類素材]`。

### 課程示範場景
若使用者明示「這是教學示範」，在輸出末尾加一個「📚 教學重點提示」區塊，點出此品牌分析中最值得學員注意的 2–3 個視覺設計決策。

---

## 品質自我檢查清單

在輸出最終 Guidebook 前，確認：
- [ ] 每個 Prompt 公式都包含 Global Keywords
- [ ] 視覺解剖術語全部具體（無「簡潔」「現代」等空泛詞）
- [ ] 色彩全部附有 HEX 碼
- [ ] 每個群組都有獨立的 Platform Specs 建議
- [ ] Negative Prompts 從實際圖片「沒有」的元素推斷，非憑空捏造
- [ ] 英文 Prompt 公式語法正確，可直接貼入 Midjourney/DALL-E/Dreamina
- [ ] 字體分析已完成 Typography Treatment 表格（7 種手法逐一確認是否出現）
- [ ] 若出現圖文結合型設計（Combination Mark / Integrated Icon / Negative Space 等），已描述嵌入位置、語義連結，並輸出 AI Prompt 還原關鍵字
