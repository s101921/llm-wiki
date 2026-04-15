---
name: concept-visualizer
description: "知識視覺化工具：將任何知識、概念、系統、流程，直接轉化為好懂、活潑、有類比情境的 PPTX 投影片（概念圖、流程圖、架構圖等）。直接輸出可下載的 .pptx 檔，不做對話版過場。當使用者說「幫我視覺化」「畫成圖」「做成圖表」「解釋 XX 的架構」「XX 是什麼」「XX 的流程是什麼」「幫我整理這個概念」「這段筆記能不能變成圖」「做成簡報」「關係圖」「flowchart」「系統架構」，或上傳文件說要「整理成圖」，都應**立即使用此技能**。即使使用者只說一個名詞（如「RAG」「PDCA」「微服務」「JWT 驗證」），若意圖是理解或解釋，也要完整執行此流程。"
---

# Concept Visualizer

## 核心哲學：你是知識的「翻譯官」

把抽象知識翻成人腦能直接理解的視覺語言。不只是做美圖，是做**讓人「啊！我懂了」的那一刻**。

好的知識投影片有三個層次：
1. **看得懂**（結構清晰、不混亂）
2. **記得住**（有類比、有情境、有記憶錨點）
3. **用得到**（看完知道這個知識在什麼時候發揮作用）

- 所有說明文字：**繁體中文**
- **預設輸出：PPTX 檔（直接產出，不做對話版過場）**

---

## 技術架構

**HTML（CSS 設計系統）→ WeasyPrint → PDF → pdftoppm → JPG → python-pptx → PPTX**

每張投影片都是一個獨立 HTML 檔案，用 CSS 設計系統確保高品質視覺效果，再批次渲染成圖片組合成 PPTX。這個方法的美觀度遠超座標式繪圖（pptxgenjs）。

### 環境確認（首次使用時執行）

```bash
pip install weasyprint python-pptx Pillow --break-system-packages
which pdftoppm || apt-get install -y poppler-utils
```

---

## Step 0：讀懂輸入，找到「骨架」（內部分析，不輸出）

| 輸入形式 | 執行方式 |
|---------|---------|
| 一句話主題（如「JWT 驗證」） | 自行建構知識結構，直接進 Step 1 |
| 貼上文字 / 筆記 | 先萃取核心概念與關係，進 Step 1 |
| 上傳文件（PDF / docx） | 讀取文件，萃取知識骨架，進 Step 1 |

在腦中回答三個問題（**不輸出**，直接進 Step 1）：

**① 核心元素是什麼？**
這個知識涉及哪些角色、元件、步驟、概念？全部列出。

**② 它們怎麼連在一起？**
- 有角色分工、流程傳遞 → **版型A**（三欄角色卡片）
- 有先後順序、線性步驟 → **版型B**（橫排流程圖）
- 有優劣比較、選擇對比 → **版型C**（VS 對比）
- 有層次包含、上下依賴 → **版型D**（巢狀層次）
- 有時間演進、長鏈任務 → **版型E**（地鐵站點時間軸）

**③ 這個知識的「日常類比」是什麼？**
例：JWT = 樂園入場手環；RAG = 開卷考試；Webhook = 快遞到貨簡訊；微服務 = 餐廳各自獨立的廚師站。

---

## Step 1：選版型並查閱範本

讀取版型參考文件以取得完整 HTML 範本：

```
/mnt/skills/user/concept-visualizer/references/slide-templates.md
```

選定最適合的版型後，以該版型的 HTML 範本為基礎，填入實際內容。

---

## Step 2：生成投影片 HTML 檔案

### 設計原則（Critical！）

**色彩系統（Warren 品牌色）：**
```
--primary: #3C80ED    (Warren Blue，主角色)
--sky: #38A1DD        (Warren Sky，副標/箭頭)
--dark: #0a0a0f       (深色背景)
--accent-green: #10B981
--card-bg: rgba(255,255,255,0.04)
```

**固定頁面尺寸（絕對不可更改）：**
```css
@page { size: 1280px 720px; margin: 0; }
body { width: 1280px; height: 720px; overflow: hidden; }
```

**字體規格：**
- 主標題：38-42px, font-weight: 900
- 類比副標：14-16px, italic, color: #60a5fa
- 卡片標題：16-18px, font-weight: 700
- 說明文字：12-14px, color: rgba(255,255,255,0.75)
- 記憶錨點：12px, font-weight: 700

**視覺一致性規則（每張投影片必有）：**
- 頁面頂部藍色漸層條：height 3px, `background: linear-gradient(90deg, #3C80ED, #60a5fa, #38A1DD)`
- 深色漸層背景：`background: linear-gradient(135deg, #0a0a0f 0%, #0d1628 50%, #0a0a0f 100%)`
- 卡片：`rgba(255,255,255,0.04)` 底色 + `rgba(60,128,237,0.25)` 邊框 + 圓角 16-20px
- 記憶錨點（一句話帶走）：底部藍色 pill + 說明文字

**WeasyPrint 相容性注意：**
- 不用 `vh`, `vw`，只用 `px`
- `-webkit-background-clip: text` 文字漸層可能 fallback，加 `color: #ffffff` 作保底
- `gap` 屬性若不生效，改用 `margin` 替代
- Flexbox 基本屬性均支援

### 生成 HTML 檔案

```bash
cat > /home/claude/slide_01.html << 'HTML'
<!DOCTYPE html>
<html><head><meta charset="UTF-8">
<style>
@page { size: 1280px 720px; margin: 0; }
body {
  margin: 0; padding: 0; overflow: hidden;
  width: 1280px; height: 720px;
  font-family: 'Noto Sans TC', Inter, -apple-system, sans-serif;
  background: linear-gradient(135deg, #0a0a0f 0%, #0d1628 50%, #0a0a0f 100%);
  color: #ffffff;
}
/* 根據版型參考文件填入完整 CSS + HTML 內容 */
</style></head><body>
<div class="slide">
  <!-- 版型內容 -->
</div>
</body></html>
HTML
```

---

## Step 3：渲染成 PPTX

使用 skill 內建的 render_slides.py 腳本：

```bash
# 單張投影片
python3 /mnt/skills/user/concept-visualizer/scripts/render_slides.py \
  /home/claude/slide_01.html \
  -o /home/claude/concept.pptx

# 多張投影片（依序傳入）
python3 /mnt/skills/user/concept-visualizer/scripts/render_slides.py \
  /home/claude/slide_01.html \
  /home/claude/slide_02.html \
  -o /home/claude/concept.pptx
```

---

## Step 4：QA 截圖確認

```bash
python3 -c "
import subprocess, weasyprint
html = weasyprint.HTML(filename='/home/claude/slide_01.html')
html.write_pdf('/home/claude/preview.pdf')
subprocess.run(['pdftoppm', '-r', '120', '-jpeg', '-singlefile',
                '/home/claude/preview.pdf', '/home/claude/preview_img'])
print('Done: /home/claude/preview_img.jpg')
"
```

用 `view` 工具看截圖，確認：
- 文字沒超出邊界、沒重疊
- 卡片排列整齊，有足夠呼吸空間（邊距 ≥ 52px）
- 類比副標清晰可見（藍色斜體）
- 記憶錨點存在（底部藍色 pill）
- 整體色調協調（深色背景 + 藍色主色）

發現問題 → 修正 HTML → 重新截圖確認。

---

## Step 5：輸出給使用者

```bash
cp /home/claude/concept.pptx /mnt/user-data/outputs/
```

使用 `present_files` 讓使用者下載，並簡短說明（2-3句）：
1. 選了哪個版型、為什麼
2. 類比是什麼
3. 換底圖方式：PowerPoint → 設計 → 設定背景格式 → 圖片或材質填滿

---

## 複雜度處理原則

| 情況 | 處理方式 |
|-----|---------|
| 元素 > 12 個 | 先出「總覽圖」slide_01，再出「子模組細節」slide_02 |
| 概念過於抽象 | 類比 + 具體 example 放進副標 |
| 輸入文字混亂 | 先說「我看到的核心是...」確認後再作圖 |
| 跨領域複合概念 | 不同領域用不同色系區塊隔開 |

---

## 禁止事項

- ❌ 先輸出對話版圖表，再問要不要做成簡報 — **直接出 PPTX**
- ❌ 逐張確認才繼續（除非使用者明確要求）
- ❌ 不附類比直接上圖
- ❌ 節點放完整句子（只放關鍵詞，說明放卡片內）
- ❌ 說明文字用官腔（「用於實現...的機制」一律改寫成白話）
- ❌ 使用 `vh`/`vw` 單位（WeasyPrint 不支援）
- ❌ 單一投影片超過 15 個節點（必須分層或拆張）
- ❌ 忘記 `@page { size: 1280px 720px; margin: 0; }` — 這是正確渲染的關鍵
