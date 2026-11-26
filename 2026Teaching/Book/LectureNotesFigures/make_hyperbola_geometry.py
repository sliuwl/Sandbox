"""
Generate CentralForceImage/hyperbola-geometry.png for Section 3.4.3.

Two panels:
  (a) focus-centered Kepler frame (x, y), focus F at the origin
  (b) center-centered frame (X, Y) = (x - ae, y)

The annotations follow the discussion in 06ConicSections.md: the inward
order C, V, F; r_min, a, and c = a + r_min; the center-frame coordinates
of F, V, V', F'; the fundamental rectangle; and the fact that b is the
asymptote height at X = -a rather than a point on the curve.
"""

import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------------- parameters
e = 1.5
p = 2.0
a = p / (e**2 - 1.0)          # 1.6
b = p / np.sqrt(e**2 - 1.0)   # 1.78885...
c = a * e                     # 2.4
rmin = p / (1.0 + e)          # 0.8

# ---------------------------------------------------------------- style
STEEL = (70 / 255, 130 / 255, 180 / 255)
CRIMSON = (220 / 255, 20 / 255, 60 / 255)
ORANGE = (255 / 255, 140 / 255, 0 / 255)
GRAY = (0.72, 0.72, 0.72)
LIGHT = (0.86, 0.86, 0.86)
BLACK = "black"

plt.rcParams.update({
    "font.family": "serif",
    "mathtext.fontset": "dejavuserif",
    "font.size": 12,
    "axes.linewidth": 0.0,
    "figure.facecolor": "white",
    "savefig.facecolor": "white",
})


def draw_axis(ax, xmax, ymax, xlabel="$x$", ylabel="$y$"):
    """Draw through-the-origin coordinate axes with arrowheads."""
    ax.annotate("", xy=(xmax, 0), xytext=(-xmax, 0),
                arrowprops=dict(arrowstyle="-|>", color=BLACK, lw=1.3,
                                shrinkA=0, shrinkB=0, mutation_scale=14),
                zorder=4)
    ax.annotate("", xy=(0, ymax), xytext=(0, -ymax),
                arrowprops=dict(arrowstyle="-|>", color=BLACK, lw=1.3,
                                shrinkA=0, shrinkB=0, mutation_scale=14),
                zorder=4)
    ax.text(xmax * 0.98, -0.28, xlabel, ha="right", va="top", fontsize=14)
    ax.text(0.10, ymax * 0.98, ylabel, ha="left", va="top", fontsize=14)


def point(ax, x, y, color, label, dx=0.0, dy=0.20, ha="center", va="bottom",
          fontsize=12, zorder=6):
    ax.plot([x], [y], "o", color=color, markersize=7, zorder=zorder)
    ax.text(x + dx, y + dy, label, ha=ha, va=va, fontsize=fontsize,
            zorder=zorder)


def measure(ax, x0, x1, y, color, label, fontsize=11, label_dy=0.0,
            lw=1.3):
    """Horizontal double-headed measurement arrow with a label above it."""
    ax.annotate("", xy=(x1, y), xytext=(x0, y),
                arrowprops=dict(arrowstyle="<|-|>", color=color, lw=lw,
                                shrinkA=0, shrinkB=0, mutation_scale=10),
                zorder=5)
    ax.text(0.5 * (x0 + x1), y + 0.14 + label_dy, label,
            ha="center", va="bottom", fontsize=fontsize, color=color,
            zorder=6)


def vmeasure(ax, x, y0, y1, color, label, fontsize=11):
    """Vertical double-headed measurement arrow with a rotated label."""
    ax.annotate("", xy=(x, y1), xytext=(x, y0),
                arrowprops=dict(arrowstyle="<|-|>", color=color, lw=1.3,
                                shrinkA=0, shrinkB=0, mutation_scale=10),
                zorder=5)
    ax.text(x + 0.08, 0.5 * (y0 + y1), label, ha="left", va="center",
            fontsize=fontsize, color=color, rotation=90, zorder=6)


# ---------------------------------------------------------------- curves
t = np.linspace(-2.1, 2.1, 1201)
X_left = -a * np.cosh(t)
Y_left = b * np.sinh(t)
X_right = a * np.cosh(t)
Y_right = b * np.sinh(t)

fig, axes = plt.subplots(1, 2, figsize=(13.6, 6.6), dpi=200)

# ================================================================ panel (a)
ax = axes[0]
ax.set_xlim(-2.5, 6.3)
ax.set_ylim(-3.65, 3.55)
ax.set_aspect("equal", adjustable="box")
ax.axis("off")

draw_axis(ax, 6.25, 3.5)

# asymptotes through C
slope = b / a
xs = np.array([-2.5, 6.3])
for s in (+1, -1):
    ax.plot(xs, s * slope * (xs - c), color=GRAY, lw=1.0, ls=(0, (6, 4)),
            zorder=1)

# branches: physical branch solid, second branch dashed
xl = c + X_left
yl = Y_left
xr = c + X_right
yr = Y_right
ax.plot(xl, yl, color=STEEL, lw=2.3, zorder=3)
ax.plot(xr, yr, color=STEEL, lw=2.0, ls=(0, (7, 4)), zorder=3)

# points on the transverse axis
point(ax, 0.0, 0.0, CRIMSON, "$F$", dx=-0.16, dy=0.18, ha="right")
point(ax, rmin, 0.0, STEEL, "$V$", dy=0.20)
point(ax, c, 0.0, ORANGE, "$C$", dy=0.20)
point(ax, c + a, 0.0, STEEL, "$V'$", dy=0.20, fontsize=11)
point(ax, 2 * c, 0.0, CRIMSON, "$F'$", dy=0.20, fontsize=11)
ax.text(0.0, -0.38, "$x_F=0$", ha="center", va="top", fontsize=11)
ax.text(rmin, -0.38, "$x_V=r_{\\min}$", ha="center", va="top", fontsize=11)
ax.text(c, -0.38, "$x_C=ae$", ha="center", va="top", fontsize=11)

# inward order arrow, just below the axis
ax.annotate("", xy=(0.04, -0.95), xytext=(2.36, -0.95),
            arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.4,
                            shrinkA=0, shrinkB=0, mutation_scale=12),
            zorder=5)
ax.text(1.20, -1.20, "reading inward from $C$:  $C,\\ V,\\ F$",
        ha="center", va="top", fontsize=11)

# ruler: r_min, a, a, r_min along the axis
ry = -2.90
for xv in (0.0, rmin, c, c + a, 2 * c):
    ax.plot([xv, xv], [0.0, ry - 0.10], color=LIGHT, lw=0.8, ls=(0, (2, 3)),
            zorder=0)

segments = [
    (0.0, rmin, CRIMSON, "$r_{\\min}$"),
    (rmin, c, ORANGE, "$a$"),
    (c, c + a, ORANGE, "$a$"),
    (c + a, 2 * c, CRIMSON, "$r_{\\min}$"),
]
for x0, x1, col, lab in segments:
    ax.plot([x0, x1], [ry, ry], color=col, lw=4.0, solid_capstyle="butt",
            zorder=4)
    ax.text(0.5 * (x0 + x1), ry - 0.14, lab, ha="center", va="top",
            fontsize=11, color=col)
ax.text(2 * c + 0.12, ry - 0.14, "axis", ha="left", va="top", fontsize=10,
        color="0.35")

# c = a + r_min bracket above the ruler
measure(ax, 0.0, c, -2.35, ORANGE, "$c=a+r_{\\min}$", fontsize=11, lw=1.1)

# scale annotation, inside the empty region between the branches
ax.text(1.45, 3.35,
        "drawn for $e=1.5$, $p=2$\n"
        "$a=1.6$,  $b\\approx1.789$,  $c=2.4$",
        ha="left", va="top", fontsize=10,
        bbox=dict(boxstyle="round,pad=0.35", fc="white", ec=LIGHT, lw=0.8),
        zorder=7)

ax.text(-2.42, 3.45, "(a)", fontsize=15, fontweight="bold", va="top",
        ha="left")
ax.text(1.20, 2.55, "focus-centered frame", ha="center", va="bottom",
        fontsize=12, style="italic")

# ================================================================ panel (b)
ax = axes[1]
ax.set_xlim(-3.75, 3.75)
ax.set_ylim(-3.45, 3.45)
ax.set_aspect("equal", adjustable="box")
ax.axis("off")

draw_axis(ax, 3.70, 3.40, xlabel="$X$", ylabel="$Y$")

# asymptotes
xs = np.array([-3.75, 3.75])
for s in (+1, -1):
    ax.plot(xs, s * slope * xs, color=GRAY, lw=1.0, ls=(0, (6, 4)), zorder=1)

# fundamental rectangle
ax.plot([-a, a, a, -a, -a], [-b, -b, b, b, -b], color=ORANGE, lw=1.3,
        ls=(0, (5, 3)), zorder=1.5)

# conjugate axis X = 0
ax.plot([0, 0], [-3.35, 3.35], color=GRAY, lw=1.0, ls=(0, (2, 3)), zorder=1)
ax.text(0.10, -3.30, "conjugate axis $X=0$", ha="left", va="bottom",
        fontsize=10, color="0.35")

# branches
ax.plot(X_left, Y_left, color=STEEL, lw=2.3, zorder=3)
ax.plot(X_right, Y_right, color=STEEL, lw=2.0, ls=(0, (7, 4)), zorder=3)

# latus rectum through F: X = -c, from Y = -p to +p
ax.plot([-c, -c], [-p, p], color=STEEL, lw=0.9, ls=(0, (1, 2)), zorder=2)
for yy in (-p, p):
    ax.plot([-c], [yy], "o", mfc="white", mec=STEEL, mew=1.1, markersize=5,
            zorder=5)
vmeasure(ax, -c - 0.16, 0.0, p, STEEL, "$p$", fontsize=11)

# diagonal from C to the rectangle corner on the asymptote
ax.plot([0, a], [0, b], color=ORANGE, lw=1.1, ls=(0, (2, 2)), zorder=2)
ax.text(0.74, 0.72, "$c$", color=ORANGE, fontsize=12, ha="left", va="bottom",
        zorder=6)
ax.text(1.02, 1.15, "$c=\\sqrt{a^2+b^2}$", color=ORANGE, fontsize=10,
        ha="left", va="bottom", zorder=6)

# a and b on the rectangle
measure(ax, 0.0, a, b + 0.14, ORANGE, "$a$", fontsize=11, lw=1.0)
vmeasure(ax, a + 0.15, 0.0, b, ORANGE, "$b$", fontsize=11)

# points
point(ax, -c, 0.0, CRIMSON, "$F$", dy=0.20)
point(ax, -a, 0.0, STEEL, "$V$", dy=0.20)
point(ax, 0.0, 0.0, ORANGE, "$C$", dy=0.20)
point(ax, a, 0.0, STEEL, "$V'$", dy=0.20)
point(ax, c, 0.0, CRIMSON, "$F'$", dy=0.20)

ax.text(-c, -0.38, "$-c$", ha="center", va="top", fontsize=11)
ax.text(-a, -0.38, "$-a$", ha="center", va="top", fontsize=11)
ax.text(0.0, -0.38, "$0$", ha="center", va="top", fontsize=11)
ax.text(a, -0.38, "$+a$", ha="center", va="top", fontsize=11)
ax.text(c, -0.38, "$+c$", ha="center", va="top", fontsize=11)

# b is the asymptote height at X = -a, not a curve point
ax.plot([-a, -a], [0.0, b], color=ORANGE, lw=1.1, ls=(0, (2, 2)), zorder=2)
ax.plot([-a], [b], "o", mfc="white", mec=ORANGE, mew=1.4, markersize=6,
        zorder=5)
ax.annotate("asymptote point $(-a,\\,b)$:\nnot on the curve",
            xy=(-a + 0.02, b - 0.02), xytext=(0.05, 2.95),
            ha="center", va="top", fontsize=10,
            arrowprops=dict(arrowstyle="-|>", color="0.35", lw=0.9,
                            shrinkA=4, shrinkB=2, mutation_scale=10),
            bbox=dict(boxstyle="round,pad=0.30", fc="white", ec=LIGHT, lw=0.8),
            zorder=7)

# standard form
ax.text(0.0, -2.55,
        "$\\dfrac{X^2}{a^2}-\\dfrac{Y^2}{b^2}=1$\n\n$c^2=a^2+b^2$",
        ha="center", va="center", fontsize=13,
        bbox=dict(boxstyle="round,pad=0.40", fc="white", ec=LIGHT, lw=0.8),
        zorder=7)

ax.text(-3.70, 3.40, "(b)", fontsize=15, fontweight="bold", va="top",
        ha="left")
ax.text(0.0, 3.12, "center-centered frame", ha="center", va="bottom",
        fontsize=12, style="italic")

fig.tight_layout(pad=0.6)
out = "/Users/sliutheory/Sandbox/2026Teaching/Book/CentralForceImage/hyperbola-geometry.png"
fig.savefig(out, dpi=200, bbox_inches="tight", facecolor="white")
print("saved", out)
