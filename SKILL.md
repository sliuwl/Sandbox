---
name: sliu-root
description: 当用户要求创建、更新、同步或存放用户生成的脚本或 skill 时触发。用户生成的 scripts 和 skills 统一存放在 ~/Sandbox/.sliu_skills。
---

# Sliu Root Skill

- Unless the user explicitly requests it, never automatically update this root skill file `~/Sandbox/SKILL.md`.
- Store user-generated scripts and skills under `~/Sandbox/.sliu_skills`.
- Put scripts in `~/Sandbox/.sliu_skills/scripts/`.
- Put reference docs in `~/Sandbox/.sliu_skills/references/` when needed.
- For related tasks, first check `~/Sandbox/.sliu_skills/references/scripts.md`, then prefer using scripts in `~/Sandbox/.sliu_skills/scripts/`.
- Only when the task cannot be achieved with the documented scripts should new scripts be written, mainly in Python with some bash only when needed.
