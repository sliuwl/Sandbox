# Derivation of the Euler-Lagrange Equation

**Companion note to:** *[Variational Calculus](02VariationalCalculus.md)* (reading material: Chapter 6 of *Classical Mechanics* by John R. Taylor), especially Sections 4 (Variation) and 5.1 (Derivation of the Euler-Lagrange Equation). We will refer to that note as **the main note**.

One idea, used twice: **a point is stationary when the change starts at second order**. We first make this precise for an ordinary function $g(x)$, where "locally flat" means that $g(x+\varepsilon)-g(x)$ begins at order $\varepsilon^2$. We then lift the same Taylor-expansion logic to a functional $F[y]$, where the change of the input is a small function $\Delta y$: we expand in the change and require that the part linear in $\Delta y$ vanishes for every small change. The Euler–Lagrange equation is exactly what that requirement says about $y(x)$.

## Table of Contents

1. [Locally Flat in Ordinary Calculus](#1-locally-flat-in-ordinary-calculus)
   - [1.1 Stationary Means No First-Order Change](#11-stationary-means-no-first-order-change)
   - [1.2 Taylor Expansion of the Change](#12-taylor-expansion-of-the-change)
2. [From Numbers to Functions](#2-from-numbers-to-functions)
   - [2.1 The Perturbation Is an Entire Function](#21-the-perturbation-is-an-entire-function)
   - [2.2 Separating Shape from Size](#22-separating-shape-from-size)
   - [2.3 The Change of the Slope](#23-the-change-of-the-slope)
3. [Taylor Expansion of a Functional](#3-taylor-expansion-of-a-functional)
   - [3.1 The Order of a Change](#31-the-order-of-a-change)
   - [3.2 Expanding the Integrand](#32-expanding-the-integrand)
   - [3.3 The First-Order Change](#33-the-first-order-change)
4. [Stationarity and the Euler-Lagrange Equation](#4-stationarity-and-the-euler-lagrange-equation)
   - [4.1 Locally Flat in Function Space](#41-locally-flat-in-function-space)
   - [4.2 Integration by Parts](#42-integration-by-parts)
   - [4.3 The Fundamental Lemma and the Result](#43-the-fundamental-lemma-and-the-result)
5. [Summary and Dictionary](#5-summary-and-dictionary)

---

## 1. Locally Flat in Ordinary Calculus

Let $g$ be a smooth function of one variable, and fix a point $x$. To test whether $x$ is a stationary point, ordinary calculus compares $g(x)$ with $g(x+\varepsilon)$, where $\varepsilon$ is a small step that may be positive or negative:

$$
x \;\longrightarrow\; x+\varepsilon .
$$

The stationarity condition is

$$
\frac{dg(x)}{dx}=0,
$$

and we say the graph of $g$ is **locally flat (局部平坦)** at $x$. This section pins down exactly what that sentence means. The answer — *the change contains no first-order part* — is the entire content of this note, replayed one level up in Section 3.

### 1.1 Stationary Means No First-Order Change

"Locally flat" does **not** mean that $g(x+\varepsilon)-g(x)$ is zero. It means that the change contains **no part proportional to $\varepsilon$**.

To see what the derivative has to do with this, divide the change by the step. For a differentiable function,

$$
\frac{g(x+\varepsilon)-g(x)}{\varepsilon}
\;\longrightarrow\;
\frac{dg}{dx}
\qquad \text{as } \varepsilon\to 0.
$$

So the derivative is precisely the **first-order change of $g$ per unit step**: for small $\varepsilon$,

$$
g(x+\varepsilon)-g(x) \approx \frac{dg}{dx}\,\varepsilon .
$$

This linear formula is the best first-order approximation to the change, and $\frac{dg}{dx}\varepsilon$ is its only first-order part.

Therefore $\frac{dg}{dx}=0$ says exactly:

> **Locally flat.** The change $g(x+\varepsilon)-g(x)$ contains no term proportional to $\varepsilon$. To first order, $g$ does not respond to the step: moving an infinitesimal amount away from $x$ changes $g$ by nothing at first order.

### 1.2 Taylor Expansion of the Change

The claim above becomes concrete when we write out the Taylor expansion (泰勒展开) of $g(x+\varepsilon)$ around the base point $x$:

$$
g(x+\varepsilon)
=
g(x)
+
\varepsilon\,\frac{dg}{dx}
+
\frac{\varepsilon^2}{2}\,\frac{d^2g}{dx^2}
+
\frac{\varepsilon^3}{3!}\,\frac{d^3g}{dx^3}
+\cdots,
$$

where every derivative is evaluated at the point $x$. Subtracting $g(x)$ gives the change:

$$
\Delta g
\equiv
g(x+\varepsilon)-g(x)
=
\varepsilon\,\frac{dg}{dx}
+
\frac{\varepsilon^2}{2}\,\frac{d^2g}{dx^2}
+
\frac{\varepsilon^3}{3!}\,\frac{d^3g}{dx^3}
+\cdots .
$$

The condition $\frac{dg}{dx}=0$ knocks out the first term, and we obtain the equivalence

$$
\frac{dg}{dx}=0
\qquad\Longleftrightarrow\qquad
\Delta g
=
\frac{\varepsilon^2}{2}\,\frac{d^2g}{dx^2}
+O(\varepsilon^3).
$$

**In words: at a stationary point, the change starts at order $\varepsilon^2$.** The first-order term is gone; whatever change remains is second order or smaller.

This is the precise meaning of "locally flat." It does not mean the graph is a horizontal line — it means the graph has **no tilt**: the $\varepsilon$-linear part of the change, which is the part a tilted graph would produce, is absent.

Why the first-order term is the decisive one: for sufficiently small $\varepsilon$, the **lowest-order surviving term dominates** all higher ones. So if a linear term $\varepsilon\,\frac{dg}{dx}$ is present, it wins near $\varepsilon=0$; since it is odd in $\varepsilon$, it raises $g$ in one direction and lowers it in the other, so the point cannot be an extremum. Only when the linear term vanishes can the leading behavior be even in $\varepsilon$ (typically order $\varepsilon^2$), giving the same sign both ways — a bowl or a dome.



------

## 2. From Numbers to Functions

Now replace the number $x$ by an entire function $y(x)$, and the function $g$ by a functional $F[y]$ (main note, Section 2). We want to repeat Section 1 verbatim. The first job is to understand what plays the role of the small step $\varepsilon$.

### 2.1 The Perturbation Is an Entire Function

For a functional, the input is a whole curve. Changing the input therefore cannot be described by a single number: the new curve differs from the old one *at every point*. The change of the input is itself a function:

$$
y(x)
\;\longrightarrow\;
y(x)+\Delta y(x),
$$

where $\Delta y(x)$ is small on $[x_1,x_2]$, and — for the fixed-endpoint problems of the main note (Section 4.2) — it must vanish at the endpoints:

$$
\Delta y(x_1)=0, \qquad \Delta y(x_2)=0 .
$$

For example, perturbing $y(x)=x^2$ on $[0,1]$ by $\Delta y(x)=0.01\sin(\pi x)$ produces a slightly wiggled parabola that still starts and ends at the same points.

Anticipating Section 3, "locally flat" for a functional will mean: $F[y+\Delta y]-F[y]$ contains **no part linear in $\Delta y$**, for every small change $\Delta y$. But "linear in $\Delta y$" is a statement about order of smallness: we must agree on what counts as "first order" and what counts as "second order" when the small object is a whole function. Section 3.1 settles this — order is counted by the number of factors of the change — and Sections 3.2–3.3 then expand $F$ directly in $\Delta y$. It is also useful, and it is how the main note organizes the same computation, to factor the change into a shape and a size; that dictionary comes next.

### 2.2 Separating Shape from Size

Any small change of the curve can be factored into a **shape** and a **size** — this is the parametrization the main note (its Sections 4.1 and 5.1) uses to set up its derivation:

$$
\Delta y(x)=\varepsilon\,\eta(x),
\qquad\qquad
y_\varepsilon(x)=y(x)+\varepsilon\,\eta(x).
$$

Here:

- $\eta(x)$ fixes the **direction** in function space — which way we push the curve (main note, Section 4.1);
- $\varepsilon$ fixes the **step size** — how far we push it;
- $\Delta y(x)=\varepsilon\,\eta(x)$ is the resulting change of the input.

> **The notational dictionary.** The change of the input function is
> $$
> \Delta y(x)=\varepsilon\,\eta(x).
> $$
> This is the same object under two names: the symbol $\Delta y$ emphasizes that the input change is a function, while the factored form $\varepsilon\eta$ separates its size from its shape. **In the main note, the change $\Delta y$ is written as $\varepsilon\eta(x)$ precisely so that $\varepsilon$ can serve as the Taylor-expansion variable: along the family $y+\varepsilon\eta$, "$\Phi(\varepsilon)=F[y+\varepsilon\eta]$ is an ordinary function of $\varepsilon$" takes over from ordinary calculus.** Fixed endpoints read $\eta(x_1)=\eta(x_2)=0$.

Two roads, one destination — the view taken in this note is that $\varepsilon\eta$ is the *dressed* form of the change $\Delta y$: the Taylor expansion of Section 3 can be performed directly in the change itself, and the factorization can be left implicit, exactly as on a line the change is a single number that nobody factors. But the factorization forces a question that must be answered anyway: **how big is a change?** The integrand $f(x,y,y')$ responds to $\Delta y$ *and* to the induced $\Delta y'$ (Section 2.3), so a change must count as small only when the curve *and* its slope are displaced little. Accordingly, the size of a change is measured by

$$
\lVert\Delta y\rVert
\;=\;
\max\Bigl(\max_{[x_1,x_2]}\lvert\Delta y(x)\rvert,\;\max_{[x_1,x_2]}\lvert\Delta y'(x)\rvert\Bigr),
$$

and a change is small when $\lVert\Delta y\rVert\ll1$. This measure scales correctly — $\lVert\lambda\,\Delta y\rVert=\lvert\lambda\rvert\,\lVert\Delta y\rVert$, and $-\Delta y$ is exactly as small as $\Delta y$ — and it splits the factorized form cleanly: one may always take $\varepsilon=\lVert\Delta y\rVert$ and $\eta=\Delta y/\varepsilon$, so that $\lVert\eta\rVert=1$ — **the size lives in $\varepsilon$, the unit-sized shape in $\eta$**. Section 3.1 uses this measure to say what "first order" and "second order" mean.

Comparing with ordinary calculus makes the structural difference visible:

- On a line, there is only *one* direction: the step $\varepsilon$ is a number, and its sign is the only directional information.
- In function space, there are *infinitely many* directions: **one $\Delta y$ per way of deforming the curve**. Directions are labeled by functions — we may take the direction to be $\Delta y$ itself, or equivalently the normalized shape $\eta=\Delta y/\lVert\Delta y\rVert$.

Holding one direction $\Delta y$ fixed and scaling it to $\lambda\,\Delta y$ for small $\lambda$ traces out a segment through $y$ in that direction, the function-space analogue of the line through $x$. In the main note's parametrization, the same segment is generated by holding the shape $\eta$ fixed and letting $\varepsilon$ run over a small interval: the family $y_\varepsilon=y+\varepsilon\eta$.

### 2.3 The Change of the Slope

If the curve changes by $\Delta y$, its slope changes too, and the change of the slope is the slope of the change:

$$
\bigl(y+\Delta y\bigr)'(x)=y'(x)+\Delta y'(x),
\qquad\text{i.e.}\qquad
\Delta y'(x)=\frac{d}{dx}\,\Delta y(x).
$$

Because the variation moves the curve but never the independent variable $x$, varying and differentiating commute (main note, Section 4.4). In the factorized notation of the main note, $\Delta y=\varepsilon\,\delta y$ with $\delta y=\eta$ — the change with its size divided out — and this commutation is the statement $\delta y'=\frac{d}{dx}\delta y$ there; it is the display above, $\Delta y'=\frac{d}{dx}\Delta y$, here.

This matters because the integrand $f(x,y,y')$ depends on both $y$ and $y'$. When the input function changes, **both** slots of $f$ shift, and by the same amount:

$$
\bigl(y,\;y'\bigr)
\;\longrightarrow\;
\bigl(y+\Delta y,\;y'+\Delta y'\bigr).
$$

Both shifts must be kept in the Taylor expansion of the next section.

------

## 3. Taylor Expansion of a Functional

We now have everything needed to expand $F[y+\Delta y]$ "around $y$," in exact analogy with $g(x+\varepsilon)$ around $x$. Throughout this section, $\Delta y$ is one fixed, small, smooth change that vanishes at the endpoints (Section 2), and $\Delta y'=\frac{d}{dx}\,\Delta y$ is the accompanying change of the slope (Section 2.3).

### 3.1 The Order of a Change

Order counts factors of the change. This rule, which does all the work below, is taken directly from Section 1: there, "first-order part" meant the term $\varepsilon\,g'(x)$ with exactly **one factor of the step**, and "second order" meant terms like $\tfrac{\varepsilon^2}{2}g''(x)$ with **two factors of the step**. Nothing in that bookkeeping used the fact that the step was a *number* — only that it was the *small object being counted*. So we adopt, for functionals:

> **Order of a term = the number of factors of the change ($\Delta y$ or $\Delta y'$) it carries.**
> A term with one factor is **first order**; a term with two factors is **second order**; and so on. "The part linear in the change" and "the first-order part" are synonyms.

The rule is meaningful because of how the change enters the functional. When $y\to y+\Delta y$, the integrand $f(x,y,y')$ is evaluated at shifted arguments, and *ordinary* Taylor expansion in its second and third slots gives terms that carry the increments $\Delta y$ and $\Delta y'$ openly, factor by factor:

$$
\text{zeroth order: } f(x,y,y'),\qquad
\text{first: } \frac{\partial f}{\partial y}\Delta y, \ \ \frac{\partial f}{\partial y'}\Delta y',\qquad
\text{second: } \tfrac{1}{2}\frac{\partial^2 f}{\partial y^2}(\Delta y)^2,\ \ldots
$$

Every term is a smooth coefficient — evaluated on the unperturbed curve — times a monomial in the change; the order of the term is the degree of that monomial. Integration over $x$ sums orders without mixing them (Section 3.3), so the same classification applies to $F$ itself:

- the **first variation (一阶变分)** $\delta F[y;\Delta y]$ is the first-order part of the change of $F$ — the functional's analogue of $\varepsilon\,\frac{dg}{dx}$;
- the **second variation (二阶变分)**, e.g. $\tfrac{1}{2}\delta^2F[y;\Delta y]$, is the second-order part — the analogue of $\tfrac{\varepsilon^2}{2}\,\frac{d^2g}{dx^2}$; it decides minimum vs. maximum vs. saddle and is set aside until then.

Why "higher order" really is negligible. Fix one smooth change $\Delta y$ and scale it: $y_\lambda=y+\lambda\,\Delta y$, $0\le\lambda\le1$ — the segment through $y$ in the direction $\Delta y$ (Section 2.2; in the main note's language, the family $y+\varepsilon\eta$ with shape $\eta=\Delta y$ and step $\varepsilon=\lambda$). The original curve is $\lambda=0$, the perturbed one $\lambda=1$. For each $\lambda$, the value $F[y_\lambda]$ is a number, and the one-variable calculus of Section 1 applies to the ordinary function $\lambda\mapsto F[y+\lambda\Delta y]$. Its Taylor expansion at $\lambda=0$ is

$$
F[y+\lambda\,\Delta y]
=F[y]
+\lambda\,\delta F[y;\Delta y]
+\tfrac{\lambda^2}{2}\,\delta^2F[y;\Delta y]
+\cdots,
$$

and setting $\lambda=1$ — the actual change, made at once — gives the expansion of $F$ in the change itself. All the counting is now visible: a $k$-th order term of $F[y+\Delta y]$ is exactly the degree-$k$ monomial in the change, with its coefficient fixed by the curve $y$ alone. Quadratic terms therefore come with two factors of the change; since $\lVert\lambda\,\Delta y\rVert$ never exceeds $\lVert\Delta y\rVert$, their size is controlled — through the sup-norm measure of Section 2.2 — by a constant multiple of $\lVert\Delta y\rVert^2$, i.e. they are $O(\lVert\Delta y\rVert^2)$. Generally:

$$
\text{sum of all terms of order }\ge k \;=\; O(\lVert\Delta y\rVert^{\,k}) .
$$

This is the exact sense in which terms of higher order "don't matter at first order": they are bounded by a higher power of the size of the same change. The derivation below keeps everything through first order and lumps the rest into $O(\lVert\Delta y\rVert^2)$.

One more piece of structure, for later. The first-order part is *linear* in the change: scaling $\Delta y\to c\,\Delta y$ scales it by $c$, and superposing changes superposes first-order parts,

$$
\delta F[y;\Delta y_1+\Delta y_2]=\delta F[y;\Delta y_1]+\delta F[y;\Delta y_2],
$$

for admissible changes (those vanishing at the endpoints, Section 2.1) — the functional's analogue of $\Delta g$ being linear in the step, and the exact parallel of $\delta F[y;\eta]$ being linear in $\eta$ (main note, Section 4.3). On this point, in fact, we could equally phrase everything using the main note's convention: divide the change by its size and integrate along the family; what matters is that the choice made here — expand directly in $\Delta y$ — makes the statement $F[y+\Delta y]-F[y]=\delta F[y;\Delta y]+O(\lVert\Delta y\rVert^2)$, with the first variation *defined* as its first-order part, as stated in Section 4.3 of the main note; in this note $\delta F[y;\Delta y]$ is simply the integrated version of $\varepsilon\,\delta F[y;\eta]$ with $\varepsilon\eta=\Delta y$, i.e. the same quantity under the two conventions — because both are the sum of degree-one monomials in the change, and that sum does not depend on any parametrization.

What remains is to compute $\delta F[y;\Delta y]$ explicitly for the standard functional.

### 3.2 Expanding the Integrand

Consider

$$
F[y]=\int_{x_1}^{x_2} f\left(x,y(x),y'(x)\right)\,dx,
$$

with fixed endpoints $y(x_1)=y_1$, $y(x_2)=y_2$. Evaluated on the perturbed curve,

$$
F[y+\Delta y]
=
\int_{x_1}^{x_2}
f\left(x,\;y+\Delta y,\;y'+\Delta y'\right)\,dx .
$$

The only thing that changed is the input curve, so the integrand must be expanded in the change of the input. At each fixed $x$, $f$ is an ordinary smooth function of its second and third arguments near $(y(x),y'(x))$, and the change moves both slots by the displacements $\Delta y(x)$ and $\Delta y'(x)$ (Section 2.3). Ordinary Taylor expansion of a function of two variables, in both arguments at once, gives

$$
f\left(x,\;y+\Delta y,\;y'+\Delta y'\right)
=
f\left(x,y,y'\right)
+
\left(
\frac{\partial f}{\partial y}\,\Delta y
+
\frac{\partial f}{\partial y'}\,\Delta y'
\right)
+
O(\lVert\Delta y\rVert^2),
$$

where the partial derivatives are evaluated along the unperturbed curve, at $\left(x,\,y(x),\,y'(x)\right)$.

The parenthesis is the familiar total differential of multivariable calculus (main note, Section 5.1),

$$
df=\frac{\partial f}{\partial y}\,dy+\frac{\partial f}{\partial y'}\,dy',
$$

with the small displacements $dy=\Delta y(x)$ and $dy'=\Delta y'(x)$: each slot of $f$ contributes its own partial derivative times the displacement of that slot. The three-term structure — value, plus one linear correction per shifted argument, plus quadratics — is the two-variable version of the one-variable expansion of Section 1.2, with the difference that here *two* arguments shift, so the first-order part has *two* contributions, one per slot. In the order language of Section 3.1: the parenthesis carries exactly one factor of the change, one for each way the change enters; the remainder carries at least two.

The remainder estimate. Since $\Delta y$ is fixed and smooth, the implicit-function constant in the remainder is controlled on the compact interval $[x_1,x_2]$: the exact statement is

$$
f\left(x,\;y+\Delta y,\;y'+\Delta y'\right)
=
f\left(x,y,y'\right)
+
\left(
\frac{\partial f}{\partial y}\,\Delta y(x)
+
\frac{\partial f}{\partial y'}\,\Delta y'(x)
\right)
+
R(x),
\qquad
|R(x)|\le C\,\lVert\Delta y\rVert^2,
$$

with $C$ depending only on $f$ and $y$ on a fixed neighborhood of the curve — for smooth $f$, the constant is uniform because the relevant second derivatives of $f$ are bounded on compact sets. This is the sense in which the remainder is "second and higher order" in the change: after the fact, one may check it by inserting $t\,\Delta y$ in place of $\Delta y$ and verifying that the displaced term behaves as $t^2$, which is what the main note's $\varepsilon$-parametrized version (its Section 5.1) makes explicit. Everything below needs only: *the error is bounded by a constant multiple of $\lVert\Delta y\rVert^2$.*

Now integrate over $x$. The first term integrates to $F[y]$. The parenthesis integrates to the first-order part of the change of $F$; the remainder stays controlled, because

$$
\Bigl|\int_{x_1}^{x_2} R(x)\,dx\Bigr|
\le
C\,(x_2-x_1)\,\lVert\Delta y\rVert^2
=
O(\lVert\Delta y\rVert^2).
$$

The result:

$$
F[y+\Delta y]
=
F[y]
+
\int_{x_1}^{x_2}
\left(
\frac{\partial f}{\partial y}\,\Delta y
+
\frac{\partial f}{\partial y'}\,\Delta y'
\right)dx
+
O(\lVert\Delta y\rVert^2).
$$

Reading off the first-order part (Section 3.1):

$$
\delta F[y;\Delta y]
=
\int_{x_1}^{x_2}
\left(
\frac{\partial f}{\partial y}\,\Delta y
+
\frac{\partial f}{\partial y'}\,\Delta y'
\right)dx ,
$$

which is the first-variation formula of the main note, Section 5.1, with $\eta$ replaced by the change itself and the factor $\varepsilon$ never introduced — the same integral, written in the undressed notation.

### 3.3 The First-Order Change

Assembled, the expansion of the functional in its input's change reads

$$
F[y+\Delta y]
=
F[y]
+
\underbrace{\int_{x_1}^{x_2}
\left(
\frac{\partial f}{\partial y}\,\Delta y
+
\frac{\partial f}{\partial y'}\,\Delta y'
\right)dx}_{\displaystyle \delta F[y;\Delta y]\;\text{— one factor of the change}}
+
O(\lVert\Delta y\rVert^2).
$$

**The entire first-order change of the functional is linear in the change of the input.** It is "proportional to $\Delta y$": double the change, double the first-order response; superpose two changes, and the first-order responses superpose — as claimed in Section 3.1, and now visible in the formula, since $\Delta y$ and $\Delta y'$ enter the integrand only through first powers, with coefficients fixed by $y$ alone. This is the functional analogue of the fact that the first-order change of $g$ is proportional to $\varepsilon$.

> **Note on rigor.** The phrase "higher order in $\Delta y$" is a statement about a bound, not a limit along a family: it means the term is $O(\lVert\Delta y\rVert^2)$ — bounded by a constant times the square of the size of the change (Section 2.2) — uniformly over the changes considered. Equivalently, and closer to the main note's organization, it can be phrased as a limit along each family: writing the change as $\Delta y=\varepsilon\eta$ with fixed shape $\eta$, "second order" means $O(\varepsilon^2)$ as $\varepsilon\to0$ for that family. That is the version the main note (its Sections 4.3 and 5.1) develops; the two formulations are interchangeable, since the bound version implies the limit version for every family, and the family version for arbitrary shapes implies the bound.

------

## 4. Stationarity and the Euler-Lagrange Equation

### 4.1 Locally Flat in Function Space

Suppose $y(x)$ is a **stationary function** of $F$ (main note, Section 4.5): the first variation vanishes in *every* admissible direction,

$$
\delta F[y;\Delta y]=0
\qquad
\text{for every smooth } \Delta y \text{ with } \Delta y(x_1)=\Delta y(x_2)=0 .
$$

In the Taylor language of this note, that says:

$$
F[y+\Delta y]-F[y]
=
O(\lVert\Delta y\rVert^2)
\qquad
\text{for every admissible change } \Delta y .
$$

This is the definition of **locally flat in function space**, and it is the lift of $\frac{dg}{dx}=0$:

> Push the curve away from $y(x)$ in *any* allowed way, by *any* small amount. To first order, the functional does not respond. Whatever change $F$ shows begins at second order.

The task is now purely computational: impose $\delta F[y;\Delta y]=0$ on the explicit formula of Section 3.2 and see what it forces $y(x)$ to satisfy.

### 4.2 Integration by Parts

Set the first variation to zero:

$$
0=\delta F[y;\Delta y]
=
\int_{x_1}^{x_2}
\left(
\frac{\partial f}{\partial y}\,\Delta y
+
\frac{\partial f}{\partial y'}\,\Delta y'
\right)dx .
$$

The second term still involves $\Delta y'$. We want every dependence on the change to enter through the single factor $\Delta y$, so that "for every $\Delta y$" can be exploited. Integrate the second term by parts:

> Recall (main note, Section 5.1)
> $$
> \int_a^b u\,v'\,dx=\int_a^b u\,dv=\left.(uv)\right|_a^b-\int_a^b v\,du .
> $$

With $u=\frac{\partial f}{\partial y'}$ and $v=\Delta y$ (Section 2.3: $v'=\Delta y'$):

$$
\int_{x_1}^{x_2}\frac{\partial f}{\partial y'}\,\Delta y'\,dx
=
\underbrace{\left.\frac{\partial f}{\partial y'}\,\Delta y\right|_{x_1}^{x_2}}_{=\,0}
-\int_{x_1}^{x_2}
\frac{d}{dx}\!\left(\frac{\partial f}{\partial y'}\right)\Delta y\,dx ,
$$

where the boundary term vanishes because the endpoints are fixed, $\Delta y(x_1)=\Delta y(x_2)=0$. The first variation becomes

$$
\delta F[y;\Delta y]
=
\int_{x_1}^{x_2}
\Delta y(x)\left[
\frac{\partial f}{\partial y}
-
\frac{d}{dx}\left(\frac{\partial f}{\partial y'}\right)
\right]dx .
$$

Here $\frac{d}{dx}$ is the **total derivative** along the curve: it acts on $\frac{\partial f}{\partial y'}\bigl(x,y(x),y'(x)\bigr)$ through the explicit $x$, and through $y(x)$ and $y'(x)$ as well.

### 4.3 The Fundamental Lemma and the Result

Stationarity requires

$$
\int_{x_1}^{x_2}\eta(x)\,g(x)\,dx=0
\quad\text{for every admissible }\eta,
\qquad
g(x)\equiv
\frac{\partial f}{\partial y}
-
\frac{d}{dx}\left(\frac{\partial f}{\partial y'}\right).
$$

By the **fundamental lemma of the calculus of variations** (main note, Section 5.2), a continuous $g$ that integrates to zero against every such $\eta$ must vanish identically. (Intuition: if $g(x_0)\neq0$, take $\eta$ to be a smooth bump concentrated near $x_0$; the integrand is then positive on that bump, contradicting the vanishing integral.)

Therefore $y(x)$ must satisfy the **Euler–Lagrange equation**:

$$
\boxed{\;
\frac{\partial f}{\partial y}
-
\frac{d}{dx}\frac{\partial f}{\partial y'}
=0
\;}
$$

Two remarks on what just happened:

- **Infinitely many directions collapse into one equation.** On a line there is only one direction to test, and stationarity is the single condition $\frac{dg}{dx}=0$. In function space, "no first-order change" must hold for infinitely many directions $\eta$ — a priori infinitely many conditions. The fundamental lemma collapses all of them into a single condition holding *at every point*: the bracket vanishes identically on $[x_1,x_2]$. Carrying out the total derivative turns the Euler–Lagrange equation into a second-order ordinary differential equation, closed by the two boundary conditions $y(x_1)=y_1$, $y(x_2)=y_2$ (main note, Section 7).
- **Stationarity is only the first-order condition.** Exactly as with $g(x)=x^3$ in Section 1.3, the Euler–Lagrange equation is *necessary* for an extremal path but does not decide minimum, maximum, or saddle. That decision belongs to the next Taylor coefficient — the second variation — except that in function space saddle behavior is generic: a path that is minimal against some perturbations can be maximal against others.

------

## 5. Summary and Dictionary

The derivation of this note is one line long, and it is the same line twice:

$$
\text{expand } g(x+\varepsilon) \text{ about } x;
\qquad
\text{expand } F[y+\varepsilon\eta] \text{ about } y;
\qquad
\text{stationarity}=\text{the linear term vanishes.}
$$

| Ordinary calculus | Calculus of variations |
|---|---|
| Input: a number $x$ | Input: an entire function $y(x)$ |
| Output: a number $g(x)$ | Output: a number $F[y]$ |
| Small step: a number $\varepsilon$ | Small step: a function $\Delta y(x)=\varepsilon\,\eta(x)$ |
| Direction: the sign of $\varepsilon$ (only two) | Direction: the shape $\eta(x)$ (infinitely many) |
| Size of the step: $\lvert\varepsilon\rvert$ | Size of the step: $\lvert\varepsilon\rvert$ |
| Taylor: $g(x+\varepsilon)=g(x)+\varepsilon\,g'(x)+\frac{\varepsilon^2}{2}g''(x)+\cdots$ | Taylor: $F[y+\varepsilon\eta]=F[y]+\varepsilon\,\delta F[y;\eta]+\frac{\varepsilon^2}{2}\delta^2F[y;\eta]+\cdots$ |
| First-order change: $\varepsilon\,g'(x)$, proportional to the step | First-order change: $\varepsilon\,\delta F[y;\eta]$, proportional to $\Delta y=\varepsilon\eta$ |
| Stationary point: $g'(x)=0$ | Stationary function: $\delta F[y;\eta]=0$ for every admissible $\eta$ |
| Meaning: $\Delta g$ starts at $\varepsilon^2$ | Meaning: $F[y+\Delta y]-F[y]$ starts at $\varepsilon^2$ in every direction |
| One direction $\Rightarrow$ one condition $g'(x)=0$ | Infinitely many directions $\Rightarrow$ (by the fundamental lemma) one condition at every point — the Euler–Lagrange equation |
| $g''$ decides min / max | The second variation decides min / max / saddle |

Finally, the physics payoff. In Lagrangian mechanics the functional is the **action** (main note, Section 2),

$$
S[q]=\int_{t_1}^{t_2}L\left(t,q,\dot q\right)dt,
\qquad \dot q=\frac{dq}{dt},
$$

and Hamilton's principle says the physical path makes it stationary, $\delta S=0$. Running the derivation of Sections 3–4 on $S$ — expand $S[q+\varepsilon\eta]$ in $\varepsilon$, keep the term linear in the change $\Delta q=\varepsilon\eta$, integrate by parts, invoke the lemma — produces

$$
\frac{\partial L}{\partial q}
-
\frac{d}{dt}\frac{\partial L}{\partial \dot q}
=0,
$$

Lagrange's equation of motion, the subject of the next note ([03LagrangianMechanics-A.md](03LagrangianMechanics-A.md)).

**The Euler–Lagrange equation is the statement $\frac{dg}{dx}=0$, lifted from points to functions: a stationary function is one where every change of the input that is linear in the perturbation produces no response, so whatever change remains in the functional begins at second order.**
