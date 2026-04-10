# Slidev 元件庫 & 動態規範

> 此檔案供 Step 3.6 讀取使用。
> 包含：安裝說明、全域設定、YAML 轉譯規則、頁面類型模板、CSS 動畫庫、背景圖處理規則。
> 持續迭代更新，主 SKILL.md 不需要跟著動。

---

## 安裝說明（對話首次輸出時附上）

```
🚀 Slidev 快速開始

① 安裝 Node.js
  https://nodejs.org → 下載 LTS 版本 → 一路下一步安裝

② 建立專案（終端機執行）
  npm init slidev@latest my-presentation
  cd my-presentation

③ 貼入 Claude 給的程式碼
  用任何編輯器（VS Code 推薦）開啟 slides.md
  全選刪除，貼入 Claude 輸出的程式碼

④ 放入背景圖
  把 AI 生成的背景圖放進 public/ 資料夾
  命名規則：slide-01-bg.jpg、slide-02-bg.jpg……

⑤ 預覽
  npm run dev   → 瀏覽器自動開啟，即時預覽

⑥ 投影播放
  npm run present → 全螢幕簡報模式

播放快捷鍵：
  →  下一個元素出現 / 下一頁
  ←  退回上一個元素
  F  全螢幕切換
  O  投影片總覽（縮圖模式）
  數字 + Enter  跳至指定頁碼
```

---

## 全域設定模板（每份簡報 slides.md 開頭）

```md
---
theme: default
background: none
class: text-white
highlighter: shiki
fonts:
  sans: Noto Sans TC
  mono: Fira Code
---
```

> `Noto Sans TC` 支援繁體中文，`Fira Code` 用於頁碼與等寬數字。
> Slidev 會自動從 Google Fonts 載入，無需手動安裝。

---

## YAML → Slidev 轉譯規則

| YAML 欄位 | 轉譯為 Slidev |
|----------|-------------|
| `visual_instruction.background` | `background-image: url('./public/slide-XX-bg.jpg')` |
| `visual_instruction.composition` | CSS `position: absolute` 定位各區塊 |
| `visual_instruction.elements` | 獨立 `<div>`，各自加 `v-click` 編號 |
| `content.title` | Layer 3 文字，`v-click="2"` |
| `content.subtitle` | Layer 3 文字，`v-click="3"` |
| `content.body_text` 每一條 | 各自獨立 `<div>`，`v-click` 從 4 依序遞增 |
| 頁面裝飾元素（色塊、線條、頁碼） | Layer 2，統一 `v-click="1"` 最先出現 |

### v-click 標準順序

```
v-click="1"  → 裝飾層（色塊、線條、頁碼、幾何）同時出現
v-click="2"  → 主標題
v-click="3"  → 副標題 / 區域標籤
v-click="4"  → body_text 第一條 / 第一張卡片
v-click="5"  → body_text 第二條 / 第二張卡片
...以此類推
```

> 若使用者指定出場順序，依使用者指定覆蓋此預設。

---

## CSS 動畫庫（每份簡報的 `<style>` 區塊，固定附上）

```html
<style>
/* ── 基礎動畫 ── */
@keyframes slideUp {
  from { transform: translateY(40px); opacity: 0; }
  to   { transform: translateY(0);    opacity: 1; }
}
@keyframes slideDown {
  from { transform: translateY(-40px); opacity: 0; }
  to   { transform: translateY(0);     opacity: 1; }
}
@keyframes slideRight {
  from { transform: translateX(-40px); opacity: 0; }
  to   { transform: translateX(0);     opacity: 1; }
}
@keyframes slideLeft {
  from { transform: translateX(40px); opacity: 0; }
  to   { transform: translateX(0);    opacity: 1; }
}
@keyframes fadeIn {
  from { opacity: 0; }
  to   { opacity: 1; }
}
@keyframes scaleIn {
  from { transform: scale(0.85); opacity: 0; }
  to   { transform: scale(1);    opacity: 1; }
}
@keyframes scaleInBounce {
  0%   { transform: scale(0.7);  opacity: 0; }
  70%  { transform: scale(1.05); opacity: 1; }
  100% { transform: scale(1);    opacity: 1; }
}
@keyframes blurIn {
  from { filter: blur(12px); opacity: 0; }
  to   { filter: blur(0);    opacity: 1; }
}
@keyframes lineExpand {
  from { width: 0; opacity: 0; }
  to   { width: 100%; opacity: 1; }
}

/* ── 動畫 class ── */
.anim-up       { animation: slideUp      0.55s ease-out forwards; }
.anim-down     { animation: slideDown    0.55s ease-out forwards; }
.anim-right    { animation: slideRight   0.50s ease-out forwards; }
.anim-left     { animation: slideLeft    0.50s ease-out forwards; }
.anim-fade     { animation: fadeIn       0.50s ease-out forwards; }
.anim-scale    { animation: scaleIn      0.45s ease-out forwards; }
.anim-bounce   { animation: scaleInBounce 0.6s ease-out forwards; }
.anim-blur     { animation: blurIn       0.60s ease-out forwards; }
.anim-line     { animation: lineExpand   0.55s ease-out forwards; }

/* ── 延遲 modifier（疊加使用） ── */
.delay-1 { animation-delay: 0.1s; }
.delay-2 { animation-delay: 0.2s; }
.delay-3 { animation-delay: 0.3s; }
</style>
```

### 動畫選擇邏輯

| 頁面類型 | 標題動畫 | 內容動畫 | 裝飾元素動畫 |
|---------|---------|---------|-----------|
| Cover 封面 | `anim-up` | `anim-fade` | `anim-fade` |
| 核心概念 | `anim-right` | `anim-right` + delay | `anim-fade` |
| 資訊列表 | `anim-up` | `anim-right` 逐條 | `anim-line`（線條） |
| 數據/圖表 | `anim-up` | `anim-scale` | `anim-fade` |
| 引言/呼吸頁 | `anim-blur` | `anim-fade` | `anim-fade` |
| 結論/Q&A | `anim-up` | `anim-fade` | `anim-scale` |

---

## 頁面類型模板庫

> 使用時：複製對應模板 → 替換 `[佔位符]` → 調整顏色與位置數值

---

### 模板 T1：Cover 封面

適用：`type: "Cover"`

**版面：左側文字堆疊 × 右側 AI 背景主角物件**

```html
---
layout: none
---
<div style="position:relative;width:100%;height:100%;
  background-image:url('./public/slide-[XX]-bg.jpg');
  background-size:cover;background-position:center;overflow:hidden;">

  <!-- Layer 2：裝飾元素 -->
  <div v-click="1" class="anim-line" style="
    position:absolute;bottom:0;left:0;height:5px;
    background:linear-gradient(90deg,[ACCENT_COLOR],[SECONDARY_COLOR]);
    width:100%;"/>

  <div v-click="1" class="anim-fade" style="
    position:absolute;bottom:28px;right:52px;
    font-size:96px;font-weight:900;font-family:'Fira Code';
    color:rgba(255,255,255,0.10);line-height:1;">
    [PAGE_NUM]
  </div>

  <!-- Layer 3：文字內容 -->
  <div v-click="2" class="anim-fade" style="
    position:absolute;top:20px;left:60px;
    font-size:12px;font-weight:300;letter-spacing:4px;
    color:[ACCENT_COLOR];text-transform:uppercase;">
    [CATEGORY_LABEL]
  </div>

  <div v-click="3" class="anim-up" style="
    position:absolute;top:36%;left:60px;
    font-size:[TITLE_SIZE]px;font-weight:900;line-height:1.05;
    color:#FFFFFF;max-width:48%;">
    [TITLE]
  </div>

  <div v-click="4" class="anim-fade" style="
    position:absolute;top:62%;left:62px;
    font-size:17px;font-weight:300;font-style:italic;
    color:rgba(255,255,255,0.65);max-width:44%;">
    [SUBTITLE]
  </div>

  <div v-click="5" class="anim-fade" style="
    position:absolute;bottom:24px;left:60px;
    font-size:12px;font-weight:500;letter-spacing:1px;
    color:rgba(255,255,255,0.4);">
    [BRAND_TAG]
  </div>

</div>
```

**佔位符說明：**
- `[XX]` → 頁碼數字（01、02...）
- `[ACCENT_COLOR]` → 強調色 hex
- `[SECONDARY_COLOR]` → 次強調色 hex
- `[PAGE_NUM]` → 頁碼文字（01、02...）
- `[CATEGORY_LABEL]` → 頂部小標籤（例：Generative AI）
- `[TITLE_SIZE]` → 標題字級，建議 56–80
- `[TITLE]` → `content.title`
- `[SUBTITLE]` → `content.subtitle`
- `[BRAND_TAG]` → 品牌標識文字

---

### 模板 T2：核心概念頁（卡片列表型）

適用：`type: "Core Concept"` / `type: "Key Points"`

**版面：上方標題 × 下方 2–4 張橫向卡片，逐張出場**

```html
---
layout: none
---
<div style="position:relative;width:100%;height:100%;
  background-image:url('./public/slide-[XX]-bg.jpg');
  background-size:cover;background-position:center;overflow:hidden;">

  <!-- Layer 2：裝飾元素 -->
  <div v-click="1" class="anim-line" style="
    position:absolute;top:76px;left:0;
    height:1px;width:100%;
    background:linear-gradient(90deg,[ACCENT_COLOR],transparent);"/>

  <div v-click="1" class="anim-fade" style="
    position:absolute;bottom:28px;right:52px;
    font-size:96px;font-weight:900;font-family:'Fira Code';
    color:rgba(255,255,255,0.08);line-height:1;">
    [PAGE_NUM]
  </div>

  <!-- Layer 3：文字內容 -->
  <div v-click="2" class="anim-fade" style="
    position:absolute;top:38px;left:60px;
    font-size:11px;font-weight:400;letter-spacing:4px;
    color:[ACCENT_COLOR];text-transform:uppercase;">
    [SECTION_LABEL]
  </div>

  <div v-click="3" class="anim-up" style="
    position:absolute;top:82px;left:60px;
    font-size:38px;font-weight:900;color:#FFFFFF;">
    [TITLE]
  </div>

  <!-- 卡片區（每張卡片獨立 v-click） -->
  <div v-click="4" class="anim-right" style="
    position:absolute;top:[CARD1_TOP]px;left:60px;right:140px;
    padding:16px 22px;border-radius:6px;
    border-left:4px solid [ACCENT_COLOR];
    background:[CARD_BG];
    box-shadow:0 4px 20px [SHADOW_COLOR];">
    <div style="display:flex;align-items:baseline;gap:14px;">
      <span style="font-size:26px;font-weight:900;font-family:'Fira Code';
        color:[ACCENT_COLOR];">[NUM1]</span>
      <span style="font-size:17px;font-weight:700;color:#fff;">[CARD1_TITLE]</span>
    </div>
    <div style="font-size:13px;color:rgba(255,255,255,0.6);
      margin-top:6px;padding-left:2px;">[CARD1_BODY]</div>
  </div>

  <div v-click="5" class="anim-right delay-1" style="
    position:absolute;top:[CARD2_TOP]px;left:60px;right:140px;
    padding:16px 22px;border-radius:6px;
    border-left:4px solid [ACCENT_COLOR];
    background:[CARD_BG];
    box-shadow:0 4px 20px [SHADOW_COLOR];">
    <div style="display:flex;align-items:baseline;gap:14px;">
      <span style="font-size:26px;font-weight:900;font-family:'Fira Code';
        color:[ACCENT_COLOR];">[NUM2]</span>
      <span style="font-size:17px;font-weight:700;color:#fff;">[CARD2_TITLE]</span>
    </div>
    <div style="font-size:13px;color:rgba(255,255,255,0.6);
      margin-top:6px;padding-left:2px;">[CARD2_BODY]</div>
  </div>

  <div v-click="6" class="anim-right delay-2" style="
    position:absolute;top:[CARD3_TOP]px;left:60px;right:140px;
    padding:16px 22px;border-radius:6px;
    border-left:4px solid [ACCENT_COLOR];
    background:[CARD_BG];
    box-shadow:0 4px 20px [SHADOW_COLOR];">
    <div style="display:flex;align-items:baseline;gap:14px;">
      <span style="font-size:26px;font-weight:900;font-family:'Fira Code';
        color:[ACCENT_COLOR];">[NUM3]</span>
      <span style="font-size:17px;font-weight:700;color:#fff;">[CARD3_TITLE]</span>
    </div>
    <div style="font-size:13px;color:rgba(255,255,255,0.6);
      margin-top:6px;padding-left:2px;">[CARD3_BODY]</div>
  </div>

</div>
```

**卡片位置參考（3張）：**
- `CARD1_TOP`: 170
- `CARD2_TOP`: 295
- `CARD3_TOP`: 420

**卡片位置參考（4張）：**
- `CARD1_TOP`: 160, `CARD2_TOP`: 265, `CARD3_TOP`: 370, `CARD4_TOP`: 475（加第四個 v-click="7" 區塊）

---

### 模板 T3：資訊圖文頁（左文右圖型）

適用：`type: "Info"` / `type: "Process"` / `type: "Comparison"`

**版面：左 55% 文字資訊 × 右 45% AI 背景視覺錨點**

```html
---
layout: none
---
<div style="position:relative;width:100%;height:100%;
  background-image:url('./public/slide-[XX]-bg.jpg');
  background-size:cover;background-position:center;overflow:hidden;">

  <!-- Layer 2：裝飾元素 -->
  <div v-click="1" class="anim-fade" style="
    position:absolute;top:0;left:0;bottom:0;width:58%;
    background:linear-gradient(90deg,
      rgba(0,0,0,0.75) 70%, transparent 100%);"/>

  <div v-click="1" class="anim-line" style="
    position:absolute;top:0;left:58%;
    width:1px;height:100%;
    background:linear-gradient(180deg,
      transparent,[ACCENT_COLOR],transparent);opacity:0.4;"/>

  <div v-click="1" class="anim-fade" style="
    position:absolute;bottom:28px;right:52px;
    font-size:96px;font-weight:900;font-family:'Fira Code';
    color:rgba(255,255,255,0.08);line-height:1;">
    [PAGE_NUM]
  </div>

  <!-- Layer 3：文字內容 -->
  <div v-click="2" class="anim-fade" style="
    position:absolute;top:36px;left:52px;
    font-size:11px;letter-spacing:4px;
    color:[ACCENT_COLOR];text-transform:uppercase;">
    [SECTION_LABEL]
  </div>

  <div v-click="3" class="anim-up" style="
    position:absolute;top:72px;left:52px;
    font-size:36px;font-weight:900;color:#FFFFFF;max-width:52%;">
    [TITLE]
  </div>

  <!-- 條列項目，每條獨立出場 -->
  <div v-click="4" class="anim-right" style="
    position:absolute;top:[ITEM1_TOP]px;left:52px;
    max-width:50%;font-size:15px;color:rgba(255,255,255,0.85);
    padding-left:16px;border-left:3px solid [ACCENT_COLOR];
    line-height:1.6;">
    [ITEM1]
  </div>

  <div v-click="5" class="anim-right delay-1" style="
    position:absolute;top:[ITEM2_TOP]px;left:52px;
    max-width:50%;font-size:15px;color:rgba(255,255,255,0.85);
    padding-left:16px;border-left:3px solid [ACCENT_COLOR];
    line-height:1.6;">
    [ITEM2]
  </div>

  <div v-click="6" class="anim-right delay-2" style="
    position:absolute;top:[ITEM3_TOP]px;left:52px;
    max-width:50%;font-size:15px;color:rgba(255,255,255,0.85);
    padding-left:16px;border-left:3px solid [ACCENT_COLOR];
    line-height:1.6;">
    [ITEM3]
  </div>

</div>
```

---

### 模板 T4：引言 / 呼吸頁

適用：`type: "Quote"` / `type: "Transition"` / `type: "Breather"`

**版面：大字置中，極簡，衝擊感強**

```html
---
layout: none
---
<div style="position:relative;width:100%;height:100%;
  background-image:url('./public/slide-[XX]-bg.jpg');
  background-size:cover;background-position:center;overflow:hidden;">

  <!-- Layer 2：裝飾元素 -->
  <div v-click="1" class="anim-scale" style="
    position:absolute;top:50%;left:50%;
    transform:translate(-50%,-50%);
    width:320px;height:320px;border-radius:50%;
    border:1px solid rgba(255,255,255,0.15);"/>

  <div v-click="1" class="anim-fade" style="
    position:absolute;bottom:0;left:0;
    width:100%;height:3px;
    background:linear-gradient(90deg,
      transparent,[ACCENT_COLOR],transparent);"/>

  <!-- Layer 3：文字內容 -->
  <div v-click="2" class="anim-blur" style="
    position:absolute;top:38%;left:50%;
    transform:translate(-50%,-50%);
    font-size:[QUOTE_SIZE]px;font-weight:900;
    color:#FFFFFF;text-align:center;
    line-height:1.2;white-space:nowrap;">
    [QUOTE_TEXT]
  </div>

  <div v-click="3" class="anim-fade" style="
    position:absolute;top:62%;left:50%;
    transform:translate(-50%,-50%);
    font-size:15px;font-weight:300;
    color:rgba(255,255,255,0.55);text-align:center;">
    [ATTRIBUTION]
  </div>

</div>
```

---

### 模板 T5：數據 / 統計頁

適用：`type: "Data"` / `type: "Stats"`

**版面：大數字橫排展示，每個數字獨立出場**

```html
---
layout: none
---
<div style="position:relative;width:100%;height:100%;
  background-image:url('./public/slide-[XX]-bg.jpg');
  background-size:cover;background-position:center;overflow:hidden;">

  <!-- Layer 2：裝飾元素 -->
  <div v-click="1" class="anim-line" style="
    position:absolute;top:100px;left:60px;right:60px;
    height:1px;background:rgba(255,255,255,0.15);"/>

  <div v-click="1" class="anim-line" style="
    position:absolute;bottom:110px;left:60px;right:60px;
    height:1px;background:rgba(255,255,255,0.15);"/>

  <!-- Layer 3：標題 -->
  <div v-click="2" class="anim-up" style="
    position:absolute;top:48px;left:60px;
    font-size:32px;font-weight:900;color:#FFFFFF;">
    [TITLE]
  </div>

  <!-- 數據區塊（3個，橫排） -->
  <div v-click="3" class="anim-scale" style="
    position:absolute;top:130px;left:7%;
    width:26%;text-align:center;">
    <div style="font-size:72px;font-weight:900;
      color:[ACCENT_COLOR];font-family:'Fira Code';
      line-height:1;">[STAT1_NUM]</div>
    <div style="font-size:14px;color:rgba(255,255,255,0.7);
      margin-top:8px;">[STAT1_LABEL]</div>
  </div>

  <div v-click="4" class="anim-scale delay-1" style="
    position:absolute;top:130px;left:37%;
    width:26%;text-align:center;">
    <div style="font-size:72px;font-weight:900;
      color:[ACCENT_COLOR];font-family:'Fira Code';
      line-height:1;">[STAT2_NUM]</div>
    <div style="font-size:14px;color:rgba(255,255,255,0.7);
      margin-top:8px;">[STAT2_LABEL]</div>
  </div>

  <div v-click="5" class="anim-scale delay-2" style="
    position:absolute;top:130px;left:67%;
    width:26%;text-align:center;">
    <div style="font-size:72px;font-weight:900;
      color:[ACCENT_COLOR];font-family:'Fira Code';
      line-height:1;">[STAT3_NUM]</div>
    <div style="font-size:14px;color:rgba(255,255,255,0.7);
      margin-top:8px;">[STAT3_LABEL]</div>
  </div>

  <!-- 說明文字 -->
  <div v-click="6" class="anim-fade" style="
    position:absolute;bottom:48px;left:60px;right:60px;
    font-size:14px;color:rgba(255,255,255,0.45);
    text-align:center;">[DATA_SOURCE]</div>

</div>
```

---

### 模板 T6：結論 / Q&A 頁

適用：`type: "Closing"` / `type: "QA"` / `type: "CTA"`

**版面：大標題居中偏左，行動呼籲明確，視覺乾淨**

```html
---
layout: none
---
<div style="position:relative;width:100%;height:100%;
  background-image:url('./public/slide-[XX]-bg.jpg');
  background-size:cover;background-position:center;overflow:hidden;">

  <!-- Layer 2：裝飾元素 -->
  <div v-click="1" class="anim-scale" style="
    position:absolute;left:-80px;top:50%;
    transform:translateY(-50%);
    width:280px;height:280px;border-radius:50%;
    background:radial-gradient(circle,
      [ACCENT_COLOR_20] 0%, transparent 70%);"/>

  <div v-click="1" class="anim-fade" style="
    position:absolute;bottom:0;left:0;width:100%;height:4px;
    background:linear-gradient(90deg,[ACCENT_COLOR],[SECONDARY_COLOR]);"/>

  <div v-click="1" class="anim-fade" style="
    position:absolute;bottom:28px;right:52px;
    font-size:96px;font-weight:900;font-family:'Fira Code';
    color:rgba(255,255,255,0.08);line-height:1;">
    [PAGE_NUM]
  </div>

  <!-- Layer 3：文字 -->
  <div v-click="2" class="anim-up" style="
    position:absolute;top:32%;left:60px;
    font-size:56px;font-weight:900;
    color:#FFFFFF;line-height:1.1;max-width:60%;">
    [TITLE]
  </div>

  <div v-click="3" class="anim-fade" style="
    position:absolute;top:58%;left:62px;
    font-size:18px;font-weight:300;
    color:rgba(255,255,255,0.70);max-width:55%;">
    [SUBTITLE]
  </div>

  <div v-click="4" class="anim-scale" style="
    position:absolute;top:70%;left:60px;
    display:inline-block;
    padding:12px 28px;border-radius:4px;
    background:[ACCENT_COLOR];
    font-size:15px;font-weight:700;color:#FFFFFF;
    letter-spacing:1px;">
    [CTA_BUTTON_TEXT]
  </div>

</div>
```

---

## 背景圖 Prompt 修改規則（Slidev 版）

Step 3.5 的圖片 Prompt 預設包含文字排版描述。輸出 Slidev 背景圖版本時，做以下兩項修改：

### ① 加入無文字指令（每頁必加，放在 Prompt 最後）

```
no text, no typography, no written characters, no labels,
no captions, no watermark, no UI overlay elements,
pure visual scene only, composition space reserved for text layer
```

### ② 依版面留空（依頁面類型調整）

| 頁面類型 | 留空指令 |
|---------|---------|
| Cover（左文右圖） | `left 48% kept as clean negative space for text placement` |
| 核心概念（上標下卡） | `upper 45% kept as negative space, lower half for visual element` |
| 左文右圖型 | `left 58% kept as negative space, visual weight on right side` |
| 引言/呼吸頁 | `center composition, edges kept dark for text overlay` |
| 數據頁 | `upper band and lower band kept dark, center for visual element` |
| 結論頁 | `left 60% kept as negative space, right side for atmospheric visual` |

---

## 版本更新日誌

| 版本 | 更新內容 |
|-----|---------|
| v1.0 | 初始建立：T1–T6 六種模板、CSS 動畫庫、背景圖修改規則 |

> 未來擴充方向：Bento Grid 模板（T7）、毛玻璃卡片（T8）、時間軸模板（T9）、3D 視差效果
