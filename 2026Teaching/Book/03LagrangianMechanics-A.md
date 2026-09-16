# Lagrangian Mechanics

**Reading material:** Chapter 7 of *Classical Mechanics* by John R. Taylor

## Table of Contents

1. [Mathematical Spaces](#1-mathematical-spaces)
   - [1.1 Physical Space](#11-physical-space)
   - [1.2 Configuration Space](#12-configuration-space)
   - [1.3 Phase Space](#13-phase-space)
2. [Hamilton's Principle](#2-hamiltons-principle)
3. [Action](#3-action)
4. [Derivation of the Euler–Lagrange Equation](#4-derivation-of-the-eulerlagrange-equation)
5. [Comments on the Variational Principle](#5-comments-on-the-variational-principle)
   - [5.1 Fixed but Arbitrary Endpoints](#51-fixed-but-arbitrary-endpoints)
   - [5.2 Euler–Lagrange Equation as a Local Condition](#52-eulerlagrange-equation-as-a-local-condition)
   - [5.3 How the Physical Path Is Selected](#53-how-the-physical-path-is-selected)
6. [Multi-Dimensional Configuration Space](#6-multi-dimensional-configuration-space)
7. [Generalized Coordinates and Constrained Systems](#7-generalized-coordinates-and-constrained-systems)
   - [7.1 Generalized Coordinates](#71-generalized-coordinates)
   - [7.2 Lagrangian in Generalized Coordinates](#72-lagrangian-in-generalized-coordinates)
8. [Examples](#8-examples)
   - [8.1 Polar Coordinates](#81-polar-coordinates)
   - [8.2 Simple Pendulum](#82-simple-pendulum)
   - [8.3 Atwood Machine](#83-atwood-machine)
   - [8.4 Block Sliding on a Movable Wedge](#84-block-sliding-on-a-movable-wedge)
9. [Generalized Momenta and Ignorable Coordinates](#9-generalized-momenta-and-ignorable-coordinates)
10. [Hamiltonian and Conservation Laws](#10-hamiltonian-and-conservation-laws)
11. [Summary](#11-summary)

---

## 1. Mathematical Spaces

Before we develop the formalism, it is helpful to be clear about the mathematical spaces in which the various quantities live.

------

### 1.1 Physical Space

For ordinary nonrelativistic mechanics, the **physical space** in which particles are located is modeled as three-dimensional Euclidean space,

$$
\mathbb{R}^3.
$$

For a single particle, its **position** is represented by a vector

$$
\mathbf r \in \mathbb{R}^3,
$$

and its **momentum** is represented by another vector

$$
\mathbf p \in \mathbb{R}^3.
$$

Thus, for each particle, position and momentum are separate vector quantities, each with three components.

------

### 1.2 Configuration Space

For a system of $N$ particles, specifying the **configuration** means specifying the position of every particle.

If the particles have positions

$$
\mathbf r_1,\mathbf r_2,\dots,\mathbf r_N \in \mathbb{R}^3,
$$

then a complete configuration is obtained by collecting all of these position vectors together in a single ordered list:

$$
q = (\mathbf r_1,\mathbf r_2,\dots,\mathbf r_N).
$$

What does this mean concretely?  Each position vector $\mathbf r_\alpha$ has three components $(x_\alpha, y_\alpha, z_\alpha)$.  Putting all $N$ particles together gives a grand list of $3N$ numbers:

$$
(x_1, y_1, z_1,\; x_2, y_2, z_2,\; \dots,\; x_N, y_N, z_N).
$$

This is simply the familiar idea of "coordinates," but now we have $3N$ of them instead of just three.  The collection of all possible such lists forms a $3N$-dimensional space called the **configuration space** of the system.

Each point in configuration space corresponds to one complete arrangement of the $N$ particles in physical space.  The time evolution of the system is therefore represented by a path

$$
q(t) \in \mathbb{R}^{3N}.
$$

Equivalently,

$$
q(t)=\bigl(\mathbf r_1(t),\mathbf r_2(t),\dots,\mathbf r_N(t)\bigr).
$$

So instead of tracking $N$ separate position vectors in $\mathbb{R}^3$, we may track one point moving in the higher-dimensional configuration space.

------

### 1.3 Phase Space

Configuration space records only the positions of the particles.  To specify the complete mechanical state of a system in Hamiltonian mechanics, one must also specify the momenta.

For $N$ particles, the momenta are

$$
\mathbf p_1,\mathbf p_2,\dots,\mathbf p_N \in \mathbb{R}^3.
$$

The complete state is therefore

$$
(q,p) = (\mathbf r_1,\dots,\mathbf r_N,\mathbf p_1,\dots,\mathbf p_N).
$$

This is an element of

$$
\mathbb{R}^{3N}\times \mathbb{R}^{3N} \cong \mathbb{R}^{6N}.
$$

This $6N$-dimensional space is called the **phase space**.

A point in phase space specifies both:

$$
\text{positions} + \text{momenta}.
$$

In Hamiltonian mechanics, $q$ and $p$ are treated as independent coordinates on phase space.  This does not mean that their time evolution is independent; rather, it means that a state is specified by giving both $q$ and $p$, and their evolution is determined by Hamilton's equations.

------

## 2. Hamilton's Principle

Lagrangian mechanics is based on the **principle of stationary action**, also known as **Hamilton's principle**.

Informally, this principle is sometimes described as saying that "nature is economical" or that "nature minimizes action."  However, the rigorous statement is more precise:

> The actual path followed by a system between two fixed configurations at fixed initial and final times makes the action stationary with respect to small variations of the path.

The **action** is defined by

$$
S[q] = \int_{t_i}^{t_f} L(q,\dot q,t)\,dt,
$$

where:

- $q(t)$ is a path in configuration space,
- $\dot q(t)$ is the velocity along that path,
- $L(q,\dot q,t)$ is the **Lagrangian**,
- $t_i$ and $t_f$ are fixed initial and final times.

For many elementary mechanical systems,

$$
L = T - V,
$$

where $T$ is **kinetic energy** and $V$ is **potential energy**.

Hamilton's principle states that the physical path satisfies

$$
\delta S = 0.
$$

This means the action is **stationary**, not necessarily minimal.  A stationary value may be a minimum, a maximum, or a saddle point in the space of paths.

------

## 3. Action

The action assigns a number to each possible path in configuration space.  Therefore, it is not an ordinary function of a point; it is a **functional**, meaning a function whose input is itself a function.

A path

$$
q(t)
$$

is mapped to a real number:

$$
q(t) \longmapsto S[q] \longmapsto \mathbb{R}.
$$

Explicitly,

$$
S[q] = \int_{t_i}^{t_f} L(q,\dot q,t)\,dt.
$$

The units of action are energy multiplied by time:

$$
[S] = [E][t] = \mathrm{J}\cdot\mathrm{s} = \frac{\mathrm{kg}\,\mathrm{m}^2}{\mathrm{s}}.
$$

Different paths between the same endpoints generally have different action values.  For example,

$$
S[q_1(t)] = 8.73, \qquad S[q_2(t)] = 9.21, \qquad S[q_3(t)] = 10.5.
$$

The actual path is the one for which the first-order change in the action vanishes under all allowed infinitesimal variations.

------

## 4. Derivation of the Euler–Lagrange Equation

Consider a one-dimensional configuration variable $q(t)$.  The multidimensional case is obtained by applying the same argument to each generalized coordinate.

Let the physical path be $q(t)$.  We compare it with nearby paths of the form

$$
q_\alpha(t)=q(t)+\alpha \eta(t),
$$

where:

- $\alpha$ is a real parameter,
- $\eta(t)$ is an arbitrary smooth variation,
- the endpoints are fixed, so

$$
\eta(t_i)=\eta(t_f)=0.
$$

The corresponding velocity is

$$
\dot q_\alpha(t)=\dot q(t)+\alpha \dot\eta(t).
$$

The action evaluated on the varied path is

$$
S[\alpha] = \int_{t_i}^{t_f} L(q+\alpha\eta,\dot q+\alpha\dot\eta,t)\,dt.
$$

The physical path makes the action stationary, so

$$
\left.\frac{dS[\alpha]}{d\alpha}\right|_{\alpha=0}=0.
$$

Differentiating under the integral sign gives

$$
\left.\frac{dS[\alpha]}{d\alpha}\right|_{\alpha=0} = \int_{t_i}^{t_f} \left[ \frac{\partial L}{\partial q}\eta + \frac{\partial L}{\partial \dot q}\dot\eta \right]dt.
$$

Therefore, stationarity requires

$$
\int_{t_i}^{t_f} \left[ \frac{\partial L}{\partial q}\eta + \frac{\partial L}{\partial \dot q}\dot\eta \right]dt =0.
$$

Now integrate the second term by parts:

$$
\int_{t_i}^{t_f} \frac{\partial L}{\partial \dot q}\dot\eta\,dt = \left. \eta\frac{\partial L}{\partial \dot q} \right|_{t_i}^{t_f} - \int_{t_i}^{t_f} \eta \frac{d}{dt} \left( \frac{\partial L}{\partial \dot q} \right)dt.
$$

Because $\eta(t_i)=\eta(t_f)=0$, the boundary term vanishes:

$$
\left. \eta\frac{\partial L}{\partial \dot q} \right|_{t_i}^{t_f} =0.
$$

Thus,

$$
\int_{t_i}^{t_f} \frac{\partial L}{\partial \dot q}\dot\eta\,dt = - \int_{t_i}^{t_f} \eta \frac{d}{dt} \left( \frac{\partial L}{\partial \dot q} \right)dt.
$$

Substituting this into the stationarity condition gives

$$
\int_{t_i}^{t_f} \left[ \frac{\partial L}{\partial q} - \frac{d}{dt} \left( \frac{\partial L}{\partial \dot q} \right) \right]\eta(t)\,dt =0.
$$

Since $\eta(t)$ is arbitrary except for vanishing at the endpoints, the fundamental lemma of the calculus of variations implies

$$
\frac{\partial L}{\partial q} - \frac{d}{dt} \left( \frac{\partial L}{\partial \dot q} \right) =0.
$$

Equivalently,

$$
\boxed{ \frac{d}{dt} \left( \frac{\partial L}{\partial \dot q} \right) - \frac{\partial L}{\partial q} =0 }
$$

This is the **Euler–Lagrange equation**.

> **Note.** The two sign conventions are identical up to multiplication by $-1$.  In mechanics one often sees $\partial L/\partial q = \frac{d}{dt}(\partial L/\partial \dot q)$; in field theory the opposite sign is common.  Both are correct.

------

## 5. Comments on the Variational Principle

------

### 5.1 Fixed but Arbitrary Endpoints

In Hamilton’s principle, we compare the actual path with nearby trial paths.

Suppose the path satisfies

$$
q(t_i)=q_i,
\qquad
q(t_f)=q_f.
$$

During the variation, the endpoints are held fixed. That means every allowed trial path must have the same initial and final configurations:

$$
q_\varepsilon(t_i)=q_i,
\qquad
q_\varepsilon(t_f)=q_f.
$$

If

$$
q_\varepsilon(t)=q(t)+\varepsilon \eta(t),
$$

then fixed endpoints imply

$$
\eta(t_i)=0,
\qquad
\eta(t_f)=0.
$$

So the variation may change the path in the interior, but not at the endpoints.

#### Meaning of “Fixed but Arbitrary”

The endpoints are **fixed** during a particular variational problem.

They are **arbitrary** because their values are not special. We may choose any endpoint configurations $q_i$ and $q_f$, and the same derivation works.

Therefore:

$$
\boxed{
\text{fixed during the variation, arbitrary in their choice}
}
$$

Because the endpoints were arbitrary, the resulting equation of motion is not tied to a particular pair of endpoints.

------

### 5.2 Euler–Lagrange Equation as a Local Condition

Hamilton’s principle states that the physical path makes the action stationary:

$$
\delta S=0,
$$

where

$$
S[q]=\int_{t_i}^{t_f} L(q,\dot q,t)\,dt.
$$

For fixed-endpoint variations, this condition leads to the Euler–Lagrange equation:

$$
\boxed{
\frac{d}{dt}
\left(
\frac{\partial L}{\partial \dot q}
\right)
-
\frac{\partial L}{\partial q}
=0
}
$$

This is a **local differential equation**. It must hold at each time along the physical path.

Important:

$$
\boxed{
\text{stationary action} \neq \text{always least action}
}
$$

The action may be a minimum, maximum, or saddle point. Hamilton’s principle requires stationarity, not necessarily global minimization.

------

### 5.3 How the Physical Path Is Selected

Hamilton’s principle is usually used to derive the equations of motion.

After the Euler–Lagrange equation is known, the actual physical trajectory is selected by initial conditions, such as

$$
q(t_i),
\qquad
\dot q(t_i).
$$

Equivalently, in Hamiltonian mechanics, one uses

$$
q(t_i),
\qquad
p(t_i).
$$

Thus the final configuration does not have to be known in advance when predicting motion.

The logical structure is:

$$
\boxed{
\text{stationary action with fixed endpoints}
\Longrightarrow
\text{Euler--Lagrange equation}
\Longrightarrow
\text{initial conditions select the trajectory}
}
$$

So the fixed final endpoint is mainly part of the variational derivation, while physical prediction is usually done from initial position and velocity.

------

## 6. Multi-Dimensional Configuration Space

In general, the configuration variable has several components.  Write

$$
q(t)=\bigl(q^1(t),q^2(t),\dots,q^n(t)\bigr),
$$

where $n$ is the dimension of the configuration space.

For $N$ unconstrained particles in three-dimensional physical space,

$$
n=3N.
$$

The Lagrangian is then a function

$$
L(q^1,\dots,q^n,\dot q^1,\dots,\dot q^n,t).
$$

Applying the same variational argument to each coordinate gives one Euler–Lagrange equation for each generalized coordinate:

$$
\boxed{ \frac{d}{dt} \left( \frac{\partial L}{\partial \dot q^k} \right) - \frac{\partial L}{\partial q^k} =0, \qquad k=1,\dots,n. }
$$

Equivalently,

$$
\boxed{ \frac{\partial L}{\partial q^k} - \frac{d}{dt} \left( \frac{\partial L}{\partial \dot q^k} \right) =0, \qquad k=1,\dots,n. }
$$

The two forms are identical up to multiplication by $-1$.

------

## 7. Generalized Coordinates and Constrained Systems

For a system of $N$ particles, a complete configuration in Cartesian coordinates requires $3N$ coordinates.  However, many mechanical systems are subject to **constraints** that restrict the motion — for example, a simple pendulum is constrained to move at a fixed distance from its pivot, and the particles in a rigid body are constrained to maintain fixed relative separations.

------

### 7.1 Generalized Coordinates

The parameters $q_1, \dots, q_n$ are called **generalized coordinates** if each particle's position can be expressed as

$$
\mathbf r_\alpha = \mathbf r_\alpha(q_1, \dots, q_n, t), \qquad \alpha = 1, \dots, N,
$$

and conversely each $q_i$ can be expressed in terms of the positions.  The number $n$ is the smallest number of parameters that describes the system completely.

- The **number of degrees of freedom** is the number of coordinates that can be independently varied in a small displacement.
- When $n < 3N$ the system is **constrained**.
- A system is called **holonomic** if the number of degrees of freedom equals the number of generalized coordinates.
- If the transformation between Cartesian coordinates and generalized coordinates does not involve time explicitly, the coordinates are said to be **natural**.

------

### 7.2 Lagrangian in Generalized Coordinates

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

Moreover, the forces of constraint — such as tension in a string or the normal force from a surface — do not appear in these equations, provided the constraints are holonomic and the non-constraint forces are derivable from a potential energy $V$.

------

## 8. Examples

The following examples illustrate how to apply the Lagrangian formalism to concrete mechanical systems.

------

### 8.1 Polar Coordinates

Consider a particle of mass $m$ moving in a plane, described by polar coordinates $(r, \phi)$.  The velocity components are $v_r = \dot r$ and $v_\phi = r\dot\phi$, so the kinetic energy is

$$
T = \frac{1}{2}m(\dot r^2 + r^2\dot\phi^2).
$$

With potential energy $V(r, \phi)$, the Lagrangian is

$$
L = \frac{1}{2}m(\dot r^2 + r^2\dot\phi^2) - V(r, \phi).
$$

**The $r$ equation:**

$$
\frac{\partial L}{\partial r} = \frac{d}{dt}\frac{\partial L}{\partial \dot r}
\;\Longrightarrow\;
mr\dot\phi^2 - \frac{\partial V}{\partial r} = m\ddot r,
$$

which is the radial component of $\mathbf F = m\mathbf a$.

**The $\phi$ equation:**

$$
\frac{\partial L}{\partial \phi} = \frac{d}{dt}\frac{\partial L}{\partial \dot\phi}
\;\Longrightarrow\;
-\frac{\partial V}{\partial \phi} = \frac{d}{dt}(mr^2\dot\phi).
$$

If $V$ depends only on $r$, then $\partial V/\partial\phi = 0$ and $mr^2\dot\phi$ — the **angular momentum** — is conserved.  This illustrates how choosing natural coordinates leads to equations that automatically reveal conservation laws.

------

### 8.2 Simple Pendulum

A bob of mass $m$ is attached to a massless rod of length $l$ pivoted at a fixed point.  The system has one degree of freedom.  Using the angle $\phi$ measured from the vertical as generalized coordinate,

$$
x = l\sin\phi, \qquad y = -l\cos\phi,
$$

so the kinetic energy is

$$
T = \frac{1}{2}ml^2\dot\phi^2,
$$

and the potential energy (taking the pivot height as reference) is

$$
V = -mgl\cos\phi.
$$

The Lagrangian is

$$
L = \frac{1}{2}ml^2\dot\phi^2 + mgl\cos\phi.
$$

The Euler–Lagrange equation gives

$$
- mgl\sin\phi = \frac{d}{dt}(ml^2\dot\phi) = ml^2\ddot\phi,
$$

or

$$
\boxed{ \ddot\phi + \frac{g}{l}\sin\phi = 0, }
$$

the familiar pendulum equation.  The tension in the rod never appeared.

------

### 8.3 Atwood Machine

Two masses $m_1$ and $m_2$ are connected by a light inextensible string of fixed length passing over a frictionless pulley.  Because the string length is constant,

$$
x + y = \text{const},
$$

where $x$ and $y$ measure the vertical positions of the masses.  Choosing $x$ as the single generalized coordinate gives $\dot y = -\dot x$.

The kinetic energy is

$$
T = \frac{1}{2}m_1\dot x^2 + \frac{1}{2}m_2\dot y^2 = \frac{1}{2}(m_1+m_2)\dot x^2,
$$

and the potential energy is

$$
V = -m_1gx - m_2gy = -(m_1-m_2)gx + \text{const}.
$$

Dropping the constant, the Lagrangian is

$$
L = \frac{1}{2}(m_1+m_2)\dot x^2 + (m_1-m_2)gx.
$$

The Euler–Lagrange equation yields

$$
(m_1-m_2)g = (m_1+m_2)\ddot x,
$$

so

$$
\boxed{ \ddot x = \frac{m_1-m_2}{m_1+m_2}g. }
$$

Again, the unknown tension (a force of constraint) never appears in the Lagrangian derivation.

------

### 8.4 Block Sliding on a Movable Wedge

A block of mass $m$ slides on a frictionless wedge of mass $M$, which itself slides without friction on a horizontal table.  The wedge has angle $\alpha$.

Choose $q_1$ as the distance of the block down the slope and $q_2$ as the horizontal position of the wedge.  The velocity of the block relative to the inertial table is the vector sum of its velocity down the wedge and the wedge's horizontal velocity:

$$
\mathbf v_m = (\dot q_1\cos\alpha + \dot q_2,\; \dot q_1\sin\alpha).
$$

The kinetic energies are

$$
T_M = \frac{1}{2}M\dot q_2^2, \qquad
T_m = \frac{1}{2}m(\dot q_1^2 + \dot q_2^2 + 2\dot q_1\dot q_2\cos\alpha).
$$

Total kinetic energy:

$$
T = \frac{1}{2}(M+m)\dot q_2^2 + \frac{1}{2}m(\dot q_1^2 + 2\dot q_1\dot q_2\cos\alpha).
$$

Taking the table level as the reference for potential energy,

$$
V = -mgq_1\sin\alpha.
$$

The Lagrangian is

$$
L = \frac{1}{2}(M+m)\dot q_2^2 + \frac{1}{2}m(\dot q_1^2 + 2\dot q_1\dot q_2\cos\alpha) + mgq_1\sin\alpha.
$$

Because $L$ is independent of $q_2$, the corresponding generalized momentum is conserved:

$$
(M+m)\dot q_2 + m\dot q_1\cos\alpha = \text{const},
$$

which is the total horizontal momentum.  The $q_1$ equation gives

$$
mg\sin\alpha = m(\ddot q_1 + \ddot q_2\cos\alpha).
$$

Differentiating the momentum equation to eliminate $\ddot q_2$ yields

$$
\boxed{ \ddot q_1 = \frac{g\sin\alpha}{1 - \frac{m\cos^2\alpha}{M+m}}. }
$$

------

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

- In **Section 8.1** above, when $V$ depends only on $r$, the coordinate $\phi$ is ignorable and $p_\phi = mr^2\dot\phi$ (angular momentum) is conserved.
- In **Section 8.4**, $q_2$ was ignorable and the conserved momentum was the total horizontal momentum.

This profound connection between symmetry (invariance of $L$ under a coordinate transformation) and conservation laws is the essential content of **Noether's theorem (诺特定理)**.

> **Physical interpretation.**  The generalized momentum $p_i$ need not have the dimensions of ordinary momentum.  In polar coordinates, $p_\phi$ is angular momentum.  The generalized force $\partial L/\partial q_i$ need not have the dimensions of force either — in polar coordinates, $\partial L/\partial\phi$ is torque.  Nevertheless, the equation $\dot p_i = \partial L/\partial q_i$ is always the correct equation of motion.

------

## 10. Hamiltonian and Conservation Laws

Having defined the generalized momenta, we can introduce the **Hamiltonian**

$$
\mathcal H = \sum_{i=1}^n p_i\dot q_i - L.
$$

Using the chain rule and the Euler–Lagrange equations, one finds

$$
\frac{d\mathcal H}{dt} = -\frac{\partial L}{\partial t}.
$$

Consequently, **if the Lagrangian does not depend explicitly on time, the Hamiltonian is conserved:**

$$
\boxed{ \frac{\partial L}{\partial t} = 0 \quad\Longrightarrow\quad \frac{d\mathcal H}{dt} = 0. }
$$

When the transformation between Cartesian and generalized coordinates is time-independent (**natural coordinates**), the kinetic energy is a homogeneous quadratic function of the generalized velocities:

$$
T = \frac{1}{2}\sum_{j,k} A_{jk}(q)\,\dot q_j\dot q_k.
$$

Under these conditions, $\sum_i p_i\dot q_i = 2T$, and

$$
\mathcal H = 2T - (T - V) = T + V.
$$

Thus, for natural coordinates, the Hamiltonian equals the total mechanical energy of the system, and its conservation is equivalent to **energy conservation**.

Similarly:
- Translational invariance of $L$ implies conservation of total linear momentum.
- Rotational invariance of $L$ implies conservation of total angular momentum.

These results are all instances of **Noether's theorem**.

------

## 11. Summary

The main results of Lagrangian mechanics are summarized below.

1. **Spaces:**
   - Physical space: $\mathbb{R}^3$.
   - Configuration space for $N$ particles: $\mathbb{R}^{3N}$.
   - Phase space: $\mathbb{R}^{6N}$ (positions + momenta).

2. **Action:**
   - The action is a functional,
     $$
     S[q] = \int_{t_i}^{t_f} L(q,\dot q,t)\,dt.
     $$
   - Hamilton's principle: $\delta S = 0$.

3. **Euler–Lagrange equations:**
   - Stationarity implies
     $$
     \boxed{ \frac{d}{dt} \left( \frac{\partial L}{\partial \dot q^k} \right) - \frac{\partial L}{\partial q^k} =0, \qquad k=1,\dots,n. }
     $$

4. **Newton recovery:**
   - For $L=\frac{1}{2}m\dot q^2 - V(q)$, this reduces to Newton's second law:
     $$
     \boxed{ F = \frac{dp}{dt} = m\ddot q. }
     $$

5. **Generalized coordinates:**
   - $q_1,\dots,q_n$ reduce constrained problems to the same standard Euler–Lagrange form.
   - Constraint forces never appear explicitly.

6. **Generalized momenta:**
   - $p_i = \partial L/\partial \dot q_i$.
   - Ignorable coordinates yield conserved momenta (Noether's theorem).

7. **Hamiltonian:**
   - $\displaystyle\mathcal H = \sum p_i\dot q_i - L$.
   - Conserved when $\partial L/\partial t = 0$.
   - For natural coordinates, $\mathcal H = T + V$.
