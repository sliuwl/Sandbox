# Constraints and Symmetries

An enormous advantage of using Lagrangian methods in mechanics is the simpli fications that can occur when a system is constrained or if there are symmetries of some kind in the environment of the system. Constraints can be used to reduce the number of generalized coordinates so that solutions become more practicable. In this chapter we will illustrate this fact using the example of contact forces, and we will demonstrate the use of Lagrange multipliers to learn about the contact forces themselves.

Constraints are also typically associated with the breaking of symmetries. Lagrangian mechanics allows us to efficiently explore the relationship between symmetries in a physical situation and dynamical quantities that are conserved. These properties are nicely summarized in a theorem by the German mathematician Emmy Noether (1882–1935), and provide us with deep insight into the physics – in addition to helping us make important technical simplifications while solving problems.

We first discuss constraints and contact forces, and then symmetries and conservation laws.

## 6.1 Contact Forces

A square block of mass M rests on a horizontal floor, as shown in Figure 6.1. Newtonian mechanics tells us that the block experiences two forces: the downward pull of gravity Mg and the upward push of the floor, called the normal force N. A static scenario implies that $N = M g$ , so the forces sum to zero and there is no acceleration. Hence, the normal force adjusts its strength as needed to counteract the gravitational pull Mg. If the balance succeeds, the block stays put on the floor. If, however, the normal push of the floor is not enough because the block is too heavy, the floor would disintegrate and the block would fall through.

The normal force is an example of a contact force. It arises by virtue of the physical contact between two objects. Contact forces are always electromagnetic in origin. As two objects touch, the atoms at the contact interface push against one another through electromagnetic forces. Each of these tiny pushes may be negligible, but with $1 0 ^ { 2 3 }$ atoms reinforcing the effect, we get a net, effective, macroscopic force we call the contact force. Hence, contact forces are not fundamental: they are the sum of many complicated microscopic interactions. However, we can often characterize them by a simple, effective, phenomenological force “law.” The normal force, the tension force, and the friction force are all examples. They really consist of intricate electromagnetic interactions between large numbers of constituent atoms.

![](images/116882b081940fad0cacd5ee2c912a441142af9797502a16d86a612c75c0046f.jpg)  
Fig. 6.1 (a) A block resting on the ground subject to the normal contact force that constrains it to horizonta motion. (b) A bob pendulum involves the tension contact force in the rope that constrains the bob from flying away.

Our square block rests on the floor. The net effect of the contact force is to constrain its vertical motion: the block can move only sideways and not up and down. The dynamics ofthe center ofmass ofthe box is now reduced to two degrees of freedom from the original three. Similarly, the tension force in the rope of a bob pendulum implements a constraint that assures that the bob at the end of the rope does not fly way beyond a distance equal to the length ofthe rope. Many more such contact forces translate into statements of constraints on the degrees of freedom. In this section, we develop the technology of solving mechanics problems with various types of constraints.

Consider a mechanical system parameterized by N coordinates $q _ { k } , k = 1 , \ldots , N .$ However, due to some constraint forces, there are P algebraic relations amongst these coordinates, given by

$$
C _ {l} (q _ {1}, q _ {2}, \dots , q _ {N}, t) = 0,\tag{6.1}
$$

where $l = 1 , \ldots , P .$ . This means we have effectively $N - P$ generalized coordinates or degrees of freedom, instead of the nominal N. In our problem of the block on the floor, for example, let us suppose that the floor is at $z = 0$ . Then we can define $C = z ,$ , so that the single algebraic equation $C = 0$ implies that $z = 0$ . We started with $N = 3$ coordinates $x , y , z ;$ then we specified $P = 1$ constraint, the constraint that $z = 0$ , where z is the vertical direction and the center of mass of the block rests at $z = 0$ . We are then left with $N - P = 3 - 1 = 2$ degrees of freedom, x and y.

In tackling such situations with constraints, we have two choices. We could try to use the P relations (6.1) to eliminate P of the $q _ { k } \mathbf { S } ,$ , and write the Lagrangian in terms of $N - P$ generalized coordinates. This is in a sense what we have been doing so far. For the example of the block, we would write

$$
L = \frac {1}{2} m (\dot {x} ^ {2} + \dot {y} ^ {2} + \dot {z} ^ {2}) - m g z = \frac {1}{2} m (\dot {x} ^ {2} + \dot {y} ^ {2}).\tag{6.2}
$$

Alternatively, we may want to delay implementing the constraint. There are two good reasons for this. First, it may be difficult or inconvenient to eliminate $P \ q _ { k } \mathbf { s }$ using the constraints (6.1). Second, we may be interested in finding the constraint forces underlying these constraint relations. For example, we may want to find the normal force on a block sliding along a curved rail; when this force vanishes, the block is losing contact with the rail, and we would be able to determine this critical point in the evolution.

Therefore we now focus on a method that delays the implementation of the constraints in a mechanical problem, instead dealing with all $N ~ q _ { k } \mathbf { s }$ in the problem. This requires a careful treatment, since the variational formalism assumes independent $q _ { k } \mathbf { S }$ : the $q _ { k } \mathbf { S }$ must not have relations amongst them such as those given by (6.1). Otherwise, in the process of extremizing the action we would get to the step

$$
\delta I = \int \left[ \frac {d}{d t} \left(- \frac {\partial L}{\partial \dot {q} _ {k}}\right) + \frac {\partial L}{\partial q _ {k}} \right] \delta q _ {k} d t = 0,\tag{6.3}
$$

and, since the $\delta q _ { k } \mathbf { s }$ are not independent due to (6.1), we cannot conclude that the vanishing of the bracketed expression – that is the Lagrange equations of motion – is necessary individually for every $k .$ .

Instead, let us consider a new Lagrangian defined as

$$
L ^ {\prime} = L + \sum_ {l = 1} ^ {P} \lambda_ {l} C _ {l},\tag{6.4}
$$

where we have introduced P additional degrees of freedom labeled $\lambda _ { l }$ with $l =$ $1 , \ldots , P ,$ each multiplying a related constraint equation from (6.1). For example, with the block on a horizontal floor, we would write

$$
L ^ {\prime} = \frac {1}{2} m (\dot {x} ^ {2} + \dot {y} ^ {2} + \dot {z} ^ {2}) - m g z + \lambda_ {1} z.\tag{6.5}
$$

We now assume that the constraint equations (6.1) are not satisfied a priori. We then have $N + P$ degrees of freedom: $N q _ { k } \mathbf { s }$ and $P \ \lambda _ { l } \mathbf { s }$ . Correspondingly, we have $N { \mathrel { + { \cal P } } }$ equations of motion. For our example, we have $N + P = 3 + 1 = 4$ variables remaining: x, y, z, and $\lambda _ { 1 }$

The equations of motion for (6.4) are then

• $P$ equations for the $\lambda _ { l } \mathbf { s }$ :

$$
\frac {d}{d t} \left(\frac {\partial L ^ {\prime}}{\partial \dot {\lambda} _ {l}}\right) - \frac {\partial L ^ {\prime}}{\partial \lambda_ {l}} = z = 0 \Rightarrow \frac {\partial L ^ {\prime}}{\partial \lambda_ {l}} = 0 \Rightarrow C _ {l} = 0.\tag{6.6}
$$

These are simply the original constraints (6.1)! But they now arise dynamically through the equations of motion and need not be implemented from the outset. The $P$ parameters labeled $\lambda _ { l }$ are called Lagrange multipliers. For our simple example, we have a single Lagrange multiplier $\lambda _ { 1 }$ with the equation of motion $z = 0$

• N equations for the $q _ { k } \mathbf { S } \mathbf { \dot { \mathbf { \ell } } }$ :

$$
\frac {d}{d t} \left(\frac {\partial L ^ {\prime}}{\partial \dot {q} _ {k}}\right) - \frac {\partial L ^ {\prime}}{\partial q _ {k}} = 0.\tag{6.7}
$$

In terms of the original L from (6.4), these look like

$$
\frac {d}{d t} \left(\frac {\partial L}{\partial \dot {q} _ {k}}\right) - \frac {\partial L}{\partial q _ {k}} - \lambda_ {l} \frac {\partial C _ {l}}{\partial q _ {k}} = 0.\tag{6.8}
$$

Note the additional terms involving the $\lambda _ { l } \mathbf { s }$ (l is repeated and hence summed over). We can rewrite these as

$$
\frac {d}{d t} \left(\frac {\partial L}{\partial \dot {q} _ {k}}\right) - \frac {\partial L}{\partial q _ {k}} = \mathcal {F} _ {k} \equiv \lambda_ {l} \frac {\partial C _ {l}}{\partial q _ {k}},\tag{6.9}
$$

where we have defined the generalized constraint forces $\mathcal { F } _ { k }$ that essentially enforce the constraints onto the $q _ { k }$ dynamics. For the block on the horizontal floor problem these become

$$
m \ddot {x} = 0, m \ddot {y} = 0, m \ddot {z} = - m g + \lambda_ {1}.\tag{6.10}
$$

In this case it is obvious that $\lambda _ { 1 }$ is the normal force. More generally, how do we relate the generalized constraint forces – and hence the λs – to the actual forces? For every object i in the problem located at position $\mathbf { r } _ { i } ,$ , denote the total constraint force acting on it by $\mathbf { F } _ { i }$ . We also know the relations $\mathbf { r } _ { i } ( q _ { k } , t )$ that connect the position of every object to the generalized coordinates $q _ { k }$ . Using all this, we can relate the Lagrange multipliers to the constraint forces by noting that the righthand side of the new Lagrange equations must be given by

$$
\mathcal {F} _ {k} = \lambda_ {l} \frac {\partial C _ {l}}{\partial q _ {k}} = \frac {\partial (\lambda_ {l} C _ {l})}{\partial q _ {k}}.\tag{6.11}
$$

Since $\lambda _ { l } C _ { l }$ is added to the Lagrangian, it should correspond to the energy or work associated with the constraint forces $\mathbf { F } _ { i } ^ { \mathrm { c } }$ :

$$
\lambda_ {l} C _ {l} = \int^ {\mathbf {r} _ {i}} \mathbf {F} _ {i} ^ {\mathbf {c}} \cdot d \mathbf {r} _ {i} ^ {\prime},\tag{6.12}
$$

where i sums over the various entities tracked by the Lagrangian with corresponding position vectors $\mathbf { r } _ { i } .$ . The prime on the measure $d \mathbf { r } _ { i } ^ { \prime }$ is to avoid a variable naming clash with the limit of the integral. Notice that if a force on a particle $\mathbf { F } _ { i } ^ { \mathrm { c } }$ were conservative and if we were to write it in terms of a potential energy $\mathbf { F } _ { i } ^ { \mathrm { { c } } } ~ = ~ - \nabla U _ { \mathrm { c } }$ , this would correspond to adding ${ - } U _ { C } ( \mathbf { r } _ { i } )$ to the Lagrangian as expected. Since we have a map between these position vectors and the generalized coordinates $\mathbf { r } _ { i } ( q _ { k } , t )$ , we can write

$$
\lambda_ {l} C _ {l} = \int^ {\mathbf {r} _ {i}} \mathbf {F} _ {i} ^ {\mathbf {c}} \cdot d \mathbf {r} _ {i} ^ {\prime} = \int^ {q _ {k}} \mathbf {F} _ {i} ^ {\mathbf {c}} \cdot \frac {\partial \mathbf {r} _ {i} ^ {\prime}}{\partial q _ {k} ^ {\prime}} d q _ {k} ^ {\prime},\tag{6.13}
$$

where we used the chain rule and the fact that $d t = 0$ , since the expression added to the Lagrangian should be evaluated at a fixed time. We then have

$$
\mathcal {F} _ {k} = \lambda_ {l} \frac {\partial C _ {l}}{\partial q _ {k}} = \frac {\partial (\lambda_ {l} C _ {l})}{\partial q _ {k}} = \mathbf {F} _ {i} ^ {\mathbf {c}} \cdot \frac {\partial \mathbf {r} _ {i}}{\partial q _ {k}}.\tag{6.14}
$$

Once we determine the Lagrange multipliers $\lambda _ { l } ,$ we can use this relation to read off constraint forces $\mathbf { F } _ { i } ^ { \mathrm { c } }$ . For the example at hand, we have

$$
\lambda_ {1} = \mathbf {F} ^ {\mathbf {c}} \cdot \frac {\partial \mathbf {r}}{\partial z} = F _ {z} ^ {\mathbf {c}} = N.\tag{6.15}
$$

Hence $\lambda _ { 1 }$ is the normal force, as expected.

Before we apply this general and abstract treatment to particular examples, we note that the method of constraints can easily be generalized a bit further. Looking back at Eq. (6.3), we see that we only need the constraint to be in the form of a variation. That is, we only need to add the constraint in the infinitesimal change of the action or Lagrangian, not the Lagrangian itself as we did in Eq. (6.4). We write instead

$$
\delta I = \int \left(\frac {d}{d t} \left(- \frac {\partial L}{\partial \dot {q} _ {k}}\right) + \frac {\partial L}{\partial q _ {k}} + \lambda_ {l} a _ {l k}\right) \delta q _ {k} d t = 0,\tag{6.16}
$$

for some functions $a _ { l k }$ of $q _ { k }$ and t. That is, if the constraints on the generalized coordinates $q _ { k }$ can be written in the form

$$
a _ {l k} \delta q _ {k} + a _ {l t} \delta t = 0,\tag{6.17}
$$

where $a _ { l k }$ and $a _ { l t }$ are arbitrary functions of $q _ { k }$ and t, we can write the following set of $N + P$ equations of motion:

$$
\frac {d}{d t} \left(\frac {\partial L}{\partial \dot {q} _ {k}}\right) - \frac {\partial L}{\partial q _ {k}} = \lambda_ {l} a _ {l k} = \mathcal {F} _ {k},\tag{6.18}
$$

$$
a _ {l k} \dot {q} _ {k} + a _ {l t} = 0.\tag{6.19}
$$

This is a useful generalization of the original formulation of the problem given by Eq. (6.6) and (6.9) because in a particular case perhaps

$$
\frac {\partial a _ {l k}}{\partial t} \neq \frac {\partial a _ {l t}}{\partial q _ {k}}.\tag{6.20}
$$

To see the further reach ofthis approach, note that ifthe constraints could be written as before in terms of P algebraic relations $C _ { l } ( t , q ) = 0$ , we could write

$$
0 = d C _ {l} = \frac {\partial C _ {l}}{\partial q _ {k}} d q _ {k} + \frac {\partial C _ {l}}{\partial t} d t = a _ {l k} d q _ {k} + a _ {l t} d t,\tag{6.21}
$$

reading off the needed $a _ { l k }$ and $a _ { l t }$ as functions of $q _ { k }$ and t. However, in this special class of constraints, we would have

$$
\frac {\partial a _ {l k}}{\partial t} = \frac {\partial a _ {l t}}{\partial q _ {k}}\tag{6.22}
$$

because of the commutativity of derivatives $\partial ^ { 2 } C _ { l } / \partial q _ { k } \partial t = \partial ^ { 2 } C _ { l } / \partial t \partial q _ { k }$ . For the example at hand, we would write

$$
d z = 0 \Rightarrow a _ {1 z} = 1, a _ {1 t} = 0,\tag{6.23}
$$

with Eq. (6.22) satisfied as expected. Algebraic constraints of the form $C _ { l } ( q , t ) = 0$ are called holonomic constraints, already discussed briefly in Chapter 4. The type of constraints that cannot be expressed in this form but instead can be written in variational form (6.17) are nonholonomic constraints. In either case, Eqs. (6.18) and (6.19) give us a powerful recipe for investigating the problem of constraints.

In summary, when dealing with a mechanics problem involving constraints of the form (6.17), we may choose to delay the implementation of the constraints in an effort to extract any constraint forces acting on the system. To do so we would need to solve a set of $N + P$ differential equations given by (6.18) and (6.19). In addition to finding $q _ { k } ( t )$ , this procedure also leads to P Lagrange multipliers that can be related to constraint forces through Eq. (6.14). Once again, the best way to learn this technology is through examples.

<table><tr><td>Example 6.1</td><td>Rolling Down the Plane</td></tr><tr><td></td><td><img src="images/b3b79b2f358dec169bb4e17cd46e55c7e7c4be92e069429336656be13e170807.jpg"/></td></tr><tr><td>Fig. 6.2</td><td>A hoop rolling down an inclined plane without slipping.Consider a hoop of radius R and mass M rolling down an inclined plane, as shown in Figure 6.2. To describe the hoop, we may prescribe three variables: a center of mass position in two dimensions r, and a rotational angle θ:r = xx̂ + yŷ, θ, (6.24)</td></tr></table>

where the coordinate system is set up tilted, as shown in the figure. However, we know of two potential constraints. First, the hoop is prevented from falling through the incline because of the normal force. This contact force enforces the constraint

$$
y = R \Rightarrow d y = 0.\tag{6.25}
$$

Furthermore, if there is friction involved, the hoop may roll down without slipping. This rolling without slipping condition amounts to the constraint

$$
d x = R d \theta .\tag{6.26}
$$

At the end of the day, these two constraints suggest that the problem involves only $3 - 2 = 1$ degree of freedom, not three. The kinetic energy is

$$
T = \frac {1}{2} M (\dot {x} ^ {2} + \dot {y} ^ {2}) + \frac {1}{2} M R ^ {2} \dot {\theta} ^ {2}\tag{6.27}
$$

while the potential energy can be written as (dropping constant shifts)

$$
U = - M g x \sin \varphi ,\tag{6.28}
$$

where $\varphi$ is the tilt of the incline. We may then proceed as usual by implementing the constraints (6.25) and (6.26) from the outset. We arrive at the Lagrangian with a single degree offreedom, which we may choose to be the x coordinate, so

$$
L = T - U = M \dot {x} ^ {2} + M g x \sin \varphi .\tag{6.29}
$$

The equation of motion then tells us the acceleration down the incline:

$$
\ddot {x} = \frac {g}{2} \sin \varphi .\tag{6.30}
$$

But what if we are interested in knowing the friction force, although we still do not care at all about the normal force? This means we will implement the normal force constraint given by (6.25) from the outset, eliminating the y coordinate, but we will delay implementing the frictional constraint given by (6.26). This leaves us with two of the original coordinates, x and $\theta ,$ and a new third degree of freedom, $\lambda _ { 1 } ,$ a Lagrange multiplier that we can use to find the friction force. We then need three diferential equations. Looking back at (6.26) and mapping it onto the general form (6.19), we read of

$$
a _ {1 \theta} = R, a _ {1 x} = - 1, a _ {1 t} = 0.\tag{6.31}
$$

We then write the Lagrangian in terms ofx and θ only:

$$
L = \frac {1}{2} m \dot {x} ^ {2} + \frac {1}{2} M R ^ {2} \dot {\theta} ^ {2} + M g x \sin \varphi\tag{6.32}
$$

and use the modified equations of motion given by (6.18). This gives for the x direction

$$
M \ddot {x} - M g \sin \varphi = - \lambda_ {1} = \mathcal {F} _ {x}\tag{6.33}
$$

and for the θ direction

$$
M R ^ {2} \ddot {\theta} = \lambda_ {1} R = \mathcal {F} _ {\theta}.\tag{6.34}
$$

We now have a set of three diferential equations, given by (6.33), (6.34), and

$$
R \dot {\theta} = \dot {x},\tag{6.35}
$$

which follows from the constraint (6.26). Solving this system of equations, we get

$$
\ddot {x} = \frac {g}{2} \sin \varphi , \lambda_ {1} = \frac {M g}{2} \sin \varphi .\tag{6.36}
$$

The novelty, of course, is the determination of $\lambda _ { 1 }$ , which we can now relate to the friction force through

$$
\mathcal {F} _ {\theta} = \lambda_ {1} R = \frac {M g R}{2} \sin \varphi = \mathbf {F} \cdot \frac {\partial \mathbf {r}}{\partial \theta} = \mathbf {F} \cdot \frac {\partial x}{\partial \theta} \hat {\mathbf {x}} = \mathbf {F} \cdot \frac {\partial (R \theta)}{\partial \theta} \hat {\mathbf {x}} = F _ {x} R = \tau .\tag{6.37}
$$

Tha ${ \mathrm { i } } \mathsf { s } ,$ the friction force (Mg sin $\varphi ) / 2$ supplies a torque equal to $( M g R$ sin $\varphi ) / 2$ . The method ofLagrangian multipliers has allowed us to selectively extract forces of constraint in a mechanical problem – without abandoning the elegant and powerful machinery of the Lagrangian formalism.

![](images/1b793e5a7beb04372e81b227cb9e9b0f8bf6b74e4a32b1d974f5e45d7a12e02e.jpg)

Two barrels stacked, one on top of the other. The lower barrel is stationary, while the upper one rolls down without slipping.

Consider the problem of two cylindrical barrels, one on top of the other, as shown in Figure 6.3. The bottom barrel is fixed in position and orientation, but the top one, of mass $m ,$ is free to move. It starts rolling down from its initial position at the top, rolling without slipping due to friction between the barrels. The problem is to find the point along the lower barrel where the top barrel loses contact with it. That is, we need to find the moment when the normal force acting on the top barrel vanishes.

We are tracking the motion of the top barrel. Hence, we have a priori three variables to keep track of, two positions r and $\theta ,$ and one rotational angle $\varphi \mathrm { : }$

$$
\mathbf {r} = r \hat {\mathbf {r}}, \varphi ,\tag{6.38}
$$

where we use polar coordinates centered on the bottom barrel to track the position of the top barrel. A normal force acting on the top barrel enforces the constraint

$$
r = R + a.\tag{6.39}
$$

If the top barrel rolls without slipping, the friction force enforces an additional constraint

$$
a d \varphi = R d \theta .\tag{6.40}
$$

The full kinetic energy in terms of $r , \theta , \varphi$ is

$$
T = \frac {1}{2} m \left(\dot {r} ^ {2} + r ^ {2} \dot {\theta} ^ {2}\right) + \frac {1}{2} m a ^ {2} \dot {\varphi} ^ {2}\tag{6.41}
$$

and the potential energy is

$$
U = m g r \cos \theta .\tag{6.42}
$$

Note that we included the rotational kinetic energy of the top, hoop-like barrel (whose endcaps have negligible mass), given by $\scriptstyle { \frac { 1 } { 2 } } m a ^ { 2 } { \dot { \varphi } } ^ { 2 }$ . Since we are only interested in the normal force, we implement the frictional constraint (6.40) from the outset to eliminate $\varphi$ in favor of θ. We then get

$$
L = T - U = \frac {1}{2} m (\dot {r} ^ {2} + r ^ {2} \dot {\theta} ^ {2}) + \frac {1}{2} m R ^ {2} \dot {\theta} ^ {2} - m g r \cos \theta .\tag{6.43}
$$

We do not implement the normal force constraint (6.39), which we now write in the canonical form (6.17):

$$
d r = 0.\tag{6.44}
$$

This means we will have three degrees of freedom: $r , \theta ,$ and a Lagrange multiplier $\lambda _ { 1 }$ associated with constraint (6.39). We can now read of the relevant coeficients of (6.19):

$$
a _ {1 r} = 1, \quad a _ {1 \theta} = a _ {1 t} = 0.\tag{6.45}
$$

The equations of motion follow from (6.18). For the r direction:

$$
m \ddot {r} - m r \dot {\theta} ^ {2} + m g \cos \theta = \lambda_ {1} = \mathcal {F} _ {r} = \mathbf {F} \cdot \frac {\partial \mathbf {r}}{\partial r} = F _ {r} = N\tag{6.46}
$$

while for the θ direction:

$$
m r ^ {2} \ddot {\theta} + m R ^ {2} \ddot {\theta} - m g r \sin \theta = 0.\tag{6.47}
$$

The third and final equation follows from the constraint (6.39), which we now write as

$$
\dot {r} = 0.\tag{6.48}
$$

We may now proceed to solve this set of three diferential equations. It is more elegant, however, to realize that energy is conserved in this problem (since all forces acting are conservative), so we can write

$$
E = T + U = \frac {1}{2} m \left((R + a) ^ {2} \dot {\theta} ^ {2}\right) + \frac {1}{2} m R ^ {2} \dot {\theta} ^ {2} + m g (R + a) \cos \theta\tag{6.49}
$$

with $r = R + a$ from the constraint and where E is a constant. Arranging for the initial conditions $\theta ( 0 ) = 0$ and $\dot { \theta } ( 0 ) = 0 .$ , we have ${ \cal E } = m g \left( R + a \right)$ . This implies

$$
\dot {\theta} ^ {2} = \frac {2 g (R + a)}{2 R ^ {2} + a ^ {2} + 2 R a} (1 - \cos \theta).\tag{6.50}
$$

From Eq. (6.46), we have

$$
- m (R + a) \dot {\theta} ^ {2} + m g \cos \theta = \lambda_ {1} = N.\tag{6.51}
$$

And setting $N = 0$ at the moment when the top barrel loses contact with the bottom one, we find

$$
\dot {\theta} _ {c} ^ {2} = \frac {g \cos \theta_ {c}}{R + a},\tag{6.52}
$$

where $\theta _ { c }$ denotes the critical angle at which this condition is satisfied. Using Eq. (6.50), we find

$$
\cos \theta_ {c} = \frac {2}{3 + R ^ {2} / (R + a) ^ {2}}.\tag{6.53}
$$

There are two interesting limiting cases. If the top barrel is tiny, we have $a / R \ll 1$ , which leads to

$$
\cos \theta_ {c} = \frac {1}{2}.\tag{6.54}
$$

In contrast, taking the opposite regime $a / R \gg 1$ , one finds

$$
\cos \theta_ {c} = \frac {2}{3}.\tag{6.55}
$$

## Example 6.3

## On the Rope

A classic problem is that of a bob pendulum consisting of a point mass m at the end of a rope of length l swinging in a plane (see Figure 6.4). We would like to determine the tension in the rope as a function of the angle θ. We start with two variables

$$
\mathbf {r} = r \hat {\mathbf {r}}\tag{6.56}
$$

using a polar coordinate system centered at the pivot, as shown in the figure. Hence, our variables are r and θ. However, we have a constraint enforced by the tension in the rope:

$$
r = I \Rightarrow d r = 0 \Rightarrow a _ {1 r} = 1, a _ {1 t} = 0,\tag{6.57}
$$

which we immediately use to read of the relevant coeficients for (6.19). The kinetic energy is

![](images/7347c728d8d83742edba2e9a8dd6f05e20528ae13669025e44bd838f336fdb03.jpg)  
A bob pendulum with one constraint given by the finite length of the rope.

$$
T = \frac {1}{2} m \left(\dot {r} ^ {2} + r ^ {2} \dot {\theta} ^ {2}\right)\tag{6.58}
$$

while the potential energy is simply

$$
U = - m g r \cos \theta .\tag{6.59}
$$

The Lagrangian becomes

$$
L = T - U = \frac {1}{2} m (\dot {r} ^ {2} + r ^ {2} \dot {\theta} ^ {2}) + m g r \cos \theta ,\tag{6.60}
$$

where we keep track of both r and $\theta$ as independent degrees of freedom at the cost of introducing one Lagrange multiplier $\lambda _ { 1 }$ associated with the constraint. The equation of motion for r comes from (6.18):

$$
m \ddot {r} + m r \dot {\theta} ^ {2} - m g \cos \theta = \lambda_ {1} = \mathbf {F} \cdot \frac {\partial \mathbf {r}}{\partial r} = F _ {r} = T,\tag{6.61}
$$

while that for $\theta$ is

$$
\frac {d}{d t} \left(m r ^ {2} \dot {\theta}\right) + m g r \sin \theta = 0.\tag{6.62}
$$

Our three degrees of freedom are associated with three diferential equations, and the third comes of course from the constraint (6.57), which we now write as

$$
\dot {r} = 0.\tag{6.63}
$$

This is enough to determine all three variables of interest. Once again, however, it is easier to use energy conservation:

$$
E = T + U = \frac {1}{2} m l ^ {2} \dot {\theta} ^ {2} - m g l \cos \theta .\tag{6.64}
$$

We start with initial conditions given by

$$
\theta (0) = \theta_ {0}, \dot {\theta} (0) = 0 \Rightarrow E = - m g I \cos \theta_ {0}.\tag{6.65}
$$

We then have

$$
\dot {\theta} ^ {2} = \frac {2 g}{I} (\cos \theta - \cos \theta_ {0}).\tag{6.66}
$$

This allows us to find the Lagrange multiplier $\lambda _ { 1 }$ in terms of θ:

$$
\lambda_ {1} = - m g \cos \theta + 2 m g (\cos \theta - \cos \theta_ {0}) = - m g (\cos \theta - 2 \cos \theta_ {0}) = T,\tag{6.67}
$$

which is the tension in the rope.

## Example 6.4

## A Rubber Wheel on a Road

A wheel of radius R rolls on a two-dimensional surface without slipping. If the wheel cannot skid in any direction, we have an interesting problem containing constraints. Assuming that the wheel does not tip over, we can describe its state by specifying the coordinatesx,y on the plane, the orientation angle θ measured from the x axis, and the roll angle $\varphi - \mathsf { a } \mathsf { s }$ shown in Figure 6.5. Because of the rolling without slipping condition, the roll angle can be related to x and y and hence can be eliminated from the outset:

$$
R ^ {2} d \varphi^ {2} = d x ^ {2} + d y ^ {2}.\tag{6.68}
$$

![](images/53fe608cf553213af6019e28885a85a1ae783cb978876825c70811ecc258dc19.jpg)

## Fig. 6.5

The coordinates used to describe the rolling rubber wheel.

Furthermore, the wheel cannot move sideways, although it can make gradual turns. So there is indeed another constraint in the problem. How can we quantify it? If we write the vector perpendicular to the wheel a $\pmb { \ k } =$ (sin $\theta , - \cos \theta )$ ), we want to say that the velocity of the wheel is always perpendicular to k:

$$
\mathbf {k} \cdot (\dot {x}, \dot {y}) = 0 \Rightarrow \dot {x} \sin \theta - \dot {y} \cos \theta = 0.\tag{6.69}
$$

Hence, we start with four variables minus two constraints, and end up with two degrees of freedom. The orientation angle θ is a freedom we could actually take control of by steering the wheel by some external mechanical method. This would amount to imposing a third constraint. For example, if we externally lock the orientation so that $\dot { \theta } = 0 ,$ , Eq. (6.69) can be integrated and we have an algebraic relation between x and y. With such a holonomic constraint, the problem now involves only a single degree of freedom: θ is fixed to a constant, while x and y are related to each other algebraically; the wheel rolls in a straight line along a single direction.

Suppose however we steer the wheel in pursuit ofa moving target! Say we aim the wheel toward a running person, with the wheel’s orientation thus determined by the line joining its position and the position of the runner. This implies that θ is not constant, but instead is generally given by a function ofx,y, and t: $\theta ( x , y , t )$ In general, Eq. (6.69) becomes non-integrable, so we have a nonholonomic constraint. As seen in our general treatment earlier, however, we can still handle this problem since our new constraint is in the form (6.17). We write the Lagrangian of the wheel as the sum of its rotational and translational kinetic energies; and we then use Eqs. (6.18) and (6.19). We leave the treatment as a problem for the reader.

## 6.2 Symmetries and Conservation Laws: A Preview

At a very fundamental level, physics is about identifying patterns in Nature. The field arguably begins with Tycho Brahe (1546–1601) – the first modern experimen tal physicist<sup>1</sup> – and Johannes Kepler (1571–1630) – the first modern theoretical physicist. In the sixteenth century, Brahe painstakingly accrued huge quantities of astronomical data about the location of planets and stars with unprecedented accuracy – using impressive observing instruments that he had designed and set up in his castle. Kepler pondered for years over Brahe’s long tables until he could finally identify patterns underlying planetary dynamics, summarized in what we now call Kepler’s three laws. Later on, Isaac Newton (1643–1727) referred to these achievements, among others, in his famous quote: “IfI have seenfurther it is only by standing on the shoulders ofgiants.”

Ever since, physics has always been about identifying patterns in numbers, in measurements. And a pattern is simply an indication of a repeating rule, a constant attribute within seeming complexity, an underlying symmetry. In 1918, Emmy Noether published a seminal work that clarified the deep relations between symmetries and conserved quantities in Nature. In a sense, this work organizes physics into a clear diagram that gives us a bird’s eye view of the myriad of branches of the field. Noether’s theorem, as it is called, can change the way one thinks about physics in general. It is simple yet profound.

While one can study Noether’s theorem in the context of Newton’s formulation of mechanics, the methods in that case are quite cumbersome. Studying Noether’s theorem using Lagrangian mechanics instead is an excellent demonstration of the power of the newer formalism.

In the following section we begin by recounting the connections between symmetries and conserved quantities already encountered in Chapter 4. We then use the variational principle to develop a statement of Noether’s theorem, and go on to prove it and demonstrate its importance through examples.

## 6.3 Cyclic Coordinates and Generalized Momenta

Already in Chapter 4 we defined a cyclic coordinate $q _ { k }$ as a generalized coordinate absent from the Lagrangian. The corresponding generalized velocity $\dot { \boldsymbol { q } } _ { k }$ is present in $L ,$ but not $q _ { k }$ itself. For example, a particle free to move in three dimensions $x , y , z$ with uniform gravity in the z direction has Lagrangian

$$
L = \frac {1}{2} m (\dot {x} ^ {2} + \dot {y} ^ {2} + \dot {z} ^ {2}) - m g z,\tag{6.70}
$$

so both x and y are cyclic, but z is not. Then from Lagrange’s equations

$$
\frac {d}{d t} \frac {\partial L}{\partial \dot {q} _ {k}} - \frac {\partial L}{\partial q _ {k}} = 0\tag{6.71}
$$

it follows that for each of the cyclic coordinates $q _ { k }$ the generalized momentum

$$
p _ {k} \equiv \frac {\partial L}{\partial \dot {q} _ {k}}\tag{6.72}
$$

is conserved, since $d p _ { k } / d t = 0$ . So in this example, both $p _ { x } = m { \dot { x } }$ and $p _ { y } = m { \dot { y } }$ are conserved, but $p _ { z }$ is not.

Now the interesting question is: Why is a particular coordinate cyclic, from a physical point of view? Why are x and y cyclic in our example, but z is not?

The answer is quite clear. The physical environment is invariant under displacements in the x and y directions, but not under vertical displacements. Changes in z mean that we get closer or farther from the ground, but changes in x or y make no difference whatever. Everything looks exactly the same if we displace ourselves horizontally. We say there is a symmetry under horizontal displacements, but not under vertical displacements. So through Lagrange’s equations we see that the momenta $p _ { x } , p _ { y }$ are conserved but $p _ { z }$ is not. Two symmetries, those in the x and y directions, have led to two conserved quantities.

If a generalized coordinate $q _ { i }$ is missing from the Lagrangian, that means there is a symmetry under changes in that coordinate: the physical environment, whether a potential energy or a constraint, is independent of that coordinate. And if the environment possesses the symmetry, the corresponding generalized momentum will be conserved. This is very important, not least because the equation of motion for that coordinate will be only first order rather than second order, so becomes much easier to solve.

## Example 6.5

## A Star Orbiting a Spheroidal Galaxy

A particular galaxy consists of an enormous sphere of stars somewhat squashed along one axis, so it becomes spheroidal in shape, as shown in Figure 6.6. A star at the outer fringes of the galaxy experiences the genera gravitational pull of the galaxy. Are there any conserved quantities in the motion of this star?

We can answer this question by identifying any symmetries in the environment of the star. There are no translational symmetries; any finite translation takes one nearer or farther from the galaxy, so no component of linear momentum is conserved.

![](images/1892c63fb6cad94180bc89f3825e1311baf52bc27e83a3c9afffff23844706e7.jpg)  
An elliptical galaxy (NGC 1132) pulling on a star at the outer fringes. Image credit: Optical: NASA/ESA/STScI/M. West; X-ray: NASA/CXC/Penn State/G. Garmire.

## Fig. 6.6

There is, however, a symmetry under rotation about the squashed axis ofthe galaxy; ifwe imagine rotating about that axis, the shape of the galaxy, and therefore its gravitational field, will be unchanged. Therefore we expect that the angular momentum $p _ { \varphi }$ about this axis will be conserved. No other component of angular momentum will be conserved, because if we rotate about any other axis, the galaxy will look diferent. Therefore we expect conservation of angular momentum about a single axis only, and no conservation of linear momentum in any direction.

Mathematically, using cylindrical coordinates $( \rho , \varphi , z )$ , the kinetic and gravitational potential energies of the star are

$$
T = \frac {1}{2} m (\dot {\rho} ^ {2} + \rho^ {2} \dot {\varphi} ^ {2} + \dot {z} ^ {2}) \text { and } U = U (\rho , z),\tag{6.73}
$$

where the symmetric shape of the galaxy means that the gravitational potential depends on $\rho$ and $z ,$ but not $\varphi .$ . Therefore the Lagrangian $L = T \ - \ U$ depends on $\rho$ and $z ,$ but $\varphi$ is cyclic. The corresponding generalized momentum $p _ { \varphi } = \partial l / \partial { \dot { \varphi } } _ { \scriptscriptstyle { \ L } }$ , which is in fact the angular momentum about thez axis, is therefore conserved.

Example 6.6

## A Charged Particle Moving Outside a Charged Rod

An infinite straight dielectric rod is oriented in the z direction, and given a uniform electric charge per unit length. A point charge is free to move outside it, as shown in Figure 6.7. Are there any conserved quantities for the motion of the particle?

![](images/3c309a0898c35dfe0b1c813a744e6b5342c73a48fd59cd202247f15daeb5e7d7.jpg)

Fig. 6.7 A charged particle moving near a charged rod.

This time the environment of the particle has two symmetries: a symmetry corresponding to a rotation about the rod axis, and a symmetry corresponding to displacements in the z direction, along the rod axis. ${ \sf I f } \varphi$ is the angle about the rod in the $x , y$ plane, then the generalized momentum $p _ { \varphi } .$ , which is in fact the angular momentum ofthe particle about thez axis, is conserved, because ofsymmetry under rotation. The generalized momentum $p _ { z }$ is also conserved, because of symmetry under displacement in the z direction; this is the linear momentum of the particle in the z direction. The other components of linear momentum are not conserved, and the other components ofangular momentum are also not conserved, because there is no symmetry under displacements in the x or y direction, or under rotations about any other axis.

Mathematically, the kinetic and potential energies in this case (using cylindrical coordinates) have the form

$$
T = \frac {1}{2} m \left(\dot {\rho} ^ {2} + \rho^ {2} \dot {\varphi} ^ {2} + \dot {z} ^ {2}\right) \text {   and   } U = U (\rho).\tag{6.74}
$$

Therefore, when the Lagrangian $L = T - U$ is assembled, both $\varphi$ and z are cyclic, so the corresponding generalized momenta $p _ { \varphi } , p _ { z }$ are conserved, as we already knew from our more “physical”analysis.

## 6.4 A Less Straightforward Example

Consider the simple mechanics problem we described in Section 4.5. Two particles, with masses $m _ { 1 }$ and $m _ { 2 }$ , are constrained to move along a horizontal frictionless rail, as depicted in Figure 4.9. The action for the system is

$$
S = \int d t \left(\frac {1}{2} m _ {1} \dot {q} _ {1} ^ {2} + \frac {1}{2} m _ {2} \dot {q} _ {2} ^ {2} - U (q _ {1} - q _ {2})\right),\tag{6.75}
$$

with some interaction between the particles described by a potential $U ( q _ { 1 } - q _ { 2 } )$ that depends only on the distance between the particles.

Note that neither $q _ { 1 }$ nor $q _ { 2 }$ is cyclic, so it might seem that there are no symmetries in this problem. However, let us consider a simple transformation of the coordinates given by

$$
q _ {1} ^ {\prime} = q _ {1} + \mathrm{C}, \quad q _ {2} ^ {\prime} = q _ {2} + \mathrm{C},\tag{6.76}
$$

where C is some arbitrary constant. So in this case, we have simply changed the origin of coordinates, which should have no effect on the physics. We then have

$$
\dot {q} _ {1} ^ {\prime} = \dot {q} _ {1}, \quad \dot {q} _ {2} ^ {\prime} = \dot {q} _ {2},\tag{6.77}
$$

so the kinetic terms in the action are unchanged under this transformation. Furthermore, we also have

$$
q _ {1} ^ {\prime} - q _ {2} ^ {\prime} = q _ {1} - q _ {2},\tag{6.78}
$$

implying that the potential term is also unchanged. The action then preserves its overall structural form under the transformation

$$
S \rightarrow \int d t \left(\frac {1}{2} m _ {1} (\dot {q} _ {1} ^ {\prime}) ^ {2} + \frac {1}{2} m _ {2} (\dot {q} _ {2} ^ {\prime}) ^ {2} - U (q _ {1} ^ {\prime} - q _ {2} ^ {\prime})\right).\tag{6.79}
$$

This means that the equations of motion, written in the primed transformed coordinates, are identical to the ones written in the unprimed original coordinates. We can then say that the transformation given by (6.76) is a symmetry of our system. Physically, we are simply saying that – since the interaction between the particles depends only on the distance between them – a constant shift of both coordinates leaves the dynamics unaffected. Indeed, we showed in Chapter 4 that in this problem a simple linear transformation of coordinates to center-of-mass and relative coordinates produced a cyclic coordinate, the position of the center of mass. As a result, the momentum of the center of mass, that is the total momentum, is conserved.

It is also useful to consider an infinitesimal version of such a transformation. Assume that the constant C is small, $\mathrm { C }  \epsilon ;$ and write

$$
q _ {k} ^ {\prime} - q _ {k} = \epsilon\tag{6.80}
$$

for $k \ = \ 1 , 2$ . We then say that the shift of the coordinates is a symmetry of our system. To make these ideas more useful, in the next section we extend this example by considering a general class of interesting transformations.

## 6.5 Infinitesimal Transformations

We consider two types of infinitesimal transformations: direct and indirect.

## Direct Transformations

A direct transformation deforms the generalized coordinates of a system as in

$$
\delta q _ {k} (t) = q _ {k} ^ {\prime} (t) - q _ {k} (t) \equiv \Delta q _ {k} (t, q).\tag{6.81}
$$

We use the notation $\Delta$ to label a direct transformation. Note that $\Delta q _ { k } ( t , q )$ is possibly a function of time and all of the generalized coordinates in the problem. In the example of Section 6.4, we used the special case $\Delta q _ { k } ( t , q )$ = constant. But it need not be so. Figure 6.8(a) depicts a direct transformation: it is an arbitrary, but small shift in the $q _ { k } \mathbf { S }$ atfixed time. In the figure, a particular generalized coordinate $q _ { k }$ is shifted to slightly larger variable values for early times, and then to slightly smaller variable values for later times.

![](images/b5e0806865979f7967d808f9f79f9315bd7ac3e838a4700a72b891e15c0121ed.jpg)

![](images/e50d36f59a47ce23e81bd44757c58d0994455c2697ac1ac1494ddb5f96456960.jpg)  
Fig. 6.8 The two types of transformations considered: (a) direct; (b) indirect.

## Indirect Transformations

By contrast, an indirect transformation affects the generalized coordinates indirectly – through the transformation of the time coordinate

$$
\delta t (t, q) \equiv t ^ {\prime} - t.\tag{6.82}
$$

Note again that the shift in time is assumed to be small, and this shift can itself depend on time. The small shifts in time then bring about small shifts in the generalized coordinates, in which case they have been affected indirectly:

$$
q _ {k} (t) = q _ {k} \left(t ^ {\prime} - \delta t\right) \simeq q _ {k} \left(t ^ {\prime}\right) - \frac {d q _ {k}}{d t ^ {\prime}} \delta t \simeq q _ {k} \left(t ^ {\prime}\right) - \dot {q} _ {k} \delta t,\tag{6.83}
$$

where we have used a Taylor expansion in $\delta t$ to linear order only, since $\delta t$ is small (see Appendix F). We also have used $d q _ { k } / d t ^ { \prime } = - ~ d q _ { k } / d t$ since this term already multiplies a power of $\delta t \colon$ to linear order in $\delta t ,$ δ $d q _ { k } / d t ^ { \prime } = \delta t d q _ { k } / d t \equiv \delta t \dot { q } _ { k }$ . We then see that shifting time results in a shift in the generalized coordinates

$$
\delta q _ {k} = q _ {k} (t ^ {\prime}) - q _ {k} (t) = \dot {q} \delta t (t, q).\tag{6.84}
$$

Compare with Eq. (6.81) and note that the coordinates are now evaluated at different times. Figure 6.8(b) shows how we can think of this effect graphically: a small change in time has caused a small change in the generalized coordinate $\delta q _ { k } ( t )$

## Combined Transformations

In general, we want to consider a transformation that may include both direct and indirect pieces. We write

$$
\begin{array}{l} \delta q _ {k} = q _ {k} ^ {\prime} (t ^ {\prime}) - q _ {k} (t) = q _ {k} ^ {\prime} (t ^ {\prime}) + \left(- q _ {k} (t ^ {\prime}) + q _ {k} (t ^ {\prime})\right) - q _ {k} (t) \\ \qquad = \left(q _ {k} ^ {\prime} (t ^ {\prime}) - q _ {k} (t ^ {\prime})\right) + \left(q _ {k} (t ^ {\prime}) - q _ {k} (t)\right) = \Delta q _ {k} (t ^ {\prime}, q) + \dot {q}   \delta t (t, q) \\ \qquad = \Delta q _ {k} (t, q) + \dot {q}   \delta t (t, q), \end{array}\tag{6.85}
$$

where in the last line we have equated t and $t ^ { \prime }$ since the first term is already linear in the small parameters. To specify a particular transformation, we could then provide a set of functions

$$
\delta t (t, q) \quad \text { and } \quad \delta q _ {k} (t, q),\tag{6.86}
$$

from which Eq. (6.85) determines $\Delta q _ { k } ( t , q )$ . For N degrees of freedom, that amounts to $N + ~ 1$ functions of time and the $q _ { k } \mathbf { S }$ . Let us look at a few examples.

## Example 6.7 Translations

Consider a single particle in three dimensions, described by the three Cartesian coordinate $r ^ { x } = x , r ^ { y } = y ,$ and $r ^ { Z } = Z .$ We also have the time coordinate $r ^ { t } = c t .$ . An infinitesimal constant spatial translation can be realized by

$$
\delta r ^ {i} (t, x) = \epsilon^ {i}, \delta t (t, x) = 0 \Rightarrow \Delta r ^ {i} (t, x) = \delta \epsilon^ {i},\tag{6.87}
$$

where $\begin{array} { r } { i = x , y , z , } \end{array}$ and the $\epsilon ^ { j } \mathfrak { s }$ are three small constants. A translation in space is then defined by

$$
\left\{\delta t (t, x) = 0, \delta r ^ {i} (t, x) = \delta \epsilon^ {i} \right\} \quad \text { Translation   in   space. }\tag{6.88}
$$

A constant translation in time would be given by

$$
\delta r ^ {i} (t, x) = 0, \delta t (t, x) = \delta \epsilon \Rightarrow \Delta r ^ {i} (t, x) = - \dot {r} ^ {i} \delta \epsilon\tag{6.89}
$$

for constant $\varepsilon .$ Notice that for a translation purely in time, we need to require that the total shifts in the $r ^ { j } s \mathrm { ~ - ~ }$ the $\delta r ^ { j } ( t , x ) s$ – vanish. This then generates direct shifts, the $\Delta r ^ { j } \mathsf { s } ,$ to compensate for the indirect efect on the spatial coordinates from the shifting of the time. A translation in time is then defined by

$$
\{\delta t (t, x) = \delta \epsilon , \delta r ^ {i} (t, x) = 0 \} \quad \text { Translation   in   time }.\tag{6.90}
$$

## Example 6.8

## Rotations

To describe constant rotations, we consider for simplicity a particle moving in two dimensions. We use the coordinates $r ^ { x } = x { \sf a n d } r ^ { y } = y ,$ and start by specifying

$$
\delta t (t, x) = 0 \Rightarrow \delta r ^ {i} (t, x) = \Delta r ^ {i} (t, x),\tag{6.91}
$$

with $\begin{array} { r } { i = x , y . } \end{array}$ . Next, we look at an arbitrary rotation angle θ using Eq. (2.21):

$$
\binom{r ^ {x ^ {\prime}}}{r ^ {y ^ {\prime}}} = \left( \begin{array}{c c} \cos \theta & \sin \theta \\ - \sin \theta & \cos \theta \end{array} \right) \binom{r ^ {x}}{r ^ {y}}.\tag{6.92}
$$

However, we need to focus on an infinitesimal version of this transformation: i.e., we need to consider small angles $\delta \theta .$ . Using cos $\delta \theta \sim 1$ and sin $\delta \theta \sim \delta \theta$ to first order in $\delta \theta ,$ , we then write<sup>a</sup>

$$
\binom{r ^ {x ^ {\prime}}}{r ^ {y ^ {\prime}}} = \left( \begin{array}{c c} 1 & \delta \theta \\ - \delta \theta & 1 \end{array} \right) \binom{r ^ {x}}{r ^ {y}}.\tag{6.93}
$$

This gives

$$
\delta r ^ {x} (t, x) = r ^ {x ^ {\prime}} (t) - r ^ {x} (t) = \delta \theta r ^ {y} (t) = \Delta r ^ {x} (t, x),
$$

$$
\delta r ^ {y} (t, x) = r ^ {y ^ {\prime}} (t) - r ^ {y} (t) = - \delta \theta r ^ {x} (t) = \Delta r ^ {y} (t, x).\tag{6.94}
$$

We now have a less trivial transformation. Rotations can be defined by

$$
\{\delta t (t, x) = 0, \delta r ^ {i} (t, x) = \delta \theta \varepsilon_ {j} ^ {i} r ^ {j} (t) \} \quad \text { Two - dimensional   spatial   rotation },\tag{6.95}
$$

wherej is summed over 1 and 2. We have also introduced a useful shorthand: $\boldsymbol { \varepsilon } _ { j } ^ { j }$ is the totally antisymmetric matrix in two dimensions, given by

$$
\varepsilon_ {x} ^ {x} = \varepsilon_ {y} ^ {y} = 0, \varepsilon_ {y} ^ {x} = - \varepsilon_ {x} ^ {y} = 1,\tag{6.96}
$$

which has allowed us to write the transformation in a more compact notation.

<sup>a</sup>Recall that the Taylor series expansions of cos δθ and sin $\delta \theta$ are cos $\delta \theta = 1 ~ - ~ \delta \theta ^ { 2 } / 2 ! + \delta \theta ^ { 4 } / 4 ! - . .$ . and sin $\delta \theta = \delta \theta ~ - ~$ $\delta \theta ^ { 3 } / 3 ! + \delta \theta ^ { 5 } / 5 ! - . .$ . (see Appendix F for more).

## Example 6.9

## Lorentz Transformations

To find the infinitesimal form of Lorentz transformations, we can start with the general transformation equations (2.15) and take the velocity paramete $\beta = v / c$ c to be small. We need to be careful, however, to keep the leading-order terms in $\beta$ in all expansions. Given our previous example, it is easier to map the problem onto a rotation with hyperbolic trig functions and the rapidity $\xi ,$ which (as shown in Chapter 2) is

$$
\left( \begin{array}{c} c t \\ x \\ y \\ z \end{array} \right) = \left( \begin{array}{c c c c} \cosh \xi & \sinh \xi & 0 & 0 \\ \sinh \xi & \cosh \xi & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{array} \right) \left( \begin{array}{c} c t ^ {\prime} \\ x ^ {\prime} \\ y ^ {\prime} \\ z ^ {\prime} \end{array} \right),\tag{6.97}
$$

where $\gamma = \cosh \xi , \ \gamma \beta = \sinh \xi .$ . For simplicity, let us consider a particle in one dimension, with two relevant coordinates $r ^ { t } = c t$ and $r ^ { X } .$ . We take the rapidity $\xi ~  ~ \delta \xi$ to be small and use cosh $\delta \xi \sim 1$ and sinh $\delta \xi \sim \delta \xi$ to linear order in $\delta \xi$ . Using the same steps as in the previous example, we find

$$
\delta r ^ {t} (t, x) = \delta \xi r ^ {x}, \delta r ^ {x} (t, x) = \delta \xi r ^ {t}.\tag{6.98}
$$

Using Eq. (6.85), we then have

$$
\Delta r ^ {x} (t, x) = \delta r ^ {x} (t, x) - \dot {r} ^ {x} \frac {\delta r ^ {t} (t , x)}{c} = \delta \xi r ^ {t} - \frac {\delta \xi}{c} \dot {r} ^ {x} r ^ {x}.\tag{6.99}
$$

Note that

$$
\sinh \xi = \gamma \beta \Rightarrow \sinh \delta \xi \sim \delta \xi \sim \beta .\tag{6.100}
$$

The Lorentz transformations can then be defined by

$$
\left\{\delta r ^ {t} = \beta r ^ {x}, \delta r ^ {x} = \beta r ^ {t}, \delta r ^ {y} = \delta r ^ {z} = 0 \right\} \text { Lorentz   transformation },\tag{6.101}
$$

where we added the efect on the transverse directions as well.

## 6.6 Symmetry

We define a symmetry to be a transformation that leaves the action unchanged in form. In the particular example of two interacting particles on a frictionless rail, it was simple to see that the transformation was indeed a symmetry. Now that we have a general class oftransformations, we want to find a general condition that can be used to test whether a particular transformation – possibly a complicated one – is or is not a symmetry. We then need to look at how the action changes under a general transformation: for a symmetry, this change should vanish. We start with the usual form for the action:

$$
S = \int d t L (q, \dot {q}, t).\tag{6.102}
$$

Then we apply a general transformation given by $\Delta q _ { k } ( t , q )$ and $\delta t ( t , q )$ . It follows that

$$
\delta S = \int \delta (d t) L + \int d t \delta (L),\tag{6.103}
$$

where we have used the Leibniz product rule $\delta ( a b ) = ( \delta a ) b + a ( \delta b )$ , since $\delta$ is an infinitesimal change. The first term is the change in the measure of the integrand:

$$
\delta (d t) = d t \frac {\delta (d t)}{d t} = d t \frac {d}{d t} (\delta t),\tag{6.104}
$$

where in the last part we exchanged the order of $\cdot \delta$ and $d ,$ , since they commute.<sup>3</sup> The second term has two parts

$$
\delta (L) = \Delta (L) + \delta t \frac {d L}{d t}.\tag{6.105}
$$

The first part is the change in L resulting from its dependence on the $q _ { k } \mathbf { S }$ and ${ \dot { q } } _ { k } \mathbf { s } .$ Hence, we labeled it as a direct change with a $\Delta$ . The second part is the change in $L$ to linear order in δt due to the change in t. This comes from changes in the $q _ { k } \mathbf { S }$ on which $L$ depends, as well as changes in t directly, since t can make an explicit appearance in $L$ . This is an identical situation to the linear expansion encountered for $q _ { k }$ in Eq. (6.85): there is a part from direct changes in the degrees of freedom, as well as a part from the transformation of time. Then, using multivariable calculus:

$$
\Delta (L) = \frac {\partial L}{\partial q _ {k}} \Delta q _ {k} + \frac {\partial L}{\partial \dot {q} _ {k}} \Delta (\dot {q} _ {k}) = \frac {\partial L}{\partial q _ {k}} \Delta q _ {k} + \frac {\partial L}{\partial \dot {q} _ {k}} \frac {d}{d t} (\Delta q _ {k}).\tag{6.106}
$$

Note that in the last term we exchanged the orders of $\Delta$ and $d / d t$ . We can now put everything together, so that

$$
\begin{array}{l} \delta S = \int d t \left(\frac {\partial L}{\partial q _ {k}} \Delta q _ {k} + \frac {\partial L}{\partial \dot {q} _ {k}} \frac {d}{d t} (\Delta q _ {k}) + \delta t \frac {d L}{d t} + L \frac {d}{d t} (\delta t)\right) \\ = \int d t \left(\frac {\partial L}{\partial q _ {k}} \Delta q _ {k} + \frac {\partial L}{\partial \dot {q} _ {k}} \frac {d}{d t} (\Delta q _ {k}) + \frac {d}{d t} (L \delta t)\right). \end{array}\tag{6.107}
$$

Now given $L , \delta t ( t , q )$ , and $\delta q _ { k } ( t , q )$ (hence also $\Delta q _ { k } ( t , q ) )$ , we can substitute these into Eq. (6.107) and check whether the expression vanishes. If it does vanish, we conclude that the given transformation $\{ \delta t ( t , q ) , \delta q _ { k } ( t , q ) \}$ is a symmetry of our system. This shall be our notion of symmetry. A bit later, we will revisit this statement and generalize it further. For now, this is enough to move on to the heart of the topic, Noether’s theorem.

## 6.7 Noether’s Theorem

We start by simply stating the theorem:

Noether’s theorem: For every symmetry, i.e., for every set of transformations $\{ \delta t ( t , q ) , \delta q _ { k } ( t , q ) \}$ that leave the action unchanged, there exists a quantity that is conserved under time evolution.

A symmetry implies a conservation law. This is important for two reasons:

• First, a conservation law identifies a rule in the laws of physics. Virtually everything we have a name for in physics – mass, momentum, energy, charge, etc. – is tied by definition to a conservation law. Noether’s theorem then states that fundamental physics is founded on the principle of identifying symmetries. If we want to know all the laws of physics, we need to ask: What are all the symmetries in Nature? From there, we find conservation laws and associated interesting conserved quantities. We can then study how these conservation laws can sometimes be violated. This leads us to equations that can predict the future. It’s all about symmetries.

• Second, conservation laws have the form

$$
\frac {d}{d t} (\text { something }) = 0 \Rightarrow \text { something } = \text { constant }.\tag{6.108}
$$

The “something” is typically a function of the degrees of freedom and the first derivatives of the degrees of freedom. The conservation statement then inherently leads to first-order differential equations. First-order differential equations are much more pleasant than second or higher-order equations. Thus, technically, finding the symmetries and corresponding conservation laws in a problem helps a great deal in solving and understanding the physical system.

The easiest way to understand Noether’s theorem is to prove it, which is a surprisingly simple exercise.

## Proof of the Theorem

The premise of the theorem is that we have a given symmetry $\{ \delta t ( t , q ) , \Delta q _ { k } ( t , q ) \}$ This then implies, using Eq. (6.107), that

$$
\delta S = 0 = \int d t \left(\frac {\partial L}{\partial q _ {k}} \Delta q _ {k} + \frac {\partial L}{\partial \dot {q} _ {k}} \frac {d}{d t} (\Delta q _ {k}) + \frac {d}{d t} (L \delta t)\right).\tag{6.109}
$$

We know that this equation is satisfied for any set of curves $q _ { k } ( t )$ by virtue of the assumption that $\{ \delta t ( t , q ) , \Delta q _ { k } ( t , q ) \}$ constitutes a symmetry. And now comes the crucial step: what if the $q _ { k } ( t ) \mathbf { s }$ satisfy the Lagrange equations of motion

$$
\frac {d}{d t} \left(\frac {\partial L}{\partial \dot {q} _ {k}}\right) = \frac {\partial L}{\partial q _ {k}}?\tag{6.110}
$$

Of all possible curves $q _ { k } ( t )$ , we pick the ones that satisfy the equations of motion. Given this additional statement, we can rearrange the terms in δS to give

$$
0 = \int d t \frac {d}{d t} \left(\frac {\partial L}{\partial \dot {q} _ {k}} \Delta q _ {k} + L \delta t\right).\tag{6.111}
$$

Since the integration interval is arbitrary, we then conclude that

$$
\frac {d}{d t} (Q) = 0,\tag{6.112}
$$

where

$$
Q \equiv \frac {\partial L}{\partial \dot {q} _ {k}} \Delta q _ {k} + L \delta t.\tag{6.113}
$$

Therefore we have a conserved quantity $\boldsymbol { Q }$ called the Noether charge. Note a few important points:

• We used the equations of motion to prove the conservation law. However, we did not use the equations of motion to conclude that a particular transformation is a symmetry. The symmetry exists at the level of the action for any $q _ { k } ( t )$ . The conservation law exists for trajectories that satisfy the equations of motion.

• The proof identifies explicitly the conserved quantity through Eq. (6.113). Knowing L, $\delta t ( t , q )$ , and $\delta q _ { k } ( t , q )$ (hence also $\Delta q _ { k } ( t , q )$ from Eq. (6.85)), this equation tells us immediately the conserved quantity associated with the given symmetry.

This proofalso highlights a way to generalize the original definition ofsymmetry. All that was needed was to be able to write

$$
\delta S = \int d t \frac {d}{d t} (K),\tag{6.114}
$$

where K is some function that we can discover by using Eq. (6.107). If K turns out to be a constant, we would get $\delta S = 0$ trivially, and we are back to the situation just discussed. However, if K is nontrivial, we get (using Lagrange’s equations)

$$
\delta S = \int d t \frac {d}{d t} (K) = \int d t \frac {d}{d t} \left(\frac {\partial L}{\partial \dot {q} _ {k}} \Delta q _ {k} + L \delta t\right),\tag{6.115}
$$

from which it follows from the definitions that

$$
\frac {d}{d t} (Q - K) = 0.\tag{6.116}
$$

Therefore the conserved quantity is $Q - K$ rather than $\boldsymbol { Q }$ by itself. Since the interesting conceptual content of a symmetry is its associated conservation law, we want to turn the problem on its back: we want to define a symmetry through a conservation statement. So, here is a revised, more general statement:

$$
\{\delta t (t, q), \delta q _ {k} (t, q) \} \text {   is   a   symmetry   if   }
$$

$$
\delta S = \int d t \frac {d K}{d t} \text {   for   some   } K.\tag{6.117}
$$

Noether’s theorem then states that for every such symmetry, there is a conserved quantity given by $Q - K$

To summarize, the general prescription is as follows:

1. Given a Lagrangian L and a candidate symmetry $\{ \delta t ( t , q ) , \delta q _ { k } ( t , q ) \}$ , use Eq. (6.107) to find δS. If $\delta S ~ = ~ \int d t d K / d t$ for some K we are to determine, $\{ \delta t ( t , q ) , \delta q _ { k } ( t , q ) \}$ is indeed a symmetry.

2. If $\{ \delta t ( t , q ) , \delta q _ { k } ( t , q ) \}$ is found to be a symmetry with some K, we can find an associated conserved quantity $\mathcal Q - K$ , with Q given by Eq. (6.113).

The best way to understand all of this is to look at a few examples.

## Example 6.10 Space Translations and Momentum

We start with the spatial translation transformation in a fixed ith direction, as in our previous example (6.87):

$$
\delta r ^ {i} (t, x) = \delta \epsilon^ {i}, \delta t (t, x) = 0 \Rightarrow \Delta r ^ {i} (t, x) = \delta \epsilon^ {i},\tag{6.118}
$$

where $\delta \epsilon ^ { j }$ is a constant and $\delta r ^ { k } = \Delta r ^ { k } , = 0$ for k -= i (both i and k lie in the spatial directions). We next need a Lagrangian to test this transformation. Consider first a free nonrelativistic particle whose Lagrangian is

$$
L = \frac {1}{2} m \dot {r} ^ {k} \dot {r} ^ {k}.\tag{6.119}
$$

Substitute eqs. (6.118) and (6.119) into (6.107):

$$
\begin{array}{l} \delta S = \int d t \left(\frac {\partial L}{\partial q _ {k}} \Delta q _ {k} + \frac {\partial L}{\partial \dot {q} _ {k}} \frac {d}{d t} (\Delta q _ {k}) + \frac {d}{d t} (L \delta t)\right) \\ = \int d t \left(0 \cdot \Delta q _ {k} + m \dot {r} ^ {j} \frac {d}{d t} \delta \epsilon^ {i} + \frac {d}{d t} (0)\right) = 0 (\text { no   sum   on } i), \end{array}\tag{6.120}
$$

since $\delta \epsilon ^ { j }$ is a constant. Therefore $K = \mathsf { c o n s t a n t } ,$ , so we have a symmetry. To find the associated conserved charge, we use Eq. (6.113) and find

$$
Q ^ {i} = m \dot {r} ^ {i} \delta \epsilon^ {i} (\text { no   sum   on } i).\tag{6.121}
$$

We can repeat this for every $~ i ~ = ~ x , y , z .$ We then have three charges for the three possible directions for translation. Any overall additive or multiplicative constant is arbitrary, since it does not afect the statement of conservation $\dot { Q } ^ { j } = 0$ . Writing the conserved quantities as $P ^ { j }$ instead, we can then state

$$
P ^ {i} = m \dot {r} ^ {i}.\tag{6.122}
$$

That is, momentum is the Noether charge associated with the symmetry of spatial translational invariance. If we have a physical system set up on a table and we notice that we can shift the table by any amount in any of the three spatial directions without afecting the dynamics of the system, we can conclude that there is a quantity – called momentum by definition – that remains constant in time.

We can then try to find the conditions under which this symmetry, and hence the conservation law, is violated. For example, we can add a simple harmonic oscillator potential to the Lagrangian:

$$
L = \frac {1}{2} m \dot {r} ^ {k} \dot {r} ^ {k} - \frac {1}{2} k r ^ {i} r ^ {i} (\text { no   sum   on } i).\tag{6.123}
$$

Using Eq. (6.107), we now get

$$
\delta S = \int d t (- k r ^ {i} \delta \epsilon^ {i}) \neq \int \frac {d}{d t} (K) (\text { no   sum   on } i).\tag{6.124}
$$

Hence, momentum is no longer conserved in the ith direction and we can write

$$
\dot {P} ^ {i} \neq 0 \Rightarrow \dot {P} ^ {i} \equiv F ^ {i},\tag{6.125}
$$

thus introducing the concept of force. We now see that the existence or non-existence of forces in Newton’s second law arises from the existence or non-existence of a certain symmetry in Nature.

Newton’s third law is also related to this idea: action–reaction pairs cancel each other, so that the total force on an isolated system is zero and hence the total momentum is conserved. To see this, look back at the two-particle system on a rail, described by the Lagrangian (6.75). Using once again Eq. (6.107) with $\delta t = 0$ and $\delta q _ { i } = \delta \epsilon$ , we get

$$
\delta S = \int d t \left(- \frac {\partial U}{\partial q _ {1}} \delta \epsilon + \frac {\partial U}{\partial q _ {2}} \delta \epsilon\right) = 0\tag{6.126}
$$

since

$$
\frac {\partial}{\partial q _ {1}} U (q _ {1} - q _ {2}) = - \frac {\partial}{\partial q _ {2}} U (q _ {1} - q _ {2}).\tag{6.127}
$$

The forces on each particle are $- \partial U / \partial q _ { 1 }$ and $- \partial U / \partial q _ { 2 }$ , which are equal in magnitude but opposite in sign, since the potential energy has the form $U ( q _ { 1 } \mathrm { ~ - ~ } q _ { 2 } )$ – note the relative minus sign between $q _ { 1 }$ and $q _ { 2 } .$ . These two forces form the action–reaction pair. The cancellation of forces arises because of the dependence of the potential and force on the distance $q _ { 1 } ~ - ~ q _ { 2 }$ between the particles – which is what makes the problem translationally invariant as well. We now see that the third law is intimately tied to the statement of translational symmetry. The associated conserved quantity determined from Eq. (6.113) is

$$
P _ {i} = m _ {1} \dot {q} _ {1} + m _ {2} \dot {q} _ {2},\tag{6.128}
$$

and so the Noether charge is now the total momentum of the system, and it is conserved.

## Example 6.11

## Time Translation and the Hamiltonian

Next, let us consider time translational invariance. Due to its particular usefulness, we want to treat this example with greater generality. We focus on a system with an arbitrary number ofdegrees offreedom labeled by $q _ { k } \mathsf { S } ,$ , with a general Lagrangian $L ( q , \dot { q } , t )$ . We propose the transformation

$$
\delta t = \delta \epsilon , \delta q _ {k} = 0.\tag{6.129}
$$

Therefore the degrees offreedom are left unchanged, but the time is shifted by a constant $\delta \epsilon$ . This means that we need a direct shift

$$
\delta q _ {k} = 0 = \Delta q _ {k} + \dot {q} _ {k} \delta t = \Delta q _ {k} + \delta \epsilon \dot {q} _ {k} \Rightarrow \Delta q _ {k} = - \delta \epsilon \dot {q} _ {k}\tag{6.130}
$$

to compensate for the indirect change in $q _ { k }$ induced by the shift in time. We then use Eq. (6.107) to find that the change in the action is

$$
\delta S = \int d t \left(- \delta \epsilon \dot {q} _ {k} \frac {\partial L}{\partial q _ {k}} - \delta \epsilon \ddot {q} _ {k} \frac {\partial L}{\partial \dot {q} _ {k}} + \delta \epsilon \frac {d L}{d t}\right).\tag{6.131}
$$

But we also know from multivariable calculus that

$$
\frac {d L}{d t} = \frac {\partial L}{\partial t} + \frac {\partial L}{\partial q _ {k}} \dot {q} _ {k} + \frac {\partial L}{\partial \dot {q} _ {k}} \ddot {q} _ {k},\tag{6.132}
$$

so we can write simply

$$
\delta S = \int d t \frac {\partial L}{\partial t} \delta \epsilon .\tag{6.133}
$$

In general, since L depends on the $q _ { k } \mathsf { S }$ as well as explicit $t 5 ,$ we need to consider the more restrictive condition for symmetry $\delta { \sf S } = 0 , i . e .$ , we have K = constant. This implies that we have time translational symmetry if

$$
\frac {\partial L}{\partial t} = 0,\tag{6.134}
$$

$\therefore e .$ , if the Lagrangian does not depend on time explicitly. If this is the case, we then have a conserved quantity given by Eq. (6.113):

$$
Q = - \delta \epsilon \dot {q} _ {k} \frac {\partial L}{\partial \dot {q} _ {k}} + \delta \epsilon L.\tag{6.135}
$$

Dropping the overall constant term −δ	 and rearranging:

$$
Q \rightarrow \dot {q} _ {k} \frac {\partial L}{\partial \dot {q} _ {k}} - L = H,\tag{6.136}
$$

which we recognize as the Hamiltonian H of the system, already introduced in Chapter 4.

Consider, for example, the two-particle problem in one dimension described by the Lagrangian (4.48). We then find

$$
H = \frac {1}{2} m _ {1} \dot {q} _ {1} ^ {2} + \frac {1}{2} m _ {2} \dot {q} _ {2} ^ {2} + U (q _ {1} - q _ {2}),\tag{6.137}
$$

which is obviously also the energy $E = T + U$ in this case. As shown in Section 4.7 ofChapter 4, the Hamiltonian H is equal to the energy E if the transformation $\boldsymbol { \mathsf { r } } = \boldsymbol { \mathsf { r } } ( \boldsymbol { q } _ { k } , t )$ , from the generalized coordinates to Cartesian coordinates, is not an explicit function oftime. Therefore, ifthe results ofa series ofexperiments do not depend upon when the experiments are performed, we expect that the Hamiltonian of the system will be conserved. In many circumstances $H = E ,$ , so we often say that invariance under displacements in time indicates that the energy of the system is conserved. We can then look at dissipative efects involving loss of energy and learn about new physics through the nonconservation of energy.

Example 6.12

## Rotations and Angular Momentum

Consider the problem of a nonrelativistic particle of mass m moving in two dimensions, in a plane labeled by $\mathfrak { r } ^ { x } = x \mathrm { a n d } \mathfrak { r } ^ { y } = y .$ . We add to the problem a central force with a Lagrangian of the form

$$
L = \frac {1}{2} m \dot {\mathbf {r}} ^ {i} \dot {\mathbf {r}} ^ {j} - U (\dot {\mathbf {r}} ^ {i} \dot {\mathbf {r}} ^ {j}) \text {   summed   on   } i, \text {   with   } i = x, y.\tag{6.138}
$$

Note that the potential depends only on the distance $\sqrt { \mathsf { r } ^ { i } \mathsf { r } ^ { i } }$ of the particle from the origin of the coordinate system. Rotations are described by Eq. (6.95). We can then use Eq. (6.107) to test for rotational symmetry, where the change in the action is

$$
\begin{array}{l} \delta S = \int d t \left(\frac {\partial U}{\partial r ^ {i}} \Delta r ^ {i} + m \dot {r} ^ {i} \frac {d}{d t} (\Delta r ^ {i})\right) \\ = \int d t \left(2 U ^ {\prime} \delta \theta \varepsilon_ {i j} r ^ {i} r ^ {j} + m \delta \theta \varepsilon_ {i j} \dot {r} ^ {i} \dot {r} ^ {j}\right). \end{array}\tag{6.139}
$$

In the second line we wrote

$$
\frac {\partial U}{\partial \mathbf {r} ^ {i}} = \frac {\partial U}{\partial u} \frac {\partial u}{\partial \mathbf {r} ^ {i}} = \frac {\partial U}{\partial u} (2 \mathbf {r} ^ {i}) = 2 U ^ {\prime} \mathbf {r} ^ {i},\tag{6.140}
$$

where $u \equiv \mathsf { r } ^ { j } \mathsf { r } ^ { j } ,$ , and where we have used the chain rule. We now want to show that $\delta { \sf S } = 0 .$ . Focus on the first term in Eq. (6.139):

$$
2 U ^ {\prime} \delta \theta \varepsilon_ {i j} r ^ {j} r ^ {j} = 2 U ^ {\prime} \delta \theta \varepsilon_ {x y} r ^ {x} r ^ {y} + 2 U ^ {\prime} \delta \theta \varepsilon_ {y x} r ^ {y} r ^ {x} = 2 U ^ {\prime} \delta \theta r ^ {x} r ^ {y} - 2 U ^ {\prime} \delta \theta r ^ {y} r ^ {x} = 0.\tag{6.141}
$$

Let us do this one more time, with more grace and elegance:

$$
\begin{array}{r l} 2 U ^ {\prime} \delta \theta \varepsilon_ {i j} \mathfrak {r} ^ {i} \mathfrak {r} ^ {j} & = 2 U ^ {\prime} \delta \theta \varepsilon_ {j i} \mathfrak {r} ^ {i} \mathfrak {r} ^ {j} \\ & = 2 U ^ {\prime} \delta \theta \varepsilon_ {j i} \mathfrak {r} ^ {i} \mathfrak {r} ^ {j} \\ & = - 2 U ^ {\prime} \delta \theta \varepsilon_ {i j} \mathfrak {r} ^ {i} \mathfrak {r} ^ {j}. \end{array}\tag{6.142}
$$

In the second line, we just relabeled the indices $i  j { \mathsf { a n d } } j $ i: since they are summed indices, it does not matter what they are called. In the third line, we used the fact that multiplication is commutative ${ \mathfrak { p } } ^ { j } { \mathfrak { r } } ^ { j } = { \mathfrak { r } } ^ { j } { \mathfrak { r } } ^ { j }$ Finally, in the third line, we used the property $\varepsilon _ { i j } = - \varepsilon _ { j i }$ from Eq. (6.96). Hence, we have shown

$$
2 U ^ {\prime} \delta \theta \varepsilon_ {i j} r ^ {i} r ^ {j} = - 2 U ^ {\prime} \delta \theta \varepsilon_ {i j} r ^ {i} r ^ {j} \Rightarrow 2 U ^ {\prime} \delta \theta \varepsilon_ {i j} r ^ {i} r ^ {j} = 0.\tag{6.143}
$$

The key idea is that $\varepsilon _ { i j }$ is antisymmetric in its indices while $\boldsymbol { \mathsf { r } } ^ { j } \boldsymbol { \mathsf { r } } ^ { j }$ is symmetric under the same indices. The sum of their product therefore cancels. The same is true for the second term in Eq. (6.139):

$$
m \delta \theta \varepsilon_ {i j} \dot {\mathbf {r}} ^ {j} \dot {\mathbf {r}} ^ {j} = - m \delta \theta \varepsilon_ {i j} \dot {\mathbf {r}} ^ {j} \dot {\mathbf {r}} ^ {j} \Rightarrow m \delta \theta \varepsilon_ {i j} \dot {\mathbf {r}} ^ {j} \dot {\mathbf {r}} ^ {j} = 0.\tag{6.144}
$$

We will use this trick occasionally later on in other contexts. We thus have shown that our system is rotationa symmetric:

$$
\delta S = 0 \Rightarrow K = \text { constant }.\tag{6.145}
$$

We can then determine the conserved quantity using Eq. (6.113):

$$
Q = \frac {\partial L}{\partial \dot {r} ^ {i}} \Delta r ^ {i} = m \dot {r} ^ {i} \delta \theta \varepsilon_ {i j} r ^ {j}.\tag{6.146}
$$

Dropping a constant term $\delta \theta ,$ , we write

$$
I = m \varepsilon_ {i j} \dot {\mathbf {r}} ^ {i} \mathbf {r} ^ {j} = m (\dot {\mathbf {r}} ^ {x} \mathbf {r} ^ {y} - \dot {\mathbf {r}} ^ {y} \mathbf {r} ^ {x}) = (\mathbf {r} \times m \mathbf {v}) ^ {z},\tag{6.147}
$$

i.e., this is the z-component of the angular momentum of the particle. As expected, it is perpendicular to the plane of motion. Rotational symmetry implies conservation of angular momentum, and rotation about the z axis corresponds to angular momentum along the z axis.

## Example 6.13

## Lorentz and Galilean Boosts

How about a Lorentz transformation? Special relativity requires the Lorentz transformation to be a symmetry of any physical system: it is not a question of whether it is a symmetry of any particular system – it better be. We could then use Eq. (6.107), with Lorentz transformations, as a condition for sensible Lagrangians. Noether’s theorem can be used to construct theories consistent with the required symmetries. In general, an experiment would identify a set ofsymmetries in a newly discovered system. Then the theorist’s task is to build a Lagrangian that describes the system; and a good starting point would be to ensure that the Lagrangian has all the needed symmetries. We now see the power of Noether’s theorem: it allows us to mold equations and theories to our symmetry needs.

Returning to Lorentz transformations, let us look at an explicit example and find the associated conserved charge. We consider a relativistic system, say a free relativistic particle with action

$$
S = - m c ^ {2} \int d \tau = - m c ^ {2} \int d t \sqrt {1 - \frac {\dot {r} ^ {i} \dot {r} ^ {i}}{c ^ {2}}}.\tag{6.148}
$$

A particular Lorentz transformation is given by Eq. (6.101), which we can then substitute into Eq. (6.107) to show that there is a symmetry. We will return to this case in the next example. For now, consider instead the limit of small speeds, $i . e . ,$ a nonrelativistic system with Galilean symmetry. We take a single free particle in one dimension with Lagrangian

$$
L = \frac {1}{2} m \dot {x} ^ {2}.\tag{6.149}
$$

The expected symmetry is Galilean, given by (1.1):

$$
x = x ^ {\prime} + V t ^ {\prime}, y = y ^ {\prime}, z = z ^ {\prime}, t = t ^ {\prime}.\tag{6.150}
$$

We can then write the infinitesimal version

$$
\begin{array}{l} \delta t = \delta y = \delta z = 0, \delta x = - V t \\ \Rightarrow \Delta t = \Delta y = \Delta z = 0 \text { and } \Delta x = - V t. \end{array}\tag{6.151}
$$

Note that we want to think ofthis transformation near $t \sim 0 ,$ , the instant in time when the two origins coincide, to keep it as a small deformation for any V. Using Eq. (6.107), we then find

$$
\delta S = \int d t m V \dot {x}.\tag{6.152}
$$

Before we become overly concerned by the fact that this quantity does not vanish, let us remember that all that is needed is $\delta { \sf S } = \textstyle \int$ dt $d K / d t$ for some K. That is indeed the case:

$$
\delta S = \int d t \frac {d}{d t} (m V x).\tag{6.153}
$$

We then have

$$
K = m V x + \text { constant }.\tag{6.154}
$$

This system does have Galilean symmetry. We look at the associated Noether charge, using Eq. (6.113):

$$
Q = \frac {\partial L}{\partial \dot {x}} \Delta x = m \dot {x} V t.\tag{6.155}
$$

But this is not the conserved charge: the conserved quantity is

$$
Q - K = m \dot {x} V t - m V x = \text { constant }.\tag{6.156}
$$

Rewriting things, we have a simple first-order diferential equation

$$
\dot {x} t - x = \text { constant }.\tag{6.157}
$$

Integrating this gives the expected linear trajectory $\chi ( t ) \propto t .$ Unlike momentum, energy, and angular momentum, this conserved quantity $Q - K$ is not given its own glorified name. Since Galilean (or the more general Lorentz) symmetry is expected to be prevalent in all systems, this does not add any useful distinguishing physics to a problem. Perhaps if we were to discover a fundamental phenomenon that breaks Galilean/Lorentz symmetry, we could then revisit this conserved quantity and study its nonconservation. For now, this conserved charge is relegated to second-rate status.

## Example 6.14

## Lorentz Invariance

We now return to the case ofLorentz invariance. We saw in Chapter 2 that Lorentz transformations are a kind of rotation in spacetime – using hyperbolic trigonometric functions. Let us start by writing infinitesimal Lorentz transformations (6.101) in a more compact form along the lines of Eq. (6.95). We write

$$
\delta r ^ {\mu} = \beta \varepsilon^ {\mu \nu} r ^ {\lambda} \eta_ {\nu \lambda} = \beta \varepsilon^ {\mu \nu} r ^ {\nu},\tag{6.158}
$$

where $\mu$ and ν run over t and x only, and $\varepsilon _ { \mu \nu }$ is nonzero only for

$$
\varepsilon^ {t x} = + 1, \varepsilon^ {x t} = - 1,\tag{6.159}
$$

as for the case ofrotations. Note that we need the metric factor $\eta _ { \nu \lambda }$ to flip the sign ofthe time transformation to the correct form. This transformation corresponds to an infinitesimal boost in the $r ^ { X } = X$ direction. More generally, Lorentz boosts can be in any of three spatial directions. By symmetry, we can guess that the most general infinitesimal Lorentz boost and spatial rotation must have the form

$$
\delta r ^ {\mu} = \omega^ {\mu \nu} r ^ {\lambda} \eta_ {\nu \lambda} \text {   Lorentz   boosts   and   rotations, }\tag{6.160}
$$

where $\mu$ and $\nu$ now run over $t , x , y ,$ , and $\scriptstyle { Z _ { r } }$ the $\omega ^ { \mu \nu } \mathfrak { s }$ are a set of boost or rotational angle parameters that satisfy the antisymmetry relation

$$
\omega^ {\mu \nu} = - \omega^ {\nu \mu}.\tag{6.161}
$$

For example, if all $\omega ^ { \mu \nu } s$ are zero except for $\omega ^ { x y } = - \omega ^ { y x } = \delta \theta$ , we get rotation about the z axis as in Eq. (6.95); in contrast, if all $\omega ^ { \mu \nu } s$ are zero except for $\omega ^ { t x } = - \omega ^ { x t } = \beta ,$ , we get Eq. (6.158). Correspondingly, $\omega ^ { y z } = - \omega ^ { z y }$ rotates about the x axis, $\omega ^ { x z } = - \omega ^ { z x }$ rotates about the y axis, $\omega ^ { t y } = - \omega ^ { y t }$ boosts in they direction, and $\omega ^ { \mathrm { { z } } } = - \omega ^ { \mathrm { { z } } t }$ boosts in the z direction. We then have a total ofthree rotations and three boosts as needed, packaged into one antisymmetric matrix $\omega ^ { \mu \nu }$

Notice that we cannot have general Lorentz invariance without rotational invariance: otherwise, we can always break the Lorentz boost symmetry by simply realigning the axes by a rotation. To see where the requirement of Lorentz invariance leads us, consider the general change in the action given by Eq. (6.107):

$$
\delta S = \int d \tau \left(\frac {\partial L}{\partial q _ {k}} \Delta q _ {k} + \frac {\partial L}{\partial \dot {q} _ {k}} \frac {d}{d \tau} (\Delta q _ {k}) + \frac {d}{d \tau} (L \delta \tau)\right),\tag{6.162}
$$

where we have traded the t dependence for a dependence on proper time $\tau$ instead, expecting that this will make the analysis cleaner. This means that the action is

$$
S = \int d \tau L,\tag{6.163}
$$

and the dot in ${ \dot { q } } _ { k }$ denotes a derivative with respect to $\tau .$ . We can rearrange Eq. (6.162) into

$$
\delta S = \int d \tau \left(\frac {\partial L}{\partial q _ {k}} \delta q _ {k} + \frac {\partial L}{\partial \dot {q} _ {k}} \frac {d}{d \tau} (\delta q _ {k})\right),\tag{6.164}
$$

where we have used $\delta \tau = 0$ (since proper time is unchanged under Lorentz transformations and rotations) and hence $\delta q _ { k } = \Delta q _ { k } + \dot { q } _ { k } \delta \tau = \Delta q _ { k }$ . Noting that $q _ { k } \to r ^ { \mu }$ , we can then write instead

$$
\delta S = \int d \tau \left(\frac {\partial L}{\partial r ^ {\mu}} \delta r ^ {\mu} + \frac {\partial L}{\partial \dot {r} ^ {\mu}} \frac {d}{d \tau} (\delta r ^ {\mu})\right).\tag{6.165}
$$

We can now read ofthe condition ofLorentz invariance. For example, consider any function of $s \equiv r ^ { \mu } r ^ { \nu } \eta _ { \mu \nu } ;$ that is, say L contains a piece $L \to L ( r ^ { \mu } r ^ { \nu } \eta _ { \mu \nu } )$ . We then get

$$
\frac {\partial L}{\partial r ^ {\mu}} \delta r ^ {\mu} = \frac {\partial L}{\partial s} \frac {\partial s}{\partial r ^ {\mu}} \delta r ^ {\mu} = \frac {\partial L}{\partial s} 2 r ^ {\nu} \eta_ {\mu \nu} \delta r ^ {\mu} = \frac {\partial L}{\partial s} 2 r ^ {\nu} \eta_ {\mu \nu} \omega^ {\mu \alpha} \eta_ {\alpha \beta} r ^ {\beta} = 0.\tag{6.166}
$$

The last statement follows because the product of xs is symmetric while the $\omega ^ { \mu \nu }$ matrix is antisymmetric: the argument is the same one we saw in Eq. (6.142). This mechanism of cancellation is so general that it will apply whenever the Lagrangian depends on mathematical objects that are properly Lorentz contracted: there are no “hanging”Lorentz indices, and pairs of Lorentz indice $\mu$ and $\nu$ ar always summed over through $\eta _ { \mu \nu } .$ We can then easily build Lagrangians L out o $r ^ { \mu } s$ and $d r ^ { \mu } / d \tau \mathsf { s } ,$ as long as we contract the indices properly. The result is guaranteed to be Lorentz invariant. The simplest case is that of a free relativistic particle, for which we have from Eq. (3.71) L = 1 – which obviously works. In Chapte $\ 8 ,$ we will see the case of a charged relativistic particle where the Lorentz invariant form of L will be less trivial.

## Example 6.15

## Sculpting Lagrangians from Symmetry

What if we were to stipulate a particular symmetry and ask for all possible Lagrangians that fit the mold? To be more specific, consider a one-dimensional system with a single degree of freedom, denoted by q(t). We want to ask: What are all possible theories that can describe this system with the conditions that they are Galilean invariant and invariant under time translations? Time translational invariance is easy to handle: we need $\partial { \cal L } / \partial t = 0$ . The Galilean symmetry, however, is obtained from Eq. (6.151) in the previous example:

$$
\delta t = 0 \text {   and   } \delta x = \Delta x = - V t.\tag{6.167}
$$

Substituting this into Eq. (6.107), we get

$$
\delta S = \int d t \left(- \frac {\partial L}{\partial x} V t - \frac {\partial L}{\partial \dot {x}} V\right) = \int d t \frac {d}{d t} K.\tag{6.168}
$$

The question is to find the most general L that does the job for some $K .$ This means we need

$$
\frac {\partial L}{\partial x} t + \frac {\partial L}{\partial \dot {x}} = - \frac {d}{d t} K \equiv \frac {d}{d t} \widetilde {K}.\tag{6.169}
$$

Note also that we are not allowed to use the equations ofmotion while imposing the desired symmetry! Using the chain rule with $\widetilde { K } ( t , x , \dot { x } , \ddot { x } , \ldots )$ , we can write

$$
\frac {d}{d t} \widetilde {K} = \frac {\partial \widetilde {K}}{\partial t} + \frac {\partial \widetilde {K}}{\partial x} \dot {x} + \frac {\partial \widetilde {K}}{\partial \dot {x}} \ddot {x} + \dots .\tag{6.170}
$$

Comparing this to Eq. (6.169), we see that we need $\widetilde { K } ( t , \boldsymbol { x } ) - \mathsf { a }$ function of t and x only – since we know L is a function of $t , \chi ,$ and x˙ only. Therefore we have

$$
\frac {\partial L}{\partial x} t + \frac {\partial L}{\partial \dot {x}} = \frac {\partial \widetilde {K}}{\partial t} + \frac {\partial \widetilde {K}}{\partial x} \dot {x}.\tag{6.171}
$$

We want a general form for L, yet $\widetilde { K } ( t , \boldsymbol { x } )$ is also arbitrary. Since the right-hand side is linear in ${ \dot { X } } ,$ , the left-hand "side must be linear as well. This implies we need L to be a quadratic polynomial in $\dot { x } \mathrm { : }$

$$
L = f _ {1} (x) \dot {x} ^ {2} + f _ {2} (x) \dot {x} + f _ {3} (x),\tag{6.172}
$$

with three unknown functions $f _ { 1 } ( \chi ) , f _ { 2 } ( \chi )$ , and $f _ { 3 } ( \chi )$ . Note that no time dependence is allowed because of time translational symmetry. Looking at the ${ \partial L } / { \partial x } { \sf t e r m } _ { \sf }$ , we can immediately see that we need $\begin{array} { r } { f _ { 1 } ( \boldsymbol { x } ) = C _ { 1 } , } \end{array}$ a constant independent ofx: otherwise we generate a term quadratic inx˙ that does not exist on the right-hand side of Eq. (6.171). Our Lagrangian now looks like

$$
L = C _ {1} \dot {x} ^ {2} + f _ {2} (x) \dot {x} + f _ {3} (x).\tag{6.173}
$$

But the second term is irrelevant to the dynamics. This is because L will appear in the action integrated over time, and this second term can be integrated out:

$$
\int d t f _ {2} (x) \dot {x} = \int d t \frac {d}{d t} \left(F _ {2} (x)\right) = \left. F _ {2} (x) \right| _ {\text { boundaries }}\tag{6.174}
$$

for some function $\begin{array} { r } { F _ { 2 } ( x ) = \int ^ { x } d \xi f _ { 2 } ( \xi ) } \end{array}$ . Hence the term does not depend on the shape of paths plugged into the action functional and cannot contribute to the statement of stationarity – otherwise known as the equation of motion. We are now left with

$$
L \rightarrow C _ {1} \dot {x} ^ {2} + f _ {3} (x).\tag{6.175}
$$

The condition (6.171) on L now looks like

$$
\frac {\partial f _ {3} (x)}{\partial x} t + 2 C _ {1} \dot {x} = \frac {\partial \widetilde {K}}{\partial t} + \frac {\partial \widetilde {K}}{\partial x} \dot {x}.\tag{6.176}
$$

Picking out the x˙ dependences on either side, this implies

$$
2 C _ {1} = \frac {\partial \widetilde {K}}{\partial x}, \frac {\partial f _ {3} (x)}{\partial x} t = \frac {\partial \widetilde {K}}{\partial t}.\tag{6.177}
$$

Since we know that

$$
\frac {\partial^ {2} \widetilde {K}}{\partial x \partial t} = \frac {\partial^ {2} \widetilde {K}}{\partial t \partial x},\tag{6.178}
$$

diferentiating the two equations in (6.177) leads to the condition

$$
\frac {\partial^ {2} f _ {3} (x)}{\partial x ^ {2}} = 0 \Rightarrow f _ {3} (x) = C _ {2} x + C _ {3}\tag{6.179}
$$

for some constants $C _ { 2 }$ and $C _ { 3 }$ . The Lagrangian is now

$$
L = C _ {1} \dot {x} ^ {2} + C _ {2} x,\tag{6.180}
$$

where we set ${ \cal C } _ { 3 } = 0$ since a constant shift of L does not afect the equation of motion. We can now solve for $\widetilde { K }$ as well if we want to, using (6.177):

$$
\widetilde {K} = 2 C _ {1} x + \frac {C _ {2}}{2} t ^ {2} + \text { constant }.\tag{6.181}
$$

Now, let us focus on the important point, which is Eq. (6.180). We write the constant $C _ { 1 }$ and $C _ { 2 }$ as $C _ { 1 } = m / 2$ and $C _ { 2 } = - m g \mathrm { : }$

$$
L = \frac {1}{2} m \dot {x} ^ {2} - m g x.\tag{6.182}
$$

That is, we have shown that the most general Galilean and time translation-invariant mechanics problem in one dimension necessarily looks like a particle in uniform gravity.<sup>a</sup> We were able to derive the canonical kinetic energy term and gravitational potential from a symmetry requirement. This is just a hint at the power of symmetries and conservation laws in physics. Indeed, all the known forces of Nature can be derived from first principles using symmetries!<sup>b</sup>

<sup>a</sup>Or a uniform electrostatic potential or any other potential linear in x.

<sup>b</sup>See for example Quantum Field Theory in a Nutshell by A. Zee, and references therein.

## 6.8 Some Comments on Symmetries

Let us step back for a moment and comment on several additional issues about symmetries and conservation laws.

• If a system has N degrees of freedom, then the typical Lagrangian leads to N second-order differential equations (provided the Lagrangian depends on at most first derivatives of the variables). If we were lucky enough to solve these equations, we would parameterize the solution with 2 N constants related to the boundary conditions. If our system has M symmetries, it would then have M conserved quantities. Each of the symmetries leads to a first-order differentia equation, and hence a total of M constants of motion. In total, the conservation equations will give 2 M constants to parameterize the solution: M from the constants of motion, and another M from integrating the first-order equations. These 2 M constants would necessarily be related to the 2 N constants mentioned earlier. What if we have M = N? The system is then said to be integrable. This means that all one needs to do is write the conservation equations and integrate them. We need not even consider any second-order differential equations to find the solution to the dynamics. In general, we will have $M \leq N ,$ and the closer M is to N, the easier it will be to solve the given physical problem. As soon as an experienced physicist sees a mechanics problem, he or she would first count the degrees of freedom, and then instinctively look for the symmetries and associated conserved charges. This immediately lays out a strategy for how to tackle the problem, based on how many symmetries one has versus the number of degrees of freedom.

• Noether’s theorem is based on infinitesimal transformations: symmetries that can be built up from small incremental steps of deformations. There are other symmetries in Nature that do not fit this prescription. For example, discrete symmetries are rather common. Reflection transformations, e.g., time reflection t → −t or discrete rotations of a lattice, can be very important for understanding the physics of a problem. Noether’s theorem does not apply to these. However, such symmetries are also often associated with conserved quantities. Sometimes, these are called topological conservation laws.

• Infinitesimal transformations can be catalogued rigorously in mathematics. A large and useful class of such transformations fall under the general topic of group theory, more particularly Lie groups. The Lie group catalogue (developed by the French mathematician Élie Cartan) is exhaustive. Many if not all of the entries in the catalogue are indeed realized in Nature in various physical systems.

## 6.9 Summary

In this chapter we presented a technique that allows us to determine constraint forces while working within the Lagrangian formalism. This involved the use of Lagrange multipliers – additional degrees of freedom that one adds to the action. This allows us to formulate a variational principle while being subject to constraints. This approach turns out to be very useful beyond mechanics, from thermodynamics to quantum field theory.

We also encountered a profound formulation of physics, Noether’s theorem, that we can use to organize the subject in terms of a catalogue of symmetries in Nature and corresponding conservation laws. Once again, this topic extends beyond the realm of classical mechanics and pervades throughout our modern understanding of physics.

## Problems

Problem 6.1 A particle ofmass m slides inside a smooth hemispherical bowl ofradius R. Use spherical coordinates r, θ, and φ to describe the dynamics. (a) Write the Lagrangian in terms of generalized coordinates and solve the dynamics. (b) Repeat the exercise using a Lagrange multiplier. What does the multiplier measure in this case?

 Problem 6.2 A pendulum consisting of a ball at the end of a rope swings back and forth in a two-dimensional vertical plane, with the angle θ between the rope and the vertical evolving in time. The rope is pulled upward at a constant rate so that the length l of the pendulum’s arm is decreasing according to dl/dt = −α ≡ constant. (a) Find the Lagrangian for the system with respect to the angle θ. (b) Write the corresponding equations of motion. (c) Repeat parts (a) and (b) using Lagrange multipliers.

Problem 6.3 A particle of mass m slides inside a smooth paraboloid of revolution whose surface is defined by $z = \alpha \rho ^ { 2 }$ , where z and $\rho$ are cylindrical coordinates. (a) Write the Lagrangian for the three-dimensional system using the method of Lagrange multipliers. (b) Find the equations of motion.

Problem 6.4 In certain situations, it is possible to incorporate frictional effects without introducing the dissipation function. As an example, consider the Lagrangian

$$
L = e ^ {\gamma t} \left(\frac {1}{2} m \dot {q} ^ {2} - \frac {1}{2} k q ^ {2}\right).\tag{6.183}
$$

(a) Find the equation of motion for the system. (b) Make the coordinate change $s = e ^ { \gamma t / 2 } q ,$ , and rewrite the dynamics in terms of s. (c) How would you describe the system?

Problem 6.5 A massive particle moves under the acceleration of gravity and without friction on the surface of an inverted cone of revolution with half angle α. (a) Find the Lagrangian in polar coordinates. (b) Provide a complete analysis of the trajectory problem. Do not integrate the final orbit equation, but explore circular orbits in detail.

![](images/019a5cd8338475173725b7a3fc8376641ac416a006afb439cad3a83382c7110e.jpg)  
Problem 6.6 A toy model for our expanding universe during the inflationary epoch consists of a circle of radius $\boldsymbol { r } ( t ) ~ = ~ r _ { 0 } e ^ { \omega t }$ where we are confined to the onedimensional world that is the circle. To probe the physics, imagine two point masses of identical mass m free to move on this circle without friction, connected by a spring of force constant k and relaxed length zero, as depicted in the figure above.

(a) Write the Lagrangian for the two-particle system in terms of the common radial coordinate r, and the two polar coordinates $\theta _ { 1 }$ and $\theta _ { 2 }$ . Do not implement the radial constraint $r ( t ) = r _ { 0 } e ^ { \omega t }$ yet.

(b) Using a Lagrange multiplier for the radial constraint, write four equations describing the dynamics. In this process, show that

$$
a _ {1 r} = 1, \quad a _ {1 t} = - \omega r.\tag{6.184}
$$

(c) Consider the coordinate relabeling

$$
\alpha \equiv \theta_ {1} + \theta_ {2}, \beta \equiv \theta_ {1} - \theta_ {2}.\tag{6.185}
$$

Show that the equations of motion of part (b) for the two angle variables $\theta _ { 1 }$ and $\theta _ { 2 }$ can be rewritten in decoupled form as

$$
\ddot {\alpha} = C _ {1} \dot {\alpha},\tag{6.186}
$$

$$
\ddot {\beta} = C _ {2} \dot {\beta} + C _ {3} \beta ,\tag{6.187}
$$

where $C _ { 1 } , C _ { 2 }$ , and $C _ { 3 }$ are constants that you will need to find.

(d) Identify a symmetry transformation $\{ \delta t , \delta \alpha , \delta \beta \}$ for this system. Find the associated conserved quantity. What would you call this conserved quantity?

(e) Then find $\alpha ( t )$ and $\beta ( t )$ using Eqs. (6.186) and (6.187). Use the boundary conditions

$$
\alpha (0) = \alpha_ {0}, \dot {\alpha} (0) = 0, \beta (0) = 0, \dot {\beta} (0) = C.\tag{6.188}
$$

What is the effect of the expansion on the dynamics? Note: This conclusion is the same as in the more realistic three-dimensional cosmological scenario.

(f) Find the force on the particles exerted by the expansion of the universe. Write this as a function of $\alpha ( t ) , \beta ( t )$ , and $r ( t )$ ; then show that its limiting form for later times in the evolution is given by

$$
2 m \omega^ {2} r (t).\tag{6.189}
$$

![](images/59283d9469c1aecc3562033d3d88f10474c9dca7c14dfdde3c6e4c940bc88f6f.jpg)  
 Problem 6.7 The figure above shows a mass m connected to a spring offorce constant k along a wooden track. The mass is restricted to move along this track without friction. The entire system is mounted on a toy wagon of zero mass resting on a

track along a second frictionless beam. The wagon is connected by a spring offorce constant $\bar { k ^ { \prime } }$ to an axle about which the whole apparatus is spinning with constant angular speed $\omega .$ . The figure is a top-down view, with gravity pointing into the page, and the rest length of each spring is zero. (a) First, write the Lagrangian of the system in terms of the four variables $r , \theta , R ,$ , and Θ shown in the figure, without implementing any constraints. (b) Identify two constraint equations. Implement the one, keeping the two tracks perpendicular to one another in the result of part (a) by eliminating R. Do not implement the constraint causing everything to spin at constant angular speed ω. (c) Introducing a Lagrange multiplier for the constraint having to do with the spin, write four differential equations describing the system. (d) Identify the force on the mass m due to the spin of the system, and find al conditions for which this force vanishes.

![](images/a3e5a7baf6919428929d97304b10438e29d0d89ee6007e3d468661ab1725286a.jpg)  
Problem 6.8 Consider the system shown in the figure above. The particle of mass $m _ { 2 }$ moves on a vertical axis without friction and the entire system rotates about this axis with a constant angular speed Ω. The frictionless joint near the top assures that the three masses always lie in the same plane, and the rods of length a are all rigid. (Hint: Use the origin of your coordinate system at the upper frictionless joint.)

(a) Find the equation of motion in terms of the single degree of freedom θ. (b) Using the method of Lagrange multipliers, find the torque on the masses $m _ { 1 }$ due to the rotational motion. (c) Find a static solution in $\theta$ and identify the corresponding angle in terms of $m _ { 1 }$ , m<sub>2</sub>, g, $^ { a , }$ and Ω. Consider some limits/inequalities in your result and comment on whether they make sense. (d) Is the solution in part (c) stable? If so, what is the frequency of small oscillations about the configuration? (Hint: Use $\xi ~ = ~ \cos \theta$ and work on the Lagrangian instead of the equation of motion.)

Problem 6.9 Find the equations of motion for the example in the text of a wheel chasing a moving target using the nonholonomic constraint.

Problem 6.10 Consider the example of the wheel from the example in the text, except that now we have no control over the wheel’s steering – except of course at time zero. We start the wheel at some position on the plane, give it an initial roll $\omega _ { 0 }$ and an initial spin $\dot { \theta } _ { 0 }$ . Describe the trajectory, assuming that the wheel does not tip away from the vertical.

Problem 6.11 Consider a particle of mass m moving in two dimensions in the x–y plane, constrained to a rail-track whose shape is described by an arbitrary function $y = f ( x )$ . There is no gravity acting on the particle.

(a) Write the Lagrangian in terms of the x degree of freedom only.

(b) Consider some general transformation of the form

$$
\delta x = g (x), \quad \delta t = 0,\tag{6.190}
$$

where $g ( x )$ is an arbitrary function of x. Assuming that this transformation is a symmetry of the system such that $\delta S \ : = \ : 0$ , show that it implies the following differential equation relating $f ( x )$ and $g ( x )$ :

$$
\frac {g ^ {\prime}}{g} = - \frac {1}{2 (1 + f ^ {2})} \frac {d}{d x} \left(f ^ {2}\right),\tag{6.191}
$$

where prime stands for derivative with respect to x (not t).

(c) Write a general expression for the associated conserved charge in terms of $f ( x ) , g ( x )$ , and x˙ .

(d) We will now specify a certain $g ( x )$ , and try to find the laws ofphysics obeying the prescribed symmetry; $i . e .$ , for given $g ( x )$ , we want to find the shape of the railtrack $f ( x )$ . Let

$$
g (x) = \frac {g _ {0}}{\sqrt {x}},\tag{6.192}
$$

where $g _ { 0 }$ is a constant. Find the corresponding $f ( x )$ such that this $g ( x )$ yields a symmetry. Sketch the shape of the rail-track. (Hint: $h ( x ) = f ^ { 2 } . )$

Problem 6.12 One of the most important symmetries in Nature is that of scale invariance. This symmetry is very common $( \mathrm { e . g . }$ , it arises whenever a substance undergoes a phase transition), fundamental (e.g., it is at the foundation of the concept of the renormalization group, for which a physics Nobel Prize was awarded in 1982), and entertaining (as you will now see in this problem).

Consider the action

$$
S = \int d t \sqrt {h} \dot {q} ^ {2}\tag{6.193}
$$

of two degrees of freedom $h ( t )$ and $q ( t )$ .

(a) Show that the following transformation (known as a scale transformation or dilatation)

$$
\delta q = \alpha q, \delta h = - 2 \alpha h, \delta t = \alpha t\tag{6.194}
$$

is a symmetry of this system.

(b) Find the resulting constant of motion.

Problem 6.13 A massive particle moves under the acceleration of gravity and without friction on the surface of an inverted cone of revolution with half angle α.

(a) Find the Lagrangian in polar coordinates.

(b) Provide a complete analysis of the trajectory problem. Use Noether charge when useful.

Problem 6.14 For the two-body central-force problem with a Newtonian potential, the effective two-dimensional orbit dynamics can be described by the Lagrangian

$$
L = \frac {1}{2} \mu (\dot {r} ^ {2} + r ^ {2} \dot {\phi} ^ {2}) + \frac {k}{r} = \frac {1}{2} \mu (\dot {x} ^ {2} + \dot {y} ^ {2}) + \frac {k}{\sqrt {x ^ {2} + y ^ {2}}},\tag{6.195}
$$

where $k > 0$ and we have chosen to use Cartesian coordinates.

(a) Show that the equations of motion become

$$
\mu \ddot {x} = - k \frac {x}{(x ^ {2} + y ^ {2}) ^ {3 / 2}}, \quad \mu \ddot {y} = - k \frac {y}{(x ^ {2} + y ^ {2}) ^ {3 / 2}}.\tag{6.196}
$$

(b) Consider the rotation

$$
\delta x = \alpha y, \quad \delta y = - \alpha x, \quad \delta t = 0\tag{6.197}
$$

for small $\alpha .$ . Show that this is a symmetry of the action.

Problem 6.15 In the previous problem show that the conserved Noether charge associated with the symmetry (6.197) is indeed the angular momentum $| \mathbf { r } \times \mu \mathbf { v } |$ which is naturally entirely in the z direction.

Problem 6.16 The two-body central-force problem we have been dealing with in the previous two problems also has another unexpected and amazing symmetry. Consider the transformation

$$
\delta x = - \frac {\beta}{2} \mu y \dot {y}, \quad \delta y = \frac {\beta}{2} \mu (2 x \dot {y} - y \dot {x}), \quad \delta t = 0\tag{6.198}
$$

for some constant $\beta .$ . This horrific velocity-dependent transformation is a symmetry if and only if the equations of motion (6.196) are satisfied – unlike other symmetries we’ve seen where the equations of motion need not be satisfied. It is said that it is an on-shell symmetry. Show that the change in the Lagrangian resulting from this transformation is given by

$$
\delta L = \beta \mu k \frac {d}{d t} \left(\frac {x}{\sqrt {x ^ {2} + y ^ {2}}}\right).\tag{6.199}
$$

Therefore, it’s a total derivative and generates a symmetry under our generalized definition of a symmetry. (Hint: You will need to use Eqs. (6.196) to get this result.)

Problem 6.17 In the previous problem, show that the conserved charge associated with the symmetry is

$$
Q \propto \mu^ {2} x \dot {y} ^ {2} - \mu^ {2} y \dot {x} \dot {y} - \mu k \frac {x}{\sqrt {x ^ {2} + y ^ {2}}}.\tag{6.200}
$$

Problem 6.18 The hidden symmetry ofthe previous few problems is part ofa twofold transformation – one ofwhich is given by Eqs. (6.198), and another similar one that we have not shown. Together, they result in the conservation of a vector known as the Laplace–Runge–Lenz vector

$$
\mathbf {A} = \mu \mathbf {v} \times (\mathbf {r} \times \mu \mathbf {v}) - \mu k \frac {\mathbf {r}}{r}.\tag{6.201}
$$

Show that (6.200) is the x-component of this more general vector quantity. (Hint: You may find it useful to use the identity $\mathbf { a } \times ( \mathbf { b } \times \mathbf { c } ) = \mathbf { b } ( \mathbf { a } \cdot \mathbf { c } ) - \mathbf { c } ( \mathbf { a } \cdot \mathbf { b } ) . )$ )

Problem 6.19 Show using Eq. (6.201) that

$$
\frac {d \mathbf {A}}{d t} = 0.\tag{6.202}
$$

Draw an elliptical orbit in the x–y plane and show on it the Laplace–Runge– Lenz vector A. The existence of this conserved vector quantity is the reason why one can smoothly deform ellipses into a circle without changing the energy of the system. Mathematically, this additional hidden symmetry implies that the Newtonian problem is equivalent to a free particle on a three-dimensional sphere embedded in an abstract four-dimensional world. It is believed that this is a mathematical accident; no physical significance of this fourth dimension has yet been identified...

![](images/e35056b7f88501003329a57b07d73ed47d1ea692eda1b3139f1d9c874194f35d.jpg)

Problem 6.20 Consider a simple pendulum of mass $m _ { 2 }$ and arm length l having its pivot on a point of support of mass $m _ { 1 }$ that is free to move horizontally on a frictionless rail.

(a) Find the Lagrangian of the system in terms of the two degrees of freedom x and θ shown on the figure above. Do not assume small displacements. (b) Identify two symmetries and the two corresponding conservation laws. Write two first-order differential equations that describe the dynamics of the two degrees of freedom x and θ. Correspondingly, write a single nasty integral for $\theta ( t )$