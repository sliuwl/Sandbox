---
name: sliu-root
description: 当用户要求创建、更新、同步或存放用户生成的脚本或 skill 时触发。用户生成的 scripts 和 skills 统一存放在 ~/Sandbox/.sliu_skills。
---

# Sliu Root Skill

- Unless the user explicitly requests it, never automatically update this root skill file `~/Sandbox/SKILL.md`.
- Store user-generated scripts and skills under `~/Sandbox/.sliu_skills`.

## 2. Standard Workflow

Whenever you receive an instruction to "do a task," follow the steps below in this exact order.

**Step 0: Preliminary Check (Must Be Done First)**

If the user request involves generating input files or writing submission scripts, first check whether `references/*.md` already documents a corresponding public entry point. If it is documented, continue. If not, inform the user that "the current skill has not yet consolidated this scenario," and proceed only if the user explicitly asks to update the skill content.

**Step 1: Receive the Instruction**

Parse only the user's explicit literal instruction; do not infer hidden intent. If the instruction is incomplete and prevents script execution due to missing input files, directories, or parameters, ask only the minimum clarification questions required before proceeding.

**Step 2: Make a Plan**

Output a short plan of 1–4 steps, with each step corresponding to one executable action. The plan must clearly specify: the task type, which script(s) or lightweight bash command(s) will be called, what the input is, and where the output will go.

If the task involves generating input files or writing submission scripts, the plan must also specify: which consolidated entry point will be used, which inputs the user is allowed to modify, and where the final files will be written.

If the task involves report writing, the plan must also specify: which data, figures, or scripts will be referenced, where the report will be written, and whether figures need to be copied or redrawn into report/figures/.

If the task involves "new presentation data" and requires adding scripts, the plan must also specify: the save path of the script (within the working directory), the script filename, the command to be executed, and the expected outputs.

**Step 3: Execute**

Only execute the actions explicitly listed in the plan; do not perform additional "helpful" optimizations, cleanup, renaming, or archiving.

Before running any script, first run it once with `--help` (for shell scripts, use `bash <script> --help`) to confirm parameters, and then execute it formally.

If the task involves generating input files or writing submission scripts, prefer reusing consolidated templates or public scripts; do not improvise a new unregistered specification outside thereferences.

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
1. Check `~/Sandbox/.sliu_skills/references/` for relevant documentation
2. **Prefer reusing existing scripts first**: By default, use the existing scripts in `~/Sandbox/.sliu_skills/scripts/` to complete the task. Do not turn temporary scripts in the working directory into stable entry points for the skill.
3. Only write new scripts when existing ones cannot accomplish the task
4. Write new scripts primarily in Python; use Bash only when necessary

## Important: Analyzing QE Optimized Structures

When asked to analyze or extract optimized structures from QE output files:
- **Always use the scripts** in `~/Sandbox/.sliu_skills/scripts/`:
  1. `qe_out_to_vasp.py` - Extract last structure from QE output → VASP format
  2. `find_sym.py` - Analyze symmetry (space group, lattice parameters)

Do NOT manually parseQE output with grep/sed for structure extraction.

Example workflow:
```bash
# Step 1: Extract VASP from QE output
python3 ~/Sandbox/.sliu_skills/scripts/qe_out_to_vasp.py qe.out -o structure.vasp

# Step 2: Analyze symmetry
python3 ~/Sandbox/.sliu_skills/scripts/find_sym.py structure.vasp -k conventional
```

See `~/Sandbox/.sliu_skills/references/scripts.md` for details.