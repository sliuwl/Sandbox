"""How a tangential impulse changes the effective potential.

Units m = k = r0 = 1, so the circular angular momentum satisfies
l_c^2 = m k r0 = 1 and the speed ratio alpha = v/v_c gives l = alpha l_c,
hence l^2 = alpha^2.  The effective potential is

    V_eff(r) = -1/r + alpha^2 / (2 r^2).

Its minimum is at r_c = alpha^2 r0 and its value at r0 = 1 is the new energy
E = (alpha^2 - 2)/2.  The particle is at r0 with zero radial velocity, so r0
is a turning point; the other turning point follows from

    2E r^2 + 2r - alpha^2 = 0  =>  r = alpha^2 / (2 - alpha^2).

Panel (a): alpha = 0.7 < 1, the well moves inward, r0 is the outer turning
           point and P is the apoapsis.
Panel (b): alpha = 1.2 > 1, the well moves outward, r0 is the inner turning
           point and P is the periapsis.

Both panels use the same r grid and the same axis limits, so the dashed
original potential (alpha = 1) is identical in the two panels and can be
compared directly.
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# ---------------------------------------------------------------------------
# Style (matches the other CentralForce figures)
# ---------------------------------------------------------------------------
BLUE = "#3a78b5"
ORANGE = "#e07b24"
GRAY = "#b8b8b8"
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


def effective_potential(r, alpha):
    """V_eff(r) = -k/r + l^2/(2 m r^2) with m = k = 1 and l = alpha."""
    return -1.0 / r + 0.5 * alpha**2 / r**2


# ---------------------------------------------------------------------------
# Shared axes and data
# ---------------------------------------------------------------------------
XLIM = (0.16, 3.10)
YLIM = (-1.30, 0.30)

# One common grid: the original potential is evaluated once and reused.
r = np.linspace(XLIM[0], XLIM[1], 3000)
V_old = effective_potential(r, 1.0)

panels = [
    {
        "alpha": 0.7,
        "color": BLUE,
        "title": r"(a)  $\alpha=0.7<1$:  $P$ is the apoapsis",
    },
    {
        "alpha": 1.2,
        "color": ORANGE,
        "title": r"(b)  $\alpha=1.2>1$:  $P$ is the periapsis",
    },
]

fig, axes = plt.subplots(1, 2, figsize=(12.6, 5.4))

for ax, panel in zip(axes, panels):
    alpha = panel["alpha"]
    color = panel["color"]

    r_c = alpha**2                      # minimum of the new potential
    E = 0.5 * (alpha**2 - 2.0)          # new energy, V_eff(r0)
    r_turn = alpha**2 / (2.0 - alpha**2)  # the other turning point
    r_lo, r_hi = sorted((1.0, r_turn))  # classically allowed interval

    V_new = effective_potential(r, alpha)

    # Original circular potential: dashed grey (same data in both panels)
    ax.plot(r, V_old, color=GRAY, lw=2.2, ls=(0, (5, 3)), zorder=2)

    # New effective potential: solid colour
    ax.plot(r, V_new, color=color, lw=2.6, zorder=3)

    # Classically allowed region between the turning points
    mask = (r >= r_lo) & (r <= r_hi)
    ax.fill_between(r[mask], YLIM[0], V_new[mask],
                    color=color, alpha=0.13, lw=0, zorder=1)

    # New energy: horizontal dashed line
    ax.axhline(E, color=DARK, lw=1.3, ls=(0, (6, 4)), zorder=4)

    # r_c and r0: vertical dotted lines
    for rr in (r_c, 1.0):
        ax.axvline(rr, color=DARK, lw=1.0, ls=(0, (2, 3)), zorder=1)

    # Turning points on the energy line
    ax.plot(1.0, E, "o", ms=8.5, color=color, mec="white", mew=1.5, zorder=6)
    ax.plot(r_turn, E, "o", ms=8.0, mfc="white", mec=color, mew=1.8, zorder=6)

    # Bottom of the new well
    V_min = -1.0 / (2.0 * alpha**2)
    ax.plot(r_c, V_min, "o", ms=4.5, color=color, mec="white", mew=1.0,
            zorder=5)

    # Annotations
    ax.annotate(r"$r_0$", xy=(1.0, YLIM[0]),
                xytext=(0, 6), textcoords="offset points",
                ha="center", va="bottom", fontsize=12, color=DARK)
    ax.annotate(r"$r_c=\alpha^2 r_0$", xy=(r_c, YLIM[0]),
                xytext=(0, 6), textcoords="offset points",
                ha="center", va="bottom", fontsize=12, color=color)
    ax.annotate(r"$E$", xy=(XLIM[1], E),
                xytext=(-2, 6), textcoords="offset points",
                ha="right", va="bottom", fontsize=12, color=DARK)
    ax.annotate(r"$V_{\rm eff}$", xy=(XLIM[0], V_min),
                xytext=(6, 0), textcoords="offset points",
                ha="left", va="center", fontsize=12, color=color)

    # Axis labels
    ax.set_xlabel(r"$r\,/\,r_0$", fontsize=13)
    ax.set_ylabel(r"$V_{\rm eff}\,r_0\,/\,k$", fontsize=13)
    ax.set_xlim(*XLIM)
    ax.set_ylim(*YLIM)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    ax.set_title(panel["title"], fontsize=13.5, pad=8)

    handles = [
        Line2D([], [], color=GRAY, lw=2.2, ls=(0, (5, 3)),
               label=r"original circular orbit ($\alpha=1$)"),
        Line2D([], [], color=color, lw=2.6,
               label=rf"new potential ($\alpha={alpha}$)"),
    ]
    ax.legend(handles=handles, loc="lower right", frameon=True,
              framealpha=0.95, edgecolor="#dddddd", fontsize=10.5,
              handlelength=2.2, borderpad=0.6)

fig.tight_layout(w_pad=2.2)

out = (
    "/Users/sliutheory/Sandbox/2026Teaching/Book/"
    "CentralForceImage/effective-potential-tangential-impulse.png"
)
fig.savefig(out, dpi=200, bbox_inches="tight", facecolor="white")
print("saved", out)
