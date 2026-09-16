# Lagrangian Mechanics

## Mathematical Space

### Physical Space

We describe the **location** and the **momentum** of each object using an individual vector.

Physical space is the Euclidean three-dimensional space:

\[
\mathbb{R}^3
\]

---

### Configuration Space

In physical space, we need \(N\) vectors, each living in \(\mathbb{R}^3\), to track the locations of \(N\) objects.

By gluing the \(N\) copies of \(\mathbb{R}^3\) together, we only need one vector in

\[
\mathbb{R}^{3N}
\]

This high-dimensional \(\mathbb{R}^{3N}\) space is the **configuration space**.

Each point in the configuration space corresponds to one specific configuration the system can be in.

The time evolution of a system is described in configuration space by a **single path**.

---

## Phase Space

A point in the configuration space only keeps track of the **position information**.

Following the “space gluing” idea, we can act as if the momenta live in a different space, and glue the momentum spaces to the location space.

Therefore, we can describe the **complete state** — not just the configuration — of the system using a single vector in

\[
\mathbb{R}^{6N}
\]

This space is called the **phase space**.

In phase space, the state includes:

\[
\text{location} + \text{momentum}
\]

We treat \(q\) and \(p\) as independent coordinates.

---

# Lagrangian Mechanics

> “Nature is Lazy”

Also known as:

- Least Action Principle
- Stationary Action Principle
- Hamilton’s Principle

The basic idea is:

> Any system evolves in such a way that the action required is minimal.

The action is defined as

\[
S = \int_{t_i}^{t_f} L \, dt
  = \int_{t_i}^{t_f} (T - V) \, dt
\]

where

\[
\delta S = 0
\]

Technically, this is equivalent to saying:

> The actual path which a particle follows between two points, \(1\) and \(2\), in a given time interval \(t_i\) to \(t_f\), is such that the action
>
> \[
> S = \int_{t_i}^{t_f} L(q, \dot q, t)\,dt
> \]
>
> is stationary when evaluated along the actual path.

---

## Action

Action measures how much “cost” is necessary for each possible path between two points.

---

## Comments

### 1. Fixed but Arbitrary Endpoints

We are talking about **fixed but arbitrary** initial and final points in the configuration space.

According to Hamilton’s principle, we can derive the equations of motion and predict the correct final configuration given the initial condition.

In physical space, we may have several particles with individual initial and final positions:

\[
q_1^i \to q_1^f,\qquad
q_2^i \to q_2^f,\qquad
q_3^i \to q_3^f
\]

In configuration space, we simply use one path:

\[
q(t)
\]

to denote a path in the configuration space, with endpoints

\[
\{q_k^i\}
\quad \text{and} \quad
\{q_k^f\}
\]

---

### 2. Action Is a Functional

The action \(S\) is a **functional**, which means it is a function of a function.

A path

\[
q(t)
\]

is mapped to an action value:

\[
q(t)
\longrightarrow
S[q(t)]
\longrightarrow
\text{number}
\]

where

\[
S = \int_{t_i}^{t_f} L(q,\dot q,t)\,dt
\]

and

\[
L = T - V
\]

The units of action are

\[
[S] = \frac{\mathrm{kg}\cdot \mathrm{m}^2}{\mathrm{s}}
\]

Different paths between the same endpoints can have different action values, for example:

\[
S[q_1(t)] = 8.73
\]

\[
S[q_2(t)] = 9.21
\]

\[
S[q_3(t)] = 10.5
\]

---

# Derivation of the Euler–Lagrange Equation

Out of infinitely many paths connecting the initial and final configurations, the actual path is the one that makes the action stationary.

Consider a variation of the path:

\[
q(t) \to q(t) + \varepsilon(t)
\]

with boundary condition

\[
\varepsilon(t_i) = \varepsilon(t_f) = 0
\]

We are looking for the condition that makes all terms first order in \(\varepsilon(t)\) vanish.

The action becomes

\[
S
=
\int_{t_i}^{t_f}
dt\,
L\left[
q(t)+\varepsilon(t),
\dot q(t)+\dot\varepsilon(t)
\right]
\]

Using Taylor expansion,

\[
S
=
\int_{t_i}^{t_f}
dt
\left[
L(q,\dot q)
+
\frac{\partial L}{\partial q}
\left(q+\varepsilon-q\right)
+
\frac{\partial L}{\partial \dot q}
\left(\dot q+\dot\varepsilon-\dot q\right)
+
\cdots
\right]
\]

Thus,

\[
S
=
\int_{t_i}^{t_f}
dt
\left[
L(q,\dot q)
+
\varepsilon
\frac{\partial L}{\partial q}
+
\dot\varepsilon
\frac{\partial L}{\partial \dot q}
+
\cdots
\right]
\]

The first-order variation is

\[
\int_{t_i}^{t_f}
dt
\left[
\varepsilon \frac{\partial L}{\partial q}
+
\dot\varepsilon \frac{\partial L}{\partial \dot q}
\right]
=0
\]

Now integrate the second term by parts:

\[
\int_{t_i}^{t_f}
dt\,
\dot\varepsilon
\frac{\partial L}{\partial \dot q}
=
\left.
\varepsilon
\frac{\partial L}{\partial \dot q}
\right|_{t_i}^{t_f}
-
\int_{t_i}^{t_f}
dt\,
\varepsilon
\frac{d}{dt}
\left(
\frac{\partial L}{\partial \dot q}
\right)
\]

Using the boundary condition

\[
\varepsilon(t_i)=\varepsilon(t_f)=0
\]

we get

\[
\left.
\varepsilon
\frac{\partial L}{\partial \dot q}
\right|_{t_i}^{t_f}
=0
\]

Therefore,

\[
\int_{t_i}^{t_f}
dt\,
\dot\varepsilon
\frac{\partial L}{\partial \dot q}
=
-
\int_{t_i}^{t_f}
dt\,
\varepsilon
\frac{d}{dt}
\left(
\frac{\partial L}{\partial \dot q}
\right)
\]

Substituting back,

\[
\int_{t_i}^{t_f}
dt
\left[
\frac{\partial L}{\partial q}
-
\frac{d}{dt}
\left(
\frac{\partial L}{\partial \dot q}
\right)
\right]
\varepsilon
=0
\]

This condition must be correct for any possible variation \(\varepsilon(t)\), if \(q(t)\) is the least-action path.

Therefore,

\[
\boxed{
\frac{\partial L}{\partial q}
-
\frac{d}{dt}
\left(
\frac{\partial L}{\partial \dot q}
\right)
=0
}
\]

This is the **Euler–Lagrange equation**.

---

## Multi-Dimensional Configuration Space

Note that \(q(t)\) generally describes a path in a high-dimensional configuration space.

We can write

\[
q(t) \sim \{q_k(t)\}
=
\{q_1(t),q_2(t),\cdots,q_N(t)\}
\]

This means we have \(N\) such equations:

\[
\boxed{
\frac{\partial L}{\partial q_k}
-
\frac{d}{dt}
\left(
\frac{\partial L}{\partial \dot q_k}
\right)
=0,
\qquad
k=1,\cdots,N
}
\]

---

# A Simple Example

Let

\[
L = T - V
=
\frac{1}{2}m\dot q^2 - V(q)
\]

Then

\[
\frac{\partial L}{\partial q}
=
-
\frac{\partial V(q)}{\partial q}
=
F
\]

where \(F\) is the generalized force.

Also,

\[
\frac{d}{dt}
\left(
\frac{\partial L}{\partial \dot q}
\right)
=
\frac{d}{dt}
\left(
m\dot q
\right)
=
\frac{d}{dt}(p)
\]

where \(p\) is the generalized momentum.

The Euler–Lagrange equation gives

\[
\frac{\partial L}{\partial q}
=
\frac{d}{dt}
\left(
\frac{\partial L}{\partial \dot q}
\right)
\]

so

\[
F = \frac{d p}{dt}
\]

That is,

\[
\boxed{
\text{The rate of change of the momentum equals the force.}
}
\]

This is **Newton’s Second Law**.
