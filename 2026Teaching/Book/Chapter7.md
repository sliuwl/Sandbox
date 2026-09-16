# Lagrange's Equations

The theoretical development of the laws of motion of bodies is a problem of such interest and importance that it has engaged the attention of all the most eminent mathematicians since the invention of dynamics as a mathematical science by Galileo, and especially since the wonderful extension which was given to that science by Newton. Among the successors of those illustrious men, Lagrange has perhaps done more than any other analyst to give extent and harmony to such deductive researches, by showing that the most varied consequences respecting the motions of systems of bodies may be derived from one radical formula; the beauty of the methods so suiting the dignity of the results as to make of his great work a kind of scientific poem.

William Rowan Hamilton, 1834

—William Rowan Hamilton, 1834

Armed with the ideas of the calculus of variations, we are ready to set up the version of mechanics published in 1788 by the Italian–French astronomer and mathematician Lagrange (1736–1813). The Lagrangian formulation has two important advantages over the earlier Newtonian formulation. First, Lagrange's equations, unlike Newton's, take the same form in any coordinate system. Second, in treating constrained systems, such as a bead sliding on a wire, the Lagrangian approach eliminates the forces of constraint (such as the normal force of the wire, which constrains the bead to remain on the wire). This greatly simplifies most problems, since the constraint forces are usually unknown, and this simplification comes at almost no cost, since we usually do not want to know these forces anyway.

In Section 7.1, I prove that Lagrange's equations are equivalent to Newton's second law for a particle moving unconstrained in three dimensions. The extension of this result to $N$ unconstrained particles is surprisingly straightforward, and I leave the details for you to supply (Problem 7.7). In the next few sections, I take up the harder, and more interesting, case of constrained systems. I begin with some simple examples and important definitions (such as degrees of freedom). Then, in Section 7.4, I prove Lagrange's equations for a particle constrained to move on a curved surface (leaving the general case to Problem 7.13). Section 7.5 offers several examples, some of which are distinctly easier to set up in the Lagrangian formulation than in the Newtonian. In

Section 7.6, I introduce the curious terminology of “ignorable coordinates.” Finally, after some summarizing remarks in Section 7.7, the chapter concludes with three sections on topics which, although very important, could be omitted on a first reading. In Section 7.8, I discuss how the laws of energy and momentum conservation appear in Lagrangian mechanics. Section 7.9 describes how Lagrange’s equations can be extended to include magnetic forces, and Section 7.10 is an introduction to the idea of Lagrange multipliers.

Throughout this chapter, except in Section 7.9. I treat only the case that all nonconstraint forces are conservative or can, at least, be derived from a potential energy function. This restriction can be significantly relaxed, but already includes most of the applications that you are likely to meet in practice.

## 7.1 Lagrange's Equations for Unconstrained Motion

Consider a particle moving unconstrained in three dimensions, subject to a conservative net force $\mathbf{F}(\mathbf{r})$ . The particle's kinetic energy is, of course,

$$
T = \frac {1}{2} m v ^ {2} = \frac {1}{2} m \dot {\mathbf {r}} ^ {2} = \frac {1}{2} m (\dot {x} ^ {2} + \dot {y} ^ {2} + \dot {z} ^ {2}),\tag{7.1}
$$

and its potential energy is

$$
U = U (\mathbf {r}) = U (x, y, z).\tag{7.2}
$$

The Lagrangian function, or just Lagrangian, is defined as

$$
\mathcal {L} = T - U.\tag{7.3}
$$

Notice first that the Lagrangian is the KE minus the PE. It is not the same as the total energy. You are certainly entitled to ask why the quantity T - U should be of any interest. There seems to be no simple answer to this question except that it is, as we shall see directly. Notice also that I am using a script L for the Lagrangian $^{1}$ (to distinguish it from the angular momentum L and a length L) and that L depends on the particle's position $(x, y, z)$ and its velocity $(\dot{x}, \dot{y}, \dot{z})$ ; that is, $\mathcal{L} = \mathcal{L}(x, y, z, \dot{x}, \dot{y}, \dot{z})$ .

Let us consider the two derivatives,

$$
\frac {\partial \mathcal {L}}{\partial x} = - \frac {\partial U}{\partial x} = F _ {x}\tag{7.4}
$$

and

$$
\frac {\partial \mathcal {L}}{\partial \dot {x}} = \frac {\partial T}{\partial \dot {x}} = m \dot {x} = p _ {x}.\tag{7.5}
$$

Differentiating the second equation with respect to time and remembering Newton's second law, $F_{x} = \dot{p}_{x}$ (I take for granted that our coordinate frame is inertial), we see that

$$
\frac {\partial \mathcal {L}}{\partial x} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {x}}.\tag{7.6}
$$

In exactly the same way we can prove corresponding equations in $y$ and $z$ . Thus we have shown that Newton's second law implies the three Lagrange equations (in Cartesian coordinates so far):

$$
\frac {\partial \mathcal {L}}{\partial x} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {x}}, \quad \frac {\partial \mathcal {L}}{\partial y} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {y}}, \quad \text { and } \quad \frac {\partial \mathcal {L}}{\partial z} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {z}}.\tag{7.7}
$$

You can easily check that the argument just given works equally well in reverse, so that (for a single particle in Cartesian coordinates, at least) Newton's second law is exactly equivalent to the three Lagrange equations (7.7). The particle's path as determined by Newton's second law is the same as the path determined by the three Lagrange equations.

Our next step is to recognize that the three equations of (7.7) have exactly the form of the Euler–Lagrange equations (6.40). Therefore, they imply that the integral $S = \int L dt$ is stationary for the path followed by the particle. That this integral, called the action integral, is stationary for the particle's path is called Hamilton's principle $^{2}$ (after its inventor, the Irish mathematician, Hamilton, 1805–1865) and can be restated as follows:

## Hamilton's Principle

The actual path which a particle follows between two points 1 and 2 in a given time interval, $t_{1}$ to $t_{2}$ , is such that the action integral

$$
S = \int_ {t _ {1}} ^ {t _ {2}} \mathscr {L} d t\tag{7.8}
$$

is stationary when taken along the actual path.

Although we have so far proved this principle only for a single particle and in Cartesian coordinates, we are going to find that it is valid for a huge class of mechanical systems and for almost any choice of coordinates.

So far we have proved for a single particle that the following three statements are exactly equivalent:

1. A particle's path is determined by Newton's second law $\mathbf{F} = m\mathbf{a}$ .

2. The path is determined by the three Lagrange equations (7.7), at least in Cartesian coordinates.

3. The path is determined by Hamilton's principle.

Hamilton's principle has found generalizations in many fields outside classical mechanics (field theories, for example) and has given a unity to various diverse areas of physics. In the twentieth century it has played an important role in the formulation of quantum theories. However, for our present purposes its great importance is that it lets us prove that Lagrange's equations hold in more-or-less any coordinate system:

Instead of the Cartesian coordinates $\mathbf{r}=(x,y,z)$ , suppose that we wish to use some other coordinates. These could be spherical polar coordinates $(r,\theta,\phi)$ , or cylindrical polars $(\rho,\phi,z)$ , or any set of “generalized coordinates” $q_{1},q_{2},q_{3}$ , with the property that each position r specifies a unique value of $(q_{1},q_{2},q_{3})$ and vice versa; that is,

$$
q _ {i} = q _ {i} (\mathbf {r}) \quad \text {   for   } i = 1, 2, \text {   and   } 3,\tag{7.9}
$$

and

$$
\mathbf {r} = \mathbf {r} (q _ {1}, q _ {2}, q _ {3}).\tag{7.10}
$$

These two equations guarantee that for any value of $\mathbf{r} = (x, y, z)$ there is a unique $(q_1, q_2, q_3)$ and vice versa. Using (7.10) we can rewrite $(x, y, z)$ and $(\dot{x}, \dot{y}, \dot{z})$ in terms of $(q_1, q_2, q_3)$ and $(\dot{q}_1, \dot{q}_2, \dot{q}_3)$ . Next, we can rewrite the Lagrangian $\mathcal{L} = \frac{1}{2} m\dot{\mathbf{r}}^2 - U(\mathbf{r})$ in terms of these new variables as

$$
\mathcal {L} = \mathcal {L} (q _ {1}, q _ {2}, q _ {3}, \dot {q} _ {1}, \dot {q} _ {2}, \dot {q} _ {3})
$$

and the action integral as

$$
S = \int_ {t _ {1}} ^ {t _ {2}} \mathcal {L} (q _ {1}, q _ {2}, q _ {3}, \dot {q} _ {1}, \dot {q} _ {2}, \dot {q} _ {3}) d t.
$$

Now, the value of the integral S is unaltered by this change of variables. Therefore, the statement that S is stationary for variations of the path around the correct path must still be true in our new coordinate system, and, by the results of Chapter 6, this means that the correct path must satisfy the three Euler–Lagrange equations,

$$
\frac {\partial \mathcal {L}}{\partial q _ {1}} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {q} _ {1}}, \qquad \frac {\partial \mathcal {L}}{\partial q _ {2}} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {q} _ {2}}, \qquad \text { and } \qquad \frac {\partial \mathcal {L}}{\partial q _ {3}} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {q} _ {3}},\tag{7.11}
$$

with respect to the new coordinates $q_{1}$ , $q_{2}$ , and $q_{3}$ . Since these new coordinates are any set of generalized coordinates, the qualification “in Cartesian coordinates” can be omitted from the statement (2) above. This result — that Lagrange’s equations have the same form for any choice of generalized coordinates — is one of the two main reasons that the Lagrangian formalism is so useful.

There is one point about our derivation of Lagrange's equations that is worth keeping at the back of your mind. A crucial step in our proof was the observation that (7.6) was equivalent to Newton's second law $F_{x} = \dot{p}_{x}$ , which in turn is true only if the original frame in which we wrote down $\mathcal{L} = T - U$ is inertial. Thus, although

Lagrange's equations are true for any choice of generalized coordinates $q_1, q_2, q_3$ and these generalized coordinates may in fact be the coordinates of a noninertial reference frame—we must nevertheless be careful that, when we first write down the Lagrangian $\mathcal{L} = T - U$ , we do so in an inertial frame.

We can easily generalize Lagrange's equations to systems of many particles, but let us first look at a couple of simple examples.

## EXAMPLE 7.1 One Particle in Two Dimensions; Cartesian Coordinates

Write down Lagrange's equations in Cartesian coordinates for a particle moving in a conservative force field in two dimensions and show that they imply Newton's second law. (Of course, we have already proved this, but it is worth seeing it worked out explicitly.)

The Lagrangian for a single particle in two dimensions is

$$
\mathcal {L} = \mathcal {L} (x, y, \dot {x}, \dot {y}) = T - U = \frac {1}{2} m (\dot {x} ^ {2} + \dot {y} ^ {2}) - U (x, y).\tag{7.12}
$$

To write down the Lagrange equations we need the derivatives

$$
\frac {\partial \mathcal {L}}{\partial x} = - \frac {\partial U}{\partial x} = F _ {x} \quad \text { and } \quad \frac {\partial \mathcal {L}}{\partial \dot {x}} = \frac {\partial T}{\partial \dot {x}} = m \dot {x},\tag{7.13}
$$

with corresponding expressions for the y derivatives. Thus the two Lagrange equations can be rewritten as follows:

$$
\left. \begin{array}{l l l} \frac {\partial \mathcal {L}}{\partial x} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {x}} & \Longleftrightarrow & F _ {x} = m \ddot {x} \\ \frac {\partial \mathcal {L}}{\partial y} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {y}} & \Longleftrightarrow & F _ {y} = m \ddot {y} \end{array} \right\} \Longleftrightarrow \mathbf {F} = m \mathbf {a}.\tag{7.14}
$$

Notice how in (7.13) the derivative $\partial\mathcal{L}/\partial x$ is the x component of the force, and $\partial\mathcal{L}/\partial\dot{x}$ is the x component of the momentum (and similarly with the y components). When we use generalized coordinates $q_{1}, q_{2}, \cdots, q_{n}$ , we shall find that $\partial\mathcal{L}/\partial q_{i}$ , although not necessarily a force component, plays a role very similar to a force. Similarly, $\partial\mathcal{L}/\partial\dot{q}_{i}$ , although not necessarily a momentum component, acts very like a momentum. For this reason we shall call these derivatives the generalized force and generalized momentum respectively; that is,

$$
\frac {\partial \mathcal {L}}{\partial q _ {i}} = (i \text {   th   component   of   generalized   force) }\tag{7.15}
$$

and

$$
\frac {\partial \mathcal {L}}{\partial \dot {q} _ {i}} = (i \text {   th   component   of   generalized   momentum }).\tag{7.16}
$$

With these notations, each of the Lagrange equations (7.11)

$$
\frac {\partial \mathcal {L}}{\partial q _ {i}} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {q} _ {i}}
$$

takes the form

$$
(\text { generalized   force }) = (\text { rate   of   change   of   generalized   momentum })\tag{7.17}
$$

I shall illustrate these ideas in the next example.

## EXAMPLE 7.2 One Particle in Two Dimensions; Polar Coordinates

Find Lagrange's equations for the same system, a particle moving in two dimensions, using polar coordinates.

As in all problems in Lagrangian mechanics, our first task is to write down the Lagrangian $L = T - U$ in terms of the chosen coordinates. In this case we have been told to use polar coordinates, as sketched in Figure 7.1. This means the components of the velocity are $v_{r} = \dot{r}$ and $v_{\phi} = r\dot{\phi}$ , and the kinetic energy is $T = \frac{1}{2}mv^{2} = \frac{1}{2}m(\dot{r}^{2} + r^{2}\dot{\phi}^{2})$ . Therefore, the Lagrangian is

$$
\mathcal {L} = \mathcal {L} (r, \phi , \dot {r}, \dot {\phi}) = T - U = \frac {1}{2} m (\dot {r} ^ {2} + r ^ {2} \dot {\phi} ^ {2}) - U (r, \phi).\tag{7.18}
$$

Given the Lagrangian, we now have only to write down the two Lagrange equations, one involving derivatives with respect to r and the other derivatives with respect to $\phi$ .

## The r Equation

The equation involving derivatives with respect to r (the r equation) is

$$
\frac {\partial \mathcal {L}}{\partial r} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {r}}
$$

or

$$
m r \dot {\phi} ^ {2} - \frac {\partial U}{\partial r} = \frac {d}{d t} (m \dot {r}) = m \ddot {r}.\tag{7.19}
$$

Since $-\partial U/\partial r$ is just $F_{r}$ , the radial component of F, we can rewrite the r equation as

$$
F _ {r} = m (\ddot {r} - r \dot {\phi} ^ {2}),\tag{7.20}
$$

![](images/f3fdcf5afb2b5c7ae1186b1a9d4de94e3af5708229219ba6fe03d08da5846690.jpg)  
Figure 7.1 The velocity of a particle expressed in two-dimensional polar coordinates.

which you should recognize as $F_{r}=ma_{r}$ , the r component of F=ma, first derived in Equation (1.48). (The term $-r\dot{\phi}^{2}$ is the infamous centripetal acceleration.) That is, when we use polar coordinates $(r,\phi)$ , the Lagrange equation corresponding to r is just the radial component of Newton's second law. (Note, however, that the Lagrangian derivation avoided the tedious calculation of the components of the acceleration.) As we shall see directly, the $\phi$ equation works a bit differently and illustrates a remarkable feature of the Lagrangian approach.

## The $\phi$ Equation

The Lagrange equation for the coordinate $\phi$ is

$$
\frac {\partial \mathcal {L}}{\partial \phi} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {\phi}}\tag{7.21}
$$

or, substituting (7.18) for L,

$$
- \frac {\partial U}{\partial \phi} = \frac {d}{d t} (m r ^ {2} \dot {\phi}).\tag{7.22}
$$

To interpret this equation, we need to relate the left side to the appropriate component of the force $F = -\nabla U$ . This requires that we know the components of $\nabla U$ in polar coordinates:

$$
\nabla U = \frac {\partial U}{\partial r} \hat {\mathbf {r}} + \frac {1}{r} \frac {\partial U}{\partial \phi} \hat {\boldsymbol {\phi}}.\tag{7.23}
$$

(If you don't remember this, see Problem 7.5.) The $\phi$ component of the force is just the coefficient of $\hat{\phi}$ in $\mathbf{F} = -\nabla U$ , that is,

$$
F _ {\phi} = - \frac {1}{r} \frac {\partial U}{\partial \phi}.
$$

Thus the left side of (7.22) is $rF_{\phi}$ , which is simply the torque $\Gamma$ on the particle about the origin. Meanwhile, the quantity $mr^{2}\dot{\phi}$ on the right can be recognized as the angular momentum L about the origin. Therefore, the $\phi$ equation (7.22) states that

$$
\Gamma = \frac {d L}{d t},\tag{7.24}
$$

the familiar condition from elementary mechanics, that torque equals the rate of change of angular momentum.

The result (7.24) illustrates a wonderful feature of Lagrange's equations, that when we choose an appropriate set of generalized coordinates the corresponding Lagrange equations automatically appear in a corresponding, natural form. When we choose $r$ and $\phi$ for our coordinates, the $\phi$ equation turns out to be the equation for angular momentum. In fact, the situation is even better than this. Recall that I introduced the notion of generalized force and generalized momentum in (7.15) and (7.16). In the present case, the $\phi$ component of the generalized force is just the torque,

$$
(\phi \text {   component   of   generalized   force   }) = \frac {\partial \mathcal {L}}{\partial \phi} = \Gamma (\text { torque })\tag{7.25}
$$

and the corresponding component of the generalized momentum is

$$
(\phi \text {   component   of   generalized   momentum }) = \frac {\partial \mathcal {L}}{\partial \dot {\phi}} = L (\text { angular   momentum }).\tag{7.26}
$$

With the “natural” choice for the coordinates $(r \text{ and } \phi)$ the $\phi$ components of the generalized force and momentum turn out to be the corresponding “natural” quantities, the torque and the angular momentum.

Notice that the generalized “force” does not necessarily have the dimensions of force, nor the generalized “momentum” those of momentum. In the present case, the generalized force ( $\phi$ component) is a torque (that is, force $\times$ distance) and the generalized momentum is an angular momentum (momentum $\times$ distance).

This example illustrates another feature of Lagrange's equations: The $\phi$ component $\partial \mathcal{L} / \partial \phi$ of the generalized force turned out to be the torque on the particle. If the torque happens to be zero, then the corresponding generalized momentum $\partial \mathcal{L} / \partial \dot{\phi}$ (the angular momentum, in this case) is conserved. Clearly this is a general result: The $i$ th component of the generalized force is $\partial \mathcal{L} / \partial q_i$ . If this happens to be zero, then the Lagrange equation

$$
\frac {\partial \mathcal {L}}{\partial q _ {i}} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {q} _ {i}}
$$

says simply that the $i$ th component $\partial \mathcal{L} / \partial q_i$ of the generalized momentum is constant. That is, if $\mathcal{L}$ is independent of $q_i$ , the $i$ th component of the generalized force is zero, and the corresponding component of the generalized momentum is conserved. In practice, it is often easy to spot that a Lagrangian is independent of a coordinate $q_i$ , and, if you can, then you immediately know a corresponding conservation law. We shall return to this point in Section 7.8.

## Several Unconstrained Particles

The extension of the above ideas to a system of $N$ unconstrained particles (a gas of $N$ molecules, for instance) is very straightforward, and I shall leave you to fill in the details (Problems 7.6 and 7.7). Here I shall just sketch the argument for the case of two particles, mainly to show the form of Lagrange's equations for $N > 1$ . For two particles, the Lagrangian is defined (exactly as before) as $\mathcal{L} = T - U$ , but this now means that

$$
\mathcal {L} (\mathbf {r} _ {1}, \mathbf {r} _ {2}, \dot {\mathbf {r}} _ {1}, \dot {\mathbf {r}} _ {2}) = \frac {1}{2} m _ {1} \dot {\mathbf {r}} _ {1} ^ {2} + \frac {1}{2} m _ {2} \dot {\mathbf {r}} _ {2} ^ {2} - U (\mathbf {r} _ {1}, \mathbf {r} _ {2}).\tag{7.27}
$$

As usual, the forces on the two particles are $\mathbf{F}_1 = -\nabla_1U$ and $\mathbf{F}_2 = -\nabla_2U$ . Newton's second law can be applied to each particle and yields six equations,

$$
F _ {1 x} = \dot {p} _ {1 x}, \qquad F _ {1 y} = \dot {p} _ {1 y}, \qquad \dots , \qquad F _ {2 z} = \dot {p} _ {2 z}.
$$

Exactly as in Equation (7.7), each of these six equations is equivalent to a corresponding Lagrange equation

$$
\frac {\partial \mathcal {L}}{\partial x _ {1}} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {x} _ {1}}, \quad \frac {\partial \mathcal {L}}{\partial y _ {1}} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {y} _ {1}}, \quad \dots , \quad \frac {\partial \mathcal {L}}{\partial z _ {2}} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {z} _ {2}}.\tag{7.28}
$$

These six equations imply that the integral $S = \int_{t_{1}}^{t_{2}} L dt$ is stationary. Finally, we can change to any other suitable set of six coordinates $q_{1}, q_{2}, \cdots, q_{6}$ . The statement that S is stationary must also be true in this new coordinate system, and this implies in turn that Lagrange's equations must be true with respect to the new coordinates:

$$
\frac {\partial \mathcal {L}}{\partial q _ {1}} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {q} _ {1}}, \quad \frac {\partial \mathcal {L}}{\partial q _ {2}} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {q} _ {2}}, \quad \dots , \quad \frac {\partial \mathcal {L}}{\partial q _ {6}} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {q} _ {6}}.\tag{7.29}
$$

An example of a set of six such generalized coordinates that we shall use repeatedly in Chapter 8 is this: In place of the six coordinates of $\mathbf{r}_1$ and $\mathbf{r}_2$ , we could use the three coordinates of the CM position $\mathbf{R} = (m_1\mathbf{r}_1 + m_2\mathbf{r}_2) / (m_1 + m_2)$ and the three coordinates of the relative position $\mathbf{r} = \mathbf{r}_1 - \mathbf{r}_2$ . We shall find that this choice of coordinates leads to a dramatic simplification. For now, the main point is simply that Lagrange's equations are automatically true in their standard form (7.29) with respect to these new, generalized coordinates.

The extension of these ideas to the case of $N$ unconstrained particles is entirely straightforward, and I leave it for you to check. (See Problem 7.7.) The upshot is that there are $3N$ Lagrange equations

$$
\frac {\partial \mathcal {L}}{\partial q _ {i}} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {q} _ {i}}, \quad [ i = 1, 2, \dots , 3 N ],
$$

valid for any choice of the 3N coordinates $q_{1}, \cdots, q_{3N}$ needed to describe the N particles.

## 7.2 Constrained Systems; an Example

Perhaps the greatest advantage of the Lagrangian approach is that it can handle systems that are constrained so that they cannot move arbitrarily in the space that they occupy. A familiar example of a constrained system is the bead which is threaded on a wire — the bead can move along the wire, but not anywhere else. Another example of a very constrained system is a rigid body, whose individual atoms can only move in such a way that the distance between any two atoms is fixed. Before I discuss the nature of constraints in general, I shall discuss another simple example, the plane pendulum.

Consider the simple pendulum shown in Figure 7.2. A bob of mass m is fixed to a massless rod, which is pivoted at O and free to swing without friction in the xy plane. The bob moves in both the x and y directions, but it is constrained by the rod so that $\sqrt{x^{2} + y^{2}} = l$ remains constant. In an obvious sense, only one of the coordinates is independent (as x changes, the variation of y is predetermined by the constraint equation), and we say that the system has only one degree of freedom. One way to express this would be to eliminate one of the coordinates, for instance by writing $y = \sqrt{l^{2} - x^{2}}$ and expressing everything in terms of the one coordinate $x$ . Although this is a perfectly legitimate way to proceed, a simpler way is to express both $x$ and $y$ in terms of the single parameter $\phi$ , the angle between the pendulum and its equilibrium position, as shown in Figure 7.2.

![](images/51def9e0ee35f073a16607633f56394873af344f6c3840beb10a0b1ae5933e62.jpg)  
Figure 7.2 A simple pendulum. The bob of mass m is constrained by the rod to remain at distance l from O.

We can express all the quantities of interest in terms of $\phi$ . The kinetic energy is $T = \frac{1}{2}mv^{2} = \frac{1}{2}ml^{2}\dot{\phi}^{2}$ . The potential energy is U = mgh where h denotes the height of the bob above its equilibrium position and is (as you should check) $h = l(1 - \cos\phi)$ . Thus the potential energy is $U = mgl(1 - \cos\phi)$ , and the Lagrangian is

$$
\mathcal {L} = T - U = \frac {1}{2} m l ^ {2} \dot {\phi} ^ {2} - m g l (1 - \cos \phi).\tag{7.30}
$$

Whichever way we choose to proceed — to write everything in terms of x (or y) or $\phi$ — the Lagrangian is expressed in terms of a single generalized coordinate q and its time derivative $\dot{q}$ , in the form $\mathcal{L} = \mathcal{L}(q, \dot{q})$ . Now, it is a fact (which I shall not prove just yet) that once the Lagrangian is written in terms of this one variable (for a system with one degree of freedom), the evolution of the system again satisfies Lagrange's equation (just as we proved for an unconstrained particle in the previous section.) That is,

$$
\frac {\partial \mathcal {L}}{\partial q} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {q}}.\tag{7.31}
$$

If we choose the angle $\phi$ as our generalized coordinate, then Lagrange's equation reads

$$
\frac {\partial \mathcal {L}}{\partial \phi} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {\phi}}.\tag{7.32}
$$

The Lagrangian $\mathcal{L}$ is given by (7.30), and the needed derivatives are easily evaluated to give

$$
- m g l \sin \phi = \frac {d}{d t} (m l ^ {2} \dot {\phi}) = m l ^ {2} \ddot {\phi}.\tag{7.33}
$$

Referring to Figure 7.2 you can see that the left side of this equation is just the torque $\Gamma$ exerted by gravity on the pendulum, while the term $ml^2$ is the pendulum's moment of inertia $I$ . Since $\ddot{\phi}$ is the angular acceleration $\alpha$ , we see that Lagrange's equation for the simple pendulum simply reproduces the familiar result $\Gamma = I\alpha$ .

## 7.3 Constrained Systems in General

## Generalized Coordinates

Consider now an arbitrary system of N particles, $\alpha = 1, \cdots, N$ with positions $r_{\alpha}$ . We say that the parameters $q_{1}, \cdots, q_{n}$ are a set of generalized coordinates for the system if each position $r_{\alpha}$ can be expressed as a function of $q_{1}, \cdots, q_{n}$ , and possibly the time t,

$$
\mathbf {r} _ {\alpha} = \mathbf {r} _ {\alpha} (q _ {1}, \dots , q _ {n}, t) \quad [ \alpha = 1, \dots , N ],\tag{7.34}
$$

and conversely each $q_{i}$ can be expressed in terms of the $r_{\alpha}$ and possibly t,

$$
q _ {i} = q _ {i} (\mathbf {r} _ {1}, \dots , \mathbf {r} _ {N}, t) \qquad [ i = 1, \dots , n ].\tag{7.35}
$$

In addition, we require that the number of the generalized coordinates $(n)$ is the smallest number that allows the system to be parametrized in this way. In our three-dimensional world, the number n of generalized coordinates for N particles is certainly no more than 3N and, for a constrained system, is usually less — sometimes dramatically so. For example, for a rigid body, the number of particles N may be of order $10^{23}$ , whereas the number of generalized coordinates n is 6 (three coordinates to give the position of the center of mass and three to give the orientation of the body).

To illustrate the relation (7.34), consider again the simple pendulum of Figure 7.2. There is one particle (the bob) and two Cartesian coordinates (since the pendulum is restricted to two dimensions). As we saw, there is just one generalized coordinate, which we took to be the angle $\phi$ . The analog of (7.34) is

$$
\mathbf {r} \equiv (x, y) = (l \sin \phi , l \cos \phi)\tag{7.36}
$$

and expresses the two Cartesian coordinates $x$ and $y$ in terms of the one generalized coordinate $\phi$ .

The double pendulum shown in Figure 7.3 has two bobs, both confined to a plane, so it has four Cartesian coordinates, all of which can be expressed in terms of the two generalized coordinates $\phi_{1}$ and $\phi_{2}$ . Specifically, if we put our origin at the suspension point of the top pendulum,

$$
\mathbf {r} _ {1} = (l _ {1} \sin \phi_ {1}, l _ {1} \cos \phi_ {1}) = \mathbf {r} _ {1} (\phi_ {1})\tag{7.37}
$$

and

$$
\mathbf {r} _ {2} = (l _ {1} \sin \phi_ {1} + l _ {2} \sin \phi_ {2}, l _ {1} \cos \phi_ {1} + l _ {2} \cos \phi_ {2}) = \mathbf {r} _ {2} (\phi_ {1}, \phi_ {2}).\tag{7.38}
$$

Notice that the components of $r_{2}$ depend on $\phi_{1}$ and $\phi_{2}$ .

![](images/a99701bad52bfe9526f6525dbde65034e35e6d8818e128b0f9a2d0e7e731ea31.jpg)  
Figure 7.3 The positions of both masses in a double pendulum are uniquely specified by the two generalized coordinates $\phi_{1}$ and $\phi_{2}$ , which can themselves be varied independently.

In these two examples, the transformation between the Cartesian and the generalized coordinates did not depend on the time t, but it is easy to think of examples in which it does. Consider the railroad car shown in Figure 7.4, which has a pendulum suspended from its ceiling and is being forced $^{3}$ to accelerate with a fixed acceleration a. It is natural to specify the position of the pendulum by the angle $\phi$ as usual, but we must recognize that, in the first instance, this gives the pendulum's position relative to the accelerating, and hence non-inertial, reference frame of the car. If we wish to specify the bob's position relative to an inertial frame, we can choose a frame fixed relative to the ground, and we can easily express the position relative to this inertial frame in terms of the angle $\phi$ . The position of the point of suspension relative to the ground is (if we choose our axes and origin properly) just $x_{s} = \frac{1}{2} at^{2}$ , and the position of the bob is then easily seen to be

$$
\mathbf {r} \equiv (x, y) = (l \sin \phi + \frac {1}{2} a t ^ {2}, l \cos \phi) = \mathbf {r} (\phi , t).\tag{7.39}
$$

![](images/ac28ad29bb5df306da86418e17d3a4b91c76862be8cb3a871fa88ff7a03cef01.jpg)  
Figure 7.4 A pendulum is suspended from the roof of a railroad car that is being forced to accelerate with a fixed, known acceleration a.

The relation between r and the generalized coordinate $\phi$ depends on the time t, a possibility that I allowed for when writing (7.34).

We shall sometimes describe a set of coordinates $q_{1}, \cdots, q_{n}$ as natural if the relation (7.34) between the Cartesian coordinates $r_{\alpha}$ and the generalized coordinates does not involve the time t. We shall find certain convenient properties of natural coordinates that do not generally apply to coordinates for which (7.34) does involve the time. Fortunately, as the name implies, there are many problems for which the most convenient choice of coordinates is also natural. $^{4}$

## Degrees of Freedom

The number of degrees of freedom of a system is the number of coordinates that can be independently varied in a small displacement — the number of independent “directions” in which the system can move from any given initial configuration. For example, the simple pendulum of Figure 7.2 has just one degree of freedom, while the double pendulum of Figure 7.3 has two. A particle that is free to move anywhere in three dimensions has three degrees of freedom, while a gas comprised of N particles has 3N.

When the number of degrees of freedom of an N-particle system in three dimensions is less than 3N, we say that the system is constrained. (In two dimensions, the corresponding number is 2N of course.) The bob of a simple pendulum, with one degree of freedom, is constrained. The two masses of a double pendulum, with two degrees of freedom, are constrained. The N atoms of a rigid body have just six degrees of freedom and are certainly constrained. Other examples are a bead constrained to slide on a fixed wire and a particle constrained to move on a fixed surface in three dimensions.

In all of the examples I have given so far, the number of degrees of freedom was equal to the number of generalized coordinates needed to describe the system's configuration. (The double pendulum has two degrees of freedom and needs two generalized coordinates, and so on.) A system with this natural-seeming property is said to be holonomic. $^{5}$ That is, a holonomic system has n degrees of freedom and can be described by n generalized coordinates, $q_{1}, \cdots, q_{n}$ . Holonomic systems are easier to treat than nonholonomic, and in this book I shall restrict myself to holonomic systems.

You might imagine that all systems would be holonomic, or at least that nonholonomic systems would be rare and bizarrely complicated. In fact, there are some quite simple examples of nonholonomic systems. Consider, for instance, a hard rubber ball that is free to roll (but not to slide nor to spin about a vertical axis) on a horizontal table. Starting at any position $(x, y)$ it can move in only two independent directions. Therefore, the ball has two degrees of freedom, and you might well imagine that its configuration could be uniquely specified by two coordinates, x and y, of its center. But consider the following: Let us place the ball at the origin O and make a mark on its top point. Now, carry out the following three moves. (See Figure 7.5.) Roll the ball along the x axis for a distance equal to the circumference c, to a point P, where the mark will once again be on the top. Now roll it the same distance c in the y direction to Q, where the mark is again on top. Finally roll it straight back to the origin along the hypotenuse of the triangle OPQ. Since this last move has length $\sqrt{2}c$ , it brings the ball back to its starting point, but with the mark no longer on the top. The position $(x, y)$ has returned to its initial value, but the ball now has a different orientation. Evidently the two coordinates $(x, y)$ are not enough to specify a unique configuration. In fact, three more numbers are needed to specify the orientation of the ball, and we need five coordinates in all to specify the configuration completely. The ball has two degrees of freedom but needs five generalized coordinates. Evidently it is a nonholonomic system.

![](images/16d4ce11d7ff10453b563a491df3807907ef02bef183b49d424f91f0fc6888e4.jpg)  
Figure 7.5 The right triangle OPQ lies in the xy plane with sides OP and PQ of length c. If you roll a ball of circumference c around OPQ, it will return to its starting point with a changed orientation.

Although nonholonomic systems certainly exist, they are more complicated to analyze than holonomic systems, and I shall not discuss them further. For any holonomic system with generalized coordinates $q_{1}, \cdots, q_{n}$ and potential energy $U(q_{1}, \cdots, q_{n}, t)$ (which may depend on the time t as described in Section 4.5), the evolution in time is determined by the n Lagrange equations

$$
\frac {\partial \mathcal {L}}{\partial q _ {i}} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {q} _ {i}} \quad [ i = 1, \dots , n ],\tag{7.40}
$$

where the Lagrangian L is defined as usual to be $L = T - U$ . I shall prove this result in Section 7.4.

## 7.4 Proof of Lagrange's Equations with Constraints

We are now ready to prove Lagrange's equations for any holonomic system. To keep things reasonably simple, I shall treat explicitly the case that there is just one particle. (The generalization to arbitrary numbers of particles is fairly straightforward — see

Problem 7.13.) To be definite, I shall suppose the particle is constrained to move on a surface. $^{6}$ This means that it has two degrees of freedom and can be described by two generalized coordinates $q_{1}$ and $q_{2}$ that can vary independently.

We must recognize that there are two kinds of forces on the particle (or particles, in the general case). First, there are the forces of constraint: For a bead on a wire the constraining force is the normal force of the wire on the bead; for our particle, constrained to move on a surface, it is the normal force of the surface. For the atoms in a rigid body, the constraining forces are the interatomic forces that hold the atoms in place within the body. In general, the forces of constraint are not necessarily conservative, but this doesn't matter. One of the objectives of the Lagrangian approach is to find equations that do not involve the constraining forces, which we usually don't want to know anyway. (Notice, however, that if the constraining forces are nonconservative, Lagrange's equations in the simple unconstrained form of Section 7.1 certainly do not apply.) I shall denote the net constraining force on the particle by $\mathbf{F}_{\mathrm{estr}}$ , which in our case is just the normal force of the surface to which the particle is confined.

Second, there are all the other “nonconstraint” forces on the particle, such as gravity. These are the forces with which we are usually concerned in practice, and I shall denote their resultant by F. I shall assume that the nonconstraint forces all satisfy at least the second condition for conservatism, so that they are derivable from a potential energy, $U(\mathbf{r}, t)$ , and

$$
\mathbf {F} = - \nabla U (\mathbf {r}, t).\tag{7.41}
$$

(If all the nonconstraint forces are actually conservative, then $U$ is independent of $t$ , but we don't need to assume this.) The total force on our particle is $\mathbf{F}_{\mathrm{tot}} = \mathbf{F}_{\mathrm{cstr}} + \mathbf{F}$ .

Finally, I shall define the Lagrangian, as usual, to be

$$
\mathcal {L} = T - U.\tag{7.42}
$$

Since $U$ is the potential energy for the nonconstraint forces only, this definition of $\mathcal{L}$ excludes the constraint forces. This correctly reflects that Lagrange's equations for a constrained system cleverly eliminate the constraint forces, as we shall see.

## The Action Integral is Stationary at the Right Path

Consider any two points $r_{1}$ and $r_{2}$ through which the particle passes at times $t_{1}$ and $t_{2}$ . I shall denote by $\mathbf{r}(t)$ the “right” path, the actual path that our particle follows between the two points, and by $\mathbf{R}(t)$ any neighboring “wrong” path between the same two points. It is convenient to write

$$
\mathbf {R} (t) = \mathbf {r} (t) + \boldsymbol {\epsilon} (t),\tag{7.43}
$$

which defines $\epsilon(t)$ as the infinitesimal vector pointing from $\mathbf{r}(t)$ on the right path to the corresponding point $\mathbf{R}(t)$ on the wrong path. Since I shall assume that both of the points $\mathbf{r}(t)$ and $\mathbf{R}(t)$ lie in the surface to which the particle is confined, the vector $\epsilon(t)$ is contained in the same surface. Since both $\mathbf{r}(t)$ and $\mathbf{R}(t)$ go through the same endpoints, $\epsilon(t)=0$ at $t_{1}$ and $t_{2}$ .

Let us denote by S the action integral

$$
S = \int_ {t _ {1}} ^ {t _ {2}} \mathcal {L} (\mathbf {R}, \dot {\mathbf {R}}, t) d t,\tag{7.44}
$$

taken along any path $\mathbf{R}(t)$ lying in the constraining surface, and by $S_{0}$ the corresponding integral taken along the right path $\mathbf{r}(t)$ . As I shall now prove, the integral S is stationary for variations of the path $\mathbf{R}(t)$ , when $\mathbf{R}(t)=\mathbf{r}(t)$ or, equivalently, when the difference $\epsilon$ is zero. Another way to say this is that the difference in the action integrals

$$
\delta S = S - S _ {0}\tag{7.45}
$$

is zero to first order in the distance $\epsilon$ between the paths, and this is what I shall prove.

The difference (7.45) is the integral of the difference between the Lagrangians on the two paths,

$$
\delta \mathcal {L} = \mathcal {L} (\mathbf {R}, \dot {\mathbf {R}}, t) - \mathcal {L} (\mathbf {r}, \dot {\mathbf {r}}, t).\tag{7.46}
$$

If we substitute $\mathbf{R}(t) = \mathbf{r}(t) + \epsilon(t)$ and

$$
\mathcal {L} (\mathbf {r}, \dot {\mathbf {r}}, t) = T - U = \frac {1}{2} m \dot {\mathbf {r}} ^ {2} - U (\mathbf {r}, t),
$$

this becomes $^{7}$

$$
\begin{array}{l} \delta \mathcal {L} = \frac {1}{2} m \left[ (\dot {\mathbf {r}} + \dot {\boldsymbol {\epsilon}}) ^ {2} - \dot {\mathbf {r}} ^ {2} \right] - [ U (\mathbf {r} + \boldsymbol {\epsilon}, t) - U (\mathbf {r}, t) ] \\ = m \dot {\mathbf {r}} \cdot \dot {\boldsymbol {\epsilon}} - \boldsymbol {\epsilon} \cdot \nabla U + O (\boldsymbol {\epsilon} ^ {2}), \end{array}
$$

where $O(\epsilon^{2})$ denotes terms involving squares and higher powers of $\epsilon$ and $\dot{\epsilon}$ . Returning to the difference (7.45) in the two action integrals, we find that, to first order in $\epsilon$ ,

$$
\delta S = \int_ {t _ {1}} ^ {t _ {2}} \delta \mathcal {L} d t = \int_ {t _ {1}} ^ {t _ {2}} [ m \dot {\mathbf {r}} \cdot \dot {\boldsymbol {\epsilon}} - \boldsymbol {\epsilon} \cdot \nabla U ] d t.\tag{7.47}
$$

The first term in the final integral can be integrated by parts. (Recall that this just means moving the time derivative from one factor to the other and changing the sign.) The difference $\epsilon$ is zero at the two endpoints, so the endpoint contribution is zero, and we get

$$
\delta S = - \int_ {t _ {1}} ^ {t _ {2}} \epsilon \cdot [ m \ddot {\mathbf {r}} + \nabla U ] d t.\tag{7.48}
$$

Now, the path $\mathbf{r}(t)$ is the “right” path and satisfies Newton’s second law. Therefore the term $m\ddot{r}$ is just the total force on the particle, $F_{tot} = F_{cstr} + F$ . Meanwhile $\nabla U = -F$ . Therefore, the second term in (7.48) cancels the second piece of the first, and we are left with

$$
\delta S = - \int_ {t _ {1}} ^ {t _ {2}} \boldsymbol {\epsilon} \cdot \mathbf {F} _ {\mathrm{cstr}} d t.\tag{7.49}
$$

But the constraint force $F_{cstr}$ is normal to the surface in which our particle moves, while $\epsilon$ lies in the surface. Therefore $\epsilon \cdot F_{cstr} = 0$ , and we have proved that $\delta S = 0$ . That is, the action integral is stationary at the right path, as claimed. $^{8}$

## The Final Proof

We have proved Hamilton's principle, that the action integral is stationary at the path which the particle actually follows. However, we have proved it, not for arbitrary variations of the path, but rather for those variations of path that are consistent with the constraints—that is, paths which lie in the surface to which our particle is constrained. This means that we cannot prove Lagrange's equations with respect to the three Cartesian coordinates. On the other hand, we can prove them with respect to the appropriate generalized coordinates. We are assuming that our particle is confined by holonomic constraints to move on a surface, that is, a two-dimensional subset of the full three-dimensional world. This means that the particle has two degrees of freedom and can be described by two generalized coordinates, $q_1$ and $q_2$ , that can be varied independently. Any variation of $q_1$ and $q_2$ is consistent with the constraints. $^9$ Accordingly, we can rewrite the action integral in terms of $q_1$ and $q_2$ as

$$
S = \int_ {t _ {1}} ^ {t _ {2}} \mathcal {L} (q _ {1}, q _ {2}, \dot {q} _ {1}, \dot {q} _ {2}, t) d t,\tag{7.50}
$$

and this integral is stationary for any variations of $q_{1}$ and $q_{2}$ about the correct path $[q_{1}(t), q_{2}(t)]$ . Therefore, by the argument of Chapter 6 the correct path must satisfy the two Lagrange equations

$$
\frac {\partial \mathcal {L}}{\partial q _ {1}} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {q} _ {1}} \qquad \text { and } \qquad \frac {\partial \mathcal {L}}{\partial q _ {2}} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {q} _ {2}}  .\tag{7.51}
$$

The proof that I have given here applies directly only to a single particle in three dimensions, constrained to move on a two-dimensional surface, but the main ideas of the general case are all present. The generalization is, for the most part, relatively straightforward (see Problem 7.13), and meanwhile I hope that I have said enough to convince you of the truth of the general result: For any holonomic system, with n degrees of freedom and n generalized coordinates, and with the nonconstraint forces derivable from a potential energy $U(q_{1},\cdots,q_{n},t)$ , the path followed by the system is determined by the n Lagrange equations

$$
\frac {\partial \mathcal {L}}{\partial q _ {i}} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {q} _ {i}} \qquad [ i = 1, \dots , n ],\tag{7.52}
$$

where L is the Lagrangian $L = T - U$ and $U = U(q_{1}, \cdots, q_{n}, t)$ is the total potential energy corresponding to all the forces excluding the forces of constraint.

It was essential to our proof of Lagrange's equations that the nonconstraint forces be conservative (or, at a minimum, that they satisfy the second condition for conservatism) so that they are derivable from a potential energy, $F = -\nabla U$ . If this is not true, then Lagrange's equations may not hold, at least in the form (7.52). An obvious example of a force that does not satisfy this condition is sliding friction. Sliding friction cannot be regarded as a force of constraint (it is not normal to the surface) and cannot be derived from a potential energy. Thus, when sliding friction is present, Lagrange's equations do not hold in the form (7.52). Lagrange's equations can be modified to include forces like friction (see Problem 7.12), but the result is clumsy and I shall confine myself to situations where the equations (7.52) do hold.

## 7.5 Examples of Lagrange's Equations

In this section I present five examples of the use of Lagrange's equations. The first two are sufficiently simple that they can be easily solved within the Newtonian formalism. My main purpose for including them is just to give you experience with using the Lagrangian approach. Nevertheless, even these simple cases show some advantages of the Lagrangian over the Newtonian formalism; in particular, we shall see how the Lagrangian approach obviates any need to consider the forces of constraint. The last three examples are sufficiently complex that solution using the Newtonian approach requires considerable ingenuity; by contrast, the Lagrangian approach lets us write down the equations of motion almost without thinking.

The examples given here illustrate an important point to recognize about Lagrange's equations: The Lagrangian formalism always (or nearly always) gives a straightforward means of writing down the equations of motion. On the other hand, it cannot guarantee that the resulting equations are easy to solve. If we are very lucky, the equations of motion may have an analytic solution, but, even when they do not, they are the essential first step to understanding the solutions and they often suggest a starting point for an approximate solution. The equations of motion can give simple answers to certain subsidiary questions. (For instance, once we have the equations of motion, we can usually find the positions of equilibrium of a system very easily.) And we can always solve the equations of motion numerically for given initial conditions.

The Lagrangian method is so important that it certainly deserves more than just five examples. However, the crucial thing is that you work through several examples yourself; therefore I have given plenty of problems at the end of the chapter, and it is essential that you work several of these as soon as possible after reading this section.

## EXAMPLE 7.3 Atwood's Machine

Consider the Atwood machine first met in Figure 4.15 and shown again in Figure 7.6, in which the two masses $m_{1}$ and $m_{2}$ are suspended by an inextensible string (length l) which passes over a massless pulley with frictionless bearings and radius R. Write down the Lagrangian L, using the distance x as generalized coordinate, find the Lagrange equation of motion, and solve it for the acceleration $\ddot{x}$ . Compare your results with the Newtonian solution.

Because the string has fixed length, the heights x and y of the two masses cannot vary independently. Rather, $x + y + \pi R = l$ , the length of the string, so that y can be expressed in terms of x as

$$
y = - x + \text { const }.\tag{7.53}
$$

Therefore, we can use $x$ as our one generalized coordinate. From (7.53) we see that $\dot{y} = -\dot{x}$ , so that the kinetic energy of the system is

$$
T = \frac {1}{2} m _ {1} \dot {x} ^ {2} + \frac {1}{2} m _ {2} \dot {y} ^ {2} = \frac {1}{2} (m _ {1} + m _ {2}) \dot {x} ^ {2},
$$

![](images/58cdc1c9dd86a8f79d4293198375dda14d0adf1a0bf0f9b388cc6380dd1990f0.jpg)  
Figure 7.6 An Atwood machine consisting of two masses, $m_1$ and $m_2$ , suspended by a massless inextensible string that passes over a massless, frictionless pulley of radius $R$ . Because the string's length is fixed, the position of the whole system can be specified by a single variable, which we can take to be the distance $x$ .

while the potential energy is

$$
U = - m _ {1} g x - m _ {2} g y = - (m _ {1} - m _ {2}) g x + \mathrm{const.}
$$

Combining these, we find the Lagrangian

$$
\mathcal {L} = T - U = \frac {1}{2} (m _ {1} + m _ {2}) \dot {x} ^ {2} + (m _ {1} - m _ {2}) g x,\tag{7.54}
$$

where I have dropped an uninteresting constant.

The Lagrange equation of motion is just

$$
\frac {\partial \mathcal {L}}{\partial x} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {x}}
$$

or, substituting (7.54) for L,

$$
(m _ {1} - m _ {2}) g = (m _ {1} + m _ {2}) \ddot {x},\tag{7.55}
$$

which we can solve at once to give the desired acceleration

$$
\ddot {x} = \frac {m _ {1} - m _ {2}}{m _ {1} + m _ {2}} g.\tag{7.56}
$$

By choosing $m_{1}$ and $m_{2}$ fairly close together, one can make this acceleration much less than g, and hence much easier to measure. Therefore, the Atwood machine gave an early and reasonably accurate method for measuring g.

The corresponding Newtonian solution requires us to write down Newton's second law for each of the masses separately. The net force on $m_1$ is $m_1g - F_t$ where $F_t$ is the tension in the string. (This is the force of constraint and needed no consideration in the Lagrangian solution.) Thus Newton's second law for $m_1$ is

$$
m _ {1} g - F _ {\mathrm{t}} = m _ {1} \ddot {x}.
$$

In the same way, Newton's second law for $m_2$ reads

$$
F _ {\mathrm{t}} - m _ {2} g = m _ {2} \ddot {x}.
$$

(Remember that the upward acceleration of $m_{2}$ is the same as the downward acceleration of $m_{1}$ .) We see that the Newtonian approach has given us two equations for two unknowns, the required acceleration $\ddot{x}$ and the force of constraint $F_{t}$ . By adding these two equations, we can eliminate $F_{t}$ and arrive at precisely the equation (7.55) of the Lagrangian method and thence the same value (7.56) for $\ddot{x}$ .

The Newtonian solution of the Atwood machine is too simple for us to get very excited by an alternative solution. Nevertheless, this simple example does illustrate how the Lagrangian approach allows us to ignore the unknown (and usually uninteresting) force of constraint and to eliminate at least one step of the Newtonian solution.

## EXAMPLE 7.4 A Particle Confined to Move on a Cylinder

Consider a particle of mass m constrained to move on a frictionless cylinder of radius R, given by the equation $\rho = R$ in cylindrical polar coordinates $(\rho, \phi, z)$ , as shown in Figure 7.7. Besides the force of constraint (the normal force of the cylinder), the only force on the mass is a force F = -kr directed toward the origin. (This is the three dimensional version of the Hooke's-law force.) Using z and $\phi$ as generalized coordinates, find the Lagrangian L. Write down and solve Lagrange's equations and describe the motion.

Since the particle's coordinate $\rho$ is fixed at $\rho = R$ , we can specify its position by giving just $z$ and $\phi$ , and since these two coordinates can vary independently the system has two degrees of freedom and we can use $(z, \phi)$ as generalized coordinates. The velocity has $v_{\rho} = 0$ , $v_{\phi} = R\dot{\phi}$ , and $v_z = \dot{z}$ . Therefore the kinetic energy is

$$
T = \frac {1}{2} m v ^ {2} = \frac {1}{2} m (R ^ {2} \dot {\phi} ^ {2} + \dot {z} ^ {2}).
$$

The potential energy for the force $\mathbf{F} = -kr$ is (Problem 7.25) $U = \frac{1}{2} kr^2$ , where $r$ is the distance from the origin to the particle, given by $r^2 = R^2 + z^2$ (see Figure 7.7). Therefore

$$
U = \frac {1}{2} k (R ^ {2} + z ^ {2}),
$$

and the Lagrangian is

$$
\mathcal {L} = \frac {1}{2} m (R ^ {2} \dot {\phi} ^ {2} + \dot {z} ^ {2}) - \frac {1}{2} k (R ^ {2} + z ^ {2}).\tag{7.57}
$$

Since the system has two degrees of freedom, there are two equations of motion. The z equation is

$$
\frac {\partial \mathcal {L}}{\partial z} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {z}} \quad \text { or } \quad - k z = m \ddot {z}.\tag{7.58}
$$

![](images/6dbc4265928c60c0c47cdb791d05b58e811e0a733c0cccec9bd666beb4490f17.jpg)  
Figure 7.7 A mass m is confined to the surface of the cylinder $\rho = R$ and subject to a Hooke's law force F = -kr.

The $\phi$ equation is even simpler. Since $\mathcal{L}$ does not depend on $\phi$ , it follows that $\partial \mathcal{L} / \partial \phi = 0$ and the $\phi$ equation is just

$$
\frac {\partial \mathcal {L}}{\partial \phi} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {\phi}} \qquad \text { or } \qquad 0 = \frac {d}{d t} m R ^ {2} \dot {\phi}.\tag{7.59}
$$

The z equation (7.58) tells us that the mass executes simple harmonic motion in the z direction, with $z = A \cos(\omega t - \delta)$ . The $\phi$ equation (7.59) tells us that the quantity $m R^{2}\dot{\phi}$ is constant, that is, that the z component of the angular momentum is conserved — a result we could have anticipated since there is no torque in this direction. Because $\rho$ is fixed, this implies simply that $\dot{\phi}$ is constant, and the mass moves around the cylinder with constant angular velocity $\dot{\phi}$ , at the same time that it moves up and down in the z direction in simple harmonic motion.

These two examples illustrate the steps to be followed in solving any problem by the Lagrangian method (provided all constraints are holonomic and the nonconstraint forces are derivable from a potential energy, as we are assuming):

1. Write down the kinetic and potential energies and hence the Lagrangian $L = T - U$ , using any convenient inertial reference frame.

2. Choose a convenient set of n generalized coordinates $q_{1}, \cdots, q_{n}$ and find expressions for the original coordinates of step 1 in terms of your chosen generalized coordinates. (Steps 1 and 2 can be done in either order.)

3. Rewrite L in terms of $q_{1}, \cdots, q_{n}$ and $\dot{q}_{1}, \cdots, \dot{q}_{n}$ .

4. Write down the n Lagrange equations (7.52).

As we shall see, these four steps provide an almost infallible route to the equations of motion of any system, no matter how complex. Whether the resulting equations can be easily solved is another matter, but even when they cannot, just having them is a huge step toward understanding a system and an essential step to finding approximate or numerical solutions.

The next two examples illustrate how the Lagrangian approach can give the equations of motion, almost effortlessly, for problems that would require considerable care and ingenuity using Newtonian methods.

## EXAMPLE 7.5 A Block Sliding on a Wedge

Consider the block and wedge shown in Figure 7.8. The block (mass m) is free to slide on the wedge, and the wedge (mass M) can slide on the horizontal table, both with negligible friction. The block is released from the top of the wedge, with both initially at rest. If the wedge has angle $\alpha$ and the length of its sloping face is l, how long does the block take to reach the bottom?

The system has two degrees of freedom, and a good choice of the two generalized coordinates is, as shown, the distance $q_{1}$ of the block from the top of the wedge and the distance $q_{2}$ of the wedge from any convenient fixed point on the table. The quantity we need to find is the acceleration $\ddot{q}_{1}$ of the block relative to the wedge, since with this we can quickly find the time required to slide the length of the wedge. Our first task is to write down the Lagrangian, and it is often safest to do this in Cartesian coordinates, and then rewrite it in terms of the chosen generalized coordinates.

![](images/645e5578e8bdaa9fe687eb71ca548ee6fc60765ce35f3826d66245b71981e510.jpg)  
Figure 7.8 A block of mass m slides down a wedge of mass M, which is free to slide over the horizontal table.

The kinetic energy of the wedge is just $T_{M} = \frac{1}{2} M \dot{q}_{2}^{2}$ but that of the block is more complicated. The block's velocity relative to the wedge is $\dot{q}_{1}$ down the slope, but the wedge itself has a horizontal velocity $\dot{q}_{2}$ relative to the table. The velocity of the block relative to the inertial frame of the table is the vector sum of these two. Resolving into rectangular components (x to the right, y downward), we find for the velocity of the block relative to the table

$$
\mathbf {v} = \left(v _ {x}, v _ {y}\right) = \left(\dot {q} _ {1} \cos \alpha + \dot {q} _ {2}, \dot {q} _ {1} \sin \alpha\right).
$$

Thus the kinetic energy of the block is

$$
T _ {m} = \frac {1}{2} m (v _ {x} ^ {2} + v _ {y} ^ {2}) = \frac {1}{2} m (\dot {q} _ {1} ^ {2} + \dot {q} _ {2} ^ {2} + 2 \dot {q} _ {1} \dot {q} _ {2} \cos \alpha).
$$

(I used the identity $\cos^{2}\alpha + \sin^{2}\alpha = 1$ to simplify this.) The total kinetic energy of the system is

$$
T = T _ {M} + T _ {m} = \frac {1}{2} (M + m) \dot {q} _ {2} ^ {2} + \frac {1}{2} m (\dot {q} _ {1} ^ {2} + 2 \dot {q} _ {1} \dot {q} _ {2} \cos \alpha).\tag{7.60}
$$

The potential energy of the wedge is a constant, which we may as well take to be zero. That of the block is -mgy, where $y = q_{1} \sin \alpha$ is the height of the block measured down from the top of the wedge. Therefore

$$
U = - m g q _ {1} \sin \alpha
$$

and the Lagrangian is

$$
\mathcal {L} = T - U = \frac {1}{2} (M + m) \dot {q} _ {2} ^ {2} + \frac {1}{2} m (\dot {q} _ {1} ^ {2} + 2 \dot {q} _ {1} \dot {q} _ {2} \cos \alpha) + m g q _ {1} \sin \alpha .\tag{7.61}
$$

Once we have found the Lagrangian in terms of the generalized coordinates $q_{1}$ and $q_{2}$ , all we have to do is to write down the two Lagrange equations, one for $q_{1}$ and one for $q_{2}$ , and then solve them. The $q_{2}$ equation (which is a little simpler) is

$$
\frac {\partial \mathcal {L}}{\partial q _ {2}} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {q} _ {2}}\tag{7.62}
$$

but, since $\mathcal{L}$ in (7.61) is clearly independent of $q_{2}$ , this just tells us that the generalized momentum $\partial \mathcal{L} / \partial \dot{q}_2$ is constant,

$$
M \dot {q} _ {2} + m (\dot {q} _ {2} + \dot {q} _ {1} \cos \alpha) = \mathrm{const}\tag{7.63}
$$

— a result you will recognize as conservation of the total momentum in the x direction (and something you could have written down without any help from Lagrange).

The $q_{1}$ equation

$$
\frac {\partial \mathcal {L}}{\partial q _ {1}} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {q} _ {1}}\tag{7.64}
$$

is more complicated, since neither derivative is zero. Sustituting (7.61) for $\mathcal{L}$ , we can write this as

$$
\begin{array}{c} m g \sin \alpha = \frac {d}{d t} m (\dot {q} _ {1} + \dot {q} _ {2} \cos \alpha) \\ = m (\ddot {q} _ {1} + \ddot {q} _ {2} \cos \alpha). \end{array}\tag{7.65}
$$

Differentiating (7.63) we see that

$$
\ddot {q} _ {2} = - \frac {m}{M + m} \ddot {q} _ {1} \cos \alpha ,\tag{7.66}
$$

which lets us eliminate $\ddot{q}_{2}$ from (7.65) and solve for $\ddot{q}_{1}$ :

$$
\ddot {q} _ {1} = \frac {g \sin \alpha}{1 - \frac {m \cos^ {2} \alpha}{M + m}}.\tag{7.67}
$$

Armed with this value for $\ddot{q}_{1}$ we can quickly answer the original question: Since the acceleration down the slope is constant, the distance traveled down the slope in time t is $\frac{1}{2}\ddot{q}_{1}t^{2}$ , and the time to travel the length l is just $\sqrt{2l/\ddot{q}_{1}}$ , with $\ddot{q}_{1}$ given by (7.67). More interesting than this answer is to check that the formula (7.67) for $\ddot{q}_{1}$ agrees with common sense in various special cases. For example, if $\alpha = 90^{\circ}$ , (7.67) implies that $\ddot{q}_{1} = g$ , which is clearly right; and, if $M \to \infty$ , (7.67) implies that $\ddot{q}_{1} \to g \sin \alpha$ , which is the well-known acceleration for a block on a fixed incline and clearly makes sense. I leave it as an exercise (Problem 7.19) to check that in the limit that $M \to 0$ , our answers agree with what you could have predicted.

## EXAMPLE 7.6 A Bead on a Spinning Wire Hoop

A bead of mass m is threaded on a frictionless circular wire hoop of radius R. The hoop lies in a vertical plane, which is forced to rotate about the hoop's vertical diameter with constant angular velocity $\dot{\phi} = \omega$ , as shown in Figure 7.9. The bead's position on the hoop is specified by the angle $\theta$ measured up from the vertical. Write down the Lagrangian for the system in terms of the generalized coordinate $\theta$ and find the equation of motion for the bead. Find any equilibrium positions at which the bead can remain with $\theta$ constant, and explain their locations in terms of statics and the “centrifugal force” $m\omega^{2}\rho$ (where $\rho$ is the bead’s distance from the axis). Use the equation of motion to discuss the stability of the equilibrium positions.

![](images/84707398312dd578c25b2c66d7a26ac6858361d1ddda243f91a9535182333fa2.jpg)  
Figure 7.9 A bead is free to move around the frictionless wire hoop, which is spinning at a fixed rate $\omega$ about its vertical axis. The bead's position is specified by the angle $\theta$ ; its distance from the axis of rotation is $\rho = R\sin \theta$ .

Our first task is to write down the Lagrangian. Relative to a nonrotating frame, the bead has velocity $R\dot{\theta}$ tangential to the hoop and $\rho\omega = (R\sin\theta)\omega$ normal to the hoop (the latter due to the spinning of the hoop with angular velocity $\omega$ ). Thus the kinetic energy is $T = \frac{1}{2}mv^{2} = \frac{1}{2}mR^{2}(\dot{\theta}^{2} + \omega^{2}\sin^{2}\theta)$ . The gravitational potential energy is easily seen to be $U = mgR(1 - \cos\theta)$ , measured from the bottom of the hoop. Therefore, the Lagrangian is

$$
\mathcal {L} = \frac {1}{2} m R ^ {2} (\dot {\theta} ^ {2} + \omega^ {2} \sin^ {2} \theta) - m g R (1 - \cos \theta),\tag{7.68}
$$

and the Lagrange equation is

$$
\frac {\partial \mathcal {L}}{\partial \theta} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {\theta}} \quad \text { or } \quad m R ^ {2} \omega^ {2} \sin \theta \cos \theta - m g R \sin \theta = m R ^ {2} \ddot {\theta}.
$$

Dividing through by $mR^2$ , we arrive at the desired equation of motion:

$$
\ddot {\theta} = (\omega^ {2} \cos \theta - g / R) \sin \theta .\tag{7.69}
$$

Although this equation cannot be solved analytically in terms of elementary functions, it can, nevertheless, tell us lots about the system's behavior. To illustrate this, let us use (7.69) to find the equilibrium positions of the bead. An equilibrium point is any value of $\theta$ — call it $\theta_{\mathrm{o}}$ — satisfying the following condition: If the bead is placed at rest ( $\dot{\theta} = 0$ ) at $\theta = \theta_{\mathrm{o}}$ , then it will remain at rest at $\theta_{\mathrm{o}}$ . This condition is guaranteed if $\ddot{\theta} = 0$ . (To see this, note that if $\ddot{\theta} = 0$ , then $\dot{\theta}$ doesn't change and remains zero, which means that $\theta$ doesn't change and remains equal to $\theta_0$ .) Thus to find the equilibrium positions we have only to equate the right side of (7.69) to zero:

$$
(\omega^ {2} \cos \theta - g / R) \sin \theta = 0.\tag{7.70}
$$

This equation is satisfied if either of the two factors is zero. The factor $\sin\theta$ is zero if $\theta=0$ or $\pi$ . Thus the bead can remain at rest at the bottom or top of the hoop. The first factor in (7.70) vanishes when

$$
\cos \theta = \frac {g}{\omega^ {2} R}.
$$

Since $|\cos\theta|$ must be less than or equal to 1, the first factor can vanish only when $\omega^{2} \geq g/R$ . When this condition is satisfied, there are two more equilibrium positions at

$$
\theta_ {0} = \pm \arccos \left(\frac {g}{\omega^ {2} R}\right).\tag{7.71}
$$

We conclude that when the hoop is rotating slowly $(\omega^{2} < g/R)$ , there are just two equilibrium positions, at the bottom and top of the hoop, but when it rotates fast enough $(\omega^{2} > g/R)$ , there are two more, symmetrically placed on either side of the bottom, as given by (7.71). $^{10}$

Perhaps the simplest way to understand the various equilibrium positions is in terms of the “centrifugal force.” In most introductory physics courses, the centrifugal force is dismissed as an abomination to be avoided by all right-thinking physicists. As long as we confine our attention to inertial frames, this is a correct (and certainly a safe) point of view. Nevertheless, as we shall see in Chapter 9, from the point of view of a noninertial rotating frame there is a perfectly real centrifugal force $m\omega^{2}\rho$ (perhaps more familiar as $mv^{2}/\rho$ ), where $\rho$ is the object’s distance from the axis of rotation. Thus, taking the point of view of a fly perched on the rotating hoop, we can understand the equilibrium positions as follows: At the bottom or top of the hoop, the bead is on the axis of rotation and $\rho = 0$ ; therefore, the centrifugal force $m\omega^{2}\rho$ is zero. Furthermore, the force of gravity is normal to the hoop, so there is no force tending to move the bead along the wire and the bead remains at rest. The other two equilibrium points are a little subtler: At any position off the axis (such as that shown in Figure 7.9) the centrifugal force is nonzero and has a component pushing the bead outward along the wire; meanwhile the force of gravity has a component pulling the bead inward along the wire (provided the bead is below the halfway marks, $\theta = \pm\pi/2$ ). At either of the points given by (7.71), these two components are balanced (check this for yourself — Problem 7.28) and the bead can remain at rest.

An equilibrium point $\theta_0$ is not especially interesting unless it is stable — that is, the bead, if nudged a little away from $\theta_0$ , moves back toward $\theta_0$ . Using our equation of motion (7.69), we can easily address this issue, and I'll start with the equilibrium at the bottom, $\theta = 0$ . As long as $\theta$ remains close to 0, we can set $\cos \theta \approx 1$ and $\sin \theta \approx \theta$ and approximate the equation by

$$
\ddot {\theta} = (\omega^ {2} - g / R) \theta \quad [ \theta \text {   near   } 0 ].\tag{7.72}
$$

If the hoop is rotating slowly ( $\omega^{2} < g/R$ ), this has the form

$$
\ddot {\theta} = (\text { negative   number }) \theta .
$$

If we nudge the bead to the right $(\theta > 0)$ , then since $\theta$ is positive $\ddot{\theta}$ is negative, and the bead accelerates to the left, that is, back toward the bottom. If we nudge it to the left, $(\theta < 0)$ , then $\ddot{\theta}$ becomes positive, and the bead accelerates to the right, which is again back toward the bottom. Either way, the bead returns toward the equilibrium, which is, therefore, stable.

If we speed up the rotation of the hoop, so that $\omega^{2} > g/R$ , then the approximate equation of motion (7.72) takes the form

$$
\ddot {\theta} = (\text { positive   number }) \theta .
$$

Now a small displacement to the right makes $\ddot{\theta}$ positive, and the bead accelerates away from the bottom. Similarly a displacement to the left makes $\ddot{\theta}$ negative, and again the bead accelerates away from the bottom. Thus, as we increase $\omega$ past the critical value where $\omega^{2}=g/R$ , the equilibrium at the bottom changes from stable to unstable.

The equilibrium at the top $(\theta = \pi)$ is always unstable (see Problem 7.28). This is easy to understand from our discussion of the centrifugal force. Near the top of the hoop, both the centrifugal and gravitational forces tend to push the bead away from the top, so there is no chance of a restoring force to pull it back to the equilibrium position.

The other two equilibrium positions only exist when $\omega^{2} > g/R$ , and are easily seen to be stable: The equation of motion (7.69) is

$$
\ddot {\theta} = (\omega^ {2} \cos \theta - g / R) \sin \theta .\tag{7.73}
$$

To be definite, let us consider the equilibrium on the right with $0 < \theta < \pi/2$ . At the equilibrium point, the term in parenthesis on the right of (7.73) is zero, while $\sin\theta$ is positive. If we increase $\theta$ a little (bead moves up and to the right), $\sin\theta$ remains positive, but the term in parenthesis becomes negative. (Remember, $\cos\theta$ is a decreasing function in this quadrant.) Thus $\ddot{\theta}$ becomes negative, and the bead accelerates back toward its equilibrium point. If we decrease $\theta$ a little from the equilibrium, then $\ddot{\theta}$ becomes positive, and again the bead accelerates back toward equilibrium. Therefore the equilibrium on the right is stable. As you would expect, a similar analysis shows that the same is true of the equilibrium on the left.

We arrive at the following interesting story: When the hoop is rotating slowly $(\omega^{2} < g/R)$ , there is just one stable equilibrium, at $\theta = 0$ . If we speed up the rotation, then as $\omega$ passes the critical value where $\omega^{2} = g/R$ , this original equilibrium becomes unstable, but two new stable equilibrium points appear, emerging from $\theta = 0$ and moving out to the right and left as we increase $\omega$ still more. This phenomenon — the disappearance of one stable equilibrium and the simultaneous appearance of two others diverging from the same point — is called a bifurcation and will be one of our principal topics in Chapter 12 on chaos theory.

It is interesting to note that the device of this example was used by James Watt (1736–1829) as a governor for his steam engines. The device rotated with the engine, and as the engine sped up the bead rose on the hoop. When the angular velocity $\omega$ reached some predetermined maximum allowable value, the bead, arriving at a corresponding height, caused the supply of steam to be shut off.

This example illustrates another strength of the Lagrangian method that was mentioned back in Section 7.1: The generalized coordinates can even be coordinates relative to a noninertial reference frame, just as long as the frame in which the Lagrangian $L = T - U$ was originally written was inertial. In this example, the angle $\theta$ was the polar angle of the bead, measured in the noninertial rotating frame of the hoop, but the Lagrangian (7.68) was defined as $L = T - U$ with T and U evaluated in the inertial frame relative to which the hoop rotates. $^{11}$

In the next and final example of this section, we pursue the previous example of the bead on the rotating hoop, and obtain approximate solutions of the equation of motion in the neighborhood of the stable equilibrium points.

## EXAMPLE 7.7 Oscillations of the Bead near Equilibrium

Consider again the bead of the previous example and use the equation of motion to find the bead's approximate behavior in the neighborhood of the stable equilibrium positions.

When $\omega^{2} < g/R$ , the only stable equilibrium is at the bottom of the hoop with $\theta = 0$ . As long as $\theta$ remains small, we can approximate the equation of motion (7.73) by setting $\sin\theta \approx \theta$ and $\cos\theta \approx 1$ to give

$$
\begin{array}{l l} \ddot {\theta} = - (g / R - \omega^ {2}) \theta & [ \theta \text { near } 0 ] \\ = - \Omega^ {2} \theta \end{array}\tag{7.74}
$$

where the second line introduces the frequency

$$
\Omega = \sqrt {g / R - \omega^ {2}}.
$$

As long as $\omega^{2} < g/R$ , this defines $\Omega$ as a real positive number, and we recognize (7.74) as the equation for simple harmonic motion with frequency $\Omega$ . We conclude that a bead which is displaced a little from the stable equilibrium at $\theta = 0$ , executes harmonic motion with frequency $\Omega$ ,

$$
\theta (t) = A \cos (\Omega t - \delta).\tag{7.75}
$$

If we speed up the rate of the hoop's rotation until $\omega^{2} > g/R$ , then $\Omega$ becomes pure imaginary, and, since $\cos i\alpha = \cosh\alpha$ , our solution (7.75) becomes a hyperbolic cosine, which grows with time, correctly reflecting that the equilibrium at $\theta = 0$ has become unstable.

Once $\omega^{2} > g/R$ , there are two stable equilibrium positions given by (7.71) and located symmetrically to the right and left of the bottom of the hoop. As you might expect, these behave in the same way, and to be definite I shall focus on the one on the right. Let us denote its position by $\theta = \theta_{0}$ , where, according to (7.70), $\theta_{0}$ satisfies

$$
\omega^ {2} \cos \theta_ {\mathrm{o}} - g / R = 0.\tag{7.76}
$$

Let us now imagine the bead placed close to $\theta_{0}$ at

$$
\theta = \theta_ {0} + \epsilon
$$

and investigate the time dependence of the small parameter $\epsilon$ . Once again we can approximate the equation of motion (7.73), though this requires more care. If we approximate the factors of $\cos(\theta_{0}+\epsilon)$ and $\sin(\theta_{0}+\epsilon)$ by the first two terms of their Taylor series,

$$
\cos (\theta_ {0} + \epsilon) \approx \cos \theta_ {0} - \epsilon \sin \theta_ {0} \quad \text { and } \quad \sin (\theta_ {0} + \epsilon) \approx \sin \theta_ {0} + \epsilon \cos \theta_ {0}\tag{7.77}
$$

then the equation of motion (7.73) becomes

$$
\begin{array}{l} \ddot {\theta} = [ \omega^ {2} \cos (\theta_ {0} + \epsilon) - g / R ] \sin (\theta_ {0} + \epsilon) \\ \qquad = [ \omega^ {2} \cos \theta_ {0} - \epsilon   \omega^ {2} \sin \theta_ {0} - g / R ] [ \sin \theta_ {0} + \epsilon \cos \theta_ {0} ]. \end{array}\tag{7.78}
$$

By (7.76) the first and third terms in the first square bracket cancel, leaving just the middle term $-\epsilon \omega^{2} \sin \theta_{0}$ . To lowest order in $\epsilon$ we can drop the second term of the second bracket, and, since $\ddot{\theta}$ is the same as $\ddot{\epsilon}$ , we are left with

$$
\ddot {\epsilon} = - \epsilon   \omega^ {2} \sin^ {2} \theta_ {\mathrm{o}} = - \Omega^ {\prime 2} \epsilon .\tag{7.79}
$$

Here the second equality defines the frequency $\Omega^{\prime}=\omega\sin\theta_{0}$ , or, using (7.76),

$$
\Omega^ {\prime} = \sqrt {\omega^ {2} - \left(\frac {g}{\omega R}\right) ^ {2}}\tag{7.80}
$$

(see Problem 7.26). Equation (7.79) is the equation for simple harmonic motion. Therefore, the parameter $\epsilon$ oscillates about zero, and the bead itself oscillates about the equilibrium position $\theta_0$ with frequency $\Omega'$ .

## 7.6 Generalized Momenta and Ignorable Coordinates

As I have already mentioned, for any system with n generalized coordinates $q_{i}$ ( $i = 1, \cdots, n$ ), we refer to the n quantities $\partial L/\partial q_{i} = F_{i}$ as generalized forces and $\partial L/\partial \dot{q}_{i} = p_{i}$ as generalized momenta. With this terminology, the Lagrange equation,

$$
\frac {\partial \mathcal {L}}{\partial q _ {i}} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {q} _ {i}},\tag{7.81}
$$

can be rewritten as

$$
F _ {i} = \frac {d}{d t} p _ {i}.\tag{7.82}
$$

That is, “generalized force = rate of change of generalized momentum.” In particular, if the Lagrangian is independent of a particular coordinate $q_{i}$ , then $F_{i} = \partial L / \partial q_{i} = 0$ and the corresponding generalized momentum $p_{i}$ is constant.

Consider, for example, a single projectile subject only to the force of gravity. The potential energy is U = mgz (if we use Cartesian coordinates with z measured vertically up), and the Lagrangian is

$$
\mathcal {L} = \mathcal {L} (x, y, z, \dot {x}, \dot {y}, \dot {z}) = \frac {1}{2} m (\dot {x} ^ {2} + \dot {y} ^ {2} + \dot {z} ^ {2}) - m g z.\tag{7.83}
$$

With respect to Cartesian coordinates, the generalized force is just the usual force $(\partial\mathcal{L}/\partial x=-\partial U/\partial x=F_{x},\text{etc.})$ and the generalized momentum is just the usual momentum $(\partial\mathcal{L}/\partial\dot{x}=m\dot{x}=p_{x},\text{etc.})$ . Because L is independent of x and y, it immediately follows that the components $p_{x}$ and $p_{y}$ are constant, as we already knew.

In general, the generalized forces and momenta are not the same as the usual forces and momenta. For instance, we saw in Equations (7.25) and (7.26) that in two-dimensional polar coordinates the $\phi$ component of the generalized force is the torque, and that of the generalized momentum is actually the angular momentum. In any case, when the Lagrangian is independent of a coordinate $q_{i}$ the corresponding generalized momentum is conserved. Thus, if the Lagrangian of a two-dimensional particle is independent of $\phi$ , then the particle's angular momentum is conserved — another important result (and one that is clear from the Newtonian perspective as well). When the Lagrangian is independent of a coordinate $q_{i}$ , that coordinate is sometimes said to be ignorable or cyclic. Obviously it is a good idea, when possible, to choose coordinates so that as many as possible are ignorable and their corresponding momenta are constant. In fact, this is perhaps the main criterion in choosing generalized coordinates for any given problem: Try to find coordinates as many as possible of which are ignorable.

We can rephrase the result of the last three paragraphs by noting that the statement “L is independent of a coordinate $q_{i}$ ” is equivalent to saying “L is unchanged, or invariant, when $q_{i}$ varies (with all the other $q_{j}$ held fixed).” Thus we can say that if L is invariant under variations of a coordinate $q_{i}$ then the corresponding generalized momentum $p_{i}$ is conserved. This connection between invariance of L and certain conservation laws is the first of several similar results relating invariance under transformations (translations, rotations, and so on) to conservation laws. These results are known collectively as Noether's theorem, after the German mathematician Emmy Noether (1882–1935). I shall return to this important theorem in Section 7.8.

## 7.7 Conclusion

The Lagrangian version of classical mechanics has the two great advantages that, unlike the Newtonian version, it works equally well in all coordinate systems and it can handle constrained systems easily, avoiding any need to discuss the forces of constraint. If the system is constrained, one must choose a suitable set of independent generalized coordinates. Whether or not there are constraints, the next task is to write down the Lagrangian $\mathcal{L}$ in terms of the chosen coordinates. The equations of motion then follow automatically in the standard form

$$
\frac {\partial \mathcal {L}}{\partial q _ {i}} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {q} _ {i}} \quad [ i = 1, \dots , n ].
$$

There is, of course, no guarantee that the resulting equations will be easy to solve, and in most real problems they are not, requiring numerical solution or at least some approximations before they can be solved analytically.

Even in problems that are only moderately complicated, like the examples of Section 7.5, finding the equations of motion by Lagrange's method is remarkably easier than by using Newton's second law. Indeed, some purists object that the Lagrangian approach makes life too easy, removing the need to think about the physics.

The Lagrangian formalism can be extended to include more general systems than those considered so far. One important case is that of magnetic forces, which I take up in Section 7.9. Dissipative forces, such as friction or air resistance, can sometimes be included, but it should be admitted that the Lagrangian formalism is primarily suited to problems where dissipative forces are absent or, at least, negligible.

The final three sections of this chapter treat three advanced topics, all of which are centrally important in Lagrangian mechanics, but all of which could be omitted on a first reading. In Section 7.8, I give two more examples of the remarkable connection between invariance under certain transformations and conservation laws. This connection, known as Noether's theorem, is important in all of modern physics, but especially in quantum physics. Section 7.9 discusses how to include magnetic forces in Lagrangian mechanics, another topic of great importance in quantum theory. Finally, Section 7.10 introduces the method of Lagrange multipliers. This technique appears in many different guises in many areas of physics, but I shall restrict myself to some simple examples in Lagrangian mechanics. These last three sections are arranged to be self-contained and independent. You could study all of them, none of them, or any selection in between.

## 7.8 More about Conservation Laws\*

\* The material of this section is more advanced than the preceding sections, and you should feel free to omit it on a first reading. Be aware, however, that the material discussed here is needed before you read Section 11.5 and Chapter 13.

In this section I shall discuss how the laws of conservation of momentum and energy fit into the Lagrangian formulation of mechanics. Since we derived the Lagrangian formulation from the Newtonian, anything that we already knew about conservation laws, based on Newtonian mechanics, will naturally still be true in Lagrangian mechanics. Nevertheless, we can gain some new insights by examining the conservation laws from a Lagrangian perspective. Furthermore, much modern work takes the Lagrangian formulation (based on Hamilton's principle, for example) as its starting point. In this context, it is important to know what can be said about conservation laws strictly within the Lagrangian framework.

## Conservation of Total Momentum

We already know from Newtonian mechanics that the total momentum of an isolated system of N particles is conserved, but let us examine this important property from the Lagrangian point of view. One of the most prominent features of an isolated system is that it is translationally invariant; that is, if we transport all N particles bodily through the same displacement $\epsilon$ , nothing physically significant about the system should change. This is illustrated in Figure 7.10, where we see that the effect of moving the whole system through the fixed displacement $\epsilon$ is to replace every position $r_{\alpha}$ by $r_{\alpha} + \epsilon$ .

$$
\mathbf {r} _ {1} \rightarrow \mathbf {r} _ {1} + \boldsymbol {\epsilon}, \qquad \mathbf {r} _ {2} \rightarrow \mathbf {r} _ {2} + \boldsymbol {\epsilon}, \qquad \dots , \qquad \mathbf {r} _ {N} \rightarrow \mathbf {r} _ {N} + \boldsymbol {\epsilon}.\tag{7.84}
$$

In particular, the potential energy must be unaffected by this displacement, so that

$$
U (\mathbf {r} _ {1} + \boldsymbol {\epsilon}, \dots , \mathbf {r} _ {N} + \boldsymbol {\epsilon}, t) = U (\mathbf {r} _ {1}, \dots , \mathbf {r} _ {N}, t)\tag{7.85}
$$

![](images/3effce0011af8f4f8790956b2c2f0b571b41fc19275464e3d5a9688a098e56d5.jpg)  
Figure 7.10 An isolated system of N particles is translationally invariant, which means that when every particle is transported through the same displacement $\epsilon$ , nothing physically significant changes.

or, more briefly,

$$
\delta U - ()
$$

where $\delta U$ denotes the change in $U$ under the translation (7.84). Clearly the velocities are unchanged by the translation (7.84). (Adding a constant $\epsilon$ to all the $\mathbf{r}_{\alpha}$ doesn't change the $\dot{\mathbf{r}}_{\alpha}$ .) Therefore $\delta T = 0$ , and hence

$$
\delta \mathcal {L} = 0\tag{7.86}
$$

under the translation (7.84). This result is true for any displacement $\epsilon$ . If we choose $\epsilon$ to be an infinitesimal displacement in the x direction, then all of the x coordinates $x_{1},\cdots,x_{N}$ increase by $\epsilon$ , while the y and z coordinates are unchanged. For this translation, the change in L is

$$
\delta \mathcal {L} = \epsilon   \frac {\partial \mathcal {L}}{\partial x _ {1}} + \dots + \epsilon   \frac {\partial \mathcal {L}}{\partial x _ {N}} = 0.
$$

This implies that

$$
\sum_ {\alpha = 1} ^ {N} \frac {\partial \mathcal {L}}{\partial x _ {\nu}} = 0.\tag{7.87}
$$

Now using Lagrange's equations we can rewrite each derivative as

$$
\frac {\partial \mathcal {L}}{\partial x _ {\alpha}} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {x} _ {\alpha}} = \frac {d}{d t} p _ {\alpha},
$$

where $p_{\alpha x}$ is the x component of the momentum of particle $\alpha$ . Thus (7.87) becomes

$$
\sum_ {\sigma = 1} ^ {N} \frac {d}{d t} p _ {\sigma} = \frac {d}{d t} P _ {\lambda} = 0
$$

where $P_{x}$ is the x component of the total momentum $P = \sum_{\sigma} p_{\sigma}$ . By choosing the small displacement $\epsilon$ successively in the y and z directions, we can prove the same result for the y and z components, and we reach the conclusion that, provided the Lagrangian is unchanged by the translation (7.84), the total momentum of the N-particle system is conserved. This connection between translational invariance of L and conservation of total momentum is another example of Noether's theorem.

## Conservation of Energy

Finally, I would like to discuss conservation of energy from the Lagrangian point of view. The analysis proves somewhat complicated, but introduces a number of ideas that are important in more advanced work, particularly in the Hamiltonian formulation of mechanics (Chapter 13).

As time advances the function $\mathcal{L}(q_{1},\cdots,q_{n},\dot{q}_{1},\cdots,\dot{q}_{n},t)$ changes, both because $t$ is changing, and because the $q$ 's and $\dot{q}$ 's change with the evolving system. Thus, by the chain rule,

$$
\frac {d}{d t} \mathscr {L} (q _ {1}, \dots , q _ {n}, \dot {q} _ {1}, \dots , \dot {q} _ {n}, t) = \sum_ {i} \frac {\partial \mathscr {L}}{\partial q _ {i}} \dot {q} _ {i} + \sum_ {i} \frac {\partial \mathscr {L}}{\partial \dot {q} _ {i}} \ddot {q} _ {i} + \frac {\partial \mathscr {L}}{\partial t}.\tag{7.88}
$$

Now, by Lagrange's equation, I can replace the derivative in the first sum on the right by

$$
\frac {\partial \mathcal {L}}{\partial q _ {i}} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {q} _ {i}} = \frac {d}{d t} p _ {i} = \dot {p} _ {i}.
$$

Meanwhile, the derivative in the second sum on the right of (7.88) is just the generalized momentum $p_{i}$ . Thus, I can rewrite (7.88) as

$$
\begin{array}{r l} \frac {d}{d t} \mathcal {L} & = \sum_ {i} \left(\dot {p _ {i}} \dot {q} _ {i} + p _ {i} \ddot {q} _ {i}\right) + \frac {\partial \mathcal {L}}{\partial t} \\ & = \frac {d}{d t} \sum_ {i} \left(p _ {i} \dot {q} _ {i}\right) + \frac {\partial \mathcal {L}}{\partial t}. \end{array}\tag{7.89}
$$

Now, for many interesting systems, the Lagrangian does not depend explicitly on time; that is, $\partial L/\partial t = 0$ . When this is the case, the second term on the right of (7.89) vanishes. If we move the left side of (7.89) over to the right, we see that the time derivative of the quantity $\sum p_{i}\dot{q}_{i} - L$ is zero. This quantity is so important that it has its own symbol,

$$
\mathcal {H} = \sum_ {i = 1} ^ {n} p _ {i} \dot {q} _ {i} - \mathscr {L},\tag{7.90}
$$

and is called the Hamiltonian of the system. With this terminology, we can state the following important conclusion:

If the Lagrangian L does not depend explicitly on time (that is, $\partial L/\partial t = 0$ ), then the Hamiltonian H is conserved.

The discovery of any conservation law is a momentous event and is enough to justify saying that the Hamiltonian is an important quantity. In fact, it goes much further than this. As we shall see in Chapter 13, the Hamiltonian H is the basis of the Hamiltonian formulation of mechanics, in just the same way that L is the basis of Lagrangian mechanics.

For the moment, the chief importance of our newly discovered Hamiltonian is that in many situations it is in fact just the total energy of the system. Specifically, we shall prove that, provided the relation between the generalized coordinates and Cartesians is time-independent,

$$
\mathbf {r} _ {\alpha} = \mathbf {r} _ {\alpha} (q _ {1}, \dots , q _ {n}),\tag{7.91}
$$

the Hamiltonian 9c is just the total energy,

$$
\mathcal {H} = T + U.\tag{7.92}
$$

You may recall that we agreed in Section 7.3 to describe generalized coordinates that satisfy (7.91) as natural; thus, we can paraphrase the result (7.92) to say that, provided the generalized coordinates are natural, H is just the total energy $T + U$ . To prove that, let us expect the total kinetic energy $I = \sum_{j=1}^{n} m_{ij} r_{ij}$ , in terms of the generalized coordinates $q_{1}, \cdots, q_{n}$ . First, differentiating (7.91) with respect to t and using the chain rule, we find that $^{12}$

$$
\dot {\mathbf {r}} _ {i j} = \sum_ {i} ^ {n} \frac {\partial \mathbf {r} _ {i j}}{\partial q} \dot {q} _ {i}.\tag{7.93}
$$

If we now form the scalar product of this equation with itself, we find

$$
\dot {\mathbf {r}} _ {\alpha} ^ {2} = \sum_ {j} \left(\frac {\partial \mathbf {r} _ {\alpha}}{\partial q _ {j}} \dot {q} _ {j}\right) \cdot \sum_ {k} \left(\frac {\partial \mathbf {r} _ {\alpha}}{\partial q _ {k}} \dot {q} _ {k}\right)
$$

where I have renamed the summation indices as $j$ and $k$ to avoid future confusion. The kinetic energy is now given as a triple sum, which I can reorganize and write as

$$
I = \frac {1}{2} \sum_ {\alpha} m _ {\alpha} \dot {\mathbf {r}} _ {\alpha} ^ {2} = \frac {1}{2} \sum_ {j, k} A _ {j k} \dot {q} _ {j} \dot {q} _ {k}\tag{7.94}
$$

where $A_{jk}$ is shorthand for the sum

$$
A _ {j k} = A _ {j k} (q _ {1}, \dots , q _ {n}) = \sum_ {\alpha} m _ {\alpha} \left(\frac {\partial \mathbf {r} _ {\alpha}}{\partial q _ {j}}\right) \cdot \left(\frac {\partial \mathbf {r} _ {\alpha}}{\partial q _ {k}}\right).\tag{7.95}
$$

We can now evaluate the generalized momentum $p$ by differentiating 7.94 with respect to $\dot{q}_i$ (Problem 7.45),

$$
p _ {i} = \frac {\partial \mathcal {L}}{\partial \dot {q} _ {i}} = \frac {\partial T}{\partial \dot {q} _ {i}} = \sum_ {j} A _ {i j} \dot {q} _ {j}.\tag{7.96}
$$

Returning to Equation 7(90) for the Hamiltonian, we can rewrite the sum on the right as

$$
\sum_ {i} p _ {i} \dot {q} _ {i} = \sum_ {i} \left(\sum_ {j} A _ {i j} \dot {q} _ {j}\right) \dot {q} _ {i} = \sum_ {i, j} A _ {i j} \dot {q} _ {i} \dot {q} _ {j} = 2 T\tag{7.97}
$$

where the last step follows from $(7.94)$ . Therefore

$$
\mathcal {H} = \sum_ {i} p _ {i} \dot {q} _ {i} - \mathscr {L} = 2 T - (T - U) = T + U.\tag{7.98}
$$

That is, provided the transformation between the Cartesian and generalized coordinates is time-independent, as in (7.91), the Hamiltonian $\mathcal{H}$ is just the total energy of the system.

I have already proved that, provided the Lagrangian is independent of time, the Hamiltonian is conserved. Thus we now see that time independence of the Lagrangian [together with the condition (7.91)] implies conservation of energy. We can rephrase the time independence of $\mathcal{L}$ by saying that $\mathcal{L}$ is unchanged by translations of time, $t\to t + \epsilon$ . Thus the result we have just proved is that invariance of $\mathcal{L}$ under time translations is related to energy conservation, in much the same way that invariance of $\mathcal{L}$ under translations of space $(\mathbf{r}\rightarrow \mathbf{r} + \epsilon)$ is related to conservation of momentum. Both results are manifestations of Noether's famous theorem.

## 7.9 Lagrange's Equations for Magnetic Forces\*

\* This section requires a knowledge of the scalar and vector potentials of electromagnetism. Although the ideas described here play an important role in the quantum-mechanical treatment of magnetic fields, they will not be used again in this book.

Although I have so far consistently defined the Lagrangian as $L = T - U$ , there are systems, such as a charged particle in a magnetic field, which can be treated by the Lagrangian method, but for which L is not just T - U. The natural question to ask is then: What is the definition of the Lagrangian for such systems? This is the first question I address.

## Definition and Nonuniqueness of the Lagrangian

Probably the most satisfactory general definition of a Lagrangian for a mechanical system is this:

## General Definition of a Lagrangian

For a given mechanical system with generalized coordinates $q = (q_{1}, \cdots, q_{n})$ , a Lagrangian L is a function $\mathcal{L}(q_{1}, \cdots, q_{n}, \dot{q}_{1}, \cdots, \dot{q}_{n}, t)$ of the coordinates and velocities, such that the correct equations of motion for the system are the Lagrange equations

$$
\frac {\partial \mathcal {L}}{\partial q _ {i}} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {q} _ {i}} \quad [ i = 1, \dots , n ].
$$

In other words, a Lagrangian is any function $\mathcal{L}$ for which Lagrange's equations are true for the system under consideration.

Obviously, for the systems that we have discussed so far, the old definition $L = T - U$ fits this new definition. But the new definition is much more general. In particular, it is easy to see that our new definition does not define a unique Lagrangian function. For example, consider a single particle in one dimension and suppose that we have found a Lagrangian L for this particle. That is, the equation of motion of the particle is

$$
\frac {\partial \mathcal {L}}{\partial x} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {x}}.\tag{7.99}
$$

Now let $f(x, \dot{x})$ be any function for which

$$
\frac {\partial f}{\partial x} \equiv \frac {d}{d t} \frac {\partial f}{\partial \dot {x}}.\tag{7.100}
$$

(It is easy to think up such a function, for instance, $f = x\dot{x}$ .) If we replace $\mathcal{L}$ in (7.99) by

$$
\mathcal {L} ^ {\prime} = \mathcal {L} + f
$$

then, by virtue of (7.100), the Lagrangian $\mathcal{L}'$ gives exactly the same equation of motion as $\mathcal{L}$ .

The lack of uniqueness of the Lagrangian is similar to, though more radical than, the familiar lack of uniqueness in the potential energy (to which one can add any constant without changing any of the physical predictions). The crucial point is that any function $\mathcal{L}$ which gives the right equation of motion has all of the features that we require of a Lagrangian (for instance, that the integral $\int \mathcal{L} dt$ is stationary at the right path) and so is just as acceptable as any other such function $\mathcal{L}$ . If, for a given system, we can spot a function $\mathcal{L}$ that leads to the right equation of motion, then we don't need to debate whether it is the "right" Lagrangian — if it gives the right equation of motion, then it is just as right as any other conceivable Lagrangian.

## Lagrangian for a Charge in a Magnetic Field

Consider now a particle (mass m and charge q) moving in electric and magnetic fields E and B. The force on the particle is the well-known Lorentz force $\mathbf{F}=q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$ , so Newton's second law reads

$$
m \ddot {\mathbf {r}} = q (\mathbf {E} + \dot {\mathbf {r}} \times \mathbf {B}).\tag{7.101}
$$

To reformulate (7.101) in Lagrangian form, we have only to spot a function L for which the three Lagrange equations are the same as (7.101). This can be done using the scalar and vector potentials, $V(\mathbf{r}, t)$ and $\mathbf{A}(\mathbf{r}, t)$ , in terms of which the two fields can be written $^{14}$

$$
\mathbf {E} = - \nabla V - \frac {\partial \mathbf {A}}{\partial t} \quad \text { and } \quad \mathbf {B} = \nabla \times \mathbf {A}.\tag{7.102}
$$

I now claim that the Lagrangian function $^{15}$

$$
\begin{array}{r l} \mathcal {L} (\mathbf {r}, \dot {\mathbf {r}}, t) & = \frac {1}{2} m \dot {\mathbf {r}} ^ {2} - q (V - \dot {\mathbf {r}} \cdot \mathbf {A}) \\ & = \frac {1}{2} m (\dot {x} ^ {2} + \dot {y} ^ {2} + \dot {z} ^ {2}) - q (V - \dot {x} A _ {x} - \dot {y} A _ {y} - \dot {z} A _ {z}) \end{array}\tag{7.103}
$$

(7.104)

has the desired property, that it reproduces Newton's second law (7.101). To check this, let us examine the first of the three Lagrange equations,

$$
\frac {\partial \mathcal {L}}{\partial x} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {x}}.\tag{7.105}
$$

To see what this implies we have to evaluate the two derivatives of the proposed Lagrangian (7.104):

$$
\frac {\partial \mathcal {L}}{\partial x} = - q \left(\frac {\partial V}{\partial x} - \dot {x} \frac {\partial A _ {x}}{\partial x} - \dot {y} \frac {\partial A _ {y}}{\partial x} - \dot {z} \frac {\partial A _ {z}}{\partial x}\right)\tag{7.106}
$$

and

$$
\frac {\partial \mathcal {L}}{\partial \dot {x}} = m \dot {x} + q A _ {x}.
$$

When we differentiate this with respect to t, we must remember that $A_{x}=A_{x}(x,y,z,t)$ . As t varies, x,y,z move with the particle and, by the chain rule, we find

$$
\frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {x}} = m \ddot {x} + q \left(\dot {x} \frac {\partial A _ {x}}{\partial x} + \dot {y} \frac {\partial A _ {x}}{\partial y} + \dot {z} \frac {\partial A _ {x}}{\partial z} + \frac {\partial A _ {x}}{\partial t}\right).\tag{7.107}
$$

Substituting (7.106) and (7.107) into (7.105), cancelling the two terms in $\dot{x}$ , and rearranging, we find that Lagrange's equation (the $x$ component, with the proposed Lagrangian) is the same as

$$
m \ddot {x} = - q \left(\frac {\partial V}{\partial x} + \frac {\partial A _ {x}}{\partial t}\right) + q \dot {y} \left(\frac {\partial A _ {y}}{\partial x} - \frac {\partial A _ {x}}{\partial y}\right) - q \dot {z} \left(\frac {\partial A _ {x}}{\partial z} - \frac {\partial A _ {z}}{\partial x}\right)\tag{7.108}
$$

or, according to (7.102),

$$
m \ddot {x} = q \left(E _ {x} + \dot {y} B _ {z} - \dot {z} B _ {y}\right)\tag{7.109}
$$

which you will recognize as the $x$ component of Newton's second law (7.101). Since the $y$ and $z$ components work in the same way, we conclude that Lagrange's equations, with the proposed Lagrangian (7.104), are exactly equivalent to Newton's second law for the charged particle. That is, we have successfully recast Newton's second law for a charged particle into Lagrangian form with the Lagrangian (7.104).

Using the Lagrangian (7.104), one can solve various problems involving charged particles in electric and magnetic fields. (See Problem 7.49 for an example.) Theoretically, the most important conclusion of this analysis emerges when we evaluate the generalized momentum. For example,

$$
p _ {x} = \frac {\partial \mathcal {L}}{\partial \dot {x}} = m \dot {x} + q A _ {x}.
$$

Since the y and z components work the same way, we conclude that

$$
(\text { generalized   momentum }, \mathbf {p}) = m \mathbf {v} + q \mathbf {A}.\tag{7.110}
$$

That is, the generalized momentum is the mechanical momentum $m\mathbf{v}$ plus a magnetic term $q\mathbf{A}$ . This result is at the heart of the quantum theory of a charged particle in a magnetic field, where it turns out that the generalized momentum corresponds to the differential operator $-i\hbar\nabla$ (where $\hbar$ is Planck's constant over $2\pi$ ), so that the quantum analog of the mechanical momentum $m\mathbf{v}$ is the operator $-i\hbar\nabla - q\mathbf{A}$ .

## 7.10 Lagrange Multipliers and Constraint Forces

\* The method of Lagrange multipliers is used in many areas of physics. Nevertheless, we shan't be using it again in this book, and you could omit this section without any loss of continuity.

In this section, we discuss the method of Lagrange multipliers. This powerful method finds application in several areas of physics and takes on quite different appearances in different contexts. Here I shall treat only its application to Lagrangian mechanics, $^{16}$ and to keep the analysis simple I shall restrict the discussion to two-dimensional systems with just one degree of freedom.

We have seen that one of the strengths of Lagrangian mechanics is that it can bypass all of the forces of constraint. However, there are situations where one actually needs to know these forces. For example, the designer of a roller coaster needs to know the normal force of the track on the car to know how strong to build the track. In this case, we can still use a modified form of Lagrange's equations, but the procedure is somewhat different: We do not choose generalized coordinates $q_{1}, \cdots, q_{n}$ all of which can be independently varied. (Remember that it was the independence of $q_{1}, \cdots, q_{n}$ that let us use the standard Lagrange equations without worrying about constraints.) Instead we use a larger number of coordinates and use Lagrange multipliers to handle the constraints.

To illustrate this procedure, we'll consider a system with just two rectangular coordinates $x$ and $y$ , which are restricted by a constraint equation of the form $^{17}$

$$
f (x, y) = \text { const. }\tag{7.111}
$$

For example, we could consider a simple pendulum with just one degree of freedom (as in Figure 7.2). In treating this by the standard Lagrange approach one would use the one generalized coordinate $\phi$ , the angle between the pendulum and the vertical, and avoid any discussion of the constraints. If, instead, we choose to use the original rectangular coordinates x and y, then we must recognize that these coordinates are not independent; they satisfy the constraint equation

$$
f (x, y) = \sqrt {x ^ {2} + y ^ {2}} = l
$$

where l is the length of the pendulum. We shall find that the method of Lagrange multipliers lets us accommodate this constraint, determine the time dependence of x and y, and find the tension in the rod. As a second example, consider the Atwood machine of Figure 7.6. In our previous treatment we used the one generalized coordinate x, the position of the mass $m_{1}$ , but we could instead use both coordinates x and y (the positions of both masses), provided we remember that the constancy of the string's length imposes the constraint that

$$
f (x, y) = x + y = \text { const }.
$$

Here too, Lagrange multipliers will let us accommodate this constraint, solve for the time dependence of x and y, and find the constraint force, which is here the tension in the string.

To set up our new method we start from Hamilton's principle. Our Lagrangian has the form $\mathcal{L}(x, \dot{x}, y, \dot{y})$ . (We could allow it to have an explicit dependence on $t$ as well, but to simplify notation I shall assume it doesn't.) The proof of Hamilton's principle given in Section 7.4 applies even when the coordinates are constrained. (Indeed it was designed to allow for constraints.) Thus we can conclude as before that the action integral

$$
S = \int_ {t _ {1}} ^ {t _ {2}} \mathcal {L} (x, \dot {x}, y, \dot {y}) d t\tag{7.112}
$$

is stationary when taken along the actual path followed. If we denote this “right” path by $x(t)$ , $y(t)$ and imagine a small displacement to a neighboring “wrong” path,

$$
\left. \begin{array}{l} x (t) \to x (t) + \delta x (t) \\ y (t) \to y (t) + \delta y (t) \end{array} \right\}\tag{7.113}
$$

then, provided the displacement is consistent with the constraint equation, the action integral (7.112) is unchanged, $\delta S = 0$ . To exploit this, we must write $\delta S$ in terms of the small displacements $\delta x$ and $\delta y$ :

$$
\delta S = \int \left(\frac {\partial \mathcal {L}}{\partial x} \delta x + \frac {\partial \mathcal {L}}{\partial \dot {x}} \delta \dot {x} + \frac {\partial \mathcal {L}}{\partial y} \delta y + \frac {\partial \mathcal {L}}{\partial \dot {y}} \delta \dot {y}\right) d t.\tag{7.114}
$$

The second and fourth terms can be integrated by parts, and we conclude that

$$
\delta S = \int \left(\frac {\partial \mathcal {L}}{\partial x} - \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {x}}\right) \delta x d t + \int \left(\frac {\partial \mathcal {L}}{\partial y} - \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {y}}\right) \delta y d t = 0\tag{7.115}
$$

for any displacements $\delta x$ and $\delta y$ consistent with the constraints.

If (7.115) were true for any displacements, we could immediately prove two separate Lagrange equations, one for $x$ and one for $y$ . (Choosing 6.2.0), we would be left with just the first integral; since this has to vanish for any choice of 6.2, the factor in parentheses would have to be zero, which implies the usual Lagrange equation with respect to $x$ . And similarly for $y$ .) This is exactly the correct conclusion for the case that there are no constraints.

However, there are constraints, and (7.115) is only true for displacements $\delta x$ and $\delta y$ consistent with the constraints. Therefore, we proceed as follows: Since all points with which we are concerned satisfy $f(x,y)=\text{const}$ , the displacement (7.113) leave $f(x,y)$ unchanged, so

$$
\delta f = \frac {\partial f}{\partial x} \delta x + \frac {\partial f}{\partial y} \delta y = 0\tag{7.116}
$$

for any displacement consistent with the constraints. Since this is zero, we can multiply it by an arbitrary function $\lambda(t)$ -- this is the Lagrange multiplier and add it to the integrand in (7.115), without changing the value of the integral (namely zero). Therefore

$$
\begin{array}{r l} \delta S & = \int \left(\frac {\partial \mathcal {L}}{\partial x} + \lambda (t) \frac {\partial f}{\partial x} - \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {x}}\right) \delta x d t \\ & + \int \left(\frac {\partial \mathcal {L}}{\partial y} + \lambda (t) \frac {\partial f}{\partial y} - \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {y}}\right) \delta y d t = 0 \end{array}\tag{7.117}
$$

for any displacement consistent with the constraints. Now comes the supreme cunning: So far $\lambda(t)$ is an arbitrary function of $t$ , but we can choose it so that the coefficient of $\delta x$ in the first integral is zero. That is, by choice of the multiplier $\lambda(t)$ , we can arrange that

$$
\frac {\partial \mathcal {L}}{\partial x} - i. \frac {\partial f}{\partial x} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {x}}\tag{7.118}
$$

along the actual path of the system. This is the first of two modified Lagrange equations and differs from the usual equation only by the extra term involving $\lambda$ on the left. With the multiplier chosen in this way, the whole first integral in (7.117) is zero. Therefore the second integral is also zero (since their sum is), and this is true for any choice of $\delta y$ . (The constraint places no restriction on $\delta x$ or $\delta y$ separately — it only fixes $\delta x$ once $\delta y$ is chosen, or vice versa.) Therefore the coefficient of $\delta y$ in this second integral must also be zero and we have a second modified Lagrange equation,

$$
\frac {\partial \mathcal {L}}{\partial y} + \lambda \frac {\partial f}{\partial y} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {y}}.\tag{7.119}
$$

We now have two modified Lagrange equations for the two unknown functions $x(t)$ and $y(t)$ . This elegant result has been bought at the price of introducing a third unknown function, the Lagrange multiplier $\lambda(t)$ . To find three unknown functions, we need three equations, but fortunately a third equation is already at hand, the constraint equation

$$
f (x, y) = \text { const. }\tag{7.120}
$$

The three equations (7.118), (7.119), and (7.120) are sufficient, in principle at least, to determine the coordinates $x(t)$ and $y(t)$ and the multiplier $\lambda(t)$ . Before we illustrate this with an example, there is one more bit of theory to develop.

So far the Lagrange multiplier $\lambda(t)$ is just a mathematical artifact, introduced to help us solve our problem. However, it turns out to be closely related to the forces of constraint. To see this, we have only to look more closely at the modified Lagrange equations (7.118) and (7.119). The Lagrangian of our present discussion has the form

$$
\mathcal {L} = \frac {1}{2} m _ {1} \dot {x} ^ {2} + \frac {1}{2} m _ {2} \dot {y} ^ {2} - U (x, y).
$$

(In a problem like the simple pendulum, x and y are the two coordinates of a single mass and $m_{1}=m_{2}$ . In a problem like the Atwood machine, there are two separate masses and $m_{1}$ and $m_{2}$ are not necessarily equal.) Inserting this Lagrangian into (7.118), we find

$$
- \frac {\partial U ^ {\prime}}{\partial x} + \lambda \frac {\partial f}{\partial x} = m _ {1} \ddot {x}.\tag{7.121}
$$

Now, on the left side $-\partial U/\partial x$ is the x component of the nonconstraint force. (Remember that U was defined as the potential energy of the nonconstraint forces.) On the right, $m_{1}\ddot{x}$ is the x component of the total force, equal to the sum of the nonconstraint and constraint forces. Thus $m_{1}\ddot{x} = -\partial U/\partial x + F_{x}^{cstr}$ . Canceling the term $-\partial U/\partial x$ from both sides of (7.121), we reach the important conclusion that

$$
\lambda \frac {\partial f}{\partial x} = F _ {x} ^ {\mathrm{cstr}}\tag{7.122}
$$

with a corresponding result for the y components. This then is the significance of the Lagrange multiplier: Multiplied by the appropriate partial derivatives of the constraint function $f(x, y)$ , the Lagrange multiplier $\lambda(t)$ gives the corresponding components of the constraint force.

Let us now see how these ideas work in practice by using the formalism to analyse the example of the Atwood machine.

## EXAMPLE 7.8 Atwood's Machine Using a Lagrange Multiplier

Analyze the Atwood machine of Figure 7.6 (shown again here as Figure 7.11) by the method of Lagrange multipliers and using the coordinates $x$ and $y$ of the two masses.

In terms of the given coordinates, the Lagrangian is

$$
\mathcal {L} = T - U = \frac {1}{2} m _ {1} \dot {x} ^ {2} + \frac {1}{2} m _ {2} \dot {y} ^ {2} + m _ {1} g x + m _ {2} g y\tag{7.123}
$$

and the constraint equation is

$$
f (x, y) = x + y = \mathrm{const}.\tag{7.124}
$$

The modified Lagrange equation (7.118) for x reads

$$
\frac {\partial \mathcal {L}}{\partial x} + \lambda \frac {\partial f}{\partial x} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {x}} \quad \text { or } \quad m _ {1} g + \lambda = m _ {1} \ddot {x}\tag{7.125}
$$

and that for $y$ is

$$
\frac {\partial \mathcal {L}}{\partial y} + \lambda \frac {\partial f}{\partial y} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {y}} \quad \text { or } \quad m _ {2} g + \lambda = m _ {2} \ddot {y}.\tag{7.126}
$$

These two equations, together with the constraint equation (7.124), are easily solved for the unknowns $x(t)$ , $y(t)$ , and $\lambda(t)$ . From (7.124) we see that $\ddot{y} = -\ddot{x}$ , and then subtracting (7.126) from (7.125) we can eliminate $\lambda$ and arrive at the same result as before,

$$
\ddot {x} = (m _ {1} - m _ {2}) g / (m _ {1} + m _ {2}).
$$

To better understand the two modified Lagrange equations (7.125) and (7.126), it is helpful to compare them with the two equations of the Newtonian solution. Newton's second law for $m_1$ is

$$
m _ {1} g - F _ {\mathrm{t}} = m _ {1} \ddot {x}
$$

![](images/79eb5776752cc6847ea43a303be0606826dafdef66a93bcaf6ee53b23fe02bba.jpg)  
Figure 7.11 The Atwood machine again.

where $F_{t}$ is the tension in the string, and that for $m_{2}$ is

$$
m _ {2} g - F _ {\mathrm{t}} = m _ {2} \ddot {y}.
$$

These are precisely the two Lagrange equations (7.125) and (7.126), with the Lagrange multiplier identified as the constraint force

$$
\lambda = - F _ {\mathrm{t}}.
$$

[Two small comments: The minus sign occurs because both coordinates $x$ and $y$ were measured downward, whereas both tension forces are upward. In general, according to (7.122) the constraint force is $\lambda \partial f / \partial x$ , but in this simple case, $\partial f / \partial x = 1$ .]

You can find some more examples of the use of Lagrange multipliers in Problems 7.50 through 7.52.

## Principal Definitions and Equations of Chapter 7

## The Lagrangian

The Lagrangian $\mathcal{L}$ of a conservative system is defined as

$$
\mathcal {L} = T - U,\tag{[Eq. (7.3)]}
$$

where T and U are respectively the kinetic and potential energies.

## Generalized Coordinates

The n parameters $q_{1}, \cdots, q_{n}$ are generalized coordinates for an N-particle system if every particle's position $r_{\alpha}$ can be expressed as a function of $q_{1}, \cdots, q_{n}$ (and possibly the time t) and vice versa, and if n is the smallest number that allows the system to be described in this way. [Eqs. (7.34) & (7.35)]

If $n < 3N$ (in three dimensions) the system is said to be constrained. The coordinates $q_1, \cdots, q_n$ are said to be natural if the functional relationships of the $\mathbf{r}_{\alpha}$ to $q_1, \cdots, q_n$ are independent of time. The number of degrees of freedom of a system is the number of coordinates that can be independently varied. If the number of degrees of freedom is equal to the number of generalized coordinates (in some sense the "normal" state of affairs), the system is said to be holonomic. [Section 7.3]

## Lagrange's Equations

For any holonomic system, Newton's second law is equivalent to the $n$ Lagrange equations

$$
\frac {\partial \mathcal {L}}{\partial q _ {i}} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {q} _ {i}} \quad [ i = 1, \dots , n ] \quad [ \text { Sections   7.3 } \& 7. 4 ]
$$

and the Lagrange equations are in turn equivalent to Hamilton's principle — a fact we used only to prove the Lagrange equations. [Eq. (7.8)]

## Generalized Momenta and Ignorable Coordinates

The ith generalized momentum $p_{i}$ is defined to be the derivative

$$
p _ {i} = \frac {\partial \mathcal {L}}{\partial \dot {q} _ {i}}.
$$

If $\partial \mathcal{L} / \partial q_i = 0$ , then we say the coordinate $q_i$ is ignorable and the corresponding generalized momentum is constant. [Section 7.6]

## The Hamiltonian

The Hamiltonian is defined as

$$
\mathcal {H} = \sum_ {i = 1} ^ {n} p _ {i} \dot {q} _ {i} - \mathcal {L}.\tag{[Eq. (7.90)]}
$$

If $\partial\mathcal{L}/\partial t=0$ , then H is conserved; if the coordinates $q_{1},\cdots,q_{n}$ are natural, H is just the energy of the system.

## Lagrangian for a Charge in an Electromagnetic Field

The Lagrangian for a charge q in an electromagnetic field is

$$
\mathcal {L} (\mathbf {r}, \dot {\mathbf {r}}, t) = \frac {1}{2} m \dot {\mathbf {r}} ^ {2} - q (V - \dot {\mathbf {r}} \cdot \mathbf {A}).\tag{[Eq. (7.103)]}
$$

## Problems for Chapter 7

Stars indicate the approximate level of difficulty, from easiest ( $\star$ ) to most difficult ( $\star\star\star$ ).

## SECTION 7.1 Lagrange's Equations for Unconstrained Motion

7.1 $\star$ Write down the Lagrangian for a projectile (subject to no air resistance) in terms of its Cartesian coordinates $(x, y, z)$ , with $z$ measured vertically upward. Find the three Lagrange equations and show that they are exactly what you would expect for the equations of motion.

7.2\* Write down the Lagrangian for a one-dimensional particle moving along the $x$ axis and subject to a force $F = -kx$ (with $k$ positive). Find the Lagrange equation of motion and solve it.

7.3\* Consider a mass $m$ moving in two dimensions with potential energy $U(x, y) = \frac{1}{2} kr^2$ , where $r^2 = x^2 + y^2$ . Write down the Lagrangian, using coordinates $x$ and $y$ , and find the two Lagrange equations of motion. Describe their solutions. [This is the potential energy of an ion in an "ion trap," which can be used to study the properties of individual atomic ions.]

7.4\* Consider a mass $m$ moving in a frictionless plane that slopes at an angle $\alpha$ with the horizontal. Write down the Lagrangian in terms of coordinates $x$ , measured horizontally across the slope, and $y$ , measured down the slope. (Treat the system as two-dimensional, but include the gravitational potential energy.) Find the two Lagrange equations and show that they are what you should have expected.

7.5 \* Find the components of $\nabla f(r, \phi)$ in two-dimensional polar coordinates. [Hint: Remember that the change in the scalar f as a result of an infinitesimal displacement dr is $df = \nabla f \cdot dr$ .]

7.6\* Consider two particles moving unconstrained in three dimensions, with potential energy $U^{\prime}(\mathbf{r}_1,\mathbf{r}_2)$ . (a) Write down the six equations of motion obtained by applying Newton's second law to each particle. (b) Write down the Lagrangian $\mathcal{L}(\mathbf{r}_1,\mathbf{r}_2,\dot{\mathbf{r}}_1,\dot{\mathbf{r}}_2) = T - U$ and show that the six Lagrange equations are the same as the six Newtonian equations of part (a). This establishes the validity of Lagrange's equations in rectangular coordinates, which in turn establishes Hamilton's principle. Since the latter is independent of coordinates, this proves Lagrange's equations in any coordinate system.

7.7 \* Do Problem 7.6, but for $N$ particles moving unconstrained in three dimensions (in which case there are $3N$ equations of motion).

7.8\*\* (a) Write down the Lagrangian $\mathcal{L}(x_1, x_2, \dot{x}_1, \dot{x}_2)$ for two particles of equal masses, $m_1 = m_2 = m$ , confined to the $x$ axis and connected by a spring with potential energy $U = \frac{1}{2} kx^2$ . [Here $x$ is the extension of the spring, $x = (x_1 - x_2 - l)$ , where $l$ is the spring's unstretched length, and I assume that mass 1 remains to the right of mass 2 at all times.] (b) Rewrite $\mathcal{L}$ in terms of the new variables $X = (x_1 - x_2)$ (the CM position) and $x$ (the extension), and write down the two Lagrange equations for $X$ and $x$ . (c) Solve for $X(t)$ and $x(t)$ and describe the motion.

## SECTION 7.3 Constrained Systems in General

7.9 \* Consider a bead that is threaded on a rigid circular hoop of radius $R$ lying in the $xy$ plane with its center at $O$ , and use the angle $\phi$ of two-dimensional polar coordinates as the one generalized coordinate to describe the bead's position. Write down the equations that give the Cartesian coordinates $(x, y)$ in terms of $\phi$ and the equation that gives the generalized coordinate $\phi$ in terms of $(x, y)$ .

7.10 \* A particle is confined to move on the surface of a circular cone with its axis on the z axis, vertex at the origin (pointing down), and half-angle $\alpha$ . The particle's position can be specified by two generalized coordinates, which you can choose to be the coordinates $(\rho, \phi)$ of cylindrical polar coordinates. Write down the equations that give the three Cartesian coordinates of the particle in terms of the generalized coordinates $(\rho, \phi)$ and vice versa.

7.11 \* Consider the pendulum of Figure 7.4, suspended inside a railroad car, but suppose that the car is oscillating back and forth, so that the point of suspension has position $x_{s} = A \cos \omega t$ , $y_{s} = 0$ . Use the angle $\phi$ as the generalized coordinate and write down the equations that give the Cartesian coordinates of the bob in terms of $\phi$ and vice versa.

## SECTION 7.4 Proof of Lagrange's Equations with Constraints

7.12 \* Lagrange's equations in the form discussed in this chapter hold only if the forces (at least the nonconstraint forces) are derivable from a potential energy. To get an idea how they can be modified to include forces like friction, consider the following: A single particle in one dimension is subject to various conservative forces (net conservative force = $F = -\partial U / \partial x$ ) and a nonconservative force (let's call it $F_{\mathrm{fric}}$ ). Define the Lagrangian as $\mathcal{L} = T - U$ and show that the appropriate modification is

![](images/0e1eac24957ea02f77af4cdb2adbee1530e402bae39d0e5d2b410d201cb0f027.jpg)  
Figure 7.12 Problem 7.14

$$
\frac {\partial \mathcal {L}}{\partial x} + F _ {\text { f   r   i   c }} = \frac {d}{d t} \frac {\partial \mathcal {L}}{\partial \dot {x}}.
$$

7.13\*\* In Section 7.4 [Equations (7.41) through (7.51)], I proved Lagrange's equations for a single particle constrained to move on a two-dimensional surface. Go through the same steps to prove Lagrange's equations for a system consisting of two particles subject to various unspecified constraints. [Hint: The net force on particle 1 is the sum of the total constraint force $\mathbf{F}_1^{\mathrm{estr}}$ and the total nonconstraint force $\mathbf{F}_1$ , and likewise for particle 2. The constraint forces come in many guises (the normal force of a surface, the tension force of a string tied between the particles, etc.), but it is always true that the net work done by all constraint forces in any displacement consistent with the constraints is zero — this is the defining property of constraint forces. Meanwhile, we take for granted that the nonconstraint forces are derivable from a potential energy $U(\mathbf{r}_1,\mathbf{r}_2,t)$ ; that is, $\mathbf{F}_1 = -\nabla_1U$ and likewise for particle 2. Write down the difference $\delta S$ between the action integral for the right path given by $\mathbf{r}_1(t)$ and $\mathbf{r}_2(t)$ and any nearby wrong path given by $\mathbf{r}_1(t) + \epsilon_1(t)$ and $\mathbf{r}_2(t) + \epsilon_2(t)$ . Paralleling the steps of Section 7.4, you can show that $\delta S$ is given by an integral analogous to (7.49), and this is zero by the defining property of constraint forces.]

## SECTION 7.5 Examples of Lagrange's Equations

7.14★ Figure 7.12 shows a crude model of a yoyo. A massless string is suspended vertically from a fixed point and the other end is wrapped several times around a uniform cylinder of mass m and radius R. When the cylinder is released it moves vertically down, rotating as the string unwinds. Write down the Lagrangian, using the distance x as your generalized coordinate. Find the Lagrange equation of motion and show that the cylinder accelerates downward with $\ddot{x}=2g/3$ . [Hints: You need to remember from your introductory physics course that the total kinetic energy of a body like the yoyo is $T=\frac{1}{2}mv^{2}+\frac{1}{2}I\omega^{2}$ , where v is the velocity of the center of mass, I is the moment of inertia (for a uniform cylinder, $I=\frac{1}{2}mR^{2}$ ) and $\omega$ is the angular velocity about the CM. You can express $\omega$ in terms of $\dot{x}$ .]

7.15★ A mass $m_{1}$ rests on a frictionless horizontal table and is attached to a massless string. The string runs horizontally to the edge of the table, where it passes over a massless, frictionless pulley and then hangs vertically down. A second mass $m_{2}$ is now attached to the bottom end of the string. Write down the Lagrangian for the system. Find the Lagrange equation of motion, and solve it for the acceleration of the blocks. For your generalized coordinate, use the distance x of the second mass below the tabletop.

7.16 \* Write down the Lagrangian for a cylinder (mass m, radius R, and moment of inertia I) that rolls without slipping straight down an inclined plane which is at an angle $\alpha$ from the horizontal. Use as your generalized coordinate the cylinder's distance x measured down the plane from its starting point. Write down the Lagrange equation and solve it for the cylinder's acceleration $\ddot{x}$ . Remember that $T = \frac{1}{2}mv^{2} + \frac{1}{2}I\omega^{2}$ , where v is the velocity of the center of mass and $\omega$ is the angular velocity.

7.17 \* Use the Lagrangian method to find the acceleration of the Atwood machine of Example 7.3 (page 255) including the effect of the pulley's having moment of inertia I. (The kinetic energy of the pulley is $\frac{1}{2}I\omega^{2}$ , where $\omega$ is its angular velocity.)

7.18 \* A mass $m$ is suspended from a massless string, the other end of which is wrapped several times around a horizontal cylinder of radius $R$ and moment of inertia $I$ , which is free to rotate about a fixed horizontal axle. Using a suitable coordinate, set up the Lagrangian and the Lagrange equation of motion, and find the acceleration of the mass $m$ . [The kinetic energy of the rotating cylinder is $\frac{1}{2} I\omega^2$ .]

7.19 \* In Example 7.5 (page 258) the two accelerations are given by Equations (7.66) and (7.67). Check that the acceleration of the block is given correctly in the limit $M \to 0$ . [You need to find the components of this acceleration relative to the table.]

7.20 \* A smooth wire is bent into the shape of a helix, with cylindrical polar coordinates $\rho = R$ and $z = \lambda \phi$ , where $R$ and $\lambda$ are constants and the $z$ axis is vertically up (and gravity vertically down). Using $z$ as your generalized coordinate, write down the Lagrangian for a bead of mass $m$ threaded on the wire. Find the Lagrange equation and hence the bead's vertical acceleration $\ddot{z}$ . In the limit that $R \to 0$ , what is $\ddot{z}$ ? Does this make sense?

7.21 \* The center of a long frictionless rod is pivoted at the origin, and the rod is forced to rotate in a horizontal plane with constant angular velocity $\omega$ . Write down the Lagrangian for a bead of mass $m$ threaded on the rod, using $r$ as your generalized coordinate, where $r, \phi$ are the polar coordinates of the bead. (Notice that $\phi$ is not an independent variable since it is fixed by the rotation of the rod to be $\phi = \omega t$ .) Solve Lagrange's equation for $r(t)$ . What happens if the bead is initially at rest at the origin? If it is released from any point $r_0 > 0$ , show that $r(t)$ eventually grows exponentially. Explain your results in terms of the centrifugal force $m\omega^2 r$ .

7.22 \* Using the usual angle $\phi$ as generalized coordinate, write down the Lagrangian for a simple pendulum of length $l$ suspended from the ceiling of an elevator that is accelerating upward with constant acceleration $a$ . (Be careful when writing $T$ ; it is probably safest to write the bob's velocity in component form.) Find the Lagrange equation of motion and show that it is the same as that for a normal, nonaccelerating pendulum, except that $g$ has been replaced by $g + a$ . In particular, the angular frequency of small oscillations is $\sqrt{(g + a) / l}$ .

7.23 \* A small cart (mass m) is mounted on rails inside a large cart. The two are attached by a spring (force constant k) in such a way that the small cart is in equilibrium at the midpoint of the large. The distance of the small cart from its equilibrium is denoted x and that of the large one from a fixed point on the ground is X, as shown in Figure 7.13. The large cart is now forced to oscillate such that $X = A \cos \omega t$ , with both A and $\omega$ fixed. Set up the Lagrangian for the motion of the small cart and show that the Lagrange equation has the form

$$
\ddot {x} + \omega_ {\mathrm{o}} ^ {2} x = B \cos \omega t
$$

where $\omega_{0}$ is the natural frequency $\omega_{0}=\sqrt{k/m}$ and B is a constant. This is the form assumed in Section 5.5, Equation (5.57), for driven oscillations (except that we are here ignoring damping). Thus the system described here would be one way to realize the motion discussed there. (We could fill the large cart with molasses to provide some damping.)

![](images/68f51a13923bcef779ed762cf801495185be5fea621b57f9140213b5b31bbcc8.jpg)  
Figure 7.13 Problem 7.23

7.24\* We saw in Example 7.3 (page 255) that the acceleration of the Atwood machine is $\ddot{x} = (m_1 - m_2)g / (m_1 + m_2)$ . It is sometimes claimed that this result is "obvious" because, it is said, the effective force on the system is $(m_1 - m_2)g$ and the effective mass is $(m_1 + m_2)$ . This is not, perhaps, all that obvious, but it does emerge very naturally in the Lagrangian approach. Recall that Lagrange's equation can be thought of as [Equation (7.17)]

(generalized force) = (rate of change of generalized momentum).

Show that for the Atwood machine the generalized force is $(m_{1}-m_{2})g$ and the generalized momentum $(m_{1}+m_{2})\dot{x}$ . Comment.

7.25 $\star$ Prove that the potential energy of a central force $\mathbf{F} = -kr^n\hat{\mathbf{r}}$ (with $n\neq -1$ ) is $U = kr^{n + 1}/(n + 1)$ if we choose the zero of $U$ appropriately. In particular, if $n = 1$ , then $\mathbf{F} = -kr$ and $U = \frac{1}{2} kr^2$ .

7.26 $\star$ In Example 7.7 (page 264), we saw that the bead on a spinning hoop can make small oscillations about any of its stable equilibrium points. Verify that the oscillation frequency $\Omega'$ defined in (7.79) is equal to $\sqrt{\omega^2 - (g / \omega R)^2}$ as claimed in (7.80).

7.27 \*\* Consider a double Atwood machine constructed as follows: A mass $4m$ is suspended from a string that passes over a massless pulley on frictionless bearings. The other end of this string supports a second similar pulley, over which passes a second string supporting a mass of $3m$ at one end and $m$ at the other. Using two suitable generalized coordinates, set up the Lagrangian and use the Lagrange equations to find the acceleration of the mass $4m$ when the system is released. Explain why the top pulley rotates even though it carries equal weights on each side.

7.28 \*\* A couple of points need checking from Example 7.6 (page 260). (a) From the point of view of a noninertial frame rotating with the hoop, the bead is subject to the force of gravity and a centrifugal force $m\omega^2\rho$ (in addition to the constraint force, which is the normal force of the wire). Verify that at the equilibrium points given by (7.71), the tangential components of these two forces balance one another. (A free-body diagram will help.) (b) Verify that the equilibrium point at the top ( $\theta = \pi$ ) is unstable. (c) Verify that the equilibrium at the second point given by (7.71) (the one on the left, with $\theta$ negative) is stable.

7.29 \*\* Figure 7.14 shows a simple pendulum (mass $m$ , length $l$ ) whose point of support $P$ is attached to the edge of a wheel (center $O$ , radius $R$ ) that is forced to rotate at a fixed angular velocity $\omega$ . At $t = 0$ , the point $P$ is level with $O$ on the right. Write down the Lagrangian and find the equation of motion for the angle $\phi$ . [Hint: Be careful writing down the kinetic energy $T$ . A safe way to get the velocity right is to write down the position of the bob at time $t$ , and then differentiate.] Check that your answer makes sense in the special case that $\omega = 0$ .

![](images/592184e8c61a22ad9442a86b18600d39f75c7285b155f5638f1703619c0cd6dc.jpg)  
Figure 7.14 Problem 7.29

7.30 \*\* Consider the pendulum of Figure 7.4, suspended inside a railroad car that is being forced to accelerate with a constant acceleration $a$ . (a) Write down the Lagrangian for the system and the equation of motion for the angle $\phi$ . Use a trick similar to the one used in Equation (5.11) to write the combination of $\sin \phi$ and $\cos \phi$ as a multiple of $\sin (\phi + \beta)$ . (b) Find the equilibrium angle $\phi$ at which the pendulum can remain fixed (relative to the car) as the car accelerates. Use the equation of motion to show that this equilibrium is stable. What is the frequency of small oscillations about this equilibrium position? (We shall find a much slicker way to solve this problem in Chapter 9, but the Lagrangian method does give a straightforward route to the answer.)

7.31 \*\* A simple pendulum (mass $M$ and length $L$ ) is suspended from a cart (mass $m$ ) that can oscillate on the end of a spring of force constant $k$ , as shown in Figure 7.15. (a) Write the Lagrangian in terms of the two generalized coordinates $x$ and $\phi$ , where $x$ is the extension of the spring from its equilibrium length. (Read the hint in Problem 7.29.) Find the two Lagrange equations. (Warning: They're pretty ugly!) (b) Simplify the equations to the case that both $x$ and $\phi$ are small. (They're still pretty ugly, and note, in particular, that they are still coupled; that is, each equation involves both variables. Nonetheless, we shall see how to solve these equations in Chapter 11 — see particularly Problem 11.19.)

![](images/a304b9bee65affb747a1b5253bfc9c62ba655ddaa62534ea26589c2240dfc043.jpg)  
Figure 7.15 Problem 7.31

7.32 \*\* Consider the cube balanced on a cylinder as described in Example 4.7 (page 130). Assuming that $b < r$ , use the Lagrangian approach to find the angular frequency of small oscillations about the top. The simplest procedure is to make the small-angle approximations to $\mathcal{L}$ before you differentiate to get Lagrange's equation. As usual, be careful in writing down the kinetic energy; this is $\frac{1}{2}(mv^2 + I\dot{\theta}^2)$ , where $v$ is the speed of the CM and $I$ is the moment of inertia about the CM ( $2mb^2/3$ ). The safe way to find $v$ is to write down the coordinates of the CM and then differentiate.

7.33 \*\* A bar of soap (mass $m$ ) is at rest on a frictionless rectangular plate that rests on a horizontal table. At time $t = 0$ , I start raising one edge of the plate so that the plate pivots about the opposite edge with constant angular velocity $\omega$ , and the soap starts to slide toward the downhill edge. Show that the equation of motion for the soap has the form $\ddot{x} - \omega^2 x = -g \sin \omega t$ , where $x$ is the soap's distance from the downhill edge. Solve this for $x(t)$ , given that $x(0) = x_0$ . | You'll need to use the method used to solve Equation (5.48). You can easily solve the homogeneous equation; for a particular solution try $x = A \sin \omega t$ and solve for $A$ .]

7.34\*\* Consider the well-known problem of a cart of mass $m$ moving along the $x$ axis attached to a spring (force constant $k$ ), whose other end is held fixed (Figure 5.2). If we ignore the mass of the spring (as we almost always do) then we know that the cart executes simple harmonic motion with angular frequency $\omega = \sqrt{k / m}$ . Using the Lagrangian approach, you can find the effect of the spring's mass $M$ , as follows: (a) Assuming that the spring is uniform and stretches uniformly, show that its kinetic energy is $\frac{1}{6} M\dot{x}^2$ . (As usual $x$ is the extension of the spring from its equilibrium length.) Write down the Lagrangian for the system of cart plus spring. (Note: The potential energy is still $\frac{1}{2} kx^2$ .) (b) Write down the Lagrange equation and show that the cart still executes SHM but with angular frequency $\omega = \sqrt{k / (m + M / 3)}$ ; that is, the effect of the spring's mass $M$ is just to add $M / 3$ to the mass of the cart.

![](images/9a2ab843483acafbc10ad5f46e67d4e7f8b84067cefffee3aa98dea9ca3c2697.jpg)  
Figure 7.16 Problem 7.35

7.35\*\* Figure 7.16 is a bird's-eye view of a smooth horizontal wire hoop that is forced to rotate at a fixed angular velocity $\omega$ about a vertical axis through the point $A$ . A bead of mass $m$ is threaded on the hoop and is free to move around it, with its position specified by the angle $\phi$ that it makes at the center with the diameter $AB$ . Find the Lagrangian for this system using $\phi$ as your generalized coordinate. (Read the hint in Problem 7.29.) Use the Lagrange equation of motion to show that the bead oscillates about the point $B$ exactly like a simple pendulum. What is the frequency of these oscillations if their amplitude is small?

7.36 \*\*\* A pendulum is made from a massless spring (force constant $k$ and unstretched length $l_0$ ) that is suspended at one end from a fixed pivot $O$ and has a mass $m$ attached to its other end. The spring can stretch and compress but cannot bend, and the whole system is confined to a single vertical plane. (a) Write down the Lagrangian for the pendulum, using as generalized coordinates the usual angle $\phi$ and the length $r$ of the spring. (b) Find the two Lagrange equations of the system and interpret them in terms of Newton's second law, as given in Equation (1.48). (c) The equations of part (b) cannot be solved analytically in general. However, they can be solved for small oscillations. Do this and describe the motion. [Hint: Let $l$ denote the equilibrium length of the spring with the mass hanging from it and write $r = l + \epsilon$ . “Small oscillations” involve only small values of $\epsilon$ and $\phi$ , so you can use the small-angle approximations and drop from your equations all terms that involve powers of $\epsilon$ or $\phi$ (or their derivatives) higher than the first power (also products of $\epsilon$ and $\phi$ or their derivatives). This dramatically simplifies and uncouples the equations.]

7.37 \*\*\* Two equal masses, $m_1 = m_2 = m$ , are joined by a massless string of length $L$ that passes through a hole in a frictionless horizontal table. The first mass slides on the table while the second hangs below the table and moves up and down in a vertical line. (a) Assuming the string remains taut, write down the Lagrangian for the system in terms of the polar coordinates $(r, \phi)$ of the mass on the table. (b) Find the two Lagrange equations and interpret the $\phi$ equation in terms of the angular momentum $\ell$ of the first mass. (c) Express $\dot{\phi}$ in terms of $\ell$ and eliminate $\dot{\phi}$ from the $r$ equation. Now use the $r$ equation to find the value $r = r_0$ at which the first mass can move in a circular path. Interpret your answer in Newtonian terms. (d) Suppose the first mass is moving in this circular path and is given a small radial nudge. Write $r(t) = r_0 + \epsilon(t)$ and rewrite the $r$ equation in terms of $\epsilon(t)$ dropping all powers of $\epsilon(t)$ higher than linear. Show that the circular path is stable and that $r(t)$ oscillates sinusoidally about $r_0$ . What is the frequency of its oscillations?

7.38 \*\*\* A particle is confined to move on the surface of a circular cone with its axis on the vertical z axis, vertex at the origin (pointing down), and half-angle $\alpha$ . (a) Write down the Lagrangian L in terms of the spherical polar coordinates r and $\phi$ . (b) Find the two equations of motion. Interpret the $\phi$ equation in terms of the angular momentum $\ell_{z}$ , and use it to eliminate $\dot{\phi}$ from the r equation in favor of the constant $\ell_{z}$ . Does your r equation make sense in the case that $\ell_{z}=0$ ? Find the value $r_{0}$ of r at which the particle can remain in a horizontal circular path. (c) Suppose that the particle is given a small radial kick, so that $r(t)=r_{0}+\epsilon(t)$ , where $\epsilon(t)$ is small. Use the r equation to decide whether the circular path is stable. If so, with what frequency does r oscillate about $r_{0}$ ?

7.39 \*\*\* (a) Write down the Lagrangian for a particle moving in three dimensions under the influence of a conservative central force with potential energy $U(r)$ , using spherical polar coordinates $(r, \theta, \phi)$ . (b) Write down the three Lagrange equations and explain their significance in terms of radial acceleration, angular momentum, and so forth. (The $\theta$ equation is the tricky one, since you will find it implies that the $\phi$ component of $\ell$ varies with time, which seems to contradict conservation of angular momentum. Remember, however, that $\ell_{\phi}$ is the component of $\ell$ in a variable direction.) (c) Suppose that initially the motion is in the equatorial plane (that is, $\theta_0 = \pi/2$ and $\dot{\theta}_0 = 0$ ). Describe the subsequent motion. (d) Suppose instead that the initial motion is along a line of longitude (that is, $\dot{\phi}_0 = 0$ ). Describe the subsequent motion.

7.40 \*\*\* The "spherical pendulum" is just a simple pendulum that is free to move in any sideways direction. (By contrast a "simple pendulum" — unqualified — is confined to a single vertical plane.) The bob of a spherical pendulum moves on a sphere, centered on the point of support with radius $r = R$ , the length of the pendulum. A convenient choice of coordinates is spherical polars, $r, \theta, \phi$ , with the origin at the point of support and the polar axis pointing straight down. The two variables $\theta$ and $\phi$ make a good choice of generalized coordinates. (a) Find the Lagrangian and the two Lagrange equations. (b) Explain what the $\phi$ equation tells us about the $z$ component of angular momentum $\ell_z$ . (c) For the special case that $\phi = \text{const}$ , describe what the $\theta$ equation tells us. (d) Use the $\phi$ equation to replace $\dot{\phi}$ by $\iota_z$ in the $\theta$ equation and discuss the existence of an angle $\theta_0$ at which $\theta$ can remain constant. Why is this motion called a conical pendulum? (e) Show that if $\theta = \theta_0 + \epsilon$ , with $\epsilon$ small, then $\theta$ oscillates about $\theta_0$ in harmonic motion. Describe the motion of the pendulum's bob.

7.41 \*\*\* Consider a bead of mass m sliding without friction on a wire that is bent in the shape of a parabola and is being spun with constant angular velocity $\omega$ about its vertical axis, as shown in Figure

7.17. Use cylindrical polar coordinates and let the equation of the parabola be $z = k\rho^{2}$ . Write down the Lagrangian in terms of $\rho$ as the generalized coordinate. Find the equation of motion of the bead and determine whether there are positions of equilibrium, that is, values of $\rho$ at which the bead can remain fixed, without sliding up or down the spinning wire. Discuss the stability of any equilibrium positions you find.

![](images/9b7fd08ccd16ebe372501856e878850fe8b613dc083532cf655fbbb147e966b7.jpg)  
Figure 7.17 Problem 7.41

7.42 \*\*\* [Computer] In Example 7.7 (page 264), we saw that the bead on a spinning hoop can make small oscillations about its nonzero stable equilibrium points that are approximately sinusoidal, with frequency $\Omega' = \sqrt{\omega^2 - (g / \omega R)^2}$ as in (7.80). Investigate how good this approximation is by solving the equation of motion (7.73) numerically and then plotting both your numerical solution and the approximate solution $\theta(t) = \theta_0 + A\cos(\Omega't - \delta)$ on the same graph. Use the following numbers: $g = R = 1$ and $\omega^2 = 2$ , and initial conditions $\dot{\theta}(0) = 0$ and $\theta(0) = \theta_0 + \epsilon_0$ , where $\epsilon_0 = 1^\circ$ . Repeat with $\epsilon_0 = 10^\circ$ . Comment on your results.

7.43 \*\*\* [Computer] Consider a massless wheel of radius $R$ mounted on a frictionless horizontal axis. A point mass $M$ is glued to the edge, and a massless string is wrapped several times around the perimeter and hangs vertically down with a mass $m$ suspended from its bottom end. (See Figure 4.28.) Initially I am holding the wheel with $M$ vertically below the axle. At $t = 0$ , I release the wheel, and $m$ starts to fall vertically down. (a) Write down the Lagrangian $\mathcal{L} = T - U$ as a function of the angle $\phi$ through which the wheel has turned. Find the equation of motion and show that, provided $m < M$ , there is one position of stable equilibrium. (b) Assuming $m < M$ , sketch the potential energy $U(\phi)$ for $-\pi \leq \phi \leq 4\pi$ and use your graph to explain the equilibrium positions you found. (c) Because the equation of motion cannot be solved in terms of elementary functions, you are going to solve it numerically. This requires that you choose numerical values for the various parameters. Take $M = g = R = 1$ (this amounts to a convenient choice of units) and $m = 0.7$ . Before solving the equation make a careful plot of $U(\phi)$ against $\phi$ and predict the kind of motion expected when $M$ is released from rest at $\phi = 0$ . Now solve the equation of motion for $0 \leq t \leq 20$ and verify your prediction. (d) Repeat part (c), but with $m = 0.8$ .

7.44 \*\*\* [Computer] If you haven't already done so, do Problem 7.29. One might expect that the rotation of the wheel would have little effect on the pendulum, provided the wheel is small and rotates slowly. (a) Verify this expectation by solving the equation of motion numerically, with the following numbers: Take $g$ and $l$ to be 1. (This means that the natural frequency $\sqrt{g / l}$ of the pendulum is also 1.) Take $\omega = 0.2$ , so that the wheel's rotational frequency is small compared to the natural frequency of the pendulum; and take the radius $R = 0.2$ , significantly less than the length of the pendulum. As initial conditions take $\phi = 0.2$ and $\dot{\phi} = 0$ at $t = 0$ , and make a plot of your solution $\phi(t)$ for $0 < t < 20$ . Your graph should look very like the sinusoidal oscillations of an ordinary simple pendulum. Does the period look correct? (b) Now plot $\phi(t)$ for 0 < t < 100 and notice that the rotating support does make a small difference, causing the amplitude of the oscillations to grow and shrink periodically. Comment on the period of these small fluctuations.

## SECTION 7.8 More About Conservation Laws\*

7.45 \*\* (a) Verify that the coefficients $A_{ij}$ in the important expression (7.94) for the kinetic energy of any “natural” system are symmetric; that is, $A_{ij} = A_{ji}$ . (b) Prove that for any $n$ variables $v_1, \cdots, v_n$

$$
\frac {\partial}{\partial v _ {i}} \sum_ {j, k} A _ {j k} v _ {j} v _ {k} = 2 \sum_ {j} A _ {i j} v _ {j}.
$$

[Hint: Start with the case that n = 2, for which you can write out the sums in full. Notice that you need the result of part (a).] This identity is useful in many areas of physics; we needed it to prove the expression (7.96) for the generalized momentum $p_{i}$ .

7.46 \*\* Noether's theorem asserts a connection between invariance principles and conservation laws. In Section 7.8 we saw that translational invariance of the Lagrangian implies conservation of total linear momentum. Here you will prove that rotational invariance of $\mathcal{L}$ implies conservation of total angular momentum. Suppose that the Lagrangian of an $N$ -particle system is unchanged by rotations about a certain symmetry axis. (a) Without loss of generality, take this axis to be the $z$ axis, and show that the Lagrangian is unchanged when all of the particles are simultaneously moved from $(r_{\alpha}, \theta_{\alpha}, \phi_{\alpha})$ to $(r_{\alpha}, \theta_{\alpha}, \phi_{\alpha} + \epsilon)$ (same $\epsilon$ for all particles). Hence show that

$$
\sum_ {\alpha = 1} ^ {N} \frac {\partial \mathcal {L}}{\partial \phi_ {\alpha}} = 0.
$$

(b) Use Lagrange's equations to show that this implies that the total angular momentum $L_{z}$ about the symmetry axis is constant. In particular, if the Lagrangian is invariant under rotations about all axes, then all components of L are conserved.

7.47 \*\*\* In Chapter 4 (at the end of Section 4.7) I claimed that, for a system with one degree of freedom, positions of stable equilibrium “normally” correspond to minima of the potential energy $U(q)$ . Using Lagrangian mechanics, you can now prove this claim. (a) Consider a one-degree system of $N$ particles with positions $\mathbf{r}_{\alpha} = \mathbf{r}_{\alpha}(q)$ , where $q$ is the one generalized coordinate and the transformation between $\mathbf{r}$ and $q$ does not depend on time; that is, $q$ is what we have now agreed to call “natural.” (This is the meaning of the qualification “normally” in the statement of the claim. If the transformation depends on time, then the claim is not necessarily true.) Prove that the KE has the form $T = \frac{1}{2} A\dot{q}^2$ , where $A = A(q) > 0$ may depend on $q$ but not on $\dot{q}$ . [This corresponds exactly to the result (7.94) for $n$ degrees of freedom. If you have trouble with the proof here, review the proof there.] Show that the Lagrange equation of motion has the form

$$
A (q) \ddot {q} = - \frac {d U}{d q} - \frac {1}{2} \frac {d A}{d q} \dot {q} ^ {2}.
$$

(b) A point $q_{0}$ is an equilibrium point if, when the system is placed at $q_{0}$ with $\dot{q}=0$ , it remains there. Show that $q_{0}$ is an equilibrium point if and only if dU/dq=0. (c) Show that the equilibrium is stable if and only if U is minimum at $q_{0}$ . (d) If you did Problem 7.30, show that the pendulum of that problem does not satisfy the conditions of this problem and that the result proved here is false for that system.

## SECTION 7.9 Lagrange's Equations for Magnetic Forces\*

7.48 $\star\star$ Let $F = F(q_1, \cdots, q_n)$ be any function of the generalized coordinates $(q_1, \cdots, q_n)$ of a system with Lagrangian $\mathcal{L}(q_1, \cdots, q_n, \dot{q}_1, \cdots, \dot{q}_n, t)$ . Prove that the two Lagrangians $\mathcal{L}$ and $\mathcal{L}' = \mathcal{L} + dF/dt$ give exactly the same equations of motion.

7.49 $\star\star$ Consider a particle of mass $m$ and charge $q$ moving in a uniform constant magnetic field $\mathbf{B}$ in the $z$ direction. (a) Prove that $\mathbf{B}$ can be written as $\mathbf{B} = \nabla \times \mathbf{A}$ with $\mathbf{A} = \frac{1}{2}\mathbf{B} \times \mathbf{r}$ . Prove equivalently that in cylindrical polar coordinates, $\mathbf{A} = \frac{1}{2} B\rho \hat{\phi}$ . (b) Write the Lagrangian (7.103) in cylindrical polar coordinates and find the three corresponding Lagrange equations. (c) Describe in detail those solutions of the Lagrange equations in which $\rho$ is a constant.

## SECTION 7.10 Lagrange Multipliers and Constraint Forces\*

7.50 $\star$ A mass $m_{1}$ rests on a frictionless horizontal table. Attached to it is a string which runs horizontally to the edge of the table, where it passes over a frictionless, small pulley and down to where it supports a mass $m_{2}$ . Use as coordinates $x$ and $y$ the distances of $m_{1}$ and $m_{2}$ from the pulley. These satisfy the constraint equation $f(x,y) = x + y = \text{const}$ . Write down the two modified Lagrange equations and solve them (together with the constraint equation) for $\ddot{x},\ddot{y}$ , and the Lagrange multiplier $\lambda$ . Use (7.122) (and the corresponding equation in $y$ ) to find the tension forces on the two masses. Verify your answers by solving the problem by the elementary Newtonian approach.

7.51 $\star$ Write down the Lagrangian for the simple pendulum of Figure 7.2 in terms of the rectangular coordinates $x$ and $y$ . These coordinates are constrained to satisfy the constraint equation $f(x, y) = \sqrt{x^2 + y^2} = l$ . (a) Write down the two modified Lagrange equations (7.118) and (7.119). Comparing these with the two components of Newton's second law, show that the Lagrange multiplier is (minus) the tension in the rod. Verify Equation (7.122) and the corresponding equation in $y$ . (b) The constraint equation can be written in many different ways. For example we could have written $f'(x, y) = x^2 + y^2 = l^2$ . Check that using this function would have given the same physical results.

7.52 \* The method of Lagrange multipliers works perfectly well with non-Cartesian coordinates. Consider a mass $m$ that hangs from a string, the other end of which is wound several times around a wheel (radius $R$ , moment of inertia $I$ ) mounted on a frictionless horizontal axle. Use as coordinates for the mass and the wheel $x$ , the distance fallen by the mass, and $\phi$ , the angle through which the wheel has turned (both measured from some convenient reference position). Write down the modified Lagrange equations for these two variables and solve them (together with the constraint equation) for $\ddot{x}$ and $\ddot{\phi}$ and the Lagrange multiplier. Write down Newton's second law for the mass and wheel, and use them to check your answers for $\ddot{x}$ and $\ddot{\phi}$ . Show that $\lambda \partial f / \partial x$ is indeed the tension force on the mass. Comment on the quantity $\lambda \partial f / \partial \phi$ .

The image provided is completely blank and contains no text or visible content. Therefore, there is no OCR result to output.