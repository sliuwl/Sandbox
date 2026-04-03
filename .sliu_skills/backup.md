---
name: backup-skill
description: 当用户说"backup SKILL.md"或"备份技能"时，备份 SKILL.md 和 .sliu_skills 到远程 Git 仓库
trigger: 备份 SKILL.md
---

# Backup Skill

When user says "backup SKILL.md" or "备份", automatically backup `~/Sandbox/SKILL.md` and `~/Sandbox/.sliu_skills/` to remote Git repository.

Steps:
1. cd to /Users/sliutheory/Sandbox
2. git add SKILL.md .sliu_skills/
3. git commit -m "Backup $(date +'%Y-%m-%d %H:%M')"
4. git push
