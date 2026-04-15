# HTML 投影片版型庫（CSS 設計系統）

本文件為 concept-visualizer skill 的版型參考。每個版型都是完整的 HTML 檔案。

## 共用 CSS 變數（所有版型必須遵守）

```css
/* Warren 品牌色系 */
--primary: #3C80ED;       /* Warren Blue — 主角色 */
--sky: #38A1DD;           /* Warren Sky — 副標/箭頭 */
--dark: #0a0a0f;          /* 深色背景 */
--card-bg: rgba(255,255,255,0.04); /* 卡片底色 */
--card-border: rgba(60,128,237,0.25);
--text-main: #ffffff;
--text-sub: rgba(255,255,255,0.75);
--text-muted: rgba(255,255,255,0.4);
--accent-green: #10B981;
--accent-warn: #A0522D;
```

## 頁面尺寸規格（固定，不可變動）

```css
@page { size: 1280px 720px; margin: 0; }
body { width: 1280px; height: 720px; overflow: hidden; }
```

---

## 版型 A：三欄角色卡片（有角色分工的概念）

適用：JWT 驗證、微服務架構、MVC 模式、前後端分工

```html
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
.slide {
  width: 1280px; height: 720px;
  padding: 52px 64px 40px;
  box-sizing: border-box;
  display: flex; flex-direction: column;
  position: relative;
}
.slide::before {
  content: ''; position: absolute;
  top: 0; left: 0; right: 0; height: 3px;
  background: linear-gradient(90deg, #3C80ED, #60a5fa, #38A1DD);
}
h1 {
  font-size: 38px; font-weight: 900; margin: 0 0 8px 0;
  background: linear-gradient(135deg, #fff 0%, #a0c4ff 100%);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.analogy { color: #60a5fa; font-size: 14px; font-style: italic; margin-bottom: 32px; }
.cards { display: flex; gap: 20px; flex: 1; }
.card {
  flex: 1; background: rgba(255,255,255,0.04);
  border: 1px solid rgba(60,128,237,0.25);
  border-radius: 18px; padding: 24px 22px;
  position: relative; overflow: hidden;
}
.card::before {
  content: ''; position: absolute;
  top: 0; left: 0; right: 0; height: 3px;
  background: linear-gradient(90deg, #3C80ED, #60a5fa, transparent);
}
.card-num { font-size: 10px; font-weight: 700; letter-spacing: 0.15em; color: #3C80ED; margin-bottom: 6px; }
.card-title { font-size: 17px; font-weight: 700; margin-bottom: 6px; }
.card-role { font-size: 12px; color: rgba(255,255,255,0.4); font-style: italic; margin-bottom: 14px; }
.card-body { font-size: 13px; color: rgba(255,255,255,0.75); line-height: 1.65; }
.memo { margin-top: 20px; display: flex; align-items: center; gap: 12px; }
.memo-pill {
  background: linear-gradient(90deg, #3C80ED, #60a5fa);
  border-radius: 20px; padding: 7px 18px;
  font-size: 12px; font-weight: 700; white-space: nowrap;
}
.memo-text { font-size: 13px; color: rgba(255,255,255,0.5); }
</style></head><body>
<div class="slide">
  <h1>概念主標題</h1>
  <div class="analogy">💡 類比副標——讓觀眾先建立直覺</div>
  <div class="cards">
    <div class="card">
      <div class="card-num">01 / ROLE_A</div>
      <div class="card-title">🎯 角色 A</div>
      <div class="card-role">「它的核心問題是？」</div>
      <div class="card-body">具體說明角色 A 的職責與行為，用日常語言描述。</div>
    </div>
    <div class="card">
      <div class="card-num">02 / ROLE_B</div>
      <div class="card-title">⚙️ 角色 B</div>
      <div class="card-role">「它的核心問題是？」</div>
      <div class="card-body">具體說明角色 B 的職責與行為，用日常語言描述。</div>
    </div>
    <div class="card">
      <div class="card-num">03 / ROLE_C</div>
      <div class="card-title">📦 角色 C</div>
      <div class="card-role">「它的核心問題是？」</div>
      <div class="card-body">具體說明角色 C 的職責與行為，用日常語言描述。</div>
    </div>
  </div>
  <div class="memo">
    <div class="memo-pill">💬 一句話帶走</div>
    <div class="memo-text">用一句話總結這個概念的精髓</div>
  </div>
</div>
</body></html>
```

---

## 版型 B：橫排流程圖（線性步驟）

適用：CI/CD 流程、OAuth 認證流、資料處理管道

```html
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
.slide {
  width: 1280px; height: 720px;
  padding: 52px 64px 40px;
  box-sizing: border-box;
  display: flex; flex-direction: column;
  position: relative;
}
.slide::before {
  content: ''; position: absolute;
  top: 0; left: 0; right: 0; height: 3px;
  background: linear-gradient(90deg, #3C80ED, #60a5fa, #38A1DD);
}
h1 {
  font-size: 38px; font-weight: 900; margin: 0 0 8px 0;
  background: linear-gradient(135deg, #fff 0%, #a0c4ff 100%);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.analogy { color: #60a5fa; font-size: 14px; font-style: italic; margin-bottom: 40px; }
.flow { display: flex; align-items: center; justify-content: center; gap: 0; flex: 1; }
.step {
  flex: 1; max-width: 200px;
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(60,128,237,0.3);
  border-radius: 16px; padding: 24px 18px;
  text-align: center; position: relative;
}
.step-num {
  width: 32px; height: 32px; border-radius: 50%;
  background: linear-gradient(135deg, #3C80ED, #60a5fa);
  display: inline-flex; align-items: center; justify-content: center;
  font-size: 14px; font-weight: 700; margin-bottom: 12px;
}
.step-title { font-size: 15px; font-weight: 700; margin-bottom: 8px; }
.step-desc { font-size: 12px; color: rgba(255,255,255,0.65); line-height: 1.55; }
.arrow {
  font-size: 24px; color: #38A1DD;
  padding: 0 8px; flex-shrink: 0;
}
.memo { margin-top: 24px; display: flex; align-items: center; gap: 12px; }
.memo-pill {
  background: linear-gradient(90deg, #3C80ED, #60a5fa);
  border-radius: 20px; padding: 7px 18px;
  font-size: 12px; font-weight: 700; white-space: nowrap;
}
.memo-text { font-size: 13px; color: rgba(255,255,255,0.5); }
</style></head><body>
<div class="slide">
  <h1>流程主標題</h1>
  <div class="analogy">💡 類比——讓步驟更好理解</div>
  <div class="flow">
    <div class="step">
      <div class="step-num">1</div>
      <div class="step-title">步驟一</div>
      <div class="step-desc">說明這個步驟做什麼</div>
    </div>
    <div class="arrow">→</div>
    <div class="step">
      <div class="step-num">2</div>
      <div class="step-title">步驟二</div>
      <div class="step-desc">說明這個步驟做什麼</div>
    </div>
    <div class="arrow">→</div>
    <div class="step">
      <div class="step-num">3</div>
      <div class="step-title">步驟三</div>
      <div class="step-desc">說明這個步驟做什麼</div>
    </div>
    <div class="arrow">→</div>
    <div class="step">
      <div class="step-num">4</div>
      <div class="step-title">步驟四</div>
      <div class="step-desc">說明這個步驟做什麼</div>
    </div>
  </div>
  <div class="memo">
    <div class="memo-pill">💬 一句話帶走</div>
    <div class="memo-text">流程的精髓總結</div>
  </div>
</div>
</body></html>
```

---

## 版型 C：VS 對比（左右對照）

適用：REST vs GraphQL、SQL vs NoSQL、同步 vs 異步

```html
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
.slide {
  width: 1280px; height: 720px;
  padding: 52px 64px 40px;
  box-sizing: border-box;
  display: flex; flex-direction: column;
  position: relative;
}
.slide::before {
  content: ''; position: absolute;
  top: 0; left: 0; right: 0; height: 3px;
  background: linear-gradient(90deg, #3C80ED, #60a5fa, #38A1DD);
}
h1 {
  font-size: 38px; font-weight: 900; margin: 0 0 8px 0;
  background: linear-gradient(135deg, #fff 0%, #a0c4ff 100%);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.analogy { color: #60a5fa; font-size: 14px; font-style: italic; margin-bottom: 28px; }
.vs-container { display: flex; gap: 0; align-items: stretch; flex: 1; }
.side {
  flex: 1; border-radius: 18px; padding: 28px 28px;
  position: relative;
}
.side-left { background: rgba(16,185,129,0.08); border: 1px solid rgba(16,185,129,0.3); margin-right: 16px; }
.side-right { background: rgba(239,68,68,0.08); border: 1px solid rgba(239,68,68,0.3); margin-left: 16px; }
.vs-badge {
  position: absolute; top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  width: 52px; height: 52px; border-radius: 50%;
  background: linear-gradient(135deg, #3C80ED, #60a5fa);
  display: flex; align-items: center; justify-content: center;
  font-size: 14px; font-weight: 900; z-index: 10;
  border: 3px solid #0a0a0f;
}
.side-title { font-size: 22px; font-weight: 800; margin-bottom: 20px; }
.side-left .side-title { color: #10B981; }
.side-right .side-title { color: #f87171; }
.point { display: flex; align-items: flex-start; gap: 10px; margin-bottom: 12px; }
.point-icon { font-size: 14px; margin-top: 2px; flex-shrink: 0; }
.point-text { font-size: 13px; color: rgba(255,255,255,0.8); line-height: 1.5; }
.memo { margin-top: 16px; display: flex; align-items: center; gap: 12px; }
.memo-pill {
  background: linear-gradient(90deg, #3C80ED, #60a5fa);
  border-radius: 20px; padding: 7px 18px;
  font-size: 12px; font-weight: 700; white-space: nowrap;
}
.memo-text { font-size: 13px; color: rgba(255,255,255,0.5); }
</style></head><body>
<div class="slide">
  <h1>方案 A vs 方案 B</h1>
  <div class="analogy">💡 選擇的核心是什麼？讓使用情境說話</div>
  <div class="vs-container">
    <div class="side side-left">
      <div class="side-title">✅ 方案 A</div>
      <div class="point"><span class="point-icon">✓</span><span class="point-text">優點一</span></div>
      <div class="point"><span class="point-icon">✓</span><span class="point-text">優點二</span></div>
      <div class="point"><span class="point-icon">⚠</span><span class="point-text">限制或缺點</span></div>
    </div>
    <div class="vs-badge">VS</div>
    <div class="side side-right">
      <div class="side-title">⚡ 方案 B</div>
      <div class="point"><span class="point-icon">✓</span><span class="point-text">優點一</span></div>
      <div class="point"><span class="point-icon">✓</span><span class="point-text">優點二</span></div>
      <div class="point"><span class="point-icon">⚠</span><span class="point-text">限制或缺點</span></div>
    </div>
  </div>
  <div class="memo">
    <div class="memo-pill">💬 選哪個？</div>
    <div class="memo-text">當…時選A，當…時選B</div>
  </div>
</div>
</body></html>
```

---

## 版型 D：巢狀層次圖（包含關係）

適用：OSI 模型、TCP/IP、Clean Architecture、容器 vs VM

```html
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
.slide {
  width: 1280px; height: 720px;
  padding: 52px 64px 40px;
  box-sizing: border-box;
  display: flex; flex-direction: column;
  position: relative;
}
.slide::before {
  content: ''; position: absolute;
  top: 0; left: 0; right: 0; height: 3px;
  background: linear-gradient(90deg, #3C80ED, #60a5fa, #38A1DD);
}
h1 {
  font-size: 38px; font-weight: 900; margin: 0 0 8px 0;
  background: linear-gradient(135deg, #fff 0%, #a0c4ff 100%);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.analogy { color: #60a5fa; font-size: 14px; font-style: italic; margin-bottom: 28px; }
.layers-container { display: flex; gap: 40px; align-items: center; flex: 1; }
.layers {
  flex: 1; display: flex; flex-direction: column; gap: 10px;
}
.layer {
  border-radius: 12px; padding: 16px 22px;
  display: flex; align-items: center; gap: 16px;
}
.layer:nth-child(1) { background: rgba(60,128,237,0.15); border: 1px solid rgba(60,128,237,0.4); }
.layer:nth-child(2) { background: rgba(56,161,221,0.12); border: 1px solid rgba(56,161,221,0.35); margin: 0 20px; }
.layer:nth-child(3) { background: rgba(16,185,129,0.10); border: 1px solid rgba(16,185,129,0.3); margin: 0 40px; }
.layer:nth-child(4) { background: rgba(168,85,247,0.10); border: 1px solid rgba(168,85,247,0.3); margin: 0 60px; }
.layer-name { font-size: 16px; font-weight: 700; min-width: 120px; }
.layer-desc { font-size: 12px; color: rgba(255,255,255,0.7); }
.side-note {
  width: 280px; background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 16px; padding: 24px 20px;
}
.side-note-title { font-size: 14px; font-weight: 700; color: #60a5fa; margin-bottom: 12px; }
.side-note-text { font-size: 12px; color: rgba(255,255,255,0.65); line-height: 1.6; }
.memo { margin-top: 16px; display: flex; align-items: center; gap: 12px; }
.memo-pill {
  background: linear-gradient(90deg, #3C80ED, #60a5fa);
  border-radius: 20px; padding: 7px 18px;
  font-size: 12px; font-weight: 700; white-space: nowrap;
}
.memo-text { font-size: 13px; color: rgba(255,255,255,0.5); }
</style></head><body>
<div class="slide">
  <h1>層次架構標題</h1>
  <div class="analogy">💡 就像洋蔥——每層包覆內層，外層依賴內層</div>
  <div class="layers-container">
    <div class="layers">
      <div class="layer">
        <div class="layer-name">🌐 最外層</div>
        <div class="layer-desc">說明最外層的職責</div>
      </div>
      <div class="layer">
        <div class="layer-name">⚙️ 第二層</div>
        <div class="layer-desc">說明第二層的職責</div>
      </div>
      <div class="layer">
        <div class="layer-name">🎯 第三層</div>
        <div class="layer-desc">說明第三層的職責</div>
      </div>
      <div class="layer">
        <div class="layer-name">💎 核心層</div>
        <div class="layer-desc">說明核心的職責</div>
      </div>
    </div>
    <div class="side-note">
      <div class="side-note-title">🔑 關鍵原則</div>
      <div class="side-note-text">補充說明這個層次架構的設計原則，或什麼時候會打破這個結構。</div>
    </div>
  </div>
  <div class="memo">
    <div class="memo-pill">💬 一句話帶走</div>
    <div class="memo-text">層次架構的精髓總結</div>
  </div>
</div>
</body></html>
```

---

## 版型 E：地鐵站點式時間軸（有先後順序）

適用：Git 工作流、部署流程、Scrum sprint、演化歷程

```html
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
.slide {
  width: 1280px; height: 720px;
  padding: 52px 64px 40px;
  box-sizing: border-box;
  display: flex; flex-direction: column;
  position: relative;
}
.slide::before {
  content: ''; position: absolute;
  top: 0; left: 0; right: 0; height: 3px;
  background: linear-gradient(90deg, #3C80ED, #60a5fa, #38A1DD);
}
h1 {
  font-size: 38px; font-weight: 900; margin: 0 0 8px 0;
  background: linear-gradient(135deg, #fff 0%, #a0c4ff 100%);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.analogy { color: #60a5fa; font-size: 14px; font-style: italic; margin-bottom: 32px; }
.timeline { flex: 1; display: flex; flex-direction: column; justify-content: center; position: relative; }
.track {
  position: absolute; left: 24px; right: 24px;
  top: 50%; height: 4px;
  background: linear-gradient(90deg, #3C80ED, #60a5fa);
  border-radius: 2px; transform: translateY(-50%);
}
.stations { display: flex; justify-content: space-between; position: relative; z-index: 1; }
.station { display: flex; flex-direction: column; align-items: center; width: 180px; }
.station:nth-child(odd) { flex-direction: column; }
.station:nth-child(even) { flex-direction: column-reverse; }
.station-dot {
  width: 40px; height: 40px; border-radius: 50%;
  background: linear-gradient(135deg, #3C80ED, #60a5fa);
  display: flex; align-items: center; justify-content: center;
  font-size: 16px; font-weight: 800; flex-shrink: 0;
  border: 3px solid #0a0a0f;
}
.station-card {
  background: rgba(255,255,255,0.05);
  border: 1px solid rgba(60,128,237,0.25);
  border-radius: 12px; padding: 12px 14px;
  text-align: center; margin: 10px 0;
}
.station-name { font-size: 13px; font-weight: 700; margin-bottom: 4px; }
.station-desc { font-size: 11px; color: rgba(255,255,255,0.6); line-height: 1.45; }
.memo { margin-top: 16px; display: flex; align-items: center; gap: 12px; }
.memo-pill {
  background: linear-gradient(90deg, #3C80ED, #60a5fa);
  border-radius: 20px; padding: 7px 18px;
  font-size: 12px; font-weight: 700; white-space: nowrap;
}
.memo-text { font-size: 13px; color: rgba(255,255,255,0.5); }
</style></head><body>
<div class="slide">
  <h1>流程時間軸標題</h1>
  <div class="analogy">💡 就像搭地鐵——每站都有其目的，不能跳站</div>
  <div class="timeline">
    <div class="track"></div>
    <div class="stations">
      <div class="station">
        <div class="station-card">
          <div class="station-name">站點一</div>
          <div class="station-desc">說明</div>
        </div>
        <div class="station-dot">1</div>
      </div>
      <div class="station">
        <div class="station-dot">2</div>
        <div class="station-card">
          <div class="station-name">站點二</div>
          <div class="station-desc">說明</div>
        </div>
      </div>
      <div class="station">
        <div class="station-card">
          <div class="station-name">站點三</div>
          <div class="station-desc">說明</div>
        </div>
        <div class="station-dot">3</div>
      </div>
      <div class="station">
        <div class="station-dot">4</div>
        <div class="station-card">
          <div class="station-name">站點四</div>
          <div class="station-desc">說明</div>
        </div>
      </div>
      <div class="station">
        <div class="station-card">
          <div class="station-name">站點五</div>
          <div class="station-desc">說明</div>
        </div>
        <div class="station-dot">5</div>
      </div>
    </div>
  </div>
  <div class="memo">
    <div class="memo-pill">💬 一句話帶走</div>
    <div class="memo-text">流程精髓總結</div>
  </div>
</div>
</body></html>
```

---

## 注意事項

1. **WeasyPrint 不支援 CSS flexbox 的 `-webkit-background-clip`**：文字漸層效果可能 fallback 到純色，這是正常的。可改用 `color: #ffffff` 作為 fallback。
2. **WeasyPrint 不支援 `display: flex` 中的部分屬性**：如 `gap` 在舊版可能無效，改用 `margin` 替代。
3. **字體**：WeasyPrint 使用系統字體，`Noto Sans TC` 通常已安裝在 Ubuntu 上。
4. **Emoji**：WeasyPrint 的 Emoji 支援依賴 Noto Color Emoji 字體，可能顯示為方塊或系統預設。
5. **所有尺寸**：頁面固定 1280×720px，不要使用 vh/vw 單位。
