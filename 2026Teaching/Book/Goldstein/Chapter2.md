2

# Variational Principles and Lagrange’s Equations

## 2.1 HAMILTON’S PRINCIPLE

The derivation of Lagrange’s equations presented in Chapter 1 started from a consideration of the instantaneous state of the system and small virtua displacements about the instantaneous state, i.e., from a “differential principle” such as D’Alembert’s principle. It is also possible to obtain Lagrange’s equations from a principle that considers the entire motion of the system between times $t _ { 1 }$ and $t _ { 2 } ,$ and small virtual variations of this motion from the actual motion. A principle of this nature is known as an “integral principle.”

Before presenting the integral principle, the meaning attached to the phrase “motion of the system between times $t _ { 1 }$ and $t _ { 2 } ^ { \prime \prime }$ must first be stated in more precise language. The instantaneous configuration of a system is described by the values of the n generalized coordinates $q _ { 1 } , \ldots , q _ { n }$ , and corresponds to a particula point in a Cartesian hyperspace where the $q ^ { * } { \bf s }$ form the n coordinate axes. This n-dimensional space is therefore known as configuration space. As time goes on, the state of the system changes and the system point moves in configuration space tracing out a curve, described as “the path of motion of the system.” The “motion of the system,” as used above, then refers to the motion of the system point along this path in configuration space. Time can be considered formally as a parameter of the curve; to each point on the path there is associated one or more values of the time. Note that configuration space has no necessary connection with the physical three-dimensional space, just as the generalized coordinates are not necessarily position coordinates. The path of motion in configuration space has no resemblance to the path in space of any actual particle; each poin on the path represents the entire system configuration at some given instan of time.

The integral Hamilton’s principle describes the motion of those mechanica systems for which all forces (except the forces of constraint) are derivable from a generalized scalar potential that may be a function of the coordinates, velocities, and time. Such systems will be denoted as monogenic. Where the potential is an explicit function of position coordinates only, then a monogenic system is also conservative (cf. Section 1.2).

For monogenic systems, Hamilton’s principle can be stated as

The motion of the system from time $t _ { 1 }$ to time $t _ { 2 }$ is such that the line integral (called the action or the action integral),

## 2.1 Hamilton’s Principle

$$
I = \int_ {t _ {1}} ^ {t _ {2}} L d t,\tag{2.1}
$$

where $L = T - V$ , has a stationary value for the actual path of the motion.

That is, out of all possible paths by which the system point could travel from its position at time $t _ { 1 }$ to its position at time $t _ { 2 }$ , it will actually travel along that path for which the value of the integral (2.1) is stationary. By the term “station ary value” for a line integral, we mean that the integral along the given path has the same value to within first-order infinitesimals as that along all neighboring paths (i.e., those that differ from it by infinitesimal displacements). (Cf. Fig. 2.1.) The notion of a stationary value for a line integral thus corresponds in ordinary function theory to the vanishing of the first derivative.

We can summarize Hamilton’s principle by saying that the motion is such that the variation of the line integral I for fixed $t _ { 1 }$ and $t _ { 2 }$ is zero:

$$
\delta I = \delta \int_ {t _ {1}} ^ {t _ {2}} L (q _ {1}, \dots , q _ {n}, \dot {q} _ {1}, \dots , \dot {q} _ {n}, t) d t = 0.\tag{2.2}
$$

Where the system constraints are holonomic, Hamilton’s principle, Eq. (2.2), is both a necessary and sufficient condition for Lagrange’s equations, Eqs. (1.57). Thus, it can be shown that Hamilton’s principle follows directly from Lagrange’s equations. Instead, however, we shall prove the converse, namely, that Lagrange’s equations follow from Hamilton’s principle, as being the more important theorem. That Hamilton’s principle is a sufficient condition for deriving the equations of motion enables us to construct the mechanics of monogenic systems from Hamil ton’s principle as the basic postulate rather than Newton’s laws of motion. Such a formulation has advantages; e.g., since the integral I is obviously invariant to the system of generalized coordinates used to express $L$ , the equations of motion must always have the Lagrangian form no matter how the generalized coordinates are transformed. More important, the formulation in terms of a variational prin ciple is the route that is generally followed when we try to describe apparently nonmechanical systems in the mathematical clothes of classical mechanics, as in the theory of fields.

![](images/9ec63c06647b4c3ae8a8954c3864e1683793dc1ba1ec4960a38e1459601a70d3.jpg)  
FIGURE 2.1 Path of the system point in configuration space.

## 2.2 SOME TECHNIQUES OF THE CALCULUS OF VARIATIONS

Before demonstrating that Lagrange’s equations do follow from (2.2), we must first examine the methods of the calculus of variations, for a chief problem of this calculus is to find the curve for which some given line integral has a stationary value. (See website for necessary comments.)

Consider first the problem in an essentially one-dimensional form: We have a function $f ( y , { \dot { y } } , x )$ defined on a path $y = y ( x )$ between two values $x _ { 1 }$ and $x _ { 2 }$ where $\dot { y }$ is the derivative of $y$ with respect to x. We wish to find a particular path $y ( x )$ such that the line integral J of the function $f$ between $x _ { 1 }$ and $x _ { 2 }$

$$
\begin{array}{l} \dot {y} \equiv \frac {d y}{d x}, \\ J = \int_ {x _ {1}} ^ {x _ {2}} f (y, \dot {y}, x) d x, \end{array}\tag{2.3}
$$

has a stationary value relative to paths differing infinitesimally from the correc function $y ( x )$ . The variable x here plays the role of the parameter t, and we consider only such varied paths for which $y ( x _ { 1 } ) = y _ { 1 } , y ( x _ { 2 } ) = y _ { 2 }$ . (Cf. Fig. 2.2.) Note that Fig. 2.2 does not represent configuration space. In the one-dimensiona configuration space, both the correct and varied paths are the segment of the straight line connecting $y _ { 1 }$ and $y _ { 2 } ;$ the paths differ only in the functional rela tion between $y$ and x. The problem is one-dimensional, y is not a coordinate, it is a function of x.

![](images/85c00a16ff9531015d5af3e5d96e4481766b43c604a0203f9993046487e45183.jpg)  
FIGURE 2.2 Varied paths of the function of $y ( x )$ in the one-dimensional extremum problem.

## 2.2 Some Techniques of the Calculus of Variations

We put the problem in a form that enables us to use the familiar apparatus of the differential calculus for finding the stationary points of a function. Since J must have a stationary value for the correct path relative to any neighboring path, the variation must be zero relative to some particular set of neighboring paths labeled by an infinitesimal parameter $\alpha .$ . Such a set of paths might be denoted by $y ( x , \alpha )$ , with $y ( x , 0 )$ representing the correct path. For example, if we select any function $\eta ( x )$ that vanishes at $x = x _ { 1 }$ and $x = x _ { 2 }$ , then a possible set of varied paths is given by

$$
y (x, \alpha) = y (x, 0) + \alpha \eta (x).\tag{2.4}
$$

For simplicity, it is assumed that both the correct path $y ( x )$ and the auxiliary function $\eta ( x )$ are well-behaved functions—continuous and nonsingular between $x _ { 1 }$ and $x _ { 2 }$ , with continuous first and second derivatives in the same interval. For any such parametric family of curves, J in Eq. (2.3) is also a function of α:

$$
J (\alpha) = \int_ {x _ {1}} ^ {x _ {2}} f (y (x, \alpha), \dot {y} (x, \alpha), x) d x,\tag{2.5}
$$

and the condition for obtaining a stationary point is the familiar one tha

$$
\left(\frac {d J}{d \alpha}\right) _ {\alpha = 0} = 0.\tag{2.6}
$$

By the usual methods of differentiating under the integral sign, we find that

$$
\frac {d J}{d \alpha} = \int_ {x _ {1}} ^ {x _ {2}} \left(\frac {\partial f}{\partial y} \frac {\partial y}{\partial \alpha} + \frac {\partial f}{\partial \dot {y}} \frac {\partial \dot {y}}{\partial \alpha}\right) d x.\tag{2.7}
$$

Consider the second of these integrals:

$$
\int_ {x _ {1}} ^ {x _ {2}} \frac {\partial f}{\partial \dot {y}} \frac {\partial \dot {y}}{\partial \alpha} d x = \int_ {x _ {1}} ^ {x _ {2}} \frac {\partial f}{\partial \dot {y}} \frac {\partial^ {2} y}{\partial x \partial \alpha} d x.
$$

Integrating by parts, the integral becomes

$$
\int_ {x _ {1}} ^ {x _ {2}} \frac {\partial f}{\partial \dot {y}} \frac {\partial^ {2} y}{\partial x \partial \alpha} d x = \left. \frac {\partial f}{\partial \dot {y}} \frac {\partial y}{\partial \alpha} \right| _ {x _ {1}} ^ {x _ {2}} - \int_ {x _ {1}} ^ {x _ {2}} \frac {d}{d x} \left(\frac {\partial f}{\partial \dot {y}}\right) \frac {\partial y}{\partial \alpha} d x.\tag{2.8}
$$

The conditions on all the varied curves are that they pass through the point $( x _ { 1 } , y _ { 1 } ) , ( x _ { 2 } , y _ { 2 } )$ , and hence the partial derivative of $y$ with respect to α at $x _ { 1 }$ and $x _ { 2 }$ must vanish. Therefore, the first term of (2.8) vanishes and $\operatorname { E q }$ . (2.7) reduces to

$$
\frac {d J}{d \alpha} = \int_ {x _ {1}} ^ {x _ {2}} \left(\frac {\partial f}{\partial y} - \frac {d}{d x} \frac {\partial f}{\partial \dot {y}}\right) \frac {\partial y}{\partial \alpha} d x.
$$

The condition for a stationary value, Eq. (2.6), is therefore equivalent to the equa tion

Chapter 2 Variational Principles and Lagrange’s Equation

$$
\int_ {x _ {1}} ^ {x _ {2}} \left(\frac {\partial f}{\partial y} - \frac {d}{d x} \frac {\partial f}{\partial \dot {y}}\right) \left(\frac {\partial y}{\partial \alpha}\right) _ {0} d x = 0.\tag{2.9}
$$

Now, the partial derivative of y with respect to $\alpha$ occurring in Eq. (2.9) is a function of x that is arbitrary except for continuity and end point conditions. Fo example, for the particular parametric family of varied paths given by Eq. (2.4), it is the arbitrary function $\eta ( x )$ . We can therefore apply to Eq (2.9) the so-called “fundamental lemma” of the calculus of variations, which says if

$$
\int_ {x _ {1}} ^ {x _ {2}} M (x) \eta (x) d x = 0\tag{2.10}
$$

for all arbitrary functions $\eta ( x )$ continuous through the second derivative, then $M ( x )$ must identically vanish in the interval $( x _ { 1 } , x _ { 2 } )$ . While a formal mathematical proof of the lemma can be found in texts on the calculus of variations, the validity of the lemma is easily seen intuitively. We can imagine constructing a function $\eta$ that is positive in the immediate vicinity of any chosen point in the interval and zero everywhere else. Equation (2.10) can then hold only if M(x) vanishes at that (arbitrarily) chosen point, which shows M must be zero throughout the interval. From Eq. (2.9) and the fundamental lemma, it therefore follows that J can have a stationary value only if

$$
\frac {\partial f}{\partial y} - \frac {d}{d x} \left(\frac {\partial f}{\partial \dot {y}}\right) = 0.\tag{2.11}
$$

The differential quantity,

$$
\left(\frac {\partial y}{\partial \alpha}\right) _ {0} d \alpha \equiv \delta y,\tag{2.12}
$$

represents the infinitesimal departure of the varied path from the correct path $y ( x )$ at the point x and thus corresponds to the virtual displacement introduced in Chapter 1 (hence the notation δy). Similarly, the infinitesimal variation of J abou the correct path can be designated

$$
\left(\frac {d J}{d \alpha}\right) _ {0} d \alpha \equiv \delta J.\tag{2.13}
$$

The assertion that J is stationary for the correct path can thus be written

$$
\delta J = \int_ {x _ {1}} ^ {x _ {2}} \left(\frac {\partial f}{\partial y} - \frac {d}{d x} \frac {\partial f}{\partial \dot {y}}\right) \delta y d x = 0,
$$

requiring that $y ( x )$ satisfy the differential equation (2.11). The δ-notation, intro duced through Eqs. (2.12) and (2.13), may be used as a convenient shorthand for treating the variation of integrals, remembering always that it stands for the manipulation of parametric families of varied paths such as Eq. (2.4).

Some simple examples of the application of Eq. (2.11) (which clearly resembles a Lagrange equation) may now be considered:

1. Shortest distance between two points in a plane. An element of length in a plane is

$$
d s = \sqrt {d x ^ {2} + d y ^ {2}}
$$

and the total length of any curve going between points 1 and 2 is

$$
I = \int_ {1} ^ {2} d s = \int_ {x _ {1}} ^ {x _ {2}} \sqrt {1 + \left(\frac {d y}{d x}\right) ^ {2}} d x.
$$

The condition that the curve be the shortest path is that I be a minimum. This is an example of the extremum problem as expressed by Eq. (2.3), with

$$
f = \sqrt {1 + \dot {y} ^ {2}}.
$$

Substituting in (2.11) with

$$
\frac {\partial f}{\partial y} = 0, \quad \frac {\partial f}{\partial \dot {y}} = \frac {\dot {y}}{\sqrt {1 + \dot {y} ^ {2}}},
$$

we have

$$
\frac {d}{d x} \left(\frac {\dot {y}}{\sqrt {1 + \dot {y} ^ {2}}}\right) = 0
$$

or

$$
\frac {\dot {y}}{\sqrt {1 + \dot {y} ^ {2}}} = c,
$$

where $c$ is constant. This solution can be valid only if

$$
\dot {y} = a,
$$

where $a$ is a constant related to $c$ by

$$
a = \frac {c}{\sqrt {1 - c ^ {2}}}.
$$

But this is clearly the equation of a straight line,

$$
y = a x + b,
$$

where b is another constant of integration. Strictly speaking, the straight line has only been proved to be an extremum path, but for this problem it is obviously also a minimum. The constants of integration, a and $^ { b , }$ are determined by the condition that the curve pass through the two end points, $( x _ { 1 } , y _ { 1 } ) , ( x _ { 2 } , y _ { 2 } )$

In a similar fashion we can obtain the shortest distance between two points on a sphere, by setting up the arc length on the surface of the sphere in terms of the angle coordinates of position on the sphere. In general, curves that give the shortest distance between two points on a given surface are called the geodesics of the surface. (See website about part 2 below.)

2. Minimum surface of revolution. Suppose we form a surface of revolution by taking some curve passing between two fixed end points $( x _ { 1 } , y _ { 1 } )$ ) and $( x _ { 2 } , y _ { 2 } )$ defining the xy plane, and revolving it about the y axis (cf. Fig. 2.3a). The problem then is to find that curve for which the surface area is a minimum. The area of a strip of the surface is 2πx $d s = 2 \pi x \sqrt { 1 + \dot { y } ^ { 2 } }$ dx, and the total area is

$$
2 \pi \int_ {1} ^ {2} x \sqrt {1 + \dot {y} ^ {2}} d x.
$$

The extremum of this integral is again given by (2.11) where

$$
f = x \sqrt {1 + \dot {y} ^ {2}}
$$

and

$$
{\frac {\partial f}{\partial y}} = 0, \qquad {\frac {\partial f}{\partial {\dot {y}}}} = {\frac {x {\dot {y}}}{\sqrt {1 + {\dot {y}} ^ {2}}}}.
$$

Equation (2.11) becomes in this case

![](images/8c2bd3d667d262f02bf9ba0bfba35ecc92c27b7f79f8dfcef0d286cb86306cfd.jpg)  
FIGURE 2.3a Minimum surface of revolution. Note that this figure is drawn for $y _ { 1 }$ and $y _ { 2 }$ having the same sign relative to the rotation axis. This is not assumed in the genera solution.

2.2 Some Techniques of the Calculus of Variations

$$
{\frac {d}{d x}} \left({\frac {x {\dot {y}}}{\sqrt {1 + {\dot {y}} ^ {2}}}}\right) = 0
$$

or

$$
\frac {x \dot {y}}{\sqrt {1 + \dot {y} ^ {2}}} = a,
$$

where $a$ is some constant of integration clearly smaller than the minimum value of x. Squaring the above equation and factoring terms, we have

$$
\dot {y} ^ {2} (x ^ {2} - a ^ {2}) = a ^ {2},
$$

or solving,

$$
{\frac {d y}{d x}} = {\frac {a}{\sqrt {x ^ {2} - a ^ {2}}}}.
$$

The general solution of this differential equation, in light of the nature of $^ { a , }$ , is

$$
y = a \int {\frac {d x}{\sqrt {x ^ {2} - a ^ {2}}}} + b = a \operatorname{arc} \cosh {\frac {x}{a}} + b
$$

or

$$
x = a \cosh {\frac {y - b}{a}},
$$

which is the equation of a catenary. Again the two constants of integration, $a$ and $^ { b , }$ are determined in principle by the requirements that the curve pass through the two given end points, as shown in Fig. 2.3b.

Curves satisfying the preceding equation all scale as $x / a$ and $y / a$ with one independent parameter $b / a$ . This suggests that when the solutions are examined in detail they turn out to be a great deal more complicated than these considerations suggest. For some pairs of end points, unique constants of integration a and b can be found. But for other end points, it is possible to draw two different catenary curves through the end points, while for additional cases no possible values can be found for $a$ and $b .$ . Further, recall that Eq. (2.11) represents a condition for finding curves $y ( x )$ continuous through the second derivative that render the integral stationary. The catenary solutions therefore do not always represent minimum values, but may represent “inflection points” where the length of the curve is stationary but not minimum.

![](images/0bc76232dab8ac7cb7b7b44a0546f0c3940575d81469c5c787fabac00c5d54ae.jpg)  
FIGURE 2.3b General catenary solution for minimum surface of revolution.

For certain combinations of end points (an example is $x _ { 1 }$ and $x _ { 2 }$ both positive and both much smaller than $y _ { 2 } \mathrm { ~ - ~ } y _ { 1 } )$ , the absolute minimum in the sur face of revolution is provided (cf. Exercise 8) by a curve composed of straigh line segments—from the first end point parallel to the x axis until the y axis is reached, then along the y axis until the point $( 0 , y _ { 2 } )$ and then out in a straigh line to the second end point corresponding to the area $\pi ( x _ { 1 } ^ { 2 } + x _ { 2 } ^ { 2 } )$ . This curve results when $a = 0$ , forcing either x = 0 or y = constant. Since this curve has discontinuous first derivatives, we should not expect to find it as a solution to Eq. (2.11).

This example is valuable in emphasizing the restrictions that surround the derivation and the meaning of the stationary condition. Exercises 7 and 8 examine the conditions for the pathological behavior for a symmetric example. More information can be found in many texts on the calculus of variations.

3. The brachistochrone problem. (See Fig. 2.4a.) This well-known problem is to find the curve joining two points, along which a particle falling from res under the influence of gravity travels from the higher to the lower point in the least time.

If v is the speed along the curve, then the time required to fall an arc length d is $d s / v$ , and the problem is to find a minimum of the integral

$$
t _ {1 2} = \int_ {1} ^ {2} \frac {d s}{v}.
$$

![](images/457404bfb068f4f11094b8b9a2c30697afec5459d4d68043b5f1fdf1632f9f64.jpg)  
FIGURE 2.4a The brachistochrone problem.

## 2.2 Some Techniques of the Calculus of Variations

If y is measured down from the initial point of release, the conservation theorem for the energy of the particle can be written as

$$
\frac {1}{2} m v ^ {2} = m g y
$$

or

$$
v = \sqrt {2 g y}.
$$

Then the expression for $t _ { 1 2 }$ becomes

$$
t _ {1 2} = \int_ {1} ^ {2} \frac {\sqrt {1 + \dot {y} ^ {2}}}{\sqrt {2 g y}} d x,
$$

and f is identified as

$$
f = \sqrt {\frac {1 + \dot {y} ^ {2}}{2 g y}}.
$$

The integration of Eq. (2.11) with this form for f is straightforward and is left a an exercise.

The parametric solution in terms of its one parameter, a, given by

$$
x = a (\phi - \sin \phi), y = a (1 - \cos \phi),
$$

is sketched in Fig. 2.4b for the first cycle $( 0 \leq x \leq 2 \pi a )$ and the beginning of the second cycle. Three cases of solutions are indicated. A power-series expansion of the solution for the limit $y \ll a$ gives

$$
y = a \sqrt [ 3 ]{\frac {9}{2} (x / a) ^ {2}}.
$$

The brachistochrone problem is famous in the history of mathematics, for it was the analysis of this problem by John Bernoulli that led to the formal foundation of the calculus of variations.

![](images/85fd4726516c59b33502545d47f49d55800a34679e2097210b4c9edf7df922e9.jpg)  
FIGURE 2.4b Cycloid solution to the brachistochrone problem showing positions on the curve for the three cases x $\ll y _ { 2 } , x _ { 2 } = { \frac { \pi } { 2 } } y _ { 2 }$ , and $x _ { 2 } \gg y _ { 2 }$

## 2.3 DERIVATION OF LAGRANGE’S EQUATIONS FROM HAMILTON’S PRINCIPLE

The fundamental problem of the calculus of variations is easily generalized to the case where $f$ is a function of many independent variables $y _ { i }$ , and their derivatives $\dot { y } _ { i }$ . (Of course, all these quantities are considered as functions of the parametric variable x.) Then a variation of the integral J,

$$
\delta J = \delta \int_ {1} ^ {2} f (y _ {1} (x); y _ {2} (x), \dots , \dot {y} _ {1} (x); \dot {y} _ {2} (x), \dots , x) d x,\tag{2.14}
$$

is obtained, as before, by considering J as a function of parameter α that labels a possible set of curves $y _ { 1 } ( x , \alpha )$ . Thus, we may introduce α by setting

$$
\begin{array}{c} y _ {1} (x, \alpha) = y _ {1} (x, 0) + \alpha \eta_ {1} (x), \\ y _ {2} (x, \alpha) = y _ {2} (x, 0) + \alpha \eta_ {2} (x), \\ \vdots \qquad \qquad \vdots \qquad \qquad \vdots \end{array}\tag{2.15}
$$

where $y _ { 1 } ( x , 0 ) , y _ { 2 } ( x , 0 )$ , etc., are the solutions of the extremum problem (to be obtained) and $\eta _ { 1 } , \eta _ { 2 }$ , etc., are independent functions of x that vanish at the end points and that are continuous through the second derivative, but otherwise are completely arbitrary.

The calculation proceeds as before. The variation of J is given in terms of

$$
\frac {\partial J}{\partial \alpha} d \alpha = \int_ {1} ^ {2} \sum_ {i} \left(\frac {\partial f}{\partial y _ {i}} \frac {\partial y _ {i}}{\partial \alpha} d \alpha + \frac {\partial f}{\partial \dot {y} _ {i}} \frac {\partial \dot {y} _ {i}}{\partial \alpha} d \alpha\right) d x.\tag{2.16}
$$

Again we integrate by parts the integral involved in the second sum of Eq. (2.16):

$$
\int_ {1} ^ {2} \frac {\delta f}{\partial \dot {y} _ {i}} \frac {\partial^ {2} y _ {i}}{\partial \alpha \partial x} d x = \left. \frac {\partial f}{\partial \dot {y} _ {i}} \frac {\partial y _ {i}}{\partial \alpha} \right| _ {1} ^ {2} - \int_ {1} ^ {2} \frac {\partial y _ {i}}{\partial \alpha} \frac {d}{d x} \left(\frac {\partial f}{\partial \dot {y} _ {i}}\right) d x,
$$

where the first term vanishes because all curves pass through the fixed end points. Substituting in (2.16), δ J becomes

$$
\delta J = \int_ {1} ^ {2} \sum_ {i} \left(\frac {\partial f}{\partial y _ {i}} - \frac {d}{d x} \frac {\partial f}{\partial \dot {y} _ {i}}\right) \delta y _ {i} d x,\tag{2.17}
$$

where, in analogy with (2.12), the variation $\delta y _ { i }$ is

$$
\delta y _ {i} = \left(\frac {\partial y _ {i}}{\partial \alpha}\right) _ {0} d \alpha .
$$

Since the y variables are independent, the variations $\delta y _ { i }$ are independen $( \mathrm { e . g . }$ the functions $\eta _ { i } ( x )$ will be independent of each other). Hence, by an obvious extension of the fundamental lemma (cf. Eq. (2.10)), the condition that δ J is zero

## 2.4 Extending Hamilton’s Principle to Systems with Constraint

requires that the coefficients of the $\delta y _ { i }$ separately vanish:

$$
\frac {\partial f}{\partial y _ {i}} - \frac {d}{d x} \frac {\partial f}{\partial \dot {y} _ {i}} = 0, \qquad i = 1, 2, \ldots , n.\tag{2.18}
$$

Equations (2.18) represent the appropriate generalization of (2.11) to several variables and are known as the Euler-Lagrange differential equations. Their solutions represent curves for which the variation of an integral of the form given in (2.14) vanishes. Further generalizations of the fundamental variational prob lem are easily possible. Thus, we can take $f$ as a function of higher derivatives ${ \ddot { y } } , { \overset { \underset { \mathrm { ~ . ~ . ~ } } { \mathrm { ~ y ~ } } } { \mathrm { ~ . ~ } } }$ , etc., leading to equations different from (2.18). Or we can extend it to cases where there are several parameters $x _ { j }$ and the integral is then multiple, with $f$ also involving as variables derivatives of $y _ { i }$ with respect to each of the parameters $x _ { j }$ . Finally, it is possible to consider variations in which the end points are not held fixed.

For present purposes, what we have derived here suffices, for the integral in Hamilton’s principle,

$$
I = \int_ {1} ^ {2} L (q _ {i}, \dot {q} _ {i}, t) d t,\tag{2.19}
$$

has just the form stipulated in (2.14) with the transformation

$$
\begin{array}{c} x \to t \\ y _ {i} \to q _ {i} \\ f (y _ {i}, \dot {y} _ {i}, x) \to L (q _ {i}, \dot {q} _ {i}, t). \end{array}
$$

In deriving Eqs. (2.18), we assumed that the $y _ { i }$ variables are independent. The corresponding condition in connection with Hamilton’s principle is that the gen eralized coordinates $q _ { i }$ be independent, which requires that the constraints be holonomic. The Euler-Lagrange equations corresponding to the integral I then become the Lagrange equations of motion,

$$
\frac {d}{d t} \frac {\partial L}{\partial \dot {q} _ {i}} - \frac {\partial L}{\partial q _ {i}} = 0, \quad i = 1, 2, \dots , n,
$$

and we have accomplished our original aim, to show that Lagrange’s equa tions follow from Hamilton’s principle—for monogenic systems with holonomic constraints.

## 2.4 EXTENDING HAMILTON’S PRINCIPLE TO SYSTEMS WITH CONSTRAINTS

In Section 1.3 we solved problems with holonomic constraints by choosing coordinates such that the constraint equations (1.37) become a trivial $0 = 0$ set of equations. In this section we show that Hamilton’s principle can be used to solve systems with holonomic constraints as well as certain types of non-holonomic systems.

First consider holonomic constraints. When we derive Lagrange’s equations from either Hamilton’s or D’Alembert’s principle, the holonomic constraints appear in the last step when the variations in the $q _ { i }$ were considered independen of each other. However, the virtual displacements in the $\delta q _ { I } \mathrm { \ ' } { \mathrm { s } }$ may not be consis tent with the constraints. If there are n variables and m constraint equations $f _ { \alpha }$ of the form of Eq. (1.37), the extra virtual displacements are eliminated by the method of Lagrange undetermined multipliers.

We modify the integral in Eq. (2.19) to be

$$
I = \int_ {1} ^ {2} \left(L + \sum_ {\alpha = 1} ^ {m} \lambda_ {\alpha} f _ {a}\right) d t,\tag{2.20}
$$

and allow the $q _ { \alpha }$ and the $\lambda _ { \alpha }$ to vary independently to obtain $n + m$ equations. The variations of the $\lambda _ { \alpha } { ^ { \mathbf { \beta } } } \mathbf { s }$ give the m constraint equations. The variations of the $q _ { i } \mathrm { \dag } \mathrm { s }$ give

$$
\delta I = \int_ {1} ^ {2} d t \left(\sum_ {i = 1} ^ {n} \left(\frac {d}{d t} \frac {\partial L}{\partial \dot {q} _ {i}} - \frac {\partial L}{\partial q _ {i}} + \sum_ {\alpha = 1} ^ {m} \lambda_ {a} \frac {\partial f _ {a}}{\partial q _ {i}}\right) \delta q _ {i}\right) = 0.\tag{2.21}
$$

However, the $\delta q _ { i } \mathbf { \dot { s } }$ are not independent. We choose the $\lambda _ { \alpha } \mathbf { \bar { s } }$ so that m of the equations are satisfied for arbitrary $\delta { q } _ { i }$ , and then choose the variations of the $\delta \boldsymbol { q } _ { i }$ in the remaining $n - m$ equations independently. Thus we obtain m equations o the form

$$
\frac {d}{d t} \frac {\partial L}{\partial \dot {q} _ {k}} - \frac {\partial L}{\partial q _ {k}} + \sum_ {\alpha = 1} ^ {m} \lambda_ {a} \frac {\partial f _ {a}}{\partial q _ {k}} = 0,\tag{2.22}
$$

for $k = 1 , \ldots , m$ . The equality follows from the choice of the $\lambda _ { \alpha }  { \mathrm { ~  ~ \cdot ~ } } _ { \bf s }$ . We also have the same expressions as Eq. (2.22) for $k = m + 1 , \ldots , n$ , where the equality follows from the virtual variations of the $\delta q _ { i } \mathbf { \ ' } _ { \mathbf { S } }$

This solves the system at the expense of introducing m functions $\lambda _ { \alpha }$ . We can understand this by considering that Eqs. (2.22), for $k = 1 , \ldots , n$ , can be written as

$$
\frac {d}{d t} \frac {\partial L}{\partial \dot {q} _ {k}} - \frac {\partial L}{\partial q _ {k}} = - \sum_ {\alpha = 1} ^ {m} \lambda_ {a} \frac {\partial f _ {a}}{\partial q _ {k}} = Q _ {k},\tag{2.23}
$$

where the $Q _ { k }$ are generalized forces. The functions, $Q _ { \kappa }$ , have the magnitudes of the forces needed to produce the individual constraints; however, since the choice of the “+” in the third term of Eq. (2.22) is arbitrary, we can mathematically determine only the magnitudes of these generalized forces. You need to understand the physics to determine their directions.

As an example, consider a smooth solid hemisphere of radius a placed with its flat side down and fastened to the Earth whose gravitational acceleration is $g .$ Place a small mass M at the top of the hemisphere with an infinitesimal displacement off center so the mass slides down without friction. Choose coordinate $x , y , z$ centered on the base of the hemisphere with z vertical and the x-z plane containing the initial motion of the mass.

Let θ be the angle from the top of the sphere to the mass. The Lagrangian is $L = { \textstyle { \frac { 1 } { 7 } } } M ( \dot { x } ^ { 2 } + \dot { y } ^ { \overline { { 2 } } } + \dot { z } ^ { 2 } ) - m g z$ . The initial conditions allow us to ignore the y coordinate, so the constraint equation is $a - { \sqrt { x ^ { 2 } + z ^ { 2 } } } = 0$ . Expressing the problem in terms of $r ^ { 2 } = x ^ { 2 } + \stackrel { . } { z } ^ { 2 }$ and $x / z = \cos \theta$ , Lagrange’s equations are $M a \dot { \theta } ^ { 2 } - M g \cos \theta + \lambda = 0 ,$ , and $M a ^ { 2 } { \ddot { \theta } } + M g a$ sin $\theta \ : = \ : 0$ . Solve the second equation and then the first to obtain

$$
\dot {\theta} ^ {2} = - \frac {2 g}{a} \cos \theta + \frac {2 g}{a} \quad \text { and } \quad \lambda = M g (3 \cos \theta - 2).
$$

So $\lambda$ is the magnitude of the force keeping the particle on the sphere and since $\lambda = 0$ when $\theta = \cos ^ { - 1 } ( \frac { 2 } { 3 } )$ , the mass leaves the sphere at that angle.

In general, nonholonomic constraints cannot be expressed by a variational principle. One of the exceptions is semi-holonomic constraints where the con straints can be written as a set of functions of the form

$$
f _ {\alpha} (q _ {1}, \ldots , q _ {n}; \dot {q} _ {1}, \ldots , \dot {q} _ {n}; t) = 0,\tag{2.24}
$$

where $\alpha = 1 , 2 , \ldots , m$ . Equation (2.24) commonly appears in the restricted form

$$
f _ {\alpha} = \sum_ {k = 1} ^ {n} a _ {a k} \dot {q} _ {k} + a _ {0} = 0,\tag{2.25}
$$

where the $f _ { \alpha }$ are a set of nonintegrable differential expressions and the $a _ { \alpha k }$ and $a _ { 0 }$ are functions of the $q _ { \iota }$ and t. In these cases, since we cannot integrate the constraints, there are more variables than equations. However, we can treat the variations in the same fashion as before by writing\*

$$
\delta \int_ {t _ {1}} ^ {t _ {2}} \left(L + \sum_ {\alpha = 1} ^ {m} \mu_ {a} f _ {a}\right) d t = 0,\tag{2.26}
$$

where the symbol $\mu$ is used to distinguish these multipliers from the holonomic Lagrange multipliers. If we assume that $\mu _ { \alpha } = \mu _ { \alpha } ( t )$ , the equations resulting from the virtual displacements are

$$
\frac {d}{d t} \frac {\partial L}{\partial \dot {q} _ {k}} - \frac {\partial L}{\partial q _ {k}} = Q _ {k} = - \sum_ {\alpha = 1} ^ {m} \mu_ {a} \frac {\partial f _ {a}}{\partial \dot {q} _ {k}},\tag{2.27}
$$

and the $\delta \mu _ { \alpha }$ give the equations of constraint (2.23). These two sets (Eq. (2.26) and (2.27)) together constitute $n + m$ equations for the $n + m$ unknowns. Hence they can be interpreted as equivalent to an $n + m$ holonomic system with generalized forces $Q _ { k }$ . The generalization to $\mu _ { \alpha } = \mu _ { \alpha } ( q _ { 1 } , \dots , q _ { n } ; { \dot { q } } _ { 1 } , \dots , { \dot { q } } _ { n } ; t )$ is straightforward.

As an example, consider a particle with the Lagrangian

$$
L = \frac {1}{2} m (\dot {x} ^ {2} + \dot {y} ^ {2} + \dot {z} ^ {2}) - V (x, y, z)\tag{2.28}
$$

subject to the nonholonomic constraint

$$
f (x, \dot {x}, y, \dot {y}, z) = \dot {x} y ^ {2} + x \dot {y} + k z = 0,\tag{2.29}
$$

with k a constant. The resulting equations of motion are

$$
m \ddot {x} + \mu y ^ {2} - \frac {\partial V}{\partial x} = 0,\tag{2.30a}
$$

$$
m \ddot {y} + \mu x - \frac {\partial V}{\partial y} = 0,\tag{2.30b}
$$

and

$$
m \ddot {z} - \frac {\partial V}{\partial z} = 0.\tag{2.30c}
$$

We now solve the four equations ((2.29) and (3.30)) to find $x ( t ) , y ( t ) , z ( t )$ , and the multiplier $\mu ( t )$

In this process we have obtained more information than was originally sought. Not only do we get the $q _ { k } \mathbf { \dot { s } }$ we set out to find, but we also get $m \lambda _ { l } { ' } \mathrm { s } .$ . What is the physical significance of the $\lambda _ { l } ' \mathbf { s } ?$ Suppose we remove the constraints on the system, but instead apply external forces $Q _ { k } ^ { \prime }$ in such a manner as to keep the motion of the system unchanged. The equations of motion likewise remain the same. Clearly these extra applied forces must be equal to the forces of constraint, for they are the forces applied to the system so as to satisfy the condition of constraint. Under the influence of these forces $Q _ { k } ^ { \prime }$ , the equations o motion are

$$
\frac {d}{d t} \frac {\partial L}{\partial \dot {q} _ {k}} - \frac {\partial L}{\partial q _ {k}} = Q _ {k} ^ {\prime}.\tag{2.31}
$$

But these must be identical with Eqs. (2.24). Hence, we can identify (2.25) with $Q _ { k } ^ { \prime }$ , the generalized forces of constraint. In this type of problem we really do no eliminate the forces of constraint from the formulation. They are supplied as par of the answer.

Although it is not obvious, the version of Hamilton’s principle adopted here for semiholonomic systems also requires that the constraints do no work in virtua displacements. This can be most easily seen by rewriting Hamilton’s principle in

## 2.4 Extending Hamilton’s Principle to Systems with Constraint

the form

$$
\delta \int_ {t _ {1}} ^ {t _ {2}} L d t = \delta \int_ {t _ {1}} ^ {t _ {2}} T d t - \delta \int_ {t _ {1}} ^ {t _ {2}} U d t = 0.\tag{2.32}
$$

If the variation of the integral over the generalized potential is carried out by the procedures of Section 2.3, the principle takes the form

$$
\delta \int_ {t _ {1}} ^ {t _ {2}} T d t = \int_ {t _ {1}} ^ {t _ {2}} \sum_ {k} \left[ \frac {\partial U}{\partial q _ {k}} - \frac {d}{d t} \left(\frac {\partial U}{\partial \dot {q} _ {k}}\right) \right] \delta q _ {k} d t;\tag{2.33}
$$

or, by Eq. (1.58),

$$
\delta \int_ {t _ {1}} ^ {t _ {2}} T d t = - \int_ {t _ {1}} ^ {t _ {2}} \sum_ {k} Q _ {k} \delta q _ {k} d t.\tag{2.34}
$$

In this dress, Hamilton’s principle says that the difference in the time integral of the kinetic energy between two neighboring paths is equal to the negative of the time integral of the work done in the virtual displacements between the paths. The work involved is that done only by the forces derivable from the generalized potential. The same Hamilton’s principle holds for both holonomic and semiholonomic systems, it must be required that the additional forces of semiholonomic constraints do no work in the displacements $\delta q _ { k }$ . This restriction parallels the earlier condition that the virtual work of the forces of holonomic constraint also be zero (cf. Section 1.4). In practice, the restriction presents little handi cap to the applications, as many problems in which the semiholonomic formalism is used relate to rolling without slipping, where the constraints are obviously workless.

Note that Eq. (2.20) is not the most general type of nonholonomic constraint; e.g., it does not include equations of constraint in the form of inequalities. On the other hand, it does include holonomic constraints. A holonomic equation of constraint,

$$
f (q _ {1}, q _ {2}, q _ {3}, \ldots , q _ {n}, t) = 0,\tag{2.35}
$$

is equivalent to (2.20) with no dependence on $\dot { q } _ { k }$ . Thus, the Lagrange multiplier method can be used also for holonomic constraints when (1) it is inconvenient to reduce all the $q ^ { * } { \bf s }$ to independent coordinates or (2) we might wish to obtain the forces of constraint.

As another example of the method, let us consider the following somewhat trivial illustration—a hoop rolling, without slipping, down an inclined plane. In this example, the constraint of “rolling” is actually holonomic, but this fact will be immaterial to our discussion. On the other hand, the holonomic constraint that the hoop be on the inclined plane will be contained implicitly in our choice of generalized coordinates.

![](images/5241e763bb5a55da206a57e3082eabc5c959f03de7ab8e8e7f7cc0700ba7bcbf.jpg)  
FIGURE 2.5 A hoop rolling down an inclined plane.

The two generalized coordinates are x, θ, as in Fig. 2.5, and the equation o rolling constraint is

$$
r d \theta = d x.
$$

The kinetic energy can be resolved into kinetic energy of motion of the cente of mass plus the kinetic energy of motion about the center of mass:

$$
T = \frac {1}{2} M \dot {x} ^ {2} + \frac {1}{2} M r ^ {2} \dot {\theta} ^ {2}.
$$

The potential energy is

$$
V = M g (l - x) \sin \phi ,
$$

where l is the length of the inclined plane and the Lagrangian is

$$
\begin{array}{l} L = T - V \\ \qquad = \frac {M \dot {x} ^ {2}}{2} + \frac {M r ^ {2} \dot {\theta} ^ {2}}{2} - M g (l - x) \sin \phi . \end{array}\tag{2.36}
$$

Since there is one equation of constraint, only one Lagrange multiplier λ is needed. The coefficients appearing in the constraint equation are:

$$
a _ {\theta} = r, \quad a _ {x} = - 1.
$$

The two Lagrange equations therefore are

$$
M \ddot {x} - M g \sin \phi + \lambda = 0,\tag{2.37}
$$

$$
M r ^ {2} \ddot {\theta} - \lambda r = 0,\tag{2.38}
$$

which along with the equation of constraint,

$$
r \dot {\theta} = \dot {x},\tag{2.39}
$$

constitutes three equations for three unknowns, θ, x, λ.

Differentiating (2.39) with respect to time, we have

$$
r \ddot {\theta} = \ddot {x}.
$$

Hence, from (2.38)

$$
M \ddot {x} = \lambda ,
$$

and (2.37) becomes

$$
\ddot {x} = \frac {g \sin \phi}{2}
$$

along with

$$
\lambda = \frac {M g \sin \phi}{2}
$$

and

$$
\ddot {\theta} = \frac {g \sin \phi}{2 r}.
$$

Thus, the hoop rolls down the incline with only one-half the acceleration it would have slipping down a frictionless plane, and the friction force of constraint is $\lambda = M g$ sin $\phi / 2 .$

## 2.5 ADVANTAGES OF A VARIATIONAL PRINCIPLE FORMULATION

Although we can extend the original formulation of Hamilton’s principle (2.2) to include some nonholonomic constraints, in practice this formulation of mechanics is most useful when a Lagrangian of independent coordinates can be set up for the system. The variational principle formulation has been justly described as “elegant,” for in the compact Hamilton’s principle is contained all of the mechanics of holonomic systems with forces derivable from potentials. The principle has the further merit that it involves only physical quantities that can be defined without reference to a particular set of generalized coordi nates, namely, the kinetic and potential energies. The formulation is therefore automatically invariant with respect to the choice of coordinates for the system.

From the variational Hamilton’s principle, it is also obvious why the Lagrangian is always uncertain to a total time derivative of any function of the coordinates and time, as mentioned at the end of Section 1.4. The time integral of such a total derivative between points 1 and 2 depends only on the values of the arbitrary function at the end points. As the variation at the end points is zero, the addition of the arbitrary time derivative to the Lagrangian does not affect the variational behavior of the integral.

Another advantage is that the Lagrangian formulation can be easily extended to describe systems that are not normally considered in dynamics—such as the elastic field, the electromagnetic field, and field properties of elementary particles. Some of these generalizations will be considered later, but as three simple examples of its application outside the usual framework of mechanics, le us consider the cases of an $R L$ circuit, an $L C$ circuit, and coupled circuits.

We consider the physical system of a battery of voltage V in series with an inductance L and a resistance of value R and choose the electric charge $q$ as the dynamical variable. The inductor acts as the kinetic energy term since the inductive effect depends upon the time rate of change of the charge. The resisto provides a dissipative term and the potential energy is $q V$ . The dynamic terms in Lagrange’s equation with dissipation (1.70) are

$$
T = \frac {1}{2} L \dot {q} ^ {2}, \quad \mathcal {F} = \frac {1}{2} R \dot {q} ^ {2},
$$

and potential energy $= q V$ . The equation of motion is

$$
V = L \ddot {q} + R \dot {q} = L \dot {I} + R I,\tag{2.40}
$$

where $I = { \dot { q } }$ is the electric current. A solution for a battery connected to the circuit at time $t = 0$ is

$$
I = I _ {0} (1 - e ^ {- R t / L}),
$$

where $I _ { 0 } = V / R$ is the final steady-state current flow.

The mechanical analog for this is a sphere of radius a and effective mass $m ^ { \prime }$ falling in a viscous fluid of constant density and viscosity η under the force of gravity. The effective mass is the difference between the actual mass and the mass of the displaced fluid, and the direction of motion is along the y axis. For this system,

$$
T = \frac {1}{2} m ^ {\prime} \dot {y} ^ {2}, \quad \mathcal {F} = 3 \pi \eta a \dot {y} ^ {2},
$$

and potential energy $\ = = \ m ^ { \prime } g y$ , where the frictional drag force, $F _ { f } ~ = ~ 6 \pi \eta a { \dot { y } }$ called Stokes’ law, was given at the end of Section 1.5.

The equation of motion is given by Lagrange’s equations (1.70) a

$$
m ^ {\prime} g = m ^ {\prime} \ddot {y} + 6 \pi \eta a \dot {y}.
$$

Using $v = \dot { y }$ , the solution (if the motion starts from rest at $t = 0 )$ ), is

$$
v = v _ {o} (1 - e ^ {- t / \tau})
$$

where $\tau = m ^ { \prime } / ( 6 \pi \eta a )$ is a measure of the time it takes for the sphere to reach $1 / e$ of its terminal speed of $v _ { 0 } = m ^ { \prime } g / 6 \pi \eta a$

Another example from electrical circuits is an inductance, $L .$ , in series with a capacitance, $C .$ The capacitor acts as a source of potential energy given by $q ^ { 2 } / C$ where $q$ is the electric charge. The Lagrangian produces the equation of motion,

$$
L \ddot {q} + \frac {q}{C} = 0,\tag{2.41}
$$

which has the solution

$$
q = q _ {0} \cos \omega_ {0} t,
$$

where $q _ { 0 }$ is the charge stored in the capacitor at $t = 0$ , and the assumption is that no charge is flowing at $t = 0$ . The quantity

$$
\omega_ {0} = \frac {1}{\sqrt {L C}}
$$

is the resonant frequency of the system.

The mechanical analog of this system is the simple harmonic oscillator described by the Lagrangian $L \ = \ { \textstyle { \frac { 1 } { 2 } } } { \dot { m } } { \dot { x } } ^ { 2 } \ - \ { \textstyle { \frac { 1 } { 2 } } } k x ^ { 2 }$ , which gives an equation of motion,

$$
m \ddot {x} + k x = 0,
$$

whose solution for the same boundary conditions is

$$
x = x _ {0} \cos \omega_ {0} t \qquad \mathrm{with} \quad \omega_ {0} = \sqrt {k / m}.
$$

These two examples show that an inductance is an inertial term, the electrical analog of mass. Resistance is the analog of Stokes’ law type of frictional drag, and the capacitance term $1 / C$ represents a Hooke’s law spring constant. With this background, a system of coupled electrical circuits of the type shown in Fig. 2.6 has a Lagrangian of the form

![](images/c72bf105e58c731923c2c9c65b7c743c97d44b6c42296fc54fe508fcfab7aad0.jpg)  
FIGURE 2.6 A system of coupled circuits to which the Lagrangian formulation can be applied.

$$
L = \frac{1}{2}\sum_{j}L_{j}\dot{q}_{j}^{2} + \frac{1}{2}\sum_{\substack{jk\\ j\neq k}}M_{jk}\dot{q}_{j}\dot{q}_{k} - \sum_{j}\frac{q_{j}^{2}}{2C_{j}} +\sum_{j}e_{j}(t)q_{j},
$$

and a dissipation function

$$
\mathcal {F} = \frac {1}{2} \sum_ {j} R _ {j} \dot {q} _ {j} ^ {2}.
$$

where the mutual inductance terms, $M _ { j k } { \dot { q } } _ { j } { \dot { q } } _ { k }$ , are added to take into account the coupling between inductors. The Lagrange equations are

$$
L_{j}\frac{d^{2}q_{j}}{dt^{2}} +\sum_{\substack{k\\ j\neq k}}M_{jk}\frac{d^{2}q_{k}}{dt^{2}} +R_{j}\frac{dq_{j}}{dt} +\frac{q_{j}}{C_{j}} = E_{j}(t).\tag{2.42}
$$

where the $E _ { j } ( t )$ terms are the external emf’s.

This description of two different physical systems by Lagrangians of the same form means that all the results and techniques devised for investigating one of the systems can be taken over immediately and applied to the other. In this particular case, the study of the behavior of electrical circuits has been pursued intensely and some special techniques have been developed; these can be directly applied to the corresponding mechanical systems. Much work has been done in formulating equivalent electrical problems for mechanical or acoustical systems, and vice versa. Terms hitherto reserved for electrical circuits (reactance, susceptance, etc.) are now commonly found in treatises on the theory of vibrations of mechanica systems.

Additionally, one type of generalization of mechanics is due to a subtle form of equivalence. We have seen that the Lagrangian and Hamilton’s principle together form a compact invariant way of obtaining the mechanical equations of motion. This possibility is not reserved for mechanics only; in almost every field of physics variational principles can be used to express the “equations of motion,” whether they be Newton’s equations, Maxwell’s equations, or the Schrodinger¨ equation. Consequently, when a variational principle is used as the basis of the formulation, all such fields will exhibit, at least to some degree, a structural analogy. When the results of experiments show the need for alterating the physica content in the theory of one field, this degree of analogy has often indicated how similar alterations may be carried out in other fields. Thus, the experiments performed early in this century showed the need for quantization of both electromagnetic radiation and elementary particles. The methods of quantization, however, were first developed for particle mechanics, starting essentially from the Lagrangian formulation of classical mechanics. By describing the electromagnetic field by a Lagrangian and corresponding Hamilton’s variational principle, it is possible to carry over the methods of particle quantization to construct a quantum electrodynamics (cf. Sections 13.5 and 13.6).

## 2.6 CONSERVATION THEOREMS AND SYMMETRY PROPERTIES

Thus far, we have been concerned primarily with obtaining the equations of motion, but little has been said about how to solve them for a particular problem once they are obtained. In general, this is a question of mathematics. A system of n degrees of freedom will have n differential equations that are second order in time. The solution of each equation will require two integrations resulting, all told, in 2n constants of integration. In a specific problem these constants will be determined by the initial conditions, i.e., the initial values of the $n q _ { j } ;$ ’s and the $n \dot { q } _ { j } \mathbf { \bar { s } }$ . Sometimes the equations of motion will be integrable in terms of known functions, but not always. In fact, the majority of problems are not completely integrable. However, even when complete solutions cannot be obtained, it is often possible to extract a large amount of information about the physical nature of the system motion. Indeed, such information may be of greater interest to the physicist than the complete solution for the generalized coordinates as a function of time. It is important, therefore, to see how much can be stated about the motion of a given system without requiring a complete integration of the problem.\*

In many problems a number of first integrals of the equations of motion can b obtained immediately; by this we mean relations of the type

$$
f (q _ {1}, q _ {2}, \dots , \dot {q} _ {1}, \dot {q} _ {2}, \dots , t) = \text { constant },\tag{2.43}
$$

which are first-order differential equations. These first integrals are of interest because they tell us something physically about the system. They include, in fact, the conservation laws obtained in Chapter 1.

Let us consider as an example a system of mass points under the influence of forces derived from potentials dependent on position only. Then

$$
\begin{array}{c} \frac {\partial L}{\partial \dot {x} _ {i}} \equiv \frac {\partial T}{\partial \dot {x} _ {i}} - \frac {\partial V}{\partial \dot {x} _ {i}} = \frac {\partial T}{\partial \dot {x} _ {i}} = \frac {\partial}{\partial \dot {x} _ {i}} \sum \frac {1}{2} m _ {i} (\dot {x} _ {i} ^ {2} + \dot {y} _ {i} ^ {2} + \dot {z} _ {i} ^ {2}) \\ = m _ {i} \dot {x} _ {i} = p _ {i x}, \end{array}
$$

which is the x component of the linear momentum associated with the ith particle. This result suggests an obvious extension to the concept of momentum. The generalized momentum associated with the coordinate $q _ { j }$ shall be defined as

$$
p _ {j} = \frac {\partial L}{\partial \dot {q} _ {j}}.\tag{2.44}
$$

The terms canonical momentum and conjugate momentum are often also used for $p _ { j }$ . Notice that if $q _ { j }$ is not a Cartesian coordinate, $p _ { j }$ does not necessarily have the dimensions of a linear momentum. Further, if there is a velocity-dependent potential, then even with a Cartesian coordinate $q _ { j }$ the associated generalized momentum will not be identical with the usual mechanical momentum. Thus, in the case of a group of particles in an electromagnetic field, the Lagrangian is (cf. 1.63)

$$
L = \sum_ {i} \frac {1}{2} m _ {i} \dot {r} _ {i} ^ {2} - \sum_ {i} q _ {i} \phi (x _ {i}) + \sum_ {i} q _ {i} {\bf A} (x _ {i}) \cdot \dot {\bf r} _ {i}
$$

$( q _ { i }$ here denotes charge) and the generalized momentum conjugate to $x _ { i }$ is

$$
p _ {i x} = \frac {\partial L}{\partial \dot {x} _ {i}} = m _ {i} \dot {x} _ {i} + q _ {i} A _ {x},\tag{2.45}
$$

i.e., mechanical momentum plus an additional term.

If the Lagrangian of a system does not contain a given coordinate $q _ { j }$ (although it may contain the corresponding velocity ${ \dot { q } } _ { j } )$ ), then the coordinate is said to be cyclic or ignorable. This definition is not universal, but it is the customary one and will be used here. The Lagrange equation of motion,

$$
\frac {d}{d t} \frac {\partial L}{\partial \dot {q} _ {j}} - \frac {\partial L}{\partial q _ {j}} = 0,
$$

reduces, for a cyclic coordinate, to

$$
\frac {d}{d t} \frac {\partial L}{\partial \dot {q} _ {j}} = 0
$$

or

$$
\frac {d p _ {j}}{d t} = 0,
$$

which mean that

$$
p _ {j} = \text { constant }.\tag{2.46}
$$

Hence, we can state as a general conservation theorem that the generalized momentum conjugate to a cyclic coordinate is conserved.

Note that the derivation of Eq. (2.46) assumes that $q _ { j }$ is a generalized coordinate; one that is linearly independent of all the other coordinates. When equations of constraint exist, all the coordinates are not linearly independent. For example, the angular coordinate $\theta$ is not present in the Lagrangian of a hoop rolling without slipping in a horizontal plane that was previously discussed, but the angle appears in the constraint equations $r d \theta = d x$ . As a result, the angular momentum, $p _ { \theta } = m r ^ { 2 } { \dot { \theta } }$ , is not a constant of the motion.

Equation (2.46) constitutes a first integral of the form (2.43) for the equations of motion. It can be used formally to eliminate the cyclic coordinate from the problem, which can then be solved entirely in terms of the remaining generalized coordinates. Briefly, the procedure, originated by Routh, consists in modifying the Lagrangian so that it is no longer a function of the generalized velocity corresponding to the cyclic coordinate, but instead involves only its conjugate momentum. The advantage in so doing is that $p _ { j }$ can then be considered one of the constants of integration, and the remaining integrations involve only the noncyclic coordinates. We shall defer a detailed discussion of Routh’s method until the Hamiltonian formulation (to which it is closely related) is treated.

Note that the conditions for the conservation of generalized momenta are more general than the two momentum conservation theorems previously derived. For example, they furnish a conservation theorem for a case in which the law of action and reaction is violated, namely, when electromagnetic forces are present. Sup pose we have a single particle in a field in which neither $\phi$ nor A depends on x. Then x nowhere appears in L and is therefore cyclic. The corresponding canonical momentum $p _ { x }$ must therefore be conserved. From (1.63) this momentum now has the form

$$
p _ {x} = m \dot {x} + q A _ {x} = \text { constant }.\tag{2.47}
$$

In this case, it is not the mechanical linear momentum mx˙ that is conserved but rather its sum with $q A _ { x } . ^ { * }$ Nevertheless, it should still be true that the conservation theorems of Chapter 1 are contained within the general rule for cyclic coordinates; with proper restrictions (2.46) should reduce to the theorems of Section 1.2.

We first consider a generalized coordinate $q _ { j }$ , for which a change $d q _ { j }$ represents a translation of the system as a whole in some given direction. An example would be one of the Cartesian coordinates of the center of mass of the system. Then clearly $q _ { j }$ cannot appear in $T ,$ , for velocities are not affected by a shift in the origin, and therefore the partial derivative of T with respect to $q _ { j }$ must be zero. Further, we will assume conservative systems for which V is not a function of the velocities, so as to eliminate such complications as electromagnetic forces. The Lagrange equation of motion for a coordinate so defined then reduces to

$$
\frac {d}{d t} \frac {\partial T}{\partial \dot {q} _ {j}} \equiv \dot {p} _ {j} = - \frac {\partial V}{\partial q _ {j}} \equiv Q _ {j}.\tag{2.48}
$$

We will now show that (2.48) is the equation of motion for the total linear momentum, i.e., that $Q _ { j }$ represents the component of the total force along the direction of translation of $q _ { j }$ , and $p _ { j }$ is the component of the total linear momentum along this direction. In general, the generalized force $Q _ { j }$ is given by Eq. (1.49):

$$
Q _ {j} = \sum_ {i} \mathbf {F} _ {i} \cdot \frac {\partial \mathbf {r} _ {i}}{\partial q _ {j}}.
$$

Since $d q _ { j }$ corresponds to a translation of the system along some axis, the vectors $\mathbf { r } _ { i } ( q _ { j } )$ and $\mathbf { r } _ { i } ( q _ { j } + d q _ { j } )$ are related as shown in Fig. 2.7. By the definition of a

![](images/8211ebd64d20b807cd5097776bc3102d9ac5c435794be45ca157d0e6acfef017.jpg)  
FIGURE 2.7 Change in a position vector under translation of the system.

derivative, we have

$$
\frac {\partial \mathbf {r} _ {i}}{\partial q _ {j}} = \lim _ {d q _ {j} \rightarrow 0} \frac {\mathbf {r} _ {i} (q _ {j} + d q _ {j}) - \mathbf {r} _ {i} (q _ {j})}{d q _ {j}} = \frac {d q _ {j}}{d q _ {j}} \mathbf {n} = \mathbf {n},\tag{2.49}
$$

where n is the unit vector along the direction of the translation. Hence,

$$
Q _ {j} = \sum \mathbf {F} _ {i} \cdot \mathbf {n} = \mathbf {n} \cdot \mathbf {F},
$$

which (as was stated) is the component of the total force in the direction of n. To prove the other half of the statement, note that with the kinetic energy in the form

$$
T = \frac {1}{2} \sum m _ {i} \dot {\mathbf {r}} _ {i} ^ {2},
$$

the conjugate momentum is

$$
\begin{array}{c} p _ {j} = \frac {\partial T}{\partial \dot {q} _ {j}} = \sum_ {i} m _ {i} \dot {\mathbf {r}} _ {i} \cdot \frac {\partial \dot {\mathbf {r}} _ {i}}{\partial \dot {q} _ {j}} \\ = \sum_ {i} m _ {i} \mathbf {v} _ {i} \cdot \frac {\partial \mathbf {r} _ {i}}{\partial q _ {j}}, \end{array}
$$

using Eq. (1.51). Then from Eq. (2.49)

$$
p _ {j} = \mathbf {n} \cdot \sum_ {i} m _ {i} \mathbf {v} _ {i},
$$

which again, as predicted, is the component of the total system linear momentum along n.

Suppose now that the translation coordinate $q _ { j }$ that we have been discussing is cyclic. Then $q _ { j }$ cannot appear in V and therefore

$$
- \frac {\partial V}{\partial q _ {j}} \equiv Q _ {j} = 0.
$$

But this is simply the familiar conservation theorem for linear momentum—that if a given component of the total applied force vanishes, the corresponding component of the linear momentum is conserved.

In a similar fashion, it can be shown that if a cyclic coordinate $q _ { j }$ is such that $d q _ { j }$ corresponds to a rotation of the system of particles around some axis, then the conservation of its conjugate momentum corresponds to conservation of an angular momentum. By the same argument used above, $T$ cannot contain $q _ { j }$ , for a rotation of the coordinate system cannot affect the magnitude of the velocities. Hence, the partial derivative of $T$ with respect to $q _ { j }$ must again be zero, and since V is independent of ${ \dot { q } } _ { j }$ , we once more get Eq. (2.48). But now we wish to show that with $q _ { j }$ a rotation coordinate the generalized force is the component of the total applied torque about the axis of rotation, and $p _ { j }$ is the component of the total angular momentum along the same axis.

The generalized force $Q _ { j }$ is again given by

$$
Q _ {j} = \sum_ {i} \mathbf {F} _ {i} \cdot \frac {\partial \mathbf {r} _ {i}}{\partial q _ {j}},
$$

only the derivative now has a different meaning. Here the change in $q _ { j }$ must correspond to an infinitesimal rotation of the vector $\mathbf { r } _ { i }$ , keeping the magnitude of the vector constant. From Fig. 2.8, the magnitude of the derivative can easily be obtained:

$$
\left| d \mathbf {r} _ {i} \right| = r _ {i} \sin \theta d q _ {j} \quad \text { and } \quad \left| \frac {\partial \mathbf {r} _ {i}}{\partial q _ {j}} \right| = r _ {i} \sin \theta ,
$$

![](images/d289ee23d8356a2a5ffd4fdb6a8b9f30ea4010efdfda979de6e2578d07c46909.jpg)  
FIGURE 2.8 Change of a position vector under rotation of the system

and its direction is perpendicular to both $\mathbf { r } _ { i }$ and n. Clearly, the derivative can be written in vector form as

$$
\frac {\partial \mathbf {r} _ {i}}{\partial q _ {j}} = \mathbf {n} \times \mathbf {r} _ {i}.\tag{2.50}
$$

With this result, the generalized force becomes

$$
\begin{array}{c} Q _ {j} = \sum_ {i} \mathbf {F} _ {i} \cdot \mathbf {n} \times \mathbf {r} _ {i} \\ = \sum_ {i} \mathbf {n} \cdot \mathbf {r} _ {i} \times \mathbf {F} _ {i}, \end{array}
$$

reducing to

$$
Q _ {j} = \mathbf {n} \cdot \sum_ {i} \mathbf {N} _ {i} = \mathbf {n} \cdot \mathbf {N},
$$

which proves the first part. A similar manipulation of $p _ { j }$ with the aid of Eq. (2.50) provides proof of the second part of the statement:

$$
p _ {j} = \frac {\partial T}{\partial \dot {q} _ {j}} = \sum_ {i} m _ {i} \mathbf {v} _ {i} \cdot \frac {\partial \mathbf {r} _ {i}}{\partial q _ {j}} = \sum_ {i} \mathbf {n} \cdot \mathbf {r} _ {i} \times m _ {i} \mathbf {v} _ {i} = \mathbf {n} \cdot \sum_ {i} \mathbf {L} _ {i} = \mathbf {n} \cdot \mathbf {L}.
$$

Summarizing these results, we see that if the rotation coordinate $q _ { j }$ is cyclic, then $Q _ { j }$ , which is the component of the applied torque along n, vanishes, and the component of L along n is constant. Here we have recovered the angula momentum conservation theorem out of the general conservation theorem relating to cyclic coordinates.

The significance of cyclic translation or rotation coordinates in relation to the properties of the system deserves some comment at this point. If a generalized coordinate corresponding to a displacement is cyclic, it means that a translation of the system, as if rigid, has no effect on the problem. In other words, if the sys tem is invariant under translation along a given direction, the corresponding linear momentum is conserved. Similarly, the fact that a generalized rotation coordinate is cyclic (and therefore the conjugate angular momentum conserved) indicates that the system is invariant under rotation about the given axis. Thus, the momentum conservation theorems are closely connected with the symmetry properties of the system. If the system is spherically symmetric, we can say without furthe ado that all components of angular momentum are conserved. $\mathrm { O r } ,$ , if the system is symmetric only about the z axis, then only $L _ { z }$ will be conserved, and so on for the other axes. These symmetry considerations can often be used with relatively complicated problems to determine by inspection whether certain constants of the motion exist. (cf. Noether’s theorem—Sec. 13.7.)

Suppose, for example, the system consists of a set of mass points moving in a potential field generated by fixed sources uniformly distributed on an infinite plane, say, the $z = 0$ plane. (The sources might be a mass distribution if the forces

## 2.7 Energy Function and the Conservation of Energy

were gravitational, or a charge distribution for electrostatic forces.) Then the sym metry of the problem is such that the Lagrangian is invariant under a translation of the system of particles in the x- or y-directions (but not in the z-direction) and also under a rotation about the z axis. It immediately follows that the x- and y-components of the total linear momentum, $P _ { x }$ and $P _ { y }$ , are constants of the motion along with $L _ { z }$ , the z-component of the total angular momentum. However, if the sources were restricted only to the half plane, $x \ge 0$ , then the symmetry fo translation along the x axis and for rotation about the z axis would be destroyed. In that case, $P _ { x }$ and $L _ { z }$ could not be conserved, but $P _ { y }$ would remain a constant of the motion. We will encounter the connections between the constants of motion and the symmetry properties of the system several times in the following chapters.

## 2.7 ENERGY FUNCTION AND THE CONSERVATION OF ENERGY

Another conservation theorem we should expect to obtain in the Lagrangian formulation is the conservation of total energy for systems where the forces are derivable from potentials dependent only upon position. Indeed, it is possible to demonstrate a conservation theorem for which conservation of total energy represents only a special case. Consider a general Lagrangian, which will be a function of the coordinates $q _ { j }$ and the velocities ${ \dot { q } } _ { j }$ and may also depend explicitly on the time. (The explicit time dependence may arise from the time variation of external potentials, or from time-dependent constraints.) Then the total time derivative of $L$ is

$$
\frac {d L}{d t} = \sum_ {j} \frac {\partial L}{\partial q _ {j}} \frac {d q _ {j}}{d t} + \sum_ {j} \frac {\partial L}{\partial \dot {q} _ {j}} \frac {d \dot {q} _ {j}}{d t} + \frac {\partial L}{\partial t}.\tag{2.51}
$$

From Lagrange’s equations,

$$
\frac {\partial L}{\partial q _ {j}} = \frac {d}{d t} \left(\frac {\partial L}{\partial \dot {q} _ {j}}\right),
$$

and (2.51) can be rewritten as

$$
\frac {d L}{d t} = \sum_ {j} \frac {d}{d t} \left(\frac {\partial L}{\partial \dot {q} _ {j}}\right) \dot {q} _ {j} + \sum_ {j} \frac {\partial L}{\partial \dot {q} _ {j}} \frac {d \dot {q} _ {j}}{d t} + \frac {\partial L}{\partial t}
$$

or

$$
\frac {d L}{d t} = \sum_ {j} \frac {d}{d t} \left(\dot {q} _ {j} \frac {\partial L}{\partial \dot {q} _ {j}}\right) + \frac {\partial L}{\partial t}.
$$

It therefore follows that

$$
\frac {d}{d t} \left(\sum_ {j} \dot {q} _ {j} \frac {\partial L}{\partial \dot {q} _ {j}} - L\right) + \frac {\partial L}{\partial t} = 0.\tag{2.52}
$$

The quantity in parentheses is oftentimes called the energy function\* and will be denoted by h:

$$
h (q _ {1}, \dots , q _ {n}; \quad \dot {q} _ {1}, \dots , \dot {q} _ {n}; \quad t) = \sum_ {j} \dot {q} _ {j} \frac {\partial L}{\partial \dot {q} _ {j}} - L,\tag{2.53}
$$

and Eq. (2.52) can be looked on as giving the total time derivative of h:

$$
{\frac {d h}{d t}} = - {\frac {\partial L}{\partial t}}.\tag{2.54}
$$

If the Lagrangian is not an explicit function of time, i.e., if t does not appear in L explicitly but only implicitly through the time variation of $q$ and $\dot { \boldsymbol { q } }$ , then Eq. (2.54) says that h is conserved. It is one of the first integrals of the motion and is sometimes referred to as Jacobi’s integral.<sup>†</sup>

Under certain circumstances, the function h is the total energy of the system. To determine what these circumstances are, we recall that the total kinetic energy of a system can always be written as

$$
T = T _ {0} + T _ {1} + T _ {2},\tag{1.73}
$$

where $T _ { 0 }$ is a function of the generalized coordinates only, $T _ { 1 } ( q , \dot { q } )$ is linear in the generalized velocities, and $T _ { 2 } ( q , \dot { q } )$ is a quadratic function of the $\dot { q } ^ { \mathbf { \lambda } } \mathbf { s } .$ . For a very wide range of systems and sets of generalized coordinates, the Lagrangian can be similarly decomposed as regards its functional behavior in the $\dot { \boldsymbol { q } }$ variables:

$$
L (q, \dot {q}, t) = L _ {0} (q, t) + L _ {1} (q, \dot {q}, t) + L _ {2} (q, \dot {q}, t).\tag{2.55}
$$

Here $L _ { 2 }$ is a homogeneous function of the second degree (not merely quadratic) in $\dot { \boldsymbol { q } }$ , while $L _ { 1 }$ is homogeneous of the first degree in $\dot { \boldsymbol { q } }$ . There is no reason intrinsic to mechanics that requires the Lagrangian to conform to Eq. (2.55), but in fact i does for most problems of interest. The Lagrangian clearly has this form when the forces are derivable from a potential not involving the velocities. Even with the velocity-dependent potentials, we note that the Lagrangian for a charged par ticle in an electromagnetic field, Eq. (1.63), satisfies Eq. (2.55). Now, recall tha Euler’s theorem states that if $f$ is a homogeneous function of degree n in the variables $x _ { i }$ , then

$$
\sum_ {i} x _ {i} \frac {\partial f}{\partial x _ {i}} = n f.\tag{2.56}
$$

Applied to the function h, Eq. (2.53), for the Lagrangians of the form (2.55), this theorem implies that

$$
h = 2 L _ {2} + L _ {1} - L = L _ {2} - L _ {0}.\tag{2.57}
$$

If the transformation equations defining the generalized coordinates, Eqs. (1.38), do not involve the time explicitly, then by Eqs. (1.73) $T ~ = ~ T _ { 2 }$ . If, further, the potential does not depend on the generalized velocities, then $L _ { 2 } \ = \ T$ and $L _ { 0 } = - V$ , so that

$$
h = T + V = E,\tag{2.58}
$$

and the energy function is indeed the total energy. Under these circumstances, if V does not involve the time explicitly, neither will L. Thus, by Eq. (2.54), h (which is here the total energy), will be conserved.

Note that the conditions for conservation of h are in principle quite distinct from those that identify h as the total energy. We can have a set of generalized coordinates such that in a particular problem h is conserved but is not the total energy. On the other hand, h can be the total energy, in the form $T + V$ , but not be conserved. Also note that whereas the Lagrangian is uniquely fixed for each system by the prescription $L = T - U$ independent of the choice of generalized coordinates, the energy function h depends in magnitude and functional form on the specific set of generalized coordinates. For one and the same system, various energy functions h of different physical content can be generated depending on how the generalized coordinates are chosen.

The most common case that occurs in classical mechanics is one in which the kinetic energy terms are all of the form $m \dot { q } _ { i } ^ { 2 } / 2$ or $p _ { i } ^ { 2 } / 2 m$ and the potential energy depends only upon the coordinates. For these conditions, the energy function is both conserved and is also the total energy.

Finally, note that where the system is not conservative, but there are frictional forces derivable from a dissipation function ${ \mathcal F }$ , it can be easily shown that $\mathcal { F }$ is related to the decay rate of h. When the equations of motion are given by Eq. (1.70), including dissipation, then Eq. (2.52) has the form

$$
\frac {d h}{d t} + \frac {\partial L}{\partial t} = \sum_ {j} \frac {\partial \mathcal {F}}{\partial \dot {q} _ {j}} \dot {q} _ {j}.
$$

By the definition of ${ \mathcal { F } } _ { : }$ , Eq. (1.67), it is a homogeneous function of the $\dot { q } ^ { \mathrm { ~ s ~ } }$ of degree 2. Hence, applying Euler’s theorem again, we have

$$
\frac {d h}{d t} = - 2 \mathcal {F} - \frac {\partial L}{\partial t}.\tag{2.59}
$$

If $L$ is not an explicit function of time, and the system is such that h is the same as the energy, then Eq. (2.59) says that $2 \mathcal { F }$ is the rate of energy dissipation,

$$
\frac {d E}{d t} = - 2 \mathcal {F},\tag{2.60}
$$

a statement proved above (cf. Sec. 1.5) in less general circumstances.

## DERIVATIONS

1. Complete the solution of the brachistochrone problem begun in Section 2.2 and show that the desired curve is a cycloid with a cusp at the initial point at which the particle is released. Show also that if the particle is projected with an initial kinetic energy $\frac { 1 } { 2 } m v _ { 0 } ^ { 2 }$ that the brachistochrone is still a cycloid passing through the two points with a cusp at a height z above the initial point given by $v _ { 0 } ^ { 2 } = 2 g z$

2. Show that if the potential in the Lagrangian contains velocity-dependent terms, the canonical momentum corresponding to a coordinate of rotation θ of the entire system is no longer the mechanical angular momentum $L _ { \theta }$ but is given by

$$
p _ {\theta} = L _ {\theta} - \sum_ {i} \mathbf {n} \cdot \mathbf {r} _ {i} \times \nabla_ {\mathbf {v} _ {i}} U,
$$

where $\nabla _ { \mathbf { v } }$ is the gradient operator in which the derivatives are with respect to the velocity components and n is a unit vector in the direction of rotation. If the forces are electromagnetic in character, the canonical momentum is therefore

$$
p _ {\theta} = L _ {\theta} + \sum_ {i} \mathbf {n} \cdot \mathbf {r} _ {i} \times \frac {q _ {i}}{c} \mathbf {A} _ {i}.
$$

3. Prove that the shortest distance between two points in space is a straight line.

4. Show that the geodesics of a spherical surface are great circles, i.e., circles whose centers lie at the center of the sphere.

## EXERCISES

5. A particle is subjected to the potential $V ( x ) = - F x$ , where F is a constant. The particle travels from $x = 0 \mathrm { t o } x = a$ in a time interval $t _ { 0 }$ . Assume the motion of the particle can be expressed in the form $x ( t ) = A + B t + C t ^ { 2 }$ . Find the values of A, B, and C such that the action is a minimum.

6. Find the Euler–Lagrange equation describing the brachistochrone curve for a particle moving inside a spherical Earth of uniform mass density. Obtain a first integral fo this differential equation by analogy to the Jacobi integral h. With the help of this integral, show that the desired curve is a hypocycloid (the curve described by a poin on a circle rolling on the inside of a larger circle). Obtain an expression for the time of travel along the brachistochrone between two points on Earth’s surface. How long would it take to go from New York to Los Angeles (assumed to be 4800 km apart on the surface) along a brachistochrone tunnel (assuming no friction) and how far below the surface would the deepest point of the tunnel be?

7. In Example 2 of Section 2.1 we considered the problem of the minimum surface o revolution. Examine the symmetric case $x _ { 1 } = x _ { 2 } , y _ { 2 } = - y _ { 1 } > 0$ , and express the condition for the parameter a as a transcendental equation in terms of the dimension less quantities $k = x _ { 2 } / a$ , and $\alpha = y _ { 2 } / x _ { 2 }$ . Show that for α greater than a certain value $\alpha _ { 0 }$ two values of k are possible, for $\alpha = \alpha _ { 0 }$ only one value of k is possible, while if $\alpha \prec \alpha _ { 0 }$ no real value of k (or a) can be found, so that no catenary solution exists in this region. Find the value of $\alpha _ { 0 }$ , numerically if necessary.

8. The broken-segment solution described in the text (cf. p. 42), in which the area of revolution is only that of the end circles of radius $y _ { 1 }$ and $y _ { 2 }$ , respectively, is known as the Goldschmidt solution. For the symmetric situation discussed in Exercise $^ { 7 , }$ obtain an expression for the ratio of the area generated by the catenary solutions to that given by the Goldschmidt solution. Your result should be a function only of the parameters $k$ and $\alpha .$ . Show that for sufficiently large values of $\alpha$ at least one of the catenaries gives an area below that of the Goldschmidt solution. On the other hand, show that if $\alpha = \alpha _ { 0 }$ , the Goldschmidt solution gives a lower area than the catenary.

9. A chain or rope of indefinite length passes freely over pulleys at heights $y _ { 1 }$ and $y _ { 2 }$ above the plane surface of Earth, with a horizontal distance $x _ { 2 } - x _ { 1 }$ between them. If the chain or rope has a uniform linear mass density, show that the problem of finding the curve assumed between the pulleys is identical with that of the problem of minimum surface of revolution. (The transition to the Goldschmidt solution as the heights $y _ { 1 }$ and $y _ { 2 }$ are changed makes for a striking lecture demonstration. See Exercise 8.)

10. Suppose it is known experimentally that a particle fell a given distance $y _ { 0 }$ in a time $t _ { 0 } = \sqrt { 2 y _ { 0 } / g }$ . The times of fall for distances other than $y _ { 0 }$ are not known. Sup-pose further that the Lagrangian for the problem is known, but that instead of solving the equation of motion for $y$ as a function of $t ,$ it is guessed that the functional form is

$$
y = a t + b t ^ {2}.
$$

If the constants $a$ and b are adjusted always so that the time to fall $y _ { 0 }$ is correctly given by $t _ { 0 }$ , show directly that the integral

$$
\int_ {0} ^ {t _ {0}} L d t
$$

is an extremum for real values of the coefficients only when $a = 0$ and $b = g / 2$

11. When two billiard balls collide, the instantaneous forces between them are very large but act only in an infinitesimal time $\Delta t .$ , in such a manner that the quantity

$$
\int_ {\Delta t} F d t
$$

remains finite. Such forces are described as impulsive forces, and the integral over $\Delta t$ is known as the impulse of the force. Show that if impulsive forces are present Lagrange’s equations may be transformed into

$$
\left(\frac {\partial L}{\partial \dot {q} _ {j}}\right) _ {f} - \left(\frac {\partial L}{\partial \dot {q} _ {j}}\right) _ {i} = S _ {j},
$$

where the subscripts i and $f$ refer to the state of the system before and after the impulse, $S _ { j }$ is the impulse of the generalized impulsive force corresponding to $q _ { j }$ and L is the Lagrangian including all the nonimpulsive forces.

12. The term generalized mechanics has come to designate a variety of classical mechan ics in which the Lagrangian contains time derivatives o $q _ { i }$ higher than the first. Problems for which $\dddot { \boldsymbol { x } } = f ( \boldsymbol { x } , \dot { \boldsymbol { x } } , \ddot { \boldsymbol { x } } , t )$ have been referred to as $\mathrm { ^ { * } j e r k y ^ { * } }$ mechanics. Such equations of motion have interesting applications in chaos theory (cf. Chapter 11). By applying the methods of the calculus of variations, show that if there is a Lagrangian of the form $L ( q _ { i } , \dot { q } _ { i } , \ddot { q } _ { i } , t )$ , and Hamilton’s principle holds with the zero variation o both $q _ { i }$ and ${ \dot { q } } _ { i }$ at the end points, then the corresponding Euler–Lagrange equations are

$$
\frac {d ^ {2}}{d t ^ {2}} \left(\frac {\partial L}{\partial \ddot {q} _ {i}}\right) - \frac {d}{d t} \left(\frac {\partial L}{\partial \dot {q} _ {i}}\right) + \frac {\partial L}{\partial q _ {i}} = 0, \quad i = 1, 2, \dots , n.
$$

Apply this result to the Lagrangian

$$
{\cal L} = - \frac {m}{2} q \ddot {q} - \frac {k}{2} q ^ {2}.
$$

Do you recognize the equations of motion?

13. A heavy particle is placed at the top of a vertical hoop. Calculate the reaction of the hoop on the particle by means of the Lagrange’s undetermined multipliers and Lagrange’s equations. Find the height at which the particle falls off.

14. A uniform hoop of mass m and radius r rolls without slipping on a fixed cylin der of radius R as shown in the figure. The only external force is that of gravity. If the smaller cylinder starts rolling from rest on top of the bigger cylinder, use the method of Lagrange mulipliers to find the point at which the hoop falls off the cylinder.

![](images/d4030ab7f7bbb778f1ff394352149b0615949f445682905fe4c28d31a97b5da2.jpg)

15. A form of the Wheatstone impedance bridge has, in addition to the usual four resis tances, an inductance in one arm and a capacitance in the opposite arm. Set up L and for the unbalanced bridge, with the charges in the elements as coordinates. Using the Kirchhoff junction conditions as constraints on the currents, obtain the Lagrange equations of motion, and show that eliminating the λ’s reduces these to the usual net work equations.

16. In certain situations, particularly one-dimensional systems, it is possible to incorpo rate frictional effects without introducing the dissipation function. As an example, find the equations of motion for the Lagrangian

$$
L = e ^ {\gamma t} \left(\frac {m \dot {q} ^ {2}}{2} - \frac {k q ^ {2}}{2}\right).
$$

How would you describe the system? Are there any constants of motion? Suppose a point transformation is made of the form

$$
s = e ^ {\gamma t / 2} q.
$$

What is the effective Lagrangian in terms of $s ?$ Find the equation of motion for s. What do these results say about the conserved quantities for the system?

17. It sometimes occurs that the generalized coordinates appear separately in the kinetic energy and the potential energy in such a manner that T and $V$ may be written in the form

$$
T = \sum_ {i} f _ {i} (q _ {i}) \dot {q} _ {i} ^ {2} \quad \text { and } \quad V = \sum_ {i} V _ {i} (q _ {i}).
$$

Show that Lagrange’s equations then separate, and that the problem can always be reduced to quadratures.

18. A point mass is constrained to move on a massless hoop of radius a fixed in a vertical plane that rotates about its vertical symmetry axis with constant angular speed $\omega .$ Obtain the Lagrange equations of motion assuming the only external forces arise from gravity. What are the constants of motion? Show that if ω is greater than a critical value ω , there can be a solution in which the particle remains stationary on the hoop at a point other than at the bottom, but that i $\omega < \omega _ { 0 }$ , the only stationary point for th particle is at the bottom of the hoop. What is the value of $\omega _ { 0 } ?$

19. A particle moves without friction in a conservative field of force produced by various mass distributions. In each instance, the force generated by a volume element of the distribution is derived from a potential that is proportional to the mass of the volume element and is a function only of the scalar distance from the volume element. For the following fixed, homogeneous mass distributions, state the conserved quantities in th motion of the particle:

(a) The mass is uniformly distributed in the plane $z = 0 .$

(b) The mass is uniformly distributed in the half-plane $z = 0 , y > 0 .$

(c) The mass is uniformly distributed in a circular cylinder of infinite length, with axis along the z axis.

(d) The mass is uniformly distributed in a circular cylinder of finite length, with axi along the z axis.

(e) The mass is uniformly distributed in a right cylinder of elliptical cross section and infinite length, with axis along the z axis.

(f) The mass is uniformly distributed in a dumbbell whose axis is oriented along the z axis.

(g) The mass is in the form of a uniform wire wound in the geometry of an infinit helical solenoid, with axis along the z axis.

20. A particle of mass m slides without friction on a wedge of angle α and mass M that can move without friction on a smooth horizontal surface, as shown in the figure. Treating the constraint of the particle on the wedge by the method of Lagrange multipliers, find the equations of motion for the particle and wedge. Also obtain an expression for the forces of constraint. Calculate the work done in time t by the forces of constraint acting on the particle and on the wedge. What are the constants of motion for the system? Contrast the results you have found with the situation when the wedge is fixed. [Suggestion: For the particle you may either use a Cartesian coordinate system with y vertical, or one with y normal to the wedge or, even more instructively, do it in both systems.]

![](images/3e97bec402c000442c8f97ce62f772b8efb4aff46dadb2fcc3fe04ce374ea8be.jpg)

21. A carriage runs along rails on a rigid beam, as shown in the figure below. The carriage is attached to one end of a spring of equilibrium length $r _ { 0 }$ and force constant k, whose other end is fixed on the beam. $\mathrm { O n }$ the carriage, another set of rails is perpendicular to the first along which a particle of mass m moves, held by a spring fixed on the beam, of force constant k and zero equilibrium length. Beam, rails, springs, and carriage are assumed to have zero mass. The whole system is forced to move in a plane about the point of attachment of the first spring, with a constant angular speed ω. The length o the second spring is at all times considered small compared to $r _ { 0 }$

(a) What is the energy of the system? Is it conserved?

(b) Using generalized coordinates in the laboratory system, what is the Jacobi integra for the system? Is it conserved?

(c) In terms of the generalized coordinates relative to a system rotating with the angu lar speed $\omega ,$ what is the Lagrangian? What is the Jacobi integral? Is it conserved? Discuss the relationship between the two Jacobi integrals.

![](images/585a80c9cc28df45cdb1315de471dc7229672473f2a1494d334c08a08f6dc753.jpg)

22. Suppose a particle moves in space subject to a conservative potential $V ( \mathbf { r } )$ but is constrained to always move on a surface whose equation is $\sigma ( \mathbf { r } , t ) = 0 $ . (The explicit dependence on t indicates that the surface may be moving.) The instan taneous force of constraint is taken as always perpendicular to the surface. Show analytically that the energy of the particle is not conserved if the surface moves in time. What physically is the reason for nonconservation of the energy under this circumstance?

23. Consider two particles of masses $m _ { 1 }$ and $m _ { 2 }$ . Let $m _ { 1 }$ be confined to move on a circle of radius a in the $z = 0$ plane, centered at $x = y = 0$ . Let $m _ { 2 }$ be confined to move on a circle of radius b in the $z = c$ plane, centered at $x = y = 0 . \mathrm { A }$ light (massless) spring of spring constant k is attached between the two particles.

(a) Find the Lagrangian for the system.

(b) Solve the problem using Lagrange multipliers and give a physical interpretation for each multiplier.

24. The one-dimensional harmonic oscillator has the Lagrangian $L = m \dot { x } ^ { 2 } / 2 - k x ^ { 2 } / 2$ Suppose you did not know the solution to the motion, but realized that the motion must be periodic and therefore could be described by a Fourier series of the form

$$
x (t) = \sum_ {j = 0} a _ {j} \cos j \omega t,
$$

(taking $t = 0$ at a turning point) where ω is the (unknown) angular frequency of th motion. This representation for $x ( t )$ defines a many-parameter path for the system point in configuration space. Consider the action integral I for two points, $t _ { 1 }$ and $t _ { 2 }$ separated by the period $T = 2 \pi / \omega$ . Show that with this form for the system path, I is an extremum for nonvanishing x only if $a _ { j } = 0 .$ , for $j \neq 1$ , and only if $\omega ^ { 2 } = k / m$

25. A disk of radius R rolls without slipping inside the stationary parabola $y = a x ^ { 2 }$ . Find the equations of constraint. What condition allows the disk to roll so that it touches the parabola at one and only one point independent of its position?

26. A particle of mass m is suspended by a massless spring of length L. It hangs, without initial motion, in a gravitational field of strength g. It is struck by an impulsive hor izontal blow, which introduces an angular velocity ω. If ω is sufficiently small, it is obvious that the mass moves as a simple pendulum. If ω is sufficiently large, the mass will rotate about the support. Use a Lagrange multiplier to determine the conditions under which the string becomes slack at some point in the motion.

27. (a) Show that the constraint Eq. (2.29) is truly nonholonomic by showing that it can not be integrated to a homonomic form.

(b) Show that the corresponding constraint forces do no virtual work.

(c) Find one or more solutions to (2.29)–(2.30) for $V ~ = ~ 0$ and show that they conserve energy.