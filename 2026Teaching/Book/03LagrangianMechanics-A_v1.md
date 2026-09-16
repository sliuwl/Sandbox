## Mathematical Spaces

### Physical Space

For ordinary nonrelativistic mechanics, the **physical space** in which particles are located is modeled as three-dimensional Euclidean space,

$\mathbb{R}^3.$

For a single particle, its position is represented by a vector

$\mathbf r \in \mathbb{R}^3,$

and its momentum is represented by another vector

$\mathbf p \in \mathbb{R}^3.$

Thus, for each particle, position and momentum are separate vector quantities, each with three components.

------

### Configuration Space

For a system of $N$ particles, specifying the configuration means specifying the position of every particle.

If the particles have positions

$\mathbf r_1,\mathbf r_2,\dots,\mathbf r_N \in \mathbb{R}^3,$

then a complete configuration is the ordered tuple

$q = (\mathbf r_1,\mathbf r_2,\dots,\mathbf r_N).$

Mathematically, this tuple is an element of the Cartesian product

$\underbrace{\mathbb{R}^3 \times \mathbb{R}^3 \times \cdots \times \mathbb{R}^3}_{N\text{ copies}} \cong \mathbb{R}^{3N}.$

This $3N$-dimensional space is called the **configuration space** of the system.

Each point in configuration space corresponds to one complete arrangement of the $N$ particles in physical space.

The time evolution of the system is therefore represented by a path

$q(t) \in \mathbb{R}^{3N}.$

Equivalently,

$q(t)=\bigl(\mathbf r_1(t),\mathbf r_2(t),\dots,\mathbf r_N(t)\bigr).$

So instead of tracking $N$ separate position vectors in $\mathbb{R}^3$, we may track one point moving in the higher-dimensional configuration space.

------

## Phase Space

Configuration space records only the positions of the particles. To specify the complete mechanical state of a system in Hamiltonian mechanics, one must also specify the momenta.

For $N$ particles, the momenta are

$\mathbf p_1,\mathbf p_2,\dots,\mathbf p_N \in \mathbb{R}^3.$

The complete state is therefore

$(q,p) = (\mathbf r_1,\dots,\mathbf r_N,\mathbf p_1,\dots,\mathbf p_N).$

This is an element of

$\mathbb{R}^{3N}\times \mathbb{R}^{3N} \cong \mathbb{R}^{6N}.$

This $6N$-dimensional space is called the **phase space**.

A point in phase space specifies both:

$\text{positions} + \text{momenta}.$

In Hamiltonian mechanics, $q$ and $p$ are treated as independent coordinates on phase space. This does not mean that their time evolution is independent; rather, it means that a state is specified by giving both $q$ and $p$, and their evolution is determined by Hamilton’s equations.

------

# Lagrangian Mechanics

Lagrangian mechanics is based on the **principle of stationary action**, also known as **Hamilton’s principle**.

Informally, this principle is sometimes described as saying that “nature is economical” or that “nature minimizes action.” However, the rigorous statement is more precise:

> The actual path followed by a system between two fixed configurations at fixed initial and final times makes the action stationary with respect to small variations of the path.

The action is defined by

$S[q] = \int_{t_i}^{t_f} L(q,\dot q,t)\,dt,$

where:

- $q(t)$ is a path in configuration space,
- $\dot q(t)$ is the velocity along that path,
- $L(q,\dot q,t)$ is the Lagrangian,
- $t_i$ and $t_f$ are fixed initial and final times.

For many elementary mechanical systems,

$L = T - V,$

where $T$ is kinetic energy and $V$ is potential energy.

Hamilton’s principle states that the physical path satisfies

$\delta S = 0.$

This means the action is **stationary**, not necessarily minimal. A stationary value may be a minimum, a maximum, or a saddle point in the space of paths.

------

## Action

The action assigns a number to each possible path in configuration space. Therefore, it is not an ordinary function of a point; it is a **functional**, meaning a function whose input is itself a function.

A path

$q(t)$

is mapped to a real number:

$q(t) \longmapsto S[q] \longmapsto \mathbb{R}.$

Explicitly,

$S[q] = \int_{t_i}^{t_f} L(q,\dot q,t)\,dt.$

The units of action are energy multiplied by time:

$[S] = [E][t] = \mathrm{J}\cdot\mathrm{s} = \frac{\mathrm{kg}\,\mathrm{m}^2}{\mathrm{s}}.$

Different paths between the same endpoints generally have different action values. For example,

$S[q_1(t)] = 8.73,$

$S[q_2(t)] = 9.21,$

$S[q_3(t)] = 10.5.$

The actual path is the one for which the first-order change in the action vanishes under all allowed infinitesimal variations.

------

## Comments

### 1. Fixed but Arbitrary Endpoints

In Hamilton’s principle, the initial and final times,

$t_i,\qquad t_f,$

are fixed. The initial and final configurations,

$q(t_i)=q_i, \qquad q(t_f)=q_f,$

are also fixed while performing the variation.

The phrase **fixed but arbitrary** means that the derivation is carried out for endpoints held fixed, but the resulting Euler–Lagrange equations hold for any choice of endpoints for which the variational problem is well-defined.

For a system of several particles, the endpoint data in physical space may be written as

$\mathbf r_1(t_i)=\mathbf r_1^i, \qquad \mathbf r_1(t_f)=\mathbf r_1^f,$

$\mathbf r_2(t_i)=\mathbf r_2^i, \qquad \mathbf r_2(t_f)=\mathbf r_2^f,$

and so on.

In configuration space, this same information is summarized as

$q(t_i)=q_i, \qquad q(t_f)=q_f,$

where

$q_i=(\mathbf r_1^i,\dots,\mathbf r_N^i), \qquad q_f=(\mathbf r_1^f,\dots,\mathbf r_N^f).$

Thus the motion of all particles is represented by a single path

$q(t)$

in configuration space.

A subtle but important point is that Hamilton’s principle is not usually used by already knowing both endpoints in order to “predict” the final point. Rather, the variational principle yields the equations of motion. Once those equations are known, one commonly predicts the future motion using initial data such as

$q(t_i), \qquad \dot q(t_i),$

or equivalently, in Hamiltonian mechanics,

$q(t_i), \qquad p(t_i).$

------

### 2. Action Is a Functional

The action is a functional because its input is an entire path, not just a single point.

For example,

$S[q] = \int_{t_i}^{t_f} L(q,\dot q,t)\,dt.$

This expression depends on the full history of $q(t)$ over the interval $[t_i,t_f]$, not merely on the values of $q$ at one time.

Therefore, the notation

$S[q]$

is used to emphasize that $S$ depends on the function $q(t)$.

------

# Derivation of the Euler–Lagrange Equation

Consider a one-dimensional configuration variable $q(t)$. The multidimensional case is obtained by applying the same argument to each generalized coordinate.

Let the physical path be $q(t)$. We compare it with nearby paths of the form

$q_\alpha(t)=q(t)+\alpha \eta(t),$

where:

- $\alpha$ is a real parameter,
- $\eta(t)$ is an arbitrary smooth variation,
- the endpoints are fixed, so

$\eta(t_i)=\eta(t_f)=0.$

The corresponding velocity is

$\dot q_\alpha(t)=\dot q(t)+\alpha \dot\eta(t).$

The action evaluated on the varied path is

$S[\alpha] = \int_{t_i}^{t_f} L(q+\alpha\eta,\dot q+\alpha\dot\eta,t)\,dt.$

The physical path makes the action stationary, so

$\left.\frac{dS[\alpha]}{d\alpha}\right|_{\alpha=0}=0.$

Differentiating under the integral sign gives

$\left.\frac{dS[\alpha]}{d\alpha}\right|_{\alpha=0} = \int_{t_i}^{t_f} \left[ \frac{\partial L}{\partial q}\eta + \frac{\partial L}{\partial \dot q}\dot\eta \right]dt.$

Therefore, stationarity requires

$\int_{t_i}^{t_f} \left[ \frac{\partial L}{\partial q}\eta + \frac{\partial L}{\partial \dot q}\dot\eta \right]dt =0.$

Now integrate the second term by parts:

$\int_{t_i}^{t_f} \frac{\partial L}{\partial \dot q}\dot\eta\,dt = \left. \eta\frac{\partial L}{\partial \dot q} \right|_{t_i}^{t_f} - \int_{t_i}^{t_f} \eta \frac{d}{dt} \left( \frac{\partial L}{\partial \dot q} \right)dt.$

Because

$\eta(t_i)=\eta(t_f)=0,$

the boundary term vanishes:

$\left. \eta\frac{\partial L}{\partial \dot q} \right|_{t_i}^{t_f} =0.$

Thus,

$\int_{t_i}^{t_f} \frac{\partial L}{\partial \dot q}\dot\eta\,dt = - \int_{t_i}^{t_f} \eta \frac{d}{dt} \left( \frac{\partial L}{\partial \dot q} \right)dt.$

Substituting this into the stationarity condition gives

$\int_{t_i}^{t_f} \left[ \frac{\partial L}{\partial q} - \frac{d}{dt} \left( \frac{\partial L}{\partial \dot q} \right) \right]\eta(t)\,dt =0.$

Since $\eta(t)$ is arbitrary except for vanishing at the endpoints, the fundamental lemma of the calculus of variations implies

$\frac{\partial L}{\partial q} - \frac{d}{dt} \left( \frac{\partial L}{\partial \dot q} \right) =0.$

Equivalently,

$\boxed{ \frac{d}{dt} \left( \frac{\partial L}{\partial \dot q} \right) - \frac{\partial L}{\partial q} =0 }$

This is the **Euler–Lagrange equation**.

------

## Multi-Dimensional Configuration Space

In general, the configuration variable has several components. Write

$q(t)=\bigl(q^1(t),q^2(t),\dots,q^n(t)\bigr),$

where $n$ is the dimension of the configuration space.

For $N$ unconstrained particles in three-dimensional physical space,

$n=3N.$

The Lagrangian is then a function

$L(q^1,\dots,q^n,\dot q^1,\dots,\dot q^n,t).$

Applying the same variational argument to each coordinate gives one Euler–Lagrange equation for each generalized coordinate:

$\boxed{ \frac{d}{dt} \left( \frac{\partial L}{\partial \dot q^k} \right) - \frac{\partial L}{\partial q^k} =0, \qquad k=1,\dots,n. }$

Equivalently,

$\boxed{ \frac{\partial L}{\partial q^k} - \frac{d}{dt} \left( \frac{\partial L}{\partial \dot q^k} \right) =0, \qquad k=1,\dots,n. }$

The two forms are identical up to multiplication by $-1$.

------

# A Simple Example: Recovery of Newton’s Second Law

Consider a particle moving in one dimension with Lagrangian

$L(q,\dot q) = T - V = \frac{1}{2}m\dot q^2 - V(q).$

Compute the first derivative:

$\frac{\partial L}{\partial q} = -\frac{dV}{dq}.$

For a conservative force, the force is defined by

$F(q) = -\frac{dV}{dq}.$

Therefore,

$\frac{\partial L}{\partial q} = F(q).$

Next,

$\frac{\partial L}{\partial \dot q} = m\dot q.$

This quantity is the canonical momentum:

$p = \frac{\partial L}{\partial \dot q} = m\dot q.$

For this simple system, the canonical momentum equals the ordinary mechanical momentum.

Taking its time derivative gives

$\frac{d}{dt} \left( \frac{\partial L}{\partial \dot q} \right) = \frac{d}{dt}(m\dot q) = m\ddot q = \frac{dp}{dt},$

assuming $m$ is constant.

The Euler–Lagrange equation is

$\frac{d}{dt} \left( \frac{\partial L}{\partial \dot q} \right) - \frac{\partial L}{\partial q} = 0.$

Substituting the expressions above,

$\frac{dp}{dt} - F = 0.$

Hence,

$F=\frac{dp}{dt}.$

For constant mass,

$p=m\dot q,$

so

$F=m\ddot q.$

Therefore,

$\boxed{ F=\frac{dp}{dt}=m\ddot q }$

which is Newton’s second law for a particle of constant mass subject to a conservative force.

------

## Summary

- **Physical space** for nonrelativistic particles is $\mathbb{R}^3$.
- **Configuration space** for $N$ unconstrained particles is $\mathbb{R}^{3N}$.
- **Phase space** contains both positions and momenta and is $\mathbb{R}^{6N}$.
- The **action** is a functional:

$S[q] = \int_{t_i}^{t_f} L(q,\dot q,t)\,dt.$

- Hamilton’s principle says the physical path makes the action stationary:

$\delta S=0.$

- Stationarity of the action implies the Euler–Lagrange equations:

$\boxed{ \frac{d}{dt} \left( \frac{\partial L}{\partial \dot q^k} \right) - \frac{\partial L}{\partial q^k} =0. }$

- For

$L=\frac{1}{2}m\dot q^2 - V(q),$

the Euler–Lagrange equation reduces to Newton’s second law:

$\boxed{ F=\frac{dp}{dt}=m\ddot q. }$

