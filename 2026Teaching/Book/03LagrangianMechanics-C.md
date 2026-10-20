# Lagrangian Mechanics (Part C)

**Reading material:** Chapter 4 of *Introduction to Classical Mechanics* by Thomas A. Helliwell; Chapter 7 of *Classical Mechanics* by John R. Taylor; Chapter 7 of *Classical Mechanics* by David Tong

## Table of Contents

1. [Generalized Momentum and Cyclic Coordinates](#1-generalized-momentum-and-cyclic-coordinates)
   - [1.1 Generalized Momentum](#11-generalized-momentum)
   - [1.2 Cyclic Coordinates and Conservation Laws](#12-cyclic-coordinates-and-conservation-laws)
2. [The Hamiltonian](#2-the-hamiltonian)
   - [2.1 Definition of the Hamiltonian](#21-definition-of-the-hamiltonian)
   - [2.2 Conservation of the Hamiltonian](#22-conservation-of-the-hamiltonian)
   - [2.3 When the Hamiltonian Equals Total Energy](#23-when-the-hamiltonian-equals-total-energy)
3. [Example: Bead on a Rotating Parabolic Wire](#3-example-bead-on-a-rotating-parabolic-wire)
   - [3.1 Choosing the Generalized Coordinate](#31-choosing-the-generalized-coordinate)
   - [3.2 Equation of Motion](#32-equation-of-motion)
   - [3.3 The Hamiltonian and the Energy](#33-the-hamiltonian-and-the-energy)
   - [3.4 An Effective Potential](#34-an-effective-potential)
   - [3.5 Rethinking the Generalized-Coordinate Theorem](#35-rethinking-the-generalized-coordinate-theorem)
4. [When the Hamiltonian is Not the Total Energy](#4-when-the-hamiltonian-is-not-the-total-energy)
   - [4.1 The General Condition $H \neq E$](#41-the-general-condition-h-neq-e)
   - [4.2 Summary](#42-summary)

---

## 1. Generalized Momentum and Cyclic Coordinates

In our development of Lagrangian mechanics, the quantities $\partial L/\partial q_i$ and $\partial L/\partial \dot q_i$ have appeared repeatedly. We now give them names and explore their physical significance. The derivative $\partial L/\partial q_i$ plays a role analogous to a force, while $\partial L/\partial \dot q_i$ plays a role analogous to a momentum. This observation leads directly to powerful **conservation laws** that are often easier to spot in the Lagrangian formalism than in Newtonian mechanics.

------

### 1.1 Generalized Momentum

For a system with $n$ generalized coordinates $q_1,\dots,q_n$, we define the **generalized momentum** (广义动量) conjugate to $q_i$ by

$$
p_i = \frac{\partial L}{\partial \dot q_i}.
$$

With this definition, the Euler–Lagrange equation becomes simply

$$
\dot p_i = \frac{\partial L}{\partial q_i}.
$$

In words: the rate of change of the generalized momentum equals the generalized force. This is the Lagrangian analogue of Newton's second law $\dot{\mathbf p} = \mathbf F$.

> **Example: Cartesian coordinates.** For a single particle in Cartesian coordinates with $L = \tfrac12 m(\dot x^2+\dot y^2+\dot z^2) - U(x,y,z)$, we have $p_x = m\dot x$, which is exactly the ordinary momentum.

> **Example: Polar coordinates.** For a particle in two dimensions with $L = \tfrac12 m(\dot r^2 + r^2\dot\phi^2) - U(r,\phi)$, the generalized momenta are
> $$
> p_r = \frac{\partial L}{\partial\dot r} = m\dot r, \qquad p_\phi = \frac{\partial L}{\partial\dot\phi} = mr^2\dot\phi.
> $$
> The radial momentum $p_r$ is the ordinary linear momentum in the radial direction, while $p_\phi$ is the **angular momentum** about the origin. This illustrates an important point: the generalized momentum need not have the dimensions of ordinary momentum.

The generalized momentum is a central concept because it connects symmetries of the Lagrangian to conservation laws, as we shall see next.

------

### 1.2 Cyclic Coordinates and Conservation Laws

A coordinate $q_i$ is said to be **cyclic** (循环坐标) or **ignorable** (可忽略坐标) if the Lagrangian does not depend on it explicitly:

$$
\frac{\partial L}{\partial q_i} = 0.
$$

The term "cyclic" comes from the observation that in many problems (such as central-force motion) the ignorable coordinate is an angle that describes a periodic, or cyclic, motion. The term "ignorable" is equally apt: if a coordinate does not appear in $L$, we can partly ignore it when solving the equations of motion, because its conjugate momentum is immediately known.

**Conservation law.** If $q_i$ is cyclic, then the Euler–Lagrange equation gives

$$
\dot p_i = \frac{\partial L}{\partial q_i} = 0,
$$

so the corresponding generalized momentum is **conserved**:

$$
\boxed{p_i = \text{constant}.}
$$

This result is one of the great practical advantages of the Lagrangian formalism: once we have identified a cyclic coordinate, we immediately know a constant of the motion without solving any differential equations.

> **Example: Projectile motion.** For a projectile with $L = \tfrac12m(\dot x^2+\dot y^2+\dot z^2) - mgz$, the Lagrangian is independent of $x$ and $y$. Thus $p_x = m\dot x$ and $p_y = m\dot y$ are conserved, namely the horizontal components of linear momentum.

> **Example: Central potential.** For a particle in a central potential $U(r)$, using polar coordinates gives $L = \tfrac12m(\dot r^2+r^2\dot\phi^2) - U(r)$. The coordinate $\phi$ is cyclic, so $p_\phi = mr^2\dot\phi = L$ (angular momentum) is conserved.

> **Example: Two-body problem.** In the two-body problem, the centre-of-mass coordinate $\mathbf R$ appears in the Lagrangian with only a kinetic term. Hence each component of $\mathbf R$ is cyclic, and the total linear momentum $\mathbf P = (m_1+m_2)\dot{\mathbf R}$ is conserved.

The connection between cyclic coordinates and conserved momenta is the simplest manifestation of a much deeper result known as **Noether's theorem** (诺特定理), which states that **every continuous symmetry of the Lagrangian gives rise to a conserved quantity**. Translational invariance leads to momentum conservation, rotational invariance leads to angular momentum conservation, and—as we shall see in the next section—invariance under time translation leads to energy conservation.

------

## 2. The Hamiltonian

We have seen that when the Lagrangian does not depend on a particular coordinate, the corresponding momentum is conserved. It is natural to ask what happens when the Lagrangian does not depend **explicitly** on time. This question leads us to the **Hamiltonian** (哈密顿量), a quantity that is not only a constant of motion in many systems, but also serves as the foundation for an entirely different formulation of mechanics.

------

### 2.1 Definition of the Hamiltonian

For a system with Lagrangian $L(q_1,\dots,q_n,\dot q_1,\dots,\dot q_n,t)$, we define the **Hamiltonian** by

$$
\boxed{H = \sum_{i=1}^n p_i\,\dot q_i - L,}
\tag{2.1}
$$

where $p_i = \partial L/\partial\dot q_i$ are the generalized momenta. When we write $H(q,p,t)$, we mean that $H$ is to be regarded as a function of the coordinates $q_i$, the momenta $p_i$, and possibly time. This is in contrast to the Lagrangian $L(q,\dot q,t)$, which is a function of coordinates and velocities.

In practice, one first computes the momenta $p_i$ from the Lagrangian, then evaluates the right-hand side of (2.1). The resulting expression usually still contains velocities; the final step is to invert the relations $p_i = \partial L/\partial\dot q_i$ to express $\dot q_i$ in terms of $q_j$ and $p_j$, so that $H$ becomes a function purely of $(q,p,t)$.

> **Example: Particle in a potential.** For a single particle with $L = \tfrac12m\dot{\mathbf r}^2 - U(\mathbf r)$, the momentum is $\mathbf p = m\dot{\mathbf r}$. The Hamiltonian is
> $$
> H = \mathbf p\cdot\dot{\mathbf r} - L = \mathbf p\cdot\frac{\mathbf p}{m} - \left(\frac{\mathbf p^2}{2m} - U\right) = \frac{\mathbf p^2}{2m} + U(\mathbf r).
> $$
> This is exactly the total energy, expressed as a function of position and momentum.



> **Example: Harmonic oscillator.**
>  Consider a one-dimensional harmonic oscillator with coordinate $x$, mass $m$, and spring constant $k$. Its Lagrangian is
> \[
> L(x,\dot x)=\frac{1}{2}m\dot x^2-\frac{1}{2}kx^2.
> \]
> The generalized momentum conjugate to $x$ is
> \[
> p=\frac{\partial L}{\partial \dot x}=m\dot x.
> \]
> Therefore, $\dot x=\frac{p}{m}.$
>
> The Hamiltonian is defined by $H=p\dot x-L.$
>
> Substituting $\dot x=p/m$, we get
> \[
> H=p\frac{p}{m}-\left(\frac{1}{2}m\left(\frac{p}{m}\right)^2-\frac{1}{2}kx^2\right).
> \]
> Thus,
> \[
> \boxed{H(x,p)=\frac{p^2}{2m}+\frac{1}{2}kx^2.}
> \]
> This is the total energy of the harmonic oscillator, written as a function of position $x$ and momentum $p$.

> **Example: Charged particle in an electromagnetic field.**  
> Consider a particle of mass \(m\) and charge \(e\) moving in electromagnetic potentials \(\phi(\mathbf r,t)\) and \(\mathbf A(\mathbf r,t)\). The Lagrangian is
>
> \[
> L(\mathbf r,\dot{\mathbf r},t)
> =
> \frac{1}{2}m\dot{\mathbf r}^{\,2}
> +
> e\,\dot{\mathbf r}\cdot \mathbf A(\mathbf r,t)
> -
> e\,\phi(\mathbf r,t).
> \]
>
> The canonical momentum conjugate to \(\mathbf r\) is
>
> \[
> \mathbf p
> =
> \frac{\partial L}{\partial \dot{\mathbf r}}
> =
> m\dot{\mathbf r}
> +
> e\mathbf A(\mathbf r,t).
> \]
>
> It is now clear that **the momentum contains not only the mechanical momentum \(m\dot{\mathbf r}\), but also an additional term \(e\mathbf A\) from the electromagnetic vector potential**.
>
> Therefore,
>
> \[
> \dot{\mathbf r}
> =
> \frac{1}{m}\left[\mathbf p-e\mathbf A(\mathbf r,t)\right].
> \]
>
> The Hamiltonian is defined by
>
> \[
> H
> =
> \mathbf p\cdot \dot{\mathbf r}
> -
> L.
> \]
>
> Substituting the Lagrangian, we obtain
>
> \[
> H
> =
> \mathbf p\cdot\dot{\mathbf r}
> -
> \left[
> \frac{1}{2}m\dot{\mathbf r}^{\,2}
> +
> e\dot{\mathbf r}\cdot\mathbf A
> -
> e\phi
> \right].
> \]
>
> Since
>
> \[
> \mathbf p=m\dot{\mathbf r}+e\mathbf A,
> \]
>
> we have
>
> \[
> \mathbf p\cdot\dot{\mathbf r}
> =
> m\dot{\mathbf r}^{\,2}
> +
> e\dot{\mathbf r}\cdot\mathbf A.
> \]
>
> Therefore,
>
> \[
> H
> =
> \frac{1}{2}m\dot{\mathbf r}^{\,2}
> +
> e\phi.
> \]
>
> Finally, expressing the velocity in terms of \(\mathbf p\), we get
>
> \[
> \boxed{
> H(\mathbf r,\mathbf p,t)
> =
> \frac{1}{2m}
> \left[
> \mathbf p-e\mathbf A(\mathbf r,t)
> \right]^2
> +
> e\phi(\mathbf r,t).
> }
> \]
>
> This Hamiltonian describes the motion of a charged particle in electromagnetic fields. The important point is that the canonical momentum is
>
> \[
> \mathbf p=m\dot{\mathbf r}+e\mathbf A,
> \]
>
> not simply the mechanical momentum \(m\dot{\mathbf r}\). Equivalently, the mechanical momentum is
>
> \[
> m\dot{\mathbf r}=\mathbf p-e\mathbf A.
> \]
>
> This distinction is essential in electromagnetism and quantum mechanics. In quantum mechanics, the canonical momentum becomes the operator
>
> \[
> \mathbf p\to -i\hbar\nabla,
> \]
>
> leading to the  Hamiltonian
>
> \[
> \hat H
> =
> \frac{1}{2m}
> \left[
> -i\hbar\nabla-e\mathbf A(\mathbf r,t)
> \right]^2
> +
> e\phi(\mathbf r,t)
> \]
> This is the Hamiltonian in quantum mechanics for a charged particle in an electromagnetic field.

Mathematically, the passage from $L(q,\dot q,t)$ to $H(q,p,t)$ is an example of a **Legendre transform** (勒让德变换). A crucial fact is that this transformation is invertible: given $H$, one can recover $L$ by the reverse transform. We shall explore the Hamiltonian formalism more deeply in a later chapter; for now, our goal is to understand the physical significance of $H$ and the conditions under which it is conserved.

------

### 2.2 Conservation of the Hamiltonian

To discover when the Hamiltonian is conserved, we start from the total time derivative of the Lagrangian itself.  Since $L = L(q_1,\dots,q_n,\dot q_1,\dots,\dot q_n,t)$, the chain rule gives

$$
\frac{dL}{dt} = \sum_{i=1}^n\left(\frac{\partial L}{\partial q_i}\dot q_i + \frac{\partial L}{\partial \dot q_i}\ddot q_i\right) + \frac{\partial L}{\partial t}.
$$

By the Euler–Lagrange equation, the derivative in the first term is

$$
\frac{\partial L}{\partial q_i} = \frac{d}{dt}\frac{\partial L}{\partial \dot q_i} = \dot p_i,
$$

while the derivative in the second term is just the generalized momentum $p_i$.  Hence

$$
\frac{dL}{dt} = \sum_{i=1}^n\bigl(\dot p_i\dot q_i + p_i\ddot q_i\bigr) + \frac{\partial L}{\partial t}.
$$

The quantity in parentheses is itself a total time derivative:

$$
\dot p_i\dot q_i + p_i\ddot q_i = \frac{d}{dt}(p_i\dot q_i).
$$

Therefore

$$
\frac{dL}{dt} = \frac{d}{dt}\left(\sum_{i=1}^n p_i\dot q_i\right) + \frac{\partial L}{\partial t}.
$$

Rearranging, we obtain

$$
\frac{d}{dt}\left(\sum_{i=1}^n p_i\dot q_i - L\right) = -\frac{\partial L}{\partial t}.
$$

The combination in parentheses is precisely the Hamiltonian $H$ defined in (2.1).  Thus

$$
\boxed{\frac{dH}{dt} = -\frac{\partial L}{\partial t}.}
\tag{2.2}
$$

**This is the key result.** If the Lagrangian does not depend explicitly on time — that is, if $\partial L/\partial t = 0$ — then the Hamiltonian is a conserved quantity:

$$
\frac{dH}{dt} = 0 \quad\Longrightarrow\quad H = \text{constant}.
$$

This conservation law is the time-translation counterpart of momentum conservation: just as spatial homogeneity (invariance under $q_i\to q_i+\epsilon$) implies momentum conservation, temporal homogeneity (invariance under $t\to t+\epsilon$) implies Hamiltonian conservation.  Both are instances of Noether's theorem.

------

### 2.3 When the Hamiltonian Equals Total Energy

We now prove the conditions under which the Hamiltonian coincides with the total energy $T+U$. The result depends on whether the generalized coordinates are **natural** (自然坐标), meaning the relation between Cartesian and generalized coordinates does not involve time explicitly.

**Theorem.** Let the Cartesian coordinates of the particles be related to the generalized coordinates by time-independent transformations

$$
\mathbf r_\alpha = \mathbf r_\alpha(q_1,\dots,q_n), \qquad \alpha = 1,\dots,N.
$$

Then the kinetic energy $T$ is a **homogeneous quadratic function** of the generalized velocities, and the Hamiltonian equals the total energy:

$$
\boxed{H = T + U.}
\tag{2.3}
$$

**Proof.** Differentiating the coordinate transformation with respect to time gives

$$
\dot{\mathbf r}_\alpha = \sum_{i=1}^n \frac{\partial\mathbf r_\alpha}{\partial q_i}\,\dot q_i.
$$

The kinetic energy is

$$
T = \frac12\sum_\alpha m_\alpha\dot{\mathbf r}_\alpha\cdot\dot{\mathbf r}_\alpha
= \frac12\sum_{i,j}\left(\sum_\alpha m_\alpha\frac{\partial\mathbf r_\alpha}{\partial q_i}\cdot\frac{\partial\mathbf r_\alpha}{\partial q_j}\right)\dot q_i\dot q_j
= \frac12\sum_{i,j} A_{ij}(q)\,\dot q_i\dot q_j,
$$

where $A_{ij}(q)$ depends only on the coordinates, not on the velocities. Thus $T$ is a homogeneous quadratic form in the $\dot q_i$.

Because the potential energy $U$ does not depend on velocities, the generalized momentum is

$$
p_i = \frac{\partial L}{\partial\dot q_i} = \frac{\partial T}{\partial\dot q_i} = \sum_j A_{ij}\,\dot q_j.
$$

Now form the sum that appears in the definition of $H$:

$$
\sum_{i=1}^n p_i\,\dot q_i = \sum_{i,j} A_{ij}\,\dot q_i\dot q_j = 2T,
$$

where the last equality follows because $T = \tfrac12\sum_{i,j}A_{ij}\dot q_i\dot q_j$. Therefore

$$
H = \sum_i p_i\dot q_i - L = 2T - (T-U) = T + U.
$$

This completes the proof. ∎

> **Alternative viewpoint: Euler's theorem.** The result $\sum_i \dot q_i\,(\partial T/\partial\dot q_i) = 2T$ is a direct consequence of **Euler's theorem for homogeneous functions** (欧拉齐次函数定理): if $f(x_1,\dots,x_n)$ is a homogeneous function of degree $k$, then $\sum_i x_i\,(\partial f/\partial x_i) = kf$. Since $T$ is quadratic in the velocities ($k=2$), the theorem immediately gives $\sum_i \dot q_i\,(\partial T/\partial\dot q_i) = 2T$, bypassing the explicit $A_{ij}$ calculation.

> **Summary of conditions.** We have established two distinct results:
>
> 1. $H$ is conserved if and only if $\partial L/\partial t = 0$ (or equivalently $\partial H/\partial t = 0$).
> 2. $H = T+U$ if and only if the coordinate transformation is time-independent.
>
> When *both* conditions hold—namely, the Lagrangian has no explicit time dependence *and* the coordinates are natural—then the total mechanical energy $E = T+U$ is conserved.

------

## 3. Example: Bead on a Rotating Parabolic Wire

We now examine a system in which the **Hamiltonian** (哈密顿量) is conserved but is *not* equal to the total mechanical energy.  This example will motivate the more general discussion in the next section.

> Here is a simple comparison table:
>
> | Coordinate system | Coordinates       | Meaning                                                      |
> | ----------------- | ----------------- | ------------------------------------------------------------ |
> | **Cartesian**     | $(x,y,z)$         | Position described by three perpendicular axes               |
> | **Cylindrical**   | $(\rho,\phi,z)$   | Position described by distance from the $z$-axis, angle around the $z$-axis, and height |
> | **Spherical**     | $(r,\theta,\phi)$ | Position described by distance from origin, polar angle, and azimuthal angle |
>

Suppose we bend a wire into the shape of a vertically oriented parabola defined in cylindrical coordinates by
$$
z = \alpha\rho^2,
$$

where $z$ is the vertical coordinate and $\rho$ is the distance from the axis of symmetry.  Using a synchronous motor, we force the wire to spin at constant angular velocity $\omega$ about its symmetry axis.  A bead of mass $m$ slides without friction along the wire, as illustrated in Figure 1.

![
](Helliwell/images/91b9124fbe12ffd6ded9d1e32d06b2ae904d8f8a3b97801b0121a79fb6397a71.jpg)
**Figure 1**: A bead slides without friction on a vertically oriented parabolic wire forced to spin about its axis of symmetry.

>  Here the bead is constrained to remain on the parabolic wire, so $z-\alpha\rho^2=0$, and it is also forced to rotate with the wire, so $\phi-\omega t=0$. The first constraint is independent of time and is therefore **scleronomic (定常约束）**, while the second contains time explicitly and is therefore **rheonomic （非定常约束）**. Physically, this time dependence reflects the fact that the wire is being driven by an external motor, so the constraint surface itself is moving in space and can therefore do work on the bead.

------

### 3.1 Choosing the Generalized Coordinate

The bead moves in three dimensions, but the wire imposes two constraints: the parabolic shape $z = \alpha\rho^2$ and the forced rotation $\dot{\phi} = \omega$.  Hence there is only **one degree of freedom**.  A convenient choice of **generalized coordinate** (广义坐标) is the cylindrical radius $\rho$; once $\rho$ is known, both $z$ and $\phi$ are determined.

In cylindrical coordinates the square of the velocity is

$$
v^2 = \dot{\rho}^2 + \rho^2\dot{\phi}^2 + \dot{z}^2
     = \dot{\rho}^2 + \rho^2\omega^2 + (2\alpha\rho\dot{\rho})^2,
$$

where we have used $\dot{\phi} = \omega = \text{constant}$ and $z = \alpha\rho^2$, which gives $\dot{z} = 2\alpha\rho\dot{\rho}$.  The gravitational potential energy is $U = mgz = mg\alpha\rho^2$, so the **Lagrangian** is

$$
\boxed{
L = T - U = \frac{1}{2}m\Bigl[\bigl(1 + 4\alpha^2\rho^2\bigr)\dot{\rho}^2 + \rho^2\omega^2\Bigr] - mg\alpha\rho^2.
}
\tag{3.1}
$$

The contact force that keeps the bead on the wire is the normal force associated with these two constraints.  We do not include its contribution in the Lagrangian, because its net energetic effect will be accounted for automatically through the constraints.

------

### 3.2 Equation of Motion

The partial derivatives of $L$ are straightforward:

$$
\frac{\partial L}{\partial\rho}
= m\bigl(4\alpha^2\rho\,\dot{\rho}^2 + \rho\omega^2 - 2g\alpha\rho\bigr),
\qquad
\frac{\partial L}{\partial\dot{\rho}}
= m(1 + 4\alpha^2\rho^2)\,\dot{\rho}.
$$

The Euler–Lagrange equation gives

$$
m\bigl[4\alpha^2\rho\,\dot{\rho}^2 + \rho\omega^2 - 2g\alpha\rho\bigr]
- m\frac{d}{dt}\Bigl[(1 + 4\alpha^2\rho^2)\,\dot{\rho}\Bigr] = 0,
$$

which simplifies to the second-order equation of motion

$$
\bigl(1 + 4\alpha^2\rho^2\bigr)\ddot{\rho}
+ 4\alpha^2\rho\,\dot{\rho}^2
+ (2g\alpha - \omega^2)\rho = 0.
\tag{3.2}
$$

The coordinate $\rho$ is **not cyclic**, so the corresponding generalized momentum $p_\rho = \partial L/\partial\dot{\rho}$ is not conserved.  However, notice that $L$ does **not** depend explicitly on time: $\partial L/\partial t = 0$.  Therefore the **Hamiltonian** must be conserved, giving us a useful first integral of motion.

------

### 3.3 The Hamiltonian and the Energy

The generalized momentum is

$$
p_\rho = \frac{\partial L}{\partial\dot{\rho}} = m(1 + 4\alpha^2\rho^2)\,\dot{\rho}.
$$

The Hamiltonian is

$$
\begin{aligned}
H &= \dot{\rho}\,p_\rho - L \\
  &= m(1 + 4\alpha^2\rho^2)\dot{\rho}^2
     - \frac{1}{2}m\Bigl[(1 + 4\alpha^2\rho^2)\dot{\rho}^2 + \rho^2\omega^2\Bigr]
     + mg\alpha\rho^2 \\
  &= \frac{1}{2}m\Bigl[(1 + 4\alpha^2\rho^2)\dot{\rho}^2 - \rho^2\omega^2\Bigr]
     + mg\alpha\rho^2.
\end{aligned}
\tag{3.3}
$$

Because $\partial L/\partial t = 0$, this quantity is a **constant of the motion**.

Let us compare $H$ with the total mechanical energy $E = T + U$:

$$
E = T + U = \frac{1}{2}m\Bigl[\bigl(1 + 4\alpha^2\rho^2\bigr)\dot{\rho}^2 + \rho^2\omega^2\Bigr] + mg\alpha\rho^2.
\tag{3.4}
$$

Subtracting (3.3) from (3.4), we find

$$
\boxed{H - E = -m\rho^2\omega^2.}
\tag{3.5}
$$

**This difference is nonzero and varies with $\rho$.**  Thus the Hamiltonian is conserved, but the total mechanical energy is **not** conserved.  The reason is clear: the motor that keeps the wire spinning at constant $\omega$ **does work on the bead through the normal force**.  The normal force is not perpendicular to the bead's displacement in this case, because the wire itself is moving.



>The bead’s angular momentum about the vertical axis is $L_z = m\rho^2\omega.$
>
>As the bead slides radially, $\rho$ changes, so its angular momentum changes: 
>\[
>\frac{dL_z}{dt} = \frac{d}{dt}\left(m\rho^2\omega\right).
>\]
>Because the wire is forcing the bead to maintain angular speed $\omega$, the wire must exert a torque on the bead. That torque is
>\[
>\tau_z = \frac{dL_z}{dt}.
>\]
>Thus,
>\[
>\tau_z = m\omega\frac{d}{dt}\left(\rho^2\right).
>\]
>Because $dW = \tau_z d\phi = \tau_z w dt$
>\[
>dW = \tau_z w dt = m\omega\frac{d}{dt}\left(\rho^2\right)wdt =mw^2 d(\rho^2)
>\]
>Integrating:
>\[
>W = mw^2 \rho^2 +C
>\]
>where $C$ is an arbitrary constant depending on the reference point for work.
>
>Thus, up to an additive constant,
>\[
>\boxed{ W=m\omega^2\rho^2. }
>\]
>choosing the constant convention appropriately,
>\[
>\boxed{ H=E-W.}
>\]
>Physically, the wire exerts a torque on the bead to keep its angular speed equal to $\omega$.

------

### 3.4 An Effective Potential

It is helpful to rewrite the conserved Hamiltonian (3.3) in the form

$$
H = \frac{1}{2}m(1 + 4\alpha^2\rho^2)\dot{\rho}^2 + U_{\text{eff}}(\rho),
\tag{3.6}
$$

where the **effective potential energy** (有效势能) is

$$
U_{\text{eff}}(\rho) = \frac{1}{2}m\rho^2(2g\alpha - \omega^2).
\tag{3.7}
$$

This effective potential is quadratic in $\rho$.  Its sign depends on how the angular velocity $\omega$ compares with the critical value

$$
\omega_{\text{crit}} = \sqrt{2g\alpha}.
$$

- If $\omega < \omega_{\text{crit}}$, then $U_{\text{eff}}$ rises with $\rho$, so the bead is stable at $\rho = 0$ (the potential minimum).
- If $\omega > \omega_{\text{crit}}$, then $U_{\text{eff}}$ falls with increasing $\rho$, so $\rho = 0$ becomes an **unstable** equilibrium: the bead is thrown outward indefinitely.
- If $\omega = \omega_{\text{crit}}$, the stability is **neutral**.

This example illustrates a crucial point: although the Hamiltonian is often equal to the total energy, **it need not be**.  The distinction between $H$ and $E$, and the conditions under which they differ, are the subject of the next section.

![](Helliwell/images/9c01fb5ef57cd745518872e5f57dba5a5a2819da1714db0bb590e7bd7a5d4d6f.jpg)

Figure 2. If $\omega < \omega _ { \mathrm { c r i t } }$ , then $U _ { \mathrm { e f f } }$ rises with $\rho ,$ so the bead is stable at $\rho = 0 ,$ , the potential minimum. But if ω $> \omega _ { \mathrm { c r i t } }$ , then $U _ { \mathrm { e f f } }$ falls of with increasing $\rho , { \sf s } 0 \rho = 0$ is an unstable equilibrium point in that case: if the bead wanders even slightly from $\rho = 0$ at the bottom of the parabola, it will be thrown out indefinitely far. The stability is neutral if $\omega = \omega _ { \mathrm { c r i t } }$ , meaning that if placed at rest at any point along the wire, the bead will stay at that point indefinitely; but if placed at any point and pushed outward it will keep moving outward, or if pushed inward it will keep moving inward.

---

### 3.5 Rethinking the Generalized-Coordinate Theorem

This example is a direct application of the **generalized-coordinate theorem** for holonomic constraints. The bead is first described by the unconstrained Lagrangian $\mathcal L=\frac12m\dot{\mathbf r}^{\,2}-mgz$. The constraints $z=\alpha\rho^2$ and $\phi=\omega t$ allow us to write the Cartesian coordinates as $x^A=x^A(\rho,t)$. Substituting this into the free bead Lagrangian gives the reduced Lagrangian $L(\rho,\dot\rho,t)$, and the theorem says that $\rho$ satisfies the usual Euler–Lagrange equation. The motor and wire need not be included as dynamical variables because their motion is prescribed externally; their only role is to create the explicit time dependence in $x^A(\rho,t)$. 

If we wanted a more complete dynamical model, we could make the wire angle a **genuine dynamical coordinate**, denoted by \(\Phi(t)\). The bead is constrained to lie on the rotating wire, so its position is

\[
x=\rho\cos\Phi,\qquad
y=\rho\sin\Phi,\qquad
z=\alpha\rho^2 .
\]

In this full description, \(\Phi(t)\) is not prescribed in advance. It is an unknown dynamical coordinate determined by the equations of motion of the bead, wire, and motor.

We may also introduce a motor coordinate \(\theta(t)\), representing the angular position of the motor shaft (马达转轴). The motor attempts to drive the wire angle \(\Phi(t)\). As the motor and wire are connected, the interaction between them can be represented by a coupling term depending on \(\theta\) and \(\Phi\). A **schematic** full Lagrangian is

\[
L_{\text{full}}
=
L_{\text{bead}}(\rho,\dot\rho,\Phi,\dot\Phi)
+
L_{\text{wire}}(\Phi,\dot\Phi)
+
L_{\text{motor}}(\theta,\dot\theta)
+
L_{\text{coupling}}(\theta,\Phi,\dot\theta,\dot\Phi).
\]

Here \(L_{\text{bead}}\) contains all bead-dependent terms. For example,

\[
L_{\text{bead}}
=
\frac12 m\left[(1+4\alpha^2\rho^2)\dot\rho^2+\rho^2\dot\Phi^2\right]
-
mg\alpha\rho^2 .
\]

The coordinate \(\theta(t)\) denotes the motor shaft angle. If the motor shaft and the wire are connected elastically, one might model the coupling by a torsional spring term such as

\[
L_{\text{coupling}}
=
-\frac{k}{2}(\Phi-\theta)^2.
\]

This term penalizes a mismatch between the motor shaft angle \(\theta\) and the wire angle \(\Phi\). 

There is no universal Lagrangian for a motor. A real motor is an active, dissipative, controlled electromechanical device. One usually represents the motor input by a **generalized nonconservative torque** (we will revisit this). For example, if the motor applies a torque $\tau_m(t)$ to the shaft coordinate $\theta$, then the $\theta$-equation is
\[
\frac{d}{dt} \left( \frac{\partial L_{\text{full}}}{\partial \dot\theta} \right) - \frac{\partial L_{\text{full}}}{\partial \theta} = \tau_m(t).
\]
The bead and wire coordinates satisfy
\[
\frac{d}{dt} \left( \frac{\partial L_{\text{full}}}{\partial \dot\rho} \right) - \frac{\partial L_{\text{full}}}{\partial \rho} =0,
\]
and
\[
\frac{d}{dt} \left( \frac{\partial L_{\text{full}}}{\partial \dot\Phi} \right) - \frac{\partial L_{\text{full}}}{\partial \Phi} = 0.
\]
Thus, in the full dynamical model, $\Phi(t)$ is an unknown generalized coordinate, not a prescribed function of time. **To make the problem well-defined, we must specify how the motor acts, for example by prescribing an input torque $\tau_m(t)$. The coupled equations then determine $\rho(t)$, $\Phi(t)$, and possibly $\theta(t)$.**



After imposing \(\Phi(t)=\omega t\), $\Phi$ is no longer a dynamical coordinate. The wire, motor, and coupling terms may reduce to functions of time alone as they do not depend on $\rho$ or $\dot\rho$:
\[
L_{\text{wire}}+L_{\text{motor}}+L_{\text{coupling}} \longrightarrow L_{\text{wire/motor/coupling}}(t).
\]
Then
\[
\frac{\partial L_{\text{wire/motor/coupling}}(t)}{\partial \rho}=0, \qquad \frac{\partial L_{\text{wire/motor/coupling}}(t)}{\partial \dot\rho}=0.
\]
Consequently,
\[
\frac{d}{dt} \left( \frac{\partial L_{\text{wire/motor/coupling}}}{\partial \dot\rho} \right) - \frac{\partial L_{\text{wire/motor/coupling}}}{\partial \rho} =0.
\]
Therefore, once the wire motion is imposed externally, any terms describing only the wire, motor shaft, or their mutual coupling do **not** affect the bead’s Euler-Lagrange equation. 

> In short, there are two different modeling choices:
>
> 1. **Full dynamical model:**
>     Treat $\Phi(t)$ and possibly $\theta(t)$ as generalized coordinates. Include the wire, motor, and coupling terms in the Lagrangian, specify the motor input such as $\tau_m(t)$, and solve the coupled equations for $\rho(t)$, $\Phi(t)$, and possibly $\theta(t)$.
> 2. **Prescribed-motion model:**
>     Impose $\Phi(t)=\omega t$ from the beginning. Then $\Phi$ is no longer an unknown dynamical coordinate, and one solves only for $\rho(t)$. The motor, wire, and coupling are not modeled dynamically; instead, the motor is idealized as supplying whatever torque is necessary to enforce the prescribed rotation.  After solving for $\rho(t)$, one can, in principle, compute the torque required to maintain the prescribed motion $\Phi(t)=\omega t$.

## 4. When the Hamiltonian is Not the Total Energy

In the preceding example we found that $H$ was conserved while $E = T+U$ was not, and that the two quantities differed by $-m\rho^2\omega^2$.  We now derive the general condition for this difference.

------

### 4.1 The General Condition $H \neq E$

Recall the definition of the Hamiltonian (2.1),

$$
H = \sum_{i} \dot{q}_i\,\frac{\partial L}{\partial\dot{q}_i} - L,
$$

where $L = T - U$ and only the kinetic energy $T$ depends on the generalized velocities $\dot{q}_i$.  Therefore

$$
H = \sum_{i} \dot{q}_i\,\frac{\partial T}{\partial\dot{q}_i} + U - T.
\tag{4.1}
$$

Let $\mathbf{r} = \mathbf{r}(q_1,\dots,q_n,t)$ be the position vector of the particle expressed in terms of the generalized coordinates and time.  Its velocity is

$$
\mathbf{v} = \frac{d\mathbf{r}}{dt}
     = \frac{\partial\mathbf{r}}{\partial t}
     + \sum_{l} \frac{\partial\mathbf{r}}{\partial q_l}\,\dot{q}_l.
\tag{4.2}
$$

The kinetic energy is $T = \tfrac12 m\mathbf{v}\cdot\mathbf{v}$.  Substituting (4.2) and expanding, we obtain three terms:

$$
T = \frac12 m\left[
\frac{\partial\mathbf{r}}{\partial t}\cdot\frac{\partial\mathbf{r}}{\partial t}
+ 2\frac{\partial\mathbf{r}}{\partial t}\cdot\sum_{l}\frac{\partial\mathbf{r}}{\partial q_l}\dot{q}_l
+ \sum_{l,k}\frac{\partial\mathbf{r}}{\partial q_l}\cdot\frac{\partial\mathbf{r}}{\partial q_k}\dot{q}_l\dot{q}_k
\right].
\tag{4.3}
$$

Taking the partial derivative of $T$ with respect to a particular $\dot{q}_i$ gives

$$
\frac{\partial T}{\partial\dot{q}_i}
= m\left[
\frac{\partial\mathbf{r}}{\partial t}\cdot\frac{\partial\mathbf{r}}{\partial q_i}
+ \sum_{l}\frac{\partial\mathbf{r}}{\partial q_i}\cdot\frac{\partial\mathbf{r}}{\partial q_l}\dot{q}_l
\right].
\tag{4.4}
$$

Now form the sum that appears in $H$:

$$
\sum_{i}\dot{q}_i\,\frac{\partial T}{\partial\dot{q}_i}
= m\left[
\frac{\partial\mathbf{r}}{\partial t}\cdot\sum_{i}\frac{\partial\mathbf{r}}{\partial q_i}\dot{q}_i
+ \sum_{i,l}\frac{\partial\mathbf{r}}{\partial q_i}\dot{q}_i\cdot\frac{\partial\mathbf{r}}{\partial q_l}\dot{q}_l
\right].
\tag{4.5}
$$

Comparing with (4.3), we recognize that the second term inside the brackets is exactly twice the third term of $T$, while the first term inside the brackets is the cross term of $T$.  After a simple rearrangement,

$$
\sum_{i}\dot{q}_i\,\frac{\partial T}{\partial\dot{q}_i}
= 2T - m\,\frac{\partial\mathbf{r}}{\partial t}\cdot\mathbf{v}.
\tag{4.6}
$$

Substituting (4.6) into (4.1), we arrive at the **key result**:

$$
\boxed{
H = E - \mathbf{p}\cdot\frac{\partial\mathbf{r}}{\partial t},
}
\tag{4.7}
$$

where $E = T + U$ is the total mechanical energy and $\mathbf{p} = m\mathbf{v}$ is the ordinary momentum.

**Interpretation.**
- If the transformation $\mathbf{r} = \mathbf{r}(q_i)$ does **not** depend explicitly on time — that is, if $\partial\mathbf{r}/\partial t = 0$ — then the second term vanishes and $H = E$.  Such coordinates are called **natural coordinates** (自然坐标).
- If the constraints are **moving** (as in the rotating parabolic wire), then $\partial\mathbf{r}/\partial t \neq 0$, and in general $H \neq E$.

> **Check on the bead example.** For the bead on the rotating parabolic wire, the position vector is
> $$
> \mathbf{r} = (\rho\cos\omega t,\; \rho\sin\omega t,\; \alpha\rho^2).
> $$
> Hence
> $$
> \frac{\partial\mathbf{r}}{\partial t} = (-\rho\omega\sin\omega t,\; \rho\omega\cos\omega t,\; 0),
> $$
> and
> $$
> \mathbf{p}\cdot\frac{\partial\mathbf{r}}{\partial t}
> = m\rho^2\omega^2.
> $$
> Therefore $H = E - m\rho^2\omega^2$, exactly as we found in (3.5).

------

### 4.2 Summary

We have established two logically independent results:

1. **Conservation of $H$.** The Hamiltonian is conserved ($dH/dt = 0$) if and only if the Lagrangian has no explicit time dependence ($\partial L/\partial t = 0$).  This reflects **time-translation invariance**; it does not require $H$ to equal $E$.

2. **Identity $H = E$.** The Hamiltonian equals the total mechanical energy ($H = T + U$) if and only if the relation between Cartesian and generalized coordinates is time-independent ($\partial\mathbf{r}/\partial t = 0$).  This condition says nothing about whether $H$ or $E$ is conserved.

Because these are separate conditions, four situations are possible:

| Condition | $H$ conserved? | $E$ conserved? | $H = E$? |
|---|---|---|---|
| $\partial L/\partial t = 0$ and $\partial\mathbf{r}/\partial t = 0$ | Yes | Yes | Yes |
| $\partial L/\partial t = 0$ but $\partial\mathbf{r}/\partial t \neq 0$ | Yes | No | No |
| $\partial L/\partial t \neq 0$ but $\partial\mathbf{r}/\partial t = 0$ | No | No | Yes |
| Neither condition holds | No | No | No |

The rotating parabolic wire falls into the second row: the Lagrangian is independent of time, so $H$ is conserved, but the coordinate transformation depends on time because the constraint is moving.  Consequently $H \neq E$, and the total mechanical energy is not conserved because the motor does work on the system.

------
