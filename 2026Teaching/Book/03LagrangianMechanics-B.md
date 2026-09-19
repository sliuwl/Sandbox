# Lagrangian Mechanics (Part B)

**Reading material:** Chapter 7 of *Classical Mechanics* by John R. Taylor

---


## 8. Generalized Coordinates and Constrained Systems

Perhaps the greatest advantage of the Lagrangian approach is that it can handle systems that are **constrained**. 

A familiar example is a bead threaded on a wire — the bead can move along the wire, but not anywhere else. 

Another example is a rigid body, whose individual atoms can only move in such a way that the distance between any two atoms is fixed. 

For a system of $N$ particles, a complete unconstrained configuration requires $3N$ Cartesian coordinates; **constraints can reduce this number**.

------

### 8.1 Classification of Constraints

The **number of degrees of freedom** of a system is the number of coordinates that can be **independently varied** in a small displacement, or namely, the number of independent "directions" in which the system can move from any given initial configuration.

| System | Cartesian coordinates | Degrees of freedom |
|--------|----------------------|-------------------|
| Particle in 3D | 3 | 3 |
| Gas of $N$ particles | $3N$ | $3N$ |
| Simple pendulum | 2 | 1 |
| Double pendulum | 4 | 2 |
| Rigid body | $3N$ | 6 |

When the number of degrees of freedom is less than $3N$, the system is **constrained**. The particles in a rigid body are certainly constrained: although $N$ may be of order $10^{23}$, only six generalized coordinates are needed (three for the center of mass and three for orientation).

> A **particle trapped inside a box** is a useful example to show that the word "constraint" does **not always mean reducing the number of degrees of freedom**.

#### Holonomic constraints 完整约束

If the conditions of constraint can be expressed as **equations** relating the coordinates of the particles, and possibly time, in the form

$$
f(\mathbf r_1, \mathbf r_2, \dots, \mathbf r_N, t) = 0,
$$

then the constraints are said to be **holonomic**. The simplest example is a rigid body, where the constraints are expressed by equations of the form

$$
(\mathbf r_i - \mathbf r_j)^2 - c_{ij}^2 = 0,
$$

fixing the distance between every pair of particles. 

A particle constrained to move along a given curve or on a given surface is another obvious example of a holonomic constraint, with the equations defining the curve or surface acting as the equations of constraint. For example, a particle constrained to move on a sphere of radius $R$ satisfies
\[
f(x,y,z)=x^2+y^2+z^2-R^2=0
\]
For a system of $N$ particles, free from constraints, there are $3N$ independent coordinates or degrees of freedom. 

If there exist $k$ holonomic constraints expressed in the form above, then we may use these equations to eliminate $k$ of the $3N$ coordinates, and we are left with $3N-k$ independent coordinates. In other words, the system has $3N-k$ degrees of freedom. This elimination of the dependent coordinates can be expressed by the introduction of new, independent variables $q_1, q_2, \dots, q_n$ (with $n = 3N-k$), which are the **generalized coordinates** we shall discuss in the next subsection.

> **Note on the Origin of “Holonomic”**
>
> The word **holonomic** comes from the Greek roots **holos** $(\text{whole, complete})$ and **nomos** $(\text{law})$. Thus, *holonomic* literally suggests something like “governed by a complete law.”
>
> The **holonomic**  constraint imposes a complete relation among the coordinates.



#### Rheonomous and Scleronomous Constraints（非定常约束与定常约束）

Constraints can also be classified according to whether the equations of constraint contain time as an explicit variable. 

If the constraint equations depend explicitly on time, the constraints are called **rheonomous constraints**（非定常约束）. 

If they do not depend explicitly on time, they are called **scleronomous constraints**（定常约束）.

A bead sliding on a rigid curved wire fixed in space is subject to a **scleronomous constraint**. If the wire moves in a prescribed way, then the constraint becomes **rheonomous**. However, if the wire moves only in response to the bead’s motion, the time dependence enters through the coordinates of the wire, which should then be included as part of the system coordinates. In that case, the overall constraint is still **scleronomous**.

#### Nonholonomic Constraints（非完整约束）

Constraints that cannot be expressed as equations involving only the coordinates, and possibly time, are called **nonholonomic constraints**.

A common source of nonholonomic constraints is an **inequality**. For example, the walls of a gas container restrict the particles to remain inside the box, so the constraint is not an equation of the form $f=0$. Similarly, a particle constrained to remain **outside or on** a solid sphere of radius $a$ satisfies $r^2-a^2 \ge 0,$ which is an inequality rather than a holonomic equation.

Another important class consists of **nonintegrable differential constraints**. These are **velocity constraints** that cannot be integrated into relations involving coordinates alone.  A standard example is a body **rolling** on a  surface **without slipping**. The rolling condition relates the translational motion of the contact point to the rotational motion of the body. Although it imposes a restriction on the motion, it cannot generally be written as a coordinate equation.

Consider a disk of radius $a$ rolling without slipping on the horizontal $xy$-plane, with its plane always vertical. A convenient set of coordinates is
\[
(x,y,\theta,\phi),
\]
where $(x,y)$ gives the position of the disk’s center, $\theta$ gives the direction of the axis of the disk relative to the $x$-axis, and $\phi$ is the rotation angle of the disk about its own axis.

>  The angle $\phi$ is necessary because rolling without slipping relates translation to rotation. The speed of the center must equal the rim speed $a\dot\phi$. Without $\phi$, one could not distinguish rolling from sliding. 

![](Goldstein/images/d173e4e71f42702b86aef3556dc384a59bcef14e4f6cb81286d4d331e24f2245.jpg)  
**Figure 1.5** Vertical disk rolling on a horizontal plane.

As a result of the constraint the velocity of the center of the disk, $v$, has a magnitude proportional to $\dot\phi$,

$$
v = a\,\dot\phi,
$$

where $a$ is the radius of the disk, and its direction is perpendicular to the axis of the disk:

$$
\dot x = v\sin\theta, \qquad \dot y = -v\cos\theta.
$$

Combining these conditions, we have two differential equations of constraint:

$$
\begin{aligned}
dx - a\sin\theta\,d\phi &= 0, \\
dy + a\cos\theta\,d\phi &= 0.
\end{aligned}\tag{1.39}
$$

**These constraints cannot be integrated into equations involving only $x,y,\theta,\phi$.** In other words, there is no coordinate relation such as $F(x,y,\theta,\phi)=0$ that is equivalent to the rolling condition. Hence the constraints are nonholonomic. 

> The physical reason is simple: the disk may return to the same position and orientation $(x,y,\theta)$ after following different paths, such as rolling along circles of different radii, while accumulating different values of the rotation angle $\phi$. Thus, $\phi$ is path-dependent and cannot be determined solely from $(x,y,\theta)$.

Thus, nonholonomic constraints may arise either from inequalities, such as boundary constraints, or from nonintegrable differential relations, such as rolling without slipping.

For systems with **holonomic constraints**, the constraint equations can be used to eliminate dependent coordinates. This reduces the number of independent variables, so such problems can be treated systematically using the standard Lagrange equations. For **nonholonomic constraints**, there is no equally general method. Each problem often requires special treatment. Therefore, unless stated otherwise, we will consider only **holonomic systems** from now on.

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

 Consider a pendulum suspended from the roof of a car that is being forced to accelerate with fixed acceleration $a$, as shown in Figure 7.4. The position of the bob relative to the ground is

$$
\mathbf r \equiv (x,y) = \bigl(l\sin\phi + \tfrac{1}{2}at^2,\; l\cos\phi\bigr) = \mathbf r(\phi,t).
$$

![](images/ac28ad29bb5df306da86418e17d3a4b91c76862be8cb3a871fa88ff7a03cef01.jpg)  
*Figure 7.4 A pendulum is suspended from the roof of a railroad car that is being forced to accelerate with a fixed, known acceleration $a$.*

Here the relation between $\mathbf r$ and the generalized coordinate $\phi$ depends explicitly on $t$.

A set of coordinates is called **natural** (自然坐标) if the relation $\mathbf r_\alpha(q_1,\dots,q_n)$ between Cartesian and generalized coordinates does not involve time.  In such coordinates, the **kinetic energy** has especially simple properties; in particular, it is a **homogeneous quadratic function of the generalized velocities**. These properties do not generally hold when the transformation depends explicitly on time.

> Suppose the position of particle $\alpha$ is written in generalized coordinates as
>
> $\mathbf r_\alpha=\mathbf r_\alpha(q_1,\dots,q_n),$
>
> with no explicit time dependence. Then by the chain rule,
>
> $\dot{\mathbf r}_\alpha = \sum_i \frac{\partial \mathbf r_\alpha}{\partial q_i}\dot q_i .$
>
> The kinetic energy is
>
> $T = \frac12\sum_\alpha m_\alpha \dot{\mathbf r}_\alpha\cdot \dot{\mathbf r}_\alpha .$
>
> Substitute the expression for $\dot{\mathbf r}_\alpha$:
>
> $T = \frac12\sum_\alpha m_\alpha \left( \sum_i \frac{\partial \mathbf r_\alpha}{\partial q_i}\dot q_i \right) \cdot \left( \sum_j \frac{\partial \mathbf r_\alpha}{\partial q_j}\dot q_j \right).$
>
> Expanding the dot product gives
>
> $T = \frac12\sum_\alpha m_\alpha \sum_{i,j} \left( \frac{\partial \mathbf r_\alpha}{\partial q_i} \cdot \frac{\partial \mathbf r_\alpha}{\partial q_j} \right) \dot q_i\dot q_j .$
>
> Rearranging the sums,
>
> $T = \frac12 \sum_{i,j} \left[ \sum_\alpha m_\alpha \frac{\partial \mathbf r_\alpha}{\partial q_i} \cdot \frac{\partial \mathbf r_\alpha}{\partial q_j} \right] \dot q_i\dot q_j .$
>
> Therefore,
>
> $T= \frac12\sum_{i,j} a_{ij}(q)\dot q_i\dot q_j,$
>
> where
>
> $\boxed{ a_{ij}(q) = \sum_\alpha m_\alpha \frac{\partial \mathbf r_\alpha}{\partial q_i} \cdot \frac{\partial \mathbf r_\alpha}{\partial q_j} }$
>
> is the coefficient of the quadratic kinetic-energy form.
>
> So $a_{ij}(q)$ is essentially a **mass-weighted metric coefficient** in generalized coordinates. It depends only on the coordinates $q_i$, not on the velocities $\dot q_i$. Also, $a_{ij}=a_{ji},$ because the dot product is symmetric.
>
> If the transformation depends explicitly on time, then $\dot{\mathbf r}_\alpha = \sum_i \frac{\partial \mathbf r_\alpha}{\partial q_i}\dot q_i + \frac{\partial \mathbf r_\alpha}{\partial t},$ and the kinetic energy may contain terms linear in $\dot q_i$ and terms independent of $\dot q_i$. Thus the convenient quadratic form no longer generally applies.



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

One of the principal advantages of the Lagrangian formulation is that the **Euler–Lagrange equations retain exactly the same form in any choice of generalized coordinates**:

$$
\boxed{ \frac{d}{dt}\left(\frac{\partial L}{\partial \dot q_i}\right) - \frac{\partial L}{\partial q_i} = 0, \qquad i = 1, \dots, n. }
$$

Moreover, the **forces of constraint**, such as tension in a string, the normal force from a surface, or interatomic forces in a rigid body, do not appear in these equations, provided the constraints are holonomic and the non-constraint forces are derivable from a potential energy $V$. This is a tremendous simplification, because constraint forces are usually unknown and we usually do not want to know them anyway.

------





### 8.4 Form Invariance of the Euler–Lagrange Equations

One of the most powerful features of the Lagrangian formalism is that the Euler–Lagrange equations retain the **same form in any coordinate system**. This is sometimes called the **covariance** of Lagrange's equations. In this section we give an explicit proof of this statement.

For a system of $N$ particles we can collect the $n = 3N$ Cartesian coordinates into a single list $x^A$ with $A = 1,\dots,n$:
$$
x^A = (x_1, y_1, z_1, \dots, x_N, y_N, z_N).
$$
The Lagrangian is a function $\mathcal L(x^A, \dot x^A)$ and the Euler–Lagrange equations read
$$
\frac{d}{dt}\left(\frac{\partial \mathcal L}{\partial \dot x^A}\right) - \frac{\partial \mathcal L}{\partial x^A} = 0,
\qquad A = 1,\dots,n.
$$

Now introduce a new set of coordinates $q_i$ ($i = 1,\dots,n$) related to the old ones by
$$
q_i = q_i(x^1, \dots, x^n, t),
$$
where we allow for an explicit time dependence. For this to be a valid coordinate system we must be able to invert the relation, which requires a nonvanishing Jacobian determinant:
$$
\det\!\left(\frac{\partial x^A}{\partial q_i}\right) \neq 0.
$$

By the chain rule,
$$
\dot q_i = \frac{\partial q_i}{\partial x^A}\,\dot x^A + \frac{\partial q_i}{\partial t},
\qquad
\dot x^A = \frac{\partial x^A}{\partial q_i}\,\dot q_i + \frac{\partial x^A}{\partial t},
$$
where the summation convention is used (sum over repeated $A$ or $i$).

We substitute $x^A(q_j,t)$ into the Lagrangian to obtain a new function $\mathcal L(q_i,\dot q_i,t)$ and ask whether the Euler–Lagrange equations take the same form in the $q_i$ coordinates.

---

**Proof.** Using the chain rule, the derivative of $\mathcal L$ with respect to a new coordinate $q_i$ is

$$
\frac{\partial \mathcal L}{\partial q_i}
= \frac{\partial \mathcal L}{\partial x^A}\frac{\partial x^A}{\partial q_i}
+ \frac{\partial \mathcal L}{\partial \dot x^A}
\left(
\frac{\partial^2 x^A}{\partial q_i\,\partial q_j}\,\dot q_j
+ \frac{\partial^2 x^A}{\partial q_i\,\partial t}
\right).
$$

Meanwhile, differentiating the relation $\dot x^A = (\partial x^A/\partial q_i)\dot q_i + \partial x^A/\partial t$ with respect to $\dot q_i$ gives

$$
\frac{\partial \dot x^A}{\partial \dot q_i} = \frac{\partial x^A}{\partial q_i},
$$

so that

$$
\frac{\partial \mathcal L}{\partial \dot q_i}
= \frac{\partial \mathcal L}{\partial \dot x^A}\frac{\partial x^A}{\partial q_i}.
$$

Taking the total time derivative of the above expression,

$$
\frac{d}{dt}\left(\frac{\partial \mathcal L}{\partial \dot q_i}\right)
= \frac{d}{dt}\left(\frac{\partial \mathcal L}{\partial \dot x^A}\right)\frac{\partial x^A}{\partial q_i}
+ \frac{\partial \mathcal L}{\partial \dot x^A}
\left(
\frac{\partial^2 x^A}{\partial q_i\,\partial q_j}\,\dot q_j
+ \frac{\partial^2 x^A}{\partial q_i\,\partial t}
\right).
$$

Subtracting the two results, the second-order terms cancel identically, leaving the elegant result

$$
\frac{d}{dt}\left(\frac{\partial \mathcal L}{\partial \dot q_i}\right) - \frac{\partial \mathcal L}{\partial q_i}
= \left[
\frac{d}{dt}\left(\frac{\partial \mathcal L}{\partial \dot x^A}\right) - \frac{\partial \mathcal L}{\partial x^A}
\right]\frac{\partial x^A}{\partial q_i}.
$$

The quantity in brackets on the right-hand side is the Euler–Lagrange expression in the $x^A$ coordinates. Because the Jacobian matrix $\partial x^A/\partial q_i$ is invertible, we conclude:

> **If the Euler–Lagrange equations vanish in the $x^A$ coordinate system, then they also vanish in the $q_i$ coordinate system, and conversely.**

Thus the Euler–Lagrange equations are **form invariant**: they take exactly the same shape

$$
\boxed{
\frac{d}{dt}\left(\frac{\partial \mathcal L}{\partial \dot q_i}\right) - \frac{\partial \mathcal L}{\partial q_i} = 0,
\qquad i = 1,\dots,n
}
$$

in any choice of generalized coordinates.

---

**Generalized momentum.** In complete analogy with the Cartesian momentum $p_A = \partial \mathcal L/\partial \dot x^A$, we define the **generalized momentum** conjugate to $q_i$ by

$$
p_i = \frac{\partial \mathcal L}{\partial \dot q_i}.
$$

In terms of $p_i$, the Euler–Lagrange equation becomes simply

$$
\dot p_i = \frac{\partial \mathcal L}{\partial q_i}.
$$

Whenever $\mathcal L$ does not depend explicitly on a particular coordinate $q_i$, the corresponding momentum $p_i$ is conserved. We shall explore this connection between symmetries and conservation laws systematically in Section 9.

### 8.5 Why Lagrange's Equations Work for Constrained Systems

It is essential to understand why the same Euler–Lagrange equations continue to hold for constrained systems. The key is Hamilton's principle combined with the nature of constraint forces. To keep the derivation reasonably simple, we consider a single particle in three dimensions constrained by holonomic constraints to move on a surface (two degrees of freedom). The generalization to arbitrary numbers of particles is straightforward — the main ideas are all present here.

#### Setup: two kinds of forces

Consider a particle constrained to move on a fixed surface. There are two kinds of forces acting on the particle:

1. **Forces of constraint** $\mathbf F_{\text{cstr}}$: the normal force of the surface (for a bead on a wire, the normal force of the wire; for the atoms in a rigid body, the interatomic forces that hold the atoms in place). These are not necessarily conservative, but this does not matter. One of the objectives of the Lagrangian approach is to find equations that do not involve the constraining forces, which we usually do not want to know anyway.

2. **Non-constraint forces** $\mathbf F$: gravity, springs, and any other applied forces. We assume these satisfy at least the second condition for conservatism, so they are derivable from a potential energy $U(\mathbf r,t)$:

$$
\mathbf F = -\nabla U(\mathbf r,t).
$$

(If all non-constraint forces are actually conservative, then $U$ is independent of $t$, but we do not need to assume this.)

The total force on the particle is therefore

$$
\mathbf F_{\text{tot}} = \mathbf F_{\text{cstr}} + \mathbf F.
$$

We define the Lagrangian, as usual, using **only** the non-constraint potential:

$$
\mathcal L = T - U = \frac12 m\dot{\mathbf r}^2 - U(\mathbf r,t).
$$

Since $U$ is the potential energy for the non-constraint forces only, this definition of $\mathcal L$ excludes the constraint forces. This correctly reflects that Lagrange's equations for a constrained system cleverly eliminate the constraint forces, as we shall see.

#### The action integral is stationary at the right path

Consider any two fixed points on the surface, $\mathbf r_1$ and $\mathbf r_2$, through which the particle passes at times $t_1$ and $t_2$. We denote by $\mathbf r(t)$ the **right path** — the actual path the particle follows — and by $\mathbf R(t)$ any neighboring **wrong path** between the same two points, also lying in the surface. It is convenient to write

$$
\mathbf R(t) = \mathbf r(t) + \boldsymbol\epsilon(t),
$$

which defines $\boldsymbol\epsilon(t)$ as the infinitesimal vector pointing from the right path to the wrong path. Because both endpoints lie in the surface, $\boldsymbol\epsilon(t)$ is contained in (tangent to) the surface, and since both paths pass through the same endpoints,

$$
\boldsymbol\epsilon(t_1) = \boldsymbol\epsilon(t_2) = \mathbf 0.
$$

Let us denote by $S$ the action integral taken along any path $\mathbf R(t)$ lying in the constraining surface,

$$
S = \int_{t_1}^{t_2} \mathcal L(\mathbf R, \dot{\mathbf R}, t)\,dt,
$$

and by $S_0$ the corresponding integral taken along the right path $\mathbf r(t)$. We now prove that $S$ is stationary for variations about the right path, i.e. that the difference

$$
\delta S = S - S_0
$$

is zero to first order in $\boldsymbol\epsilon$.

The difference $\delta S$ is the integral of the difference between the Lagrangians on the two paths,

$$
\delta\mathcal L = \mathcal L(\mathbf R, \dot{\mathbf R}, t) - \mathcal L(\mathbf r, \dot{\mathbf r}, t).
$$

Substituting $\mathbf R = \mathbf r + \boldsymbol\epsilon$ and using $\mathcal L = \frac12 m\dot{\mathbf r}^2 - U(\mathbf r,t)$, this becomes

$$
\begin{aligned}
\delta\mathcal L &= \frac12 m\bigl[(\dot{\mathbf r} + \dot{\boldsymbol\epsilon})^2 - \dot{\mathbf r}^2\bigr] - \bigl[U(\mathbf r + \boldsymbol\epsilon,t) - U(\mathbf r,t)\bigr] \\
&= m\dot{\mathbf r}\cdot\dot{\boldsymbol\epsilon} - \boldsymbol\epsilon\cdot\nabla U + O(\boldsymbol\epsilon^2),
\end{aligned}
$$

where $O(\boldsymbol\epsilon^2)$ denotes terms involving squares and higher powers of $\boldsymbol\epsilon$ and $\dot{\boldsymbol\epsilon}$. Returning to the difference in the two action integrals, we find that, to first order in $\boldsymbol\epsilon$,

$$
\delta S = \int_{t_1}^{t_2} \delta\mathcal L\,dt = \int_{t_1}^{t_2}\bigl[m\dot{\mathbf r}\cdot\dot{\boldsymbol\epsilon} - \boldsymbol\epsilon\cdot\nabla U\bigr]\,dt.\tag{8.1}
$$

The first term can be integrated by parts (moving the time derivative from $\dot{\boldsymbol\epsilon}$ to $m\dot{\mathbf r}$ and changing the sign). Because $\boldsymbol\epsilon$ vanishes at the two endpoints, the boundary term is zero, and we obtain

$$
\int_{t_1}^{t_2} m\dot{\mathbf r}\cdot\dot{\boldsymbol\epsilon}\,dt = -\int_{t_1}^{t_2} \boldsymbol\epsilon\cdot m\ddot{\mathbf r}\,dt.
$$

Therefore Eq. (8.1) becomes

$$
\delta S = -\int_{t_1}^{t_2} \boldsymbol\epsilon\cdot\bigl[m\ddot{\mathbf r} + \nabla U\bigr]\,dt.\tag{8.2}
$$

Now, the path $\mathbf r(t)$ is the right path and satisfies Newton's second law:

$$
m\ddot{\mathbf r} = \mathbf F_{\text{tot}} = \mathbf F_{\text{cstr}} + \mathbf F.
$$

Meanwhile $\nabla U = -\mathbf F$. Substituting these into the bracket in (8.2),

$$
m\ddot{\mathbf r} + \nabla U = (\mathbf F_{\text{cstr}} + \mathbf F) - \mathbf F = \mathbf F_{\text{cstr}}.
$$

The non-constraint forces cancel exactly! We are left with

$$
\delta S = -\int_{t_1}^{t_2} \boldsymbol\epsilon\cdot\mathbf F_{\text{cstr}}\,dt.\tag{8.3}
$$

But the constraint force $\mathbf F_{\text{cstr}}$ is **normal** to the surface (that is the defining property of the normal force), while the variation $\boldsymbol\epsilon$ lies **in** (tangent to) the surface. Therefore

$$
\boldsymbol\epsilon\cdot\mathbf F_{\text{cstr}} = 0,
$$

and we have proved that

$$
\boxed{\delta S = 0}.
$$

The action integral is stationary at the right path, as claimed. The crucial ingredient was that the constraint force does no virtual work: it is perpendicular to any displacement consistent with the constraint.

#### From Hamilton's principle to Lagrange's equations

We have proved Hamilton's principle for the constrained system, but with an important caveat: the proof holds only for variations **consistent with the constraints** — paths that lie in the surface. This means we **cannot** prove Lagrange's equations with respect to the three Cartesian coordinates $(x,y,z)$, because varying $x$, $y$, or $z$ independently would take the path off the surface.

However, we **can** prove them with respect to the appropriate generalized coordinates. Because the particle is confined to a two-dimensional surface, it has two degrees of freedom and can be described by two generalized coordinates, $q_1$ and $q_2$, that can be varied independently. Any variation of $q_1$ and $q_2$ is automatically consistent with the constraints.

Accordingly, we rewrite the action integral in terms of $q_1$ and $q_2$:

$$
S = \int_{t_1}^{t_2} \mathcal L(q_1,q_2,\dot q_1,\dot q_2,t)\,dt,
$$

and this integral is stationary for any independent variations of $q_1$ and $q_2$ about the correct path. Therefore, by the calculus of variations, the correct path must satisfy the two Euler–Lagrange equations:

$$
\frac{\partial\mathcal L}{\partial q_1} = \frac{d}{dt}\frac{\partial\mathcal L}{\partial\dot q_1}\qquad\text{and}\qquad
\frac{\partial\mathcal L}{\partial q_2} = \frac{d}{dt}\frac{\partial\mathcal L}{\partial\dot q_2}.
$$

#### General result

The proof above applies directly to a single particle constrained to a surface, but the main ideas carry over to the general case: for any holonomic system with $n$ degrees of freedom and $n$ generalized coordinates $q_1,\dots,q_n$, with non-constraint forces derivable from a potential energy $U(q_1,\dots,q_n,t)$, the path followed by the system is determined by the $n$ Lagrange equations

$$
\boxed{ \frac{\partial\mathcal L}{\partial q_i} = \frac{d}{dt}\frac{\partial\mathcal L}{\partial\dot q_i},\qquad i = 1,\dots,n, }
$$

where $\mathcal L = T - U$ and $U$ is the total potential energy of all forces **excluding** the forces of constraint.

It was essential to this proof that the non-constraint forces be derivable from a potential, $\mathbf F = -\nabla U$. If this is not true, Lagrange's equations may not hold in the simple form above. An obvious example is sliding friction: it is not a force of constraint (it is not normal to the surface) and cannot be derived from a potential energy. Thus, when sliding friction is present, Lagrange's equations in the form above do not apply.

> **Important:** The action is stationary only for variations *consistent with the constraints*. This means we cannot prove Lagrange's equations with respect to the Cartesian coordinates $x,y,z$ when a constraint is present. However, we *can* prove them with respect to the generalized coordinates $q_1,q_2$, because any variation of $q_1$ and $q_2$ is automatically consistent with the constraints.

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

