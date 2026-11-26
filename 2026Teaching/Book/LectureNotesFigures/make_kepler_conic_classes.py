"""Draw the four Kepler conic classes on one set of axes.

All four orbits share the same force center (the focus at the origin) and the
same periapsis distance q.  For the orbit equation

    r(theta) = p / (1 + e cos theta),    p = q (1 + e),

theta = 0 is the common periapsis.  The circle and ellipse are written in
Cartesian form; the parabola and the physical branch of the hyperbola are
drawn from their standard Cartesian equations and clipped by the axes limits.
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Geometry
# ---------------------------------------------------------------------------
q = 1.0                       # common periapsis distance
e_circle = 0.0
e_ellipse = 0.5
e_parabola = 1.0
e_hyperbola = 1.5

xlim = (-3.15, 1.65)
ylim = (-2.55, 2.55)

# Circle and ellipse
p_circle = q * (1.0 + e_circle)
R_circle = p_circle                       # circle radius (focus = center)

p_ellipse = q * (1.0 + e_ellipse)
a_ellipse = p_ellipse / (1.0 - e_ellipse**2)
b_ellipse = p_ellipse / np.sqrt(1.0 - e_ellipse**2)
c_ellipse = a_ellipse * e_ellipse
x_center_ellipse = -c_ellipse

# Parabola: y^2 = 2 p (q - x), with vertex at x = q
p_parabola = q * (1.0 + e_parabola)

# Hyperbola physical (left) branch: center at x_c = a e, vertex at x = q
p_hyperbola = q * (1.0 + e_hyperbola)
a_hyperbola = p_hyperbola / (e_hyperbola**2 - 1.0)
b_hyperbola = p_hyperbola / np.sqrt(e_hyperbola**2 - 1.0)
x_center_hyperbola = a_hyperbola * e_hyperbola

# ---------------------------------------------------------------------------
# Curves
# ---------------------------------------------------------------------------
t = np.linspace(0.0, 2.0 * np.pi, 1200)
x_circle = R_circle * np.cos(t)
y_circle = R_circle * np.sin(t)

E = np.linspace(0.0, 2.0 * np.pi, 1200)
x_ellipse = a_ellipse * np.cos(E) + x_center_ellipse
y_ellipse = b_ellipse * np.sin(E)

y_parabola = np.linspace(-4.0, 4.0, 1200)
x_parabola = q - y_parabola**2 / (2.0 * p_parabola)

y_hyperbola = np.linspace(-4.0, 4.0, 1200)
x_hyperbola = (
    x_center_hyperbola
    - a_hyperbola * np.sqrt(1.0 + (y_hyperbola / b_hyperbola) ** 2)
)

# ---------------------------------------------------------------------------
# Style
# ---------------------------------------------------------------------------
BLUE = "#3a78b5"
ORANGE = "#e07b24"
GREEN = "#2f9e44"
PURPLE = "#8e44ad"
GRAY = "#b8b8b8"
DARK = "#222222"

plt.rcParams.update(
    {
        "font.family": "serif",
        "mathtext.fontset": "dejavuserif",
        "font.size": 13,
        "axes.linewidth": 0.0,
        "figure.facecolor": "white",
        "savefig.facecolor": "white",
    }
)

fig, ax = plt.subplots(figsize=(7.6, 7.2), dpi=200)

# Coordinate axes through the force center
ax.axhline(0.0, color=GRAY, lw=1.0, zorder=0)
ax.axvline(0.0, color=GRAY, lw=1.0, zorder=0)

ax.plot(x_circle, y_circle, color=BLUE, lw=2.4, label="circle  ($e=0$)")
ax.plot(x_ellipse, y_ellipse, color=ORANGE, lw=2.4, label="ellipse  ($0<e<1$)")
ax.plot(x_parabola, y_parabola, color=GREEN, lw=2.4, label="parabola  ($e=1$)")
ax.plot(x_hyperbola, y_hyperbola, color=PURPLE, lw=2.4, label="hyperbola  ($e>1$)")

# Force center and the common periapsis
ax.plot(0.0, 0.0, "o", ms=7.5, color=DARK, mec="white", mew=1.5, zorder=5)
ax.annotate(
    "focus\n(force center)",
    xy=(0.0, 0.0),
    xytext=(-0.86, -0.52),
    fontsize=11.5,
    color=DARK,
    ha="center",
    va="center",
    arrowprops=dict(arrowstyle="-", color=DARK, lw=0.9, shrinkA=2, shrinkB=5),
    zorder=6,
)

ax.plot(q, 0.0, "o", ms=7.0, mfc="white", mec=DARK, mew=1.6, zorder=6)
ax.annotate(
    "shared\nperiapsis",
    xy=(q, 0.0),
    xytext=(1.28, -0.66),
    fontsize=11.5,
    color=DARK,
    ha="center",
    va="center",
    arrowprops=dict(arrowstyle="-", color=DARK, lw=0.9, shrinkA=2, shrinkB=5),
    zorder=6,
)

ax.set_xlim(*xlim)
ax.set_ylim(*ylim)
ax.set_aspect("equal", adjustable="box")
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

ax.legend(
    loc="lower left",
    frameon=True,
    framealpha=0.95,
    edgecolor="#dddddd",
    fontsize=11.5,
    handlelength=2.0,
)

out = (
    "/Users/sliutheory/Sandbox/2026Teaching/Book/"
    "CentralForceImage/kepler-conic-classes.png"
)
fig.savefig(out, dpi=200, bbox_inches="tight", facecolor="white")
print("saved", out)
