# Examples of Generalized Forces

## Table of Contents

1. [Newton's Second Law in Polar Coordinates](#1-newtons-second-law-in-polar-coordinates)
   - [1.1 Generalized Forces](#11-generalized-forces)
   - [1.2 Derivation from Lagrange's Equation](#12-derivation-from-lagranges-equation)
     - [1.2.1 Radial Coordinate](#121-radial-coordinate)
     - [1.2.2 Angular Coordinate](#122-angular-coordinate)
2. [Velocity-Dependent Forces](#2-velocity-dependent-forces)
   - [2.1 Method 1: Generalized Force](#21-method-1-generalized-force)
   - [2.2 Method 2: Velocity-Dependent Potential](#22-method-2-velocity-dependent-potential)
3. [Lorentz Force](#3-lorentz-force)
   - [3.1 Lorentz Force as a Generalized Force](#31-lorentz-force-as-a-generalized-force)
   - [3.2 Uniform Magnetic Field in the z-Direction](#32-uniform-magnetic-field-in-the-z-direction)
   - [3.3 Helical Trajectory](#33-helical-trajectory)
   - [3.4 Velocity-Dependent Potential for Electromagnetism](#34-velocity-dependent-potential-for-electromagnetism)
4. [Friction and Dissipation](#4-friction-and-dissipation)
   - [4.1 Examples of Friction](#41-examples-of-friction)
   - [4.2 Free Particle Under Friction](#42-free-particle-under-friction)
   - [4.3 Generalized Friction Force and the Dissipation Function](#43-generalized-friction-force-and-the-dissipation-function)
5. [Damped Pendulum](#5-damped-pendulum)
6. [Generalized Constraint Force](#6-generalized-constraint-force)
   - [6.1 Particle Sliding on a Hemisphere](#61-particle-sliding-on-a-hemisphere)

---

## 1. Newton's Second Law in Polar Coordinates

In Cartesian coordinates, Newton's second law takes the simple form $\vec F=m\vec a$. In curvilinear coordinates, such as polar coordinates $(r,\theta)$, the components of acceleration are more complicated. The formalism of **generalized forces (广义力)** allows us to write the correct equations of motion systematically for any choice of coordinates.

We begin with Newton's second law expressed in polar basis vectors:

$$
\vec F = m\vec a.
$$

The force is decomposed as

$$
\vec F = F_r\,\hat r + F_\theta\,\hat\theta.
$$

The polar basis vectors are written in the Cartesian basis as

$$
\hat r = \cos\theta\,\hat x + \sin\theta\,\hat y,
$$

$$
\hat\theta = -\sin\theta\,\hat x + \cos\theta\,\hat y.
$$

The position vector is

$$
\vec r = r\,\hat r.
$$

------

### 1.1 Generalized Forces

The **generalized force** associated with a coordinate $q_i$ is defined by

$$
Q_i = \vec F\cdot\frac{\partial\vec r}{\partial q_i}.
$$

For the radial coordinate $q_i=r$, we have

$$
\frac{\partial\vec r}{\partial r} = \hat r,
$$

so

$$
Q_r = \vec F\cdot\hat r = F_r.
$$

For the angular coordinate $q_i=\theta$, we use

$$
\frac{\partial\vec r}{\partial\theta} = r\frac{\partial\hat r}{\partial\theta}.
$$

Since

$$
\frac{\partial\hat r}{\partial\theta} = -\sin\theta\,\hat x + \cos\theta\,\hat y = \hat\theta,
$$

we obtain

$$
Q_\theta = \vec F\cdot(r\hat\theta) = rF_\theta.
$$

> **Physical interpretation.** $Q_r$ is the ordinary radial force $F_r$, whereas $Q_\theta$ is a torque (with units of force times length). This is natural: the generalized force conjugate to an angle is a torque, just as the generalized force conjugate to a length is an ordinary force.

------

### 1.2 Derivation from Lagrange's Equation

We now show that Lagrange's equations reproduce Newton's second law in polar coordinates. The kinetic energy is

$$
T = \frac12 m\left(\dot r^2 + r^2\dot\theta^2\right).
$$

Since there is no potential energy in this example, the Lagrangian is simply $L=T$. The Lagrange equation with a generalized force $Q_i$ reads

$$
\frac{d}{dt}\left(\frac{\partial L}{\partial\dot q_i}\right) - \frac{\partial L}{\partial q_i} = Q_i.
$$

------

#### 1.2.1 Radial Coordinate

Setting $q_i=r$, we find

$$
\frac{d}{dt}(m\dot r) - mr\dot\theta^2 = Q_r = F_r.
$$

Therefore,

$$
F_r = m\ddot r - mr\dot\theta^2 = m\left(\ddot r - r\dot\theta^2\right).
$$

This is precisely the radial component of $\vec F=m\vec a$ in polar coordinates.

------

#### 1.2.2 Angular Coordinate

Setting $q_i=\theta$, we find

$$
\frac{d}{dt}\left(mr^2\dot\theta\right) - 0 = Q_\theta = rF_\theta.
$$

Expanding the time derivative gives

$$
2mr\dot r\dot\theta + mr^2\ddot\theta = rF_\theta.
$$

Dividing by $r$ and rearranging,

$$
F_\theta = m\left(r\ddot\theta + 2\dot r\dot\theta\right).
$$

This is the angular component of $\vec F=m\vec a$.

------

## 2. Velocity-Dependent Forces

A velocity-dependent force has the form

$$
\vec F = \vec F(\vec r,\vec v).
$$

Common examples include the magnetic Lorentz force and friction. Because such a force cannot be expressed as the gradient of an ordinary potential $V(\vec r)$, two methods are used to incorporate it into the Lagrangian framework.

------

### 2.1 Method 1: Generalized Force

We simply define the generalized force in the usual way,

$$
Q_i = \vec F\cdot\frac{\partial\vec r}{\partial q_i},
$$

and place it directly on the right-hand side of Lagrange's equation:

$$
\frac{d}{dt}\left(\frac{\partial L}{\partial\dot q_i}\right) - \frac{\partial L}{\partial q_i} = Q_i.
$$

In this approach, the dynamics are not fully encoded in the Lagrangian alone.

------

### 2.2 Method 2: Velocity-Dependent Potential

Alternatively, one may seek a **velocity-dependent potential (与速度相关的势)** $U(\vec r,\vec v)$ such that the Lagrangian

$$
L = T - U
$$

contains all the dynamics. The resulting generalized force then appears automatically from the left-hand side of Lagrange's equation. However, finding such a potential for an arbitrary velocity-dependent force is not always possible.

------

## 3. Lorentz Force

The Lorentz force on a particle of charge $q$ moving in electric and magnetic fields is

$$
\vec F = q\vec E + q\,\vec v\times\vec B.
$$

------

### 3.1 Lorentz Force as a Generalized Force

Using Method 1, the generalized force is

$$
Q_i = \vec F\cdot\frac{\partial\vec r}{\partial q_i}.
$$

Therefore,

$$
Q_i = q\vec E\cdot\frac{\partial\vec r}{\partial q_i} + q(\vec v\times\vec B)\cdot\frac{\partial\vec r}{\partial q_i}.
$$

An important identity connects the derivative of the position vector with the derivative of the velocity:

$$
\frac{\partial\vec r}{\partial q_i} = \frac{\partial\dot{\vec r}}{\partial\dot q_i} = \frac{\partial\vec v}{\partial\dot q_i}.
$$

Hence we may write

$$
Q_i = \bigl[q\vec E + q(\vec v\times\vec B)\bigr]\cdot\frac{\partial\vec v}{\partial\dot q_i}.
$$

------

### 3.2 Uniform Magnetic Field in the z-Direction

Consider the special case

$$
\vec B = B\,\hat z, \qquad \vec E = 0.
$$

Then

$$
Q_i = q(\vec v\times\vec B)\cdot\frac{\partial\vec v}{\partial\dot q_i}.
$$

Evaluating the cross product,

$$
\vec v\times\vec B = 
\begin{vmatrix}
\hat x & \hat y & \hat z \\
\dot x & \dot y & \dot z \\
0 & 0 & B
\end{vmatrix}
= B\dot y\,\hat x - B\dot x\,\hat y.
$$

The generalized forces in Cartesian coordinates are therefore

$$
Q_x = qB\dot y, \qquad Q_y = -qB\dot x, \qquad Q_z = 0.
$$

Using the free-particle Lagrangian

$$
L = \frac12 m\left(\dot x^2 + \dot y^2 + \dot z^2\right),
$$

Lagrange's equations give

$$
m\ddot x = qB\dot y, \qquad m\ddot y = -qB\dot x, \qquad m\ddot z = 0.
$$

Thus,

$$
\ddot x = \frac{qB}{m}\dot y, \qquad \ddot y = -\frac{qB}{m}\dot x, \qquad \ddot z = 0.
$$

> **Note.** The magnetic force acts perpendicular to the velocity, so it does no work and does not change the speed of the particle. Only the direction of motion is altered.

------

### 3.3 Helical Trajectory

A solution to the equations above is uniform motion along $z$ combined with circular motion in the $xy$-plane:

$$
x(t) = r\cos\omega t, \qquad y(t) = -r\sin\omega t, \qquad z(t) = v_z t,
$$

with the **cyclotron frequency (回旋频率)**

$$
\omega = \frac{qB}{m}.
$$

Substituting this ansatz verifies that it satisfies the equations of motion. The resulting path is a **helix (螺旋线)** whose axis lies along the direction of the magnetic field.

------

### 3.4 Velocity-Dependent Potential for Electromagnetism

For a general velocity-dependent potential $U(\vec r,\vec v)$, Lagrange's equation

$$
\frac{d}{dt}\left(\frac{\partial L}{\partial\dot q_i}\right) - \frac{\partial L}{\partial q_i} = 0
$$

yields the generalized force

$$
Q_i = -\frac{\partial U}{\partial q_i} + \frac{d}{dt}\left(\frac{\partial U}{\partial\dot q_i}\right).
$$

Remarkably, the Lorentz force can be derived from the potential

$$
U(\vec r,\vec v) = q\phi(\vec r) - q\,\vec A(\vec r)\cdot\vec v,
$$

where $\phi$ is the scalar potential and $\vec A$ is the vector potential, with $\vec E=-\nabla\phi-\partial\vec A/\partial t$ and $\vec B=\nabla\times\vec A$. Substituting this $U$ into the expression for $Q_i$ reproduces exactly the Lorentz force. Thus the full electromagnetic dynamics can be encoded in the Lagrangian $L=T-U$.

------

## 4. Friction and Dissipation

Friction is a **non-conservative force (非保守力)**: the total mechanical energy of a macroscopic object subject to friction is not conserved. Microscopically, the energy is transferred to the innumerable degrees of freedom of the surrounding medium (heat and sound). If one could account for every atom, total energy would still be conserved; friction is a phenomenological device that lets us avoid describing all those microscopic variables explicitly.

------

### 4.1 Examples of Friction

Kinetic friction between solid surfaces is often modeled as

$$
f_k = \mu N,
$$

where $N$ is the normal force and $\mu$ is the coefficient of friction.

A drag force in a fluid is typically velocity-dependent:

$$
f_d = b v^n.
$$

The friction force is opposite to the direction of motion:

$$
\vec f = -b v^n\,\hat v.
$$

More generally, the coefficient $b$ may depend on time and position:

$$
\vec f = -b(t,q_i)\,v^n\,\hat v.
$$

> **Physical values.** Linear drag ($n=1$) describes Stokes flow at low Reynolds number, while quadratic drag ($n=2$) is appropriate for turbulent flow at high Reynolds number.

------

### 4.2 Free Particle Under Friction

Consider a free particle subject to a drag force $\vec f=-bv^n\hat v$. Its mechanical energy is purely kinetic,

$$
E = T = \frac12 m\vec v\cdot\vec v.
$$

The rate of change of energy is

$$
\frac{dE}{dt} = \vec v\cdot m\vec a = \vec v\cdot\vec f = -bv^{n+1}.
$$

Thus the energy decreases monotonically, as expected for a dissipative force.

------

### 4.3 Generalized Friction Force and the Dissipation Function

The generalized friction force is defined by projecting the friction force onto the generalized coordinate:

$$
f_{n,i} = \vec f\cdot\frac{\partial\vec r}{\partial q_i}.
$$

Using the identity $\partial\vec r/\partial q_i=\partial\vec v/\partial\dot q_i$ and $\hat v=\vec v/v$, we find

$$
f_{n,i} = -bv^n\,\hat v\cdot\frac{\partial\vec v}{\partial\dot q_i} = -bv^n\frac{\partial v}{\partial\dot q_i}.
$$

Because

$$
\frac{\partial}{\partial\dot q_i}\left(\frac{1}{n+1}b v^{n+1}\right) = bv^n\frac{\partial v}{\partial\dot q_i},
$$

the generalized friction force can be written as

$$
f_{n,i} = -\frac{\partial D_n}{\partial\dot q_i},
$$

where the **dissipation function (耗散函数)** is

$$
D_n(v) = \frac{1}{n+1}b v^{n+1}.
$$

Lagrange's equation including friction then takes the form

$$
\frac{d}{dt}\left(\frac{\partial L}{\partial\dot q_i}\right) - \frac{\partial L}{\partial q_i} + \frac{\partial D_n}{\partial\dot q_i} = 0.
$$

The dissipation function is directly related to the rate of energy loss:

$$
\frac{dE}{dt} = -(n+1)D_n(v).
$$

Hence $D_n$ quantifies the power dissipated from the macroscopic motion.

------

## 5. Damped Pendulum

Consider a simple pendulum of length $l$ and mass $m$, subject to linear damping

$$
f_d = bv.
$$

The particle speed is $v=l\dot\theta$, and the Lagrangian is

$$
L = \frac12 ml^2\dot\theta^2 + mgl\cos\theta.
$$

> **Note on the sign.** Here $\theta=0$ is the stable equilibrium (hanging straight down). The potential energy is $V=-mgl\cos\theta$, so $L=T-V$ takes the form above.

For linear damping ($n=1$) the dissipation function is

$$
D_1 = \frac12 b v^2 = \frac12 bl^2\dot\theta^2.
$$

The modified Lagrange equation reads

$$
\frac{d}{dt}\left(\frac{\partial L}{\partial\dot\theta}\right) - \frac{\partial L}{\partial\theta} + \frac{\partial D_1}{\partial\dot\theta} = 0.
$$

Evaluating each term,

$$
\frac{\partial L}{\partial\dot\theta} = ml^2\dot\theta, \qquad
\frac{d}{dt}\left(\frac{\partial L}{\partial\dot\theta}\right) = ml^2\ddot\theta, \qquad
\frac{\partial L}{\partial\theta} = -mgl\sin\theta, \qquad
\frac{\partial D_1}{\partial\dot\theta} = bl^2\dot\theta.
$$

Collecting terms,

$$
ml^2\ddot\theta + mgl\sin\theta + bl^2\dot\theta = 0.
$$

Dividing by $ml^2$,

$$
\ddot\theta = -\frac{g}{l}\sin\theta - \frac{b}{m}\dot\theta.
$$

For small oscillations, $\sin\theta\simeq\theta$, and the equation linearizes to

$$
\ddot\theta + \frac{b}{m}\dot\theta + \frac{g}{l}\theta \simeq 0.
$$

In the underdamped regime $b^2 < 4m^2g/l$, the solution is

$$
\boxed{
\theta(t) = A\,e^{-\frac{bt}{2m}}\sin\!\left(\sqrt{\frac{g}{l}-\frac{b^2}{4m^2}}\;t + \phi\right)
}
$$

where $A$ and $\phi$ are constants fixed by the initial conditions.

------

## 6. Generalized Constraint Force

A **constraint force (约束力)** restricts the motion of a system to a submanifold of configuration space. In the Lagrangian formalism, such forces can be introduced via a **Lagrange multiplier (拉格朗日乘子)** $\lambda$. The multiplier appears as an additional generalized force

$$
Q_i^c = \lambda\frac{\partial g}{\partial q_i},
$$

where $g(q_i)=0$ is the constraint equation.

---



### 6.1 Particle Sliding on a Hemisphere

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

$$
\theta_0 \approx 48.2^\circ.
$$
