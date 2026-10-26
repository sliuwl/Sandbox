# Principle of Virtual Work

**Reading material:** Chapter 7 of *Classical Mechanics* by John R. Taylor; Chapter 1 of *Classical Mechanics* by Goldstein, Poole, Safko

## Table of Contents

1. [Virtual Displacements](#1-virtual-displacements)
   - [1.1 Definition](#11-definition)
   - [1.2 Physical Displacement vs. Virtual Displacement](#12-physical-displacement-vs-virtual-displacement)
2. [Virtual Work](#2-virtual-work)
   - [2.1 Definition](#21-definition)
3. [Principle of Virtual Work](#3-principle-of-virtual-work)
4. [Constraint Forces and Applied Forces](#4-constraint-forces-and-applied-forces)
5. [Why Constraint Forces Do No Virtual Work](#5-why-constraint-forces-do-no-virtual-work)
6. [Consequence for Generalized Coordinates](#6-consequence-for-generalized-coordinates)
7. [Conservative Systems](#7-conservative-systems)
8. [Newtonian vs. Lagrangian View of Static Equilibrium](#8-newtonian-vs-lagrangian-view-of-static-equilibrium)
   - [8.1 Newtonian Mechanics](#81-newtonian-mechanics)
   - [8.2 Lagrangian Mechanics](#82-lagrangian-mechanics)
   - [8.3 Connection with Euler–Lagrange Equation](#83-connection-with-eulerlagrange-equation)
9. [Static Version of the Principle of Least Action](#9-static-version-of-the-principle-of-least-action)
10. [Example: Seesaw in Static Equilibrium](#10-example-seesaw-in-static-equilibrium)
11. [d’Alembert’s Principle](#11-dalemberts-principle)
    - [11.1 Statement](#111-statement)
    - [11.2 Mathematical Formulation](#112-mathematical-formulation)
    - [11.3 Important Remarks](#113-important-remarks)
12. [Deriving the Euler–Lagrange Equation from d’Alembert’s Principle](#12-deriving-the-eulerlagrange-equation-from-dalemberts-principle)
    - [12.1 Conservative Forces](#121-conservative-forces)
    - [12.2 Non-Conservative Forces](#122-non-conservative-forces)
13. [Relationship Between Newtonian and Lagrangian Mechanics](#13-relationship-between-newtonian-and-lagrangian-mechanics)
14. [Example: Wheel Jack](#14-example-wheel-jack)
    - [14.1 Virtual Work](#141-virtual-work)
15. [Example: Plane Pendulum](#15-example-plane-pendulum)
    - [15.1 Pendulum with Variable Length](#151-pendulum-with-variable-length)
16. [Plane Rotor with Variable Radius](#16-plane-rotor-with-variable-radius)
    - [16.1 Variation in $\theta$, Keeping $r$ Fixed](#161-variation-in-θ-keeping-r-fixed)
    - [16.2 Variation in $r$, Keeping $\theta$ Fixed](#162-variation-in-r-keeping-θ-fixed)

---

## 1. Virtual Displacements

------

### 1.1 Definition

A **virtual displacement** is a hypothetical infinitesimal displacement of a system that is consistent with the constraints of the system at a fixed instant of time.

It does **not** need to be the actual physical displacement of the system.

A virtual displacement:

1. must be consistent with the constraints of the system;
2. must occur instantaneously, i.e. at fixed time.

The reason it must be instantaneous is that constraints may themselves change with time. Therefore, virtual displacements are taken with $\delta t = 0$.

------

### 1.2 Physical Displacement vs. Virtual Displacement

For a particle with position vector

$$
\vec r = \vec r(x,y,z,t),
$$

an infinitesimal physical displacement is

$$
\delta \vec r = \frac{\partial \vec r}{\partial x}\delta x + \frac{\partial \vec r}{\partial y}\delta y + \frac{\partial \vec r}{\partial z}\delta z + \frac{\partial \vec r}{\partial t}\delta t.
$$

For **generalized coordinates** $q_i$,

$$
\vec r = \vec r(q_i,t),
$$

so

$$
\delta \vec r = \sum_i \frac{\partial \vec r}{\partial q_i}\delta q_i + \frac{\partial \vec r}{\partial t}\delta t.
$$

For a **virtual displacement**, we set $\delta t = 0$. Therefore,

$$
\boxed{ \delta \vec r = \sum_i \frac{\partial \vec r}{\partial q_i}\delta q_i }
$$

------

## 2. Virtual Work

------

### 2.1 Definition

The **virtual work** done by a force $\vec F$ along a virtual displacement $\delta \vec r$ is

$$
\delta W = \vec F \cdot \delta \vec r.
$$

Using generalized coordinates,

$$
\delta W = \vec F \cdot \sum_i \frac{\partial \vec r}{\partial q_i}\delta q_i.
$$

Thus,

$$
\delta W = \sum_i \vec F \cdot \frac{\partial \vec r}{\partial q_i} \delta q_i.
$$

Define the **generalized force**

$$
Q_i = \vec F \cdot \frac{\partial \vec r}{\partial q_i}.
$$

Then

$$
\boxed{ \delta W = \sum_i Q_i \delta q_i }
$$

------

## 3. Principle of Virtual Work

In Newtonian mechanics, static equilibrium means that the net force acting on the system is zero:

$$
\vec F_{\text{net}} = 0.
$$

Therefore, the net virtual work done by all forces is also zero:

$$
\delta W = \vec F_{\text{net}}\cdot \delta \vec r = 0.
$$

Using generalized coordinates,

$$
\delta W = \sum_i Q_i^{\text{net}}\delta q_i.
$$

Hence, in static equilibrium,

$$
\boxed{ \sum_i Q_i^{\text{net}}\delta q_i = 0 }
$$

------

## 4. Constraint Forces and Applied Forces

The total generalized force may be decomposed into constraint forces and applied forces:

$$
Q_i^{\text{net}} = Q_i^c + Q_i,
$$

where:

- $Q_i^c$ is the generalized constraint force;
- $Q_i$ is the generalized applied force.

Then the virtual work condition becomes

$$
\sum_i Q_i^{\text{net}}\delta q_i = \sum_i Q_i^c \delta q_i + \sum_i Q_i \delta q_i = 0.
$$

For **ideal constraints**, the virtual work done by constraint forces is zero:

$$
\sum_i Q_i^c \delta q_i = 0.
$$

Therefore,

$$
\boxed{ \sum_i Q_i \delta q_i = 0 }
$$

This is the **principle of virtual work**:

> **Principle of Virtual Work.** In static equilibrium, the virtual work done by the applied forces is zero for all allowed virtual displacements.

------

## 5. Why Constraint Forces Do No Virtual Work

For a constraint equation

$$
g(q_i,t)=0,
$$

the generalized constraint force may be written as

$$
Q_i^c = \lambda \frac{\partial g}{\partial q_i},
$$

where $\lambda$ is a **Lagrange multiplier**.

> The constraint $g(q_i,t)=0$ tells us which configurations are allowed. If the system moves along the allowed surface, the value of $g$ does not change. Therefore, the gradient of $g$ points perpendicular to the allowed surface. Since an ideal constraint force only acts to stop the system from leaving the allowed surface, it must point in this perpendicular direction. That is why we write $Q_i^c=\lambda \frac{\partial g}{\partial q_i}.$ Here, $\frac{\partial g}{\partial q_i}$ gives the direction of the constraint force in generalized-coordinate space, and $\lambda$ tells how strong the force is and whether it points one way or the opposite way.



The virtual work of constraint forces is
$$
\delta W_c = \sum_i Q_i^c\delta q_i = \sum_i \lambda \frac{\partial g}{\partial q_i} \delta q_i.
$$

But

$$
\delta g = \sum_i \frac{\partial g}{\partial q_i}\delta q_i + \frac{\partial g}{\partial t}\delta t.
$$

For a virtual displacement,

$$
\delta t = 0.
$$

So

$$
\delta g = \sum_i \frac{\partial g}{\partial q_i}\delta q_i.
$$

Since virtual displacements satisfy the constraint,

$$
\delta g = 0.
$$

> For a **virtual displacement**, we compare two infinitesimally nearby configurations **at the same time $t$**, both of which are allowed by the constraint. Therefore the varied configuration must also lie on the constraint surface. So if the original configuration satisfies
>
> $g(q_i,t)=0,$
>
> then the virtually displaced configuration also satisfies, to first order,
>
> $g(q_i+\delta q_i,t)=0.$
>
> Expanding,
>
> $g(q_i+\delta q_i,t) = g(q_i,t) + \sum_i \frac{\partial g}{\partial q_i}\delta q_i + O(\delta q^2).$
>
> Therefore, to first order, $\sum_i \frac{\partial g}{\partial q_i}\delta q_i=0.$ That is exactly $\delta g=0.$

Therefore,
$$
\boxed{ \delta W_c = \lambda \delta g = 0 }
$$

------

## 6. Consequence for Generalized Coordinates

Because the generalized coordinate variations $\delta q_i$ are independent,

$$
\sum_i Q_i \delta q_i = 0
$$

implies

$$
\boxed{ Q_i = 0 }
$$

for each $i$.

Thus, in static equilibrium:

> **Equilibrium Condition.** Each component of generalized force is independently zero.

------

## 7. Conservative Systems

For a **conservative system**,

$$
Q_i = -\frac{\partial V}{\partial q_i},
$$

where $V$ is the potential energy.

The equilibrium condition becomes

$$
-\frac{\partial V}{\partial q_i}=0.
$$

Therefore,

$$
\boxed{ \frac{\partial V}{\partial q_i}=0 }
$$

This means:

> **Conservative Equilibrium.** Static equilibrium of a conservative system occurs at stationary points of the potential energy.

The condition is expressed entirely in terms of scalar quantities.

------

## 8. Newtonian vs. Virtual-Work  View of Static Equilibrium

------

### 8.1 Newtonian Mechanics

In Newtonian mechanics, static equilibrium means:

$$
\sum \vec F = 0, \qquad \sum \vec \tau = 0.
$$

That is, the sum of forces and torques on the system is zero.

However, individual forces may not be zero.

------

### 8.2 Virtual Work 

Based on the principle of virtual work, static equilibrium means:

$$
Q_i = 0
$$

for every generalized coordinate $q_i$.

Equivalently, for a conservative system,

$$
\frac{\partial V}{\partial q_i}=0.
$$

Thus, each generalized force vanishes independently.

------

### 8.3 Connection with Euler–Lagrange Equation

For static equilibrium, there is no time evolution:

$$
\dot q_i = 0, \qquad \ddot q_i = 0.
$$

The Euler–Lagrange equation

$$
\frac{d}{dt} \left( \frac{\partial L}{\partial \dot q_i} \right) - \frac{\partial L}{\partial q_i} = 0
$$

reduces to

$$
\frac{\partial V}{\partial q_i}=0
$$

when

$$
L = T - V.
$$

Thus, solving a static problem is a special case of the Euler–Lagrange equation.

------

## 9. Static Version of the Principle of Least Action

The principle of virtual work may be viewed as a static analogue of the principle of least action.

If one considers all possible virtual displacements, the correct equilibrium configuration is the one for which the total virtual work is zero:

$$
\delta W = 0.
$$

For a conservative system,

$$
\delta W = -\delta V.
$$

Therefore,

$$
\delta V = 0.
$$

Thus, the equilibrium configuration is a stationary point of the potential energy.

------

## 10. Example: Seesaw in Static Equilibrium

We consider a seesaw with two masses $m$ and $M$, located on opposite sides of the pivot.

Let the length of the seesaw be $L$. The distance of mass $M$ from the pivot is $\frac{L}{2}$, and the distance of mass $m$ from the pivot is $\frac{L}{2}-a$.

The potential energy is

$$
V = Mg\frac{L}{2}\sin \theta - mg\left(\frac{L}{2}-a\right)\sin\theta.
$$

For static equilibrium,

$$
\frac{\partial V}{\partial \theta}=0.
$$

Thus,

$$
Mg\frac{L}{2}\cos\theta - mg\left(\frac{L}{2}-a\right)\cos\theta = 0.
$$

Assuming $\cos\theta \neq 0$,

$$
M\frac{L}{2} = m\left(\frac{L}{2}-a\right).
$$

Solving for $a$,

$$
m a = \frac{mL}{2} - \frac{ML}{2},
$$

so

$$
\boxed{ a = \frac{m-M}{2m}L }
$$

------

## 11. d’Alembert’s Principle

------

### 11.1 Statement

d’Alembert’s principle extends the principle of virtual work to dynamical systems.

A system undergoing **acceleration** relative to an inertial frame may be described as being in **equilibrium in a non-inertial frame co-moving with the system**, provided that the appropriate inertial, or fictitious, forces are included in the force balance.

If the system accelerates with acceleration $\vec a$, the fictitious force is

$$
\vec F_{\text{fict}} = -m\vec a.
$$

Since

$$
\vec a = \ddot{\vec r},
$$

we can write

$$
\boxed{ \vec F_{\text{fict}} = -m\ddot{\vec r} }
$$

> Consider a person standing in an elevator that accelerates upward with acceleration $a$. From the ground frame, the person is not in static equilibrium, because the forces do not balance: the normal force $N$ from the floor is larger than the weight $mg$, and Newton’s second law gives $N-mg=ma$. However, in the elevator’s own accelerating rest frame, the person appears to be at rest relative to the elevator. Since this frame is non-inertial, we must include a fictitious force acting downward with magnitude $ma$. Then the person can be treated as being in static equilibrium in that accelerating frame, with the force balance $N-mg-ma=0$. This gives $N=m(g+a)$, the same result as the ground-frame analysis. Thus, an accelerating system may be treated as being in equilibrium in its own accelerating rest frame, provided fictitious forces are included.

---

### 11.2 Mathematical Formulation

In the rest frame of a dynamical system, the virtual work done by the applied and fictitious forces combined is zero:

$$
\sum_i \left( Q_i + Q_i^{\text{fict}} \right) \delta q_i = 0.
$$

The generalized fictitious force is

$$
Q_i^{\text{fict}} = \vec F_{\text{fict}} \cdot \frac{\partial \vec r}{\partial q_i}.
$$

Thus,

$$
Q_i^{\text{fict}} = -m\ddot{\vec r} \cdot \frac{\partial \vec r}{\partial q_i}.
$$

Therefore,

$$
\boxed{ \sum_i \left( Q_i - m\ddot{\vec r} \cdot \frac{\partial \vec r}{\partial q_i} \right) \delta q_i = 0 }
$$

Equivalently,

$$
\boxed{ \sum_i \left( \vec F - m\ddot{\vec r} \right) \cdot \frac{\partial \vec r}{\partial q_i} \delta q_i = 0 }
$$

This is the mathematical statement of d’Alembert’s principle.

------

### 11.3 Important Remarks

Although this resembles Newton’s second law, it is not the same statement. The equation $\vec F = m\ddot{\vec r}$ cannot simply be written here because:

1. $\vec F$ is not the total force; it is the applied force.
2. The equation appears inside a dot product with virtual displacements.
3. It is written in generalized coordinates and does not involve constraint forces explicitly.

------

## 12. Deriving the Euler–Lagrange Equation from d’Alembert’s Principle

Starting from

$$
\sum_i \left( \vec F - m\ddot{\vec r} \right) \cdot \frac{\partial \vec r}{\partial q_i} \delta q_i = 0,
$$

define

$$
Q_i = \vec F \cdot \frac{\partial \vec r}{\partial q_i}.
$$

Then

$$
\sum_i \left( Q_i - m\ddot{\vec r} \cdot \frac{\partial \vec r}{\partial q_i} \right) \delta q_i = 0.
$$

The velocity is
\[
\mathbf v=\dot{\mathbf r} = \sum_j \frac{\partial \mathbf r}{\partial q_j}\dot q_j + \frac{\partial \mathbf r}{\partial t}.
\]
Therefore,
\[
\frac{\partial \mathbf v}{\partial \dot q_i} = \frac{\partial \mathbf r}{\partial q_i}.
\]
This identity is important because it allows us to connect the inertial term with derivatives of the kinetic energy.

For a single particle, $T=\frac12 m v^2 = \frac12 m \mathbf v\cdot \mathbf v.$

First compute the derivative of $T$ with respect to $\dot q_i$:
\[
\frac{\partial T}{\partial \dot q_i} = m\mathbf v\cdot \frac{\partial \mathbf v}{\partial \dot q_i} = m\mathbf v\cdot \frac{\partial \mathbf r}{\partial q_i}
\]
Now differentiate this with respect to time:
\[
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot q_i}\right) = \frac{d}{dt} \left( m\mathbf v\cdot \frac{\partial \mathbf r}{\partial q_i} \right).
\]
Using the product rule,
\[
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot q_i}\right) = m\dot{\mathbf v}\cdot \frac{\partial \mathbf r}{\partial q_i} + m\mathbf v\cdot \frac{d}{dt}\left(\frac{\partial \mathbf r}{\partial q_i}\right) = m\ddot{\mathbf r}\cdot \frac{\partial \mathbf r}{\partial q_i} + m\mathbf v\cdot \frac{d}{dt}\left(\frac{\partial \mathbf r}{\partial q_i}\right)
\]


Next, compute $\partial T/\partial q_i$. We have
\[
\frac{\partial T}{\partial q_i} = m\mathbf v\cdot \frac{\partial \mathbf v}{\partial q_i} = m\mathbf v\cdot \frac{d}{dt}\left(\frac{\partial \mathbf r}{\partial q_i}\right)
\]

> We are interchanging two derivative operations: $\frac{\partial}{\partial q_i}$ and $\frac{d}{dt}$. The position function $\mathbf r(q,t)$ must be sufficiently differentiable and well-behaved, so that taking a time derivative and taking a derivative with respect to a generalized coordinate give the same result regardless of order.

Thus, the inertial term can be written as
\[
\boxed{ m\ddot{\mathbf r}\cdot \frac{\partial \mathbf r}{\partial q_i} = \frac{d}{dt}\left(\frac{\partial T}{\partial \dot q_i}\right) - \frac{\partial T}{\partial q_i} }.
\]
Substituting this identity back into d’Alembert’s principle, we obtain
\[
\sum_i \left[ Q_i - \frac{d}{dt}\left(\frac{\partial T}{\partial \dot q_i}\right) + \frac{\partial T}{\partial q_i} \right]\delta q_i=0.
\]
Because the generalized coordinates $q_i$ are independent, then the virtual displacements $\delta q_i$ are independent. Therefore, each coefficient of $\delta q_i$ must vanish separately:
\[
\boxed{ \frac{d}{dt}\left(\frac{\partial T}{\partial \dot q_i}\right) - \frac{\partial T}{\partial q_i} = Q_i }.
\]
This is Lagrange’s equation in terms of generalized forces. 

------

### 12.1 Conservative Forces

For conservative forces,

$$
Q_i = -\frac{\partial V}{\partial q_i}.
$$

Then

$$
\frac{d}{dt} \left( \frac{\partial T}{\partial \dot q_i} \right) - \frac{\partial T}{\partial q_i} = -\frac{\partial V}{\partial q_i}.
$$

Rearranging,

$$
\frac{d}{dt} \left( \frac{\partial T}{\partial \dot q_i} \right) - \frac{\partial (T-V)}{\partial q_i} = 0.
$$

Since

$$
L = T - V,
$$

we obtain

$$
\boxed{ \frac{d}{dt} \left( \frac{\partial L}{\partial \dot q_i} \right) - \frac{\partial L}{\partial q_i} = 0 }
$$

This is the **Euler–Lagrange equation**.

------

### 12.2 Non-Conservative Forces

If the system contains non-conservative generalized forces $Q_i^{\text{nc}}$, then

$$
\boxed{ \frac{d}{dt} \left( \frac{\partial L}{\partial \dot q_i} \right) - \frac{\partial L}{\partial q_i} = Q_i^{\text{nc}} }
$$

------

## 13. Relationship Between Newtonian and Lagrangian Mechanics

d’Alembert’s principle provides the bridge between Newtonian mechanics and Lagrangian mechanics.

$$
\text{Newtonian mechanics} \quad \longrightarrow \quad \text{d’Alembert’s principle} \quad \longrightarrow \quad \text{Lagrangian mechanics}
$$

In standard conservative systems,

$$
\boxed{ L = T - V }
$$

However, the Lagrangian formulation can be more general than simply $T-V$.

It is a different theoretical framework, not merely a rewriting of Newtonian mechanics.

------

## 14. Example: Wheel Jack

A wheel jack (千斤顶) is an articulated machine used to lift a heavy load $P$ using an applied force $F$ on a crank. The jack consists of two rigid bars of length $l$, forming a lozenge shape. A threaded screw changes length by $h$ for each full revolution of the crank. The crank arm has length $a$.

![Wheel jack diagram](LectureNotesFigures/04wheeljack.png)

![Wheel jack solution diagram](LectureNotesFigures/04wheeljack2.png)

Let the crank rotate through a virtual angle $\delta \alpha$.

The corresponding screw displacement is

$$
\delta x = \frac{h}{2\pi}\delta \alpha.
$$

Because the screw pulls symmetrically,

$$
\delta OB = \frac{\delta x}{2}.
$$

From the geometry,

$$
OA^2 + OB^2 = l^2.
$$

Since $l$ is invariant,

$$
2OA \, \delta OA + 2OB \, \delta OB = 0.
$$

Thus,

$$
\delta OA = -\frac{OB}{OA}\delta OB.
$$

Using

$$
\tan\theta = \frac{OA}{OB},
$$

we get

$$
\delta OA = -\frac{\delta OB}{\tan\theta}.
$$

The vertical displacement of the load is twice this:

$$
\delta CA = 2\delta OA = -\frac{\delta x}{\tan\theta}.
$$

Substituting $\delta x$,

$$
\delta CA = -\frac{h}{2\pi\tan\theta}\delta\alpha.
$$

------

### 14.1 Virtual Work

The load $P$ acts at $A$. Its virtual work is

$$
\delta W_P = P\frac{h}{2\pi\tan\theta}\delta\alpha.
$$

The applied force $F$ acts on the crank of length $a$, so its virtual work is

$$
\delta W_F = -Fa\delta\alpha.
$$

By the principle of virtual work,

$$
\delta W = \delta W_P+\delta W_F = 0.
$$

Therefore,

$$
\left[ \frac{Ph}{2\pi\tan\theta} - Fa \right]\delta\alpha = 0.
$$

Since $\delta\alpha$ is arbitrary,

$$
\frac{Ph}{2\pi\tan\theta} = Fa.
$$

Thus,

$$
\boxed{ \frac{P}{F} = \frac{2\pi a\tan\theta}{h} }
$$



For example, if

$$
a=20\text{ cm}, \qquad h=0.2\text{ cm}, \qquad \tan\theta=0.577,
$$

then

$$
\frac{P}{F} \approx 363.
$$

This shows that a small applied force can lift a much larger load.

------

## 15. Example: Plane Pendulum

We consider a pendulum of length $l$, mass $m$, and angular coordinate $\theta$.

For a virtual angular displacement $\delta\theta$, the displacement along the arc is

$$
l\delta\theta.
$$

The vertical change is

$$
\delta h = l\delta\theta\sin\theta.
$$

Using d’Alembert’s principle, we include the fictitious force

$$
-m\ddot\theta l.
$$

The virtual work equation is

$$
-mg l\sin\theta \, \delta\theta - m\ddot\theta l(l\delta\theta) = 0.
$$

Thus,

$$
-mg l\sin\theta - ml^2\ddot\theta = 0.
$$

Divide by $ml$:

$$
-g\sin\theta - l\ddot\theta = 0.
$$

Therefore,

$$
\boxed{ \ddot\theta = -\frac{g}{l}\sin\theta }
$$

or

$$
\boxed{ \ddot\theta + \frac{g}{l}\sin\theta = 0 }
$$

This is the equation of motion of the plane pendulum.

------

### 15.1 Pendulum with Variable Length

If the pendulum length $l$ changes with time, the tangential acceleration contains an extra term:

$$
a_\theta = l\ddot\theta + 2\dot l \dot\theta.
$$

Using d’Alembert’s principle,

$$
-mg(l\delta\theta \sin\theta) - m \left( l\ddot\theta + 2\dot l\dot\theta \right) l\delta\theta = 0.
$$

Hence,

$$
-mgl\sin\theta = ml^2\ddot\theta + 2ml\dot l\dot\theta.
$$

This can be written as

$$
\boxed{ \frac{d}{dt} \left( ml^2\dot\theta \right) = -mgl\sin\theta }
$$

If there is no gravitational field,

$$
g=0,
$$

then

$$
\frac{d}{dt} \left( ml^2\dot\theta \right) = 0.
$$

Thus,

$$
\boxed{ ml^2\dot\theta = \text{constant} }
$$

This is conservation of angular momentum.

------

## 16. Plane Rotor with Variable Radius

We consider a mass moving in a plane with polar coordinates $(r,\theta)$. A radial force $F$ may be applied, and gravity may also act.

The radial acceleration is

$$
a_r = \ddot r - r\dot\theta^2.
$$

------

### 16.1 Variation in $\theta$, Keeping $r$ Fixed

If we vary $\theta$ while keeping $r$ fixed, the generalized equation gives

$$
\boxed{ \frac{d}{dt} \left( mr^2\dot\theta \right) = -mgr\sin\theta }
$$

This is the angular equation of motion.

If $g=0$, then

$$
\boxed{ \frac{d}{dt} \left( mr^2\dot\theta \right) = 0 }
$$

so angular momentum is conserved.

------

### 16.2 Variation in $r$, Keeping $\theta$ Fixed

For a virtual radial displacement $\delta r$:

- the applied radial force does work

  $$
  -F\delta r;
  $$

- gravity does work

  $$
  mg\cos\theta\,\delta r;
  $$

- the fictitious force contributes

  $$
  -m(\ddot r-r\dot\theta^2)\delta r.
  $$

The virtual work condition is

$$
mg\cos\theta \, \delta r - F\delta r - m(\ddot r-r\dot\theta^2)\delta r = 0.
$$

Since $\delta r$ is arbitrary,

$$
mg\cos\theta - F - m(\ddot r-r\dot\theta^2) = 0.
$$

Therefore,

$$
\boxed{ m(\ddot r-r\dot\theta^2) = -F + mg\cos\theta }
$$

This is the radial equation of motion.
