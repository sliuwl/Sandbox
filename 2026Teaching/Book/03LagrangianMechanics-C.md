# Lagrangian Mechanics (Part C)

**Reading material:** Chapter 4 of *Introduction to Classical Mechanics* by Thomas A. Helliwell; Chapter 7 of *Classical Mechanics* by John R. Taylor; Chapter 7 of David Tong's *Lectures on Classical Dynamics*

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
4. [When the Hamiltonian is Not the Total Energy](#4-when-the-hamiltonian-is-not-the-total-energy)
   - [4.1 The General Condition $H \neq E$](#41-the-general-condition-h-neq-e)
   - [4.2 Summary](#42-summary)

---

## 1. Generalized Momentum and Cyclic Coordinates

In our development of Lagrangian mechanics, the quantities $\partial L/\partial q_i$ and $\partial L/\partial \dot q_i$ have appeared repeatedly. We now give them names and explore their physical significance. The derivative $\partial L/\partial q_i$ plays a role analogous to a force, while $\partial L/\partial \dot q_i$ plays a role analogous to a momentum. This observation leads directly to powerful conservation laws that are often easier to spot in the Lagrangian formalism than in Newtonian mechanics.

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

The connection between cyclic coordinates and conserved momenta is the simplest manifestation of a much deeper result known as **Noether's theorem** (诺特定理), which states that every continuous symmetry of the Lagrangian gives rise to a conserved quantity. Translational invariance leads to momentum conservation, rotational invariance leads to angular momentum conservation, and—as we shall see in the next section—invariance under time translation leads to energy conservation.

------

## 2. The Hamiltonian

We have seen that when the Lagrangian does not depend on a particular coordinate, the corresponding momentum is conserved. It is natural to ask what happens when the Lagrangian does not depend explicitly on time. This question leads us to the **Hamiltonian** (哈密顿量), a quantity that is not only a constant of motion in many systems, but also serves as the foundation for an entirely different formulation of mechanics.

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

> **Important caveat.** The Hamiltonian is conserved whenever $\partial L/\partial t = 0$, but it is *not always* the total energy.  In the next section we prove that $H = T+U$ provided the transformation from Cartesian to generalized coordinates does not depend explicitly on time.  If the transformation is time-dependent, $H$ may still be conserved but may differ from $T+U$.

> **Example: Bead on a rotating hoop.** For a bead on a hoop rotating with fixed angular velocity $\omega$, the Lagrangian is $L = \tfrac12mR^2(\dot\theta^2+\omega^2\sin^2\theta) - mgR(1-\cos\theta)$.  Since $\omega$ is a fixed parameter, $L$ has no explicit time dependence, so $H$ is conserved.  However, $H$ is *not* the total mechanical energy $T+U$; it includes an extra term from the forced rotation.  This illustrates that conservation of $H$ and identification of $H$ with $T+U$ are logically distinct statements.

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
> 1. $H$ is conserved if and only if $\partial L/\partial t = 0$ (or equivalently $\partial H/\partial t = 0$).
> 2. $H = T+U$ if and only if the coordinate transformation is time-independent.
>
> When *both* conditions hold—namely, the Lagrangian has no explicit time dependence *and* the coordinates are natural—then the total mechanical energy $E = T+U$ is conserved.

------

## 3. Example: Bead on a Rotating Parabolic Wire

We now examine a system in which the **Hamiltonian** (哈密顿量) is conserved but is *not* equal to the total mechanical energy.  This example will motivate the more general discussion in the next section.

Suppose we bend a wire into the shape of a vertically oriented parabola defined in cylindrical coordinates by

$$
z = \alpha\rho^2,
$$

where $z$ is the vertical coordinate and $\rho$ is the distance from the axis of symmetry.  Using a synchronous motor, we force the wire to spin at constant angular velocity $\omega$ about its symmetry axis.  A bead of mass $m$ slides without friction along the wire, as illustrated in Figure 1.

![
](images/placeholder_parabolic_wire.jpg)
**Figure 1**: A bead slides without friction on a vertically oriented parabolic wire forced to spin about its axis of symmetry.

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

**This difference is nonzero and varies with $\rho$.**  Thus the Hamiltonian is conserved, but the total mechanical energy is **not** conserved.  The reason is clear: the motor that keeps the wire spinning at constant $\omega$ does work on the bead through the normal force.  The normal force is not perpendicular to the bead's displacement in this case, because the wire itself is moving.

> **Physical interpretation.** Equation (3.5) can be understood as follows.  The bead's energy changes because the rotating wire continually does work on it.  The rate of work is $dW/dt = \omega\,d(m\rho^2\omega)/dt = m\omega^2\,d(\rho^2)/dt$.  Integrating, the work done is $W = m\omega^2\rho^2$ (up to a constant), so $E - W = H$ remains constant.

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

------

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
