# 簡報視覺風格體系 Presentation Visual System

> 此檔案定義簡報設計的視覺語言參考庫。
> 在 Step 1.5 執行時載入，作為風格決策的參考依據——不是硬性框架。
> 內容參考使用者上傳的參考簡報，以及 Warren 品牌美學。

---

## 核心哲學：簡報即廣告海報

> 每一頁簡報的圖片，不是「有文字的背景圖」——
> 而是一件**完整的 artwork**，文字、物件、構圖三者共同構成畫面。
> 資訊頁也是設計作品，不是 Word 文件的截圖。

**三條不可妥協的原則：**
1. **文字是視覺元素，不是說明標籤**——大小落差極端，標題字可以大到成為場景本體
2. **每頁必有視覺錨點**——3D物件、真實人像、超大字體、抽象幾何，至少其一
3. **顏色有理由**——每個色彩服務整體情緒，沒有「剛好放在那裡」的色

---

## ⚠️ 風格使用邏輯（必讀）

下方的五種風格類型（A–E）是**靈感參考庫，不是硬性選項**。

| 輸入情境 | 正確做法 |
|---------|---------|
| 使用者上傳風格參考圖 | **完全依照圖片萃取**，不強制套用 A–E，A–E 只作為延伸參考 |
| 使用者指定風格（例：「日式極簡」「賽博龐克」「奢華感」） | **依據該風格的審美邏輯自由推導**，從 A–E 中借用最接近的設計語言元素 |
| 使用者完全沒有給風格線索 | 才從 A–E 中選最適合的，作為起點 |
| 使用者提到 Warren / Warren色 / 品牌色 | 優先載入下方 **Warren 品牌色系統**，覆蓋其他色彩決策 |

> 審美標準高於框架。若使用者的需求介於兩種風格之間，或需要混合，
> 就混合——不必「選一個風格然後嚴格遵守」。

---

## 五種風格類型（參考庫）

---

### 🖤 風格 A：極簡黑白系 Minimal Black & White

**適用參考：** 學術研究、法律法規、企業治理、嚴肅議題
**氛圍：** 結構感、權威感、高級感、克制的張力
**色彩規則：** 最多 3 色——黑/深炭 + 白/米白 + 一個強調色（只用在關鍵詞或圖表）

#### 設計特徵
- 大面積留白是主角，不是空白
- 標題字極大（佔版面 30–50%），字重對比強烈（超粗 vs 超細）
- 幾何線條作為唯一裝飾（細線、規則網格、矩形框）
- 資訊層次靠字體大小而非顏色區分

#### 版面邏輯
- 左對齊為主，不對稱構圖
- 強調色只用於 1–2 個需要「被記住」的詞
- 圖片/插圖使用黑白或單色調

#### Prompt 關鍵詞
```
minimal editorial design, extreme typographic scale contrast, intentional negative space,
monochromatic palette with single accent color, geometric precision,
Swiss design influence, grid-based layout, asymmetric balance,
premium monochromatic palette, bold sans-serif headline vs hairline body text,
high contrast black and white with restrained color pop
```
#### Negative Prompt
```
colorful background, decorative illustration, multiple competing colors,
equal size text, busy layout, centered symmetric composition,
gradient rainbow, casual font mixing
```
#### image_base_prompt 模板
```
minimal editorial design, extreme typographic scale contrast, intentional negative space,
monochromatic palette with single accent color, geometric precision,
presentation slide as full artwork poster, 16:9 landscape,
ultra detailed, high production value, 8K resolution, masterpiece
```

---

### 🔵 風格 B：3D 超現實物件系 3D Surreal Object

**適用參考：** 科技、AI、創新、品牌行銷、創意提案
**氛圍：** 未來感、驚喜感、設計力、打破現實的衝擊
**色彩規則：** 一個主色調統治畫面（飽和藍/粉/紫），3D物件帶有金屬或彩虹材質光澤

#### 設計特徵
- 畫面中心有一個或多個 **3D 主角物件**（科技產品異化版、幾何體、擬人化物件）
- 物件材質豐富：毛茸茸、液態金屬、透明玻璃、iridescent 彩虹光澤
- 文字圍繞或穿插物件，不是貼在物件上方
- 背景是純色或漸層（不是照片），讓 3D 物件完全主導視覺

#### 版面邏輯
- 物件偏右或居中，文字偏左
- 大標題字可以「藏在」物件後方，製造前後層次
- 角落有小型輔助物件（散落感，不擁擠）
- 頁碼或品牌標識用超大字體作為設計元素

#### 3D 物件選擇原則
| 主題情境 | 建議 3D 物件 |
|---------|------------|
| AI / 科技 | 毛茸茸電腦、透明幾何體、液態金屬球、電路板異化 |
| 品牌行銷 | 產品巨大化、CD 長出植物、日常物件超現實錯置 |
| 創意提案 | 抽象幾何漂浮體、水晶礦石、iridescent 有機形態 |
| 數據/流程 | 連結鎖鏈（透明）、流動管道、立方體堆疊 |

#### Prompt 關鍵詞
```
CGI 3D hero object, iridescent material surface, liquid metal texture,
furry oversized object, translucent glass geometry,
surreal object in dreamlike environment, floating in gradient background,
3D render with cinematic lighting, object as main protagonist,
text layered around 3D object, floating scattered accent objects,
photorealistic CGI material, soft volumetric light
```
#### Negative Prompt
```
flat illustration, 2D graphic only, realistic photography without 3D element,
plain text on plain background, dark oppressive atmosphere,
low quality render, plastic toy look without material depth
```
#### image_base_prompt 模板
```
CGI 3D hero object with iridescent or liquid metal material, cinematic volumetric lighting,
surreal object floating in gradient environment, text layered around 3D protagonist,
saturated single dominant hue background, presentation slide as full artwork poster,
16:9 landscape, ultra detailed, high production value, 8K resolution, masterpiece
```

---

### 🌈 風格 C：CGI 夢幻世界系 CGI Dreamscape

**適用參考：** 品牌故事、課程體驗、消費者旅程、未來願景
**氛圍：** 夢幻、浸入感、粉色系或天空系、讓人想活在其中
**色彩規則：** 粉藍/粉紫/天藍漸層為主調，整個畫面是一個「可以走進去的世界」

#### 設計特徵
- 整個畫面是一個完整構建的 CGI 場景（不是物件放在背景前）
- 有天空、地平線、反射水面等環境要素製造景深
- 主角物件漂浮在場景中，帶有翅膀/發光/光環等奇幻元素
- 文字疊加在場景上，用對比色或白色確保可讀性

#### 版面邏輯
- 標題在上方，物件橫排在中間，說明文字在底部
- 物件之間有空間感，不擁擠
- 整個場景有「遠中近」三層景深

#### Prompt 關鍵詞
```
full CGI dreamscape environment, pastel pink and blue sky,
reflective water surface, floating objects in magical world,
volumetric cloud atmosphere, soft gradient horizon,
winged or glowing hero objects, three-layer depth foreground-midground-background,
kawaii surreal world, color-saturated fantasy scene,
objects casting real shadows in CGI world, cinematic soft light
```
#### Negative Prompt
```
dark moody lighting, realistic photography, harsh shadows,
corporate flat design, monochromatic only, heavy dark background,
random object placement without world-building
```
#### image_base_prompt 模板
```
full CGI dreamscape environment, pastel gradient sky, reflective surface, three-layer depth,
floating glowing objects in magical world, saturated fantasy color world,
presentation slide as full artwork poster, 16:9 landscape,
ultra detailed, high production value, 8K resolution, masterpiece
```

---

### ⚡ 風格 D：霓虹混合媒材系 Neon Mixed Media

**適用參考：** 數位轉型、社群行銷、Z世代受眾、科技 × 人文交叉
**氛圍：** 衝擊、前衛、刻意的「不協調的協調」、能量感
**色彩規則：** 深黑底 + 霓虹強調色（電藍/螢光紫/洋紅），或高飽和純色底

#### 設計特徵
- **真實人像或攝影元素**與 CGI/數位元素並置，刻意保留媒材差異
- 超大中文字與英文字混排，字體風格刻意衝突（手寫 × 粗黑 × 細線）
- 發光邊框、數位雜訊、掃描線、UI 元素（Ctrl+C、Enter、進度條）作為裝飾
- 資訊不是「整齊排列」而是「散落但有節奏」

#### 版面邏輯
- 左側大字（主題詞）+ 右側場景/人像，非對稱強分割
- 中間有明確的「分界線」或「通道」（發光門框、幾何切割）
- 文字可以放大到超出畫框邊緣（只看到一半也沒關係）
- 品牌標識用小字放在角落，反而更有設計感

#### Prompt 關鍵詞
```
neon mixed media composition, real photography composited with CGI elements,
intentional style clash between photographic and digital,
oversized Chinese and English mixed typography, extreme font weight contrast,
glowing neon outlines, digital noise texture, scan line overlay,
black background with electric accent color, UI elements as decoration,
text bleeding off frame edge, asymmetric strong split layout,
cyberpunk meets editorial photography
```
#### Negative Prompt
```
clean corporate layout, soft pastel, everything same style,
text neatly contained, symmetric composition,
no photographic element, generic tech icons, low contrast
```
#### image_base_prompt 模板
```
neon mixed media, real photography composited with CGI digital elements,
intentional style clash, oversized mixed Chinese-English typography, extreme font contrast,
deep black background with electric accent neon color, cyberpunk editorial,
presentation slide as full artwork poster, 16:9 landscape,
ultra detailed, high production value, 8K resolution, masterpiece
```

---

### 📋 風格 E：資訊海報系 Info-Poster

**適用參考：** 流程說明、數據呈現、比較分析、步驟教學
**氛圍：** 清晰但有設計感，資訊密度高但不壓迫，「好看的教材」
**色彩規則：** 白或淺色底 + 一個主強調色系 + 深色文字，用色塊區隔資訊而非線條

#### 設計特徵
- **右側永遠有一個「視覺錨點」**：3D 插圖、真實人物、產品照，打破純文字版面
- 文字區用飽和色塊（圓角矩形）包住重要詞彙，不只是底線
- 超大英文字作為背景裝飾層（低透明度），與資訊內容呼應
- 箭頭、連結線用品牌色而非灰色，有能量感

#### 版面邏輯
- 左側 60% 為資訊區，右側 40% 為視覺錨點
- 標題用大字 + 強調色強調關鍵詞（不是整句標題都強調）
- 表格/清單用色塊填底而非邊框線

#### 視覺錨點選擇原則
| 資訊類型 | 建議視覺錨點 |
|---------|-----------|
| 流程/步驟 | 3D 分層圖（菜單展開、積木堆疊） |
| 比較分析 | 真實人物手持產品、互動式場景 |
| 數據統計 | 3D 圖表物件化（柱狀圖變成積木） |
| 概念說明 | 概念的具象化 3D 物件 |

#### Prompt 關鍵詞
```
info-poster design with strong visual anchor on right,
clean white background with color block text highlights,
rounded rectangle color tags in brand palette,
large low-opacity English text as background decoration layer,
real person or 3D illustration as right-side focal point,
arrow and connector in accent color,
typographic scale contrast: bold keyword vs light body,
structured yet dynamic layout, scannable information hierarchy
```
#### Negative Prompt
```
pure text layout without visual element, gray border tables,
all same font size, no color emphasis, stock photo background,
equally sized information blocks, no typographic hierarchy
```
#### image_base_prompt 模板
```
info-poster layout, white background with bold color block highlights,
right-side 3D or photographic visual anchor, strong typographic hierarchy,
scannable information design with visual energy, brand accent color system,
presentation slide as full artwork poster, 16:9 landscape,
ultra detailed, high production value, 8K resolution, masterpiece
```

---

## Warren 品牌色系統

> **觸發條件：** 使用者輸入出現以下任一關鍵詞時載入：
> `Warren`、`瓦倫`、`Warren色`、`品牌色`、`Warren風格`、`MKT?Whatever`
>
> 載入後，Warren 色系**覆蓋**其他所有色彩決策，成為整份簡報的色彩主軸。

### 品牌主色

| 色名 | Hex | 用途 |
|------|-----|------|
| Warren Blue | `#3C80ED` | 核心主色，品牌識別錨點，永遠是視覺主角 |
| Warren Sky | `#38A1DD` | 次主色，與主色形成藍色漸層，用於次要強調 |

### 情境色票選擇

根據主題情境，從以下五個情境色票中選一組搭配 Warren Blue：

#### 情境 1：高級奢華 Luxury
**觸發詞：** 奢華、高級、精品、尊貴、luxury
```
Warren Blue (#3C80ED) + 香檳金 (#E0C56E) + 深炭灰 (#1E1E1E) + 象牙白 (#FFFDD0)
Prompt: Warren Blue (#3C80ED) as hero color, champagne gold (#E0C56E) accent trim,
deep charcoal (#1E1E1E) background, ivory white (#FFFDD0) negative space,
precious metal luster, understated luxury palette
```

#### 情境 2：時尚高端 Fashion
**觸發詞：** 時尚、fashion、editorial、前衛、態度
```
Warren Blue (#3C80ED) + 裸膚色 (#D3C5B7) + 乾燥玫瑰 (#D8AFA0) + 亮白 (#F8F8F8)
Prompt: Warren Blue (#3C80ED) as fashion statement color, nude tone (#D3C5B7) neutral base,
dusty rose (#D8AFA0) sensory accent, high-end fashion palette, editorial color language
```

#### 情境 3：文青氛圍 Artistic
**觸發詞：** 文青、藝術、復古、手感、vintage、詩意
```
Warren Blue (#3C80ED) + 赤陶色 (#A0522D) + 米書紙 (#F5F5DC) + 橄欖綠 (#556B2F)
Prompt: Warren Blue (#3C80ED) against warm terracotta (#A0522D),
aged paper (#F5F5DC) background, olive green (#556B2F) nature accent,
film grain texture, artisanal warm-cool bohemian contrast
```

#### 情境 4：商業應用 Corporate（簡報最常用）
**觸發詞：** 商業、企業、professional、corporate、品牌形象、信賴感
```
Warren Blue (#3C80ED) + 中性灰 (#808080) + 淺灰藍 (#F0F2F5) + 純白 (#FFFFFF)
Prompt: Warren Blue (#3C80ED) as primary brand color, medium gray (#808080) secondary,
light gray-blue (#F0F2F5) background zones, clean professional palette,
systematic color hierarchy, corporate trust aesthetic
```

#### 情境 5：流行消費 Trendy
**觸發詞：** 流行、消費、年輕、活力、潮流、trendy、活潑
```
Warren Blue (#3C80ED) + 活力珊瑚粉 (#FF4D6D) + 陽光黃 (#FFD166) + 深空藍 (#0D1B2A)
Prompt: Warren Blue (#3C80ED) + vibrant coral (#FF4D6D) high-contrast pop,
sunshine yellow (#FFD166) energy accent, deep space blue (#0D1B2A) dark base,
bold color clash, youthful dynamic energy, trendy color blocking
```

### Warren Negative Prompt（通用）
```
colors competing with Warren Blue, unsystematic color mixing,
warm tones without Warren Blue anchor, generic corporate blue (not #3C80ED)
```

---

## 跨風格共用原則

### 中英文混排規則（所有風格適用）
- 中文主標題 + 英文副標或分類標籤，兩者字體風格可以刻意對比
- 英文不是翻譯，是**另一個資訊層**（例：大字「趨勢」旁邊有小字「Generative AI」）
- 數字用西文字體，視覺上比中文數字更有力量感
- 頁碼可以超大（「01」佔版面角落 10%）

### 光線規則（所有風格適用）
- **禁止平光**——每頁都要有明確的光源方向（左/右/上/下）
- 3D 物件要有環境光與投影，不能浮在空中沒有影子
- 深色背景用冷色調補光（電藍/青），淺色背景用暖色調補光（金/橙）

### 構圖節奏規則（整份簡報層面）
- 深色頁與淺色頁交替出現，避免連續相同背景
- 「震撼頁」（封面/核心概念）與「資訊頁」（說明/數據）交替節奏
- 每 3–4 頁有一頁「呼吸頁」——元素極少，一個大字或一個大物件


---

## 核心哲學：簡報即廣告海報

> 每一頁簡報的圖片，不是「有文字的背景圖」——
> 而是一件**完整的 artwork**，文字、物件、構圖三者共同構成畫面。
> 資訊頁也是設計作品，不是 Word 文件的截圖。

**三條不可妥協的原則：**
1. **文字是視覺元素，不是說明標籤**——大小落差極端，標題字可以大到成為場景本體
2. **每頁必有視覺錨點**——3D物件、真實人像、超大字體、抽象幾何，至少其一
3. **顏色有理由**——每個色彩服務整體情緒，沒有「剛好放在那裡」的色

---

## 簡報風格光譜（5個風格類型）

> 根據主題情境選擇一個主風格，同一份簡報維持同一風格光譜，確保視覺一致。

---

### 🖤 風格 A：極簡黑白系 Minimal Black & White

**適用主題：** 學術研究、法律法規、企業治理、嚴肅議題
**氛圍：** 結構感、權威感、高級感、克制的張力
**色彩規則：** 最多 3 色——黑/深炭 + 白/米白 + 一個強調色（只用在關鍵詞或圖表）

#### 設計特徵
- 大面積留白是主角，不是空白
- 標題字極大（佔版面 30–50%），字重對比強烈（超粗 vs 超細）
- 幾何線條作為唯一裝飾（細線、規則網格、矩形框）
- 資訊層次靠字體大小而非顏色區分

#### 版面邏輯
- 左對齊為主，不對稱構圖
- 強調色只用於1–2個需要「被記住」的詞
- 圖片/插圖使用黑白或單色調

#### Prompt 關鍵詞
```
minimal black and white editorial design, extreme typographic hierarchy,
bold sans-serif headline vs hairline body text, intentional white space,
single accent color for key term, geometric line dividers,
high contrast black and white with restrained color pop,
Swiss design influence, grid-based layout, asymmetric balance,
premium monochromatic palette
```

#### Negative Prompt
```
colorful background, decorative illustration, multiple competing colors,
equal size text, busy layout, centered symmetric composition,
gradient rainbow, casual font mixing
```

---

### 🔵 風格 B：3D 超現實物件系 3D Surreal Object

**適用主題：** 科技、AI、創新、品牌行銷、創意提案
**氛圍：** 未來感、驚喜感、設計力、打破現實的衝擊
**色彩規則：** 一個主色調統治畫面（飽和藍/粉/紫），3D物件帶有金屬或彩虹材質光澤

#### 設計特徵
- 畫面中心有一個或多個**3D 主角物件**（可以是：科技產品異化版、幾何體、擬人化物件）
- 物件材質豐富：毛茸茸、液態金屬、透明玻璃、iridescent 彩虹光澤
- 文字圍繞或穿插物件，不是貼在物件上方
- 背景是純色或漸層（不是照片），讓 3D 物件完全主導視覺

#### 版面邏輯
- 物件偏右或居中，文字偏左
- 大標題字可以「藏在」物件後方，製造前後層次
- 角落有小型輔助物件（散落感，不擁擠）
- 頁碼或品牌標識用超大字體作為設計元素

#### 3D 物件選擇原則
| 主題情境 | 建議 3D 物件 |
|---------|------------|
| AI / 科技 | 毛茸茸電腦、透明幾何體、液態金屬球、電路板異化 |
| 品牌行銷 | 產品巨大化、CD 長出植物、日常物件超現實錯置 |
| 創意提案 | 抽象幾何漂浮體、水晶礦石、iridescent 有機形態 |
| 數據/流程 | 連結鎖鏈（透明）、流動管道、立方體堆疊 |

#### Prompt 關鍵詞
```
CGI 3D hero object, iridescent material surface, liquid metal texture,
furry oversized object, translucent glass geometry,
surreal object in dreamlike environment, floating in gradient background,
3D render with cinematic lighting, object as main protagonist,
text layered around 3D object, floating scattered accent objects,
photorealistic CGI material, soft volumetric light
```

#### Negative Prompt
```
flat illustration, 2D graphic only, realistic photography without 3D element,
plain text on plain background, dark oppressive atmosphere,
low quality render, plastic toy look without material depth
```

---

### 🌈 風格 C：CGI 夢幻世界系 CGI Dreamscape

**適用主題：** 品牌故事、課程體驗、消費者旅程、未來願景
**氛圍：** 夢幻、浸入感、粉色系或天空系、讓人想活在其中
**色彩規則：** 粉藍/粉紫/天藍漸層為主調，整個畫面是一個「可以走進去的世界」

#### 設計特徵
- 整個畫面是一個完整構建的 CGI 場景（不是物件放在背景前）
- 有天空、地平線、反射水面等環境要素製造景深
- 主角物件漂浮在場景中，帶有翅膀/發光/光環等奇幻元素
- 文字疊加在場景上，用對比色或白色確保可讀性

#### 版面邏輯
- 標題在上方，物件橫排在中間，說明文字在底部
- 物件之間有空間感，不擁擠
- 整個場景有「遠中近」三層景深

#### Prompt 關鍵詞
```
full CGI dreamscape environment, pastel pink and blue sky,
reflective water surface, floating objects in magical world,
volumetric cloud atmosphere, soft gradient horizon,
winged or glowing hero objects, three-layer depth foreground-midground-background,
kawaii surreal world, color-saturated fantasy scene,
objects casting real shadows in CGI world, cinematic soft light
```

#### Negative Prompt
```
dark moody lighting, realistic photography, harsh shadows,
corporate flat design, monochromatic only, heavy dark background,
random object placement without world-building
```

---

### ⚡ 風格 D：霓虹混合媒材系 Neon Mixed Media

**適用主題：** 數位轉型、社群行銷、Z世代受眾、科技 × 人文交叉
**氛圍：** 衝擊、前衛、刻意的「不協調的協調」、能量感
**色彩規則：** 深黑底 + 霓虹強調色（電藍/螢光紫/洋紅），或高飽和純色底

#### 設計特徵
- **真實人像或攝影元素**與 CGI/數位元素並置，刻意保留媒材差異
- 超大中文字與英文字混排，字體風格刻意衝突（手寫 × 粗黑 × 細線）
- 發光邊框、數位雜訊、掃描線、UI 元素（Ctrl+C、Enter、進度條）作為裝飾
- 資訊不是「整齊排列」而是「散落但有節奏」

#### 版面邏輯
- 左側大字（主題詞）+ 右側場景/人像，非對稱強分割
- 中間有明確的「分界線」或「通道」（發光門框、幾何切割）
- 文字可以放大到超出畫框邊緣（只看到一半也沒關係）
- 品牌標識用小字放在角落，反而更有設計感

#### Prompt 關鍵詞
```
neon mixed media composition, real photography composited with CGI elements,
intentional style clash between photographic and digital,
oversized Chinese and English mixed typography, extreme font weight contrast,
glowing neon outlines, digital noise texture, scan line overlay,
black background with electric accent color, UI elements as decoration,
text bleeding off frame edge, asymmetric strong split layout,
cyberpunk meets editorial photography
```

#### Negative Prompt
```
clean corporate layout, soft pastel, everything same style,
text neatly contained, symmetric composition,
no photographic element, generic tech icons, low contrast
```

---

### 📋 風格 E：資訊海報系 Info-Poster

**適用主題：** 流程說明、數據呈現、比較分析、步驟教學
**氛圍：** 清晰但有設計感，資訊密度高但不壓迫，「好看的教材」
**色彩規則：** 白或淺色底 + 一個主強調色系 + 深色文字，用色塊區隔資訊而非線條

#### 設計特徵
- **右側永遠有一個「視覺錨點」**：3D 插圖、真實人物、產品照，打破純文字版面
- 文字區用飽和色塊（圓角矩形）包住重要詞彙，不只是底線
- 超大英文字作為背景裝飾層（低透明度），與資訊內容呼應
- 箭頭、連結線用品牌色而非灰色，有能量感

#### 版面邏輯
- 左側 60% 為資訊區，右側 40% 為視覺錨點
- 標題用大字 + 強調色強調關鍵詞（不是整句標題都強調）
- 表格/清單用色塊填底而非邊框線

#### 視覺錨點選擇原則
| 資訊類型 | 建議視覺錨點 |
|---------|-----------|
| 流程/步驟 | 3D 分層圖（如菜單展開、積木堆疊） |
| 比較分析 | 真實人物手持產品、互動式場景 |
| 數據統計 | 3D 圖表物件化（柱狀圖變成積木） |
| 概念說明 | 概念的具象化 3D 物件 |

#### Prompt 關鍵詞
```
info-poster design with strong visual anchor on right,
clean white background with color block text highlights,
rounded rectangle color tags in brand palette,
large low-opacity English text as background decoration layer,
real person or 3D illustration as right-side focal point,
arrow and connector in accent color,
typographic scale contrast: bold keyword vs light body,
structured yet dynamic layout, scannable information hierarchy
```

#### Negative Prompt
```
pure text layout without visual element, gray border tables,
all same font size, no color emphasis, stock photo background,
equally sized information blocks, no typographic hierarchy
```

---

## ⚠️ 視覺錨點多樣化原則（最高優先，所有風格適用）

**問題根源：** 從參考圖萃取風格時，若不加區分地連主體也複製，
會導致整份簡報每頁都出現同樣的主體（山、石頭、電腦……），設計感立刻消失。

**正確做法：**
- 參考圖 → **只取視覺語言**（色彩、字體、版面分割、氛圍關鍵字）
- 每頁主體 → **根據該頁內容主題獨立發想**，刻意多樣化

**整份簡報視覺錨點節奏範例（10頁）：**

| 頁次 | 視覺錨點類型 | 具體物件方向 |
|-----|-----------|------------|
| p1 封面 | 巨大幾何體 | 半透明多面體，藍色光折射 |
| p2 背景問題 | 真實物件特寫 | 碎裂石頭/玻璃，象徵界線 |
| p3 核心概念 | 超大字即主視覺 | 版面本身是設計，無附加主體 |
| p4 第一論點 | 3D 抽象形態 | 液態金屬球體分裂 |
| p5 第二論點 | 建築/結構線框 | 幾何建築透視，帶電路感 |
| p6 流程說明 | 機械/工具物件 | 齒輪或管道連結 |
| p7 數據頁 | 數字本身即主視覺 | 超大數字，背景輔助 |
| p8 案例 | 混合媒材人像 | 真實人像 + 數位疊加元素 |
| p9 結論 | 光線爆發 | 單一冷光源向外放射 |
| p10 Q&A | 極簡符號 | 巨大問號，極度留白 |

**硬規則：**
- 同一類型主體，不連續超過 2 頁
- **「統一主體系列版」是使用者主動要求後才提供的選項，不是預設**
- 使用者說「太活潑、希望更一致」→ 才提供統一主體建議

---

## 跨風格共用原則

### 中英文混排規則（所有風格適用）
- 中文主標題 + 英文副標或分類標籤，兩者字體風格可以刻意對比
- 英文不是翻譯，是**另一個資訊層**（例：大字「趨勢」旁邊有小字「Generative AI」）
- 數字用西文字體，視覺上比中文數字更有力量感
- 頁碼可以超大（「01」佔版面角落 10%）

### 光線規則（所有風格適用）
- **禁止平光**——每頁都要有明確的光源方向（左/右/上/下）
- 3D 物件要有環境光與投影，不能浮在空中沒有影子
- 深色背景用冷色調補光（電藍/青），淺色背景用暖色調補光（金/橙）

### 構圖節奏規則（整份簡報層面）
- 深色頁與淺色頁交替出現，避免連續相同背景
- 「震撼頁」（封面/核心概念）與「資訊頁」（說明/數據）交替節奏
- 每 3–4 頁有一頁「呼吸頁」——元素極少，一個大字或一個大物件

---

## 風格選擇決策樹

```
收到主題後，判斷：

① 主題有沒有「視覺感強的主角」？
   （AI、科技產品、品牌、創意）→ B 或 C 或 D
   （法律、學術、數據、嚴肅）→ A 或 E

② 受眾是誰？
   企業決策者/學術圈 → A（極簡）或 E（資訊海報）
   品牌行銷/創意圈 → B（3D物件）或 D（霓虹混合）
   一般大眾/消費者 → C（CGI夢幻）或 B（3D物件）

③ 有無上傳風格參考圖？
   有 → 從圖片萃取最接近的風格類型，以上表為骨架延伸
   無 → 依①②判斷，大膽選擇，不選「最安全的」選「最有記憶點的」

④ 確認後，整份簡報鎖定同一風格，不混用
   （除非使用者明確要求「這一頁用不同風格」）
```

---

## 各風格的 image_base_prompt 模板

生成 `global_design_spec.image_base_prompt` 時，從對應風格直接取用：

**風格 A 模板：**
```
minimal editorial design, extreme typographic scale contrast, intentional negative space,
monochromatic palette with single accent color, geometric precision,
presentation slide as full artwork poster, 16:9 landscape,
ultra detailed, high production value, 8K resolution, masterpiece
```

**風格 B 模板：**
```
CGI 3D hero object with iridescent or liquid metal material, cinematic volumetric lighting,
surreal object floating in gradient environment, text layered around 3D protagonist,
saturated single dominant hue background, presentation slide as full artwork poster,
16:9 landscape, ultra detailed, high production value, 8K resolution, masterpiece
```

**風格 C 模板：**
```
full CGI dreamscape environment, pastel gradient sky, reflective surface, three-layer depth,
floating glowing objects in magical world, saturated fantasy color world,
presentation slide as full artwork poster, 16:9 landscape,
ultra detailed, high production value, 8K resolution, masterpiece
```

**風格 D 模板：**
```
neon mixed media, real photography composited with CGI digital elements,
intentional style clash, oversized mixed Chinese-English typography, extreme font contrast,
deep black background with electric accent neon color, cyberpunk editorial,
presentation slide as full artwork poster, 16:9 landscape,
ultra detailed, high production value, 8K resolution, masterpiece
```

**風格 E 模板：**
```
info-poster layout, white background with bold color block highlights,
right-side 3D or photographic visual anchor, strong typographic hierarchy,
scannable information design with visual energy, brand accent color system,
presentation slide as full artwork poster, 16:9 landscape,
ultra detailed, high production value, 8K resolution, masterpiece
```
