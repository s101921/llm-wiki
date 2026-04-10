---
title: "LLM Wiki — Karpathy"
date: 2026-04-08
updated: 2026-04-08
type: summary
tags: [知識管理, LLM, PKM]
source_type: article
source_url: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
source_file: "[[Clippings/llm-wiki]]"
sources: 1
status: stable
---

# LLM Wiki — Andrej Karpathy

**來源類型：** 文章（GitHub Gist）
**作者：** Andrej Karpathy
**發布日期：** 2026 年初
**原始檔案：** [[Clippings/llm-wiki]]

---

## 核心主張

與其用 RAG 在每次查詢時重新從原始文件拼湊答案，不如讓 LLM 持續維護一個結構化 wiki。Wiki 是知識的「編譯版本」，隨每次新素材加入而更新，查詢時直接讀取，不需重新推導。

## 重點摘錄

- **RAG 的根本限制**：每次問問題都重新發現知識，沒有累積，無法處理需跨越多份文件綜合的問題
- **Wiki 是複利產物**：交叉引用、矛盾標記、綜合觀點都已預先建好
- **分工**：你負責策展（sourcing）與提問；LLM 負責所有書目整理工作
- **index.md**：以內容為主的目錄，LLM 查詢時先讀這裡找相關頁面
- **log.md**：只增不減的時間軸，記錄每次 ingest / query / lint
- **Schema 共同演化**：CLAUDE.md 隨使用習慣調整，不是一次性設定

## 對 Wiki 的影響

- 建立了 [[wiki/concepts/llm-wiki-pattern]] — 核心概念頁

## 教學應用價值

- 適合在「AI 與知識管理」單元引用，說明 LLM 不只是問答工具，也能成為個人知識庫的維護者
- 本 Vault 的整體架構即基於此文設計，可直接作為示範案例
