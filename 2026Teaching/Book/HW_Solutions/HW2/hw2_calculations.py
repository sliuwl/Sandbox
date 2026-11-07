"""HW2 figures and the numerical integral for Taylor 6.23.
Requires: numpy, scipy, matplotlib.
Run: python hw2_calculations.py
"""
from pathlib import Path
import json
import numpy as np
from scipy.integrate import quad
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent

def flight_calculation():
    D, v0, V = 2000.0, 500.0, 0.5  # mi, mi/h, (mi/h)/mi
    k = V / v0
    lam = 2 * k / (np.sqrt(4 + 2 * (k * D)**2) + 2)
    y = lambda x: lam * x * (D - x)
    slope = lambda x: lam * (D - 2*x)
    approx_integrand = lambda x: (1 + 0.5*slope(x)**2) / (v0*(1+k*y(x)))
    def exact_integrand(x):
        w, p = V*y(x), slope(x)
        return (1+p*p) / (w + np.sqrt(v0*v0 + (v0*v0-w*w)*p*p))
    approximate_time = quad(approx_integrand, 0, D, epsabs=1e-11)[0]
    exact_time_same_path = quad(exact_integrand, 0, D, epsabs=1e-11)[0]
    result = {
        "D_mi": D, "v0_mph": v0, "V_mph_per_mi": V,
        "k_per_mi": k, "lambda_per_mi": lam,
        "maximum_north_mi": y(D/2),
        "maximum_path_slope": abs(slope(0)),
        "maximum_wind_mph": V*y(D/2),
        "straight_flight_hours": D/v0,
        "approximate_flight_hours": approximate_time,
        "approximate_saving_minutes": (D/v0-approximate_time)*60,
        "exact_flight_hours_on_same_parabola": exact_time_same_path,
        "exact_saving_minutes_on_same_parabola": (D/v0-exact_time_same_path)*60,
    }
    xx = np.linspace(0,D,500)
    fig, ax = plt.subplots(figsize=(8,4.7),layout="constrained")
    ax.plot(xx,y(xx),lw=2.5,color="#1967a3",label="Approximate optimum")
    ax.plot([0,D],[0,0],"--",color="#777777",label="Direct route")
    ax.scatter([0,D,D/2],[0,0,y(D/2)],color="#c05c26",zorder=5)
    ax.annotate(f"Maximum north: {y(D/2):.3f} mi",
                (D/2,y(D/2)),xytext=(0,15),textcoords="offset points",
                ha="center")
    ax.set(xlim=(-60,D+60),ylim=(-35,440),xlabel="East x (mi)",
           ylabel="North y (mi)",title="Taylor 6.23: proposed flight path")
    ax.grid(alpha=.2)
    ax.legend(loc="upper left",frameon=False)
    fig.savefig(OUT/"flight_path.png",dpi=200)
    fig.savefig(OUT/"flight_path.svg")
    plt.close(fig)
    return result

def refractive_index_figure():
    # These are illustrative coordinates, since the question gives no endpoints.
    A = np.array([-1.0,1.0])
    B = np.array([2.0,1.5])
    center = (np.dot(B,B)-np.dot(A,A))/(2*(B[0]-A[0]))
    radius = np.hypot(A[0]-center,A[1])
    xx = np.linspace(A[0],B[0],500)
    yy = np.sqrt(radius*radius-(xx-center)**2)
    fig, ax = plt.subplots(figsize=(7.5,4.7),layout="constrained")
    ax.plot(xx,yy,lw=2.5,color="#1967a3",label="Ray in n(y) = L/y")
    ax.axhline(0,color="#555555",ls="--",lw=1)
    ax.plot([center,center],[0,radius],":",color="#999999",lw=1)
    ax.scatter([A[0],B[0]],[A[1],B[1]],color="#c05c26",zorder=5)
    ax.scatter([center],[0],color="#555555",zorder=5)
    ax.annotate("a",A,xytext=(-14,3),textcoords="offset points",fontsize=12)
    ax.annotate("b",B,xytext=(7,0),textcoords="offset points",fontsize=12)
    ax.text(center+.1,.12,r"$(x_c,0)$",fontsize=11)
    ax.text(-1.5,-.33,"y = 0: singular boundary; the ray stays in y > 0",
            fontsize=10)
    ax.set(xlim=(-1.6,2.8),ylim=(-.5,2.8),xlabel="x",ylabel="y",
           title="Fermat (b): circular arc (illustrative endpoints)")
    ax.set_aspect("equal")
    ax.grid(alpha=.15)
    ax.legend(loc="upper left",frameon=False)
    fig.savefig(OUT/"fermat_ray.png",dpi=200)
    fig.savefig(OUT/"fermat_ray.svg")
    plt.close(fig)

if __name__ == "__main__":
    results = flight_calculation()
    refractive_index_figure()
    (OUT/"numerical_results.json").write_text(
        json.dumps(results,indent=2),encoding="utf-8")
    print(json.dumps(results,indent=2))

