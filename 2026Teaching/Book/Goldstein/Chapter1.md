## Survey of the Elementary Principles

The motion of material bodies formed the subject of some of the earliest research pursued by the pioneers of physics. From their efforts there has evolved a vast field known as analytical mechanics or dynamics, or simply, mechanics. In the present century the term “classical mechanics” has come into wide use to denote this branch of physics in contradistinction to the newer physical theories, especially quantum mechanics. We shall follow this usage, interpreting the name to include the type of mechanics arising out of the special theory of relativity. It i the purpose of this book to develop the structure of classical mechanics and to outline some of its applications of present-day interest in pure physics. Basic to any presentation of mechanics are a number of fundamental physical concepts, such as space, time, simultaneity, mass, and force. For the most part, however, these concepts will not be analyzed critically here; rather, they will be assumed a undefined terms whose meanings are familiar to the reader.

## 1.1 MECHANICS OF A PARTICLE

Let r be the radius vector of a particle from some given origin and v its vector velocity:

$$
\mathbf {v} = \frac {d \mathbf {r}}{d t}.\tag{1.1}
$$

The linear momentum p of the particle is defined as the product of the particle mass and its velocity:

$$
\mathbf {p} = m \mathbf {v}.\tag{1.2}
$$

In consequence of interactions with external objects and fields, the particle may experience forces of various types, e.g., gravitational or electrodynamic; the vec tor sum of these forces exerted on the particle is the total force F. The mechanics of the particle is contained in Newton’s second law of motion, which states that there exist frames of reference in which the motion of the particle is described by the differential equation

$$
\mathbf {F} = \frac {d \mathbf {p}}{d t} \equiv \dot {\mathbf {p}},\tag{1.3}
$$

Chapter 1 Survey of the Elementary Principles

or

$$
\mathbf {F} = \frac {d}{d t} (m \mathbf {v}).\tag{1.4}
$$

In most instances, the mass of the particle is constant and Eq. (1.4) reduces to

$$
\mathbf {F} = m \frac {d \mathbf {v}}{d t} = m \mathbf {a},\tag{1.5}
$$

where a is the vector acceleration of the particle defined by

$$
\mathbf {a} = \frac {d ^ {2} \mathbf {r}}{d t ^ {2}}.\tag{1.6}
$$

The equation of motion is thus a differential equation of second order, assuming F does not depend on higher-order derivatives

A reference frame in which Eq. (1.3) is valid is called an inertial or Galilean system. Even within classical mechanics the notion of an inertial system is some thing of an idealization. In practice, however, it is usually feasible to set up a co ordinate system that comes as close to the desired properties as may be required. For many purposes, a reference frame fixed in Earth (the “laboratory system”) is a sufficient approximation to an inertial system, while for some astronomica purposes it may be necessary to construct an inertial system (or inertial frame) by reference to distant galaxies.

Many of the important conclusions of mechanics can be expressed in the form of conservation theorems, which indicate under what conditions various mechanical quantities are constant in time. Equation (1.3) directly furnishes the first of these, the

Conservation Theoremfor the Linear Momentum ofa Particle: Ifthe totalforce, F, is zero, then $\dot { \mathbf p } = 0$ and the linear momentum, p, is conserved.

The angular momentum of the particle about point O, denoted by L, is defined as

$$
\mathbf {L} = \mathbf {r} \times \mathbf {p},\tag{1.7}
$$

where r is the radius vector from O to the particle. Notice that the order of the factors is important. We now define the moment offorce or torque about O as

$$
\mathbf {N} = \mathbf {r} \times \mathbf {F}.\tag{1.8}
$$

The equation analogous to (1.3) for N is obtained by forming the cross product o r with Eq. (1.4):

$$
\mathbf {r} \times \mathbf {F} = \mathbf {N} = \mathbf {r} \times \frac {d}{d t} (m \mathbf {v}).\tag{1.9}
$$

## 1.1 Mechanics of a Particle

Equation (1.9) can be written in a different form by using the vector identity:

$$
\frac {d}{d t} (\mathbf {r} \times m \mathbf {v}) = \mathbf {v} \times m \mathbf {v} + \mathbf {r} \times \frac {d}{d t} (m \mathbf {v}),\tag{1.10}
$$

where the first term on the right obviously vanishes. In consequence of this iden tity, Eq. (1.9) takes the form

$$
\mathbf {N} = \frac {d}{d t} (\mathbf {r} \times m \mathbf {v}) = \frac {d \mathbf {L}}{d t} \equiv \dot {\mathbf {L}}.\tag{1.11}
$$

Note that both N and L depend on the point O, about which the moments are taken.

As was the case for Eq. (1.3), the torque equation, (1.11), also yields an immediate conservation theorem, this time the

Conservation Theorem for the Angular Momentum of a Particle: If the total torque, N, is zero then $\dot { \mathbf { L } } = 0 ,$ , and the angular momentum L is conserved

Next consider the work done by the external force F upon the particle in going from point 1 to point 2. By definition, this work is

$$
W _ {1 2} = \int_ {1} ^ {2} \mathbf {F} \cdot d \mathbf {s}.\tag{1.12}
$$

For constant mass (as will be assumed from now on unless otherwise specified), the integral in Eq. (1.12) reduces to

$$
\int \mathbf {F} \cdot d \mathbf {s} = m \int \frac {d \mathbf {v}}{d t} \cdot \mathbf {v} d t = \frac {m}{2} \int \frac {d}{d t} (v ^ {2}) d t,
$$

and therefore

$$
W _ {1 2} = \frac {m}{2} (v _ {2} ^ {2} - v _ {1} ^ {2}).\tag{1.13}
$$

The scalar quantity m $v ^ { 2 } / 2$ is called the kinetic energy of the particle and i denoted by T, so that the work done is equal to the change in the kinetic energy:

$$
W _ {1 2} = T _ {2} - T _ {1}.\tag{1.14}
$$

If the force field is such that the work $W _ { 1 2 }$ is the same for any physically possible path between points 1 and 2, then the force (and the system) is said to be conservative. An alternative description of a conservative system is obtained by imagining the particle being taken from point 1 to point 2 by one possible path and then being returned to point 1 by another path. The independence of $W _ { 1 2 }$ on the particular path implies that the work done around such a closed circuit is zero,

i.e.:

$$
\oint \mathbf {F} \cdot d \mathbf {s} = 0.\tag{1.15}
$$

Physically it is clear that a system cannot be conservative if friction or other dis sipation forces are present, because F ? ds due to friction is always positive and the integral cannot vanish.

By a well-known theorem of vector analysis, a necessary and sufficient condition that the work, $W _ { 1 2 }$ , be independent of the physical path taken by the particle is that F be the gradient of some scalar function of position:

$$
\mathbf {F} = - \nabla V (\mathbf {r}),\tag{1.16}
$$

where V is called the potential, or potential energy. The existence of V can be inferred intuitively by a simple argument. If $W _ { 1 2 }$ is independent of the path o integration between the end points 1 and 2, it should be possible to express $W _ { 1 2 }$ as the change in a quantity that depends only upon the positions of the end points. This quantity may be designated by −V, so that for a differential path length we have the relation

$$
\mathbf {F} \cdot d \mathbf {s} = - d V
$$

or

$$
F _ {s} = - \frac {\partial V}{\partial s},
$$

which is equivalent to Eq. (1.16). Note that in Eq. (1.16) we can add to V any quantity constant in space, without affecting the results. Hence the zero level ofV is arbitrary.

For a conservative system, the work done by the forces is

$$
W _ {1 2} = V _ {1} - V _ {2}.\tag{1.17}
$$

Combining Eq. (1.17) with Eq. (1.14), we have the result

$$
T _ {1} + V _ {1} = T _ {2} + V _ {2},\tag{1.18}
$$

which states in symbols the

Energy Conservation Theorem for a Particle: If the forces acting on a particle are conservative, then the total energy ofthe particle, $T + V _ { \ast }$ , is conserved.

The force applied to a particle may in some circumstances be given by the gradient of a scalar function that depends explicitly on both the position of the particle and the time. However, the work done on the particle when it travels a distance ds,

$$
\mathbf {F} \cdot d \mathbf {s} = - \frac {\partial V}{\partial s} d s,
$$

## 1.2 Mechanics of a System of Particles

is then no longer the total change in −V during the displacement, since V also changes explicitly with time as the particle moves. Hence, the work done as the particle goes from point 1 to point 2 is no longer the difference in the function V between those points. While a total energy $T + V$ may still be defined, it is not conserved during the course of the particle’s motion.

## 1.2 MECHANICS OF A SYSTEM OF PARTICLES

In generalizing the ideas of the previous section to systems of many particles, we must distinguish between the external forces acting on the particles due to sources outside the system, and internal forces on, say, some particle i due to all other particles in the system. Thus, the equation of motion (Newton’s second law) for the i th particle is written as

$$
\sum_ {j} \mathbf {F} _ {j i} + \mathbf {F} _ {i} ^ {(e)} = \dot {\mathbf {p}} _ {i},\tag{1.19}
$$

where $\mathbf { F } _ { i } ^ { ( e ) }$ stands for an external force, and $\mathbf { F } _ { j i }$ is the internal force on the ith particle due to the jth particle $( \mathbf { F } _ { i i }$ , naturally, is zero). We shall assume that the $\mathbf { F } _ { i j }$ (like the $\mathbf { F } _ { i } ^ { ( e ) } )$ ) obey Newton’s third law of motion in its original form: that the forces two particles exert on each other are equal and opposite. This assumption (which does not hold for all types of forces) is sometimes referred to as the weak law ofaction and reaction.

Summed over all particles, Eq. (1.19) takes the form

$$
\frac{d^{2}}{dt^{2}}\sum_{i}m_{i}\mathbf{r}_{i} = \sum_{i}\mathbf{F}_{i}^{(e)} + \sum_{\substack{i,j\\ i\neq j}}\mathbf{F}_{ji}.\tag{1.20}
$$

The first sum on the right is simply the total external force $\mathbf { F } ^ { ( e ) }$ , while the second term vanishes, since the law of action and reaction states that each pair $\mathbf { F } _ { i j } + \mathbf { F } _ { j i }$ is zero. To reduce the left-hand side, we define a vector R as the average of the radii vectors of the particles, weighted in proportion to their mass:

$$
\mathbf {R} = \frac {\sum m _ {i} \mathbf {r} _ {i}}{\sum m _ {i}} = \frac {\sum m _ {i} \mathbf {r} _ {i}}{M}.\tag{1.21}
$$

The vector R defines a point known as the center of mass, or more loosely as the center of gravity, of the system (cf. Fig. 1.1). With this definition, (1.20) reduce to

$$
M \frac {d ^ {2} {\bf R}}{d t ^ {2}} = \sum_ {i} {\bf F} _ {i} ^ {(e)} \equiv {\bf F} ^ {(e)},\tag{1.22}
$$

![](images/f1ed2a861765e526d0208dcd47c5a059bd6f6362dc711ddb6a06b266a74b95f4.jpg)  
FIGURE 1.1 The center of mass of a system of particles.

which states that the center of mass moves as if the total external force were acting on the entire mass of the system concentrated at the center of mass. Purely internal forces, if the obey Newton’s third law, therefore have no effec on the motion of the center of mass. An oft-quoted example is the motion o an exploding shell—the center of mass of the fragments traveling as if the shell were still in a single piece (neglecting air resistance). The same princi ple is involved in jet and rocket propulsion. In order that the motion of the center of mass be unaffected, the ejection of the exhaust gases at high veloc ity must be counterbalanced by the forward motion of the vehicle at a slower velocity.

By Eq. (1.21) the total linear momentum of the system,

$$
\mathbf {P} = \sum m _ {i} \frac {d \mathbf {r} _ {i}}{d t} = M \frac {d \mathbf {R}}{d t},\tag{1.23}
$$

is the total mass of the system times the velocity of the center of mass. Conse quently, the equation of motion for the center of mass, (1.23), can be restated as the

Conservation Theoremfor the Linear Momentum ofa System ofParticles: Ifthe total externalforce is zero, the total linear momentum is conserved.

We obtain the total angular momentum of the system by forming the cross product $\mathbf { r } _ { i } \times \mathbf { p } _ { i }$ and summing over i. If this operation is performed in Eq. (1.19), there results, with the aid of the identity, Eq. (1.10),

$$
\sum_{i}(\mathbf{r}_{i}\times \dot{\mathbf{p}}_{i}) = \sum_{i}\frac{d}{dt} (\mathbf{r}_{i}\times \mathbf{p}_{i}) = \dot{\mathbf{L}} = \sum_{i}\mathbf{r}_{i}\times \mathbf{F}_{i}^{(e)} + \sum_{\substack{i,j\\ i\neq j}}\mathbf{r}_{i}\times \mathbf{F}_{ji}.\tag{1.24}
$$

![](images/b8cf219c2379023313366cade16f4f8ad51d4f68dcc010f611811542e5e2f824.jpg)  
FIGURE 1.2 The vector $\mathbf { r } _ { i j }$ between the ith and jth particles.

The last term on the right in (1.24) can be considered a sum of the pairs of the form

$$
\mathbf {r} _ {i} \times \mathbf {F} _ {j i} + \mathbf {r} _ {j} \times \mathbf {F} _ {i j} = (\mathbf {r} _ {i} - \mathbf {r} _ {j}) \times \mathbf {F} _ {j i},\tag{1.25}
$$

using the equality of action and reaction. But ${ \bf r } _ { i } - { \bf r } _ { j }$ is identical with the vecto $\mathbf { r } _ { i j }$ from j to i (cf. Fig. 1.2), so that the right-hand side of Eq. (1.25) can be written as

$$
\mathbf {r} _ {i j} \times \mathbf {F} _ {j i}.
$$

If the internal forces between two particles, in addition to being equal and opposite, also lie along the line joining the particles—a condition known as the strong law of action and reaction—then all of these cross products vanish. The sum over pairs is zero under this assumption and Eq. (1.24) may be written in the form

$$
\frac {d \mathbf {L}}{d t} = \mathbf {N} ^ {(e)}.\tag{1.26}
$$

The time derivative of the total angular momentum is thus equal to the moment of the external force about the given point. Corresponding to Eq. (1.26) is the

Conservation Theoremfor Total Angular Momentum: L is constant in time ifth applied (external) torque is zero.

(It is perhaps worthwhile to emphasize that this is a vector theorem; i.e., $L _ { z }$ will be conserved if $N _ { z } ^ { ( e ) }$ is zero, even if $N _ { x } ^ { \left( e \right) }$ and $N _ { y } ^ { ( e ) }$ are not zero.)

Note that the conservation of linear momentum in the absence of applied forces assumes that the weak law of action and reaction is valid for the internal forces. The conservation of the total angular momentum of the system in the absence of applied torques requires the validity of the strong law of action and reaction—that the internal forces in addition be central. Many of the familiar physical forces, such as that of gravity, satisfy the strong form of the law. But it is possible to find forces for which action and reaction are equal even though the forces are no central (see below). In a system involving moving charges, the forces between the charges predicted by the Biot-Savart law may indeed violate both forms o the action and reaction law.\* Equations (1.23) and (1.26), and their corresponding conservation theorems, are not applicable in such cases, at least in the form given here. Usually it is then possible to find some generalization of P or L that is conserved. Thus, in an isolated system of moving charges it is the sum of the mechanical angular momentum and the electromagnetic “angular momentum” o the field that is conserved.

Equation (1.23) states that the total linear momentum of the system is the same as if the entire mass were concentrated at the center of mass and moving with it. The analogous theorem for angular momentum is more complicated. With the origin $o$ as reference point, the total angular momentum of the system is

$$
\mathbf {L} = \sum_ {i} \mathbf {r} _ {i} \times \mathbf {p} _ {i}.
$$

Let R be the radius vector from O to the center of mass, and let $\mathbf { r } _ { i } ^ { \prime }$ be the radius vector from the center of mass to the ith particle. Then we have (cf. Fig. 1.3)

$$
\mathbf {r} _ {i} = \mathbf {r} _ {i} ^ {\prime} + \mathbf {R}\tag{1.27}
$$

![](images/d4a71197ade0571cffc1f1e2817d90d461d745bbf760d0d5c0a2850154ce0109.jpg)  
FIGURE 1.3 The vectors involved in the shift of reference point for the angula momentum.

## 1.2 Mechanics of a System of Particles

and

$$
\mathbf {v} _ {i} = \mathbf {v} _ {i} ^ {\prime} + \mathbf {v}
$$

where

$$
\mathbf {v} = \frac {d \mathbf {R}}{d t}
$$

is the velocity of the center of mass relative to $o$ , and

$$
\mathbf {v} _ {i} ^ {\prime} = \frac {d \mathbf {r} _ {i} ^ {\prime}}{d t}
$$

is the velocity of the ith particle relative to the center of mass of the system. Using Eq. (1.27), the total angular momentum takes on the form

$$
\mathbf {L} = \sum_ {i} \mathbf {R} \times m _ {i} \mathbf {v} + \sum_ {i} \mathbf {r} _ {i} ^ {\prime} \times m _ {i} \mathbf {v} _ {i} ^ {\prime} + \left(\sum_ {i} m _ {i} \mathbf {r} _ {i} ^ {\prime}\right) \times \mathbf {v} + \mathbf {R} \times \frac {d}{d t} \sum_ {i} m _ {i} \mathbf {r} _ {i} ^ {\prime}.
$$

The last two terms in this expression vanish, for both contain the factor $\sum m _ { i } \mathbf { r } _ { i } ^ { \prime }$ which, it will be recognized, defines the radius vector of the center of mass in the very coordinate system whose origin is the center of mass and is therefore a null vector. Rewriting the remaining terms, the total angular momentum about O is

$$
\mathbf {L} = \mathbf {R} \times M \mathbf {v} + \sum_ {i} \mathbf {r} _ {i} ^ {\prime} \times \mathbf {p} _ {i} ^ {\prime}.\tag{1.28}
$$

In words, Eq. (1.28) says that the total angular momentum about a point O is the angular momentum of motion concentrated at the center of mass, plus th angular momentum of motion about the center of mass. The form of Eq. (1.28) emphasizes that in general L depends on the origin $o$ , through the vector R. Only if the center of mass is at rest with respect to $o$ will the angular momentum be independent of the point of reference. In this case, the first term in (1.28) vanishes, and L always reduces to the angular momentum taken about the center of mass.

Finally, let us consider the energy equation. As in the case of a single particle, we calculate the work done by all forces in moving the system from an initial configuration 1, to a final configuration 2:

$$
W_{12} = \sum_{i}\int_{1}^{2}\mathbf{F}_{i}\cdot d\mathbf{s}_{i} = \sum_{i}\int_{1}^{2}\mathbf{F}_{i}^{(e)}\cdot d\mathbf{s}_{i} + \sum_{\substack{i,j\\ i\neq j}}\int_{1}^{2}\mathbf{F}_{ji}\cdot d\mathbf{s}_{i}.\tag{1.29}
$$

Again, the equations of motion can be used to reduce the integrals to

$$
\sum_ {i} \int_ {1} ^ {2} \mathbf {F} _ {i} \cdot d \mathbf {s} _ {i} = \sum_ {i} \int_ {1} ^ {2} m _ {i} \dot {\mathbf {v}} _ {i} \cdot \mathbf {v} _ {i} d t = \sum_ {i} \int_ {1} ^ {2} d \left(\frac {1}{2} m _ {i} v _ {i} ^ {2}\right).
$$

Hence, the work done can still be written as the difference of the final and initia kinetic energies:

$$
W _ {1 2} = T _ {2} - T _ {1},
$$

where $T ,$ , the total kinetic energy of the system, is

$$
T = \frac {1}{2} \sum_ {i} m _ {i} v _ {i} ^ {2}.\tag{1.30}
$$

Making use of the transformations to center-of-mass coordinates, given in Eq. (1.27), we may also write $T$ as

$$
\begin{array}{l} T = \frac {1}{2} \sum_ {i} m _ {i} (\mathbf {v} + \mathbf {v} _ {i} ^ {\prime}) \cdot (\mathbf {v} + \mathbf {v} _ {i} ^ {\prime}) \\ = \frac {1}{2} \sum_ {i} m _ {i} v ^ {2} + \frac {1}{2} \sum_ {i} m _ {i} v _ {i} ^ {\prime 2} + \mathbf {v} \cdot \frac {d}{d t} \left(\sum_ {i} m _ {i} \mathbf {r} _ {i} ^ {\prime}\right), \end{array}
$$

and by the reasoning already employed in calculating the angular momentum, the last term vanishes, leaving

$$
T = \frac {1}{2} M v ^ {2} + \frac {1}{2} \sum_ {i} m _ {i} v _ {i} ^ {\prime 2}\tag{1.31}
$$

The kinetic energy, like the angular momentum, thus also consists of two parts: the kinetic energy obtained if all the mass were concentrated at the center of mass, plus the kinetic energy of motion about the center of mass.

Consider now the right-hand side of Eq. (1.29). In the special case that the external forces are derivable in terms of the gradient of a potential, the first term can be written as

$$
\sum_ {i} \int_ {1} ^ {2} \mathbf {F} _ {i} ^ {(e)} \cdot d \mathbf {s} _ {i} = - \sum_ {i} \int_ {1} ^ {2} \nabla_ {i} V _ {i} \cdot d \mathbf {s} _ {i} = - \sum_ {i} V _ {i} \Big | _ {1} ^ {2},
$$

where the subscript i on the del operator indicates that the derivatives are with respect to the components of $\mathbf { r } _ { i }$ . If the internal forces are also conservative, then the mutual forces between the ith and jth particles, $\mathbf { F } _ { i j }$ and $\mathbf { F } _ { j i }$ , can be obtained from a potential function $V _ { i j }$ . To satisfy the strong law of action and reaction, $V _ { i j }$ can be a function only of the distance between the particles:

$$
V _ {i j} = V _ {i j} (| \mathbf {r} _ {i} - \mathbf {r} _ {j} |).\tag{1.32}
$$

The two forces are then automatically equal and opposite,

$$
\mathbf {F} _ {j i} = - \nabla_ {i} V _ {i j} = + \nabla_ {j} V _ {i j} = - \mathbf {F} _ {i j},\tag{1.33}
$$

and lie along the line joining the two particles,

$$
\nabla V _ {i j} (| \mathbf {r} _ {i} - \mathbf {r} _ {j} |) = (\mathbf {r} _ {i} - \mathbf {r} _ {j}) f,\tag{1.34}
$$

where $f$ is some scalar function. If $V _ { i j }$ were also a function of the difference of some other pair of vectors associated with the particles, such as their velocitie or (to step into the domain of modern physics) their intrinsic “spin” angular momenta, then the forces would still be equal and opposite, but would not necessarily lie along the direction between the particles.

When the forces are all conservative, the second term in Eq. (1.29) can be rewritten as a sum over pairs of particles, the terms for each pair being of the form

$$
- \int_ {1} ^ {2} (\nabla_ {i} V _ {i j} \cdot d \mathbf {s} _ {i} + \nabla_ {j} V _ {i j} \cdot d \mathbf {s} _ {j}).
$$

If the difference vector $\mathbf { r } _ { i } - \mathbf { r } _ { j }$ is denoted by $\mathbf { r } _ { i j }$ , and if $\nabla _ { i j }$ stands for the gradient with respect to $\mathbf { r } _ { i j }$ , then

$$
\nabla_ {i} V _ {i j} = \nabla_ {i j} V _ {i j} = - \nabla_ {j} V _ {i j},
$$

and

$$
d \mathbf {s} _ {i} - d \mathbf {s} _ {j} = d \mathbf {r} _ {i} - d \mathbf {r} _ {j} = d \mathbf {r} _ {i j},
$$

so that the term for the ij pair has the form

$$
- \int \nabla_ {i j} V _ {i j} \cdot d \mathbf {r} _ {i j}.
$$

The total work arising from internal forces then reduces to

$$
-\frac{1}{2}\sum_{\substack{i,j\\ i\neq j}}\int_{1}^{2}\nabla_{ij}V_{ij}\cdot d\mathbf{r}_{ij} = -\frac{1}{2}\sum_{\substack{i,j\\ i\neq j}}V_{ij}\bigg|_{1}^{2}.\tag{1.35}
$$

The factor $\frac { 1 } { 2 }$ appears in Eq. (1.35) because in summing over both i and $j$ each member of a given pair is included twice, first in the i summation and then in th j summation.

From these considerations, it is clear that if the external and internal forces are both derivable from potentials it is possible to define a total potential energy, V, of the system,

$$
V = \sum_{i}V_{i} + \frac{1}{2}\sum_{\substack{i,j\\ i\neq j}}V_{ij},\tag{1.36}
$$

such that the total energy $T + V$ is conserved, the analog of the conservation theorem (1.18) for a single particle

The second term on the right in Eq. (1.36) will be called the internal potentia energy of the system. In general, it need not be zero and, more important, it may vary as the system changes with time. Only for the particular class of systems known as rigid bodies will the internal potential always be constant. Formally, a rigid body can be defined as a system of particles in which the distances $r _ { i j }$ are fixed and cannot vary with time. In such case, the vectors $d \mathbf { r } _ { i j }$ can only be perpendicular to the corresponding $\mathbf { r } _ { i j }$ , and therefore to the $\mathbf { F } _ { i j }$ . Therefore, in a rigid body the internal forces do no work, and the internal potential must remain constant. Since the total potential is in any case uncertain to within an additive constant, an unvarying internal potential can be completely disregarded in dis cussing the motion of the system.

## 1.3 CONSTRAINTS

From the previous sections one might obtain the impression that all problems in mechanics have been reduced to solving the set of differential equations (1.19):

$$
m _ {i} \ddot {\mathbf {r}} _ {i} = \mathbf {F} _ {i} ^ {(e)} + \sum_ {j} \mathbf {F} _ {j i}.
$$

One merely substitutes the various forces acting upon the particles of the system, turns the mathematical crank, and grinds out the answers! Even from a purely physical standpoint, however, this view is oversimplified. For example, it may be necessary to take into account the constraints that limit the motion of the system. We have already met one type of system involving constraints, namely rigid bod ies, where the constraints on the motions of the particles keep the distances $r _ { i j }$ unchanged. Other examples of constrained systems can easily be furnished. The beads of an abacus are constrained to one-dimensional motion by the supporting wires. Gas molecules within a container are constrained by the walls of the ves sel to move only inside the container. A particle placed on the surface of a solid sphere is subject to the constraint that it can move only on the surface or in the region exterior to the sphere.

Constraints may be classified in various ways, and we shall use the following system. If the conditions of constraint can be expressed as equations connecting the coordinates of the particles (and possibly the time) having the form

$$
f (\mathbf {r} _ {1}, \mathbf {r} _ {2}, \mathbf {r} _ {3}, \dots , t) = 0,\tag{1.37}
$$

then the constraints are said to be holonomic. Perhaps the simplest example of holonomic constraints is the rigid body, where the constraints are expressed by equations of the form

$$
(\mathbf {r} _ {i} - \mathbf {r} _ {j}) ^ {2} - c _ {i j} ^ {2} = 0.
$$

A particle constrained to move along any curve or on a given surface is another obvious example of a holonomic constraint, with the equations defining the curve or surface acting as the equations of a constraint.

## 1.3 Constraints

Constraints not expressible in this fashion are called nonholonomic. The walls of a gas container constitute a nonholonomic constraint. The constraint involved in the example of a particle placed on the surface of a sphere is also nonholo nomic, for it can be expressed as an inequality

$$
r ^ {2} - a ^ {2} \geq 0
$$

(where $a$ is the radius of the sphere), which is not in the form of (1.37). Thus, in a gravitational field a particle placed on the top of the sphere will slide down the surface part of the way but will eventually fall off.

Constraints are further classified according to whether the equations of con straint contain the time as an explicit variable (rheonomous) or are not explicitly dependent on time (scleronomous). A bead sliding on a rigid curved wire fixed in space is obviously subject to a scleronomous constraint; if the wire is moving in some prescribed fashion, the constraint is rheonomous. Note that if the wire moves, say, as a reaction to the bead’s motion, then the time dependence of the constraint enters in the equation of the constraint only through the coordinates of the curved wire (which are now part of the system coordinates). The overal constraint is then scleronomous.

Constraints introduce two types of difficulties in the solution of mechanica problems. First, the coordinates $r _ { i }$ are no longer all independent, since they are connected by the equations of constraint; hence the equations of motion (1.19) are not all independent. Second, the forces of constraint, e.g., the force that th wire exerts on the bead (or the wall on the gas particle), is not furnished a pri ori. They are among the unknowns of the problem and must be obtained from the solution we seek. Indeed, imposing constraints on the system is simply another method of stating that there are forces present in the problem that cannot be spec ified directly but are known rather in terms of their effect on the motion of th system.

In the case of holonomic constraints, the first difficulty is solved by the introduction of generalized coordinates. So far we have been thinking implicitly in terms of Cartesian coordinates. A system of N particles, free from constraints, has 3N independent coordinates or degrees offreedom. If there exist holonomic constraints, expressed in k equations in the form (1.37), then we may use these equations to eliminate k of the 3N coordinates, and we are left with $3 N - k$ independent coordinates, and the system is said to have $3 N - k$ degrees of freedom. This elimination of the dependent coordinates can be expressed in another way, by the introduction of new, $3 N - k .$ , independent variables $q _ { 1 } , q _ { 2 } , \ldots , q _ { 3 N - k }$ in terms of which the old coordinates $\mathbf { r } _ { 1 } , \mathbf { r } _ { 2 } , \ldots , \mathbf { r } _ { N }$ are expressed by equations of the form

$$
\begin{array}{c} \mathbf {r} _ {1} = \mathbf {r} _ {1} (q _ {1}, q _ {2}, \ldots , q _ {3 N - k}, t) \\ \vdots \\ \mathbf {r} _ {N} = \mathbf {r} _ {N} (q _ {1}, q _ {2}, \ldots , q _ {3 N - k}, t) \end{array}\tag{1.38}
$$

![](images/1f07fe5363efcf8433b07b5ff4a62bef7f1ffbb3a6138a0151337756de60e341.jpg)  
FIGURE 1.4 Double pendulum

containing the constraints in them implicitly. These are transformation equations from the set of $\left( \mathbf { r } _ { l } \right)$ variables to the $( q _ { l } )$ set, or alternatively Eqs. (1.38) can be considered as parametric representations of the $\left( \mathbf { r } _ { l } \right)$ variables. It is always assumed that we can also transform back from the (q ) to the (r ) set, i.e., tha Eqs. (1.38) combined with the k equations of constraint can be inverted to obtain any q as a function of the $( { \bf r } _ { l } )$ variable and time.

Usually the generalized coordinates, $q _ { l }$ , unlike the Cartesian coordinates, wil not divide into convenient groups of three that can be associated together to form vectors. Thus, in the case of a particle constrained to move on the surface of a sphere, the two angles expressing position on the sphere, say latitude and longitude, are obvious possible generalized coordinates. Or, in the example o a double pendulum moving in a plane (two particles connected by an inextensible light rod and suspended by a similar rod fastened to one of the particles), satisfactory generalized coordinates are the two angles $\theta _ { 1 } , \theta _ { 2 }$ . (Cf. Fig. 1.4.) Gen eralized coordinates, in the sense of coordinates other than Cartesian, are often useful in systems without constraints. Thus, in the problem of a particle moving in an external central force field $( V ~ = ~ V ( r ) )$ ), there is no constraint involved, but it is clearly more convenient to use spherical polar coordinates than Cartesian coordinates. Do not, however, think of generalized coordinates in terms of conventional orthogonal position coordinates. All sorts of quantities may be invoked to serve as generalized coordinates. Thus, the amplitudes in a Fourier expansion of $\mathbf { r } _ { j }$ may be used as generalized coordinates, or we may find it convenient to employ quantities with the dimensions of energy or angular momentum.

If the constraint is nonholonomic, the equations expressing the constraint cannot be used to eliminate the dependent coordinates. An oft-quoted example o a nonholonomic constraint is that of an object rolling on a rough surface without slipping. The coordinates used to describe the system will generally involve angular coordinates to specify the orientation of the body, plus a set of coordinates describing the location of the point of contact on the surface. The constrain of “rolling” connects these two sets of coordinates; they are not independent. A change in the position of the point of contact inevitably means a change in

## 1.3 Constraints

![](images/d173e4e71f42702b86aef3556dc384a59bcef14e4f6cb81286d4d331e24f2245.jpg)  
FIGURE 1.5 Vertical disk rolling on a horizontal plane.

its orientation. Yet we cannot reduce the number of coordinates, for the “rolling” condition is not expressible as a equation between the coordinates, in the manner of (1.37). Rather, it is a condition on the velocities (i.e., the point of contact is stationary), a differential condition that can be given in an integrated form only after the problem is solved.

A simple case will illustrate the point. Consider a disk rolling on the horizontal xy plane constrained to move so that the plane of the disk is always vertical. The coordinates used to describe the motion might be the x, y coordinates of the center of the disk, an angle of rotation $\phi$ about the axis of the disk, and an angle θ between the axis of the disk and say, the x axis (cf. Fig 1.5). As a result of the constraint the velocity of the center of the disk, v, has a magnitude proportional to $\dot { \phi }$

$$
v = a \dot {\phi},
$$

where $a$ is the radius of the disk, and its direction is perpendicular to the axis of the disk:

$$
\begin{array}{l} \dot {x} = v \sin \theta , \\ \dot {y} = - v \cos \theta . \end{array}
$$

Combining these conditions, we have two differential equations of constraint:

$$
\begin{array}{l} {d x - a \sin \theta d \phi = 0,} \\ {d y + a \cos \theta d \phi = 0.} \end{array}\tag{1.39}
$$

Neither of Eqs. (1.39) can be integrated without in fact solving the problem; i.e., we cannot find an integrating factor $f ( x , y , \theta , \phi )$ ) that will turn either of the equa tions into exact differentials (cf. Derivation 4).\* Hence, the constraints cannot be reduced to the form of Eq. (1.37) and are therefore nonholonomic. Physically we can see that there can be no direct functional relation between φ and the othe coordinates x, y, and θ by noting that at any point on its path the disk can be made to roll around in a circle tangent to the path and of arbitrary radius. At the end of the process, x, y, and θ have been returned to their original values, bu $\phi$ has changed by an amount depending on the radius of the circle.

Nonintegrable differential constraints of the form of Eqs. (1.39) are of course not the only type of nonholonomic constraints. The constraint conditions may involve higher-order derivatives, or may appear in the form of inequalities, as we have seen.

Partly because the dependent coordinates can be eliminated, problems involv ing holonomic constraints are always amenable to a formal solution. But there is no general way to attack nonholonomic examples. True, if the constraint is nonintegrable, the differential equations of constraint can be introduced into the problem along with the differential equations of motion, and the dependent equations eliminated, in effect, by the method of Lagrange multipliers.

We shall return to this method at a later point. However, the more vicious cases of nonholonomic constraint must be tackled individually, and consequently in the development of the more formal aspects of classical mechanics, it is almost invari ably assumed that any constraint, if present, is holonomic. This restriction does not greatly limit the applicability of the theory, despite the fact that many of the constraints encountered in everyday life are nonholonomic. The reason is that the entire concept of constraints imposed in the system through the medium of wires or surfaces or walls is particularly appropriate only in macroscopic or large-scale problems. But today physicists are more interested in atomic and nuclear prob lems. On this scale all objects, both in and out of the system, consist alike o molecules, atoms, or smaller particles, exerting definite forces, and the notion o constraint becomes artificial and rarely appears. Constraints are then used only as mathematical idealizations to the actual physical case or as classical approximations to a quantum-mechanical property, e.g., rigid body rotations for “spin.” Such constraints are always holonomic and fit smoothly into the framework of the theory.

To surmount the second difficulty, namely, that the forces of constraint are unknown a priori, we should like to so formulate the mechanics that the forces of constraint disappear. We need then deal only with the known applied forces. A hint as to the procedure to be followed is provided by the fact that in a particula system with constraints, i.e., a rigid body, the work done by internal forces (which are here the forces of constraint) vanishes. We shall follow up this clue in the ensuing sections and generalize the ideas contained in it.

## 1.4 D’ALEMBERT’S PRINCIPLE AND LAGRANGE’S EQUATIONS

A virtual (infinitesimal) displacement of a system refers to a change in the con figuration of the system as the result of any arbitrary infinitesimal change of the coordinates $\delta \mathbf { r } _ { i }$ , consistent with theforces and constraints imposed on the system at the given instant t. The displacement is called virtual to distinguish it from an actual displacement of the system occurring in a time interval dt, during which the forces and constraints may be changing. Suppose the system is in equilibrium; i.e., the total force on each particle vanishes, $\mathbf { F } _ { i } = 0$ . Then clearly the dot product $\mathbf { F } _ { i } \cdot \delta \mathbf { r } _ { i }$ , which is the virtual work of the force $\mathbf { F } _ { i }$ in the displacement $\delta \mathbf { r } _ { i }$ , also vanishes. The sum of these vanishing products over all particles must likewise b zero:

$$
\sum_ {i} \mathbf {F} _ {i} \cdot \delta \mathbf {r} _ {i} = 0.\tag{1.40}
$$

As yet nothing has been said that has any new physical content. Decompose $\mathbf { F } _ { i }$ into the applied force, $\mathbf { F } _ { i } ^ { ( a ) }$ , and the force of constraint, $\mathbf { f } _ { i }$ ,

$$
\mathbf {F} _ {i} = \mathbf {F} _ {i} ^ {(a)} + \mathbf {f} _ {i},\tag{1.41}
$$

so that Eq. (1.40) becomes

$$
\sum_ {i} \mathbf {F} _ {i} ^ {(a)} \cdot \delta \mathbf {r} _ {i} + \sum_ {i} \mathbf {f} _ {i} \cdot \delta \mathbf {r} _ {i} = 0.\tag{1.42}
$$

We now restrict ourselves to systems for which the net virtual work of the forces of constraint is zero. We have seen that this condition holds true for rigid bodies and it is valid for a large number of other constraints. Thus, if a particle is constrained to move on a surface, the force of constraint is perpendicular to the surface, while the virtual displacement must be tangent to it, and hence the virtual work vanishes. This is no longer true if sliding friction forces are present, and we must exclude such systems from our formulation. The restriction is not unduly hampering, since the friction is essentially a macroscopic phenomenon. On the other hand, the forces of rolling friction do not violate this condition, since the forces act on a point that is momentarily at rest and can do no work in an infinites imal displacement consistent with the rolling constraint. Note that if a particle i constrained to a surface that is itself moving in time, the force of constraint is instantaneously perpendicular to the surface and the work during a virtual displacement is still zero even though the work during an actual displacement in the time dt does not necessarily vanish.

We therefore have as the condition for equilibrium of a system that the virtual work of the appliedforces vanishes:

$$
\sum_ {i} \mathbf {F} _ {i} ^ {(a)} \cdot \delta \mathbf {r} _ {i} = 0.\tag{1.43}
$$

Equation (1.43) is often called the principle of virtual work. Note that the coefficients of $\delta \mathbf { r } _ { i }$ can no longer be set equal to zero; i.e., in general $\mathbf { F } _ { i } ^ { ( a ) } \neq 0 .$ , since the $\delta \mathbf { r } _ { i }$ are not completely independent but are connected by the constraints. In order to equate the coefficients to zero, we must transform the principle into a form involving the virtual displacements of the $q _ { i }$ , which are independent. Equa tion (1.43) satisfies our needs in that it does not contain the $\mathbf { f } _ { i }$ , but it deals only with statics; we want a condition involving the general motion of the system.

To obtain such a principle, we use a device first thought of by James Bernoull and developed by $\mathbf { D } ^ { \prime }$ Alembert. The equation of motion,

$$
\mathbf {F} _ {i} = \dot {\mathbf {p}} _ {i},
$$

can be written as

$$
\mathbf {F} _ {i} - \dot {\mathbf {p}} _ {i} = 0,
$$

which states that the particles in the system will be in equilibrium under a force equal to the actual force plus a “reversed effective force $\ ' _ { - \dot { \mathbf { p } } _ { i } }$ . Instead of (1.40), we can immediately write

$$
\sum_ {i} (\mathbf {F} _ {i} - \dot {\mathbf {p}} _ {i}) \cdot \delta \mathbf {r} _ {i} = 0,\tag{1.44}
$$

and, making the same resolution into applied forces and forces of constraint, there results

$$
\sum_ {i} (\mathbf {F} _ {i} ^ {(a)} - \dot {\mathbf {p}} _ {i}) \cdot \delta \mathbf {r} _ {i} + \sum_ {i} \mathbf {f} _ {i} \cdot \delta \mathbf {r} _ {i} = 0.
$$

We again restrict ourselves to systems for which the virtual work of the forces o constraint vanishes and therefore obtain

$$
\sum_ {i} (\mathbf {F} _ {i} ^ {(a)} - \dot {\mathbf {p}} _ {i}) \cdot \delta \mathbf {r} _ {i} = 0,\tag{1.45}
$$

which is often called $D ' A$ lembert’s principle. We have achieved our aim, in tha the forces of constraint no longer appear, and the superscript $( a )$ can now be dropped without ambiguity. It is still not in a useful form to furnish equations of motion for the system. We must now transform the principle into an expression involving virtual displacements of the generalized coordinates, which are then independent of each other (for holonomic constraints), so that the coefficients o the $\delta \boldsymbol { q } _ { i }$ can be set separately equal to zero.

The translation from $\mathbf { r } _ { i }$ to $q _ { j }$ language starts from the transformation equations (1.38),

$$
\mathbf {r} _ {i} = \mathbf {r} _ {i} (q _ {1}, q _ {2}, \dots , q _ {n}, t)\tag{1.45'}
$$

(assuming n independent coordinates), and is carried out by means of the usua “chain rules” of the calculus of partial differentiation. Thus, $\mathbf { v } _ { i }$ is expressed in terms of the $\dot { q } _ { k }$ by the formula

$$
\mathbf {v} _ {i} \equiv \frac {d \mathbf {r} _ {i}}{d t} = \sum_ {k} \frac {\partial \mathbf {r} _ {i}}{\partial q _ {k}} \dot {q} _ {k} + \frac {\partial \mathbf {r} _ {i}}{\partial t}.\tag{1.46}
$$

Similarly, the arbitrary virtual displacement $\delta \mathbf { r } _ { i }$ can be connected with the virtua displacements $\delta \boldsymbol { q } _ { i }$ by

$$
\delta \mathbf {r} _ {i} = \sum_ {j} \frac {\partial \mathbf {r} _ {i}}{\partial q _ {j}} \delta q _ {j}.\tag{1.47}
$$

Note that no variation of time, $\delta t .$ , is involved here, since a virtual displacement by definition considers only displacements of the coordinates. (Only then is the virtual displacement perpendicular to the force of constraint if the constraint itself is changing in time.)

In terms of the generalized coordinates, the virtual work of the $\mathbf { F } _ { i }$ becomes

$$
\begin{array}{c} \sum_ {i} \mathbf {F} _ {i} \cdot \delta \mathbf {r} _ {i} = \sum_ {i, j} \mathbf {F} _ {i} \cdot \frac {\partial \mathbf {r} _ {i}}{\partial q _ {j}} \delta q _ {j} \\ = \sum_ {j} Q _ {j} \delta q _ {j}, \end{array}\tag{1.48}
$$

where the $Q _ { j }$ are called the components of the generalizedforce, defined a

$$
Q _ {j} = \sum_ {i} \mathbf {F} _ {i} \cdot \frac {\partial \mathbf {r} _ {i}}{\partial q _ {j}}.\tag{1.49}
$$

Note that just as the $q ^ { * } { \bf s }$ need not have the dimensions of length, so the $\boldsymbol { Q } ^ { \prime } \mathbf { s }$ do not necessarily have the dimensions of force, but $Q _ { j } \delta q _ { j }$ must always have th dimensions of work. For example, $Q _ { j }$ might be a torque $N _ { j }$ and $d q _ { j }$ a differential angle $d \theta _ { j }$ , which makes $N _ { j } d \theta _ { j }$ a differential of work.

We turn now to the other other term involved in Eq. (1.45), which may be written as

$$
\sum_ {i} \dot {\mathbf {p}} _ {i} \cdot \delta \mathbf {r} _ {i} = \sum_ {i} m _ {i} \ddot {\mathbf {r}} _ {i} \cdot \delta \mathbf {r} _ {i}.
$$

Expressing $\delta \mathbf { r } _ { i }$ by (1.47), this becomes

$$
\sum_ {i, j} m _ {i} \ddot {\mathbf {r}} _ {i} \cdot \frac {\partial \mathbf {r} _ {i}}{\partial q _ {j}} \delta q _ {j}.
$$

Consider now the relation

$$
\sum_ {i} m _ {i} \ddot {\mathbf {r}} _ {i} \cdot \frac {\partial \mathbf {r} _ {i}}{\partial q _ {j}} = \sum_ {i} \left[ \frac {d}{d t} \left(m _ {i} \dot {\mathbf {r}} _ {i} \cdot \frac {\partial \mathbf {r} _ {i}}{\partial q _ {j}}\right) - m _ {i} \dot {\mathbf {r}} _ {i} \cdot \frac {d}{d t} \left(\frac {\partial \mathbf {r} _ {i}}{\partial q _ {j}}\right) \right].\tag{1.50}
$$

In the last term of Eq. (1.50) we can interchange the differentiation with respect to t and $q _ { j }$ , for, in analogy to (1.46)

$$
\begin{array}{c} \frac {d}{d t} \left(\frac {\partial \mathbf {r} _ {i}}{\partial q _ {j}}\right) = \frac {\partial \dot {\mathbf {r}} _ {i}}{\partial q _ {j}} = \sum_ {k} \frac {\partial^ {2} \mathbf {r} _ {i}}{\partial q _ {j} \partial q _ {k}} \dot {q} _ {k} + \frac {\partial^ {2} \mathbf {r} _ {i}}{\partial q _ {j} \partial t}, \\ = \frac {\partial \mathbf {v} _ {i}}{\partial q _ {j}}, \end{array}
$$

by Eq. (1.46). Further, we also see from Eq. (1.46) that

$$
\frac {\partial \mathbf {v} _ {i}}{\partial \dot {q} _ {j}} = \frac {\partial \mathbf {r} _ {i}}{\partial q _ {j}}.\tag{1.51}
$$

Substitution of these changes in (1.50) leads to the result that

$$
\sum_ {i} m _ {i} \ddot {\mathbf {r}} _ {i} \cdot \frac {\partial \mathbf {r} _ {i}}{\partial q _ {j}} = \sum_ {i} \left[ \frac {d}{d t} \left(m _ {i} \mathbf {v} _ {i} \cdot \frac {\partial \mathbf {v} _ {i}}{\partial \dot {q} _ {j}}\right) - m _ {i} \mathbf {v} _ {i} \cdot \frac {\partial \mathbf {v} _ {i}}{\partial q _ {j}} \right],
$$

and the second term on the left-hand side of Eq. (1.45) can be expanded into

$$
\sum_ {j} \left\{\frac {d}{d t} \left[ \frac {\partial}{\partial \dot {q} _ {j}} \left(\sum_ {i} \frac {1}{2} m _ {i} v _ {i} ^ {2}\right) \right] - \frac {\partial}{\partial q _ {j}} \left(\sum_ {i} \frac {1}{2} m _ {i} v _ {i} ^ {2}\right) - Q _ {j} \right\} \delta q _ {j}.
$$

Identifying $\textstyle \sum _ { i } { \frac { 1 } { 2 } } m _ { i } v _ { i } ^ { 2 }$ with the system kinetic energy T, D’Alembert’s principle (cf. Eq. (1.45)) becomes

$$
\sum_ {j} \left\{\left[ \frac {d}{d t} \left(\frac {\partial T}{\partial \dot {q} _ {j}}\right) - \frac {\partial T}{\partial q _ {j}} \right] - Q _ {j} \right\} \delta q _ {j} = 0.\tag{1.52}
$$

Note that in a system of Cartesian coordinates the partial derivative of T with respect to $q _ { j }$ vanishes. Thus, speaking in the language of differential geometry, this term arises from the curvature of the coordinates $q _ { j }$ . In polar coordinates, e.g., it is in the partial derivative of $T$ with respect to the angle coordinate that the centripetal acceleration term appears.

Thus far, no restriction has been made on the nature of the constraints other than that they be workless in a virtual displacement. The variables $q _ { j }$ can be any set of coordinates used to describe the motion of the system. If, however, the constraints are holonomic, then it is possible to find sets of independent coordinates $q _ { j }$ that contain the constraint conditions implicitly in the transformation equations (1.38). Any virtual displacement $\delta q _ { j }$ is then independent of $\delta q _ { k }$ , and therefore the only way for (1.52) to hold is for the individual coefficients to vanish:

$$
\frac {d}{d t} \left(\frac {\partial T}{\partial \dot {q} _ {j}}\right) - \frac {\partial T}{\partial q _ {j}} = Q _ {j}.\tag{1.53}
$$

There are n such equations in all.

When the forces are derivable from a scalar potential function V,

$$
\mathbf {F} _ {i} = - \nabla_ {i} V.
$$

Then the generalized forces can be written as

$$
Q _ {j} = \sum_ {i} \mathbf {F} _ {i} \cdot \frac {\partial \mathbf {r} _ {i}}{\partial q _ {j}} = - \sum_ {i} \nabla_ {i} V \cdot \frac {\partial \mathbf {r} _ {i}}{\partial q _ {j}},
$$

which is exactly the same expression for the partial derivative of a function $- V ( \mathbf { r } _ { 1 } , \mathbf { r } _ { 2 } , \ldots , \mathbf { r } _ { N } , t )$ with respect to $q _ { j } .$ :

$$
Q _ {j} \equiv - \frac {\partial V}{\partial q _ {j}}.\tag{1.54}
$$

See Eq. (1.47). Equations (1.53) can then be rewritten as

$$
\frac {d}{d t} \left(\frac {\partial T}{\partial \dot {q} _ {j}}\right) - \frac {\partial (T - V)}{\partial q _ {j}} = 0.\tag{1.55}
$$

The equations of motion in the form (1.55) are not necessarily restricted to conservative systems; only if V is not an explicit function of time is the system conserva tive (cf. p. 4). As here defined, the potential V does not depend on the generalized velocities. Hence, we can include a term in V in the partial derivative with respect to ${ \dot { q } } _ { j }$ :

$$
\frac {d}{d t} \left(\frac {\partial (T - V)}{\partial \dot {q} _ {j}}\right) - \frac {\partial (T - V)}{\partial q _ {j}} = 0.
$$

$\mathrm { O r } ,$ defining a new function, the Lagrangian $L ,$ as

$$
L = T - V,\tag{1.56}
$$

the Eqs. (1.53) become

$$
\frac {d}{d t} \left(\frac {\partial L}{\partial \dot {q} _ {j}}\right) - \frac {\partial L}{\partial q _ {j}} = 0,\tag{1.57}
$$

expressions referred to as “Lagrange’s equations.”

Note that for a particular set of equations of motion there is no unique choice of Lagrangian such that Eqs. (1.57) lead to the equations of motion in the given generalized coordinates. Thus, in Derivations 8 and 10 it is shown that if $L ( q , \dot { q } , t )$ is an approximate Lagrangian and $F ( q , t )$ is any differentiable function of the generalized coordinates and time, then

$$
L ^ {\prime} (q, \dot {q}, t) = L (q, \dot {q}, t) + \frac {d F}{d t}\tag{1.57'}
$$

is a Lagrangian also resulting in the same equations of motion. It is also often possible to find alternative Lagrangians beside those constructed by this prescription (see Exercise 20). While Eq. (1.56) is always a suitable way to construct a Lagrangian for a conservative system, it does not provide the only Lagrangian suitable for the given system.

## 1.5 VELOCITY-DEPENDENT POTENTIALS AND THE DISSIPATION FUNCTION

Lagrange’s equations can be put in the form (1.57) even if there is no potential function, V, in the usual sense, providing the generalized forces are obtained from a function $U ( q _ { j } , \dot { q } _ { j } )$ by the prescription

$$
Q _ {j} = - \frac {\partial U}{\partial q _ {j}} + \frac {d}{d t} \left(\frac {\partial U}{\partial \dot {q} _ {j}}\right).\tag{1.58}
$$

In such case, Eqs. (1.57) still follow from Eqs. (1.53) with the Lagrangian given by

$$
L = T - U.\tag{1.59}
$$

Here U may be called a “generalized potential,” or “velocity-dependent poten tial.” The possibility of using such a “potential” is not academic; it applies to one very important type of force field, namely, the electromagnetic forces on moving charges. Considering its importance, a digression on this subject is well worth while.

Consider an electric charge, q, of mass m moving at a velocity, v, in an otherwise charge-free region containing both an electric field, E, and a magnetic field, B, which may depend upon time and position. The charge experiences a force, called the Lorentz force, given by

$$
\mathbf {F} = q \left[ \mathbf {E} + (\mathbf {v} \times \mathbf {B}) \right].\tag{1.60}
$$

Both $\mathbf { E } ( x , y , z , t )$ and $\mathbf { B } ( x , y , z , t )$ are continuous functions of time and position derivable from a scalar potential $\phi ( x , y , z , t )$ and a vector potential ${ \bf A } ( x , y , z , t )$ by

$$
\mathbf {E} = - \nabla \phi - \frac {\partial \mathbf {A}}{\partial t}\tag{1.61a}
$$

and

$$
\mathbf {B} = \nabla \times \mathbf {A}.\tag{1.61b}
$$

The force on the charge can be derived from the following velocity-dependen potential energy

$$
U = q \phi - q \mathbf {A} \cdot \mathbf {v},\tag{1.62}
$$

so the Lagrangian, $L = T - U$ , is

$$
L = \frac {1}{2} m v ^ {2} - q \phi + q \mathbf {A} \cdot \mathbf {v}.\tag{1.63}
$$

Considering just the x-component of Lagrange’s equations gives

$$
m \ddot {x} = q \left(v _ {x} \frac {\partial A _ {x}}{\partial x} + v _ {y} \frac {\partial A _ {y}}{\partial x} + v _ {z} \frac {\partial A _ {z}}{\partial x}\right) - q \left(\frac {\partial \phi}{\partial x} + \frac {d A _ {x}}{d t}\right).\tag{1.64}
$$

The total time derivative of $A _ { x }$ is related to the partial time derivative through

$$
\begin{array}{r l} \frac {d A _ {x}}{d t} & = \frac {\partial A _ {x}}{\partial t} + \mathbf {v} \cdot \nabla A _ {x} \\ & = \frac {\partial A _ {x}}{\partial t} + v _ {x} \frac {\partial A _ {x}}{\partial x} + v _ {y} \frac {\partial A _ {x}}{\partial y} + v _ {z} \frac {\partial A _ {x}}{\partial z}. \end{array}\tag{1.65}
$$

Equation (1.61b) gives

$$
(\mathbf {v} \times \mathbf {B}) _ {x} = v _ {y} \left(\frac {\partial A _ {y}}{\partial x} - \frac {\partial A _ {x}}{\partial y}\right) + v _ {z} \left(\frac {\partial A _ {z}}{\partial x} - \frac {\partial \mathrm{A} _ {x}}{\partial z}\right).
$$

Combining these expressions gives the equation of motion in the x-direction

$$
m \ddot {x} = q \left[ \mathrm{E} _ {x} + (\mathbf {v} \times \mathbf {B}) _ {x} \right].\tag{1.66}
$$

On a component-by-component comparison, Eqs. (1.66) and (1.60) are identical, showing that the Lorentz force equation is derivable from Eqs. (1.61) and (1.62).

Note that if not all the forces acting on the system are derivable from a poten tial, then Lagrange’s equations can always be written in the form

$$
\frac {d}{d t} \left(\frac {\partial L}{\partial \dot {q} _ {j}}\right) - \frac {\partial L}{\partial q _ {j}} = Q _ {j},
$$

where L contains the potential of the conservative forces as before, and $Q _ { j }$ represents the forces not arising from a potential. Such a situation often occurs when frictional forces are present. It frequently happens that the frictional force is pro portional to the velocity of the particle, so that its x-component has the form

$$
F _ {f x} = - k _ {x} v _ {x}.
$$

Frictional forces of this type may be derived in terms of a function ${ \mathcal F } ,$ , known as Rayleigh’s dissipationfunction, and defined as

$$
\mathcal {F} = \frac {1}{2} \sum_ {i} \left(k _ {x} v _ {i x} ^ {2} + k _ {y} v _ {i y} ^ {2} + k _ {z} v _ {i z} ^ {2}\right),\tag{1.67}
$$

where the summation is over the particles of the system. From this definition it is clear that

$$
F _ {f _ {x _ {i}}} = - \frac {\partial \mathcal {F}}{\partial v _ {x _ {i}}},
$$

or, symbolically,

$$
\mathbf {F} _ {f} = - \nabla_ {v} \mathcal {F}.\tag{1.68}
$$

We can also give a physical interpretation to the dissipation function. The work done by the system against friction is

$$
d W _ {f} = - \mathbf {F} _ {f} \cdot d \mathbf {r} = - \mathbf {F} _ {f} \cdot \mathbf {v} d t = \left(k _ {x} v _ {x} ^ {2} + k _ {y} v _ {y} ^ {2} + k _ {z} v _ {z} ^ {2}\right) d t.
$$

Hence, $2 \mathcal { F }$ is the rate of energy dissipation due to friction. The component of the generalized force resulting from the force of friction is then given by

$$
Q _ {j} = \sum_ {i} \mathbf {F} _ {f _ {i}} \cdot \frac {\partial \mathbf {r} _ {i}}{\partial q _ {j}} = - \sum \nabla_ {v} \mathcal {F} \cdot \frac {\partial \mathbf {r} _ {i}}{\partial q _ {j}}
$$

Chapter 1 Survey of the Elementary Principles

$$
\begin{array}{l} = - \sum \nabla_ {v} \mathcal {F} \cdot \frac {\partial \dot {\mathbf {r}} _ {i}}{\partial \dot {q} _ {j}}, \quad \text { by   (1.51) }, \\ = - \frac {\partial \mathcal {F}}{\partial \dot {q} _ {j}}. \end{array}\tag{1.69}
$$

An example is Stokes’ law, whereby a sphere of radius a moving at a speed v, in a medium of viscosity η experiences the frictional drag force $\mathbf { F } _ { f } = - 6 \pi \eta a \mathbf { v }$ The Lagrange equations with dissipation become

$$
\frac {d}{d t} \left(\frac {\partial L}{\partial \dot {q} _ {j}}\right) - \frac {\partial L}{\partial q _ {j}} + \frac {\partial \mathcal {F}}{\partial \dot {q} _ {j}} = 0,\tag{1.70}
$$

so that two scalar functions, $L$ and ${ \mathcal { F } } _ { : }$ , must be specified to obtain the equations of motion.

## 1.6 SIMPLE APPLICATIONS OF THE LAGRANGIAN FORMULATION

The previous sections show that for systems where we can define a Lagrangian, i.e., holonomic systems with applied forces derivable from an ordinary or gen eralized potential and workless constraints, we have a very convenient way o setting up the equations of motion. We were led to the Lagrangian formulation by the desire to eliminate the forces of constraint from the equations of motion, and in achieving this goal we have obtained many other benefits. In setting up the original form of the equations of motion, Eqs. (1.19), it is necessary to work with many vector forces and accelerations. With the Lagrangian method we only dea with two scalar functions, T and V, which greatly simplifies the problem.

A straightforward routine procedure can now be established for all problems of mechanics to which the Lagrangian formulation is applicable. We have only to write T and V in generalized coordinates, form L from them, and substitute in (1.57) to obtain the equations of motion. The needed transformation of T and V from Cartesian coordinates to generalized coordinates is obtained by applying the transformation equations (1.38) and (1.45<sup></sup>). Thus, T is given in general by

$$
T = \sum_ {i} \frac {1}{2} m _ {i} v _ {i} ^ {2} = \sum_ {i} \frac {1}{2} m _ {i} \left(\sum_ {j} \frac {\partial \mathbf {r} _ {i}}{\partial q _ {j}} \dot {q} _ {j} + \frac {\partial \mathbf {r} _ {i}}{\partial t}\right) ^ {2}.
$$

It is clear that on carrying out the expansion, the expression for T in generalized coordinates will have the form

$$
T = M _ {0} + \sum_ {j} M _ {j} \dot {q} _ {j} + \frac {1}{2} \sum_ {j, k} M _ {j k} \dot {q} _ {j} \dot {q} _ {k},\tag{1.71}
$$

where $M _ { 0 } , M _ { j } , M _ { j k }$ are definite functions of the $\mathbf { r } ^ { \ } \mathbf { s }$ and t and hence of the $q ^ { * } { \bf s }$ and t. In fact, a comparison shows that

$$
M _ {0} = \sum_ {i} \frac {1}{2} m _ {i} \left(\frac {\partial \mathbf {r} _ {i}}{\partial t}\right) ^ {2},
$$

1.6 Simple Applications of the Lagrangian Formulation

$$
M _ {j} = \sum_ {i} m _ {i} \frac {\partial \mathbf {r} _ {i}}{\partial t} \cdot \frac {\partial \mathbf {r} _ {i}}{\partial q _ {j}},\tag{1.72}
$$

and

$$
M _ {j k} = \sum_ {i} m _ {i} \frac {\partial \mathbf {r} _ {i}}{\partial q _ {j}} \cdot \frac {\partial \mathbf {r} _ {i}}{\partial q _ {k}}.
$$

Thus, the kinetic energy of a system can always be written as the sum of three homogeneous functions of the generalized velocities,

$$
T = T _ {0} + T _ {1} + T _ {2},\tag{1.73}
$$

where $T _ { 0 }$ is independent of the generalized velocities, $T _ { 1 }$ is linear in the velocities, and $T _ { 2 }$ is quadratic in the velocities. If the transformation equations do not contain the time explicitly, as may occur when the constraints are independent of time (scleronomous), then only the last term in Eq. (1.71) is nonvanishing, and $T$ is always a homogeneous quadratic form in the generalized velocities.

Let us now consider simple examples of this procedure:

1. Single particle in space

(a) Cartesian coordinates

(b) Plane polar coordinates

2. Atwood’s machine

3. Time-dependent constraint—bead sliding on rotating wire

1. (a) Motion of one particle: using Cartesian coordinates. The generalized forces needed in Eq. (1.53) are obviously $F _ { x } , F _ { y }$ , and $F _ { z }$ . Then

$$
T = \frac {1}{2} m \big (\dot {x} ^ {2} + \dot {y} ^ {2} + \dot {z} ^ {2} \big),
$$

$$
\frac {\partial T}{\partial x} = \frac {\partial T}{\partial y} = \frac {\partial T}{\partial z} = 0,
$$

$$
\frac {\partial T}{\partial \dot {x}} = m \dot {x}, \quad \frac {\partial T}{\partial \dot {y}} = m \dot {y}, \quad \frac {\partial T}{\partial \dot {z}} = m \dot {z},
$$

and the equations of motion are

$$
\frac {d}{d t} (m \dot {x}) = F _ {x}, \quad \frac {d}{d t} (m \dot {y}) = F _ {y}, \quad \frac {d}{d t} (m \dot {z}) = F _ {z}.\tag{1.74}
$$

We are thus led back to the original Newton’s equations of motion.

(b) Motion of one particle: using plane polar coordinates. Here we must express T in terms of $\dot { r }$ and $\dot { \theta } .$ . The transformation equations, Eqs. (1.38), are

$$
x = r \cos \theta
$$

$$
y = r \sin \theta .
$$

By analogy to (1.46), the velocities are given by

$$
\begin{array}{l} \dot {x} = \dot {r} \cos \theta - r \dot {\theta} \sin \theta , \\ \dot {y} = \dot {r} \sin \theta + r \dot {\theta} \cos \theta . \end{array}
$$

The kinetic energy $T = { \textstyle \frac { 1 } { 2 } } m ( { \dot { x } } ^ { 2 } + { \dot { y } } ^ { 2 } )$ then reduces formally to

$$
T = \frac {1}{2} m \left[ \dot {r} ^ {2} + (r \dot {\theta}) ^ {2} \right].\tag{1.75}
$$

An alternative derivation of Eq. (1.75) is obtained by recognizing that the plane polar components of the velocity are $\dot { r }$ along r, and $r { \dot { \theta } }$ along the direction perpendicular to $r ,$ , denoted by the unit vector $\begin{array} { r } { \hat { \pmb { \theta } } . } \end{array}$ . Hence, the square of the velocity expressed in polar coordinates is simply $\dot { r } ^ { 2 } + ( r \dot { \theta } ) ^ { 2 }$ . With the aid of the expression

$$
d \mathbf {r} = \hat {\mathbf {r}} d r + r \hat {\pmb {\theta}} d \theta + \hat {\mathbf {k}} d z
$$

for the differential position vector, $d \mathbf { r } ,$ , in cylindrical coordinates, restricted to the plane $\mathbf { z } = 0$ where rˆ and $\hat { \pmb { \theta } }$ are unit vectors in the r and u-directions, respec tively, the components of the generalized force can be obtained from the defini tion, Eq. (1.49),

$$
\begin{array}{l} Q _ {r} = \mathbf {F} \cdot \frac {\partial \mathbf {r}}{\partial r} = \mathbf {F} \cdot \hat {\mathbf {r}} = F _ {r}, \\ Q _ {\theta} = \mathbf {F} \cdot \frac {\partial \mathbf {r}}{\partial \theta} = \mathbf {F} \cdot r \hat {\boldsymbol {\theta}} = r F _ {\theta}, \end{array}
$$

since the derivative of r with respect to $\theta$ is, by the definition of a derivative, a vector in the direction of $\hat { \theta }$ (cf. Fig. 1.6). There are two generalized coordinates, and therefore two Lagrange equations. The derivatives occurring in the r equation are

$$
\frac {\partial T}{\partial r} = m r \dot {\theta} ^ {2}, \quad \frac {\partial T}{\partial \dot {r}} = m \dot {r}, \quad \frac {d}{d t} \left(\frac {\partial T}{\partial \dot {r}}\right) = m \ddot {r},
$$

![](images/b468def038130187a78e961e04a7d001a893ac06c1da3127638d726e06229da8.jpg)  
FIGURE 1.6 Derivative of r with respect to $\theta .$

## 1.6 Simple Applications of the Lagrangian Formulation

and the equation itself is

$$
m \ddot {r} - m r \dot {\theta} ^ {2} = F _ {r},
$$

the second term being the centripetal acceleration term. For the $\theta$ equation, we have the derivatives

$$
\frac {\partial T}{\partial \theta} = 0, \quad \frac {\partial T}{\partial \dot {\theta}} = m r ^ {2} \dot {\theta}, \quad \frac {d}{d t} (m r ^ {2} \dot {\theta}) = m r ^ {2} \ddot {\theta} + 2 m r \dot {r} \dot {\theta},
$$

so that the equation becomes

$$
\frac {d}{d t} \left(m r ^ {2} \dot {\theta}\right) = m r ^ {2} \ddot {\theta} + 2 m r \dot {r} \dot {\theta} = r F _ {\theta}.
$$

Note that the left side of the equation is just the time derivative of the angular momentum, and the right side is exactly the applied torque, so that we have simply rederived the torque equation (1.26), where $L = m r ^ { 2 } { \dot { \theta } }$ and $N ^ { ( e ) } = r F _ { \theta }$

2. Atwood’s machine—(See Fig. 1.7) an example of a conservative system with holonomic, scleronomous constraint (the pulley is assumed frictionless and massless). Clearly there is only one independent coordinate x, the position of the other weight being determined by the constraint that the length of the rop between them is l. The potential energy is

$$
V = - M _ {1} g x - M _ {2} g (l - x),
$$

while the kinetic energy is

$$
T = \frac {1}{2} (M _ {1} + M _ {2}) \dot {x} ^ {2}.
$$

![](images/bf1cb6a6d6b8090453add86348285a4af941d76caf3f547fdf74997fcf989667.jpg)  
FIGURE 1.7 Atwood’s machine

Combining the two, the Lagrangian has the form

$$
L = T - V = \frac {1}{2} (M _ {1} + M _ {2}) \dot {x} ^ {2} + M _ {1} g x + M _ {2} g (l - x).
$$

There is only one equation of motion, involving the derivatives

$$
\frac {\partial L}{\partial x} = (M _ {1} - M _ {2}) g,
$$

$$
\frac {\partial L}{\partial \dot {x}} = (M _ {1} + M _ {2}) \dot {x},
$$

so that we have

$$
(M _ {1} + M _ {2}) \ddot {x} = (M _ {1} - M _ {2}) g,
$$

or

$$
\ddot {x} = \frac {M _ {1} - M _ {2}}{M _ {1} + M _ {2}} g,
$$

which is the familiar result obtained by more elementary means. This trivial problem emphasizes that the forces of constraint—here the tension in the rope— appear nowhere in the Lagrangian formulation. By the same token, neither can the tension in the rope be found directly by the Lagrangian method.

3. A bead (or ring) sliding on a uniformly rotating wire in a force-free space. The wire is straight, and is rotated uniformly about some fixed axis perpendicular to the wire. This example has been chosen as a simple illustration of a constrain being time dependent, with the rotation axis along z and the wire in the xy plane. The transformation equations explicitly contain the time.

$$
\begin{array}{l l} x = r \cos \omega t, & (\omega = \text { angular   velocity   of   rotation }) \\ y = r \sin \omega t. & (r = \text { distance   along   wire   from   rotation   axis }) \end{array}
$$

While we could then find T (here the same as L) by the same procedure used to obtain (1.71), it is simpler to take over (1.75) directly, expressing the constrain by the relation $\dot { \theta } = \omega \colon$

$$
T = \frac {1}{2} m \big (\dot {r} ^ {2} + r ^ {2} \omega^ {2} \big).
$$

Note that T is not a homogeneous quadratic function of the generalized velocities, since there is now a term not involving r˙. The equation of motion is then

$$
m \ddot {r} - m r \omega^ {2} = 0
$$

or

$$
\ddot {r} = r \omega^ {2},
$$

which is the familiar simple harmonic oscillator equation with a change of sign. The solution $\textbf { \textit { r } } = \textbf { \textit { e } } ^ { \omega t }$ for a bead initially at rest on the wire shows that the bead moves exponentially outwards. Again, the method cannot furnish the force of constraint that keeps the bead on the wire. Equation (1.26) with the angular momentum, $L = m r ^ { \hat { 2 } } \omega = m \omega r _ { 0 } ^ { 2 } e ^ { 2 \omega t }$ , provides the force $F = N / r$ , which produces the constraint force, $F = 2 m r _ { 0 } \omega ^ { 2 } e ^ { \omega t }$ , acting perpendicular to the wire and the axis of rotation.

## DERIVATIONS

1. Show that for a single particle with constant mass the equation of motion implies the following differential equation for the kinetic energy:

$$
\frac {d T}{d t} = \mathbf {F} \cdot \mathbf {v},
$$

while if the mass varies with time the corresponding equation is

$$
{\frac {d (m T)}{d t}} = \mathbf {F} \cdot \mathbf {p}.
$$

2. Prove that the magnitude R of the position vector for the center of mass from an arbitrary origin is given by the equation

$$
M ^ {2} R ^ {2} = M \sum_ {i} m _ {i} r _ {i} ^ {2} - \frac {1}{2} \sum_ {i \neq j} m _ {i} m _ {j} r _ {i j} ^ {2}.
$$

3. Suppose a system of two particles is known to obey the equations of motion, Eqs. (1.22) and (1.26). From the equations of the motion of the individual parti cles show that the internal forces between particles satisfy both the weak and the strong laws of action and reaction. The argument may be generalized to a system with arbitrary number of particles, thus proving the converse of the arguments leading to Eqs. (1.22) and (1.26).

4. The equations of constraint for the rolling disk, Eqs. (1.39), are special cases of general linear differential equations of constraint of the form

$$
\sum_ {i = 1} ^ {n} g _ {i} (x _ {1}, \ldots , x _ {n}) d x _ {i} = 0.
$$

A constraint condition of this type is holonomic only if an integrating function $f ( x _ { 1 } , \ldots , x _ { n } )$ can be found that turns it into an exact differential. Clearly the function must be such that

$$
\frac {\partial (f g _ {i})}{\partial x _ {j}} = \frac {\partial (f g _ {j})}{\partial x _ {i}}
$$

for all $i \neq j$ . Show that no such integrating factor can be found for either of Eqs. (1.39).

5. Two wheels of radius a are mounted on the ends of a common axle of length b such that the wheels rotate independently. The whole combination rolls without slipping on a plane. Show that there are two nonholonomic equations of constraint,

$$
\cos \theta d x + \sin \theta d y = 0
$$

$$
\sin \theta d x - \cos \theta d y = \frac {1}{2} a (d \phi + d \phi^ {\prime}),
$$

(where θ, φ, and $\phi ^ { \prime }$ have meanings similar to those in the problem of a single vertica disk, and $( x , y )$ are the coordinates of a point on the axle midway between the two wheels) and one holonomic equation of constraint,

$$
\theta = C - \frac {a}{b} (\phi - \phi^ {\prime}),
$$

where C is a constant.

6. A particle moves in the xy plane under the constraint that its velocity vector is always directed towards a point on the x axis whose abscissa is some given function of time $f ( t )$ . Show that for $f ( t )$ differentiable, but otherwise arbitrary, the constraint is non holonomic.

7. Show that Lagrange’s equations in the form of Eqs. (1.53) can also be written as

$$
\frac {\partial \dot {T}}{\partial \dot {q} _ {j}} - 2 \frac {\partial T}{\partial q _ {j}} = Q _ {j}.
$$

These are sometimes known as the Nielsen form of the Lagrange equations.

8. If L is a Lagrangian for a system of n degrees of freedom satisfying Lagrange’s equa tions, show by direct substitution that

$$
L ^ {\prime} = L + \frac {d F (q _ {1} , \ldots , q _ {n} , t)}{d t}
$$

also satisfies Lagrange’s equations where F is any arbitrary, but differentiable, func tion of its arguments.

9. The electromagnetic field is invariant under a gauge transformation of the scalar and vector potential given by

$$
\begin{array}{l} \mathbf {A} \to \mathbf {A} + \nabla \psi (\mathbf {r}, \mathbf {t}), \\ \phi \to \phi - \frac {1}{c} \frac {\partial \psi}{\partial t}, \end{array}
$$

where $\psi$ is arbitrary (but differentiable). What effect does this gauge transformation have on the Lagrangian of a particle moving in the electromagnetic field? Is the motion affected?

10. Let $q _ { 1 } , \ldots , q _ { n }$ be a set of independent generalized coordinates for a system of n degrees of freedom, with a Lagrangian $L ( q , { \dot { q } } , t )$ . Suppose we transform to anothe set of independent coordinates $s _ { 1 } , \ldots , s _ { n }$ by means of transformation equation

$$
q _ {i} = q _ {i} (s _ {1}, \ldots , s _ {n}, t), \qquad i = 1, \ldots , n.
$$

(Such a transformation is called a point transformation.) Show that if the Lagrangian function is expressed as a function of $s _ { j } , \dot { s } _ { j }$ , and t through the equations of transfor mation, then L satisfies Lagrange’s equations with respect to the s coordinates:

$$
\frac {d}{d t} \left(\frac {\partial L}{\partial \dot {s} _ {j}}\right) - \frac {\partial L}{\partial s _ {j}} = 0.
$$

In other words, the form of Lagrange’s equations is invariant under a point transfor mation.

## EXERCISES

11. Check whether the force $\vec { F } = y z \hat { i } + z x \hat { j } + x y \hat { k }$ is conservative or not

12. Compute the orbital period and orbital angular velocity of a satellite revolving around the Earth at an altitude of 720 km. [Given: radius of Earth $R \ = \ 6 0 0 0$ km and $g = 9 . 8 3 \mathrm { m } / \mathrm { s } ^ { 2 } . ]$

13. Rockets are propelled by the momentum reaction of the exhaust gases expelled from the tail. Since these gases arise from the reaction of the fuels carried in the rocket, the mass of the rocket is not constant, but decreases as the fuel is expended. Show that the equation of motion for a rocket projected vertically upward in a uniform gravitational field, neglecting atmospheric friction, is

$$
m \frac {d v}{d t} = - v ^ {\prime} \frac {d m}{d t} - m g,
$$

where m is the mass of the rocket and $v ^ { \prime }$ is the velocity of the escaping gases relative to the rocket. Integrate this equation to obtain v as a function of m, assuming a constant time rate of loss of mass. Show, for a rocket starting initially from rest, with $v ^ { \prime }$ equal to 2.1 km/s and a mass loss per second equal to 1/60th of the initial mass, that in order to reach the escape velocity the ratio of the weight of the fuel to the weight of the empty rocket must be almost 300!

14. Two points of mass m are joined by a rigid weightless rod of length l, the center of which is constrained to move on a circle of radius a. Express the kinetic energy in generalized coordinates.

15. A point particle moves in space under the influence of a force derivable from a generalized potential of the form

$$
U (\mathbf {r}, \mathbf {v}) = V (r) + \boldsymbol {\sigma} \cdot \mathbf {L},
$$

where r is the radius vector from a fixed point, L is the angular momentum about that point, and s is a fixed vector in space.

(a) Find the components of the force on the particle in both Cartesian and spherical polar coordinates, on the basis of Eq. (1.58).

(b) Show that the components in the two coordinate systems are related to each other as in Eq. (1.49).

(c) Obtain the equations of motion in spherical polar coordinates.

16. A particle moves in a plane under the influence of a force, acting toward a center of force, whose magnitude is

$$
F = \frac {1}{r ^ {2}} \left(1 - \frac {\dot {r} ^ {2} - 2 \ddot {r} r}{c ^ {2}}\right),
$$

where r is the distance of the particle to the center of force. Find the generalized potential that will result in such a force, and from that the Lagrangian for the motion in a plane. (The expression for $F$ represents the force between two charges in Weber’s electrodynamics.)

17. A nucleus, originally at rest, decays radioactively by emitting an electron of momen tum 1.73 MeV/c, and at right angles to the direction of the electron a neutrino with momentum 1.00 MeV/c. (The MeV, million electron volt, is a unit of energy used in modern physics, equal to $1 . 6 0 \times 1 0 ^ { - 1 3 } \ : \mathrm { { J } }$ J. Correspondingly, MeV/c is a unit of lin ear momentum equal to $5 . 3 4 \times 1 0 ^ { - 2 2 } \mathrm { k g \cdot m / s } . )$ In what direction does the nucleus recoil? What is its momentum in MeV/c? If the mass of the residual nucleus is $3 . 9 0 \times 1 0 ^ { - 2 5 }$ kg what is its kinetic energy, in electron volts?

18. A Lagrangian for a particular physical system can be written as

$$
L ^ {\prime} = \frac {m}{2} \left(a \dot {x} ^ {2} + 2 b \dot {x} \dot {y} + c \dot {y} ^ {2}\right) - \frac {K}{2} \left(a x ^ {2} + 2 b x y + c y ^ {2}\right),
$$

where $a , b ,$ , and c are arbitrary constants but subject to the condition tha $b ^ { 2 } - a c \neq 0 .$ What are the equations of motion? Examine particularly the two cases $a = 0 = c$ and $b = 0 , c = - a$ . What is the physical system described by the above Lagrangian? Show that the usual Lagrangian for this system as defined by Eq. (1.56) is related to $L ^ { \prime }$ by a point transformation (cf. Derivation 10). What is the significance of the condition on the value of $b ^ { 2 } - a c ?$

19. Obtain the Lagrange equations of motion for a spherical pendulum, i.e., a mass poin suspended by a rigid weightless rod.

20. A particle of mass m moves in one dimension such that it has the Lagrangian

$$
L = \frac {m ^ {2} \dot {x} ^ {4}}{1 2} + m \dot {x} ^ {2} V (x) - V ^ {2} (x),
$$

where V is some differentiable function of x. Find the equation of motion for $x ( t )$ ) and describe the physical nature of the system on the basis of this equation.

21. Two mass points of mass $m _ { 1 }$ and $m _ { 2 }$ are connected by a string passing through a hole in a smooth table so that $m _ { 1 }$ rests on the table surface and $m _ { 2 }$ hangs suspended. Assuming $m _ { 2 }$ moves only in a vertical line, what are the generalized coordinates fo the system? Write the Lagrange equations for the system and, if possible, discuss the physical significance any of them might have. Reduce the problem to a single second-order differential equation and obtain a first integral of the equation. What is its physical significance? (Consider the motion only until $m _ { 1 }$ reaches the hole.)

22. Obtain the Lagrangian and equations of motion for the double pendulum illustrated in Fig. 1.4, where the lengths of the pendula are $l _ { 1 }$ and $l _ { 2 }$ with corresponding masses $m _ { 1 }$ and $m _ { 2 }$

23. Two masses 2 kg and 3 kg, respectively, are tied to the two ends of a massless, inextensible string passing over a smooth pulley. When the system is released, calculate the acceleration of the masses and the tension in the string.

24. A spring of rest length $L _ { a }$ (no tension) is connected to a support at one end and has a mass M attached at the other. Neglect the mass of the spring, the dimension of the mass M, and assume that the motion is confined to a vertical plane. Also, assume tha the spring only stretches without bending but it can swing in the plane.

(a) Using the angular displacement of the mass from the vertical and the length that the string has stretched from its rest length (hanging with the mass m), find Lagrange’s equations.

(b) Solve these equations for small stretching and angular displacements.

(c) Solve the equations in part (a) to the next order in both stretching and angula displacement. This part is amenable to hand calculations. Using some reasonable assumptions about the spring constant, the mass, and the rest length, discuss the motion. Is a resonance likely under the assumptions stated in the problem?

(d) (For analytic computer programs.) Consider the spring to have a total mass $m \ \ll \ M$ . Neglecting the bending of the spring, set up Lagrange’s equations correctly to first order in m and the angular and linear displacements.

(e) (For numerical computer analysis.) Make sets of reasonable assumptions of the constants in part (a) and make a single plot of the two coordinates as functions of time.

