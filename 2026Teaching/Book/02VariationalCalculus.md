# Variational Calculus

**Reading material:** Chapter 6 of *Classical Mechanics* by John R. Taylor

## Table of Contents

1. [Single-Variable Functions](#1-single-variable-functions)
2. [Functionals](#2-functionals)
3. [Some Examples of Functionals](#3-some-examples-of-functionals)
   - [3.1 Length of a Plane Curve](#31-length-of-a-plane-curve)
   - [3.2 Fermat's Principle](#32-fermats-principle)
4. [Variation](#4-variation)
5. [Euler-Lagrange Equation](#5-euler-lagrange-equation)
   - [5.1 Derivation of the Euler-Lagrange Equation](#51-derivation-of-the-euler-lagrange-equation)
   - [5.2 Proof of the Fundamental Lemma](#52-proof-of-the-fundamental-lemma)
6. [The Beltrami Identity](#6-the-beltrami-identity)
7. [Application of Variational Calculus](#7-application-of-variational-calculus)
8. [Brachistochrone Problem](#8-brachistochrone-problem)

---

## 1. Single-Variable Functions

In ordinary differential calculus we study functions $f:\mathbb{R}\to\mathbb{R}$.  To locate a local extremum or, more generally, a **stationary point** of $f$, we impose the first-order condition

$$
\frac{df(x)}{dx}=0.
$$

At such a point the graph is **locally flat**: an infinitesimal change $\Delta x$ produces no first-order change in $f$.  Whether the stationary point is a minimum, a maximum, or a point of inflection must be decided by further analysis (e.g., second derivative test).

Calculus of variations asks the analogous question for an object that is *one level more complicated*: instead of a function of a number, we have a **functional**, i.e. a quantity that depends on an entire function.  We now seek the function $y(x)$ that makes the functional stationary.

------

## 2. Functionals

A **functional** is a rule that takes an entire function as its input and returns a single number.

This is different from an ordinary function. An ordinary function might take a number $x$ and return another number. A functional takes something like a whole curve $y(x)$ and returns one number.

For example, suppose $y(x)$ describes a path. A functional might return the length of that path, or the time it takes light to travel along that path.

In the problems we will study, the input function $y(x)$ is usually assumed to be sufficiently smooth. Our goal is to find the function $y(x)$ that makes the value of the functional stationary.

“Stationary” means that if we make a very small change to the function, the value of the functional does not change to first order.

This is analogous to ordinary calculus, where a function $g(x)$ has a stationary point when

$\frac{dg}{dx}=0.$

In calculus of variations, however, the variable is not a number $x$. The “variable” is an entire function $y(x)$.

A common type of functional has the form

$F[y]=\int_{x_1}^{x_2} f\left(x,y(x),y'(x)\right)\,dx, \qquad y'=\frac{dy}{dx}.$

Here:

- $F[y]$ is the functional.
- $y(x)$ is the input function.
- $y'(x)$ is the derivative of the input function.
- $f(x,y,y')$ is an ordinary function of three variables.
- Once we choose a particular function $y(x)$, the integrand becomes an ordinary function of $x$, and the integral gives a number.

The square brackets in $F[y]$ remind us that the input is a function, not just a number.


In Lagrangian mechanics, the most important functional is the **action**,

$S[q]=\int_{t_1}^{t_2} L\left(t,q(t),\dot q(t)\right)\,dt, \qquad \dot q=\frac{dq}{dt}.$

Here:

- $q(t)$ is the path of the system in time.
- $\dot q(t)$ is the velocity.
- $L(t,q,\dot q)$ is the Lagrangian.
- $S[q]$ is a number assigned to the entire path $q(t)$.

Hamilton’s principle says that the physically realized path $q(t)$ makes the action stationary:

$\delta S = 0.$

This does **not** always mean that the action is minimized. It means that the first-order change in the action vanishes.

------

## 3. Examples of Functionals

A functional is a rule that takes in an entire function and returns a single number.

For example, is

$F(y)=(y(x))^2$

it a functional?

No. If $y(x)=x^2$, then

$F(y)=x^4,$

which is still a function of $x$, not a single number.

However,

$F[y]=\int_0^1 (y(x))^2\,dx$

is a functional. If $y(x)=x^2$, then

$F[y]=\int_0^1 x^4\,dx=\frac{1}{5}.$

This time, the output is a single number.

------

### 3.1 Length of a Plane Curve

Suppose a curve is described by $y=y(x)$ between $x=x_1$ and $x=x_2$. The arc length element is

$ds=\sqrt{dx^2+dy^2}.$

Since

$dy=y'(x)\,dx,$

we get

$ds=\sqrt{1+y'(x)^2}\,dx.$

Therefore the total length of the curve is

$L[y]=\int_{x_1}^{x_2}\sqrt{1+y'(x)^2}\,dx.$

This is a functional because the input is the entire curve $y(x)$, and the output is the total length, a number.

If the endpoints are fixed,

$y(x_1)=y_1, \qquad y(x_2)=y_2,$

then the problem is:

> Among all smooth curves connecting the two endpoints, which one has the shortest length?

The answer is a straight line. Calculus of variations provides a systematic way to prove this.

------

### 3.2 Fermat’s Principle

Light traveling through a medium with refractive index $n(x,y)$ has speed

$v=\frac{c}{n(x,y)}.$

For a small distance $ds$, the travel time is

$dt=\frac{ds}{v} =\frac{n(x,y)}{c}\,ds.$

Using

$ds=\sqrt{1+y'(x)^2}\,dx,$

the total travel time is

$T[y]=\frac{1}{c}\int_{x_1}^{x_2} n(x,y)\sqrt{1+y'(x)^2}\,dx.$

Fermat’s principle states that the actual path taken by light is a stationary path of the travel-time functional:

$\delta T = 0.$

If $n$ is constant, then

$T[y]=\frac{n}{c}\int_{x_1}^{x_2}\sqrt{1+y'(x)^2}\,dx.$

So minimizing travel time is equivalent to minimizing path length. Therefore, in a uniform medium, light travels in a straight line.

If $n$ varies with position, then the fastest path is generally not a straight line. Calculus of variations is the tool that determines the actual ray path.

------

## 4. Variation

We now want to define the analogue of a derivative for a functional.

In ordinary calculus, to study a function $g(x)$, we look at what happens when we change $x$ slightly:

$x \to x+\varepsilon.$

For a functional $F[y]$, the input is not a number. The input is a whole function $y(x)$. So instead of changing a number slightly, we change the whole function slightly.

We introduce a nearby function

$y_\varepsilon(x)=y(x)+\varepsilon \eta(x).$

Here:

- $y(x)$ is the original function.
- $\eta(x)$ is a chosen “shape” of the perturbation.
- $\varepsilon$ is a small real number that controls the size of the perturbation.
- $y_\varepsilon(x)$ is the perturbed function.

The function $\eta(x)$ tells us **which direction in function space** we are moving away from $y(x)$.

The number $\varepsilon$ tells us **how far** we move in that direction.

So $\eta(x)$ plays a role similar to a direction vector, while $\varepsilon$ plays a role similar to a small step size.

------

### 4.1 What Does “Direction in Function Space” Mean?

In ordinary two-dimensional space, if we start at a point $\mathbf r$, we can move in the direction of a vector $\mathbf v$:

$\mathbf r_\varepsilon = \mathbf r+\varepsilon \mathbf v.$

Here:

- $\mathbf v$ gives the direction.
- $\varepsilon$ gives the step size.

Similarly, in function space, we write

$y_\varepsilon(x)=y(x)+\varepsilon \eta(x).$

Here:

- $\eta(x)$ gives the direction in function space.
- $\varepsilon$ gives the size of the step.

For example, if

$y(x)=x^2$

and

$\eta(x)=\sin(\pi x),$

then

$y_\varepsilon(x)=x^2+\varepsilon\sin(\pi x).$

For small $\varepsilon$, this is a curve very close to $y(x)=x^2$, but slightly deformed in the shape of $\sin(\pi x)$.

If $\varepsilon>0$, we move in the $+\eta$ direction.

If $\varepsilon<0$, we move in the $-\eta$ direction.

The function $\eta(x)$ is arbitrary, except that it must satisfy any required boundary conditions.

------

### 4.2 Fixed Endpoints

Often we want all allowed curves to pass through the same two endpoints. Suppose the endpoints are fixed:

$y(x_1)=y_1, \qquad y(x_2)=y_2.$

Then we require the perturbed curve to satisfy the same endpoint conditions:

$y_\varepsilon(x_1)=y_1, \qquad y_\varepsilon(x_2)=y_2.$

Since

$y_\varepsilon(x)=y(x)+\varepsilon\eta(x),$

we have

$y_\varepsilon(x_1)=y(x_1)+\varepsilon\eta(x_1),$

and

$y_\varepsilon(x_2)=y(x_2)+\varepsilon\eta(x_2).$

Because $y(x_1)=y_1$ and $y(x_2)=y_2$, the endpoints remain fixed only if

$\eta(x_1)=0, \qquad \eta(x_2)=0.$

Thus, for fixed endpoint problems, the allowed variations must vanish at the endpoints.

This means that the perturbation can change the curve in the middle, but not at the two ends.

------

### 4.3 The First Variation

The **first variation** of $F$ at $y$ in the direction $\eta$ is defined by

$\delta F[y;\eta] = \left. \frac{d}{d\varepsilon} F[y+\varepsilon\eta] \right|_{\varepsilon=0}.$

This definition is very similar to a directional derivative.

In ordinary multivariable calculus, the directional derivative of a function $g(\mathbf r)$ in the direction $\mathbf v$ is

$\left. \frac{d}{d\varepsilon} g(\mathbf r+\varepsilon\mathbf v) \right|_{\varepsilon=0}.$

In calculus of variations, we replace:

$\mathbf r \to y(x), \qquad \mathbf v \to \eta(x).$

So the first variation measures how the functional changes when we move slightly away from the function $y(x)$ in the direction $\eta(x)$.

------

### 4.4 Variation of the Derivative

Because

$y_\varepsilon(x)=y(x)+\varepsilon\eta(x),$

we also have

$y_\varepsilon'(x)=y'(x)+\varepsilon\eta'(x).$

Therefore,

$\delta y(x)=\eta(x),$

and

$\delta y'(x)=\eta'(x).$

Equivalently,

$\delta y'(x)=\frac{d}{dx}\delta y(x).$

This is allowed because the variation changes the function $y$, but it does not change the independent variable $x$. In other words, $x$ is held fixed while the curve is being varied.

------

### 4.5 Stationary Function

A function $y(x)$ is called a **stationary function** of the functional $F[y]$ if

$\delta F[y;\eta]=0$

for every allowed perturbation $\eta(x)$.

For fixed endpoints, this means

$\delta F[y;\eta]=0 \qquad \text{for all smooth } \eta(x) \text{ with } \eta(x_1)=\eta(x_2)=0.$

This is the variational analogue of the ordinary calculus condition

$\frac{dg}{dx}=0.$

However, just as in ordinary calculus, a stationary point is not necessarily a minimum or maximum.

For example, in single-variable calculus, $x=0$ is a stationary point of

$g(x)=x^3,$

because

$g'(0)=0.$

But $x=0$ is neither a minimum nor a maximum.

Similarly, in calculus of variations, a stationary function may correspond to a minimum, a maximum, or a saddle point in function space.

Determining which one it is usually requires further analysis, such as studying the second variation.

------

### 4.6 Summary

A functional takes a function as input and returns a number:

$y(x) \longmapsto F[y].$

To study how a functional changes, we perturb the input function:

$y(x)\to y_\varepsilon(x)=y(x)+\varepsilon\eta(x).$

Here:

- $\eta(x)$ is the shape or direction of the perturbation.
- $\varepsilon$ is a small parameter controlling the size and sign of the perturbation.
- Fixed endpoints require

$\eta(x_1)=\eta(x_2)=0.$

The first variation is

$\delta F[y;\eta] = \left. \frac{d}{d\varepsilon} F[y+\varepsilon\eta] \right|_{\varepsilon=0}.$

A stationary function satisfies

$\delta F[y;\eta]=0$

for every allowed variation $\eta(x)$.

This is the key idea behind the calculus of variations and leads directly to the Euler-Lagrange equation.

------

## 5. Euler-Lagrange Equation

For a functional of the form

$$
F[y]=\int_{x_1}^{x_2} f\!\left(x,y(x),y'(x)\right)\,dx,
$$

with fixed endpoints $y(x_1)=y_1$ and $y(x_2)=y_2$, a twice-differentiable stationary function $y(x)$ must satisfy the **Euler-Lagrange equation**

$$
\frac{\partial f}{\partial y}-\frac{d}{dx}\frac{\partial f}{\partial y'}=0.
$$

Here $\partial f/\partial y$ and $\partial f/\partial y'$ are partial derivatives of the integrand $f(x,y,y')$ with respect to its second and third arguments, evaluated along the path $y(x)$.  The total derivative $d/dx$ then acts on the resulting function of $x$.

If the functional depends on several dependent variables,

$$
F[y,z]=\int_{x_1}^{x_2} f\!\left(x,y,y',z,z'\right)\,dx,
$$

then each dependent variable yields its own Euler-Lagrange equation:

$$
\frac{\partial f}{\partial y}-\frac{d}{dx}\frac{\partial f}{\partial y'}=0,
\qquad
\frac{\partial f}{\partial z}-\frac{d}{dx}\frac{\partial f}{\partial z'}=0.
$$

------

## 5.1 Derivation of the Euler-Lagrange Equation

Consider the functional
\[
F[y]=\int_{x_1}^{x_2} f\left(x,y(x),y'(x)\right)\,dx,
\]
with fixed boundary values $y(x_1)$ and $y(x_2)$. We want to find the condition that a stationary function $y(x)$ must satisfy.

To test whether $y(x)$ is stationary, we compare it with nearby functions. Introduce the perturbed function

$y_\varepsilon(x)=y(x)+\varepsilon\eta(x),$

where $\eta(x)$ is a smooth function satisfying $\eta(x_1)=\eta(x_2)=0$, which  ensure that the endpoints remain fixed. Previously, we defined the first variation by
\[
\delta F[y;\eta] = \left. \frac{d}{d\varepsilon}F[y+\varepsilon\eta] \right|_{\varepsilon=0}.
\]
Here $F[y+\varepsilon\eta]$ means the value of the functional evaluated on the perturbed function $y_\varepsilon(x)$. We compute $F[y+\varepsilon\eta]$ by replacing $y(x)$ with $y_\varepsilon(x)$, and replacing $y'(x)$ with $y_\varepsilon'(x)$.

Now,

$y_\varepsilon(x)=y(x)+\varepsilon\eta(x),$

so

$y_\varepsilon'(x) = \frac{d}{dx}\left[y(x)+\varepsilon\eta(x)\right] = y'(x)+\varepsilon\eta'(x).$

Therefore,
\[
F[y+\varepsilon\eta] = F[y_\varepsilon] = \int_{x_1}^{x_2} f\left(x,y+\varepsilon\eta,\,y'+\varepsilon\eta'\right)\,dx.
\]
This formula is simply the original definition of the functional, evaluated on the nearby function $y_\varepsilon(x)$.

At this point, $F[y+\varepsilon\eta]$ is an ordinary function of the single real variable $\varepsilon$. We can therefore differentiate it with respect to $\varepsilon$. Assuming $f$ is sufficiently smooth, we may differentiate under the integral sign:

$\delta F[y;\eta] = \left. \frac{d}{d\varepsilon} \int_{x_1}^{x_2} f\left(x,y+\varepsilon\eta,\,y'+\varepsilon\eta'\right)\,dx \right|_{\varepsilon=0}.$

Thus,

$\delta F[y;\eta] = \int_{x_1}^{x_2} \left. \frac{d}{d\varepsilon} f\left(x,y+\varepsilon\eta,\,y'+\varepsilon\eta'\right) \right|_{\varepsilon=0} dx.$

Now use the ordinary chain rule. The function $f$ depends on three arguments:

$f=f(x,y,y').$

When $\varepsilon$ changes, $x$ does not change. However, the second and third arguments do change:

$y \to y+\varepsilon\eta,$

and

$y' \to y'+\varepsilon\eta'.$

Therefore,

$\frac{d}{d\varepsilon} f\left(x,y+\varepsilon\eta,\,y'+\varepsilon\eta'\right) = \frac{\partial f}{\partial y}\eta + \frac{\partial f}{\partial y'}\eta'.$

Setting $\varepsilon=0$, we get the first variation
\[
\delta F[y;\eta] = \left. \int_{x_1}^{x_2} \left( \frac{\partial f}{\partial y}\eta + \frac{\partial f}{\partial y'}\eta' \right)dx \right|_{\varepsilon=0}.
\]
**Here the partial derivatives are evaluated along the original function $y(x)$**, meaning

$\frac{\partial f}{\partial y} = \frac{\partial f}{\partial y} \left(x,y(x),y'(x)\right),$

and

$\frac{\partial f}{\partial y'} = \frac{\partial f}{\partial y'} \left(x,y(x),y'(x)\right).$

So we have
\[
\delta F[y;\eta] = \int_{x_1}^{x_2} \left( \frac{\partial f}{\partial y}\eta + \frac{\partial f}{\partial y'}\eta' \right)dx.
\]
The first term already contains $\eta$, but the second term contains $\eta'$. We want to rewrite the expression so that the variation $\eta$ appears without its derivative. To do this, we integrate the second term by parts:
\[
\int_{x_1}^{x_2}\frac{\partial f}{\partial y'}\,\eta'\,dx = \left. \frac{\partial f}{\partial y'}\,\eta \right|_{x_1}^{x_2} - \int_{x_1}^{x_2} \eta\, \frac{d}{dx} \left( \frac{\partial f}{\partial y'} \right) dx.
\]
The boundary term vanishes because $\eta(x_1)=\eta(x_2)=0$. Therefore, $\left. \frac{\partial f}{\partial y'}\,\eta \right|_{x_1}^{x_2} = 0.$

Hence the first variation becomes
\[
\delta F[y;\eta] = \int_{x_1}^{x_2} \eta(x) \left[ \frac{\partial f}{\partial y} - \frac{d}{dx} \left( \frac{\partial f}{\partial y'} \right) \right]dx.
\]
For $y$ to be stationary, this integral must be zero for *every* admissible $\eta$.  The **fundamental lemma of the calculus of variations** then implies that the factor multiplying $\eta$ must vanish everywhere on $[x_1,x_2]$:

$$
\frac{\partial f}{\partial y}-\frac{d}{dx}\frac{\partial f}{\partial y'}=0.
$$

------

## 5.2 Proof of the Fundamental Lemma

Let $g(x)$ be continuous on $[x_1,x_2]$, and suppose

$\int_{x_1}^{x_2}\eta(x)g(x)\,dx=0$

for every smooth function $\eta(x)$ satisfying

$\eta(x_1)=\eta(x_2)=0.$

We want to show that this forces

$g(x)=0$

for all $x\in[x_1,x_2]$.

Suppose, for contradiction, that $g$ is not identically zero. Then there is some point $x_0$ where

$g(x_0)\neq 0.$

Since $g$ is continuous, it must remain nonzero with the same sign on some small interval around $x_0$.

For example, suppose $g(x)>0$ on a small interval. Then we can choose a smooth function $\eta(x)$ that is positive on that interval and zero outside it, while still satisfying

$\eta(x_1)=\eta(x_2)=0.$

For this choice, the product $\eta(x)g(x)$ is nonnegative everywhere and positive on part of the interval. Therefore,

$\int_{x_1}^{x_2}\eta(x)g(x)\,dx>0,$

which contradicts the assumption that the integral is zero for every $\eta$.

Similarly, if $g(x)<0$ on a small interval, we choose $\eta(x)<0$ there, so that $\eta(x)g(x)>0$ on that interval. Again the integral would be positive, giving a contradiction.

Therefore, $g$ must be identically zero:

$g(x)=0 \qquad \text{for all } x\in[x_1,x_2].$

Applying this result to

$g(x) = \frac{\partial f}{\partial y} - \frac{d}{dx} \left( \frac{\partial f}{\partial y'} \right),$

we obtain

$\frac{\partial f}{\partial y} - \frac{d}{dx} \left( \frac{\partial f}{\partial y'} \right) = 0.$

Thus the Euler-Lagrange equation is a necessary condition for a stationary function.

------

## 6. The Beltrami Identity

When the integrand does not depend explicitly on $x$, i.e.

$$
f=f(y,y'),
$$

the Euler–Lagrange equation can be integrated once.  This first integral is called the **Beltrami identity** (or, in physics, it is related to energy conservation when the independent variable is time).

Assume both $f$  and $y$ are $C^2$ (twice continuously differentiable).  Along the path,

$$
\frac{df}{dx}=\frac{\partial f}{\partial y}\,y'
+\frac{\partial f}{\partial y'}\,y''.
$$

Because $\partial f/\partial x=0$.  Using the Euler–Lagrange equation to replace $\partial f/\partial y$ by $\frac{d}{dx}(\partial f/\partial y')$, we get

$$
\frac{df}{dx}
=\frac{d}{dx}\!\left(\frac{\partial f}{\partial y'}\right)y'
+\frac{\partial f}{\partial y'}\,y''
=\frac{d}{dx}\!\left(y'\frac{\partial f}{\partial y'}\right).
$$

Hence

$$
\frac{d}{dx}\!\left(f-y'\frac{\partial f}{\partial y'}\right)=0,
$$

and therefore

$$
f-y'\frac{\partial f}{\partial y'}=C,
$$

where $C$ is a constant of integration.  This is a first-order differential equation, often much easier to solve than the second-order Euler–Lagrange equation.

------

## 7. Application of Variational Calculus

The general procedure for solving a variational problem is:

1. **Write the functional.**  Express the quantity of interest (length, time, action, etc.) as an integral
   $$
   F[y]=\int_{x_1}^{x_2} f(x,y,y')\,dx.
   $$

2. **Identify the integrand.**  Read off the function $f(x,y,y')$.

3. **Apply the Euler–Lagrange equation.**  Compute the partial derivatives and solve
   $$
   \frac{\partial f}{\partial y}-\frac{d}{dx}\frac{\partial f}{\partial y'}=0.
   $$
   If $f$ has no explicit $x$-dependence, you may use the Beltrami identity instead.

4. **Solve the differential equation** subject to the boundary conditions $y(x_1)=y_1$, $y(x_2)=y_2$.  The resulting function is the stationary path.

5. **Check the nature of the stationary path** if a minimum or maximum is required.  The Euler–Lagrange equation by itself guarantees only stationarity.

------

## 8. Brachistochrone Problem

The **brachistochrone problem** asks: given two points $A$ and $B$ in a vertical plane, with $A$ higher than $B$, what is the shape of a frictionless track along which a bead released from rest at $A$ reaches $B$ in the shortest possible time?  The name comes from Greek *brachistos* (shortest) and *chronos* (time).

Choose coordinates with $A$ at the origin and the $y$-axis measured vertically downward.  Let the track be described by $y=y(x)$, with $y(0)=0$ and $y(x_2)=y_2$.  Conservation of energy gives the speed at height $y$:

$$
\frac12 mv^2=mgy
\quad\Longrightarrow\quad
v=\sqrt{2gy}.
$$

An element of arc length is

$$
ds=\sqrt{1+y'(x)^2}\,dx,
$$

so the time of travel is the functional

$$
T[y]=\int_{0}^{x_2}\frac{ds}{v}
=\frac{1}{\sqrt{2g}}\int_{0}^{x_2}
\sqrt{\frac{1+y'(x)^2}{y(x)}}\,dx.
$$

The overall constant does not affect the location of the stationary path, so we may work with

$$
f(y,y')=\sqrt{\frac{1+y'^2}{y}}.
$$

Since $f$ has no explicit $x$-dependence, we use the Beltrami identity:

$$
f-y'\frac{\partial f}{\partial y'}=\text{constant}.
$$

Compute

$$
\frac{\partial f}{\partial y'}
=\frac{1}{\sqrt{y}}\,\frac{y'}{\sqrt{1+y'^2}}.
$$

Then

$$
f-y'\frac{\partial f}{\partial y'}
=\frac{1}{\sqrt{y}}\left(
\sqrt{1+y'^2}-\frac{y'^2}{\sqrt{1+y'^2}}
\right)
=\frac{1}{\sqrt{y\left(1+y'^2\right)}}.
$$

Setting this equal to a constant $1/\sqrt{2a}$ gives

$$
y\bigl(1+y'^2\bigr)=2a.
$$

Solving for $y'$,

$$
\frac{dy}{dx}=\sqrt{\frac{2a-y}{y}},
\qquad\text{or}\qquad
\frac{dx}{dy}=\sqrt{\frac{y}{2a-y}}.
$$

Thus

$$
x(y)=\int\sqrt{\frac{y}{2a-y}}\,dy.
$$

The integral is elementary with the substitution

$$
y=a(1-\cos\theta).
$$

Since $dy=a\sin\theta\,d\theta$, we have

$$
dx=\sqrt{\frac{a(1-\cos\theta)}{a(1+\cos\theta)}}\,a\sin\theta\,d\theta
=a(1-\cos\theta)\,d\theta,
$$

where the last equality uses $\sin\theta=\sqrt{1-\cos^2\theta}$ and simplifies.  Integrating,

$$
x=a(\theta-\sin\theta)+\text{constant}.
$$

The initial condition $x=y=0$ corresponds to $\theta=0$, so the constant is zero.  The stationary path is therefore the parametric curve

$$
\boxed{
x(\theta)=a(\theta-\sin\theta),\qquad
y(\theta)=a(1-\cos\theta)
}
$$

which is a **cycloid**: the curve traced by a point on the rim of a circle of radius $a$ rolling along the underside of the $x$-axis.  The constant $a$ is chosen so that the cycloid passes through the prescribed endpoint $(x_2,y_2)$.  This curve gives the minimum travel time among all smooth tracks joining the two points.
