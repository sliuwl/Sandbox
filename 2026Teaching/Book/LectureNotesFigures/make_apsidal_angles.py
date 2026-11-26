"""Illustrate the apsidal angle, the pericenter-to-pericenter advance, and precession.

Panel (a): a precessing near-circular orbit for the power law F = -k/r (n = -1),
           integrated exactly from the Binet equation.  The pericenters and
           apocenters are marked, and the three angles are drawn as arcs about
           the force center.

Panel (b): the same angle bookkeeping laid out on a linear ruler, for the
           inverse-square case n = -2 (no precession, orbit closes) and for
           n = -1 (backward precession).

Near-circular power-law results used for the annotations:

    Delta theta_apse       = pi / sqrt(n + 3)
    Delta theta_peri->peri = 2 pi / sqrt(n + 3)
    Delta theta_prec       = 2 pi / sqrt(n + 3) - 2 pi
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Arc, Patch, Rectangle, Wedge
from scipy.integrate import solve_ivp

# ---------------------------------------------------------------------------
# Panel (a): exact orbit for F = -k/r, n = -1
# ---------------------------------------------------------------------------
n = -1.0
alpha = np.sqrt(n + 3.0)                 # omega_r / omega_theta

r0 = 1.0                                 # radius of the circular orbit
rmin = 0.82                              # pericenter of the drawn orbit

uc = 1.0 / r0
A = uc ** (n + 3.0)                      # circular-orbit constant, mk/l^2


def binet(theta, y):
    u, up = y
    return [up, -u + A * u ** (-(n + 2.0))]


theta_end = 4.0 * 2.0 * np.pi / alpha
theta = np.linspace(0.0, theta_end, 4000)
sol = solve_ivp(
    binet,
    (0.0, theta_end),
    [1.0 / rmin, 0.0],
    t_eval=theta,
    rtol=1.0e-12,
    atol=1.0e-14,
    method="DOP853",
)
r = 1.0 / sol.y[0]
x = r * np.cos(theta)
y = r * np.sin(theta)

# Turning points of the radial motion.  u' starts at zero (the draw begins at a
# pericenter), so discard the first, spurious sign change at theta = 0; the
# remaining ones alternate apocenter, pericenter, apocenter, ...
idx = np.where(np.diff(np.sign(sol.y[1])) != 0)[0]
theta_turn = theta[idx]
theta_turn = theta_turn[theta_turn > 1.0e-6]
theta_apo = theta_turn[0::2]
theta_peri = np.concatenate(([0.0], theta_turn[1::2]))

r_peri = np.interp(theta_peri, theta, r)
r_apo = np.interp(theta_apo, theta, r)

# Angles from the exact integration (for the caption / console check)
apse_exact = theta_apo[0] - theta_peri[0]
periperi_exact = theta_peri[1] - theta_peri[0]
print(f"exact  apse = {apse_exact:.4f} rad ({np.degrees(apse_exact):.2f} deg)")
print(f"exact  peri-peri = {periperi_exact:.4f} rad "
      f"({np.degrees(periperi_exact):.2f} deg)")
print(f"formula apse = {np.pi/alpha:.4f} rad ({np.degrees(np.pi/alpha):.2f} deg)")
print(f"formula peri-peri = {2*np.pi/alpha:.4f} rad "
      f"({np.degrees(2*np.pi/alpha):.2f} deg)")

T_apse = np.pi / alpha                   # formula values used in the labels
T_peri = 2.0 * np.pi / alpha
T_prec = T_peri - 2.0 * np.pi

# ---------------------------------------------------------------------------
# Style
# ---------------------------------------------------------------------------
BLUE = "#3a78b5"
DARKBLUE = "#1f4e79"
ORANGE = "#e07b24"
GREEN = "#2f9e44"
GRAY = "#9a9a9a"
LIGHT = "#d9d9d9"
DARK = "#222222"

plt.rcParams.update(
    {
        "font.family": "serif",
        "mathtext.fontset": "dejavuserif",
        "font.size": 12,
        "axes.linewidth": 0.0,
        "figure.facecolor": "white",
        "savefig.facecolor": "white",
    }
)

fig, (axa, axb) = plt.subplots(
    1,
    2,
    figsize=(13.8, 6.1),
    gridspec_kw={"width_ratios": [1.0, 1.20]},
)

# ---------------------------------------------------------------------------
# Panel (a)
# ---------------------------------------------------------------------------
axa.set_aspect("equal", adjustable="box")

# The whole orbit, then the first radial cycle emphasised
axa.plot(x, y, color=BLUE, lw=1.9, alpha=0.5, zorder=2, solid_capstyle="round")
first = theta <= theta_peri[1]
axa.plot(x[first], y[first], color=DARKBLUE, lw=2.8, zorder=3)

# Rays from the force center to the first pericenter, first apocenter and
# second pericenter
for th, rr in ((theta_peri[0], r_peri[0]), (theta_apo[0], r_apo[0]),
               (theta_peri[1], r_peri[1])):
    axa.plot([0.0, rr * np.cos(th)], [0.0, rr * np.sin(th)],
             color=DARK, lw=0.9, ls=(0, (4, 4)), zorder=1)

# Markers
axa.plot(r_peri * np.cos(theta_peri), r_peri * np.sin(theta_peri), "o",
         ms=7.5, color=DARKBLUE, mec="white", mew=1.3, zorder=6)
axa.plot(r_apo * np.cos(theta_apo), r_apo * np.sin(theta_apo), "o",
         ms=7.0, mfc="white", mec=GREEN, mew=1.8, zorder=6)

# Force center
axa.plot(0.0, 0.0, "o", ms=6.5, color=DARK, mec="white", mew=1.3, zorder=7)

# Angle arcs about the force center.  They live well inside the pericenter
# radius (0.82), so they cannot touch the orbit itself.
R_apse, R_peri, R_wedge = 0.30, 0.47, 0.62
axa.add_patch(Arc((0, 0), 2 * R_apse, 2 * R_apse,
                  theta1=0.0, theta2=np.degrees(T_apse),
                  color=GREEN, lw=3.0, zorder=5))
axa.add_patch(Arc((0, 0), 2 * R_peri, 2 * R_peri,
                  theta1=0.0, theta2=np.degrees(T_peri),
                  color=DARKBLUE, lw=3.0, zorder=5))

# Precession wedge: from the second pericenter back to the original ray
axa.add_patch(Wedge((0, 0), R_wedge, np.degrees(T_peri), 360.0, width=0.09,
                    facecolor=ORANGE, alpha=0.55, edgecolor="none", zorder=4))
axa.annotate("", xy=(R_wedge * np.cos(np.radians(357)),
                     R_wedge * np.sin(np.radians(357))),
             xytext=(R_wedge * np.cos(np.radians(300)),
                     R_wedge * np.sin(np.radians(300))),
             arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.6,
                             connectionstyle="arc3,rad=0.30"), zorder=6)

# Small radial tick marks at theta = 0 and at the second pericenter
for th in (theta_peri[0], theta_peri[1]):
    axa.plot([R_peri * np.cos(th), R_wedge * np.cos(th)],
             [R_peri * np.sin(th), R_wedge * np.sin(th)],
             color=DARK, lw=0.8, ls=(0, (3, 3)), zorder=4)

# Pericenter / apocenter labels
for k, (th, rr) in enumerate(zip(theta_peri, r_peri)):
    axa.annotate(f"$P_{k + 1}$",
                 xy=(rr * np.cos(th), rr * np.sin(th)),
                 xytext=(1.12 * rr * np.cos(th), 1.12 * rr * np.sin(th)),
                 fontsize=11, color=DARKBLUE, ha="center", va="center",
                 zorder=8)
axa.annotate("$A_1$",
             xy=(r_apo[0] * np.cos(theta_apo[0]),
                 r_apo[0] * np.sin(theta_apo[0])),
             xytext=(1.10 * r_apo[0] * np.cos(theta_apo[0]),
                     1.10 * r_apo[0] * np.sin(theta_apo[0])),
             fontsize=11, color=GREEN, ha="center", va="center", zorder=8)

# A legend keeps the arc labels off the orbit itself
handles = [
    Line2D([], [], color=GREEN, lw=3.0,
           label=r"$\Delta\theta_{\rm apse}=\pi/\sqrt{n+3}$"),
    Line2D([], [], color=DARKBLUE, lw=3.0,
           label=r"$\Delta\theta_{\rm peri\to peri}=2\pi/\sqrt{n+3}$"),
    Patch(facecolor=ORANGE, alpha=0.55,
          label=r"$\Delta\theta_{\rm prec}=2\pi/\sqrt{n+3}-2\pi$"),
]
# The emphasized first radial cycle covers every direction except the sector
# 254 deg -> 360 deg, so the lower-right corner is the only one it never enters.
axa.legend(handles=handles, loc="lower right", frameon=True, framealpha=0.95,
           edgecolor="#dddddd", fontsize=10.2, handlelength=2.0,
           borderpad=0.6, labelspacing=0.55)

axa.set_xlim(-1.52, 1.52)
axa.set_ylim(-1.52, 1.52)
axa.set_xticks([])
axa.set_yticks([])
for spine in axa.spines.values():
    spine.set_visible(False)
axa.set_title("(a)  orbit and the angles", fontsize=13.5, pad=6)

# ---------------------------------------------------------------------------
# Panel (b): linear angle ruler
# ---------------------------------------------------------------------------
axb.set_xlim(-0.24, 2.0 * np.pi + 0.42)
axb.set_ylim(-0.95, 2.62)

rows = [
    {"n": -2.0, "y": 1.78, "color": ORANGE,
     "label": r"$n=-2$  (inverse square): $\Delta\theta_{\rm prec}=0$,"
              r" the orbit closes"},
    {"n": -1.0, "y": 0.22, "color": BLUE,
     "label": r"$n=-1$  ($F=-k/r$): precession is backward"},
]

for row in rows:
    nn, y0, col = row["n"], row["y"], row["color"]
    a = np.sqrt(nn + 3.0)
    t_ap = np.pi / a
    t_pp = 2.0 * np.pi / a

    # baseline
    axb.plot([-0.10, 2.0 * np.pi + 0.16], [y0, y0], color=LIGHT, lw=5.0,
             solid_capstyle="round", zorder=1)

    # turning points: filled = pericenter, open = apocenter
    axb.plot([0.0, t_pp], [y0, y0], "o", ms=8.5, color=col,
             mec="white", mew=1.3, zorder=4)
    axb.plot([t_ap], [y0], "o", ms=7.5, mfc="white", mec=col, mew=1.8, zorder=4)

    # the two spans
    h1, h2 = 0.18, 0.38
    axb.annotate("", xy=(0.0, y0 + h1), xytext=(t_ap, y0 + h1),
                 arrowprops=dict(arrowstyle="<->", color=col, lw=1.5,
                                 shrinkA=2, shrinkB=2))
    axb.text(t_ap / 2.0, y0 + h1 + 0.04, r"$\pi/\sqrt{n+3}$", fontsize=10.5,
             color=col, ha="center", va="bottom")

    axb.annotate("", xy=(0.0, y0 + h2), xytext=(t_pp, y0 + h2),
                 arrowprops=dict(arrowstyle="<->", color=col, lw=1.5,
                                 shrinkA=2, shrinkB=2))
    axb.text(t_pp / 2.0, y0 + h2 + 0.04, r"$2\pi/\sqrt{n+3}$", fontsize=10.5,
             color=col, ha="center", va="bottom")

    # labels under the ruler
    axb.text(0.0, y0 - 0.15, "pericenter", fontsize=9.6, color=DARK,
             ha="center", va="top")
    axb.text(t_ap, y0 - 0.15, "apocenter", fontsize=9.6, color=DARK,
             ha="center", va="top")
    axb.text(t_pp, y0 - 0.15, "pericenter", fontsize=9.6, color=DARK,
             ha="center", va="top")
    axb.text(2.0 * np.pi, y0 - 0.52,
             "$2\\pi$ of motion:\nsame ray", fontsize=9.6, color=DARK,
             ha="center", va="top")

    # precession gap
    if t_pp < 2.0 * np.pi - 1.0e-9:
        axb.add_patch(
            Rectangle((t_pp, y0 - 0.065), 2.0 * np.pi - t_pp, 0.13,
                      facecolor=ORANGE, alpha=0.35, edgecolor="none", zorder=2)
        )
        axb.annotate("", xy=(t_pp, y0 - 0.24), xytext=(2.0 * np.pi, y0 - 0.24),
                     arrowprops=dict(arrowstyle="<->", color=ORANGE, lw=1.5,
                                     shrinkA=1, shrinkB=1))
        axb.text((t_pp + 2.0 * np.pi) / 2.0, y0 - 0.29,
                 r"$\Delta\theta_{\rm prec}$", fontsize=10.5, color=ORANGE,
                 ha="center", va="top")

    # row title above the ruler, left aligned at theta = 0
    axb.text(0.0, y0 + 0.62, row["label"], fontsize=10.5, color=col,
             ha="left", va="bottom")

# one-full-turn reference line
axb.axvline(2.0 * np.pi, color=GRAY, lw=0.9, ls=(0, (4, 4)), zorder=0)

axb.set_xticks([0.0, np.pi / 2.0, np.pi, 3.0 * np.pi / 2.0, 2.0 * np.pi])
axb.set_xticklabels(["$0$", "$\\pi/2$", "$\\pi$", "$3\\pi/2$", "$2\\pi$"])
axb.set_yticks([])
axb.set_xlabel("angle swept, $\\theta$", fontsize=12)
for spine in ("top", "right", "left"):
    axb.spines[spine].set_visible(False)
axb.set_title("(b)  the same angles as a ruler", fontsize=13.5, pad=6)

fig.tight_layout(w_pad=2.4)

out = ("/Users/sliutheory/Sandbox/2026Teaching/Book/"
       "CentralForceImage/apsidal-angles.png")
fig.savefig(out, dpi=200, bbox_inches="tight", facecolor="white")
print("saved", out)
