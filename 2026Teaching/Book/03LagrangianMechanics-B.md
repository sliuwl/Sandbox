# Lagrangian Mechanics (Part B)

**Reading material:** Chapter 7 of *Classical Mechanics* by John R. Taylor

This document continues from [03LagrangianMechanics-A.md](03LagrangianMechanics-A.md).

---


## 8. Generalized Coordinates and Constrained Systems

Perhaps the greatest advantage of the Lagrangian approach is that it can handle systems that are **constrained** so that they cannot move arbitrarily in the space that they occupy. A familiar example is a bead threaded on a wire — the bead can move along the wire, but not anywhere else. Another example is a rigid body, whose individual atoms can only move in such a way that the distance between any two atoms is fixed. For a system of $N$ particles, a complete unconstrained configuration requires $3N$ Cartesian coordinates; **constraints can reduce this number**.

> A **particle trapped inside a box** is a useful example to show that the word “constraint” does **not always mean reducing the number of degrees of freedom**.

------

### 8.1 Constraints and Degrees of Freedom

The **number of degrees of freedom** of a system is the number of coordinates that can be independently varied in a small displacement, or namely, the number of independent “directions” in which the system can move from any given initial configuration.

| System | Cartesian coordinates | Degrees of freedom |
|--------|----------------------|-------------------|
| Particle in 3D | 3 | 3 |
| Gas of $N$ particles | $3N$ | $3N$ |
| Simple pendulum | 2 | 1 |
| Double pendulum | 4 | 2 |
| Rigid body | $3N$ | 6 |

When the number of degrees of freedom is less than $3N$, the system is **constrained**. The particles in a rigid body are certainly constrained: although $N$ may be of order $10^{23}$, only six generalized coordinates are needed (three for the center of mass and three for orientation).

A system is called **holonomic** if the number of degrees of freedom equals the number of generalized coordinates needed to describe it. Holonomic systems are easier to treat than nonholonomic ones, and we shall restrict ourselves to holonomic systems.

> **Nonholonomic example.** You might imagine that all systems are holonomic. In fact, there are simple nonholonomic systems. Consider a hard rubber ball that is free to roll (but not slide) on a horizontal table. Starting at any position $(x,y)$ it can move in only two independent directions, so it has two degrees of freedom. One might think two coordinates $(x,y)$ suffice. But if you roll the ball around a right triangle and back to the start, it returns with a **changed orientation**. The position $(x,y)$ has returned to its initial value, but the ball has a different orientation. Thus $(x,y)$ do not specify a unique configuration — five coordinates are needed in all. The ball has **two degrees of freedom** but needs five coordinates: it is nonholonomic.

![](images/16d4ce11d7ff10453b563a491df3807907ef02bef183b49d424f91f0fc6888e4.jpg)  
**Figure 7.5** The right triangle OPQ lies in the $xy$ plane with sides OP and PQ of length $c$. If you roll a ball of circumference $c$ around OPQ, it will return to its starting point with a changed orientation.

We shall not discuss nonholonomic systems further. For any holonomic system, the evolution in time is determined by the standard Lagrange equations.

> The deeper lesson is that **the final configuration can depend on the path taken**, not only on the final position. Similar path-dependent effects appear in many areas of physics, including quantum mechanics, where they are related to **geometric phases**.

------

### 8.2 Generalized Coordinates

The parameters $q_1, \dots, q_n$ are called **generalized coordinates** for the system if each particle's position can be expressed as a function of the $q_i$ and possibly time:

$$
\mathbf r_\alpha = \mathbf r_\alpha(q_1, \dots, q_n, t), \qquad \alpha = 1, \dots, N,
$$

and conversely each $q_i$ can be expressed in terms of the positions:

$$
q_i = q_i(\mathbf r_1, \dots, \mathbf r_N, t), \qquad i = 1, \dots, n.
$$

The number $n$ is the smallest number of parameters that describes the system completely.

**Example: simple pendulum.** There is one particle and two Cartesian coordinates $(x,y)$. The constraint $x^2+y^2=l^2$ leaves one degree of freedom. Choosing the angle $\phi$ as generalized coordinate,

$$
\mathbf r \equiv (x,y) = (l\sin\phi,\; l\cos\phi).
$$

This expresses two Cartesian coordinates in terms of one generalized coordinate.

**Example: double pendulum.** The double pendulum has two bobs, both confined to a plane, so it has four Cartesian coordinates. These can be expressed in terms of two generalized coordinates $\phi_1$ and $\phi_2$:

$$
\mathbf r_1 = (l_1\sin\phi_1,\; l_1\cos\phi_1),
$$

$$
\mathbf r_2 = (l_1\sin\phi_1 + l_2\sin\phi_2,\; l_1\cos\phi_1 + l_2\cos\phi_2).
$$

Notice that $\mathbf r_2$ depends on both $\phi_1$ and $\phi_2$.

![](images/a99701bad52bfe9526f6525dbde65034e35e6d8818e128b0f9a2d0e7e731ea31.jpg)  
*Figure 7.3 The positions of both masses in a double pendulum are uniquely specified by the two generalized coordinates $\phi_1$ and $\phi_2$, which can themselves be varied independently.*

In these two examples, the transformation between Cartesian and generalized coordinates did not depend on time. It is easy to think of examples where it does. Consider a pendulum suspended from the roof of a railroad car that is being forced to accelerate with fixed acceleration $a$, as shown in Figure 7.4. The position of the bob relative to the ground is

$$
\mathbf r \equiv (x,y) = \bigl(l\sin\phi + \tfrac{1}{2}at^2,\; l\cos\phi\bigr) = \mathbf r(\phi,t).
$$

![](images/ac28ad29bb5df306da86418e17d3a4b91c76862be8cb3a871fa88ff7a03cef01.jpg)  
*Figure 7.4 A pendulum is suspended from the roof of a railroad car that is being forced to accelerate with a fixed, known acceleration $a$.*

Here the relation between $\mathbf r$ and the generalized coordinate $\phi$ depends explicitly on $t$.

A set of coordinates is called **natural** if the relation $\mathbf r_\alpha(q_1,\dots,q_n)$ between Cartesian and generalized coordinates does not involve time. Natural coordinates have convenient properties that do not generally apply when the transformation depends on time.

------

### 8.3 The Lagrangian in Generalized Coordinates

The Lagrangian is defined as before,

$$
L = T - V,
$$

but now $T$ and $V$ must be expressed in terms of the chosen generalized coordinates and their velocities:

$$
L = L(q_1, \dots, q_n, \dot q_1, \dots, \dot q_n, t).
$$

One of the principal advantages of the Lagrangian formulation is that the Euler–Lagrange equations retain exactly the same form in any choice of generalized coordinates:

$$
\boxed{ \frac{d}{dt}\left(\frac{\partial L}{\partial \dot q_i}\right) - \frac{\partial L}{\partial q_i} = 0, \qquad i = 1, \dots, n. }
$$

Moreover, the **forces of constraint** — such as tension in a string, the normal force from a surface, or interatomic forces in a rigid body — do not appear in these equations, provided the constraints are holonomic and the non-constraint forces are derivable from a potential energy $V$. This is a tremendous simplification, because constraint forces are usually unknown and we usually do not want to know them anyway.

------

### 8.4 Why Lagrange's Equations Work for Constrained Systems

It is essential to understand why the same Euler–Lagrange equations continue to hold for constrained systems. The key is Hamilton's principle combined with the nature of constraint forces.

Consider a particle constrained to move on a surface. There are two kinds of forces:

1. **Forces of constraint** $\mathbf F_{\text{cstr}}$: the normal force of the surface (for a bead on a wire, the normal force of the wire). These are not necessarily conservative.
2. **Non-constraint forces** $\mathbf F$: gravity, springs, etc. We assume these are derivable from a potential: $\mathbf F = -\nabla U$.

Define the Lagrangian using only the non-constraint potential:

$$
\mathcal L = T - U.
$$

The total force is $\mathbf F_{\text{tot}} = \mathbf F_{\text{cstr}} + \mathbf F$.

Now consider two paths between the same endpoints at times $t_1$ and $t_2$: the actual path $\mathbf r(t)$ and a nearby “wrong” path $\mathbf R(t) = \mathbf r(t) + \boldsymbol\epsilon(t)$ that also lies in the surface. Because both paths are in the surface, the variation $\boldsymbol\epsilon(t)$ is tangent to the surface, and $\boldsymbol\epsilon(t_1) = \boldsymbol\epsilon(t_2) = 0$.

Computing the difference in the action to first order gives

$$
\delta S = -\int_{t_1}^{t_2} \boldsymbol\epsilon \cdot \bigl[m\ddot{\mathbf r} + \nabla U\bigr]\,dt.
$$

Since the actual path satisfies Newton's second law, $m\ddot{\mathbf r} = \mathbf F_{\text{tot}} = \mathbf F_{\text{cstr}} + \mathbf F$, and $\nabla U = -\mathbf F$, the non-constraint forces cancel. We are left with

$$
\delta S = -\int_{t_1}^{t_2} \boldsymbol\epsilon \cdot \mathbf F_{\text{cstr}}\,dt.
$$

But the constraint force is **normal** to the surface, while the variation $\boldsymbol\epsilon$ lies **in** the surface. Therefore $\boldsymbol\epsilon \cdot \mathbf F_{\text{cstr}} = 0$, and we have proved that $\delta S = 0$.

> **Important:** The action is stationary only for variations *consistent with the constraints*. This means we cannot prove Lagrange's equations with respect to the three Cartesian coordinates $x,y,z$. However, we *can* prove them with respect to the generalized coordinates $q_1,q_2$, because any variation of $q_1$ and $q_2$ is automatically consistent with the constraints.

Rewriting the action in terms of $q_1,q_2$,

$$
S = \int_{t_1}^{t_2} \mathcal L(q_1,q_2,\dot q_1,\dot q_2,t)\,dt,
$$

and requiring $\delta S = 0$ for arbitrary variations of $q_1$ and $q_2$, we obtain the standard Lagrange equations

$$
\boxed{ \frac{\partial \mathcal L}{\partial q_i} = \frac{d}{dt}\frac{\partial \mathcal L}{\partial \dot q_i}, \qquad i = 1,\dots,n. }
$$

**General result:** For any holonomic system with $n$ degrees of freedom and $n$ generalized coordinates, with non-constraint forces derivable from a potential $U(q_1,\dots,q_n,t)$, the path is determined by the $n$ Lagrange equations above, where $\mathcal L = T - U$ and $U$ excludes the constraint forces.

This result — that Lagrange's equations have the same form for any choice of generalized coordinates — is one of the two main reasons the Lagrangian formalism is so useful.

> **Caution:** It is crucial that when we first write down $\mathcal L = T - U$, we do so in an **inertial frame**. The generalized coordinates $q_i$ themselves may be coordinates of a non-inertial frame, but the original kinetic and potential energies must be evaluated in an inertial frame.

## 9. Generalized Momenta and Ignorable Coordinates

For each generalized coordinate $q_i$, define the **generalized momentum**

$$
p_i = \frac{\partial L}{\partial \dot q_i}.
$$

The Euler–Lagrange equation can then be written as

$$
\dot p_i = \frac{\partial L}{\partial q_i},
$$

so $\partial L/\partial q_i$ plays the role of a generalized force.

If the Lagrangian does not depend explicitly on a particular coordinate $q_i$, that coordinate is called **ignorable** (or **cyclic**).  In that case $\partial L/\partial q_i = 0$ and

$$
p_i = \text{const}.
$$

Therefore, each ignorable coordinate yields a conserved quantity.

- In **Section 7.1** above, when $V$ depends only on $r$, the coordinate $\phi$ is ignorable and $p_\phi = mr^2\dot\phi$ (angular momentum) is conserved.
- In **Section 7.4**, $q_2$ was ignorable and the conserved momentum was the total horizontal momentum.

This profound connection between symmetry (invariance of $L$ under a coordinate transformation) and conservation laws is the essential content of **Noether's theorem (诺特定理)**.

> **Physical interpretation.**  The generalized momentum $p_i$ need not have the dimensions of ordinary momentum.  In polar coordinates, $p_\phi$ is angular momentum.  The generalized force $\partial L/\partial q_i$ need not have the dimensions of force either — in polar coordinates, $\partial L/\partial\phi$ is torque.  Nevertheless, the equation $\dot p_i = \partial L/\partial q_i$ is always the correct equation of motion.

