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

for every admissible virtual displacement. In words, the virtual work done by the applied forces plus the virtual work done by the inertial forces $-m_j\ddot{\vec r}_j$ must vanish. The principle converts a problem in dynamics into a statement about virtual work and removes the constraint forces from the outset.

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

The first bracket defines the **generalized force** associated with $q_i$:

$$
Q_i=\sum_{j=1}^N\vec F_j^{(a)}\cdot\frac{\partial\vec r_j}{\partial q_i}.
$$

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

> D’Alembert’s principle is not a statement about arbitrary variations. It is a statement about all virtual displacements that are compatible with the constraints.

If the coordinates $q_i$ are independent, then the virtual displacements $\delta q_i$ are arbitrary and independent, and one may conclude that $A_i=0$ for each $i$. If constraints are present, however, the virtual displacements are restricted. In that case, from $A\cdot\delta q=0$ one cannot directly conclude that every $A_i$ is zero; one can only conclude that $A$ is orthogonal to every admissible virtual displacement.

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

Now suppose instead that we describe the same system using redundant coordinates $q_1,\dots,q_n$, together with $m$ independent holonomic constraints

$$
f_\alpha(q,t)=0,\qquad \alpha=1,\dots,m.
$$

The admissible virtual displacements satisfy

$$
\sum_{i=1}^n\frac{\partial f_\alpha}{\partial q_i}\,\delta q_i=0,\qquad \alpha=1,\dots,m,
$$

or, in vector form,

$$
\nabla f_\alpha\cdot\delta q=0.
$$

Thus $\delta q$ must lie in the tangent space to the constraint surface. D’Alembert’s principle says that

$$
A\cdot\delta q=0
$$

for every such admissible virtual displacement $\delta q$. Therefore, $A$ is orthogonal to the tangent space of the constraint surface.

The normal space to the constraint surface is spanned by the gradients of the constraint functions,

$$
\nabla f_1,\dots,\nabla f_m.
$$

Assuming the constraints are independent, these gradients are linearly independent. Hence there exist multipliers $\lambda_\alpha$ such that

$$
A=\sum_{\alpha=1}^m\lambda_\alpha\nabla f_\alpha.
$$

In components,

$$
A_i=\sum_{\alpha=1}^m\lambda_\alpha\frac{\partial f_\alpha}{\partial q_i}.
$$

Substituting the definition of $A_i$, we get

$$
Q_i-\frac{d}{dt}\left(\frac{\partial T}{\partial\dot q_i}\right)+\frac{\partial T}{\partial q_i}=\sum_{\alpha=1}^m\lambda_\alpha\frac{\partial f_\alpha}{\partial q_i}.
$$

Rearranging,

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial\dot q_i}\right)-\frac{\partial T}{\partial q_i}=Q_i-\sum_{\alpha=1}^m\lambda_\alpha\frac{\partial f_\alpha}{\partial q_i}.
$$

If we redefine the multipliers by changing their sign,

$$
\lambda_\alpha\mapsto-\lambda_\alpha,
$$

then the same equations can be written as

$$
\boxed{\ \frac{d}{dt}\left(\frac{\partial T}{\partial\dot q_i}\right)-\frac{\partial T}{\partial q_i}=Q_i+\sum_{\alpha=1}^m\lambda_\alpha\frac{\partial f_\alpha}{\partial q_i}\ }
$$

Thus the sign of the multiplier term is a matter of convention.

Together with the constraint equations

$$
f_\alpha(q,t)=0,\qquad \alpha=1,\dots,m,
$$

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
