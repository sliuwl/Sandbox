---
name: update-skill
description: 当用户说"update skill"、"update repo"、"pull latest"、"get latest version from repo"或"更新技能"时，先保护本地 skill 改动，再从远程 Git 仓库获取并快进更新 ~/Sandbox
trigger: update skill, update repo, pull latest, get latest version, sync repo, 更新技能, 拉取最新, 获取最新版本
---

# Update Skill

When user says "update skill", "update repo", "pull latest", or "更新技能", update `~/Sandbox` from the remote Git repository with a fast-forward pull.

## Steps

1. `cd /Users/sliutheory/Sandbox`
2. Check current repository state:
   ```bash
   git status --short --branch
   ```
3. Check whether `SKILL.md` or `.sliu_skills/` has local changes:
   ```bash
   git status --short SKILL.md .sliu_skills/
   ```
4. If `SKILL.md` or `.sliu_skills/` is modified, backup them first:
   ```bash
   git add SKILL.md .sliu_skills/
   git commit -m "Backup $(date +'%Y-%m-%d %H:%M')"
   git push
   ```
5. Fetch the latest remote state:
   ```bash
   git fetch origin
   ```
6. Fast-forward local `master` only:
   ```bash
   git pull --ff-only origin master
   ```

## Rules

- Do not use `git pull` without `--ff-only`.
- Do not auto-stash, reset, or discard user changes.
- If the pull fails because local changes would be overwritten, stop and report the exact Git error.
- If the branch cannot be fast-forwarded, stop and report the exact Git error.
- Report which commit was updated from and to when Git prints it.
