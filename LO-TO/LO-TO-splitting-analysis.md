# LO-TO Splitting Analysis for PbTiO₃

## What is LO-TO Splitting?

In polar crystals like PbTiO₃, the long-range Coulomb interaction creates a macroscopic electric field for **longitudinal optic (LO)** vibrational modes. This field raises the frequency of LO modes relative to their **transverse optic (TO)** counterparts, where the electric displacement is perpendicular to the wave vector.

The frequency difference between LO and TO modes is called **LO-TO splitting**.

This splitting is a direct consequence of:
- The **Born effective charges** (Z*) — how ions respond to electric fields
- The **dielectric permittivity** (ε₀, ε∞)

## Relationship Between Wave Vector and LO/TO Modes

The key principle is:

> **The classification of a phonon as LO or TO depends on the relative direction between the vibration eigenvector (atomic displacement) and the wave vector q.**

- If the atomic displacement is **parallel** to q → **LO mode**
- If the atomic displacement is **perpendicular** to q → **TO mode**

At the Γ point (q = 0), we must specify a **direction** to define the electric field. This is done via the `loto_acoustic` and `sigma` parameters in Quantum ESPRESSO:
- `sigma = 0` → polarization along **z-direction**
- `sigma = 1` → polarization along **x-direction**

## Why These Three Calculations Study Anisotropy

The three folders contain:

| Folder | Input Setting | Polarization Direction | Description |
|--------|---------------|------------------------|-------------|
| `000` | No `loto_acoustic` | None | Pure transverse optic (TO) modes — no LO-TO splitting applied |
| `001` | `loto_acoustic='true'`, `sigma=0` | z | LO-TO splitting for **z-polarized** modes |
| `100` | `loto_acoustic='true'`, `sigma=1` | x | LO-TO splitting for **x-polarized** modes |

By comparing:
- `000` vs `001` → LO-TO splitting in the **z-direction**
- `000` vs `100` → LO-TO splitting in the **x-direction**

This reveals the **anisotropy** of LO-TO splitting — how the splitting magnitude depends on the polarization direction in this tetragonal crystal (PbTiO₃ has polarization along z in its ferroelectric phase).

---

## Z-Polarization: 000 (TO) vs 001 (LO-z)

| 000 Mode | TO freq (cm⁻¹) | 001 Mode | LO freq (cm⁻¹) | Δ (LO-TO Splitting) |
|----------|----------------|----------|----------------|---------------------|
| 1-3 | ~0 (acoustic) | 1-3 | ~0 | 0 |
| 4-5 | 89.73 | 4-5 | 89.73 | 0 (soft TA mode, not z-pol) |
| **6** | **152.90** | **6** | **195.23** | **+42.33** |
| 7-8 | 209.19 | 7-8 | 209.19 | 0 |
| 9-10 | 274.53 | 9-10 | 274.53 | 0 |
| 11 | 275.99 | 11 | 275.99 | 0 (not IR active) |
| **12** | **360.70** | **12** | **445.72** | **+85.02** |
| 13-14 | 498.60 | 13-14 | 498.60 | 0 |
| **15** | **667.25** | **15** | **797.40** | **+130.15** |

### Z-Polarization Summary

| Mode Character | TO (cm⁻¹) | LO (cm⁻¹) | Splitting Δ (cm⁻¹) |
|----------------|-----------|-----------|---------------------|
| Soft E(1) mode (Ti-O) | 152.90 | 195.23 | **+42.33** |
| Mid-frequency O | 360.70 | 445.72 | **+85.02** |
| High-frequency O | 667.25 | 797.40 | **+130.15** |

---

## X-Polarization: 000 (TO) vs 100 (LO-x)

| 000 Mode | TO freq (cm⁻¹) | 100 Mode | LO freq (cm⁻¹) | Δ (LO-TO Splitting) |
|----------|----------------|----------|----------------|---------------------|
| 1-3 | ~0 (acoustic) | 1-3 | ~0 | 0 |
| 4-5 | 89.73 | 4 | 89.73 | 0 |
| — | — | **5** | **119.82** | **(from 89.73) +30.09** |
| 6 | 152.90 | 6 | 152.90 | 0 |
| 7-8 | 209.19 | 7 | 209.19 | 0 |
| — | — | **8** | **274.01** | **(from 209.19) +64.82** |
| 9-10 | 274.53 | 9 | 274.53 | 0 |
| 11 | 275.99 | 10 | 275.99 | 0 |
| 12 | 360.70 | **11** | **360.70** | 0 |
| — | — | **12** | **417.24** | **(from 360.70) +56.54** |
| 13-14 | 498.60 | 13 | 498.60 | 0 |
| 15 | 667.25 | 14-15 | 667.25 / 671.99 | +4.74 |

### X-Polarization Summary

| Mode Character | TO (cm⁻¹) | LO (cm⁻¹) | Splitting Δ (cm⁻¹) |
|----------------|-----------|-----------|---------------------|
| Soft A mode | 89.73 | 119.82 | **+30.09** |
| E(2) mode | 209.19 | 274.01 | **+64.82** |
| Mid-frequency O | 360.70 | 417.24 | **+56.54** |
| High-frequency O | 667.25 | 671.99 | +4.74 |

---

## Anisotropic LO-TO Splitting Summary

| Mode Character | TO (cm⁻¹) | LO-z (001) Δz | LO-x (100) Δx |
|----------------|-----------|---------------|---------------|
| Soft mode (~90 cm⁻¹) | 89.73 | 0 | **+30.09** |
| Soft E(1) mode (Ti-O) | 152.90 | **+42.33** | 0 |
| E(2) mode | 209.19 | 0 | **+64.82** |
| Mid-frequency O | 360.70 | **+85.02** | +56.54 |
| High-frequency O | 667.25 | **+130.15** | +4.74 |

---

## Key Findings

1. **Different modes split in different directions**: The 152.90 cm⁻¹ E(1) soft mode shows strong LO-TO splitting in the z-direction (+42.33 cm⁻¹) but **no splitting** in the x-direction. Conversely, the ~90 cm⁻¹ soft mode splits in x but not in z.

2. **Anisotropy reflects crystal symmetry**: PbTiO₃ has tetragonal symmetry with spontaneous polarization along z. This creates different long-range Coulomb interactions depending on the polarization direction.

3. **Physical implications**: The LO-TO splitting anisotropy is directly related to:
   - The dielectric tensor (ε_xx = 31.32, ε_zz = 28.52 from the output)
   - The Born effective charges along different crystallographic directions
   - The Lyddane-Sachs-Teller relationship: ω_LO² / ω_TO² = ε₀ / ε∞

---

## Input Files Summary

**000/dyn.in** (pure TO):
```bash
PTO phonon
&input
 fildyn='pto.gamma.dyn'
 asr='simple',
 q(1)=0.d0, q(2)=0.d0, q(3)=0.d0
/
```

**001/dyn.in** (LO-TO z-polarization):
```bash
PTO phonon
&input
 fildyn='pto.gamma.dyn'
 asr='simple',
 loto_acoustic='true',
 sigma(0)=1,
 q(1)=0.d0, q(2)=0.d0, q(3)=0.d0
/
```

**100/dyn.in** (LO-TO x-polarization):
```bash
PTO phonon
&input
 fildyn='pto.gamma.dyn'
 asr='simple',
 loto_acoustic='true',
 sigma(1)=1,
 q(1)=0.d0, q(2)=0.d0, q(3)=0.d0
/
```