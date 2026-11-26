#!/usr/bin/env bash
# Full sync for the 2026Teaching/Book folder.
#
# Stages every change inside this folder (new, modified, and deleted files),
# commits it, and pushes to origin/master.  Reference textbook folders listed
# in .gitignore are skipped automatically.
#
# Usage:
#   ./sync.sh                 # default commit message with timestamp
#   ./sync.sh "my message"    # custom commit message

set -euo pipefail

cd "$(dirname "$0")"

# Scope to this folder only; do not touch unrelated parts of the repository.
git add -A -- .

if git diff --cached --quiet; then
    echo "没有需要同步的改动。"
    exit 0
fi

message="${1:-Sync book $(date '+%Y-%m-%d %H:%M')}"
git commit -m "$message"
git push origin master

echo "已同步：$(git log -1 --oneline)"
