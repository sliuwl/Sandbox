"""Generate the lecture figures (PNG and vector PDF) using NumPy/Matplotlib.

Run from any directory: python3 /path/to/CoupledOscillatorsImage/make_figures.py
The original handwritten images are preserved; output goes into generated/.
"""

from pathlib import Path
import os
import tempfile

os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "coupled-mpl"))
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

OUT = Path(__file__).resolve().parent / "generated"
BLUE, ORANGE, GRAY = "#2369a1", "#c35f17", "#697586"
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 11,
    "mathtext.fontset": "dejavusans", "axes.spines.top": False,
    "axes.spines.right": False, "savefig.facecolor": "white",
})


def save(fig, name):
    OUT.mkdir(exist_ok=True)
    for ext in ("png", "pdf"):
        fig.savefig(OUT / f"{name}.{ext}", dpi=190, bbox_inches="tight")
    plt.close(fig)


def spring(ax, left, right, y=0, label=None):
    x = np.linspace(left, right, 23)
    z = np.zeros_like(x)
    z[2:-2] = 0.11 * (-1.0) ** np.arange(len(x) - 4)
    ax.plot(x, y + z, color=GRAY, lw=1.6)
    if label:
        ax.text((left + right) / 2, y + 0.25, label, ha="center")


def chain(ax, n, walls=True, labels=None, surface=False):
    centers = 1.5 * np.arange(n)
    if surface:
        left, right, level = -1.1, centers[-1] + 1.1, -.22
        ax.add_patch(Rectangle((left, level - .1), right - left, .1,
                               facecolor="#f0f2f5", edgecolor=GRAY,
                               hatch="///", lw=0, zorder=0))
        ax.plot([left, right], [level, level], color=GRAY, lw=1.6, zorder=1)
    for j, x in enumerate(centers):
        ax.add_patch(Rectangle((x - .25, -.22), .5, .44,
                               facecolor="#e7eff7", edgecolor=BLUE, lw=1.5))
        ax.text(x, 0, "$m$", ha="center", va="center")
        ax.text(x, -.4, str(j + 1), ha="center", color=GRAY, fontsize=9)
    for j in range(n - 1):
        spring(ax, centers[j] + .25, centers[j + 1] - .25,
               label=labels[j + 1] if labels else None)
    if walls:
        for wall, end, lab in [(-1.1, -.25, labels[0] if labels else None),
                               (centers[-1] + 1.1, centers[-1] + .25,
                                labels[-1] if labels else None)]:
            spring(ax, min(wall, end), max(wall, end), label=lab)
            ax.plot([wall, wall], [-.22 if surface else -.35, .35],
                    color=GRAY, lw=3)
    ax.set_xlim(-1.35, centers[-1] + 1.35)
    ax.set_ylim(-.75, 1.05)
    ax.set_aspect("equal")
    ax.axis("off")
    return centers


def setups():
    for n, name, labels in [(2, "two-blocks-setup", ["$k$", "$k'$", "$k$"]),
                             (3, "three-blocks-setup", ["$k$"] * 4)]:
        fig, ax = plt.subplots(figsize=(9, 2.7), layout="constrained")
        centers = chain(ax, n, labels=labels, surface=True)
        for j, x in enumerate(centers):
            ax.annotate("", (x + .5, .65), (x, .65),
                        arrowprops={"arrowstyle": "->", "color": BLUE, "lw": 1.8})
            ax.text(x + .25, .82, f"$x_{j + 1}$", ha="center", color=BLUE)
        ax.set_title("Displacements from equilibrium; positive to the right", fontsize=12)
        save(fig, name)


def mode_figure(vectors, labels, name, walls=True, surface=False):
    fig, axes = plt.subplots(len(vectors), 1, figsize=(9, 2.1 * len(vectors)),
                             layout="constrained")
    for ax, vec, title in zip(axes, vectors, labels):
        centers = chain(ax, len(vec), walls=walls, surface=surface)
        amplitudes = np.asarray(vec) / np.max(np.abs(vec))
        for x, a in zip(centers, amplitudes):
            if abs(a) < 1e-12:
                ax.plot(x, .62, "o", color=GRAY, ms=4)
                ax.text(x, .83, "stationary", ha="center", fontsize=9, color=GRAY)
            else:
                ax.annotate("", (x + .65 * a, .62), (x, .62),
                            arrowprops={"arrowstyle": "-|>", "lw": 2.2,
                                        "color": BLUE if a > 0 else ORANGE})
        ax.set_title(title, loc="left", fontsize=12)
    save(fig, name)


def trajectories(ratio, t):
    """Exact kick solution with dimensionless m=k=v1=1, v2=0."""
    w1, w2 = 1.0, np.sqrt(1 + 2 * ratio)
    x1 = .5 * (np.sin(w1 * t) / w1 + np.sin(w2 * t) / w2)
    x2 = .5 * (np.sin(w1 * t) / w1 - np.sin(w2 * t) / w2)
    v1 = .5 * (np.cos(w1 * t) + np.cos(w2 * t))
    v2 = .5 * (np.cos(w1 * t) - np.cos(w2 * t))
    return w1, w2, x1, x2, v1, v2


def weak_coupling():
    ratio = .05
    delta = (np.sqrt(1 + 2 * ratio) - 1) / 2
    period = np.pi / delta
    t = np.linspace(0, period, 6500)
    w1, w2, x1, x2, v1, v2 = trajectories(ratio, t)
    mean = (w1 + w2) / 2
    frac = t / period
    fig, axes = plt.subplots(3, 1, figsize=(9, 8), sharex=True, layout="constrained")
    for ax, x, env, color, j in zip(
            axes[:2], [x1, x2],
            [np.abs(np.cos(delta * t)) / mean, np.abs(np.sin(delta * t)) / mean],
            [BLUE, ORANGE], [1, 2]):
        ax.plot(frac, x, color=color, lw=.9, label="exact displacement")
        ax.plot(frac, env, "--", color=GRAY, lw=1.2, label="leading-order envelope")
        ax.plot(frac, -env, "--", color=GRAY, lw=1.2)
        ax.set_ylabel(rf"$x_{j}/(v_1/\omega_1)$")
        ax.legend(loc="upper right", fontsize=8)
    e1, e2, ec = .5 * (v1**2 + x1**2), .5 * (v2**2 + x2**2), .5 * ratio * (x2 - x1)**2
    np.testing.assert_allclose(e1 + e2 + ec, .5, atol=1e-13)
    axes[2].plot(frac, e1 / .5, color=BLUE, label=r"$E_1/E_0$")
    axes[2].plot(frac, e2 / .5, color=ORANGE, label=r"$E_2/E_0$")
    axes[2].plot(frac, ec / .5, color=GRAY, label=r"$U_c/E_0$")
    axes[2].set_ylabel("Energy fraction")
    axes[2].set_xlabel(r"$t/T_{\mathrm{beat}}$;  $T_{\mathrm{beat}}=2\pi/(\omega_2-\omega_1)$")
    axes[2].legend(ncol=3, loc="upper center", fontsize=9)
    for ax in axes:
        ax.axvline(.5, color=GRAY, ls=":", lw=1)
        ax.grid(alpha=.15)
        ax.set_xlim(0, 1)
    fig.suptitle(r"Weak coupling: $k'/k=0.05$, with only block 1 initially kicked")
    save(fig, "weak-coupling")


def strong_coupling():
    t = np.linspace(0, 4 * np.pi, 3000)
    w1, w2, x1, x2, _, _ = trajectories(20, t)
    fig, axes = plt.subplots(2, 1, figsize=(9, 5.8), sharex=True, layout="constrained")
    axes[0].plot(t / (2 * np.pi), x1, color=BLUE, label=r"$x_1$")
    axes[0].plot(t / (2 * np.pi), x2, color=ORANGE, label=r"$x_2$")
    axes[0].plot(t / (2 * np.pi), .5 * np.sin(t), "--", color=GRAY,
                 label=r"$X=(x_1+x_2)/2$")
    axes[0].set_ylabel(r"Displacement / $(v_1/\omega_1)$")
    axes[0].legend(ncol=3, loc="upper right")
    axes[1].plot(t / (2 * np.pi), x2 - x1, color=ORANGE)
    axes[1].set_ylabel(r"$(x_2-x_1)/(v_1/\omega_1)$")
    axes[1].set_xlabel(r"$t/T_1$;  $T_1=2\pi/\omega_1$")
    for ax in axes:
        ax.grid(alpha=.18)
        ax.set_xlim(0, 2)
    fig.suptitle(r"Strong coupling: $k'/k=20$, with only block 1 initially kicked")
    save(fig, "strong-coupling")


def main():
    setups()
    mode_figure([[1, 1], [-1, 1]],
                [r"Mode 1: $(1,1)$,  $\omega_1=\sqrt{k/m}$",
                 r"Mode 2: $(-1,1)$,  $\omega_2=\sqrt{(k+2k')/m}$"],
                "two-block-modes", surface=True)
    mode_figure([[1, 0, -1], [1, np.sqrt(2), 1], [1, -np.sqrt(2), 1]],
                [r"Mode 1: $(1,0,-1)$,  $\omega_1=\sqrt{2k/m}$",
                 r"Mode 2: $(1,\sqrt{2},1)$,  $\omega_2=\sqrt{(2-\sqrt{2})k/m}$",
                 r"Mode 3: $(1,-\sqrt{2},1)$,  $\omega_3=\sqrt{(2+\sqrt{2})k/m}$"],
                "fixed-end-modes", surface=True)
    mode_figure([[1, 1, 1], [1, 0, -1], [-1, 2, -1]],
                [r"Mode 1: $(1,1,1)$,  $\omega_1=0$ (translation)",
                 r"Mode 2: $(1,0,-1)$,  $\omega_2=\sqrt{k/m}$",
                 r"Mode 3: $(-1,2,-1)$,  $\omega_3=\sqrt{3k/m}$"],
                "free-end-modes", walls=False, surface=True)
    weak_coupling()
    strong_coupling()
    print(f"Generated 7 figures in PNG and PDF: {OUT}")


if __name__ == "__main__":
    main()
