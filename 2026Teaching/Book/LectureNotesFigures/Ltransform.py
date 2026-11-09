import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# Example function
# ------------------------------------------------------------
# Choose a simple convex function:
# L(V) = 1/2 V^2
# Then P = dL/dV = V
# The Legendre transform is H(P) = 1/2 P^2

V = np.linspace(0, 3, 400)
P = V

V0 = 2.2
P0 = V0

# ------------------------------------------------------------
# Figure 1: L(V) as area under P(V)
# ------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6, 4))

ax.plot(V, P, color="black", linewidth=2, label=r"$P(V)=\frac{dL}{dV}$")
ax.fill_between(V[V <= V0], P[V <= V0], color="lightgray", hatch="//", edgecolor="gray")

ax.axvline(V0, color="black", linestyle="--")
ax.axhline(P0, color="black", linestyle="--")

ax.text(V0 + 0.05, 0.1, r"$V$", fontsize=14)
ax.text(0.1, P0 + 0.05, r"$P$", fontsize=14)
ax.text(1.0, 0.7, r"$L(V)=\int_0^V P(V')\,dV'$", fontsize=13)

ax.set_xlabel(r"$V$")
ax.set_ylabel(r"$P$")
ax.set_title(r"Original function: $L(V)$ as area under $P(V)$")
ax.set_xlim(0, 3)
ax.set_ylim(0, 3)
ax.grid(True, alpha=0.3)
ax.legend()

plt.tight_layout()
plt.savefig("figure_1_L_of_V.png", dpi=300)
plt.show()

# ------------------------------------------------------------
# Figure 2: H(P) as area under V(P)
# ------------------------------------------------------------
P_values = np.linspace(0, 3, 400)
V_of_P = P_values

fig, ax = plt.subplots(figsize=(6, 4))

ax.plot(P_values, V_of_P, color="black", linewidth=2, label=r"$V(P)$")
ax.fill_between(P_values[P_values <= P0], V_of_P[P_values <= P0],
                color="lightgray", hatch="\\\\", edgecolor="gray")

ax.axvline(P0, color="black", linestyle="--")
ax.axhline(V0, color="black", linestyle="--")

ax.text(P0 + 0.05, 0.1, r"$P$", fontsize=14)
ax.text(0.1, V0 + 0.05, r"$V$", fontsize=14)
ax.text(0.7, 1.1, r"$H(P)=\int_0^P V(P')\,dP'$", fontsize=13)

ax.set_xlabel(r"$P$")
ax.set_ylabel(r"$V$")
ax.set_title(r"Legendre-transformed function: $H(P)$ as area under $V(P)$")
ax.set_xlim(0, 3)
ax.set_ylim(0, 3)
ax.grid(True, alpha=0.3)
ax.legend()

plt.tight_layout()
plt.savefig("figure_2_H_of_P.png", dpi=300)
plt.show()

# ------------------------------------------------------------
# Figure 3: Rectangle relation L(V) + H(P) = PV
# ------------------------------------------------------------
fig, ax = plt.subplots(figsize=(5, 5))

# Rectangle PV
ax.fill_between([0, P0], [V0, V0], color="white", edgecolor="black", linewidth=2)
ax.plot([0, P0, P0, 0, 0], [0, 0, V0, V0, 0], color="black", linewidth=2)

# Curve V(P)
ax.plot(P_values, V_of_P, color="black", linewidth=2)

# Area H(P)
ax.fill_between(P_values[P_values <= P0], V_of_P[P_values <= P0],
                color="lightgray", hatch="\\\\", edgecolor="gray", label=r"$H(P)$")

# Complementary area L(V)
ax.fill_between(P_values[P_values <= P0],
                V_of_P[P_values <= P0],
                V0,
                color="white",
                hatch="//",
                edgecolor="gray",
                label=r"$L(V)$")

ax.text(0.3, 1.7, r"$L(V)$", fontsize=14)
ax.text(1.3, 0.6, r"$H(P)$", fontsize=14)
ax.text(1.2, 2.35, r"$PV$", fontsize=14)

ax.set_xlabel(r"$P$")
ax.set_ylabel(r"$V$")
ax.set_title(r"Area relation: $L(V)+H(P)=PV$")
ax.set_xlim(0, 3)
ax.set_ylim(0, 3)
ax.set_aspect("equal", adjustable="box")
ax.grid(True, alpha=0.3)
ax.legend()

plt.tight_layout()
plt.savefig("figure_3_rectangle_relation.png", dpi=300)
plt.show()
