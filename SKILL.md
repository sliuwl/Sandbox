---
name: sliu-root
description: 当用户要求创建、更新、同步或存放用户生成的脚本或 skill 时触发。用户生成的 scripts 和 skills 统一存放在 ~/Sandbox/.sliu_skills。
---

# Sliu Root Skill

- Unless the user explicitly requests it, never automatically update this root skill file `~/Sandbox/SKILL.md`.
- Store user-generated scripts and skills under `~/Sandbox/.sliu_skills`.

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
2. Use existing scripts in `~/Sandbox/.sliu_skills/scripts/` when possible
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