## 5.1 Derivation of the Euler–Lagrange Equation

### 1. Ordinary Calculus: Stationary Means No First-Order Change

Let $g(x)$ be a smooth function. To test whether $x$ is a stationary point, compare $g(x)$ and $g(x+\varepsilon)$, where $\varepsilon$ is small.

Taylor expand around $x$:
\[
g(x+\varepsilon) = g(x) + \varepsilon \frac{dg}{dx} + O(\varepsilon^2).
\]
Thus,
\[
(x+\varepsilon)-g(x) = \varepsilon \frac{dg}{dx} + O(\varepsilon^2)
\]
Therefore,
\[
\frac{dg}{dx}=0
\]
means the change has **no first-order term**. This is the precise meaning of being **locally flat**.

------

### 2. Functionals: The Same Idea in Function Space

Now consider the functional
\[
F[y] = \int_{x_1}^{x_2} f(x,y,y')\,dx,
\]
with fixed boundary values $y(x_1)$ and $y(x_2)$.

To test whether $y(x)$ is stationary, perturb it:

$y_\varepsilon(x) = y(x)+\varepsilon\eta(x),$

where

$\eta(x_1)=\eta(x_2)=0.$

The derivative also changes:

$y_\varepsilon'(x) = y'(x)+\varepsilon\eta'(x).$

So
\[
F[y+\varepsilon\eta] = \int_{x_1}^{x_2} f(x,y+\varepsilon\eta,y'+\varepsilon\eta')\,dx.
\]

------

### 3. Taylor Expand Around $y$

At each $x$, expand the integrand around the original values $y(x)$ and $y'(x)$:
\[
f(x,y+\varepsilon\eta,y'+\varepsilon\eta') = f(x,y,y') + \varepsilon \left( \frac{\partial f}{\partial y}\eta + \frac{\partial f}{\partial y'}\eta' \right) + O(\varepsilon^2).
\]
Therefore,
\[
F[y+\varepsilon\eta] = F[y] + \varepsilon \int_{x_1}^{x_2} \left( \frac{\partial f}{\partial y}\eta + \frac{\partial f}{\partial y'}\eta' \right)dx + O(\varepsilon^2).
\]
The coefficient of $\varepsilon$ is the first variation:
\[
\delta F[y;\eta] = \int_{x_1}^{x_2} \left( \frac{\partial f}{\partial y}\eta + \frac{\partial f}{\partial y'}\eta' \right)dx.
\]
A stationary function satisfies $\delta F[y;\eta]=0$ for every admissible $\eta$.

------

### 4. Integration by Parts

The term containing $\eta'$ is integrated by parts:
\[
\int_{x_1}^{x_2} \frac{\partial f}{\partial y'}\eta'\,dx = \left. \frac{\partial f}{\partial y'}\eta \right|_{x_1}^{x_2} - \int_{x_1}^{x_2} \eta \frac{d}{dx} \left( \frac{\partial f}{\partial y'} \right)dx.
\]
Since $\eta(x_1)=\eta(x_2)=0$, the boundary term vanishes. Hence
\[
\delta F[y;\eta] = \int_{x_1}^{x_2} \eta \left[ \frac{\partial f}{\partial y} - \frac{d}{dx} \left( \frac{\partial f}{\partial y'} \right) \right]dx.
\]

------

### 5. Euler–Lagrange Equation

For stationarity, this must vanish for every $\eta$:
\[
\int_{x_1}^{x_2} \eta \left[ \frac{\partial f}{\partial y} - \frac{d}{dx} \left( \frac{\partial f}{\partial y'} \right) \right]dx = 0.
\]
By the fundamental lemma of the calculus of variations,
\[
\frac{\partial f}{\partial y} - \frac{d}{dx} \left( \frac{\partial f}{\partial y'} \right) = 0.
\]
Therefore,
\[
\boxed{ \frac{d}{dx} \left( \frac{\partial f}{\partial y'} \right) - \frac{\partial f}{\partial y} = 0 }
\]
is the Euler–Lagrange equation.

------

### Key Point

The derivation is just Taylor expansion in function space:

$F[y+\varepsilon\eta] = F[y] + \varepsilon \delta F[y;\eta] + O(\varepsilon^2).$

Stationary means the first-order term vanishes:

$\delta F[y;\eta]=0.$

