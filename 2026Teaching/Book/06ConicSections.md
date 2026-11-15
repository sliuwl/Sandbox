# Conic Sections and the Kepler Orbit Equation

**Reading material:** Section 8.6 of *Classical Mechanics* by John R. Taylor; §3.7 of *Classical Mechanics* by Herbert Goldstein.

## Table of Contents

1. [The Orbit Equation as a Conic](#1-the-orbit-equation-as-a-conic)
2. [Focus, Directrix, and the Meaning of p and e](#2-focus-directrix-and-the-meaning-of-p-and-e)
3. [The Four Eccentricity Cases](#3-the-four-eccentricity-cases)
   - [3.1 Circle](#31-circle)
   - [3.2 Ellipse](#32-ellipse)
   - [3.3 Parabola](#33-parabola)
   - [3.4 Hyperbola](#34-hyperbola)
4. [Cartesian Forms and Standard Parameters](#4-cartesian-forms-and-standard-parameters)
5. [Eccentricity and Energy](#5-eccentricity-and-energy)
6. [Summary](#6-summary)

---

## 1. The Orbit Equation as a Conic

The integrated orbit of the Kepler problem is

$$
\boxed{r(\theta)=\frac{p}{1+e\cos(\theta-\theta')},
\qquad
p=\frac{\ell^2}{mk}.}
$$

The origin is the force center, and the force is $F(r)=-k/r^2$ with $k>0$. The mass is $m$ and $\ell=|\mathbf L|$ is the constant angular momentum. The equation contains three constants:

- $p>0$, the **semi-latus rectum** (半通径), fixed by the angular momentum through $p=\ell^2/(mk)$;
- $e\ge0$, the dimensionless **eccentricity** (偏心率), which selects the type of conic;
- $\theta'$, the direction of the **periapsis** (近拱点), which only rotates the curve about the focus.

Because $\theta'$ fixes only the orientation, measure the polar angle from the periapsis direction:

$$
\phi=\theta-\theta',
\qquad
x=r\cos\phi,
\qquad
y=r\sin\phi.
$$

In these coordinates the orbit equation depends on $e$ alone:

$$
\boxed{r(\phi)=\frac{p}{1+e\cos\phi}.}
$$

> **Convention.** The polar axis $\phi=0$ points to the periapsis, so $r(0)=p/(1+e)$ is the distance of closest approach for every $e\ge0$. The polar origin is the focus, not the geometric center of the curve.

Three facts follow at once from the denominator:

1. Since $\cos\phi\le1$, the denominator is largest at $\phi=0$; therefore $r$ is smallest at periapsis.
2. At $\phi=\pm\pi/2$, $\cos\phi=0$ and $r=p$ for every $e$. Thus $p$ is the distance from the focus to the conic perpendicular to the axis, and the chord through the focus in that direction — the **latus rectum** (通径) — has length $2p$.
3. The denominator vanishes only when $e\ge1$ and $\cos\phi=-1/e$. That vanishing is the dividing line between bounded and unbounded curves.

------

## 2. Focus, Directrix, and the Meaning of p and e

Rewrite the orbit equation as

$$
r+e\,r\cos\phi=p.
$$

Since $x=r\cos\phi$,

$$
r=p-ex.
$$

Set $d=p/e$, so that $p=ed$. Then

$$
r=e(d-x).
$$

The left side is the distance from a point on the curve to the focus at the origin. The right side is $e$ times the horizontal distance from that point to the vertical line $x=d$. Therefore the conic is the locus of points whose distance to the focus is $e$ times their distance to the line $x=d$. The line is the **directrix** (准线), and

$$
d=\frac{p}{e}
$$

is the distance from the focus to the directrix.

![Focus-directrix construction for conics](CentralForceImage/focus-directrix-conics.png)

**Figure 1.** The focus–directrix construction for a common directrix $x=d$ (with $d=1$ in the plot) and three eccentricities: ellipse ($e=0.6$), parabola ($e=1$), and hyperbola ($e=1.5$). The focus $F$ is at the origin. For the marked point $P$ on each curve, the solid segment is the distance $r$ to the focus and the dashed horizontal segment is the distance $d-x$ to the directrix, so the curves satisfy $r=e(d-x)$. For the ellipse the focus distance is shorter than the directrix distance, for the parabola the two are equal, and for the hyperbola the focus distance is longer. Since $p=ed$, the semi-latus rectum changes with $e$ when $d$ is held fixed. At $e=0$ the construction degenerates ($d\to\infty$) and the curve is a circle centered on the focus.

- For $0<e<1$, a point on the curve is closer to the focus than to the directrix, and the curve is closed.
- For $e=1$, the two distances are equal: this is the definition of a parabola.
- For $e>1$, the directrix distance grows more slowly than the focus distance as the curve recedes; the curve is open.
- At $e=0$ the construction degenerates, since $d\to\infty$: the focus-distance condition alone fixes a circle.

> **Why $p$ is the natural scale.** The energy fixes only $e$ (Section 5), while the angular momentum fixes $p$. For fixed $\ell$, all conics of the family share the same $p$ and differ only in $e$.

------

## 3. The Four Eccentricity Cases

Fig. 8.11 of Taylor draws the four classes with the same periapsis distance:

![Kepler conics](CentralForceImage/taylor-8.11-kepler-conics.jpg)

**Figure 2.** The four classes of Kepler orbit: circle ($e=0$), ellipse ($0<e<1$), parabola ($e=1$), and hyperbola ($e>1$), drawn with the same periapsis distance and the same direction of closest approach. (Taylor, *Classical Mechanics*, Fig. 8.11.)

### 3.1 Circle

At $e=0$,

$$
r(\phi)=p
$$

for every $\phi$. The distance from the focus is constant, so the curve is a **circle** (圆) of radius $p$ centered on the force center. The two foci coincide at the center, every direction is a periapsis, and $\theta'$ has no geometric meaning.

The circle is the minimum-energy orbit for a given $\ell$; see Section 5.

------

### 3.2 Ellipse

For $0<e<1$ the denominator never vanishes, because $e\cos\phi>-1$. The curve is an **ellipse** (椭圆). The radial distance oscillates between two finite values:

$$
r_{\min}=r(0)=\frac{p}{1+e},
\qquad
r_{\max}=r(\pi)=\frac{p}{1-e}.
$$

The points $\phi=0$ and $\phi=\pi$ are the **periapsis** (近拱点) and **apoapsis** (远拱点). Their sum is the major axis:

$$
2a=r_{\min}+r_{\max}
=\frac{p}{1+e}+\frac{p}{1-e}
=\frac{2p}{1-e^2}.
$$

Hence the **semimajor axis** (半长轴) is

$$
a=\frac{r_{\min}+r_{\max}}{2}=\frac{p}{1-e^2}.
$$

To locate the center and the foci, note that the two vertices lie on the $x$-axis at

$$
x_{\mathrm{peri}}=\frac{p}{1+e},
\qquad
x_{\mathrm{apo}}=-\frac{p}{1-e}.
$$

Their midpoint is the geometric center $C$:

$$
x_C=\frac{1}{2}\left(\frac{p}{1+e}-\frac{p}{1-e}\right)
=-\frac{pe}{1-e^2}=-ae.
$$

Thus the distance from $C$ to the focus $F$ at the origin is

$$
c\equiv |x_C|=ae,
$$

and the second focus $F'$ is symmetric about $C$, at $x=-2ae$; the focal separation is $2c=2ae$.

To find the **semiminor axis** (半短轴) $b$, consider the top vertex $T$ of the ellipse. By symmetry of the ellipse about its axes, $T$ lies directly above $C$, so

$$
T=(-ae,\,b).
$$

At $T$ the focus-directrix relation from Section 2 gives

$$
|TF|=e\,\mathrm{dist}(T,\ell),
$$

where $F$ is the focus at the origin and $\ell$ is the directrix $x=d=p/e$. Now

$$
|TF|=\sqrt{(ae)^2+b^2},
\qquad
\mathrm{dist}(T,\ell)=d-x_T=\frac{p}{e}+ae.
$$

Substituting,

$$
\sqrt{a^2e^2+b^2}
=e\left(\frac{p}{e}+ae\right)
=p+ae^2.
$$

Since $a=p/(1-e^2)$, we have $p=a(1-e^2)$, so

$$
p+ae^2=a(1-e^2)+ae^2=a.
$$

Therefore

$$
\sqrt{a^2e^2+b^2}=a
\quad\Longrightarrow\quad
b^2=a^2(1-e^2),
$$

and hence

$$
b=a\sqrt{1-e^2}=\frac{p}{\sqrt{1-e^2}}.
$$

The ellipse parameters are therefore

$$
\boxed{a=\frac{p}{1-e^2},
\qquad
b=\frac{p}{\sqrt{1-e^2}},
\qquad
c=ae.}
$$

Equivalently, since $c=ae$,

$$
b^2+c^2=a^2(1-e^2)+a^2e^2=a^2.
$$

Thus the triangle $CFT$ in Figure 3 is right-angled at $C$, with legs $b$ and $c$ and hypotenuse $a$.

The ellipse is bounded:

$$
\frac{p}{1+e}\le r\le\frac{p}{1-e}.
$$

As $e\to0$, $a\to p$ and $b\to p$: the ellipse shrinks onto the circle. As $e\to1^-$, $r_{\max}\to\infty$ while $r_{\min}\to p/2$: the far side of the ellipse recedes and the curve approaches a parabola.

![Ellipse geometry](CentralForceImage/ellipse-abc-p.png)

**Figure 3.** Geometry of a bound Kepler ellipse with the force center at the focus $F$ (the origin). The geometric center is $C$, and $F'$ is the second focus; only $F$ is the force center. The semimajor axis $a$ runs from $C$ to the periapsis vertex, the semiminor axis $b$ from $C$ to the top vertex, and the focal distance $c$ from $C$ to $F$. The semi-latus rectum $p$ is the distance from $F$ to the curve perpendicular to the major axis; the full latus rectum is the chord of length $2p$. The dashed segment from $F$ to the top vertex has length $a$, so $CFT$ is a right triangle with $b^2+c^2=a^2$. The figure is drawn for $e=0.6$, with $a=1$, $b=0.8$, $c=0.6$, and $p=0.64$. The right vertex is the periapsis ($r_{\min}=a(1-e)$) and the left vertex is the apoapsis ($r_{\max}=a(1+e)$).

------

### 3.3 Parabola

At $e=1$,

$$
r(\phi)=\frac{p}{1+\cos\phi}
=\frac{p}{2\cos^2(\phi/2)}.
$$

The denominator vanishes at $\phi=\pm\pi$, so $r\to\infty$ in those directions. The curve is a **parabola** (抛物线), open toward negative $x$, with a single apsis

$$
r_{\min}=r(0)=\frac{p}{2}.
$$

There is no apoapsis and no finite semimajor axis. The parameter $p$ is twice the focal length: the vertex lies halfway between the focus at the origin and the directrix at $x=p$.

#### 3.3.1 From the focus–directrix definition to $x^2=4ay$

The form students know from analytic geometry is obtained by moving the origin to the vertex and putting the axis of the parabola along the $y$-axis. Then the focus is at $(0,a)$ and the directrix is the horizontal line $y=-a$, with

$$
p=2a.
$$

A point $(x,y)$ lies on the parabola exactly when its distance to the focus equals its distance to the directrix:

$$
\sqrt{x^2+(y-a)^2}=y+a.
$$

Both sides are non-negative on the curve, so squaring is reversible:

$$
x^2+(y-a)^2=(y+a)^2
\quad\Longrightarrow\quad
x^2-2ay+a^2=2ay+a^2
\quad\Longrightarrow\quad
\boxed{x^2=4ay,\qquad a=\frac{p}{2}.}
$$

Swapping the roles of $x$ and $y$ gives the horizontal version $y^2=4ax$. For the orbit parabola specifically, translate the origin to the vertex $x=p/2$ and set $X=p/2-x\ge0$; since $y^2=-2p(x-p/2)$, this is $y^2=2pX=4aX$, and interchanging the axes brings it to $x^2=4ay$.

In this form the vertex is at the origin, the focus is a distance $a$ from the vertex, and the directrix is a distance $a$ on the opposite side. The latus rectum through the focus is the horizontal chord at $y=a$, running from $x=-2a$ to $x=2a$, so its full length is $4a=2p$, consistent with the general conic result.

![Parabola geometry](CentralForceImage/parabola-geometry.png)

**Figure 4.** Geometry of the Kepler parabola ($e=1$). (a) The focus-centered frame of the orbit equation: the focus $F$ is at the origin, the vertex $V$ is at $x=p/2$, and the directrix is $x=p$. The semi-latus rectum $p$ runs from $F$ to the curve at $x=0$, and for the marked point $P$ the distance to the focus equals the distance to the directrix, $r=d-x$. (b) The same curve with the origin at the vertex and the axis along $y$: the focus is $(0,a)$, the directrix is $y=-a$, and the equation is $x^2=4ay$ with $a=p/2$. The full latus rectum is $4a=2p$. The figure is drawn for $p=2$, so $a=1$.

The parabola is the marginal case between bound and unbound motion. A particle on it reaches infinity with zero speed, which corresponds to $E=0$.

The motion is a single pass: the particle comes in from infinity along one arm, passes the periapsis at $\phi=0$, and recedes to infinity along the other arm. Since the denominator vanishes at $\phi=\pm\pi$, both arms approach the direction of the negative $x$-axis, so the parabola is asymptotic to a line parallel to its own axis. Unlike the hyperbola, it has no pair of distinct asymptotes and hence no scattering angle.

------

### 3.4 Hyperbola

For $e>1$ the denominator is positive only when

$$
\cos\phi>-\frac1e.
$$

Define the limiting angle

$$
\phi_\infty=\arccos\!\left(-\frac1e\right)
=\pi-\arccos\!\left(\frac1e\right),
\qquad
\frac{\pi}{2}<\phi_\infty<\pi.
$$

Then $r$ is finite on the interval $-\phi_\infty<\phi<\phi_\infty$ and diverges as $\phi\to\pm\phi_\infty$. The curve is a **hyperbola** (双曲线); its **asymptotes** (渐近线) lie in the two limiting directions $\phi=\pm\phi_\infty$. Only one branch is traced with $r>0$: the branch containing the focus, opening away from the periapsis.

There is a single apsis,

$$
r_{\min}=r(0)=\frac{p}{1+e}.
$$

#### 3.4.1 From the polar equation to the standard form

Start from $r=p-ex$ and square after writing $r=\sqrt{x^2+y^2}$:

$$
x^2+y^2=(p-ex)^2
\quad\Longrightarrow\quad
(1-e^2)x^2+y^2+2pex-p^2=0.
$$

For $e>1$ the coefficient $1-e^2$ is negative, so multiply by $-1$:

$$
(e^2-1)x^2-y^2-2pex+p^2=0.
$$

Complete the square in $x$. The center sits at

$$
x_C=\frac{pe}{e^2-1},
$$

and

$$
(e^2-1)(x-x_C)^2-y^2
=-p^2+(e^2-1)x_C^2
=\frac{p^2}{e^2-1}.
$$

Dividing through gives

$$
\frac{(x-x_C)^2}{a^2}-\frac{y^2}{b^2}=1,
\qquad
a=\frac{p}{e^2-1},
\qquad
b=\frac{p}{\sqrt{e^2-1}}.
$$

Since $a=p/(e^2-1)$, we have $x_C=ae$: the center is at $x=ae$. The vertices are at $x=x_C\pm a$; the one on the side of the focus is

$$
x_C-a=ae-a=\frac{p}{e^2-1}(e-1)=\frac{p}{1+e}=r_{\min},
$$

so the branch with $r>0$ is the left branch $x\le a(e-1)=p/(1+e)$. The focus of this branch is the origin, because the distance from the center to the origin is

$$
c\equiv x_C=ae,
$$

and the second focus is symmetric about the center, at $x=2ae$. The parameters of the hyperbola are therefore

$$
\boxed{a=\frac{p}{e^2-1},
\qquad
b=\frac{p}{\sqrt{e^2-1}},
\qquad
c=ae.}
$$

For large $|x-x_C|$ the term $y^2/b^2$ must balance $(x-x_C)^2/a^2$, so the curve approaches the two lines

$$
y=\pm\frac{b}{a}(x-x_C).
$$

Finally,

$$
c^2=a^2e^2=a^2+a^2(e^2-1)=a^2+b^2,
$$

which is the hyperbola counterpart of $b^2+c^2=a^2$ for the ellipse.

Here $a$ is the **transverse semiaxis** (实半轴) and $b$ the **conjugate semiaxis** (虚半轴); the eccentricity is $e=c/a$.

The vertex of the physical branch is at $x=r_{\min}=p/(1+e)$, while the center is at $x=ae$. The second branch, at $x\ge a(e+1)$, is not reached by a particle that comes in from infinity, passes periapsis, and escapes; it corresponds to negative $r$ in the polar representation.

![Hyperbola geometry](CentralForceImage/hyperbola-geometry.png)

**Figure 5.** Geometry of the Kepler hyperbola ($e>1$). (a) The focus-centered frame: the force center is the focus $F$ at the origin, the physical branch ($r>0$) is the solid curve, and the second branch is dashed. The center $C$ is at $x=ae$, and the vertex $V$ at $x=p/(1+e)$ is the periapsis. The asymptotes make angles $\pm\phi_\infty$ with the axis, and the dashed segment from the point $L$ on the latus rectum to the directrix $x=d$ verifies $r=e(d-x)$; the arrows show the incoming and outgoing directions of a scattered particle. (b) The same curve with the origin at the center: both branches, the fundamental rectangle, the transverse semiaxis $a$, the conjugate semiaxis $b$, the focal distance $c$, and the semi-latus rectum $p$ through the left focus. The standard form is $X^2/a^2-Y^2/b^2=1$ with $c^2=a^2+b^2$. The figure is drawn for $e=1.5$ and $p=2$, so $a=1.6$, $b\approx1.789$, $c=2.4$, $d\approx1.333$, and $r_{\min}=0.8$.

> **Scattering.** The repulsive Coulomb orbit is the branch of this hyperbola with the force center at the focus. The particle comes from infinity, reaches $r_{\min}$, and recedes along the other asymptote. The angle between the asymptotes determines the scattering angle; see Section 8 of the central-force chapter.

------

## 4. Cartesian Forms and Standard Parameters

To obtain the standard Cartesian equations, start from $r=p-ex$ and write $r=\sqrt{x^2+y^2}$:

$$
\sqrt{x^2+y^2}=p-ex.
$$

Squaring gives the single equation

$$
(1-e^2)x^2+y^2+2pex-p^2=0,
$$

which contains all four cases. Completing the square differs according to the sign of $1-e^2$.

**Circle, $e=0$.** The equation reduces to

$$
x^2+y^2=p^2.
$$

**Ellipse, $0<e<1$.** Since $1-e^2>0$, complete the square in $x$:

$$
(1-e^2)\left(x+\frac{pe}{1-e^2}\right)^2+y^2
=\frac{p^2}{1-e^2}.
$$

Dividing through,

$$
\frac{(x+ae)^2}{a^2}+\frac{y^2}{b^2}=1,
\qquad
a=\frac{p}{1-e^2},
\quad
b=\frac{p}{\sqrt{1-e^2}}.
$$

The center is at $x=-ae$, as expected.

**Parabola, $e=1$.** The quadratic term in $x$ disappears:

$$
y^2+2px-p^2=0
\quad\Longrightarrow\quad
y^2=-2p\left(x-\frac{p}{2}\right).
$$

This is a parabola with vertex at $x=p/2$, focus at the origin, and directrix $x=p$.

**Hyperbola, $e>1$.** Now $e^2-1>0$. Multiplying by $-1$ and completing the square, as in Section 3.4,

$$
\frac{(x-ae)^2}{a^2}-\frac{y^2}{b^2}=1,
\qquad
a=\frac{p}{e^2-1},
\quad
b=\frac{p}{\sqrt{e^2-1}}.
$$

The center is at $x=ae$, and the branch containing the focus is the left branch $x\le a(e-1)=p/(e+1)$.

The table collects the geometric parameters.

| $e$ | Conic | $r_{\min}$ | $r_{\max}$ | $a$ | $b$ |
|---|---|---|---|---|---|
| $0$ | circle | $p$ | $p$ | $p$ | $p$ |
| $0<e<1$ | ellipse | $\dfrac{p}{1+e}$ | $\dfrac{p}{1-e}$ | $\dfrac{p}{1-e^2}$ | $\dfrac{p}{\sqrt{1-e^2}}$ |
| $1$ | parabola | $\dfrac{p}{2}$ | $\infty$ | — | — |
| $e>1$ | hyperbola | $\dfrac{p}{1+e}$ | $\infty$ | $\dfrac{p}{e^2-1}$ | $\dfrac{p}{\sqrt{e^2-1}}$ |

------

## 5. Eccentricity and Energy

Evaluating the energy at periapsis in the central-force chapter gives

$$
E=\frac{mk^2}{2\ell^2}\left(e^2-1\right).
$$

Using $p=\ell^2/(mk)$, this becomes

$$
\boxed{E=\frac{k}{2p}\left(e^2-1\right).}
$$

Since $k>0$ and $p>0$, the sign of the energy is the sign of $e^2-1$:

| Eccentricity | Energy | Conic | Motion |
|---|---|---|---|
| $e=0$ | $E=-\dfrac{k}{2p}$ | circle | bound |
| $0<e<1$ | $E<0$ | ellipse | bound |
| $e=1$ | $E=0$ | parabola | marginal |
| $e>1$ | $E>0$ | hyperbola | unbound |

For the ellipse, $p/a=1-e^2$, so

$$
E=-\frac{k}{2a},
$$

which is the energy–semimajor-axis relation derived in Section 6.3 of the central-force chapter. For the hyperbola, $p/a=e^2-1$, so

$$
E=+\frac{k}{2a}.
$$

If $a$ is allowed to be signed — positive for the ellipse and negative for the hyperbola, $a=-p/(e^2-1)$ — both cases collapse to the single relation

$$
E=-\frac{k}{2a}.
$$

For fixed $\ell$, $p$ is fixed and the circular orbit has the minimum energy $E=-k/(2p)$. Raising the energy increases $e$; the conic changes from ellipse to parabola to hyperbola as $E$ passes through zero.

------

## 6. Summary

The Kepler orbit equation

$$
\boxed{r(\theta)=\frac{p}{1+e\cos(\theta-\theta')},
\qquad
p=\frac{\ell^2}{mk}.}
$$

is the polar equation of a conic with one focus at the force center. The parameter $p$ sets the scale and $e$ sets the shape:

- **Circle** ($e=0$): $r=p$ for all angles; center at the focus; minimum energy for given $\ell$.
- **Ellipse** ($0<e<1$): bounded orbit with $r_{\min}=p/(1+e)$ and $r_{\max}=p/(1-e)$; $a=p/(1-e^2)$, $b=p/\sqrt{1-e^2}$, $c=ae$.
- **Parabola** ($e=1$): $r=p/(1+\cos\phi)$; one apsis at $r=p/2$; $E=0$; escapes to infinity with zero speed.
- **Hyperbola** ($e>1$): one apsis at $r=p/(1+e)$; asymptotes at $\phi=\pm\arccos(-1/e)$; $E>0$; unbound.

The eccentricity and the energy are related by

$$
\boxed{E=\frac{k}{2p}\left(e^2-1\right)},
$$

so $E<0$, $E=0$, and $E>0$ correspond respectively to $e<1$, $e=1$, and $e>1$.
