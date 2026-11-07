"""Generate figures for HW1_answers_EN.md. Requires numpy, scipy, matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import ellipk

OUTPUT = Path(__file__).resolve().parent

def plot_pendulum():
    # scipy ellipk takes parameter m = k**2, not modulus k.
    amplitude = np.linspace(0.0, 3.0, 601)  # radians
    m = np.sin(amplitude / 2.0) ** 2
    period_ratio = 2.0 / np.pi * ellipk(m)
    fig, ax = plt.subplots(figsize=(8, 4.8), layout="constrained")
    ax.plot(amplitude, period_ratio, color="#1764a5", lw=2.5,
            label=r"$2K(\sin^2(\Phi/2))/\pi$")
    ax.axhline(1.0, color="#777777", ls="--", lw=1.1,
               label="Small-amplitude limit")
    ax.scatter([3], [period_ratio[-1]], color="#c25119", zorder=5)
    ax.annotate(f"{period_ratio[-1]:.4f}",
                xy=(3, period_ratio[-1]), xytext=(-56, -10),
                textcoords="offset points", color="#a03b12")
    ax.set(xlim=(0, 3.08), ylim=(0.92, 2.8),
           xlabel=r"Amplitude $\Phi$ (rad)",
           ylabel=r"Period ratio $\tau/\tau_0$",
           title="Simple pendulum: period versus amplitude")
    ax.grid(alpha=0.22)
    ax.legend(loc="upper left", frameon=False)
    fig.savefig(OUTPUT / "pendulum_period.png", dpi=200)
    fig.savefig(OUTPUT / "pendulum_period.svg")
    plt.close(fig)
    print("Taylor 4.38: amplitude (rad), period ratio")
    for phi in np.arange(0.0, 3.01, 0.5):
        ratio = 2 / np.pi * ellipk(np.sin(phi / 2) ** 2)
        print(f"  {phi:.1f}, {ratio:.8f}")

def plot_cylindrical_coordinates():
    fig = plt.figure(figsize=(7.4, 6.0), layout="constrained")
    ax = fig.add_subplot(111, projection="3d")
    rho, phi, height = 2.1, np.deg2rad(38), 2.0
    px, py = rho * np.cos(phi), rho * np.sin(phi)
    style = dict(color="#555555", arrow_length_ratio=0.06, linewidth=1.2)
    ax.quiver(0, 0, 0, 3.0, 0, 0, **style)
    ax.quiver(0, 0, 0, 0, 2.7, 0, **style)
    ax.quiver(0, 0, 0, 0, 0, 2.9, **style)
    ax.text(3.08, 0, 0, "$x$", fontsize=12)
    ax.text(0, 2.8, 0, "$y$", fontsize=12)
    ax.text(0, 0, 3.0, "$z$", fontsize=12)
    ax.text(-0.1, -0.15, -0.12, "$O$", fontsize=12)
    ax.plot([0, px], [0, py], [0, 0], color="#1764a5", lw=2.5)
    ax.text(px * .68, py * .68, .13, r"$\rho$", fontsize=14)
    ax.plot([px, px], [py, py], [0, height], "--", color="#c25119", lw=2)
    ax.text(px + .13, py, height / 2, "$z$", fontsize=13)
    ax.plot([0, px], [0, py], [0, height], color="#4b8174", lw=1.8)
    ax.text(px * .46, py * .46, height * .62, r"$\mathbf{r}$", fontsize=13)
    arc = np.linspace(0, phi, 60)
    ax.plot(.7 * np.cos(arc), .7 * np.sin(arc), np.zeros_like(arc),
            color="#8a4c99", lw=1.8)
    ax.text(.95 * np.cos(phi / 2), .95 * np.sin(phi / 2), -.12,
            r"$\phi$", fontsize=14)
    ax.scatter([px, px], [py, py], [0, height], s=35, color="#111111")
    ax.text(px + .12, py + .08, -.08, r"$P'=(x,y,0)$", fontsize=11)
    ax.text(px + .08, py + .06, height + .12, r"$P=(x,y,z)$", fontsize=11)
    ax.set(xlim=(-.2, 3.2), ylim=(-.2, 3.0), zlim=(-.2, 3.2))
    ax.set_box_aspect((1, 1, 1))
    ax.view_init(elev=23, azim=-63)
    ax.set_axis_off()
    ax.set_title("Cylindrical coordinates", pad=0)
    fig.savefig(OUTPUT / "cylindrical_coordinates.png", dpi=200)
    fig.savefig(OUTPUT / "cylindrical_coordinates.svg")
    plt.close(fig)

if __name__ == "__main__":
    plot_pendulum()
    plot_cylindrical_coordinates()

