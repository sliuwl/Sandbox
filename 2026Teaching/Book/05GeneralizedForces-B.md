# Generalized Forces (Part B)

## Table of Contents

1. [D’Alembert’s Principle](#1-dalemberts-principle)
   - [1.1 Generalized Coordinates and Generalized Forces](#11-generalized-coordinates-and-generalized-forces)
   - [1.2 A Careful Statement of the Principle](#12-a-careful-statement-of-the-principle)
2. [Two Different Uses of “Generalized Coordinates”](#2-two-different-uses-of-generalized-coordinates)
   - [2.1 Case A: Independent Generalized Coordinates](#21-case-a-independent-generalized-coordinates)
   - [2.2 Case B: Redundant Generalized Coordinates](#22-case-b-redundant-generalized-coordinates)
3. [First Explanation: Independent Coordinates Give the Usual Lagrange Equations](#3-first-explanation-independent-coordinates-give-the-usual-lagrange-equations)
4. [Second Explanation: Redundant Coordinates Lead to Lagrange Multipliers](#4-second-explanation-redundant-coordinates-lead-to-lagrange-multipliers)
5. [Summary](#5-summary)

------

## 1. D’Alembert’s Principle

Consider a system of $N$ particles, with particle $j$ having mass $m_j$ and position vector $\vec r_j$. Newton’s second law for each particle reads

$$
\vec F_j=m_j\ddot{\vec r}_j.
$$

The total force on particle $j$ is the sum of an applied force $\vec F_j^{(a)}$ and a constraint force $\vec f_j$, so that

$$
\vec F_j^{(a)}+\vec f_j-m_j\ddot{\vec r}_j=\vec{0}.
$$

Taking the dot product with a virtual displacement $\delta\vec r_j$ and summing over all particles gives

$$
\sum_{j=1}^N\left(\vec F_j^{(a)}+\vec f_j-m_j\ddot{\vec r}_j\right)\cdot\delta\vec r_j=0.
$$

The key assumption is that the constraints are **ideal**: the total virtual work done by the constraint forces vanishes,

$$
\sum_{j=1}^N \vec f_j\cdot\delta\vec r_j=0.
$$

The constraint forces then drop out, and we are left with **d’Alembert’s principle**:

$$
\boxed{\ \sum_{j=1}^N\left(\vec F_j^{(a)}-m_j\ddot{\vec r}_j\right)\cdot\delta\vec r_j=0\ }
$$

for every **admissible virtual displacement**. In words, the virtual work done by the applied forces plus the virtual work done by the inertial forces $-m_j\ddot{\vec r}_j$ must vanish. The principle converts a problem in dynamics into a statement about virtual work and removes the constraint forces from the outset.

------

### 1.1 Generalized Coordinates and Generalized Forces

Suppose the configuration is described by generalized coordinates $q_1,\dots,q_n$, so that

$$
\vec r_j=\vec r_j(q_1,\dots,q_n,t).
$$

A virtual displacement is taken at fixed time, hence

$$
\delta\vec r_j=\sum_{i=1}^n\frac{\partial\vec r_j}{\partial q_i}\,\delta q_i.
$$

Substituting this into d’Alembert’s principle and exchanging the order of summation gives

$$
\sum_{i=1}^n\left[\sum_{j=1}^N\vec F_j^{(a)}\cdot\frac{\partial\vec r_j}{\partial q_i}-\sum_{j=1}^N m_j\ddot{\vec r}_j\cdot\frac{\partial\vec r_j}{\partial q_i}\right]\delta q_i=0.
$$

The first bracket defines the **applied generalized force** associated with $q_i$:

$$
Q_i=\sum_{j=1}^N\vec F_j^{(a)}\cdot\frac{\partial\vec r_j}{\partial q_i}.
$$

Here $Q_i$ is the applied generalized force: it is built only from the applied forces $\vec F_j^{(a)}$ and receives no contribution from the constraint forces $\vec f_j$.

For the second bracket, two standard identities are useful:

$$
\frac{\partial\dot{\vec r}_j}{\partial\dot q_i}=\frac{\partial\vec r_j}{\partial q_i},
\qquad
\frac{d}{dt}\left(\frac{\partial\vec r_j}{\partial q_i}\right)=\frac{\partial\dot{\vec r}_j}{\partial q_i}.
$$

Using these identities, together with the kinetic energy

$$
T=\frac{1}{2}\sum_{j=1}^N m_j\,\dot{\vec r}_j\cdot\dot{\vec r}_j,
$$

the inertial term becomes

$$
\sum_{j=1}^N m_j\ddot{\vec r}_j\cdot\frac{\partial\vec r_j}{\partial q_i}=\frac{d}{dt}\left(\frac{\partial T}{\partial\dot q_i}\right)-\frac{\partial T}{\partial q_i}.
$$

Therefore, d’Alembert’s principle takes the form

$$
\sum_{i=1}^n\left[Q_i-\frac{d}{dt}\left(\frac{\partial T}{\partial\dot q_i}\right)+\frac{\partial T}{\partial q_i}\right]\delta q_i=0,
$$

which must hold for every admissible virtual displacement $(\delta q_1,\dots,\delta q_n)$. This is the starting point for everything that follows.

------

### 1.2 A Careful Statement of the Principle

Define the quantities

$$
A_i=Q_i-\frac{d}{dt}\left(\frac{\partial T}{\partial\dot q_i}\right)+\frac{\partial T}{\partial q_i}.
$$

Then d’Alembert’s principle states that

$$
\sum_{i=1}^n A_i\,\delta q_i=0,
$$

or, in vector notation,

$$
A\cdot\delta q=0,
$$

for every **admissible virtual displacement** $\delta q$.

The important point is this:

> D’Alembert’s principle is not a statement about arbitrary variations. It is a statement about all virtual displacements that are **compatible** with the constraints.

If the coordinates $q_i$ are independent, then the virtual displacements $\delta q_i$ are arbitrary and independent, and one may conclude that $A_i=0$ for each $i$.

If constraints are present, however, the virtual displacements are restricted. In that case, from $A\cdot\delta q=0$ one cannot directly conclude that every $A_i$ is zero; one can only conclude that $A$ is orthogonal to every admissible virtual displacement.



------

## 2. Two Different Uses of “Generalized Coordinates”

A common source of confusion is that the phrase **generalized coordinates** is used in two different ways.

------

### 2.1 Case A: Independent Generalized Coordinates

Suppose the system has $n$ degrees of freedom, and we choose $q_1,\dots,q_n$ as **independent generalized coordinates**. Then the corresponding virtual displacements $\delta q_1,\dots,\delta q_n$ are also independent. In this case, d’Alembert’s principle leads to

$$
\sum_{i=1}^n\left[Q_i-\frac{d}{dt}\left(\frac{\partial T}{\partial\dot q_i}\right)+\frac{\partial T}{\partial q_i}\right]\delta q_i=0.
$$

Since all $\delta q_i$ are independent, each coefficient must vanish:

$$
Q_i-\frac{d}{dt}\left(\frac{\partial T}{\partial\dot q_i}\right)+\frac{\partial T}{\partial q_i}=0.
$$

Equivalently,

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial\dot q_i}\right)-\frac{\partial T}{\partial q_i}=Q_i,\qquad i=1,\dots,n.
$$

This is the usual form of Lagrange’s equations.

------

### 2.2 Case B: Redundant Generalized Coordinates

Sometimes, however, we deliberately use more coordinates than the number of degrees of freedom. Suppose we describe the system using $q_1,\dots,q_n$, but these coordinates are subject to $m$ holonomic constraints

$$
f_\alpha(q,t)=0,\qquad \alpha=1,\dots,m.
$$

Then the actual number of degrees of freedom is $n-m$, assuming the constraints are independent. In this situation, the coordinates $q_i$ are **not all independent**.

A virtual displacement must be compatible with the constraints. Since a virtual displacement is taken at fixed time, we have

$$
\delta f_\alpha=\sum_{i=1}^n\frac{\partial f_\alpha}{\partial q_i}\,\delta q_i=0,\qquad \alpha=1,\dots,m.
$$

Thus the virtual displacements $\delta q_i$ are not independent. This is precisely the situation in which Lagrange multipliers are needed.

------

## 3. First Explanation: Independent Coordinates Give the Usual Lagrange Equations

If we choose coordinates adapted to the constraints, then the coordinates are independent. For example, suppose the system has $r$ degrees of freedom, and we choose independent coordinates $s_1,\dots,s_r$. Then the virtual displacements $\delta s_1,\dots,\delta s_r$ are arbitrary and independent. Applying d’Alembert’s principle in these independent coordinates gives

$$
\sum_{a=1}^r\left[Q_a-\frac{d}{dt}\left(\frac{\partial T}{\partial\dot s_a}\right)+\frac{\partial T}{\partial s_a}\right]\delta s_a=0.
$$

Because the $\delta s_a$ are independent, the coefficients must vanish:

$$
Q_a-\frac{d}{dt}\left(\frac{\partial T}{\partial\dot s_a}\right)+\frac{\partial T}{\partial s_a}=0.
$$

Therefore,

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial\dot s_a}\right)-\frac{\partial T}{\partial s_a}=Q_a,\qquad a=1,\dots,r.
$$

These are the ordinary Lagrange equations in independent generalized coordinates.

The advantage of this approach is that the equations contain no constraint forces explicitly, because the constraints have already been built into the choice of coordinates. The disadvantage is that finding such independent coordinates may be difficult.

------

## 4. Second Explanation: Redundant Coordinates Lead to Lagrange Multipliers

Now suppose instead that we describe the same system using redundant coordinates

\[
\vec q=(q_1,\dots,q_n),
\]

together with $m$ independent holonomic constraints

\[
f_\alpha(\vec q,t)=0,\quad \alpha=1,\dots,m.
\]

The corresponding virtual displacement in generalized-coordinate space is

\[
\delta \vec q=(\delta q_1,\dots,\delta q_n).
\]

Since a virtual displacement is taken at fixed time, the admissible virtual displacements satisfy

\[
\delta f_\alpha=0,
\]

that is,

\[
\sum_{i=1}^n \frac{\partial f_\alpha}{\partial q_i}\,\delta q_i =0,\quad \alpha=1,\dots,m.
\]

Equivalently, in vector form,

\[
\nabla f_\alpha\cdot \delta \vec q=0,
\]

where

\[
\nabla f_\alpha = \left( \frac{\partial f_\alpha}{\partial q_1}, \dots, \frac{\partial f_\alpha}{\partial q_n} \right).
\]

Thus $\delta \vec q$ must lie in the tangent space to the constraint surface.

D’Alembert’s principle says that

\[
\vec A\cdot \delta \vec q=0
\]

for every such admissible virtual displacement $\delta \vec q$, where

\[
\vec A=(A_1,\dots,A_n).
\]

Therefore, **$\vec A$ is orthogonal to the tangent space of the constraint surface**.

The normal space to the constraint surface is spanned by the gradients of the constraint functions,

\[
\nabla f_1,\dots,\nabla f_m.
\]

Assuming the constraints are independent, these gradient vectors are linearly independent. 

>The gradients of the constraints give the directions pointing “out of” the allowed surface. Combining these gradient directions gives all possible normal directions to the surface. In the case of independent constraints, the gradient vectors of the constraint functions are linearly independent and form a **basis for the normal space to the constraint surface**. However, this basis is generally not orthonormal.
>
>约束函数的梯度指向“离开”约束曲面的方向；把这些梯度方向组合起来，就可以得到所有可能的法向方向。在独立约束的情况下，约束函数的梯度向量线性无关，并构成约束曲面法空间的一组基矢；但这组基矢一般不是正交归一的。

As $\vec A$ must lie in the normal space, there exist multipliers $\lambda_\alpha$ such that
\[
\vec A = \sum_{\alpha=1}^m \lambda_\alpha \nabla f_\alpha.
\]

Using component notation, this means

\[
(A_1,\dots,A_n) = \sum_{\alpha=1}^m \lambda_\alpha \left( \frac{\partial f_\alpha}{\partial q_1}, \dots, \frac{\partial f_\alpha}{\partial q_n} \right).
\]

Equivalently, for each component,

\[
A_i = \sum_{\alpha=1}^m \lambda_\alpha \frac{\partial f_\alpha}{\partial q_i},
\]

\[
i=1,\dots,n.
\]

Substituting the definition of $A_i$, we get

\[
Q_i-\frac{d}{dt}\left(\frac{\partial T}{\partial\dot q_i}\right)+\frac{\partial T}{\partial q_i}=\sum_{\alpha=1}^m\lambda_\alpha\frac{\partial f_\alpha}{\partial q_i}.
\]

Rearranging,

\[
\frac{d}{dt}\left(\frac{\partial T}{\partial\dot q_i}\right)-\frac{\partial T}{\partial q_i}=Q_i-\sum_{\alpha=1}^m\lambda_\alpha\frac{\partial f_\alpha}{\partial q_i}.
\]

If we redefine the multipliers by changing their sign,

\[
\lambda_\alpha\mapsto-\lambda_\alpha,
\]

then the same equations can be written as

\[
\boxed{\ \frac{d}{dt}\left(\frac{\partial T}{\partial\dot q_i}\right)-\frac{\partial T}{\partial q_i}=Q_i+\sum_{\alpha=1}^m\lambda_\alpha\frac{\partial f_\alpha}{\partial q_i}\ }
\]

Here $Q_i$ is the applied generalized force, while the sum over $\lambda_\alpha$ collects the generalized constraint forces.

Thus the sign of the multiplier term is a matter of convention.

Together with the constraint equations

\[
f_\alpha(q,t)=0,\qquad \alpha=1,\dots,m,
\]

these form a closed system of equations for $q_i(t)$ and $\lambda_\alpha(t)$.

------

## 5. Summary

The key distinction is the following.

- If the generalized coordinates are **independent**, then the virtual displacements $\delta q_i$ are independent. Therefore, from d’Alembert’s principle one obtains

  $$
  \frac{d}{dt}\left(\frac{\partial T}{\partial\dot q_i}\right)-\frac{\partial T}{\partial q_i}=Q_i.
  $$

- If the generalized coordinates are **redundant**, then the virtual displacements $\delta q_i$ are constrained. Therefore, one cannot set each coefficient equal to zero. Instead, the coefficient vector must lie in the normal space to the constraint surface, giving

  $$
  \frac{d}{dt}\left(\frac{\partial T}{\partial\dot q_i}\right)-\frac{\partial T}{\partial q_i}=Q_i+\sum_{\alpha=1}^m\lambda_\alpha\frac{\partial f_\alpha}{\partial q_i},
  $$

  up to the sign convention for $\lambda_\alpha$.

In short:

> Independent coordinates eliminate the constraints by construction. Redundant coordinates keep the constraints explicit and introduce Lagrange multipliers to account for the missing independence of the virtual displacements.



------

达朗贝尔原理（d’Alembert’s principle）本质上可以看作一种**虚功原理**。它说的是：在系统的真实运动过程中，外加力与惯性力之差，对任意允许的虚位移所作的总虚功为零。这里最重要的一点是，**虚位移必须与约束相容**，也就是说，虚位移必须满足系统约束所允许的条件；但是，**达朗贝尔原理本身并不要求这些虚位移的各个分量 $\delta q_i$ 一定彼此独立**。

因此，关键问题在于我们如何选择广义坐标。大体上可以分为两种情况。

第一种情况是：我们已经利用约束条件选取了一组**独立的广义坐标**。例如，对于一个受完整约束（holonomic constraints）限制的系统，如果约束方程已经被用来消去多余变量，那么剩下的广义坐标数目就等于系统的自由度数。在这种情况下，$\delta q_1,\dots,\delta q_n$ 是彼此独立的。于是，如果
\[
\sum_{i=1}^n A_i\delta q_i=0
\]
对任意独立的 $\delta q_i$ 都成立，那么就可以推出
\[
A_i=0,\qquad i=1,\dots,n.
\]
这正是通常从达朗贝尔原理推出拉格朗日方程（Lagrange equations）时所采用的情形。

第二种情况是：我们仍然使用一组**冗余坐标**，或者某些约束条件尚未被完全消去。此时虽然仍然可以写出
\[
A\cdot \delta q=0,
\]
但是 $\delta q_i$ 不再是任意且彼此独立的变量，而必须满足由约束条件带来的关系。例如，某些允许的虚位移可能满足
\[
\sum_i c_i\delta q_i=0.
\]
在这种情况下，不能直接推出每一个 $A_i$ 都等于零。我们只能说，**向量 $A$ 与所有允许的虚位移方向正交**。若要进一步得到运动方程，通常需要引入拉格朗日乘子（Lagrange multipliers），把约束条件或约束力的影响显式地写入方程中。



关于“广义坐标”（generalized coordinates）这个术语，不同教材的侧重点确实略有不同。在许多经典力学教材中，尤其是在处理完整约束并推导拉格朗日方程时，广义坐标通常被选为一组**独立坐标**。也就是说，人们常常先利用约束方程消去多余的笛卡尔坐标（Cartesian coordinates），最后保留与系统自由度数目相同的一组变量。在这种标准语境下，$q_i$ 往往默认就是独立的广义坐标。

不过，从更宽泛的意义上说，“广义坐标”这个词也强调这些坐标不必是普通的笛卡尔坐标，而可以是任何方便描述系统构型的变量，例如角度、弧长、欧拉角等。因此，有些教材在引入广义坐标时，更强调“广义”这一点，也就是它们可以是非笛卡尔坐标；而另一些教材则会同时强调，为了唯一描述一个具有 $n$ 个自由度的系统，通常应当选取 $n$ 个彼此独立的广义坐标。

所以，更准确地说：在推导标准形式的拉格朗日方程时，广义坐标通常已经被选为与自由度数目相同的独立坐标；但从术语本身来看，“广义坐标”主要强调它们不必是笛卡尔坐标，而可以是任何适合描述系统构型的变量。如果使用的是冗余坐标，那么它们也可以在较宽泛的意义下被称为广义坐标，但这时其虚位移 $\delta q_i$ 就不能被当作独立变量处理。因此，达朗贝尔原理的核心是“$\delta q$ 是否是与约束相容的允许虚位移”。



## 6. Particle Sliding on a Hemisphere

A particle of mass $m$ begins from rest at the top of a smooth fixed hemisphere of radius $R$. We wish to find the angle $\theta_0$ at which it loses contact with the surface.

The Lagrangian in polar coordinates $(r,\theta)$, with $\theta$ measured from the vertical, is

$$
L = \frac12 m\left(\dot r^2 + r^2\dot\theta^2\right) - mgr\cos\theta.
$$

The holonomic constraint is

$$
g(r) = r - R = 0.
$$

The constrained Lagrange equations are

$$
\frac{d}{dt}\left(\frac{\partial L}{\partial\dot r}\right) - \frac{\partial L}{\partial r} = \lambda\frac{\partial g}{\partial r} = \lambda,
$$

$$
\frac{d}{dt}\left(\frac{\partial L}{\partial\dot\theta}\right) - \frac{\partial L}{\partial\theta} = \lambda\frac{\partial g}{\partial\theta} = 0.
$$

Evaluating the derivatives,

$$
m\ddot r - mr\dot\theta^2 + mg\cos\theta = \lambda,
$$

$$
2mr\dot r\dot\theta + mr^2\ddot\theta - mgr\sin\theta = 0.
$$

We now impose the constraint $r=R$, which implies $\dot r=\ddot r=0$. The radial equation becomes

$$
-mR\dot\theta^2 + mg\cos\theta = \lambda,
$$

so

$$
\dot\theta^2 = \frac{g\cos\theta}{R} - \frac{\lambda}{mR}.
$$

The angular equation reduces to

$$
mR^2\ddot\theta - mgR\sin\theta = 0 \quad\Longrightarrow\quad \ddot\theta = \frac{g\sin\theta}{R}.
$$

> **Physical meaning of $\lambda$.** The Lagrange multiplier $\lambda$ is the magnitude of the normal force that the hemisphere exerts on the particle. When $\lambda$ drops to zero, the constraint is about to break; the particle can no longer press against the surface and therefore leaves the sphere.

The particle leaves the surface precisely when the normal force vanishes:

$$
\lambda = 0.
$$

Hence, at the instant of departure,

$$
\dot\theta^2 = \frac{g\cos\theta_0}{R}.
$$

To relate $\theta_0$ to the initial condition, we differentiate the radial expression for $\dot\theta^2$ with respect to time:

$$
\frac{d}{dt}\dot\theta^2 = 2\dot\theta\ddot\theta.
$$

Using $\dot\theta^2 = (g\cos\theta)/R - \lambda/(mR)$,

$$
2\dot\theta\ddot\theta = -\frac{g}{R}\sin\theta\,\dot\theta - \frac{1}{mR}\frac{d\lambda}{dt}.
$$

Since $\ddot\theta = g\sin\theta/R$, the left-hand side becomes

$$
2\dot\theta\left(\frac{g\sin\theta}{R}\right) = -\frac{g}{R}\sin\theta\,\dot\theta - \frac{1}{mR}\frac{d\lambda}{dt},
$$

or, after rearranging,

$$
\frac{3g}{R}\sin\theta\,\dot\theta = -\frac{1}{mR}\frac{d\lambda}{dt}.
$$

Multiplying by $dt$ and using $d\theta = \dot\theta\,dt$,

$$
3g\sin\theta\,d\theta = -\frac{1}{m}\,d\lambda.
$$

Integrating from the initial position $(\theta=0,\;\lambda_0)$ to the leaving point $(\theta_0,\;0)$,

$$
3g\int_0^{\theta_0}\sin\theta\,d\theta = -\frac{1}{m}\int_{\lambda_0}^{0}d\lambda.
$$

This gives

$$
3g\bigl(1-\cos\theta_0\bigr) = \frac{\lambda_0}{m}.
$$

At the top of the sphere, the particle is initially at rest ($\dot\theta=0$ when $\theta=0$), so the radial equation yields $\lambda_0 = mg$. Therefore

$$
3g\bigl(1-\cos\theta_0\bigr) = g,
$$

which simplifies to

$$
\boxed{
\cos\theta_0 = \frac23
}
$$

or 
\[
\theta_0 \approx 48.2^\circ.
\]
