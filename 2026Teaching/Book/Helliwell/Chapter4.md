# Lagrangian Mechanics

A notable advance in mechanics took place nearly a century after Newton in the work of the French mathematician and physicist Joseph-Louis Lagrange (1736– 1813). Lagrange invented no new fundamental physics, but rather looked at mechanics in a very different way, using variational techniques that gave fresh insight and provided powerful methods for finding differential equations of motion.

We already introduced variational principles in Chapter 3, and showed that they can give the equations of motion of nonrelativistic particles subject to arbitrary conservative forces. Although useful, that is not enough: now we need to see if other kinds of forces can be included in the variational approach. In this chapter we will find that forces of constraint can be included as well, which provides us with deep insights into mechanics and also enormous simplifications in problem solving. We will introduce Hamilton’s principle and the Lagrangian, concepts that are so elegant we are encouraged to place them at the very heart of classical mechanics. We are further encouraged to do so in the following chapter, the capstone chapter to Part I of the book, where we show how they naturally emerge as we take the classical limit of the vastly more comprehensive theory of quantum mechanics.

## 4.1 Nonconservative Forces

In our initial exploration at the end of Chapter 3 we permitted only conservative forces, forces that can be derived from a potential energy function. Now what about nonconservative forces, like air resistance and sliding friction? These forces typically reduce the energy of a particle. For example, the force of friction $\mathbf { F _ { f } }$ acting on a block sliding along a tabletop typically does negative work on the block, $d W = \mathbf { F _ { f } } \cdot d s < 0$ , since the direction of the frictional force is opposite to that of the block’s displacement.

In the elegant techniques we will develop in this chapter, we will assume that no such nonconservative forces act on our system. This will not be a serious problem, however; nonconservative forces are typically macroscopic forces, caused by the interactions of our system with vast numbers of molecules in the air or on a surface; that is, nonconservative forces are typically not fundamental. It is possible to include such forces in the variational methods of this chapter, but it is seldom worth it. If friction is important in a particular problem, it is safest to revert to using $\mathbf { F } = m \mathbf { a }$ and forget the elegance. If we reject nonconservative forces, what is left?

There is another important type of force which is neither conservative nor nonconservative, as we shall now see.

## 4.2 Forces of Constraint and Generalized Coordinates

Suppose that a particular particle is free to move in all three dimensions, so three coordinates are needed to specify its position. The coordinates might be Cartesian $( x , y , z )$ , cylindrical $( \rho , \varphi , z )$ , spherical $( r , \theta , \phi )$ , as illustrated in Figure 4.1, or they might be any other complete set of three (not necessarily orthogonal) coordinates.

A different particle may be less free: it might be constrained to move on a tabletop, or along a wire, or within the confines of a closed box, for example. The constraint is enforced by a force ofconstraint. It is a normal force $F _ { \mathrm { N } }$ of the tabletop on a particle that keeps the particle from falling to the ground, and it is likewise the tension force $F _ { \mathrm { T } }$ in a supporting wire that ensures that a pendulum bob moves in a circular arc as it swings back and forth. Such constraint forces are neither conservative nor nonconservative. They are not conservative, because their magnitudes are not functions of position only. For example, the tension in a pendulum wire can depend not only upon the angle of the pendulum relative to the vertical, but also upon how fast the bob is moving at that point, which depends on how fast the bob is pushed before it is released to swing on its own. Also, if (as is often the case) the force of constraint $F _ { \mathrm { C } }$ is always perpendicular to the displacement of the particle $\delta s ,$ then $F _ { \mathrm { C } }$ does no work, and so neither adds nor subtracts from the energy of the particle.

Sometimes the presence of a constraint means that fewer than three coordinates are required to specify the position of the particle. So if the particle is restricted to slide on the surface of a table, for example, only two coordinates are needed. Or if the particle is a bead sliding along a frictionless hoop, we need only a single coordinate, say the angle denoting the location of the bead along the hoop. In contrast, if the particle is confined to move within a closed three-dimensional box, the constraint does not reduce the number of coordinates required: we still need three coordinates to specify the position of the particle inside the box.

A constraint that reduces the number of coordinates needed to specify the position of a particle is called a holonomic constraint. The requirement that a particle move anywhere on a tabletop is a holonomic constraint, for example, because the minimum set of required coordinates is lowered from three to two, from (say) $( x , y , z )$ to $( x , y )$ . The requirement that a bead move on a wire in the shape of a hoop is a holonomic constraint, because the minimum set of required coordinates is lowered from three to one, from (say) cylindrical coordinates $( \rho , \varphi , z )$ to just $\varphi .$ . The requirement that a particle remains within a closed box is nonholonomic, because a requirement that $x _ { 1 } \le x \le x _ { 2 } , y _ { 1 } \le y \le y _ { 2 } , z _ { 1 } \le z \le z _ { 2 }$ does not reduce the number of coordinates required to locate the particle.

![](images/ddebd0e11a5e5c7d8c9ec5096ccf726f37eae11f243c2a78b4248ccc2b5575f3.jpg)  
Cartesian

![](images/f9c3a898f0a71dec8f4d0553e85f3b35a42868c19f9da1825b3be493abf5911e.jpg)  
cylindrical

![](images/32d8d58a1455b9f624507f3cf6e3b0503f7310a4053b289466652e19b478a9a8.jpg)  
spherical  
Fig. 4.1 Cartesian, cylindrical, and spherical coordinates

For an unconstrained single particle, three coordinates are needed; or if there is a holonomic constraint, the number of coordinates is reduced to two or one. We call a minimal set of required independent coordinates generalized coordinates and denote them by $q _ { k } ,$ , where $k = 1$ up to 3. For each generalized coordinate there is a generalized velocity ${ \dot { q } } _ { k } = d q _ { k } / d t .$ For example, for a bead on a fixed hoop, one choice of generalized coordinates consists of the single coordinate $q _ { 1 } = \varphi$ , the angle at which the bead is located along the hoop. The three cylindrical coordinates $\rho , \varphi ,$ , and z are not generalized coordinates in this case: there are two constraint relations amongst the three coordinates which assure that the bead stays along the hoop – i.e., r = constant and z = constant. Note that a generalized velocity does not necessarily have the dimensions of length/time, just as a generalized coordinate does not necessarily have the dimensions of length. For example, the angle $\varphi$ in cylindrical coordinates is dimensionless, and its generalized velocity $\dot { \varphi }$ has dimensions of inverse time.

## 4.3 Hamilton’s Principle

The quantity

$$
L = T - U\tag{4.1}
$$

is called the Lagrangian of the particle. As we just saw at the end of Chapter $^ { 3 , }$ using the Lagrangian as the integrand in the variational problem gives us the correct equations of motion, at least in Cartesian coordinates, for any conservative force.

We now have an interesting proposal at hand: reformulate the equations of motion of nonrelativistic mechanics, $\mathbf { F } = d \mathbf { p } / d t$ , in terms of a variational principle making stationary a certain functional. This has two benefits:

1. It is an interesting idea to think of dynamics as arising from making a certain physical quantity stationary; we will appreciate some of these aspects in due time, especially when we get to the chapters on the connections between classical and quantum mechanics.

2. This reformulation provides powerful computational tools that can allow us to solve complex mechanics problems with greater ease. The formalism also lends itself more transparently to computer algorithms.

Having chosen a set of generalized coordinates $q _ { k }$ for a particle, the integrand L in the variational problem, the Lagrangian, can be written

$$
L = T - U = L (t, q _ {1}, q _ {2}, \dots , \dot {q} _ {1}, \dot {q} _ {2}, \dots) = L (t, q _ {k}, \dot {q} _ {k}),\tag{4.2}
$$

written in terms of the generalized coordinates, generalized velocities, and time.<sup>2</sup>

Given a mechanical system described by means of N dynamical generalized coordinates labeled $q _ { k } ( t )$ , with $k = 1 , 2 , \hdots , N ,$ we define its action $S [ q _ { k } ( t ) ]$ as the functional of the time integral over the Lagrangian L, from a starting time $t _ { a }$ to an ending time $t _ { b } { \mathrm { : } }$

$$
S [ q _ {k} (t) ] = \int_ {\mathrm{t} _ {\mathrm{a}}} ^ {t _ {b}} d t L (t, q _ {1}, q _ {2}, \dots , \dot {q} _ {1}, \dot {q} _ {2}, \dots) \equiv \int_ {\mathrm{t} _ {\mathrm{a}}} ^ {t _ {b}} d t L (t, q _ {k}, \dot {q} _ {k}).\tag{4.3}
$$

It is understood that the particle begins at some definite position $( q _ { 1 } , q _ { 2 } , \ldots ) _ { a }$ at time $t _ { a }$ and ends at some definite position $( q _ { 1 } , q _ { 2 } , \ldots ) _ { b }$ at time $t _ { b }$ . We then propose that, for trajectories $q _ { k } ( t )$ where S is stationary – i.e., when

$$
\delta S = \delta \int_ {t _ {\mathrm{a}}} ^ {t _ {b}} L (t, q _ {k}, \dot {q} _ {k}) d t = 0,\tag{4.4}
$$

the $q _ { k } ( t ) \mathbf { s }$ satisfy the equations of motion for the system with the prescribed boundary conditions at $t _ { a }$ and $t _ { b }$ . This proposal was first enunciated by the Irish mathematician and physicist William Rowan Hamilton (1805–1865), and is called Hamilton’s principle.<sup>3</sup> From Hamilton’s principle and our discussion of the previous chapter, we deduce the N Lagrange equations

$$
\frac {d}{d t} \frac {\partial L}{\partial \dot {q} _ {k}} - \frac {\partial L}{\partial q _ {k}} = 0 \quad (k = 1, 2, \dots , N).\tag{4.5}
$$

These then have to be the equations of motion of the system if Hamilton’s principle is correct. Note that we need to express the Lagrangian in terms of generalized coordinates $q _ { k }$ since the variational principle assumes that the perturbed variables in the functional are independent: if we were to use instead all the variables describing the system, there could be constraint relations amongst them implying that the corresponding variations in Eq. (3.67) (writing $\delta y ~ $ $\delta q )$ are not independent and the corresponding Eqs. (3.68) or (4.5) do not then follow.

Consider a general physical system involving only conservative forces and a number of particles – constrained or otherwise. We are proposing that we can describe the dynamics of this system fully through Hamilton’s principle, using the Lagrangian $L = T - U ,$ the difference between the total kinetic energy and the total potential energy of the system – written in terms ofgeneralized coordinates. For a single particle under the influence of a conservative force, and described with Cartesian coordinates, we have already shown that this is indeed possible (see Eqs. (3.101) through (4.1)). The question is whether we can extend this new technology to more general situations with several particles, constraints, and described with arbitrary coordinate systems. There are several issues we need to tackle in this process:

1. Does changing the coordinate system in which we express the kinetic and potential energies generate any obstacles to the formalism? The answer to this is “no,” since the functional we extremize – which is the action – is a scalar quantity: its value does not change under coordinate transformations $q _ { k } \to q _ { k } ^ { \prime }$

$$
S = \int d t L (t, q _ {k}, \dot {q} _ {k}) = \int d t L (t, q _ {k} ^ {\prime}, \dot {q} _ {k} ^ {\prime}).\tag{4.6}
$$

The coordinate change simply relabels the stationary path of the functional; that is, the path at the extremum transforms as $q _ { k } ^ { s o l } ( t ) \ \to \ q _ { k } ^ { \prime s o l } ( t )$ , where $q _ { k } ^ { \prime s o l } ( t )$ is the stationary path of S expressed in the new coordinates. Hence, we can safely perform coordinate transformations as long as we always write the Lagrangian as kinetic minus potential energy in our preferred coordinate system.

2. Constraints provide for relations between the variables describing a mechanical system, and so reduce their number to a minimal set of generalized coordinates. This was the premise of the variational principle: the generalized coordinates must be independent. Therefore, no constraint would interfere with the varia tional principle as long as we express $L = T - U$ in terms of the generalized coordinates. But constraints on the coordinates are due to forces in the system that restrict the dynamics. For example, the normal force pushes upward to make sure a block stays on the floor; likewise, the tension force in a rope constrains the motion of a pendulum bob. Can we be certain that these forces should not be included in the potential energy U that appears in L? To ensure that this is the case, we need to ascertain that such constraint forces do no work, and hence do not have any net energetic contribution to U. This is not always easy to see. We will demonstrate the mechanism at work through examples, and then identify the general strategy.

3. Should we expect any obstacles to the formalism when we have more than one particle? Do we simply add the kinetic and potential energies ofall the particles? With two or more particles, shouldn’t we worry about Newton’s third law? We will see soon that the Lagrangian formalism incorporates Newton’s third law through symmetries of the Lagrangian and indeed can handle many-particle systems very well.

4. Where is Newton’s first law in this formalism? This is indeed an important potential pitfall: one should always write the kinetic energy andpotential energy in $L = T - U$ as seen from the perspective of an inertial observer. This is because our contact with mechanics is through the reproduction of Newton’s second law, $\mathbf { F } = m \mathbf { a } - \mathbf { w } \mathbf { h i c h }$ is valid only in an inertial frame. Hence, the first law is hidden in the prescription $L = T - U ,$ which must be expressed from an inertial perspective.

The punchline of all this is that, for arbitrarily complicated systems with many constraints and involving many particles interacting with conservative forces, the Lagrangian formalism works, and is extremely powerful. Newton’s second law follows from Hamilton’s principle, the third law arises, as we will see, from symmetries ofthe Lagrangian, and the first law is respected by making sure that the Lagrangian is written from the perspective of an inertial observer. It is important to emphasize that the Lagrangian formalism does not introduce new physics. It is a mathematical reformulation of mechanics, both nonrelativistic and relativistic. What it does is give us powerful new technical tools to tackle problems with greater ease and less work; a deeper insight into the laws of physics and how Nature ticks; and, as we shall see later, how the classical world is linked to the quantum realm.

## Example 4.1 A Simple Pendulum

An inertial observer sees that a small plumb bob of mass m is free to swing back and forth in a vertical x– z plane at the end of a string of length R. The position of the bob can be specified uniquely by its angle θ measured up from its equilibrium position at the bottom, so we choose θ as the generalized coordinate, as illustrated in Figure 4.2. The bob’s kinetic energy is

$$
T = \frac {1}{2} m v ^ {2} = \frac {1}{2} m (\dot {x} ^ {2} + \dot {y} ^ {2} + \dot {z} ^ {2}) = \frac {1}{2} m (\dot {r} ^ {2} + r ^ {2} \dot {\theta} ^ {2} + \dot {z} ^ {2}) = \frac {1}{2} m (R ^ {2} \dot {\theta} ^ {2}).\tag{4.7}
$$

We have introduced polar coordinates r and θ in the vertical x–z plane, and then implemented the constraint equations r = R (with ˙r = 0) and $y ~ = ~ 0 \left( \mathsf { w i t h } \dot { y } ~ = ~ 0 \right)$ . Its potential energy is $U = m g h \ =$ $m g R ( 1 - \cos \theta )$ , measuring the bob’s height h up from its lowest point. The Lagrangian of the bob is therefore

![](images/2a05e91d0ebbacd8dfce0480b10f2056fed3bd1a034ca50955b75a1d49d7f785.jpg)

The simple pendulum, with $\theta$ as the generalized coordinate.

$$
L = T - U = \frac {1}{2} m R ^ {2} \dot {\theta} ^ {2} - m g R (1 - \cos \theta).\tag{4.8}
$$

The constraint reduces the dynamics from three coordinates $x , y ,$ and z to only one, $\theta ,$ a single degree of freedom. The single Euler equation in this case is

$$
\frac {\partial L}{\partial \theta} - \frac {d}{d t} \frac {\partial L}{\partial \dot {\theta}} = - m g R \sin \theta - \frac {d}{d t} \left(m R ^ {2} \dot {\theta}\right) = 0,\tag{4.9}
$$

which reduces to the well-known “pendulum equation”

$$
\ddot {\theta} + (g / R) \sin \theta = 0.\tag{4.10}
$$

Note that Eq. (4.9) (or (4.10)) is equivalent to $\tau = I { \ddot { \theta } } ,$ , where the torque $\tau = - m g R$ sin θ is taken about the point of suspension (negative because it is opposite to the direction of increasing θ), and the moment of inertia of the bob i $J = m R ^ { 2 }$

Note also two twists here. First, we switched from Cartesian to polar coordinates, which is no problem in the Lagrangian formalism, since the action is a scalar quantity. Second, we implemented constraints $r \ = \ R ,$ implying ${ \dot { \boldsymbol { r } } } \ = \ 0 ,$ and $y \ = \ 0 ,$ implying $\dot { y } ~ = ~ 0 .$ . The former is responsible for holding the bob at fixed distance from the pivot, due to the tension force in the rope. The latter keeps the bob in the x–z plane. By implementing these constraints we reduced the problem from three to a single degree of freedom. There are two forces acting on the bob: gravity and the tension in the rope. The Lagrangian already accounts for the gravitational force through the gravitational potential energy. But what about the tension force responsible for the $r \ = \ R$ constraint? This tension in the rope does no work: it is always perpendicular to the motion of the bob, and hence the work contribution T · dr = 0, where T is the tension force and dr is the displacement of the bob. Thus, our potential energy U – related to work done by a force – is simply the potential energy due to gravity alone, U = mgh. In general, whenever a contact force remains perpendicular to the displacement of the particle, it can safely be ignored in constructing the Lagrangian. Its impact on the problem comes instead through constraints that help identify a reduced set of independent generalized coordinates. By using a single degree of freedom in the Lagrangian, the general coordinate θ, we have taken care of the tension force as well – thus fully accounting for all the forces on the bob.

## Example 4.2

## A Bead Sliding on a Vertical Helix

A bead of mass m is slipped onto a frictionless wire wound in the shape of a helix of radiu $R ,$ whose symmetry axis is oriented vertically in a uniform gravitational field, as shown in Figure 4.3. As always, we assume the description is from an inertial frame’s perspective (unless explicitly stated otherwise). Using cylindrical coordinates $\rho , \varphi , z ,$ the base ofthe helix is located a $\begin{array} { r } { \mathrm { \Delta } [ Z = 0 , \varphi = 0 , } \end{array}$ , and the angle $\varphi$ is related to the height z at any point by $\varphi = \alpha Z ,$ where α is a constant with dimensions ofinverse length. The gravitational potential energy of the bead is $U = m g z ,$ , and its kinetic energy is $I = ( 1 / 2 ) m v ^ { 2 } = ( 1 / 2 ) m [ \dot { \rho } ^ { 2 } + \rho ^ { 2 } \dot { \varphi } ^ { 2 } + \dot { z } ^ { 2 } ]$ However, the bead is constrained to move along the helix, so the bead’s radius is constant at $\rho = R ,$ , and (choosing z as the single generalized coordinate), $\dot { \varphi } = \alpha \dot { z }$ . Therefore the kinetic energy of the bead is

$$
\begin{array}{l} T = \frac {1}{2} m v ^ {2} = \frac {1}{2} m (\dot {x} ^ {2} + \dot {y} ^ {2} + \dot {z} ^ {2}) = \frac {1}{2} m (\dot {\rho} ^ {2} + r ^ {2} \dot {\varphi} ^ {2} + \dot {z} ^ {2}) \\ = (1 / 2) m [ 0 + \alpha^ {2} R ^ {2} + 1 ] \dot {z} ^ {2}, \end{array}\tag{4.11}
$$

where we switched to cylindrical coordinates first and then implemented the two constraints $\varphi = \alpha z$ and $\rho = R .$ . So the Lagrangian of the bead is

$$
L = T - U = \frac {1}{2} m [ 1 + \alpha^ {2} R ^ {2} ] \dot {z} ^ {2} - m g z\tag{4.12}
$$

in terms of the single generalized coordinate z and its generalized velocity $\dot { z } .$ Two constraints reduced the dynamics from three to only one degree of freedom. In Newtonian mechanics we need to take into account the normal force of the wire on the bead as one of the forces in $\mathsf { F } = m \mathbf { a } ; \mathsf { h o w e v e r } ,$ the normal force appears nowhere in the Lagrangian, because it does no work on the bead – it is always perpendicular to the bead’s displacement. Once again, whenever a normal force is perpendicular to the displacement of a particle, we can safely ignore it in setting up the Lagrangian of the particle. In this simple case, with a single normal force, the simplification is not that impressive. However, in the more complicated scenarios we shall see later, the advantages of using the Lagrangian approach, in which the normal force never appears, will become more apparent. Lagrange’s method can save an enormous amount of efort.

![](images/7798e0982e25ada210308fff88f450ac13551fa2f41ce94b89067972b27f08da.jpg)

## Example 4.3

## Block on an Inclined Plane

A block of mass m slides down a frictionless plane tilted at angle α to the horizontal, as shown in Figure 4.4. There is only a single degree offreedom here, say the distanceX ofthe block from the bottom, measured along the incline. The gravitational potential energy is mgh = mgX sin α. Using $\chi$ as the generalized coordinate, the velocity ${ \mathfrak { i } } { \mathfrak { X } } ,$ and the Lagrangian of the block is

$$
L = T - U = \frac {1}{2} m v ^ {2} - U = \frac {1}{2} m \dot {X} ^ {2} - m g X \sin \alpha ,\tag{4.13}
$$

which depends explicitly upon the single coordinate (X) and the single velocity $( \dot { X } ) .$ . The Lagrange equation is

$$
\frac {\partial L}{\partial X} - \frac {d}{d t} \frac {\partial L}{\partial \dot {X}} = - m g \sin \alpha - \frac {d}{d t} m \dot {X} = 0, \text {or} - m g \sin \alpha = m \ddot {X},\tag{4.14}
$$

which is indeed the correct ${ \boldsymbol { \mathsf { F } } } = m$ a equation for the block along the tilted plane.

![](images/9df4225a6fefbc1fd07add444e2a92d11495db7791cafc52a56be3aeb6e6c003.jpg)

## Fig. 4.4

Block sliding down an inclined plane.

In this problem, we judiciously chose our only degree of freedom as $\chi ,$ the distance along the inclined plane. If we had originally started with three coordinates, say $\chi , \gamma ,$ and $Z ,$ where $Z$ is perpendicular to the page, we would then set $Z = 0 \Rightarrow \dot { Z } = 0$ to confine the motion to the plane of the paper; then, we would use the constraint $Y = 0 \Rightarrow { \dot { Y } } = 0$ since the block cannot sink into the inclined plane. We are then left with a single degree offreedom, the general coordinateX. The $Y = 0$ constraint is associated with the norma force that keeps the block on the incline. This normal force is always perpendicular to the displacement of the block along the incline and thus does no work. So by writing the Lagrangian in terms of a single generalized coordinate X we implicitly account for the normal force and only need to include the gravitational potential energy in the Lagrangian.

## 4.4 Generalized Momenta and Cyclic Coordinates

In Cartesian coordinates the kinetic energy ofa particle is $T = ( 1 / 2 ) m ( \dot { x } ^ { 2 } + \dot { y } ^ { 2 } + \dot { z } ^ { 2 } )$ whose derivatives with respect to the velocity components are $\partial L / \partial \dot { x } = m \dot { x } .$ , etc., which are the components of momentum. So with generalized coordinates $q _ { k } .$ , it is natural to define the generalized momenta $p _ { k }$ as

$$
p _ {k} \equiv \frac {\partial L}{\partial \dot {q} _ {k}}.\tag{4.15}
$$

In terms of ${ p _ { k } }$ , the Lagrange equations become simply

$$
\frac {d p _ {k}}{d t} = \frac {\partial L}{\partial q _ {k}}.\tag{4.16}
$$

Now sometimes a particular coordinate $q _ { l }$ is absent from the Lagrangian. Its generalized velocity $\dot { \boldsymbol { q } } _ { l }$ is present, but not $q _ { l }$ itself. A missing coordinate is said to be a cyclic coordinate or an ignorable coordinate.<sup>4</sup> For any such coordinate the Lagrange equation (4.16) tells us that the time derivative of the corresponding generalized momentum is zero, so that particular generalized momentum is conserved:

$$
\frac {d p _ {k}}{d t} = \frac {\partial L}{\partial q _ {k}} = 0.\tag{4.17}
$$

One of the first things to notice about a Lagrangian is whether there are any cyclic coordinates, because any such coordinate leads to a conservation law that is also a first integral of motion. This means that the equation of motion for that coordinate is already half solved, in that it is only a first-order differential equation rather than the second-order differential equation one typically gets for a noncyclic coordinate.

<table><tr><td>Example 4.4</td><td>Particle on a Tabletop, with a Central Force</td></tr><tr><td></td><td><img src="images/27443fba13a8ed9a2b5bb133f6211326be038ce20076ba551a5a69b52030ab4c.jpg"/></td></tr><tr><td>Fig. 4.5</td><td>Particle moving on a tabletop.For a particle moving in two dimensions and subject to a central force, it is best to use polar coordinates (r, θ) about the origin, as shown in Figure 4.5. The kinetic energy of the particle is $T = \frac{1}{2} m v^{2} = \frac{1}{2} m (\dot{x}^{2} + \dot{y}^{2} + \dot{z}^{2}) = \frac{1}{2} m [\dot{r}^{2} + (r\dot{\theta})^{2}] , \tag{4.18}$ </td></tr></table>

where we used the constraint $\dot { z }$ = 0 related to the normal force being applied by the table onto the particle vertically. This force does no work and hence does not appear explicitly in the Lagrangian.

We will assume here that any force acting on the particle is a central force, depending upon r alone, so the potential energy U of the particle also depends upon r alone. The Lagrangian is therefore

$$
L = \frac {1}{2} m (\dot {r} ^ {2} + r ^ {2} \dot {\theta} ^ {2}) - U (r).\tag{4.19}
$$

Our two degrees of freedom are r and $\theta$ and they are our generalized coordinates. We note right away that in this case the coordinate θ is cyclic, so there must be a conserved quantity

$$
p _ {\theta} \equiv \frac {\partial L}{\partial \dot {\theta}} = m r ^ {2} \dot {\theta},\tag{4.20}
$$

which we recognize as the angular momentum of the particle. In Lagrange’s approach, $p _ { \theta }$ is conserved because $\theta$ is a cyclic coordinate; in Newtonian mechanics, $p _ { \theta }$ is conserved because there is no torque on the particle, since we assumed that any force is a central force. The Lagrange equations

$$
- \frac {d}{d t} \frac {\partial L}{\partial \dot {r}} = \frac {\partial L}{\partial r} \quad \text { and } \quad - \frac {d}{d t} \frac {\partial L}{\partial \dot {\theta}} = \frac {\partial L}{\partial \theta}\tag{4.21}
$$

become

$$
m r \dot {\theta} ^ {2} + m \ddot {r} = - \frac {\partial U (r)}{\partial r} \quad \text { and } \quad - \frac {d p _ {\theta}}{d t} = - \frac {d}{d t} \left(m r ^ {2} \dot {\theta}\right) = 0\tag{4.22}
$$

or

$$
m (\ddot {r} - r \dot {\theta} ^ {2}) \equiv m a _ {r} = F _ {r} \quad \text { and } \quad m (r \ddot {\theta} + 2 \dot {r} \dot {\theta}) m a _ {\theta} = F _ {\theta} = 0,\tag{4.23}
$$

where the radial force is $F _ { r } = - \partial U /$ ∂r and the radial and tangential accelerations are<sup>a</sup>

$$
a _ {r} = \ddot {r} - r \dot {\theta} ^ {2} \quad \text { and } \quad a _ {\varphi} = r \ddot {\theta} + 2 \dot {r} \dot {\theta}.\tag{4.24}
$$

In Example 1.6 we found (using $\pmb { \mathsf { F } } = m \mathbf { a } )$ the equations ofmotion ofa particle ofmass m in two dimensions at the end of a spring of zero natural length and force constan $k ,$ with one end of the spring fixed. There we used Cartesian coordinates $\left( x , y \right)$ . Now we are equipped to write the equations ofmotion in polar coordinates instead. Equations (4.22) with $U = ( 1 / 2 ) k r ^ { 2 }$ give

$$
m (\ddot {r} - r \dot {\theta} ^ {2}) = - k r \text { and } p _ {\theta} = m r ^ {2} \dot {\theta} = \text { constant }.\tag{4.25}
$$

That ${ \mathrm { i } } \mathsf { s } ,$ since the Lagrangian is independent of $\theta ,$ , we immediately get the first integral of motion $p _ { \theta } =$ constant. Eliminating $\dot { \theta }$ between the two equations, we find the purely radial equation

$$
\ddot {r} - \frac {(p _ {\theta}) ^ {2}}{m ^ {2} r ^ {3}} + \omega_ {0} ^ {2} r = 0,\tag{4.26}
$$

where $\omega _ { 0 } = \sqrt { k / m }$ is the natural frequency the spring–mass system would have ifthe mass were oscillating <sub>in one dimension (which in fact it would do ifthe angular momentum</sub> $p _ { \theta }$ happened to be zero). Note that even though the motion is generally two-dimensional, Eq. (4.26) contains only r(t). We can then find a second integral of motion because this equation has the form of a one-dimensional ma = F equation with

$$
m \ddot {r} = \frac {p _ {\theta} ^ {2}}{m r ^ {3}} - m \omega_ {0} ^ {2} r \equiv - \frac {d U _ {\mathrm{eff}}}{d r} = F (r).\tag{4.27}
$$

The efective potential energy $U _ { \mathrm { e f f } }$ can be found as

$$
U _ {\text { eff }} (r) = - \int^ {r} F (r) d r = - \int^ {r} \left(\frac {p _ {\theta} ^ {2}}{m r ^ {3}} - m \omega_ {0} ^ {2} r\right) d r = \frac {p _ {\theta} ^ {2}}{2 m r ^ {2}} + \frac {1}{2} k r ^ {2}\tag{4.28}
$$

plus a constant ofintegration, which we might as well set to zero. Therefore, the second first integral ofmotion is given by energy conservation in this one-dimensional system:<sup>b</sup>

$$
\frac {1}{2} m \dot {r} ^ {2} + \frac {(p _ {\theta}) ^ {2}}{2 m r ^ {2}} + \frac {1}{2} k r ^ {2} = \frac {1}{2} m \dot {r} ^ {2} + U _ {\text { eff }} = \text { constant } = E.\tag{4.29}
$$

A sketch of $U _ { \mathrm { e f f } }$ is shown in Figure 4.6. Note that $U _ { \mathrm { e f f } }$ has a minimum, which is the location of an equilibrium point (the value of r for which $d { \cal U } _ { \mathrm { e f f } } ( r ) / d r = 0$ is of course also the radius for which ${ \ddot { r } } = 0 ;$ see Eq. (4.27)). If r remains at the minimum of $U _ { \mathrm { e f f } } ,$ , the mass is actually circling the origin. The motion about this point is stable because the potential energy is a minimum there, so for small displacements from equilibrium the particle oscillates back and forth about this equilibrium radius as it orbits the origin. In Section 4.9 we will calculate the frequency of these oscillations. For now, we can write a closed-integral form of the full solution of the problem by solving for r˙ in Eq. (4.29) and integrating:

![](images/05e332e5376c487c59a31bdef11a0b58654c3b1b7fefc1c2617697335a8e9303.jpg)

The effective radial potential energy for a mass m moving with an effective potential energy $U _ { \mathrm { e f f } } = ( p ^ { \theta } ) ^ { 2 } / 2 m r ^ { 2 } + ( 1 / 2 ) k r ^ { 2 }$ for various values of $\cdot _ { p ^ { \theta } }$ , m, and k.

$$
\int d t = \int \frac {d r}{\sqrt {2 E / m - U _ {\mathrm{eff}} (r)}}.\tag{4.30}
$$

This example demonstrates the use of coordinate transformations in the Lagrangian formalism. In this case, we see how useful it is to be able to change coordinates when solving problems in Lagrangian mechanics.

<sup>a</sup>Note how easy it is to get the expressions for radial and tangential accelerations in polar coordinates using this method. They are often found in classical mechanics by diferentiating the position vector r = rˆr twice with respect to time, which involves rather tricky derivatives of the unit vectors ˆr and $\hat { \pmb { \theta } } .$

<sup>b</sup>See Example 1.9.

## Example 4.5

## The Spherical Pendulum

A ball of mass m swings on the end of an unstretchable string of length R in the presence of a uniform gravitational field $g .$ This is often called the “spherical pendulum,” because the ball moves as though it were sliding on the frictionless surface of a spherical bowl. We aim to find its equations of motion.

The ball has two degrees of freedom:

(i) It can move horizontally around a vertical axis passing through the point of support, corresponding to changes in its azimuthal angle $\phi .$ (On earth’s surface this would correspond to a change in longitude.)

(ii) It can also move in the polar direction, as described by the angle θ. (On earth’s surface this would correspond to a change in latitude.)

These angles are illustrated in Figure 4.7. In spherical coordinates, the velocity squared is

$$
v ^ {2} = \dot {r} ^ {2} + r ^ {2} \dot {\theta} ^ {2} + r ^ {2} \sin^ {2} \theta \dot {\phi} ^ {2} = R ^ {2} \dot {\theta} ^ {2} + R ^ {2} \sin^ {2} \theta \dot {\phi} ^ {2}\tag{4.31}
$$

using the constraint $r = R .$ We are left with two degrees of freedom, with corresponding variables $\theta$ and $\phi .$ We know once again that the tension force is always perpendicular to the displacement in this problem, and so can be thrown away through the use of a constraint. Note that the velocities in the $\theta$ and $\phi$ directions are $v _ { \theta } = R { \dot { \theta } }$ and $v _ { \phi } = R$ sin $\theta \dot { \phi } ,$ , which are perpendicular to one another; therefore

![](images/f88416e69a69433f2743024fd5c2afd3a9169667e44a1bd5ad651a5fbacd8e07.jpg)

## Fig. 4.7

Coordinates of a ball hanging on an unstretchable string.

$$
T = \frac {1}{2} m v ^ {2} = \frac {1}{2} m R ^ {2} (\dot {\theta} ^ {2} + \sin^ {2} \theta \dot {\phi} ^ {2}).\tag{4.32}
$$

The altitude h of the ball, measured from its lowest possible point, i $h = R ( 1 - \cos \theta )$ , so the potential energy can be written

$$
U = m g h = m g R (1 - \cos \theta).\tag{4.33}
$$

The Lagrangian is therefore

$$
L = T - U = \frac {1}{2} m R ^ {2} (\dot {\theta} ^ {2} + \sin^ {2} \theta \dot {\phi} ^ {2}) - m g R (1 - \cos \theta).\tag{4.34}
$$

The derivatives of L are

$$
\frac {\partial L}{\partial \theta} = m R ^ {2} \sin \theta \cos \theta \dot {\phi} ^ {2} - m g R \sin \theta , \quad \frac {\partial L}{\partial \dot {\theta}} = m R ^ {2} \dot {\theta},\tag{4.35}
$$

$$
\frac {\partial L}{\partial \phi} = 0, \quad \frac {\partial L}{\partial \dot {\phi}} = m R ^ {2} \sin^ {2} \theta \dot {\phi},\tag{4.36}
$$

and so the Lagrange equations are

$$
\frac {\partial L}{\partial \theta} - \frac {d}{d t} \frac {\partial L}{\partial \dot {\theta}} = 0 \quad \text { and } \quad \frac {\partial L}{\partial \phi} - \frac {d}{d t} \frac {\partial L}{\partial \dot {\phi}} = 0.\tag{4.37}
$$

Note that $\phi$ is cyclic, so the corresponding generalized momentum is

$$
p _ {\phi} = \frac {\partial L}{\partial \dot {\phi}} = m R ^ {2} \sin^ {2} \theta \dot {\phi} = \text { constant },\tag{4.38}
$$

which is an immediate first integral of motion. We identify $p _ { \phi }$ as the angular momentum about the vertical axis.

Now since

$$
\frac {\partial L}{\partial \dot {\theta}} = m R ^ {2} \dot {\theta},\tag{4.39}
$$

the $\theta$ equation can be written

$$
m R ^ {2} \ddot {\theta} = m R ^ {2} \sin \theta \cos \theta \dot {\phi} ^ {2} - m g R \sin \theta ,\tag{4.40}
$$

so

$$
\ddot {\theta} - \sin \theta \cos \theta \dot {\phi} ^ {2} + \left(\frac {g}{R}\right) \sin \theta = 0.\tag{4.41}
$$

We can eliminate the ${ \dot { \phi } } ^ { 2 }$ term using $\dot { \phi } = p _ { \phi } / ( m R ^ { 2 } \sin ^ { 2 } \theta )$ from Eq. (4.38), to give

$$
\ddot {\theta} - \left(\frac {p _ {\phi}}{m R ^ {2}}\right) ^ {2} \frac {\cos \theta}{\sin^ {3} \theta} + \left(\frac {g}{R}\right) \sin \theta = 0,\tag{4.42}
$$

a second-order diferential equation for the polar angle θ as a function of time.

Do we have to tackle this diferential equation head-on? Not if we can find another integral of motion instead. We have already identified one first integral, the conservation of angular momentum (4.38) about the vertical axis. Another first integral is energy conservation

$$
E = T + U = \frac {1}{2} m R ^ {2} (\dot {\theta} ^ {2} + \sin^ {2} \theta \dot {\phi} ^ {2}) + m g R (1 - \cos \theta),\tag{4.43}
$$

valid because no work is being done on the ball aside from the work done by gravity, which is already accounted for in the potential energy. By combining the two conservation laws (4.38) and (4.43), we can eliminate $\dot { \phi }$ and write

$$
E = \frac {1}{2} m R ^ {2} \dot {\theta} ^ {2} + \frac {(p _ {\phi}) ^ {2}}{2 m R ^ {2} \sin^ {2} \theta} + m g R (1 - \cos \theta) = \text { constant }\tag{4.44}
$$

or

$$
E = \frac {1}{2} m R ^ {2} \dot {\theta} ^ {2} + U _ {\text { eff }},\tag{4.45}
$$

where the “efective potential energy”is

$$
U _ {\text { eff }} = \frac {(p _ {\phi}) ^ {2}}{2 m R ^ {2} \sin^ {2} \theta} + m g R (1 - \cos \theta).\tag{4.46}
$$

This efective potential energy $U _ { \mathrm { e f f } }$ is sketched in Figure 4.8. The second term is the actual gravitational potential energy, while the first term is really a piece of the kinetic energy that has become a function of position only, thanks to angular momentum conservation. We can then solve for $\dot { \theta }$ in Eq. (4.45), separate the variables t and $\theta ,$ and integrate to find

![](images/3a426f72e6243d091d8b5491ca03b32deeb3065a8e6c1deaf83da2f850d538a2.jpg)  
A sketch of the effective potential energy $U _ { \mathrm { e f f } }$ for a spherical pendulum. A ball at the minimum of $U _ { \mathrm { e f f } }$ is circling the vertical axis passing through the point of suspension, at constant θ. The fact that there is a potential energy minimum at some angle $\theta _ { 0 }$ means that ifdisturbed from this value the ball will oscillate back and forth about $\theta _ { 0 }$ as it orbits the vertical axis.

## Fig. 4.8

$$
t (\theta) = \sqrt {\frac {m R ^ {2}}{2}} \int_ {\theta_ {0}} ^ {\theta} \frac {d \theta}{\sqrt {(E - m g R) - (p _ {\phi}) ^ {2} / (2 m R ^ {2} \sin^ {2} \theta) + m g R \cos \theta}}.\tag{4.47}
$$

In summary, the constraint reduced the number of degrees of freedom – from three to two in this case. The associated tension constraint force does no work, since it is perpendicular to the trajectory; we did not need to include its contribution in the Lagrangian. There were only two generalized coordinates, and we were able to solve the problem by finding two first integrals of motion.

## 4.5 Systems of Particles

So far we have treated the motion of single particles only, described by at most three generalized coordinates and three generalized velocities. But often we want to find the motion ofsystems of particles, in which two or more particles may interact with one another, like two blocks on opposite ends of a spring, or several stars orbiting around one another. Can we still use the variational approach, by writing down a Lagrangian that contains the total kinetic energy and the total potentia energy of the entire system?

Begin with a system of two particles, with masses $m _ { 1 }$ and $m _ { 2 } .$ , confined to move along a horizontal frictionless rail. Figure 4.9 shows a picture of the system, where we label the coordinates ofthe particles $x _ { 1 }$ and $x _ { 2 }$ . We write an action for the system

$$
S = \int d t \left(\frac {1}{2} m _ {1} \dot {x} _ {1} ^ {2} + \frac {1}{2} m _ {2} \dot {x} _ {2} ^ {2} - U (x _ {2} - x _ {1})\right)\tag{4.48}
$$

![](images/1c0798dd70e7762bccb1e99bbc038874db44b5cb005e71babda2979860e26f36.jpg)  
Two interacting beads on a one-dimensional frictionless rail. The interaction between the particles depends only on the distance between them.

where, in addition to the usual kinetic energy terms, there is some unknown interaction between the particles described by a potential $U ( x _ { 2 } - x _ { 1 } )$ . Note that we use the total kinetic energy, and we assume that the potential – hence the associated force law – depends only upon the distance between the particles. We then have two equations of motion with two generalized coordinates, $x _ { 1 }$ and $x _ { 2 } .$ , so that

$$
\frac {d}{d t} \left(\frac {\partial L}{\partial \dot {x} _ {1}}\right) - \frac {\partial L}{\partial x _ {1}} = 0 \Rightarrow m _ {1} \ddot {x} _ {1} = - \frac {\partial U}{\partial x _ {1}}\tag{4.49}
$$

and

$$
\frac {d}{d t} \left(\frac {\partial L}{\partial \dot {x} _ {2}}\right) - \frac {\partial L}{\partial x _ {2}} = 0 \Rightarrow m _ {2} \ddot {x} _ {2} = - \frac {\partial U}{\partial x _ {2}} = + \frac {\partial U}{\partial x _ {1}},\tag{4.50}
$$

where in the last step we used the fact that $U = U ( x _ { 2 } - x _ { 1 } )$ . The equations are equivalent to Newton’s second law applied to each of the two particles: kinetic energy is additive and each of its terms will generally give the ma part ofNewton’s second law for the corresponding particle. Hence, in multi-particle systems we need to consider the total kinetic energy T minus the total potential energy. Terms that mix the variables of different particles, such as $U ( x _ { 2 } - x _ { 1 } )$ , will give the correct forces on the particles as well. In this case, we see that the action–reaction pair, $\partial U / \partial x _ { 1 } = - \partial U / \partial x _ { 2 }$ , comes out for $f r e e _ { : }$ , and arises from the fact that the force law depends only on the distance between the particles! That is, Newton’s third law is naturally incorporated in the formalism and originates from the fact that forces between two particles depend only upon the distance between the interacting entities, and not (say) their absolute positions.

In such a case the total momentum of the system must be conserved, which is easily verified simply by adding the two Eqs. (4.49) and (4.50), giving

$$
\frac {d}{d t} (m _ {1} \dot {x} _ {1} + m _ {2} \dot {x} _ {2}) = 0.\tag{4.51}
$$

These results suggest that there must be a more transparent set of generalized coordinates to use here, in which one of the new coordinates is cyclic, so that its generalized momentum will be conserved automatically. These new coordinates are the center of mass and relative coordinates

$$
X \equiv \frac {m _ {1} x _ {1} + m _ {2} x _ {2}}{M} \quad \text { and } \quad x \equiv x _ {2} - x _ {1},\tag{4.52}
$$

where $M = m _ { 1 } + m _ { 2 }$ is the total mass of the system. Note that X and x are simply linear combinations of $x _ { 1 }$ and $x _ { 2 }$ . Then in terms ofX and x, it is straightforward to show that the Lagrangian of the system has the form

$$
L = \frac {1}{2} M \dot {X} ^ {2} + \frac {1}{2} \mu \dot {x} ^ {2} - U (x),\tag{4.53}
$$

where $\mu \equiv m _ { 1 } m _ { 2 } / M$ is called the reduced mass of the system (note that $\mu$ is in fact smaller than either $m _ { 1 }$ or $m _ { 2 } )$ . Using this Lagrangian, it is obvious that the center of mass coordinate X is cyclic, so the corresponding momentum

$$
P = \frac {\partial L}{\partial \dot {X}} = M \dot {X} \equiv m _ {1} \dot {x} _ {1} + m _ {2} \dot {x} _ {2}\tag{4.54}
$$

is conserved; this is simply the conservation of the total momentum. The setup easily extends to the case with an arbitrary number of particles – pairwise interacting with forces that depend on the distance between them. Action–reaction pairs would immediately arise realizing Newton’s third law, and the sum of all the momenta would be conserved.

This problem is also an example of reducing a two-body problem to an equivalent one-body problem through a coordinate transformation. The motion of the center of mass of the system is trivial: the center of mass just drifts along at constant velocity. The interesting motion of the particles is their relative motion $x ,$ which behaves as though it were a single particle of mass $\mu$ and position $x ( t )$ subject to the potential energy $U ( x )$ , with Lagrangian

$$
L = \frac {1}{2} \mu \dot {x} ^ {2} - U (x).\tag{4.55}
$$

This problem exemplifies the fact that coordinate transformations $o f$ the Lagrangian can be a very powerful technique.

<table><tr><td colspan="2">Example 4.6 Pulleys Everywhere</td></tr><tr><td></td><td><img src="images/7eeb5cc6706c057d5049eca71a1f7136ef72a9ba0e9dc557861f977fa4941e8c.jpg"/></td></tr><tr><td>Fig. 4.10 A contraption of pulleys. We want to find the accelerations of all three weights. We assume that the three pulleys have negligible mass so they have negligible kinetic and potential energies.Another classic set of mechanics problems involves pulleys, often lots of pulleys. Consider the setup shown in Figure 4.10. Two weights, with masses  $m_1$  and  $m_2$ , hang on the outside of a three-pulley system, while a weight of mass M hangs on the middle pulley. We assume the pulleys and the connecting rope have negligible mass, so their kinetic and potential energies are also negligible. We will suppose for now that all three pulleys have the same radius R, but this will turn out to be of no importance. We want to find the accelerations of  $m_1$ ,  $m_2$ , and M. We construct a Cartesian coordinate system as shown in the figure, which remains fixed in the inertial frame of the ground. First of all, note that there are three massive objects moving in two dimensions,</td><td></td></tr></table>

so we might think that we have six variables to track, $, X _ { 1 }$ and $y _ { 1 }$ for weight $m _ { 1 } , x _ { 2 }$ and $y _ { 2 }$ for weight $m _ { 2 } ,$ , and $\chi$ and Y for weight M. We can then write the total kinetic energy

$$
T = \frac {1}{2} m _ {1} \left(\dot {x} _ {1} ^ {2} + \dot {y} _ {1} ^ {2}\right) + \frac {1}{2} m _ {2} \left(\dot {x} _ {2} ^ {2} + \dot {y} _ {2} ^ {2}\right) + \frac {1}{2} M \left(\dot {X} ^ {2} + \dot {Y} ^ {2}\right).\tag{4.56}
$$

But that is obviously overkill. We know the dynamics is entirely vertical, so we can focus on $y _ { 1 } , y _ { 2 } ,$ , and $\boldsymbol { \mathsf { Y } }$ only and set ${ \dot { x } } _ { 1 } = { \dot { x } } _ { 2 } = { \dot { X } } = 0$ . But that is still too much. There are only two degrees of freedom in this problem! Just pick any two of $y _ { 1 } , y _ { 2 }$ , or $\boldsymbol { \ Y } ,$ and we can draw the figure uniquely, as long as we know the length of the rope. Another way of saying this is to write

$$
\text { Length   of   rope } = (H - y _ {1}) + 2 (H - Y) + (H - y _ {2}) + 3 \pi R,\tag{4.57}
$$

where H is the height of the upper-pulley centers, as shown in the figure. We can therefore write in general

$$
y _ {1} + 2 Y + y _ {2} = \text { constant },\tag{4.58}
$$

which can be used to eliminate one of the three variables. We choose to get rid of $\boldsymbol { \ Y } ,$ , writing

$$
Y = - \frac {y _ {1} + y _ {2}}{2} + \text { constant },\tag{4.59}
$$

which implies

$$
\dot {Y} = - \frac {\dot {y} _ {1} + \dot {y} _ {2}}{2}.\tag{4.60}
$$

We can now write our kinetic energy in terms of two variables only, $, y _ { 1 }$ and $y _ { 2 } { \mathrm { : } }$ :

$$
T = \frac {1}{2} m _ {1} \dot {y} _ {1} ^ {2} + \frac {1}{2} m _ {2} \dot {y} _ {2} ^ {2} + \frac {1}{2} M \left(\frac {\dot {y} _ {1} + \dot {y} _ {2}}{2}\right) ^ {2}.\tag{4.61}
$$

We next need the potential energy, which is entirely gravitational. We can write

$$
\begin{array}{l} U = m _ {1} g y _ {1} + m _ {2} g y _ {2} + M g Y \\ = m _ {1} g y _ {1} + m _ {2} g y _ {2} - M g \left(\frac {y _ {1} + y _ {2}}{2}\right) + \text { constant }, \end{array}\tag{4.62}
$$

where the zero of the potential was chosen at the ground, and we can also drop the additive constant term since it does not afect the equations of motion. In summary, we have a variational problem with the Lagrangian

$$
\begin{array}{c} L = T - U = \frac {1}{2} m _ {1} \dot {y} _ {1} ^ {2} + \frac {1}{2} m _ {2} \dot {y} _ {2} ^ {2} + \frac {1}{2} M \left(\frac {\dot {y} _ {1} + \dot {y} _ {2}}{2}\right) ^ {2} \\ - m _ {1} g y _ {1} - m _ {2} g y _ {2} + M g \left(\frac {y _ {1} + y _ {2}}{2}\right). \end{array}\tag{4.63}
$$

There are two dependent variables $y _ { 1 }$ and $y _ { 2 } ,$ , so we have two equations of motion:

$$
\frac {d}{d t} \left(\frac {\partial L}{\partial \dot {y} _ {1}}\right) - \frac {\partial L}{\partial y _ {1}} = 0 \Rightarrow m _ {1} \ddot {y} _ {1} + \frac {M}{4} (\ddot {y} _ {1} + \ddot {y} _ {2}) = - m _ {1} g + \frac {M g}{2}\tag{4.64}
$$

and

$$
\frac {d}{d t} \left(\frac {\partial L}{\partial \dot {y} _ {2}}\right) - \frac {\partial L}{\partial y _ {2}} = 0 \Rightarrow m _ {2} \ddot {y} _ {2} + \frac {M}{4} (\ddot {y} _ {1} + \ddot {y} _ {2}) = - m _ {2} g + \frac {M g}{2}.\tag{4.65}
$$

We can now solve for¨y<sub>1</sub> and¨y<sub>2</sub>:

$$
\begin{array}{l} \ddot {y} _ {1} = - g + \frac {4 m _ {2} g}{m _ {1} + m _ {2} + 4 m _ {1} m _ {2} / M}, \\ \ddot {y} _ {2} = - g + \frac {4 m _ {1} g}{m _ {1} + m _ {2} + 4 m _ {1} m _ {2} / M}. \end{array}\tag{4.66}
$$

Note that these accelerations have magnitudes less than g, as we might expect intuitively. We can also find $\ddot { \boldsymbol { Y } }$ from Eq. (4.60):

$$
\ddot {Y} = - \frac {\ddot {y} _ {1} + \ddot {y} _ {2}}{2} \Rightarrow \ddot {Y} = g - \frac {2 (m _ {1} + m _ {2}) g}{m _ {1} + m _ {2} + 4 m _ {1} m _ {2} / M}.\tag{4.67}
$$

The astute reader may rightfully wonder whether we have overlooked something in this treatment. We never encountered the tension force of the rope on each of the masses! Consider the two tension forces ${ { T } _ { 1 } }$ and $T _ { 2 }$ at the end of this (or any) massless rope. If we wanted to account for such forces in a Lagrangian, we would need the associated energy, or work, they contribute to the system. Since the rope has zero mass, we know that $\left| \bar { I } _ { 1 } \right| = \left| \bar { I } _ { 2 } \right|$ . The two tension forces, however, point in opposite directions. When one end of the rope moves by $\Delta s _ { 1 } > 0$ parallel to $I _ { 1 } , I _ { 1 }$ does work $W _ { 1 } = | I _ { 1 } | \Delta s _ { 1 }$ . At the same time, the other end must move the same distance $\Delta s _ { 2 } = \Delta s _ { 1 }$ . However, at this other end, the tension force points opposite to the displacement, and the work is $W _ { 2 } = - | I _ { 2 } | \Delta s _ { 2 } = - | I _ { 1 } | \Delta s _ { 1 }$ . The total work is ${ \cal W } = { \cal W } _ { 1 } + { \cal W } _ { 2 } = 0 .$ Therefore, the tension forces along a massless rope will always contribute zero work, and hence cannot be associated with energy in the Lagrangian. The constraint given by Eq. (4.57), which eliminated one of the three variables, implements the physical condition that the rope has constant length. This is related to the existence of tension in the rope: if the tension were zero, there would be no rope and hence the constraint $\Delta s _ { 1 } = \Delta s _ { 2 }$ . Thus, the fact that there is no work associated with the tension is related to the use of the constraint to reduce the problem to two generalized coordinates.

## Example 4.7

## A Block on a Movable Inclined Plane

Let us return to the classic problem of a block sliding down a frictionless inclined plane, as in Example 4.2, except that we will make things a bit more interesting: now the inclined plane itself is allowed to move. Figure 4.11(a) shows the system. A block of mass m rests on an inclined plane of mass M: both the block and the inclined plane are free to move without friction. The plane’s angle is denoted by α. The problem is to find the acceleration of the block.

The observation deck is the ground, which is taken as an inertial reference frame. Note that the inclined plane is notan inertial reference frame, because it will accelerate to the left as the block slides down. We set up a convenient set of Cartesian coordinates, as shown in the figure. The origin is shifted to the top of the incline at zero time to make the geometry easier to analyze. We start by identifying the degrees of freedom. At first,

![](images/e177f27893f7719184809701607114e65f72e19c078ad46a88ae54189bf0470d.jpg)  
(a)

![](images/d9dbaba1f12230e8e4c3b6d28f97d8af6bf65ef933c59727113a5fd7f9081129.jpg)  
(b)  
A block slides along an inclined plane. Both block and inclined plane are free to move along frictionless contact surfaces. (a) The coordinate system used. (b) The normal contact forces at the block–inclined plane interface.

## Fig. 4.11

we can think of the block and inclined plane as moving in the two dimensions of the problem. The block’s coordinates could be denoted by $\chi$ and $y ,$ and the inclined plane’s coordinates by X and Y. But we quickly realize that this would be overkill: if we specify $\chi ,$ and how far down the top of the incline the block is located (denoted by D in the figure), we can draw the figure uniquely. This is because the inclined plane cannot move vertically, either jumping of the ground or burrowing into it (that’s one condition), so Y is unnecessary; and the horizontal position x or vertical position y of the block is determined by $\chi$ and D (these correspond to the second condition that the block cannot sink through the incline). We then start with four coordinates, add two conditions or restrictions, and we are left with two degrees of freedom. The choice of the two remaining generalized coordinates is arbitrary, as long as the choice uniquely fixes the geometry. We will pick X and $D ,$ although we might have chosen $\chi$ and $\scriptstyle \chi ,$ for example.

Next, we need to write the Lagrangian. The starting point for this is the total kinetic energy of the system:

$$
T = \frac {1}{2} m (\dot {x} ^ {2} + \dot {y} ^ {2}) + \frac {1}{2} M (\dot {X} ^ {2} + \dot {Y} ^ {2})\tag{4.68}
$$

in the inertial frame of the ground. Note that we must begin by writing the kinetic energy in an inertial frame before rewriting it in terms of the two degrees of freedom $\chi$ and $D$ alone. This requires a bit of geometry. Looking back at the figure, we can write the two constraint conditions as

$$
Y = 0, \quad x = X + D \cos \alpha , \text { and } y = - D \sin \alpha .\tag{4.69}
$$

This implies

$$
\dot {Y} = 0, \dot {x} = \dot {X} + \dot {D} \cos \alpha , \text { and } \dot {y} = - \dot {D} \sin \alpha .\tag{4.70}
$$

We can now substitute these into Eq. (4.68) and get

$$
T = \frac {1}{2} M \dot {X} ^ {2} + \frac {1}{2} m \dot {X} ^ {2} + \frac {1}{2} m \dot {D} ^ {2} + m \dot {X} \dot {D} \cos \alpha .\tag{4.71}
$$

Note that this result, in terms of the generalized coordinates and velocities, would have been very dificult to guess, especially the $\dot { \chi } \dot { D }$ term. Again, it is very important to start by writing the kinetic energy first in an inertial frame, and often important to use Cartesian coordinates in this initial expression to be confident that it has been done correctly.

We now need the potential energy of the system, which is entirely gravitational. The inclined plane’s potential energy does not change. Since it is a constant, we need not add it to the Lagrangian: the Lagrange equations of motion involve partial derivatives of L and, hence, a constant term in L is irrelevant to the dynamics. In contrast, the block’s potential energy does change. We can choose the zero of the potential at the origin of our coordinate system and write

$$
U = m g y = - m g D \sin \alpha .\tag{4.72}
$$

The Lagrangian then becomes

$$
L = T - U = \frac {1}{2} M \dot {X} ^ {2} + \frac {1}{2} m \dot {X} ^ {2} + \frac {1}{2} m \dot {D} ^ {2} + m \dot {X} \dot {D} \cos \alpha + m g D \sin \alpha .\tag{4.73}
$$

We observe immediately that X is cyclic, so its corresponding momentum is conserved. Note that the total energy is also conserved. Therefore we can obtain the complete set of two first integrals of motion for our two degrees of freedom.

Nevertheless, to illustrate a diferent approach, we will tackle the full second-order diferential equations of motion obtained directly from the Lagrange equations. Since we have two degrees of freedom X and D, we’ll have two second-order equations. The equation for X is

$$
\frac {d}{d t} \left(\frac {\partial L}{\partial \dot {X}}\right) - \frac {\partial L}{\partial X} = 0 \Rightarrow (m + M) \ddot {X} + m \ddot {D} \cos \alpha = 0,\tag{4.74}
$$

and the equation for D is

$$
\frac {d}{d t} \left(\frac {\partial L}{\partial \dot {D}}\right) - \frac {\partial L}{\partial D} = 0 \Rightarrow m \ddot {D} + m \ddot {X} \cos \alpha = m g \sin \alpha .\tag{4.75}
$$

This is a system of two linear equations in two unknowns $\ddot { \chi }$ and ${ \ddot { D } } .$ Separating the two algebraically, we find

$$
\ddot {X} = \frac {- m g \cos \alpha \sin \alpha}{M + m \sin^ {2} \alpha} \text { and } \ddot {D} = \frac {(M + m) g \sin \alpha}{M + m \sin^ {2} \alpha}.\tag{4.76}
$$

Since we want the acceleration of the block in our inertial reference frame, we need to find $\ddot { x } \equiv a ^ { x }$ and $\ddot { y } \equiv a ^ { y }$ . Diferentiating Eq. (4.70) with respect to time, we find

$$
a ^ {x} = \ddot {x} = \ddot {X} + \ddot {D} \cos \alpha \text { and } a ^ {y} = \ddot {y} = - \ddot {D} \sin \alpha .\tag{4.77}
$$

Substituting our solution from Eqs. (4.76) into these, we have

$$
a ^ {x} = \frac {M g \sin \alpha \cos \alpha}{M + m \sin^ {2} \alpha} \text { and } a ^ {y} = - \frac {(M + m) g \sin^ {2} \alpha}{M + m \sin^ {2} \alpha}.\tag{4.78}
$$

It is always useful to look at various limiting cases to see if a result makes sense. For example, what if $\alpha = 0 ,$ $j . e . _ { \cdot }$ , what if the block moves on a horizontal plane? Both accelerations then vanish, as expected: if started at rest, both block and incline just stay put. Now what if the inclined plane is much heavier than the block, $j . e . ,$ $M \gg m ?$ We then have

$$
a ^ {x} \simeq g \cos \alpha \sin \alpha \text { and } a ^ {y} \simeq - g \sin^ {2} \alpha ,\tag{4.79}
$$

so that $a ^ { y } / a ^ { x } \simeq - \tan \alpha ,$ , which is what we would expect ifthe inclined plane were not moving appreciably. Finally, i ${ \mathfrak { M } } = 0 ,$ , then $\smash { q ^ { X } = 0 }$ and $a ^ { y } = - g ,$ , so the block would fall straight down; this is exactly what would happen if there were no inclined plane at all.

The most impressive aspect of this example is the absence of any normal forces from our computations! With the traditional approach of problem solving, we would need to include several normal forces in the computation, shown in Figure 4.11(b): the normal force exerted by the inclined plane on the block, the normal force exerted by the ground on the inclined plane, and the normal force exerted by the block on the inclined plane as a reaction force. The role of these normal forces is to hold the inclined plane on the ground and to hold the block on the inclined plane. If we think of the contributions of the normal forces to the Lagrangian, we would want to include some potential energy terms for them. But potential energy is related to work done by forces. The normal force is often perpendicular to the direction of motion, and hence does no work, $\boldsymbol { \mathsf { N } } \cdot \Delta \boldsymbol { \mathsf { r } } = 0$ , where N is a normal force and $\Delta \mathfrak { r }$ is the displacement of a contact point. Therefore, there is no potential energy term to include in the Lagrangian to account for such normal forces. In our example, however, this is not entirely correct. While it is true for the normal force exerted by the ground onto the inclined plane, it is not true for the two normal forces acting between the block and the inclined plane. This is because the inclined plane is moving as well and the trajectory of the block is not parallel to the incline! However, there is another reason why this normal force is safely left out of the Lagrangian. These normal forces occur as an action–reaction pair; and the displacement of the interface between the block and the incline is the same for both forces, and hence the contributions to the total work or energy of the system from these two normal forces cancel. As we saw from the previous example, such force pairs do not appear in the Lagrangian. The computational step at the beginning, where we zeroed onto the degrees of freedom of the problem – going from $\chi , Y , \chi ,$ andy to X and D – is in a sense the process of accounting for the normal forces in the Lagrangian approach to the problem.

In Chapter 6, we will also learn of a way to force the inclusion of normal and tension forces in a Lagrangian even when we need not do so – for the purpose of finding the magnitude of a normal or tension force if so desired. For now, we are very happy to drop normal and tension forces from consideration. This can be a big simplification for problem solving: fewervariables, fewerforces to consider, less work to do (no pun intended). -

## 4.6 The Hamiltonian

We will now prove an enormously useful consequence of the Lagrange equations that will at the end look very familiar. First, take the total derivative of the Lagrangian $L ( t , q _ { k } , { \dot { q } } _ { k } )$ with respect to time t. There are many ways in which L can change with time: it can change because of explicit dependence on t, but also because of implicit dependence on t through the time dependence of one or more of the coordinates $q _ { k } ( t )$ or velocities ${ { \dot { q } } _ { k } } ( t )$ . Therefore, from multivariable calculus and the chain rule, we have

$$
\frac {d L \left(q _ {k} , \dot {q} _ {k} , t\right)}{d t} = \frac {\partial L}{\partial t} + \frac {\partial L}{\partial q _ {k}} \dot {q} _ {k} + \frac {\partial L}{\partial \dot {q} _ {k}} \ddot {q} _ {k},\tag{4.80}
$$

using the Einstein summation convention from Chapter 2. That is, since the index k is repeated in each of the last two terms, a sum over k is implied in each term; we have also used the fact that $d \dot { q } _ { k } / d t \equiv \ddot { q } _ { k }$ . Now, take the time derivative of the quantity $\dot { q } _ { k } ( \partial L / \partial \dot { q } _ { k } )$ ; again, with implied sums over k:

$$
\frac {d}{d t} \left(\dot {q} _ {k} \frac {\partial L}{\partial \dot {q} _ {k}}\right) = \ddot {q} _ {k} \frac {\partial L}{\partial \dot {q} _ {k}} + \dot {q} _ {k} \frac {d}{d t} \left(\frac {\partial L}{\partial \dot {q} _ {k}}\right) = \ddot {q} _ {k} \frac {\partial L}{\partial \dot {q} _ {k}} + \dot {q} _ {k} \frac {\partial L}{\partial q _ {k}},\tag{4.81}
$$

using the product rule. We have also used the Lagrange equations to simplify the last term on the right. Note that this expression contains the same two summed terms that we found in Eq. (4.80). Therefore, subtracting Eq. (4.81) from Eq. (4.80) gives

$$
\frac {\partial L}{\partial t} - \frac {d}{d t} \left(L - \dot {q} _ {k} \frac {\partial L}{\partial \dot {q} _ {k}}\right) = 0.\tag{4.82}
$$

Now define the Hamiltonian H of a particle to be

$$
H \equiv \dot {q} _ {k} p _ {k} - L,\tag{4.83}
$$

where we have already defined the generalized momenta to be $p _ { i } = \partial L / \partial { \dot { q } } _ { k }$ , and again a sum over k is implied. Equation (4.82) can be written

$$
\frac {\partial L}{\partial t} = - \frac {d H}{d t}.\tag{4.84}
$$

This result is particularly interesting if L is not an explicit function of time, i.e., if $\partial L / \partial t = 0$ . It shows that ifa Lagrangian L is not an explicitfunction oftime, then the Hamiltonian H is conserved.

What is the meaning of H? Suppose that the particle is free to move in three dimensions in a potential $U ( x , y , z )$ without constraints, and that we are using Cartesian coordinates. Then $p _ { x } = m { \dot { x } } , p _ { y } = m { \dot { y } }$ , etc., so $\begin{array} { r } { \sum _ { i } \dot { q } _ { k } p _ { k } = m ( \dot { x } ^ { 2 } + \dot { y } ^ { 2 } + \dot { z } ^ { 2 } ) } \end{array}$ Therefore

$$
\begin{array}{c} H = m (\dot {x} ^ {2} + \dot {y} ^ {2} + \dot {z} ^ {2}) - \frac {1}{2} m (\dot {x} ^ {2} + \dot {y} ^ {2} + \dot {z} ^ {2}) + U (x, y, z) \\ = \frac {1}{2} m (\dot {x} ^ {2} + \dot {y} ^ {2} + \dot {z} ^ {2}) + U (x, y, z) = T + U = E, \end{array}\tag{4.85}
$$

which is simply the energy of the particle. Therefore, since this Lagrangian does not depend on time explicitly, this energy quantity is conserved, as expected.

Is H always equal to $\begin{array} { r } { E = T + U ? } \end{array}$ The answer is no, although very often it is. The precise conditions for which $H \neq E$ are worked out in Section 4.7.

## Example 4.8

## Bead on a Rotating Parabolic Wire

Suppose we bend a wire into the shape of a vertically oriented parabola defined in cylindrical coordinates by $z = \alpha \rho ^ { 2 }$ , as illustrated in Figure 4.12: here z is the vertical coordinate, and $\rho$ is the distance of a point on the wire from the vertical axis of symmetry. Using a synchronous motor, we can force the wire to spin at constant angular velocity $\omega$ about its symmetry axis. Then we slip a bead of mass m onto the wire and we want to determine its equation of motion – assuming that it slides without friction along the wire.

![](images/91b9124fbe12ffd6ded9d1e32d06b2ae904d8f8a3b97801b0121a79fb6397a71.jpg)  
A bead slides without friction on a vertically oriented parabolic wire forced to spin about its axis of symmetry.

## Fig. 4.12

We first have to choose generalized coordinate(s) for the bead. The bead moves in three dimensions, but because of the constraint confining the bead along the wire we need only a single generalized coordinate to specify the bead’s position. For example, if we know the distance $\rho$ of the bead from the vertical axis of symmetry, we also know its altitude $z , z = \alpha \rho ^ { 2 }$ . And the bead also has no freedom to choose its azimuthal angle, because the synchronous motor turns the wire around at a constant rate. Given its angle $\varphi _ { 0 }$ at time $t = 0 ,$ , its angle at other times is constrained to be $\varphi = \varphi _ { 0 } + \omega t$ . Hence, we start with three coordinates and, using two constraint conditions, we end up with just one degree of freedom. It is convenient to choose the cylindrical coordinate $\rho$ as the single generalized coordinate, although we could equally well choose the vertical coordinate z.

In cylindrical coordinates the square of the bead’s velocity is the sum of squares of the velocities in the $\rho , \varphi ,$ and z directions:

$$
v ^ {2} = \dot {\rho} ^ {2} + \rho^ {2} \dot {\varphi} ^ {2} + \dot {z} ^ {2} = \dot {\rho} ^ {2} + \rho^ {2} \omega^ {2} + (2 \alpha \rho \dot {\rho}) ^ {2},\tag{4.86}
$$

using the constraints $\dot { \varphi } = \omega =$ constant and $z = \alpha \rho ^ { 2 }$ for the parabolic wire. The gravitational potentia energy is $U = m g z = m g \alpha \rho ^ { 2 } .$ , so the Lagrangian becomes

$$
L = T - U = \frac {1}{2} m \left[ \left(1 + 4 \alpha^ {2} \rho^ {2}\right) \dot {\rho} ^ {2} + \rho^ {2} \omega^ {2} \right] - m g \alpha \rho^ {2}.\tag{4.87}
$$

We implemented two constraints, $\dot { \varphi } = \omega \mathsf { a n d } z = \alpha \rho ^ { 2 }$ , and thus reduced the problem from three variables to one, the radius $\rho .$ The contact force that keeps the bead on the wire is the normal force associated with these two constraints. We do not include its contribution to the Lagrangian, assuming that this normal force has no contribution to the energy of the system. That this is correct is far from obvious in this case, since this normal force does work! The normal force in this case is not perpendicular to the displacement. This work is associated with the energy input by the motor to keep the wire turning at constant rate $\omega .$ . Let us proceed anyway, and revisit the issue at the end. The partial derivatives $\partial L / \partial \dot { \rho }$ and $\partial L / \partial \rho$ are easy to find, leading to the Lagrange equation

$$
\frac {\partial L}{\partial \rho} - \frac {d}{d t} \frac {\partial L}{\partial \rho} = m \left[ 4 \alpha^ {2} \rho \dot {\rho} ^ {2} + \rho \omega^ {2} - 2 g \alpha \rho \right] - m \frac {d}{d t} \left[ (1 + 4 \alpha^ {2} \rho^ {2}) \dot {\rho} \right] = 0,\tag{4.88}
$$

which results in a second-order diferential equation of motion for $\rho \mathrm { : }$

$$
(1 + 4 \alpha^ {2} \rho^ {2}) \ddot {\rho} + 4 \alpha^ {2} \rho \dot {\rho} ^ {2} + (2 g \alpha - \omega^ {2}) \rho = 0.\tag{4.89}
$$

Are we stuck with having to solve this second-order diferential equation? Are there no first integrals of motion? The coordinate $\rho$ is not cyclic, so $p _ { \rho }$ is not conserved. However, note that L is not an explicit function oftime, $\partial { \cal L } / \partial t = 0 .$ , so the Hamiltonian H is conserved according to Eq. (4.84). Conservation of H gives us a first integral of motion, so we are rescued: we do not have to solve the second-order diferential equation (4.89) after all, given that we have one degree of freedom and one first integral of motion.

The generalized momentum is $p _ { \rho } = \partial L / \partial \dot { \rho } = m ( 1 + r \alpha ^ { 2 } \rho ^ { 2 } ) \dot { \rho } ,$ , so the Hamiltonian is

$$
\begin{array}{l} H = \dot {\rho} p _ {\rho} - L = m (1 + 4 \alpha^ {2} \rho^ {2}) \dot {\rho} ^ {2} - \frac {1}{2} m [ (1 + 4 \alpha^ {2} \rho^ {2}) \dot {\rho} ^ {2} + \rho^ {2} \omega^ {2} ] + m g \alpha \rho^ {2} \\ = \frac {1}{2} m [ (1 + 4 \alpha^ {2} \rho^ {2}) \dot {\rho} ^ {2} - \rho^ {2} \omega^ {2} ] + m g \alpha \rho^ {2} = \text { constant }, \end{array}\tag{4.90}
$$

which difers from the energy

$$
E = T + U = \frac {1}{2} m \left[ \left(1 + 4 \alpha^ {2} \rho^ {2}\right) \dot {\rho} ^ {2} + \rho^ {2} \omega^ {2} \right] + m g \alpha \rho^ {2}\tag{4.91}
$$

by $H - E = - m \rho ^ { 2 } \omega ^ { 2 }$ . Note that this diference changes as $\rho$ changes; that is because even though H is conserved, the energy E is not conserved, because the normal force of the wire does work on the bead.

Equation (4.90) is a first-order diferential equation, which can be reduced to quadrature. Without going that far, we can understand a good deal about the motion just by using Eq. (4.90), and noting that it has a similar mathematical form to that of energy-conservation equations. That ${ \mathrm { i } } \mathsf { s } ,$ rewrite the equation as

$$
H = \frac {1}{2} m (1 + 4 \alpha^ {2} \rho^ {2}) \dot {\rho} ^ {2} + U _ {\text { eff }},\tag{4.92}
$$

where

$$
U _ {\text { eff }} = \frac {1}{2} m (- \rho^ {2} \omega^ {2}) + m g \alpha \rho^ {2} = \frac {1}{2} m \rho^ {2} (2 g \alpha^ {2} - \omega^ {2}).\tag{4.93}
$$

This efective potential is quadratic in $\rho ,$ with the interesting feature that its sign depends upon how the angular velocity $\omega$ of the wire is related to a critical angular velocity $\omega _ { \mathrm { c r i t } } \equiv ( 2 g ) ^ { 1 / 2 } \alpha _ { \cdot }$ , as illustrated in

Figure 4.13. If $\omega < \omega _ { \mathrm { c r i t } }$ , then $U _ { \mathrm { e f f } }$ rises with $\rho ,$ so the bead is stable at $\rho = 0 ,$ , the potential minimum. But if ω $> \omega _ { \mathrm { c r i t } }$ , then $U _ { \mathrm { e f f } }$ falls of with increasing $\rho , { \sf s } 0 \rho = 0$ is an unstable equilibrium point in that case: if the bead wanders even slightly from $\rho = 0$ at the bottom of the parabola, it will be thrown out indefinitely far. The stability is neutral if $\omega = \omega _ { \mathrm { c r i t } }$ , meaning that if placed at rest at any point along the wire, the bead will stay at that point indefinitely; but if placed at any point and pushed outward it will keep moving outward, or if pushed inward it will keep moving inward.

This example shows that although the Hamiltonian function H is often equal to $\begin{array} { r } { E \equiv I + U , } \end{array}$ , this is not always so. Section 4.7 explains when and why they can difer. In any case, the Hamiltonian can be very useful, because it provides a first integral of motion if L is not explicitly time dependent.

![](images/9c01fb5ef57cd745518872e5f57dba5a5a2819da1714db0bb590e7bd7a5d4d6f.jpg)

The effective potential $U _ { \mathrm { e f f } }$ for the Hamiltonian of a bead on a rotating parabolic wire with $z = \alpha \rho ^ { 2 }$ depending upon whether the angular velocity $\omega$ is less than, greater than, or equal to $\omega _ { \mathrm { c r i t } } = { \sqrt { 2 g } } \alpha$

Once again, the Lagrangian formalism avoids dealing with contact forces and accounts for them through constraints – simplifying the problem significantly. We leave it as an exercise for the reader to solve this same problem using traditional force body diagram methods so as to appreciate the power of the Lagrangian formalism.

## 4.7 When is $\pmb { H } \neq \pmb { E } \pmb { \ ? }$

In Example 4.8 the Hamiltonian H was not equal to E. Why were they different, and why was H conserved while E was not?

The definition $H = \dot { q } _ { k } \partial L / \partial \dot { q } _ { k } - L$ (using the Einstein summation convention, implying a sum over k in the first term on the right, since k is repeated in that term) contains the Lagrangian $L = T - U ,$ where only the kinetic energy T depends upon the generalized velocities $\dot { \boldsymbol { q } } _ { k }$ . Therefore:

$$
H = \dot {q} _ {k} \frac {\partial T}{\partial \dot {q} _ {k}} + U - T.\tag{4.94}
$$

Now let $\mathbf { r } ( q _ { k } , t )$ be the position vector of the particle from some arbitrary origin fixed in an inertial frame, in terms of the time and any or all of the generalized coordinates $q _ { k }$ . Then the velocity of the particle is

$$
\mathbf {v} = \frac {d \mathbf {r} (q _ {k} , t)}{d t} = \frac {\partial \mathbf {r}}{\partial t} + \frac {\partial \mathbf {r}}{\partial q _ {l}} \dot {q} _ {l},\tag{4.95}
$$

because r can change with time either from an explicit time dependence or because one or more of the generalized coordinates changes with time. Therefore its kinetic energy is $T = ( 1 / 2 ) m \nu ^ { 2 } = ( 1 / 2 ) m \mathbf { v } \cdot \mathbf { v }$ , which is

$$
T = \frac {1}{2} \left[ m \frac {\partial \mathbf {r}}{\partial t} \cdot \frac {\partial \mathbf {r}}{\partial t} + 2 \frac {\partial \mathbf {r}}{\partial t} \cdot \frac {\partial \mathbf {r}}{\partial q _ {l}} \dot {q} _ {l} + \frac {\partial \mathbf {r}}{\partial q _ {l}} \dot {q} _ {l} \cdot \frac {\partial \mathbf {r}}{\partial q _ {m}} \dot {q} _ {m} \right],\tag{4.96}
$$

where we have used a different dummy summation index m in the final factor to distinguish it from the sum over l in the preceding factor. That is, by the Einstein summation convention the final term above is actually the product of two sums, one over l and one over m. Now we can take the partial derivative of T with respect to a particular one of the generalized velocities ${ \dot { q } } _ { k } .$

$$
\frac {\partial T}{\partial \dot {q} _ {k}} = \frac {1}{2} m \left[ 2 \frac {\partial \mathbf {r}}{\partial t} \cdot \frac {\partial \mathbf {r}}{\partial q _ {k}} + 2 \frac {\partial \mathbf {r}}{\partial q _ {k}} \cdot \frac {\partial \mathbf {r}}{\partial q _ {l}} \dot {q} _ {l} \right],\tag{4.97}
$$

where there is a factor of two in the second term because $\dot { \boldsymbol { q } } _ { k }$ occurs in both summations in the last term of the expression for T. Therefore the sum

$$
\begin{array}{r l} \dot {q} _ {k} \frac {\partial T}{\partial \dot {q} _ {k}} & = m \left[ \frac {\partial \mathbf {r}}{\partial t} \cdot \frac {\partial \mathbf {r}}{\partial q _ {k}} \dot {q} _ {k} + \frac {\partial \mathbf {r}}{\partial q _ {k}} \dot {q} _ {k} \cdot \frac {\partial \mathbf {r}}{\partial q _ {l}} \dot {q} _ {l} \right] \\ & = 2 T - m \frac {\partial \mathbf {r}}{\partial t} \cdot \left[ \frac {\partial \mathbf {r}}{\partial t} + \frac {\partial \mathbf {r}}{\partial q _ {k}} \dot {q} _ {k} \right] \\ & = 2 T - m \frac {\partial \mathbf {r}}{\partial t} \cdot \frac {d \mathbf {r}}{d t}, \end{array}\tag{4.98}
$$

using Eqs. (4.96) and (4.97). The Hamiltonian H can therefore be written as

$$
H = E - m \frac {d \mathbf {r}}{d t} \cdot \frac {\partial \mathbf {r}}{\partial t} = E - \mathbf {p} \cdot \frac {\partial \mathbf {r}}{\partial t},\tag{4.99}
$$

where p is the momentum of the particle in the chosen inertial frame. If the transformation $\mathbf { r } = \mathbf { r } ( q _ { k } , t )$ between the Cartesian coordinates $\mathbf { r } ~ = ~ ( x , y , z )$ and the generalized coordinates $q _ { k }$ happens not to be an explicit function of time, $i . e .$ if ${ \partial \mathbf { r } } / { \partial t } = 0 .$ , then the Hamiltonian is just $T + U .$ . This case occurs when there are no constraints or when any constraints are fixed in space. But if the constraints are moving, then the transformation $\mathbf { r } = \mathbf { r } ( q _ { k } , t )$ does generally depend upon time, and so in the likely case that there is a component of $\partial \mathbf { r } / \partial t$ in the direction of the particle’s momentum p, the Hamiltonian is not equal to $T + U .$

For the problem of the bead on a rotating parabolic wire, where the constraint is obviously moving, the position vector ofthe bead can be taken to be $\mathbf { r } = ( x , y , z ) =$ (r cos ωt, r sin ωt, $\overline { { \alpha r ^ { 2 } } } )$ . In that case we found that $H = T + U - m \omega ^ { 2 } r ^ { 2 }$ , and it is easy to show that $m \omega ^ { 2 } r ^ { 2 } = \mathbf { p } \cdot { \partial \mathbf { r } } / { \partial t } ,$ , as required by Eq. (4.99). It is clear that E is not conserved in this case because the rotating wire is continually doing work on the bead. The wire exerts a force $F ^ { \theta }$ in the tangential direction, which causes work to be done at the rate $d W / d t = F ^ { \theta } \nu ^ { \theta } = F ^ { \theta } r \bar { \omega }$ . From the elementary relationship $N ^ { z } = d L ^ { z } / d t$ , with torque $N ^ { z } = F ^ { \theta } r$ and angular momentum $L ^ { z } = ( \mathbf { r } \times \mathbf { p } ) ^ { z } = m r ^ { 2 } \omega .$ it follows that

$$
\frac {d W}{d t} = \omega \frac {d (m r ^ {2} \omega)}{d t} = m \omega^ {2} \frac {d r ^ {2}}{d t},\tag{4.100}
$$

so that the work done by the wire is $W = m \omega ^ { 2 } r ^ { 2 }$ plus a constant of integration, which depends upon the initial location of the bead. Thus the energy $E = T + U$ of the bead increases by the work done upon it by the wire, so that E minus the work done must be conserved, and that difference $E - m \omega ^ { 2 } r ^ { 2 } = H .$

Note that:

1. H is conserved if the Lagrangian L is not an explicit function of time.

2. $H = E$ if the coordinate transformation $\mathbf { r } = \mathbf { r } ( q _ { k } , t )$ is not an explicit function of time.

Therefore it is possible to have $E = H ,$ with both E and H conserved, or neither conserved, and it is also possible to have $E \neq H ,$ , with both conserved, neither conserved, or only one of the two conserved.

## 4.8 The Moral of Constraints

Let us summarize the steps we have used so far in setting up and preparing to solve Lagrange’s equations.

1. Identify the degrees of freedom of each particle or object consistent with any constraints, and choose an appropriate set of generalized coordinates $q _ { k }$ for each.

2. Write the square of the velocity for each particle in terms of any convenient coordinates, usually Cartesian coordinates, in some inertial reference frame. Then re-express the kinetic energy in terms of the generalized coordinates $q _ { k } .$ the generalized velocities $\dot { \boldsymbol { q } } _ { k }$ , and the time if needed; $\bar { i } . e . , \nu ^ { 2 } = \nu ^ { 2 } ( q _ { k } , \dot { q } _ { k } , t )$ . Then write the total kinetic energy T in terms of these variables.

3. Write the total potential energy in the form $U = U ( q _ { k } , t )$ . Do not include any contributions from constraint forces.

4. Write the Lagrangian $L ( t , q _ { 1 } , q _ { 2 } , . . . , \dot { q } _ { 1 } , \dot { q } _ { 2 } , . . . ) = T - U .$

5. Identify any cyclic coordinates in $L ;$ ; that is, identify any coordinate $q _ { l }$ missing in the Lagrangian, even though its corresponding generalized velocity q˙ is present. In this case the corresponding generalized momentum $p _ { l } \equiv \partial L / \partial \dot { q } _ { l }$ is conserved.

This gives a highly valued first integral of motion, i.e., a differential equation that is first order rather than second order.

6. If L is not an explicit function of time, then the Hamiltonian $H \equiv \dot { q } _ { k } p _ { k } - L$ is conserved, providing another first integral of motion.

7. If there are more generalized coordinates in the problem than first integrals identified in the preceding steps, then one or more of the Lagrange equations of motion

$$
\frac {\partial L}{\partial q _ {k}} - \frac {d}{d t} \frac {\partial L}{\partial \dot {q} _ {k}} = 0\tag{4.101}
$$

must be used as well, to obtain a complete set of differential equations. That is, if there are N generalized coordinates, we will generally need N mutually independent differential equations whose solutions will give the coordinates as functions of time. Some of these may be first-order equations, each corresponding to a conserved quantity, while others may be second-order equations coming from Eq. (4.101).

All these steps were justified: that the Lagrangian $L = T - U$ accounts for all conservative forces, that coordinate transformations at the Lagrangian level are justified and in fact very useful, and that constraints assure that the generalized coordinates are independent and a reduced set of degrees of freedom describes the dynamics fully. As one gets used to the steps outlined above, many stages of this algorithmic process become second nature and can be done mentally. With practice, one looks at a complex mechanical system, writes down the Lagrangian immediately on a single line, and in a few more lines, writes the equations of motion! To get there, however, one needs to practice, practice, practice.

Why can we avoid constraint forces in the Lagrangian? We saw example after example in which neglecting them works out fine. We see an emerging pattern. Constraint forces implement restrictions on the dynamics between two objects in contact. If both objects in question are part of the dynamical system (i.e., they both contribute kinetic energy to the Lagrangian), these constraint forces must come in equal and opposite pairs. Since the contact point is the same, this always implies that such forces will not do work and hence need not appear in the Lagrangian. On the contrary, if only one of the two objects is part of the dynamical system, the other one must then have prescribed time evolution by definition: i.e., the ground just sits there as a function of time, the pivot of the pendulum is fixed in position, a parabolic wire – on which a bead is sliding – is rotating at a given constant angular speed driven by a motor. In some of these cases, the constraint forces do no work because they are perpendicular to the displacement. But it is easy to see this statement in more generality: extend the Lagrangian to include the nondynamical system – the ground, the parabolic wire connected to a motor – by adding their constant kinetic energies to the Lagrangian. Then the constraint force becomes part of an internal action–reaction pair, which we know does not contribute to the Lagrangian! And the cost of adding the kinetic energy of the external agent to the Lagrangian is irrelevant: it is a constant shift to the Lagrangian since the relevant dynamics is, by definition, prescribed. This, we now see, is one of the central advantages of the Lagrangian formalism: We can drop all constraintforces from the outset.

## 4.9 Small Oscillations about Equilibrium

We often find that a system of interest is at or near a state of stable equilibrium. For example, a nearby chair rests on the floor, happily doing nothing. It is in a minimal energy configuration relative to nearby configurations. If we bump the chair it may wobble and slide a bit, and then quickly come to rest again in some new equilibrium state. When we bumped the chair, we added energy to the system, and the chair eventually dissipated this energy through friction and returned to a minimal-energy, motionless state.

In general, many if not most mechanical systems can be accorded an energy of the form

$$
\mathrm{Constant} \times \dot {q} _ {k} ^ {2} + U _ {\mathrm{eff}} (q _ {k}) = E,\tag{4.102}
$$

where the $q _ { k } \mathbf { S }$ are the generalized coordinates and $U _ { \mathrm { e f f } }$ is an effective potential. We have seen this in several examples. For simplicity, imagine we have only one such coordinate, which we will call $q .$ . If the effective potential energy $U _ { \mathrm { e f f } }$ has an extremum at some particular point $q _ { 0 }$ , then that point is an equilibrium point of the motion, so if placed at rest at $q _ { 0 }$ the particle will stay there. If $q _ { 0 }$ happens to be a minimum of $U _ { \mathrm { e f f } }$ , as illustrated in Figure 4.14, $q _ { 0 }$ is a stable equilbrium point, so that if the particle is displaced slightly from $q _ { 0 }$ it will oscillate back and forth, never wandering far from that point. It is sometimes interesting to find the frequency of small oscillations about an equilibrium point. We can often do this by fitting the bottom of the effective potential energy curve to a parabola, which is the shape of the potential energy of a simple harmonic oscillator. That is, by the Taylor expansion, we write (see Appendix F))

![](images/b4d086f68fb9e2a7477b9666d5fa8169e6cfd35ad4c9bdcc862064459dec1b52.jpg)  
Fig. 4.14 An efective potential energy $U _ { \mathrm { e f f } }$ with a focus near a minimum. Such a point is a stable equilibrium point. The dotted parabola shows the leading approximation to the potential near its minimum. As the energy drains out, the system settles into its minimum, with the final moments being well approximated by harmonic oscillatory dynamics.

$$
U _ {\text { eff }} (q) = U _ {\text { eff }} (q _ {0}) + \left. \frac {d U _ {\text { eff }}}{d q} \right| _ {\mathrm{q} _ {0}} (q - q _ {0}) + \frac {1}{2 !} \left. \frac {d ^ {2} U _ {\text { eff }}}{d q ^ {2}} \right| _ {\mathrm{q} _ {0}} (q - q _ {0}) ^ {2} + \dots\tag{4.103}
$$

So if $q _ { 0 }$  is the equilibrium point, by definition the second term vanishes, and the third term has the form $( 1 / 2 ) k _ { \mathrm { e f f } } ( q - q _ { 0 } ) ^ { 2 }$ , like that for a simple harmonic oscillator with center at $q _ { 0 }$ , where the effective force constant is given by $k _ { \mathrm { e f f } } = U _ { \mathrm { e f f } } ^ { \prime \prime } ( q _ { 0 } )$ . The frequency of small oscillations is therefore

$$
\omega = \sqrt {\frac {k _ {\mathrm{eff}}}{m}} = \sqrt {\frac {U _ {\mathrm{eff}} ^ {\prime \prime} (q _ {0})}{m}}.\tag{4.104}
$$

Note that this explains the pervasiveness of the harmonic oscillator in Nature: systems will try to find their lowest-energy configurations by dissipating energy, so often find themselves near the minima of their effective potentials.<sup>5</sup> An example will demonstrate.

Example 4.9

## Particle on a Tabletop with a Central Spring Force

In Example 4.4 we considered a particle moving on a frictionless tabletop subject to a central Hooke’s-law spring force. There is an equilibrium radius for given energy and angular momentum for which the particle orbits in a circle of some radiu $r _ { 0 } .$ We now want to find the oscillation frequency $\omega$ for the mass about the equilibrium radius if it were perturbed slightly from this circular orbit.

The efective potential in Example 4.4 was

$$
U _ {\text { eff }} = \frac {(p _ {\varphi}) ^ {2}}{2 m r ^ {2}} + \frac {1}{2} k r ^ {2}\tag{4.105}
$$

from Eq. (4.28); the first derivative of this potential is $U _ { \mathsf { e f f } } ^ { \prime } ( r ) = - ( p _ { \varphi } ) ^ { 2 } / m r ^ { 3 } + k r$ . The equilibrium value of r is located where $U _ { \mathrm { e f f } } ^ { \prime } ( r ) = 0 ;$ namely, where $r = r _ { 0 } = ( ( p _ { \varphi } ) ^ { 2 } / m k ) ^ { 1 / 4 }$

The second derivative of $U _ { \mathrm { e f f } } ( \boldsymbol { r } )$ is

$$
U _ {\mathrm{eff}} ^ {\prime \prime} (r) = \frac {3 (p _ {\varphi}) ^ {2}}{m r ^ {4}} + k,\tag{4.106}
$$

so

$$
U _ {\text { eff }} ^ {\prime \prime} (r _ {0}) = \frac {3 (p _ {\varphi}) ^ {2}}{m ((p _ {\varphi}) ^ {2} / m k)} + k = 3 k + k = 4 k = k _ {\text { eff }} > 0.\tag{4.107}
$$

From Eq. (4.104), the frequency of small oscillations about the equilibrium radius $r _ { 0 }$ is therefore

$$
\omega = \sqrt {\frac {U _ {\mathrm{eff}} ^ {\prime \prime} (r _ {0})}{m}} = \sqrt {\frac {4 k}{m}} = 2 \omega_ {0}.\tag{4.108}
$$

That ${ \mathrm { i } } \mathsf { s } ,$ for the mass orbiting the origin and subject to a central Hooke’s-law spring force, the frequency of small oscillations about a circular orbit is just twice what it would be for the mass if it were oscillating back and forth about the center in one dimension.

We can also find the shape of the orbits, noting that the radial oscillations are small. The angular frequency of rotation is $\omega _ { \mathsf { r o t } } = v _ { \phi } / r _ { o } = ( p _ { \varphi } / m r _ { 0 } ) / r _ { 0 } = p _ { \varphi } / ( m r _ { 0 } ^ { 2 } )$ , where $\displaystyle \boldsymbol { v } _ { \phi }$ is the tangential component of velocity. But the equilibrium radius is $r _ { 0 } = ( ( p _ { \varphi } ) ^ { 2 } / m k ) ^ { 1 / 4 }$ , so the angular frequency of rotation is $\omega _ { \sf r o t } = p _ { \varphi } / ( m r _ { 0 } ^ { 2 } ) = p _ { \varphi } / [ m \sqrt { ( p _ { \varphi } ) ^ { 2 } / k } ] = \sqrt { k / m } = \omega _ { 0 } ,$ which is the same as the frequency of oscilla-<sub>tion ofthe system as ifit were oscillating in one dimension through the center. Therefore, the frequency of radial</sub> oscillations (4.108) is just twice the rotational frequency, so the orbits for small oscillations are closed: that is, the path retraces itselfin every orbit, as shown in Figure 4.15. The small-oscillation path appears to be elliptical. In fact, it is exactly elliptical, even for large displacements from equilibrium, as we already saw in Chapter 1 using Cartesian coordinates.

![](images/7bb927bc155c37999306f3661302b5cc30e88da8ca093743c1d5fba352ff703a.jpg)

The shape ofthe two-dimensional orbit ofa particle subject to a central spring force, for small oscillations about the equilibrium radius.

## 4.10 Recap

We began the chapter by describing a conservative mechanical system by N generalized coordinates $q _ { k } ( t )$ , with $k = 1 , 2 , \ldots , N ,$ and then defining the Lagrangian

$$
L (t, q _ {1}, q _ {2}, \dots , \dot {q} _ {1}, \dot {q} _ {2}, \dots) = T - U
$$

(4.109)

as the difference between the kinetic and potential energies of the system, expressed in terms of the generalized coordinates $q _ { k } .$ , generalized velocities ${ \dot { q } } _ { k } ,$ , and time t. We then define the action $S [ q _ { k } ( t ) ]$ of the system as the functional consisting of the time integral over the Lagrangian $L ( t , q _ { 1 } , q _ { 2 } , . . . , \dot { q } _ { 1 } , \dot { q } _ { 2 } , . . . )$ , from a starting time $t _ { a }$ to an ending time $t _ { b }$ :

$$
S [ q _ {k} (t) ] = \int_ {\mathrm{t} _ {\mathrm{a}}} ^ {t _ {b}} d t L (t, q _ {1}, q _ {2}, \dots , \dot {q} _ {1}, \dot {q} _ {2}, \dots) \equiv \int_ {\mathrm{t} _ {\mathrm{a}}} ^ {t _ {b}} d t L (t, q _ {k}, \dot {q} _ {k}),\tag{4.110}
$$

where it is understood that the particle or system ofparticles begins at some definite position $( q _ { 1 } , q _ { 2 } , \ldots ) _ { a }$ at time $t _ { a }$ and ends at some definite position $( q _ { 1 } , q _ { 2 } , \ldots ) _ { b }$ at time $t _ { b }$ .

Hamilton’s principle then proposes that, for trajectories $q _ { k } ( t )$ where the action S is stationary – i.e., when

$$
\delta S = \delta \int_ {t _ {\mathrm{a}}} ^ {t _ {b}} L (t, q _ {k}, \dot {q} _ {k}) d t = 0,\tag{4.111}
$$

the coordinates $q _ { k } ( t )$ satisfy the equations of motion for the system with the prescribed boundary conditions at $t _ { a }$ and $t _ { b }$ . That is, the variational principle $\delta S = 0$ gives the Lagrange equations

$$
\frac {d}{d t} \frac {\partial L}{\partial \dot {q} _ {k}} - \frac {\partial L}{\partial q _ {k}} = 0 \quad (k = 1, 2, \dots , N),\tag{4.112}
$$

which are the second-order differential equations of motion for the system.

We also defined the Hamiltonian of the system to be

$$
H \equiv \dot {q} _ {k} p _ {k} - L,\tag{4.113}
$$

where a sum over k is implied, and the generalized momenta $p _ { k }$ are defined as

$$
p _ {k} = \frac {\partial L}{\partial \dot {q} _ {k}}.\tag{4.114}
$$

Then

$$
\frac {\partial L}{\partial t} = - \frac {d H}{d t},\tag{4.115}
$$

so if L is not an explicit function of time, it follows that the Hamiltonian is conserved. In this case, and also when a coordinate is cyclic, we are led to first integrals of motion – that is, first-order differential equations.

If the problem is simple, exact analytic solutions of the first- and second-order differential equations may be possible. If not, we can always solve the equations numerically on a computer. There is also a very common intermediate situation, when one or more of the equations is too difficult to solve exactly, but approximate analytic techniques can be used to find the answer as accurately as required. Finding a sufficiently accurate approximate analytic technique to solve a particular problem can be very entertaining, requiring as much creativity as setting up the physical problem in the first place. One of the pleasures of doing physics is to find a way, no holds barred, to solve a problem to the extent we need it solved, using back-of-the-envelope calculations, dimensional reasoning, approximate analytical techniques, numerical calculations, or whatever it takes to get the job done.

Note that we have confined ourselves in this chapter to nonrelativistic motion. Is it possible to generalize the action and the Lagrangian to provide the correct equations of motion for relativistic particles? The answer is a somewhat qualified “yes,” but we will have to postpone a discussion of this interesting topic until Chapter 8, where we will find how to deal with relativistically correct electromag netic potential energies.

This chapter has concentrated on a primary cornerstone of the modern subject of theoretical mechanics. It has presented a reformulation of mechanics by means of a variational principle, where the central quantity is the Lagrangian. All of dynamics is packaged into a single functional. Beyond the elegance of the approach, the Lagrangian formalism gives us two additional benefits. First, by eliminating the need to keep track of a myriad of forces, it helps us zero onto the relevant mechanics and the associated differential equations; thus, it provides us a powerful new technical tool for tackling complex mechanics problem. Second, as we shall see in the next chapter, the formalism presents a natural conceptual bridge from the classical to the quantum world. Historically, the Lagrangian and the related Hamiltonian formalisms (see Chapter 11) played key roles in the development of the subject of quantum mechanics and modern physics.

## Problems

Problem 4.1 In Example 4.3, we found the equation of motion of a block on an inclined plane, using the generalized coordinate X, the distance of the block from the bottom of the incline. Solve the equation for X(t) in terms of an arbitrary initial position X(0) and velocity X<sup>˙</sup>(0).

Problem 4.2 A particle of mass m slides inside a smooth hemispherical bowl of radius R. Beginning with spherical coordinates r, θ, and $\varphi$ to describe the dynamics, select generalized coordinates, write the Lagrangian, and find the differential equations of motion of the particle.

Problem 4.3 Example 4.2 featured a bead sliding on a vertically oriented helix of radius R. The angle θ about the symmetry axis was related to its vertical coordinate z on the wire by $\theta = \alpha z$ . There is a uniform gravitational field g vertically downward. (a) Rewrite the Lagrangian and find the Lagrange equation, using θ as the generalized coordinate. (b) Are there any conserved dynamical quantities? (c) Write the simplest differential equation of motion of the bead, and go as far as you can to solve analytically for θ as a function of time.

Problem 4.4 One end of a wire is tied to a point A on the ceiling and the other end is tied to a point on a ring of radius R and negligible mass. The ring therefore hang from the wire in a vertical plane and in a gravitational field g. A bead of mass m is threaded onto the ring so it can slide around the ring without friction. The lowest point on the ring is then tied to a second wire whose opposite end is attached to point B on the floor, where point B is directly beneath point A. The wires are then drawn taut. If the ring and attached wires are made to twist sideways through an angle $\varphi$ away from equilibrium, a potential energy $( 1 / 2 ) \kappa \varphi ^ { 2 }$ is set up in the wire. (a) Using angles $\theta$ and $\varphi$ as generalized coordinates, where $\theta$ is the angle of the bead down from the top of the ring, find the kinetic and potential energies of the bead. (b) Find the equations of motion using Lagrange’s equations. Assume that during the motion of the bead it remains entirely on one side of the ring, so it does not meet the wires at $\theta = 0$ and $\theta = \pi$

Problem 4.5 A particle moves in a cylindrically symmetric potential $U ( \rho , z )$ . Use cylindrical coordinates $\rho , \varphi _ { : }$ , and $z$ to parameterize the space.

(a) Write the Lagrangian for an unconstrained particle of mass m (using cylindrical coordinates) in the presence of this potential.

(b) Write the Lagrange equations of motion for $\rho , \varphi ;$ , and z.

(c) Identify any cyclic coordinates, and write a first integral corresponding to each.

Problem 4.6 A particle of mass m slides inside a smooth paraboloid of revolution whose axis of symmetry z is vertical. The surface is defined by the equation $z =$ $\alpha \rho ^ { 2 }$ , where $z$ and $\rho$ are cylindrical coordinates, and $\alpha$ is a constant. There is a uniform gravitational field g. (a) Select two generalized coordinates for m. (b) Find $T , U ,$ and $L .$ (c) Identify any ignorable coordinates, and any conserved quantities. (d) Show that there are two first integrals of motion, and find the corresponding equations.

Problem 4.7 Repeat the preceding problem for a particle sliding inside a smooth cone defined by $z = \alpha r$

Problem 4.8 A spring pendulum features a pendulum bob of mass m attached to one end of a spring of force constant k and unstretched length R. The other end of the spring is attached to a fixed point on the ceiling. The pendulum is allowed to swing in a plane. Use $r ,$ the distance ofthe bob from the fixed point, and $\theta ,$ the angle ofthe spring relative to the vertical, as generalized coordinates. (a) Find the kinetic and potential energies of the bob in terms of the generalized coordinates and velocities. (b) Find the Lagrangian. Are there any ignorable coordinates? (c) Are there any conserved quantities? (d) Find a complete set of equations of motion, including as many first integrals as possible.

Problem 4.9 A pendulum is constructed from a bob of mass m on one end of a light string of length $D .$ . The other end of the string is attached to the top of a circular cylinder of radius R $\left( R < 2 D / \pi \right)$ . The string makes an angle $\theta$ with the vertical, as shown in Prob. 4.9, as the pendulum swings in the plane. There is a uniform gravity g directed downward. (a) Find the Lagrangian ofthe bob, using θ as the generalized coordinate. (b) Identify any first integrals ofmotion. (c) Find the frequency ofsmall oscillations about the stable equilibrium point.

Prob. 4.9 A pendulum hanging from a cylinder.  
![](images/d34e1f68c705eb28019836c46e6e263ad7002da69c9543e581cf4d7cbb84a02d.jpg)

Problem 4.10 A particle moves with a cylindrically symmetric potential energy $U = U ( \rho , z )$ , where $\rho , \varphi , z$ are cylindrical coordinates. (a) Write the Lagrangian for an unconstrained particle of mass m in this case. (b) Are there any cyclic coordinates? If so, what symmetries do they correspond to, and what are the resulting constants of motion? (c) Write the Lagrange equation for each cyclic coordinate. (d) Find the Hamiltonian H. Is it conserved? (e) Find the total energy E. Is $E = H ?$ is E conserved? (f) Write the simplest (i.e., lowest-order) complete set of differential equations of motion of the particle.

Problem 4.11 A plane pendulum is made with a plumb bob of mass m hanging on a Hooke’s-law spring of negligible mass, force constant k, and unstretched length $\ell _ { 0 }$ . The spring can stretch but is not allowed to bend. There is a uniform downward gravitational field g. (a) Select generalized coordinates for the bob, and find the Lagrangian in terms of them. (b) Write out the Lagrange equations of motion. (c) Are there any conserved quantities? Ifso, write down the corresponding conservation law(s). (d) If the bob is swinging back and forth, find the frequency of small oscillations in the general case where the spring can change its length while the bob is swinging back and forth.

Problem 4.12 Motion in a slowly changing uniform electricfield. A particle of mass m and charge $q$ moves within a parallel-plate capacitor whose charge $\boldsymbol { Q }$ decays exponentially with time, $Q = Q _ { 0 } e ^ { - t / \tau }$ , where $\tau$ is the time constant of the decay. Find the equations of motion of the particle. Ignore the effect of any magnetic field that may be generated from the changing eletric field.

Problem 4.13 A particle of mass m travels between two points $x = 0$ and $x = x _ { 1 }$ on earth’s surface, leaving at time $t = 0$ and arriving at $t = t _ { 1 }$ . The gravitational field $_ g$ is uniform. (a) Suppose m moves along the ground (keeping altitude $z = 0 )$ at steady speed. Find the total action S to go by this path. (b) Suppose instead that m moves along the least-action parabolic path. Show that the action in this case is

$$
S = \frac {m x _ {1} ^ {2}}{2 t _ {1}} - \frac {m g ^ {2} t _ {1} ^ {3}}{2 4}
$$

and verify that it is less than the action for the straight-line path of part (a).

Problem 4.14 Suppose the particle of the preceding problem moves instead at constant speed along an isoceles triangular path between the beginning point and the endpoint, with the high point at height $z _ { 1 }$ above the ground, at $x = x _ { 1 } / 2$ and $t = t _ { 1 } / 2$ . (a) Find the action for this path. (b) Find the altitude $z _ { 1 }$ corresponding to the least-action path among this class of constant-speed triangular paths. (c) Verify that the total action for this path is greater than that of the parabolic path of the preceding problem.

Problem 4.15 A plane pendulum consists of a light rod of length R supporting a plumb bob of mass m in a uniform gravitational field $g .$ . The point of support of the top end of the rod is forced to oscillate back and forth in the horizontal direction with $x = A$ cos ωt. Using the angle $\theta$ of the bob from the vertical as the generalized coordinate, (a) find the Lagrangian of the plumb bob. (b) Are there any conserved dynamical quantities? (c) Find the simplest differential equation of motion of the bob.

Problem 4.16 Solve the preceding problem if instead of being forced to oscillate in the horizontal direction, the upper end ofthe rod is forced to oscillate in the vertical direction with $y = A \cos \omega t .$

Problem 4.17 A particle of mass m on a frictionless tabletop is attached to one end of a light string. The other end of the string is threaded through a small hole in the tabletop, and held by a person under the table. If given a sideways velocity $\nu _ { 0 }$ , the particle circles the hole with radius $r _ { 0 }$ . At time $t = 0$ the mass reaches an angle defined to be $\theta = 0$ on the tabletop, and the person under the table pulls on the string so that the length of the string above the table becomes $r ( t ) = r _ { 0 } -$ αt for a period of time thereafter, where α is a constant. Using θ as the generalized coordinate of the particle, find its Lagrangian, identify any conserved quantities, find its simplest differential equation of motion, and get as far as you can using analytic means alone toward finding the solution $\theta ( t )$ (or $t ( \theta ) )$ .

Problem 4.18 A rod is bent in the middle by angle $\alpha .$ The bottom portion is kept vertical and the top portion is therefore oriented at angle α to the vertical. A bead of mass $m$ is slipped onto the top portion and the bottom portion is forced by a motor to rotate at constant angular speed $\omega$ about the vertical axis. (a) Define a generalized coordinate for the bead and write down the Lagrangian. (b) Identify any conserved quantity or quantities and explain why it (or they) are conserved. (c) Find the generalized momentum of the bead and the Hamiltonian. (d) Are there any equilibrium points of the bead? If so, are they stable or unstable?

Problem 4.19 A wire is bent into the shape of a cycloid, defined by the parametric equations $x = A ( \varphi + \sin \varphi )$ and $y = A ( 1 - \cos \varphi )$ , where $\varphi$ is the parameter $( - \pi < \varphi < \pi )$ , and $A$ is a constant. The wire is in a vertical plane, and is spun at constant angular velocity $\omega$ about a vertical axis through its center. A bead of mass m is slipped onto the wire. (a) Find the Lagrangian of the bead, using the parameter $\varphi$ as the generalized coordinate. (b) Identify any first integral of motion of the bead. (c) Reduce the problem to quadrature. That is, show that the time t can be expressed as an integral over $\varphi .$ .

Problem 4.20 Center of mass and relative coordinates. Show that for two particles moving in one dimension, with coordinates $x _ { 1 }$ and $x _ { 2 }$ , with a potential that depend only upon their separation $x _ { 2 } - x _ { 1 }$ , the Lagrangian

$$
L = \frac {1}{2} m _ {1} \dot {x} _ {1} ^ {2} + \frac {1}{2} m _ {2} \dot {x} _ {2} ^ {2} - U (x _ {2} - x _ {1})
$$

can be rewritten in the form

$$
L = \frac {1}{2} M \dot {X} ^ {2} + \frac {1}{2} \mu \dot {x} ^ {\prime 2} - U (x ^ {\prime}),
$$

where $M = m _ { 1 } + m _ { 2 }$ is the total mass and $\mu = m _ { 1 } m _ { 2 } / M$ is the “reduced mass” of the system, and $X = ( m _ { 1 } x _ { 1 } + m _ { 2 } x _ { 2 } ) / M$ is the center of mass coordinate and $x ^ { \prime } = x _ { 2 } - x _ { 1 }$ is the relative coordinate.

Problem 4.21 Two blocks of equal mass m, connected by a Hooke’s-law spring of unstretched length $\ell ,$ are free to move in one dimension. Find the equations of motion of the system, using the relative and center of mass coordinates introduced in the preceding problem.

Problem 4.22 A small block of mass m and a weight of mass M are connected by a string of length $D .$ . The string has been threaded through a small hole in a tabletop, so the block can slide without friction on the tabletop, while the weight hangs vertically beneath the tabletop. We can let the hole be the origin of coordinates, and use polar coordinates $r , \theta$ for the block, where r is the block’s distance from the hole, and z for the distance of the weight below the tabletop. (a) Using generalized coordinates r and $\theta ,$ , write down the Lagrangian of the system of block plus weight. (b) Write down a complete set of first integrals of the motion, explaining the physical meaning of each. (c) Show that the first integrals can be combined to give an equation of the form

$$
E = \frac {1}{2} (M + m) \dot {r} ^ {2} + U _ {\mathrm{eff}} (r)
$$

and write out an expression for $U _ { \mathrm { e f f } } ( r )$ . (d) Find the radius of a circular orbit of the block in terms of constants of motion. (e) Now suppose the block executes small oscillations about a circular orbit. What is the frequency of these oscillations? Is the resulting orbit of the block open or closed? That is, does the perturbed orbit of the block continually return to its former position or not?

Problem 4.23 Example 1.3 of Chapter 1 proposed that mined material on the moon might be projected off the moon’s surface by a rotating boom that slings the material into space. Assume the boom rotates in a horizontal plane with constant angular velocity $\omega ,$ , and let $r ,$ the distance of the payload from the rotation axis at one end of the boom, be the single generalized coordinate. (a) Find the Lagrangian for a bucket of material of mass m that moves along the boom. (b) Find its equation of motion. (c) Solve it for $r ( t )$ , subject to the initial conditions $r = r _ { 0 }$ and $\dot { \boldsymbol { r } } = 0$ at $t = 0$ . (d) If the boom has length R, find the radial and tangential components of the bucket’s velocity, and its total speed, as it emerges from the end of the boom. (e) Find the power input $P = d E / d t$ into a bucket of mass m as a function of time. Is the power input larger at the beginning or end of the bucket’s journey along the boom? (f) Find the torque exerted by the boom on the bucket, as a function of the position r of the bucket on the boom. There would be an equal but opposite torque back on the boom, caused by the bucket, which might break the boom. At what part of the bucket’s journey would this torque most likely break the boom? (g) If $R = 1 0 0$ m and $r _ { 0 } = 1$ m, what must be the rotational period of the boom so that buckets will reach the moon’s escape speed as they fly off the boom?

Problem 4.24 Consider a vertical circular hoop of radius R rotating about its vertical symmetry axis with constant angular velocity Ω. A bead of mass m is threaded onto the hoop, so is free to move along the hoop. Let the angle θ of the bead be measured up from the bottom of the hoop.

(a) Write the Lagrangian in terms of the generalized coordinate θ. Are there any first integrals of motion?

(b) Show that there are two equilibrium angles of the bead for sufficiently small angular velocities Ω, but that there are four equilibrium angles if Ω is sufficiently large.

(c) For each of these equilibrium angles, find out whether that position of the bead is stable or unstable. That is, ifthe bead is displaced slightly from equilibrium, does it tend to move back toward the equilibrium angle, or does it depart farther and farther from it?

Problem 4.25 In certain situations, it is possible to incorporate frictional effects in a simple way into a Lagrangian problem. As an example, consider the Lagrangian

$$
L = e ^ {\gamma t} \left(\frac {1}{2} m \dot {q} ^ {2} - \frac {1}{2} k q ^ {2}\right).
$$

(a) Find the equation of motion for the system.

(b) Do a coordinate change $s = e ^ { \gamma t / 2 } q$ . Rewrite the dynamics in terms of s.

(c) How would you describe the system?

Problem 4.26 Consider a particle moving in three dimensions with Lagrangian $L =$ $( 1 / 2 ) m ( \dot { x } ^ { 2 } + \dot { y } ^ { 2 } + \dot { z } ^ { 2 } ) + \dot { a } \dot { x } + b $ , where a and b are constants. (a) Find the equations of motion and show that the particle moves in a straight line at constant speed, so that it must be a free particle. (b) The result of (a) shows that there must be another reference frame $( x ^ { \prime } , y ^ { \prime } , z ^ { \prime } )$ such that the Lagrangian is just the usual freeparticle Lagrangian $L ^ { \prime } = \dot { ( 1 / 2 ) } m ( \dot { x } ^ { \prime 2 } + \dot { y } ^ { \prime 2 } + \dot { z } ^ { \prime 2 } )$ . However, $L ^ { \prime }$ may also be allowed an additive constant, which cannot show up in Lagrange’s equations. Find the Galilean transformation between $( x , y , z )$ and $( x ^ { \prime } , y ^ { \prime } , z ^ { \prime } )$ and find the velocity of the new primed frame in terms of a and b.

Problem 4.27 Consider a Lagrangian $L ^ { \prime } { = } L + d f / d t$ , where the Lagrangian is $L =$ $L ( q _ { k } , \dot { q } _ { k } , t )$ and the function $f = f ( q _ { k } , t )$ . (a) Show that $L ^ { \prime } = L ^ { \prime } ( q _ { k } , \dot { q } _ { k } , t )$ , so that it depends upon the proper variables. Show that this would not generally be true iff were allowed to depend upon the $\dot { q } _ { k } \mathbf { s } .$ . (b) Show that $L ^ { \prime }$ obeys Lagrange’s equations if $L$ does, by substituting $L ^ { \prime }$ into Lagrange’s equations. Therefore, the equations of motion are the same using $L ^ { \prime }$ as using $L ,$ so the Lagrangian of a particle is not unique. (This problem requires care in taking total and partial derivatives!)

Problem 4.28 Show that the function $L ^ { \prime }$ given in the preceding problem must obey Lagrange’s equations if $L$ does, directly from the principle of stationary action. Lagrange’s equations do not have to be written down for this proof!

Problem 4.29 Consider the Lagrangian $L ^ { \prime } = m \dot { x } \dot { y } - k x y$ for a particle free to move in two dimensions, where x and y are Cartesian coordinates, and m and $k$ are constants. (a) Show that this Lagrangian gives the equations of motion appropriate for a two-dimensional simple harmonic oscillator. Therefore, as far as the motion of the particle is concerned, $\bar { L ^ { \prime } }$ is equivalent to $L = ( 1 / 2 ) m ( \dot { x } ^ { 2 } + \dot { x } ^ { 2 } ) - ( 1 / 2 ) k ( x ^ { 2 } + y ^ { 2 } )$ (b) Show that $L ^ { \prime }$ and $L$ do not differ by the total time derivative of any function $f ( x , y )$ . Therefore, $L ^ { \prime }$ is not a member of the class of Lagrangians mentioned in the preceding problems, so there are even more Lagrangians describing a particle than suggested before.

Problem 4.30 Consider a Lagrangian that depends on second derivatives of the coordinates

$$
L = L (q _ {k}, \dot {q} _ {k}, \ddot {q} _ {k}, t).
$$

Through the variational principle, find the resulting differential equations of motion.

Problem 4.31 A pendulum consists of a plumb bob of mass m on the end of a string that swings back and forth in a plane. The upper end of the string passes through a small hole in the ceiling, and the angle $\theta$ of the bob relative to the vertical changes with time as it swings back and forth. The string is pulled upward at constant rate through the hole, so the length R of the pendulum decreases at a constant rate, with $d R / d t = - \alpha$ . (a) Find the Lagrangian of the bob, using $\theta$ as the generalized coordinate. (b) Find the Hamiltonian $H .$ Is H equal to the energy $E ?$ Why or why not? (c) Is either H or E conserved? Why or why not?

Problem 4.32 A spherical pendulum consists of a particle of mass m on the end of a string of length R. The position of the particle can be described by a polar angle θ and an azimuthal angle $\varphi .$ . The length of the string decreases at the rate $d R / d t =$ $- f ( t )$ , where $f ( t )$ is a positive function of time. (a) Find the Lagrangian of the particle, using θ and $\varphi$ as generalized coordinates. (b) Find the Hamiltonian $H .$ Is H equal to the energy? Why of why not? (c) Is either $E$ or H conserved? Why or why not?

Problem 4.33 The Hamiltonian of a bead on a parabolic wire turning with constant angular velocity ω is

$$
H = \frac {1}{2} m [ (1 + 4 \alpha^ {2} r ^ {2}) \dot {r} ^ {2} - r ^ {2} \omega^ {2} ] + m g \alpha r ^ {2},
$$

where H is a constant. Reduce the problem to quadrature: that is, find an equation for the time t is terms of an integral over r.

Problem 4.34 A bead of mass m is placed on a vertically oriented circular hoop of radius R that is forced to rotate with constant angular velocity $\omega$ about a vertical axis through its center. (a) Using the polar angle θ measured up from the bottom as the single generalized coordinate, find the kinetic and potential energies of the bead. (Remember that the bead has motion due to the forced rotation of the hoop as well as motion due to changing $\theta . )$ (b) Find the bead’s equation of motion using Lagrange’s equation. (c) Is its energy conserved? Why or why not? (d) Find its Hamiltonian. Is $H$ conserved? Why or why not? Is $E = H ?$ Why or why not? (e) Find the equilibrium angle $\theta _ { 0 }$ for the bead as a function of the hoop’s angular velocity $\omega .$ Sketch a graph of $\theta _ { 0 }$ vs. ω. Notice that there is a “phase transition” at a certain critical velocity $\omega _ { \mathrm { c r i t } }$ . (f) Find the frequency of small oscillations of the bead about the equilibrium angle $\theta _ { 0 }$ , as a function of ω.

Problem 4.35 A wire is bent into the shape of a quartic function $y = a x ^ { 4 }$ and oriented in a vertical plane, with x horizontal, y vertical, and a a positive constant. A bead of mass m is threaded onto the wire, and the wire is then forced to rotate with constant angular velocity $\Omega$ about the y axis. (a) Let x be the generalized coordinate for the bead and find its Lagrangian. (b) Is the bead’s energy conserved? Why or why not? (c) Is the bead’s angular momentum conserved about the vertical axis? Why or why not? (d) Find the bead’s Hamiltonian. Is H conserved? Why or why not? (e) Is $E = H ?$ Why or why not? (f) Given $\Omega > 0$ , are there any equilibrium positions of the bead? (g) If so, is each stable or unstable? For any stable equilibrium position, find the frequency $\omega$ of small oscillations about the equilibrium point, expressed as a multiple of Ω.

Problem 4.36 In Example 4.8 we analyzed the case of a bead on a rotating parabolic wire. The energy of the bead was not conserved, but the Hamiltonian was:

$$
H = \frac {1}{2} m (1 + 4 \alpha^ {2} r ^ {2}) \dot {r} ^ {2} + “ U _ {\mathrm{eff}} ” = \mathrm{constant},
$$

where

$$
U _ {\mathrm{eff}} = \frac {1}{2} m r ^ {2} (2 g \alpha^ {2} - \omega^ {2}).
$$

There is an equilibrium point at $r = 0$ which is unstable if ω $> \omega _ { 0 } \equiv \sqrt { 2 g } \alpha$ neutrally stable if $\omega ~ = ~ \omega _ { 0 }$ , and stable if $\omega \ < \ \omega _ { 0 }$ . Find the frequency of small oscillations about $r = 0$ if ω $< \omega _ { 0 }$

Problem 4.37 A wire bent in the shape of a hyperbolic cosine function $y =$ a cosh $\left( x / x _ { 0 } \right)$ is supported in a vertical plane, where x and y are the horizontal and vertical coordinates, respectively, and a and $x _ { 0 }$ are positive constants. A bead of mass m is threaded onto the wire and is free to slide without friction along it, and is subject to uniform gravity g directed downward. (a) Find Lagrange’s equations for the bead using x as the generalized coordinate, and (b) find the frequency of small oscillations of the bead about the lowest point of the wire.

Problem 4.38 The wire described in the preceding problem is now forced to rotate about its vertical axis of symmetry with constant angular velocity Ω. (a) Find $\Omega _ { c } .$ the critical value of Ω for which the equilibrium point at $x = 0$ is no longer a stable equilibrium point, and find the values of x for which there is then a stable equilibrium point for the bead. (b) Find the frequency of small oscillations of the bead about each of any new equilibrium points.

Problem 4.39 One point on a horizontal circular wire C of radius R is attached to a thin, vertical axle which turns at constant angular velocity Ω about the vertical axis, causing C to turn around with it. A bead of mass m moves without friction on C. (a) Show that relative to C the bead oscillates like a pendulum. (b) Find the frequency of small-amplitude oscillations of the bead in terms of any or all of R, Ω, and m.

Problem 4.40 A frictionless slide is constructed in the shape of a cycloid. The horizontal coordinate x and vertical coordinate y ofthe slide are given in parametric form by

$$
x = A (\varphi + \sin \varphi) \quad y = A (1 - \cos \varphi),
$$

where A is a constant. Here the y coordinate is positive upward. The slide i the portion of the cycloid with $= - \pi \leq \varphi \leq \pi$ , with the bottom of the slide corresponding to $\varphi = 0$ . There is a uniform gravitational field g in the negative y direction. (a) Find the Lagrangian of a small block of mass m moving along the slide, using $\varphi$ as the generalized coordinate. (b) The block will oscillate back and forth near the bottom ofthe slide. Is its motion simple harmonic in the limit ofsmall amplitudes? If not, explain why not; if so, find the angular frequency of oscillation ω in terms of any or all ofA, m, and g.

Problem 4.41 A mass $M _ { 1 }$ is hung on an unstretchable string A, and the other end of string A is passed over a fixed, frictionless, nonrotating pulley $P _ { 1 }$ , as shown in Prob. 4.41. This other end of string A is then attached to the center of a second frictionless, nonrotating pulley $P _ { 2 }$ of mass M<sub>2</sub>, over which is passed a second nonstretchable string B, one end of which is attached to a hanging mass $m _ { 1 }$ while the other end is attached to a hanging mass $m _ { 2 }$ . Let $X _ { 1 } ( t )$ be the length of string A beneath the center of pulley $P _ { 1 } ; X _ { 2 } ( t )$ be the length of string A beneath the center of $P _ { 1 } ; x _ { 1 } ( t )$ be the length of string B beneath the center of pulley $P _ { 2 } { \mathrm { ; } }$ ; and $x _ { 2 } ( t )$ be the length of string B beneath the center of pulley $P _ { 2 }$ . There is a uniform gravity g downward. (a) Find the total kinetic energy of the system, in terms of $X _ { 1 } , x _ { 1 }$ and the various masses. (b) Find the total potential energy of the system, measured

![](images/6ba9d8912a6d32ba32a70f01ec52d5af6bfe55238989bd19efa88d2855927843.jpg)

Prob. 4.41 Three masses and two pulleys.

from the center of fixed pulley $P _ { 1 }$ . (c) Find the Lagrangian of the system. (d) Find the acceleration of mass $M _ { 1 }$ in terms of given quantities.

 Problem 4.42 Consider a Lagrangian of the form

$$
L = m c ^ {2} \left(1 - \sqrt {1 - v ^ {2} / c ^ {2}}\right) - U (x, y, z).
$$

Show that the resulting Lagrange equations give Newton $\mathrm { ^ \circ s }$ second law $\mathbf { F } = d \mathbf { p } / d t$ for a relativistic particle, if $F ^ { i } = - \partial U / \partial x ^ { i }$