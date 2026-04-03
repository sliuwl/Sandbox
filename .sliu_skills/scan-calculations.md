---
name: scan-calculations
description: Create parameter scan folders from a template - replaces placeholder values (e.g., HOLEVALUE) in template files with actual values in a loop
trigger: scan calculation, parameter scan, create folders from template, scan job, 批量计算
---

# Parameter Scan Calculations

Create multiple calculation folders from a template, replacing placeholder values.

## Directory Structure

```
ProjectName/
├── template/
│   ├── vc-relax.in-t     # Template with PLACEHOLDER (e.g., HOLEVALUE)
│   ├── gpu_qe_sai.sbatch
│   └── psps/
├── create_folders.sh     # Script to generate folders
└── 0.Xh/                 # Generated folders
    ├── vc-relax.in       # Replaced with actual value
    ├── gpu_qe_sai.sbatch
    ├── psps/
    └── tmp/
```

## Creating the Template

1. Create `template/` folder with input files
2. Use placeholder in input file (e.g., `HOLEVALUE`, `TEMPVALUE`)
3. Name template file with `-t` suffix (e.g., `vc-relax.in-t`)

Example in vc-relax.in-t:
```bash
tot_charge     = HOLEVALUE           ! HOLEVALUE hole per unit cell
```

## Bash Script Template

Create `create_folders.sh`:

```bash
#!/bin/bash
# Create folders from template and replace HOLEVALUE with actual values

# Parameters to scan
values=(0.6 0.8 1.0)

base_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
template_dir="$base_dir/template"

for v in "${values[@]}"; do
    folder_name="${v}h"
    new_dir="$base_dir/$folder_name"

    # IMPORTANT: Delete existing folder first to avoid nested directories
    rm -rf "$new_dir"

    # Create directory and copy template
    mkdir -p "$new_dir"
    cp -r "$template_dir/"* "$new_dir/"

    # Create tmp directory
    mkdir -p "$new_dir/tmp"

    # Replace placeholder and save as vc-relax.in
    sed "s/HOLEVALUE/$v/g" "$new_dir/vc-relax.in-t" > "$new_dir/vc-relax.in"

    echo "Created $folder_name"
done

echo "Done! Created ${#values[@]} folders"
```

**Important**: Always delete the target folder with `rm -rf` before copying the template. Otherwise, files will be nested inside the existing folder, causing issues.

## Running

```bash
cd /Users/sliutheory/Sandbox/ProjectName
chmod +x create_folders.sh
./create_folders.sh
```

## Submitting Jobs

After creating folders, submit jobs:

```bash
# Submit all jobs
for folder in 0.6h 0.8h 1.0h; do
    ssh sai "cd ProjectName/$folder && mkdir -p tmp/ && sbatch gpu_qe_sai.sbatch"
done

# Check status
ssh sai "squeue -u $USER"
```

## Customization

Change values in the script:
- `values=(0.6 0.8 1.0)` → your actual values
- `"${v}h"` → your folder naming pattern (can use `${v}p` for positive, etc.)
- `sed "s/HOLEVALUE/$v/g"` → replace HOLEVALUE with your placeholder name