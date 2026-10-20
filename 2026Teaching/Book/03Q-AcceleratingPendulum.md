# Pendulum in an Accelerating Carriage

## Table of Contents

1. [Physical Setup](#1-physical-setup)
2. [The Constraint](#2-the-constraint)
   - [2.1 Length Constraint](#21-length-constraint)
   - [2.2 Why This Is a Time-Dependent Constraint](#22-why-this-is-a-time-dependent-constraint)
   - [2.3 Parametrizing the Constraint](#23-parametrizing-the-constraint)
3. [Kinematics in the Inertial Frame](#3-kinematics-in-the-inertial-frame)
4. [Lagrangian in the Inertial Frame](#4-lagrangian-in-the-inertial-frame)
   - [4.1 Kinetic Energy](#41-kinetic-energy)
   - [4.2 Potential Energy](#42-potential-energy)
   - [4.3 Lagrangian](#43-lagrangian)
5. [Euler–Lagrange Equation](#5-eulerlagrange-equation)
   - [5.1 Compute $\frac{\partial L}{\partial \dot\theta}$](#51-compute-fracpartial-lpartial-dottheta)
   - [5.2 Compute $\frac{\partial L}{\partial \theta}$](#52-compute-fracpartial-lpartial-theta)
   - [5.3 Substitute into the Euler–Lagrange Equation](#53-substitute-into-the-eulerlagrange-equation)
6. [Effective-Gravity Form](#6-effective-gravity-form)
7. [Standard Pendulum Form](#7-standard-pendulum-form)
8. [Equilibrium Angle](#8-equilibrium-angle)
9. [Small Oscillations About Equilibrium](#9-small-oscillations-about-equilibrium)
10. [Key Takeaways](#10-key-takeaways)

---

## 1. Physical Setup

Consider a **simple pendulum** of length $l$ and bob mass $m$, suspended from a point fixed in a carriage. The carriage moves horizontally with constant acceleration $a$ relative to the ground. We choose the ground frame as an inertial frame.

Let the suspension point have horizontal position $X(t)=\frac{1}{2}at^2$. We assume the suspension point moves horizontally, so its vertical coordinate is fixed.

------

## 2. The Constraint

------

### 2.1 Length Constraint

The pendulum bob is constrained to remain a fixed distance $l$ from the suspension point. If the suspension point has coordinates $\left(\frac{1}{2}at^2,0\right)$, then the distance between the bob $(x,y)$ and the suspension point must satisfy
\[
\left(x-\frac{1}{2}at^2\right)^2+y^2=l^2.
\]
This is the constraint equation.

------

### 2.2 Why This Is a Time-Dependent Constraint

A constraint is called **scleronomic (定常约束)**, or time-independent, if it can be written as $f(q_1,q_2,\dots,q_n)=0$, with no explicit dependence on time.

A constraint is called **rheonomic (非定常约束)**, or time-dependent, if it has the form $f(q_1,q_2,\dots,q_n,t)=0$.

For the accelerating pendulum, the constraint is
\[
f(x,y,t) = \left(x-\frac{1}{2}at^2\right)^2+y^2-l^2=0.
\]
Since this equation contains $t$ explicitly, it is a **time-dependent constraint (非定常约束)**.

The explicit time dependence comes from the prescribed motion of the suspension point, $X(t)=\frac{1}{2}at^2$. Therefore, in the inertial ground frame, the constraint encodes two facts:

1. The bob remains a fixed distance $l$ from the suspension point.
2. The suspension point itself moves according to the prescribed motion of the carriage.

The explicit time dependence appears because the motion of the suspension point is given as an input, not solved as part of the system's dynamics.

However, the constraint does **not** say that the bob itself has acceleration $a$. The acceleration of the bob also depends on $\theta(t)$, $\dot\theta(t)$, and $\ddot\theta(t)$.

------

### 2.3 Parametrizing the Constraint

The constraint can be solved by introducing the **generalized coordinate (广义坐标)** $\theta$:
\[
x=\frac{1}{2}at^2+l\sin\theta,\qquad y=-l\cos\theta.
\]
This automatically satisfies
\[
\left(x-\frac{1}{2}at^2\right)^2+y^2=l^2.
\]
Indeed, $x-\frac{1}{2}at^2=l\sin\theta$, so
\[
\left(x-\frac{1}{2}at^2\right)^2+y^2 = l^2\sin^2\theta+l^2\cos^2\theta = l^2.
\]
Thus the system has one generalized coordinate, $\theta$.

------

## 3. Kinematics in the Inertial Frame

------

Using
\[
x=\frac{1}{2}at^2+l\sin\theta,\qquad y=-l\cos\theta,
\]
we compute the velocities. For the $x$-coordinate,
\[
\dot x = at+l\dot\theta\cos\theta.
\]
For the $y$-coordinate,
\[
\dot y = l\dot\theta\sin\theta.
\]
Therefore the speed squared is $v^2=\dot x^2+\dot y^2$. Substituting,
\[
v^2 = \left(at+l\dot\theta\cos\theta\right)^2 + \left(l\dot\theta\sin\theta\right)^2.
\]
Expanding,
\[
v^2 = a^2t^2 + 2atl\dot\theta\cos\theta + l^2\dot\theta^2\cos^2\theta + l^2\dot\theta^2\sin^2\theta.
\]
Since $\sin^2\theta+\cos^2\theta=1$, we obtain
\[
v^2 = a^2t^2 + 2atl\dot\theta\cos\theta + l^2\dot\theta^2.
\]

------

## 4. Lagrangian in the Inertial Frame

------

### 4.1 Kinetic Energy

The **kinetic energy** is $T=\frac{1}{2}mv^2$. Hence
\[
T= \frac{1}{2}m \left( a^2t^2 + 2atl\dot\theta\cos\theta + l^2\dot\theta^2 \right),
\]
so
\[
T = \frac{1}{2}ma^2t^2 + matl\dot\theta\cos\theta + \frac{1}{2}ml^2\dot\theta^2.
\]

------

### 4.2 Potential Energy

Choose gravitational **potential energy** as $V=mgy$. Since $y=-l\cos\theta$, we have
\[
V=-mgl\cos\theta.
\]

------

### 4.3 Lagrangian

The **Lagrangian (拉格朗日量)** is $L=T-V$. Therefore,
\[
L = \frac{1}{2}ma^2t^2 + matl\dot\theta\cos\theta + \frac{1}{2}ml^2\dot\theta^2 + mgl\cos\theta.
\]
The first term $\frac{1}{2}ma^2t^2$ does not depend on $\theta$ or $\dot\theta$, so it does not affect the **Euler–Lagrange equation**. We may drop it.

Thus an equivalent Lagrangian is
\[
L = \frac{1}{2}ml^2\dot\theta^2 + matl\dot\theta\cos\theta + mgl\cos\theta.
\]

------

## 5. Euler–Lagrange Equation

------

### 5.1 Compute $\frac{\partial L}{\partial \dot\theta}$

We compute
\[
\frac{\partial L}{\partial \dot\theta} = ml^2\dot\theta + matl\cos\theta.
\]
Taking the time derivative,
\[
\frac{d}{dt} \left( \frac{\partial L}{\partial \dot\theta} \right) = ml^2\ddot\theta + mal\cos\theta - matl\dot\theta\sin\theta.
\]

------

### 5.2 Compute $\frac{\partial L}{\partial \theta}$

We compute
\[
\frac{\partial L}{\partial \theta} = -matl\dot\theta\sin\theta - mgl\sin\theta.
\]

------

### 5.3 Substitute into the Euler–Lagrange Equation

Substituting into the Euler–Lagrange equation
\[
\frac{d}{dt} \left( \frac{\partial L}{\partial \dot\theta} \right) - \frac{\partial L}{\partial \theta} =0,
\]
we obtain
\[
ml^2\ddot\theta + mal\cos\theta - matl\dot\theta\sin\theta - \left( -matl\dot\theta\sin\theta - mgl\sin\theta \right) =0.
\]
The two terms involving $t\dot\theta\sin\theta$ cancel:
\[
-matl\dot\theta\sin\theta + matl\dot\theta\sin\theta =0.
\]
Thus
\[
ml^2\ddot\theta + mal\cos\theta + mgl\sin\theta =0.
\]
Dividing by $ml$ gives
\[
l\ddot\theta+a\cos\theta+g\sin\theta=0.
\]
Therefore, the equation of motion is
\[
\boxed{ \ddot\theta+\frac{g}{l}\sin\theta+\frac{a}{l}\cos\theta=0. }
\]

------

## 6. Effective-Gravity Form

------

> **Note.** We can combine the driving terms $g\sin\theta$ and $a\cos\theta$ into a single sinusoid. We want to write
> \[
> g\sin\theta+a\cos\theta
> \]
> in the form
> \[
> R\sin(\theta-\theta_0).
> \]
> Expand:
> \[
> R\sin(\theta-\theta_0) = R\sin\theta\cos\theta_0 - R\cos\theta\sin\theta_0.
> \]
> Compare coefficients with $g\sin\theta+a\cos\theta$. So we require
> \[
> R\cos\theta_0=g,\qquad -R\sin\theta_0=a.
> \]
> Hence
> \[
> R^2\cos^2\theta_0+R^2\sin^2\theta_0 = g^2+a^2,
> \]
> and thus $R=\sqrt{g^2+a^2}$. Also,
> \[
> \tan\theta_0 = \frac{\sin\theta_0}{\cos\theta_0} = \frac{-a/R}{g/R} = -\frac{a}{g},
> \]
> so
> \[
> \theta_0=-\tan^{-1}\frac{a}{g}.
> \]
> Therefore,
> \[
> \boxed{ g\sin\theta+a\cos\theta = \sqrt{g^2+a^2}\sin(\theta-\theta_0) }
> \]
> with
> \[
> \boxed{ \theta_0=-\tan^{-1}\frac{a}{g}. }
> \]

------

## 7. Standard Pendulum Form

------

Introducing $\phi = \theta - \theta_0$, the above equation becomes
\[
\ddot \phi + \frac{\sqrt{g^2+a^2}}{l}\sin\phi = 0.
\]

------

## 8. Equilibrium Angle

------

At equilibrium, $\ddot\theta=0$, so
\[
g\sin\theta+a\cos\theta=0.
\]
Hence $\tan\theta=-\frac{a}{g}$. Therefore the **equilibrium angle** is
\[
\boxed{ \theta_{\text{eq}}=-\arctan\left(\frac{a}{g}\right). }
\]

The negative sign means that if the carriage accelerates to the right, the pendulum tilts to the left relative to the vertical. This is consistent with the effective-gravity picture: in the carriage frame, the bob experiences gravity downward and a fictitious force to the left. The **effective gravitational field** is
\[
\mathbf g_{\text{eff}}=(-a,-g),
\]
with magnitude
\[
g_{\text{eff}}=\sqrt{g^2+a^2}.
\]
The pendulum aligns with this effective field at equilibrium.

------

## 9. Small Oscillations About Equilibrium

------

Let $\theta=\theta_{\text{eq}}+\eta$, where $\eta$ is a small displacement. The equation of motion is
\[
\ddot\theta+\frac{g}{l}\sin\theta+\frac{a}{l}\cos\theta=0.
\]
Define $g_{\text{eff}}=\sqrt{g^2+a^2}$. The equilibrium direction satisfies $g\sin\theta_{\text{eq}}+a\cos\theta_{\text{eq}}=0$. Linearizing about equilibrium gives
\[
\ddot\eta+\frac{g_{\text{eff}}}{l}\eta=0.
\]
Thus the small-oscillation angular frequency is
\[
\boxed{ \omega=\sqrt{\frac{\sqrt{g^2+a^2}}{l}}. }
\]
The corresponding period is
\[
\boxed{ T=2\pi\sqrt{\frac{l}{\sqrt{g^2+a^2}}}. }
\]

------

## 10. Key Takeaways

------

1. In the ground inertial frame, the pendulum constraint is
   \[
   \left(x-\frac{1}{2}at^2\right)^2+y^2=l^2.
   \]
2. This is a time-dependent, or rheonomic, constraint because it explicitly depends on $t$.
3. The constraint encodes both the fixed length of the pendulum and the prescribed motion of the suspension point.
4. The bob itself is not constrained to have acceleration $a$; its acceleration depends on $\theta(t)$.
5. In the inertial frame, the Lagrangian is obtained using the true inertial velocity of the bob,
   \[
   T=\frac{1}{2}m(\dot x^2+\dot y^2).
   \]
6. Applying the **Euler–Lagrange equation** gives
   \[
   \boxed{ \ddot\theta+\frac{g}{l}\sin\theta+\frac{a}{l}\cos\theta=0. }
   \]
7. The same result can be obtained in the accelerating carriage frame if the fictitious inertial force is included.
8. The equilibrium angle is
   \[
   \boxed{ \theta_{\text{eq}}=-\arctan\left(\frac{a}{g}\right). }
   \]
9. Small oscillations about equilibrium have angular frequency
   \[
   \boxed{ \omega=\sqrt{\frac{\sqrt{g^2+a^2}}{l}}. }
   \]
10. Equivalently, the period is
    \[
    \boxed{ T=2\pi\sqrt{\frac{l}{\sqrt{g^2+a^2}}}. }
    \]
