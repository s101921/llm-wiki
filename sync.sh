#!/bin/bash
# sync.sh — 把 Obsidian Vault 的 wiki 內容同步到 Quartz，並推送到 GitHub

VAULT="/Users/warren/Library/CloudStorage/GoogleDrive-s101921@gmail.com/我的雲端硬碟/LLM Wiki"
CONTENT="$(dirname "$0")/content"

echo "🔄 同步 Vault → content/"
rsync -av --delete \
  --exclude='.obsidian' \
  --exclude='.DS_Store' \
  --exclude='raw/' \
  --exclude='Templates/' \
  --exclude='CLAUDE.md' \
  "$VAULT/" "$CONTENT/"

echo "📦 推送到 GitHub..."
cd "$(dirname "$0")"
git add content/
git commit -m "sync: $(date '+%Y-%m-%d %H:%M')" || echo "沒有變更"
git push origin v4

echo "✅ 完成！網站約 1 分鐘後更新：https://s101921.github.io/llm-wiki"
