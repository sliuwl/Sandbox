---
name: sliu-root
description: 当用户在 ~/Sandbox 或其任意子目录中执行任务，尤其是创建、更新、同步、解析、转换、生成输入文件、写脚本或复用工作流时触发。优先检查并复用 ~/Sandbox/.sliu_skills 中已有的 skills、references 和 scripts；用户生成的 scripts 和 skills 统一存放在 ~/Sandbox/.sliu_skills。
---

# Sliu Root Skill

- Unless the user explicitly requests it, never automatically update this root skill file `~/Sandbox/SKILL.md`.
- Store user-generated scripts and skills under `~/Sandbox/.sliu_skills`.

## Scope

- This root skill applies to the entire workspace under `~/Sandbox`, not only the root directory itself.
- Even when the task starts inside a nested subdirectory, first treat `~/Sandbox` as the workspace root and check the shared skill resources under `~/Sandbox/.sliu_skills/`.
- Do not assume that being inside another directory means ad hoc commands should be preferred. Existing skills, references, and scripts still have priority.

## Priority Rule

For all tasks anywhere under `~/Sandbox`, use the following priority order:

1. Existing system or workspace skills that already match the task
2. Existing documented entry points in `~/Sandbox/.sliu_skills/references/`
3. Existing reusable scripts in `~/Sandbox/.sliu_skills/scripts/`
4. Existing local project scripts in the current working subtree
5. New scripts or one-off logic only when the above do not cover the task

This means:

- Prefer available skills before manual exploration.
- Prefer existing scripts before writing new scripts.
- Prefer materialized scripts before one-off `python -c`, `awk`, or `sed` logic when the task is nontrivial or likely to recur.
- If a task involves parsing program output, structure extraction, symmetry analysis, input generation, plotting, or report generation, first check whether an existing skill or script already handles it.

## Backup Principle

When user requests "backup", always backup **both** `SKILL.md` and `.sliu_skills/` directory:
```bash
git add SKILL.md .sliu_skills/
git commit -m "Backup $(date +'%Y-%m-%d %H:%M')"
git push
```

This ensures the root skill file and all skill scripts/documentation are synchronized to the remote repository.

## 2. Standard Workflow

Whenever you receive an instruction to "do a task," follow the steps below in this exact order.

**Step 0: Preliminary Check (Must Be Done First)**

First determine whether the task matches an available system skill, workspace skill, or documented script workflow. If the user request involves generating input files, writing submission scripts, parsing outputs, extracting structures, plotting, or writing reports, first check whether `references/*.md` already documents a corresponding public entry point. If it is documented, continue. If not, inform the user that "the current skill has not yet consolidated this scenario," and proceed only if the user explicitly asks to update the skill content.

**Step 1: Receive the Instruction**

Parse only the user's explicit literal instruction; do not infer hidden intent. If the instruction is incomplete and prevents script execution due to missing input files, directories, or parameters, ask only the minimum clarification questions required before proceeding.

**Step 2: Make a Plan**

Output a short plan of 1–4 steps, with each step corresponding to one executable action. The plan must clearly specify: the task type, which script(s) or lightweight bash command(s) will be called, what the input is, and where the output will go.

If no existing skill or script will be used, the plan must explicitly justify why reuse is not possible.

If the task involves generating input files or writing submission scripts, the plan must also specify: which consolidated entry point will be used, which inputs the user is allowed to modify, and where the final files will be written.

If the task involves report writing, the plan must also specify: which data, figures, or scripts will be referenced, where the report will be written, and whether figures need to be copied or redrawn into report/figures/.

If the task involves "new presentation data" and requires adding scripts, the plan must also specify: the save path of the script (within the working directory), the script filename, the command to be executed, and the expected outputs.

**Step 3: Execute**

Only execute the actions explicitly listed in the plan; do not perform additional "helpful" optimizations, cleanup, renaming, or archiving.

Before running any script, first run it once with `--help` (for shell scripts, use `bash <script> --help`) to confirm parameters, and then execute it formally.

If the task involves generating input files or writing submission scripts, prefer reusing consolidated templates or public scripts; do not improvise a new unregistered specification outside the references.

If the task starts in a nested directory, still check `~/Sandbox/.sliu_skills/scripts/` and `~/Sandbox/.sliu_skills/references/` before falling back to local one-off commands.

When additional scripting is required, first save the script into the actual working directory, then run it; do not inline large blocks of logic directly in the command line.

Do not generate final presentation data directly with one-off `awk`, `sed`, or `python -c` commands; such logic must be materialized as a script file.

**Step 4: Error Handling Discipline**

If any script or command fails:

- Stop all subsequent steps immediately
- Output the complete error message exactly as is
- You may retry only once, and only by adjusting input parameters, paths, or wildcards (modifying script code is forbidden)
- If it still fails, exit directly (do not continue trying)

**Step 5: Minimal Report**

Report only: which commands were executed, which files were created or modified, and whether the task succeeded or failed. Do not provide unsolicited explanations or suggestions about physics, algorithms, or potential functions.

Example format:
```
User request: <brief>
Script(s) called: <script name or bash command>
Working path: <directory>
Result: <success/failure> - <one-paragraph summary>
```

## Organizational Principle

### Scripts → `~/Sandbox/.sliu_skills/scripts/`

Executable scripts (Python, Bash, etc.) go here:
- Utility scripts for data processing
- Wrapper scripts for external software
- Plotting and visualization scripts

### Skill Documentation → `~/Sandbox/.sliu_skills/references/`

Detailed documentation for specific workflows or tools:
- Each major topic gets its own markdown file (e.g., `QE.md`, `VASP.md`)
- Include parameter explanations, usage examples, and troubleshooting
- Reference the scripts in `scripts/` folder

## Directory Structure

```
.sliu_skills/
├── backup.md              # Special skills (e.g., backup workflow)
└── references/
    ├── QE.md              # Quantum Espresso phonon workflow
    ├── VASP.md            # VASP-related workflows
    ├── scripts.md         # General script utilities
    └── ...
└── scripts/
    ├── plot_phonon.py     # QE phonon plotting
    ├── parse_phonon.py    # QE phonon output parser
    ├── split_modes.py     # Phonon mode visualization
    └── ...
```

## How to Organize New Skills

**For code-related skills** (e.g., software workflows like QE, VASP):
1. Create/update a reference markdown file in `references/` (e.g., `software.md`)
2. Document the workflow, parameters, and usage
3. Put helper scripts in `scripts/`
4. Reference scripts from the documentation

**For utility skills** (e.g., file conversion, backup):
1. Create a simple skill markdown file at root level if standalone
2. Or integrate into existing reference file

## Usage Pattern

When working on a task:
1. Check whether an available system skill already matches the task
2. Check `~/Sandbox/.sliu_skills/references/` for relevant documentation
3. **Prefer reusing existing scripts first**: By default, use the existing scripts in `~/Sandbox/.sliu_skills/scripts/` to complete the task. Do not turn temporary scripts in the working directory into stable entry points for the skill.
4. If the current project subtree already has a reusable local script, prefer that over new one-off logic
5. Only write new scripts when existing skills and scripts cannot accomplish the task
6. Write new scripts primarily in Python; use Bash only when necessary

## Subdirectory Rule

When the task is inside any subdirectory of `~/Sandbox`:

- Do not treat the subdirectory as isolated from the workspace skill system.
- First look upward to the workspace root and reuse root-level skill resources.
- If both a root-level reusable script and a local script exist, choose the one that is already the established public entry point for the workflow.
- If you decide not to use an available script or skill, state the reason explicitly in the working notes or user update.

For software-specific workflows (e.g., QE, VASP), see the corresponding reference file in `~/Sandbox/.sliu_skills/references/`.
