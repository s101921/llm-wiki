---
title: Claude Skills 健檢 SOP
date: 2026-04-10
updated: 2026-04-10
type: ai-workflow
status: draft
tags: [Claude Code, Skills, AI 工具管理, Harnessing, SOP]
sources: 0
---

# Claude Skills 健檢 SOP

**裝了大量 Skill，Claude 卻沒變聰明——問題不是模型，是工具系統設計錯了。**

---

## 為什麼 Skill 多不等於 Claude 更聰明

Skills 是觸發式的指令注入：Claude 根據你說的話，比對所有 Skill 的 description，決定要不要啟用。

問題在這裡：

| 狀況 | 結果 |
|------|------|
| Description 太模糊 | 永遠不觸發，形同虛設 |
| 兩個 Skill 描述重疊 | 觸發哪個是隨機的，行為不可預測 |
| 太多 Skill 同時存在 | 每次對話都帶著大量無關指令，稀釋注意力 |

這對應到 Harnessing Engineering 的核心原則：**工具太少限制能力；工具太多模型會亂用**。

---

## 健檢 SOP

定期對現有所有 Skill 執行以下審查：

```
幫我審查目前所有的 Skills，找出：
1. 功能重複的（兩個在做同一件事，或超過 70% 相似）
2. Description 太模糊、可能不會觸發的
3. 有衝突的（兩個 Skill 的指令互相矛盾）
4. 很久沒用到、可以考慮刪掉的
每個問題列出來，告訴我哪個留、哪個刪、哪個要改。
```

建議頻率：每次新增 3 個以上 Skill 後，或每個月至少一次。

---

## 四個問題的判斷邏輯

### 1. 功能重複（>70% 相似）
- 問自己：如果只保留其中一個，另一個的場景還能被覆蓋嗎？
- 能覆蓋 → 刪掉重複的那個
- 不能覆蓋 → 合併成一個，Description 列出所有觸發場景

### 2. Description 太模糊
壞的 Description：「幫助我完成各種任務」
好的 Description：「當我要建立 Marp 投影片、或要把知識整理成簡報格式時」

Description 的測試方法：把它唸一遍，想像這句話出現在 10 個不同對話場景裡，有幾個場景它應該觸發？少於 2 個 → 太模糊。

### 3. 有衝突
- 常見衝突：一個要求「簡短回應」、另一個要求「詳細說明」
- 兩個都留 → 看哪個觸發取決於運氣

### 4. 很久沒用
沒有使用記錄的 Skill = 可能永遠不會被正確觸發。先停用，觀察一個月。

---

## 核心設計原則

> **Skill 設的精準 >> 數量多**

每個 Skill 應該只做一件事，Description 應該只在你真的需要的場景觸發。

---

## 與其他概念的關係

- [[wiki/ai-workflow/harnessing-engineering]] — Skill 管理是「層 2：工具系統」的實踐（工具太多模型會亂用）
- [[wiki/concepts/ai-agent]] — Skills 是 Claude 工具呼叫能力的一種擴充方式

