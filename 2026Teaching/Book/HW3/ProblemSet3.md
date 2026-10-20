# Problem Set 3
---

**Total Points: 90 points**
**Deadline: 9:00 pm, Oct. 30th**

All answers must be **handwritten**, then scanned or photographed, and submitted via Canvas.

**Late submissions will incur a penalty of 5 points per day. Submissions more than 3 days late will not be accepted.**

---

## Problem 1: Non-uniqueness of Lagrangian [15 points]

Consider a Lagrangian $L'=L+df/dt$, where the Lagrangian is $L = L(q_k,\dot{q}_k,t)$ and the function $f=f(q_k,t)$.

(a) Show that $L' = L'(q_k,\dot{q}_k,t)$, that is, $L'$ also depends on $q_k$, $\dot{q}_k$, and $t$. Show that this would not generally be true if $f$ were allowed to depend upon the $\dot{q}_k$. [10 points]

(b) Show that $L'$ obeys Euler–Lagrange equations if $L$ does, by substituting $L'$ into Euler–Lagrange equations. Therefore, the equations of motion are the same using $L'$ as using $L$, so the Lagrangian of a particle is not unique. [10 points]

---

## Problem 2: Generalized mechanics [15 points]

The term generalized mechanics refers to a formulation of classical mechanics in which the Lagrangian contains time derivatives of $q_i$ higher than the first. Problems for which $\dddot{x} = f(x, \dot{x}, \ddot{x}, t)$ have been referred to as "jerky" mechanics. Such equations of motion have interesting applications in chaos theory. By applying the methods of the calculus of variations, show that if there is a Lagrangian of the form $L(q_i, \dot{q}_i, \ddot{q}_i, t)$, and Hamilton's principle holds with the zero variation of both $q_i$ and $\dot{q}_i$ at the end points, then the corresponding Euler–Lagrange equations are
\[
\frac{d^2}{dt^2}\left(\frac{\partial L}{\partial \ddot{q}_i}\right) - \frac{d}{dt}\left(\frac{\partial L}{\partial \dot{q}_i}\right) + \frac{\partial L}{\partial q_i} = 0, \quad i = 1, 2, \dots, n.
\]
Apply this result to the Lagrangian
\[
\mathcal{L} = -\frac{m}{2} q \ddot{q} - \frac{k}{2} q^2.
\]

---

## Problem 3: Damped harmonic oscillator via time-dependent Lagrangian [15 points]

In certain situations, particularly one-dimensional systems, it is possible to incorporate frictional effects without introducing the dissipation function. As an example, find the equations of motion for the Lagrangian

$$
L = e^{\gamma t}\left(\frac{m \dot{q}^2}{2} - \frac{k q^2}{2}\right).
$$

Are there any constants of motion? Suppose a point transformation is made of the form

$$
s = e^{\gamma t / 2} q.
$$

What is the effective Lagrangian in terms of $s$? Find the equation of motion for $s$. 

---

## Problem 4: Particle sliding on a movable wedge [15 points]

A particle of mass $m$ slides without friction on a wedge of angle $\alpha$ and mass $M$ that can move without friction on a smooth horizontal surface, as shown in the figure. Treating the constraint of the particle on the wedge by the method of **Lagrange multipliers**, find the equations of motion for the particle and wedge. Also obtain an expression for the forces of constraint. Calculate the work done in time $t$ by the forces of constraint acting on the particle and on the wedge. What are the constants of motion for the system? 



<img src="../Goldstein/images/3e97bec402c000442c8f97ce62f772b8efb4aff46dadb2fcc3fe04ce374ea8be.jpg" alt="Particle on a wedge" width="300px">

---

## Problem 5: Spring pendulum with impulsive blow [15 points]

A particle of mass $m$ is suspended by a massless spring of length $L$. It hangs, without initial motion, in a gravitational field of strength $g$. It is struck by an impulsive horizontal blow, which introduces an angular velocity $\omega$. The impulse is used only to set the initial condition,
\[
\theta(0)=0, \qquad \dot\theta(0)=\omega,
\]
and is not included in the subsequent Lagrangian dynamics. If $\omega$ is sufficiently small, it is obvious that the mass moves as a simple pendulum. If $\omega$ is sufficiently large, the mass will rotate about the support. Use a Lagrange multiplier to determine the conditions under which the string becomes slack (meaning that the **tension drops to zero**) at some point in the motion.

---

## Problem 6: Separability of Lagrange's equations [15 points]

Suppose a mechanical system is described by generalized coordinates $q_i$, and assume that both the kinetic energy and potential energy are **separable**. By separable, we mean that each coordinate $q_i$ appears only in its own term, with no coupling between different coordinates. Specifically, suppose
\[
T=\sum_i f_i(q_i)\dot q_i^2, \qquad V=\sum_i V_i(q_i),
\]
where $f_i(q_i)$ and $V_i(q_i)$ depend only on the single coordinate $q_i$. Show that each generalized coordinate $q_i$ satisfies its own independent equation of motion, uncoupled from the other coordinates. Then show that, for each coordinate $q_i$, there is a conserved quantity.
