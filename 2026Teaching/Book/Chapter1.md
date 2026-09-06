# Newton's Laws of Motion

## 1.1 Classical Mechanics

Mechanics is the study of how things move: how planets move around the sun, how a skier moves down the slope, or how an electron moves around the nucleus of an atom. So far as we know, the Greeks were the first to think seriously about mechanics, more than two thousand years ago, and the Greeks' mechanics represents a tremendous step in the evolution of modern science. Nevertheless, the Greek ideas were, by modern standards, seriously flawed and need not concern us here. The development of the mechanics that we know today began with the work of Galileo (1564–1642) and Newton (1642–1727), and it is the formulation of Newton, with his three laws of motion, that will be our starting point in this book.

In the late eighteenth and early nineteenth centuries, two alternative formulations of mechanics were developed, named for their inventors, the French mathematician and astronomer Lagrange (1736–1813) and the Irish mathematician Hamilton (1805–1865). The Lagrangian and Hamiltonian formulations of mechanics are completely equivalent to that of Newton, but they provide dramatically simpler solutions to many complicated problems and are also the taking-off point for various modern developments. The term classical mechanics is somewhat vague, but it is generally understood to mean these three equivalent formulations of mechanics, and it is in this sense that the subject of this book is called classical mechanics.

Until the beginning of the twentieth century, it seemed that classical mechanics was the only kind of mechanics, correctly describing all possible kinds of motion. Then, in the twenty years from 1905 to 1925, it became clear that classical mechanics did not correctly describe the motion of objects moving at speeds close to the speed of light, nor that of the microscopic particles inside atoms and molecules. The result was the development of two completely new forms of mechanics: relativistic mechanics to describe very high-speed motions and quantum mechanics to describe the motion of microscopic particles. I have included an introduction to relativity in the “optional” Chapter 15. Quantum mechanics requires a whole separate book (or several books), and I have made no attempt to give even a brief introduction to quantum mechanics.

Although classical mechanics has been replaced by relativistic mechanics and by quantum mechanics in their respective domains, there is still a vast range of interesting and topical problems in which classical mechanics gives a complete and accurate description of the possible motions. In fact, particularly with the advent of chaos theory in the last few decades, research in classical mechanics has intensified and the subject has become one of the most fashionable areas in physics. The purpose of this book is to give a thorough grounding in the exciting field of classical mechanics. When appropriate, I shall discuss problems in the framework of the Newtonian formulation, but I shall also try to emphasize those situations where the newer formulations of Lagrange and Hamilton are preferable and to use them when this is the case. At the level of this book, the Lagrangian approach has many significant advantages over the Newtonian, and we shall be using the Lagrangian formulation repeatedly, starting in Chapter 7. By contrast, the advantages of the Hamiltonian formulation show themselves only at a more advanced level, and I shall postpone the introduction of Hamiltonian mechanics to Chapter 13 (though it can be read at any point after Chapter 7).

In writing the book, I took for granted that you have had an introduction to Newtonian mechanics of the sort included in a typical freshman course in “General Physics.” This chapter contains a brief review of the ideas that I assume you have met before.

## 1.2 Space and Time

Newton's three laws of motion are formulated in terms of four crucial underlying concepts: the notions of space, time, mass, and force. This section reviews the first two of these, space and time. In addition to a brief description of the classical view of space and time, I give a quick review of the machinery of vectors, with which we label the points of space.

## Space

Each point P of the three-dimensional space in which we live can be labeled by a position vector r which specifies the distance and direction of P from a chosen origin O as in Figure 1.1. There are many different ways to identify a vector, of which one of the most natural is to give its components $(x, y, z)$ in the directions of three chosen perpendicular axes. One popular way to express this is to introduce three unit vectors, $\hat{x}, \hat{y}, \hat{z}$ , pointing along the three axes and to write

$$
\mathbf {r} = x \hat {\mathbf {x}} + y \hat {\mathbf {y}} + z \hat {\mathbf {z}}.\tag{1.1}
$$

In elementary work, it is probably wise to choose a single good notation, such as (1.1), and stick with it. In more advanced work, however, it is almost impossible to avoid using several different notations. Different authors have different preferences (another popular choice is to use i, j, k for what I am calling $\hat{x}$ , $\hat{y}$ , $\hat{z}$ ) and you must get used to reading them all. Furthermore, almost every notation has its drawbacks, which can make it unusable in some circumstances. Thus, while you may certainly choose your preferred scheme, you need to develop a tolerance for several different schemes.

![](images/c87676d37176a2c31051bf56bf968aa66c56d42f3d109debe525535f63d1d2b9.jpg)  
Figure 1.1 The point P is identified by its position vector r, which gives the position of P relative to a chosen origin O. The vector r can be specified by its components $(x, y, z)$ relative to chosen axes Oxyz.

It is sometimes convenient to be able to abbreviate (1.1) by writing simply

$$
\mathbf {r} = (x, y, z).\tag{1.2}
$$

This notation is obviously not quite consistent with (1.1), but it is usually completely unambiguous, asserting simply that $\mathbf{r}$ is the vector whose components are $x, y, z$ . When the notation of (1.2) is the most convenient, I shall not hesitate to use it. For most vectors, we indicate the components by subscripts $x, y, z$ . Thus the velocity vector $\mathbf{v}$ has components $v_x, v_y, v_z$ and the acceleration $\mathbf{a}$ has components $a_x, a_y, a_z$ .

As our equations become more complicated, it is sometimes inconvenient to write out all three terms in sums like (1.1); one would rather use the summation sign $\sum$ followed by a single term. The notation of (1.1) does not lend itself to this shorthand, and for this reason I shall sometimes relabel the three components x, y, z of r as $r_{1}, r_{2}, r_{3}$ , and the three unit vectors $\hat{x}, \hat{y}, \hat{z}$ as $e_{1}, e_{2}, e_{3}$ . That is, we define

$$
r _ {1} = x, \qquad r _ {2} = y, \qquad r _ {3} = z,
$$

and

$$
\mathbf {e} _ {1} = \hat {\mathbf {x}}, \qquad \mathbf {e} _ {2} = \hat {\mathbf {y}}, \qquad \mathbf {e} _ {3} = \hat {\mathbf {z}}.
$$

(The symbol e is commonly used for unit vectors, since e stands for the German “eins” or “one.”) With these notations, (1.1) becomes

$$
\mathbf {r} = r _ {1} \mathbf {e} _ {1} + r _ {2} \mathbf {e} _ {2} + r _ {3} \mathbf {e} _ {3} = \sum_ {i = 1} ^ {3} r _ {i} \mathbf {e} _ {i}.\tag{1.3}
$$

For a simple equation like this, the form (1.3) has no real advantage over (1.1), but with more complicated equations (1.3) is significantly more convenient, and I shall use this notation when appropriate.

## Vector Operations

In our study of mechanics, we shall make repeated use of the various operations that can be performed with vectors. If r and s are vectors with components

$$
\mathbf {r} = (r _ {1}, r _ {2}, r _ {3}) \qquad \text { and } \qquad \mathbf {s} = (s _ {1}, s _ {2}, s _ {3}),
$$

then their sum (or resultant) $\mathbf{r} + \mathbf{s}$ is found by adding corresponding components, so that

$$
\mathbf {r} + \mathbf {s} = (r _ {1} + s _ {1}, r _ {2} + s _ {2}, r _ {3} + s _ {3}).\tag{1.4}
$$

(You can convince yourself that this rule is equivalent to the familiar triangle and parallelogram rules for vector addition.) An important example of a vector sum is the resultant force on an object: When two forces $\mathbf{F}_a$ and $\mathbf{F}_b$ act on an object, the effect is the same as a single force, the resultant force, which is just the vector sum

$$
\mathbf {F} = \mathbf {F} _ {a} + \mathbf {F} _ {b}
$$

as given by the vector addition law (1.4).

If $c$ is a scalar (that is, an ordinary number) and $\mathbf{r}$ is a vector, the product $cr$ is given by

$$
c \mathbf {r} = (c r _ {1}, c r _ {2}, c r _ {3}).\tag{1.5}
$$

This means that $\mathbf{cr}$ is a vector in the same direction $^1$ as $\mathbf{r}$ with magnitude equal to $c$ times the magnitude of $\mathbf{r}$ . For example, if an object of mass $m$ (a scalar) has an acceleration $\mathbf{a}$ (a vector), Newton's second law asserts that the resultant force $\mathbf{F}$ on the object will always equal the product $ma$ as given by (1.5).

There are two important kinds of product that can be formed from any pair of vectors. First, the scalar product (or dot product) of two vectors $\mathbf{r}$ and $\mathbf{s}$ is given by either of the equivalent formulas

$$
\mathbf {r} \cdot \mathbf {s} = r s \cos \theta
$$

$$
= r _ {1} s _ {1} + r _ {2} s _ {2} + r _ {3} s _ {3} = \sum_ {n = 1} ^ {3} r _ {n} s _ {n}\tag{1.6}
$$

(1.7)

where $r$ and $s$ denote the magnitudes of the vectors $\mathbf{r}$ and $\mathbf{s}$ , and $\theta$ is the angle between them. (For a proof that these two definitions are the same, see Problem 1.7.) For example, if a force $\mathbf{F}$ acts on an object that moves through a small displacement $d\mathbf{r}$ , the work done by the force is the scalar product $\mathbf{F} \cdot d\mathbf{r}$ , as given by either (1.6) or (1.7). Another important use of the scalar product is to define the magnitude of a vector: The magnitude (or length) of any vector $\mathbf{r}$ is denoted by $|\mathbf{r}|$ or $r$ and, by Pythagoras's theorem is equal to $\sqrt{r_1^2 + r_2^2 + r_3^2}$ . By (1.7) this is the same as

$$
r = | \mathbf {r} | = \sqrt {\mathbf {r} \cdot \mathbf {r}}.\tag{1.8}
$$

The scalar product $r \cdot r$ is often abbreviated as $r^{2}$ .

The second kind of product of two vectors r and s is the vector product (or cross product), which is defined as the vector $p = r \times s$ with components

$$
\left. \begin{array}{l} p _ {x} = r _ {y} s _ {z} - r _ {z} s _ {y} \\ p _ {y y} = r _ {z} s _ {x} - r _ {x} s _ {z} \\ p _ {z} = r _ {x} s _ {y} - r _ {y} s _ {x} \end{array} \right\}\tag{1.9}
$$

or, equivalently

$$
\mathbf {r} \times \mathbf {s} = \det \left[ \begin{array}{c c c} \hat {\mathbf {x}} & \hat {\mathbf {y}} & \hat {\mathbf {z}} \\ r _ {x} & r _ {y} & r _ {z} \\ s _ {x} & s _ {y} & s _ {z} \end{array} \right],
$$

where “det” stands for the determinant. Either of these definitions implies that $r \times s$ is a vector perpendicular to both r and s, with direction given by the familiar right-hand rule and magnitude $rs \sin \theta$ (Problem 1.15). The vector product plays an important role in the discussion of rotational motion. For example, the tendency of a force F (acting at a point r) to cause a body to rotate about the origin is given by the torque of F about O, defined as the vector product $\Gamma = r \times F$ .

## Differentiation of Vectors

Many (maybe most) of the laws of physics involve vectors, and most of these involve derivatives of vectors. There are so many ways to differentiate a vector that there is a whole subject called vector calculus, much of which we shall be developing in the course of this book. For now, I shall mention just the simplest kind of vector derivative, the time derivative of a vector that depends on time. For example, the velocity $\mathbf{v}(t)$ of a particle is the time derivative of the particle's position $\mathbf{r}(t)$ ; that is, $v = d\mathbf{r}/dt$ . Similarly the acceleration is the time derivative of the velocity, $a = d\mathbf{v}/dt$ .

The definition of the derivative of a vector is closely analogous to that of a scalar. Recall that if $x(t)$ is a scalar function of t, then we define its derivative as

$$
\frac {d x}{d t} = \lim _ {\Delta t \rightarrow 0} \frac {\Delta x}{\Delta t}
$$

where $\Delta x = x(t + \Delta t) - x(t)$ is the change in x as the time advances from t to $t + \Delta t$ . In exactly the same way, if $\mathbf{r}(t)$ is any vector that depends on t, we define its derivative as

$$
\frac {d \mathbf {r}}{d t} = \lim _ {\Delta t \rightarrow 0} \frac {\Delta \mathbf {r}}{\Delta t}\tag{1.10}
$$

where

$$
\Delta \mathbf {r} = \mathbf {r} (t + \Delta t) - \mathbf {r} (t)\tag{1.11}
$$

is the corresponding change in $\mathbf{r}(t)$ . There are, of course, many delicate questions about the existence of this limit. Fortunately, none of these need concern us here: All of the vectors we shall encounter will be differentiable, and you can take for granted that the required limits exist. From the definition (1.10), one can prove that the derivative has all of the properties one would expect. For example, if $\mathbf{r}(t)$ and $\mathbf{s}(t)$

are two vectors that depend on $t$ , then the derivative of their sum is just what you would expect:

$$
{\frac {d}{d t}} (\mathbf {r} + \mathbf {s}) = {\frac {d \mathbf {r}}{d t}} + {\frac {d \mathbf {s}}{d t}}.\tag{1.12}
$$

Similarly, if $\mathbf{r}(t)$ is a vector and $f(t)$ is a scalar, then the derivative of the product $f(t)\mathbf{r}(t)$ is given by the appropriate version of the product rule,

$$
{\frac {d}{d t}} (f \mathbf {r}) = f {\frac {d \mathbf {r}}{d t}} + {\frac {d f}{d t}} \mathbf {r}.\tag{1.13}
$$

If you are the sort of person who enjoys proving these kinds of proposition, you might want to show that they follow from the definition (1.10). Fortunately, if you do not enjoy this kind of activity, you don't need to worry, and you can safely take these results for granted.

One more result that deserves mention concerns the components of the derivative of a vector. Suppose that $\mathbf{r}$ , with components $x, y, z$ , is the position of a moving particle, and suppose that we want to know the particle's velocity $\mathbf{v} = d\mathbf{r}/dt$ . When we differentiate the sum

$$
\mathbf {r} = x \hat {\mathbf {x}} + y \hat {\mathbf {y}} + z \hat {\mathbf {z}},\tag{1.14}
$$

the rule (1.12) gives us the sum of the three separate derivatives, and, by the product rule (1.13), each of these contains two terms. Thus, in principle, the derivative of (1.14) involves six terms in all. However, the unit vectors $\hat{x}$ , $\hat{y}$ , and $\hat{z}$ do not depend on time, so their time derivatives are zero. Therefore, three of these six terms are zero, and we are left with just three terms:

$$
\frac {d \mathbf {r}}{d t} = \frac {d x}{d t} \hat {\mathbf {x}} + \frac {d y}{d t} \hat {\mathbf {y}} + \frac {d z}{d t} \hat {\mathbf {z}}.\tag{1.15}
$$

Comparing this with the standard expansion

$$
\mathbf {v} = v _ {x} \hat {\mathbf {x}} + v _ {y} \hat {\mathbf {y}} + v _ {z} \hat {\mathbf {z}}
$$

we see that

$$
v _ {x} = \frac {d x}{d t}, \quad v _ {y} = \frac {d y}{d t}, \quad \text { and } \quad v _ {z} = \frac {d z}{d t}.\tag{1.16}
$$

In words, the rectangular components of v are just the derivatives of the corresponding components of r. This is a result that we use all the time (usually without even thinking about it) in solving elementary mechanics problems. What makes it especially noteworthy is this: It is true only because the unit vectors $\hat{x}$ , $\hat{y}$ , and $\hat{z}$ are constant, so that their derivatives are absent from (1.15). We shall find that in most coordinate systems, such as polar coordinates, the basic unit vectors are not constant, and the result corresponding to (1.16) is appreciably less transparent. In problems where we need to work in nonrectangular coordinates, it is considerably harder to write down velocities and accelerations in terms of the coordinates of r, as we shall see.

## Time

The classical view is that time is a single universal parameter t on which all observers agree. That is, if all observers are equipped with accurate clocks, all properly synchronized, then they will all agree as to the time at which any given event occurred. We know, of course, that this view is not exactly correct: According to the theory of relativity, two observers in relative motion do not agree on all times. Nevertheless, in the domain of classical mechanics, with all speeds much much less than the speed of light, the differences among the measured times are entirely negligible, and I shall adopt the classical assumption of a single universal time (except, of course, in Chapter 15 on relativity). Apart from the obvious ambiguity in the choice of the origin of time (the time that we choose to label t = 0), all observers agree on the times of all events.

## Reference Frames

Almost every problem in classical mechanics involves a choice (explicit or implicit) of a reference frame, that is, a choice of spatial origin and axes to label positions as in Figure 1.1 and a choice of temporal origin to measure times. The difference between two frames may be quite minor. For instance, they may differ only in their choice of the origin of time — what one frame labels t = 0 the other may label $t' = t_{0} \neq 0$ . Or the two frames may have the same origins of space and time, but have different orientations of the three spatial axes. By carefully choosing your reference frame, taking advantage of these different possibilities, you can sometimes simplify your work. For example, in problems involving blocks sliding down inclines, it often helps to choose one axis pointing down the slope.

A more important difference arises when two frames are in relative motion; that is, when one origin is moving relative to the other. In Section 1.4 we shall find that not all such frames are physically equivalent. $^{2}$ In certain special frames, called inertial frames, the basic laws hold true in their standard, simple form. (It is because one of these basic laws is Newton's first law, the law of inertia, that these frames are called inertial.) If a second frame is accelerating or rotating relative to an inertial frame, then this second frame is noninertial, and the basic laws — in particular, Newton's laws — do not hold in their standard form in this second frame. We shall find that the distinction between inertial and noninertial frames is central to our discussion of classical mechanics. It plays an even more explicit role in the theory of relativity.

## 1.3 Mass and Force

The concepts of mass and force are central to the formulation of classical mechanics. The proper definitions of these concepts have occupied many philosophers of science and are the subject of learned treatises. Fortunately we don't need to worry much about these delicate questions here. Based on your introductory course in general physics, you have a reasonably good idea what mass and force mean, and it is easy to describe how these parameters are defined and measured in many realistic situations.

![](images/6a7529c4d47d9637291ba296d02bbe00f08c6b47e867cdccd5180ff95d2e0804.jpg)  
Figure 1.2 An inertial balance compares the masses $m_{1}$ and $m_{2}$ of two objects that are attached to the opposite ends of a rigid rod. The masses are equal if and only if a force applied at the rod's midpoint causes them to accelerate at the same rate, so that the rod does not rotate.

## Mass

The mass of an object characterizes the object's inertia — its resistance to being accelerated: A big boulder is hard to accelerate, and its mass is large. A little stone is easy to accelerate, and its mass is small. To make these natural ideas quantitative we have to define a unit of mass and then give a prescription for measuring the mass of any object in terms of the chosen unit. The internationally agreed unit of mass is the kilogram and is defined arbitrarily to be the mass of a chunk of platinum-iridium stored at the International Bureau of Weights and Measures outside Paris. To measure the mass of any other object, we need a means of comparing masses. In principle, this can be done with an inertial balance as shown in Figure 1.2. The two objects to be compared are fastened to the opposite ends of a light, rigid rod, which is then given a sharp pull at its midpoint. If the masses are equal, they will accelerate equally and the rod will move off without rotating; if the masses are unequal, the more massive one will accelerate less, and the rod will rotate as it moves off.

The beauty of the inertial balance is that it gives us a method of mass comparison that is based directly on the notion of mass as resistance to being accelerated. In practice, an inertial balance would be very awkward to use, and it is fortunate that there are much easier ways to compare masses, of which the easiest is to weigh the objects. As you certainly recall from your introductory physics course, an object's mass is found to be exactly proportional to the object's weight $^{3}$ (the gravitational force on the object) provided all measurements are made in the same location. Thus two objects have the same mass if and only if they have the same weight (when weighed at the same place), and a simple, practical way to check whether two masses are equal is simply to weigh them and see if their weights are equal.

Armed with methods for comparing masses, we can easily set up a scheme to measure arbitrary masses. First, we can build a large number of standard kilograms, each one checked against the original 1-kg mass using either the inertial or gravitational balance. Next, we can build multiples and fractions of the kilogram, again checking them with our balance. (We check a 2-kg mass on one end of the balance against two 1-kg masses placed together on the other end; we check two half-kg masses by verifying that their masses are equal and that together they balance a 1-kg mass; and so on.) Finally, we can measure an unknown mass by putting it on one end of the balance and loading known masses on the other end until they balance to any desired precision.

## Force

The informal notion of force as a push or pull is a surprisingly good starting point for our discussion of forces. We are certainly conscious of the forces that we exert ourselves. When I hold up a sack of cement, I am very aware that I am exerting an upward force on the sack; when I push a heavy crate across a rough floor, I am aware of the horizontal force that I have to exert in the direction of motion. Forces exerted by inanimate objects are a little harder to pin down, and we must, in fact, understand something of Newton's laws to identify such forces. If I let go of the sack of cement, it accelerates toward the ground; therefore, I conclude that there must be another force — the sack's weight, the gravitational force of the earth — pulling it downward. As I push the crate across the floor, I observe that it does not accelerate, and I conclude that there must be another force — friction — pushing the crate in the opposite direction. One of the most important skills for the student of elementary mechanics is to learn to examine an object's environment and identify all the forces on the object: What are the things touching the object and possibly exerting contact forces, such as friction or air pressure? And what are the nearby objects possibly exerting action-at-a-distance forces, such as the gravitational pull of the earth or the electrostatic force of some charged body?

If we accept that we know how to identify forces, it remains to decide how to measure them. As the unit of force we naturally adopt the newton (abbreviated N) defined as the magnitude of any single force that accelerates a standard kilogram mass with an acceleration of $1 \, m/s^{2}$ . Having agreed what we mean by one newton, we can proceed in several ways, all of which come to the same final conclusion, of course. The route that is probably preferred by most philosophers of science is to use Newton's second law to define the general force: A given force is 2 N if, by itself, it accelerates a standard kilogram with an acceleration of $2 \, m/s^{2}$ , and so on. This approach is not much like the way we usually measure forces in practice, $^{4}$ and for our present discussion a simpler procedure is to use some spring balances. Using our definition of the newton, we can calibrate a first spring balance to read 1 N. Then by matching a second spring balance against the first, using a balance arm as shown in Figure 1.3, we can define multiples and fractions of a newton. Once we have a fully calibrated spring balance we can, in principle, measure any unknown force, by matching it against the calibrated balance and reading off its value.

![](images/55c74f30260da09036854d7cbc7ae80c2b8191d90a53ffbd2474d85c7cd56f3b.jpg)  
Figure 1.3 One of many possible ways to define forces of any magnitude. The lower spring balance has been calibrated to read 1 N. If the balance arm on the left is adjusted so that the lever arms above and below the pivot are in the ratio 1:2 and if the force $F_{1}$ is 1 N, then the force $F_{2}$ required to balance the arm is 2 N. This lets us calibrate the upper spring balance for 2 N. By readjusting the two lever arms, we can, in principle, calibrate the second spring balance to read any force.

So far we have defined only the magnitude of a force. As you are certainly aware, forces are vectors, and we must also define their directions. This is easily done. If we apply a given force F (and no other forces) to any object at rest, the direction of F is defined as the direction of the resulting acceleration, that is, the direction in which the body moves off.

Now that we know, at least in principle, what we mean by positions, times, masses, and forces, we can proceed to discuss the cornerstone of our subject — Newton's three laws of motion.

## 1.4 Newton's First and Second Laws; Inertial Frames

In this chapter, I am going to discuss Newton's laws as they apply to a point mass. A point mass, or particle, is a convenient fiction, an object with mass, but no size, that can move through space but has no internal degrees of freedom. It can have "translational" kinetic energy (energy of its motion through space) but no energy of rotation or of internal vibrations or deformations. Naturally, the laws of motion are simpler for point particles than for extended bodies, and this is the main reason that we start with the former. Later on, I shall build up the mechanics of extended bodies from our mechanics of point particles by considering the extended body as a collection of many separate particles.

Nevertheless, it is worth recognizing that there are many important problems where the objects of interest can be realistically approximated as point masses. Atomic and subatomic particles can often be considered to be point masses, and even macroscopic objects can frequently be approximated in this way. A stone thrown off the top of a cliff is, for almost all purposes, a point particle. Even a planet orbiting around the sun can usually be approximated in the same way. Thus the mechanics of point masses is more than just the starting point for the mechanics of extended bodies; it is a subject with wide application itself.

Newton's first two laws are well known and easily stated:

## Newton's First Law (the Law of Inertia)

In the absence of forces, a particle moves with constant velocity v.

and

## Newton's Second Law

For any particle of mass m, the net force F on the particle is always equal to the mass m times the particle's acceleration:

$$
\mathbf {F} = m \mathbf {a}.\tag{1.17}
$$

In this equation $\mathbf{F}$ denotes the vector sum of all the forces on the particle and $\mathbf{a}$ is the particle's acceleration,

$$
\begin{array}{r l} \mathbf {a} & = \frac {d \mathbf {v}}{d t} \equiv \dot {\mathbf {v}} \\ & = \frac {d ^ {2} \mathbf {r}}{d t ^ {2}} \equiv \ddot {\mathbf {r}}. \end{array}
$$

Here $\mathbf{v}$ denotes the particle's velocity, and I have introduced the convenient notation of dots to denote differentiation with respect to $t$ , as in $\mathbf{v} = \dot{\mathbf{r}}$ and $\mathbf{a} = \dot{\mathbf{v}} = \ddot{\mathbf{r}}$ .

Both laws can be stated in various equivalent ways. For instance (the first law): In the absence of forces, a stationary particle remains stationary and a moving particle continues to move with unchanging speed in the same direction. This is, of course, exactly the same as saying that the velocity is always constant. Again, v is constant if and only if the acceleration a is zero, so an even more compact statement is this: In the absence of forces a particle has zero acceleration.

The second law can be rephrased in terms of the particle's momentum, defined as

$$
\mathbf {p} = m \mathbf {v}.\tag{1.18}
$$

In classical mechanics, we take for granted that the mass m of a particle never changes, so that

$$
\dot {\mathbf {p}} = m \dot {\mathbf {v}} = m \mathbf {a}.
$$

Thus the second law (1.17) can be rephrased to say that

$$
\mathbf {F} = \dot {\mathbf {p}}.\tag{1.19}
$$

In classical mechanics, the two forms (1.17) and (1.19) of the second law are completely equivalent. $^{5}$

## Differential Equations

When written in the form $m\ddot{\mathbf{r}} = \mathbf{F}$ , Newton's second law is a differential equation for the particle's position $\mathbf{r}(t)$ . That is, it is an equation for the unknown function $\mathbf{r}(t)$ that involves derivatives of the unknown function. Almost all the laws of physics are, or can be cast as, differential equations, and a huge proportion of a physicist's time is spent solving these equations. In particular, most of the problems in this book involve differential equations — either Newton's second law or its counterparts in the Lagrangian and Hamiltonian forms of mechanics. These vary widely in their difficulty. Some are so easy to solve that one scarcely notices them. For example, consider Newton's second law for a particle confined to move along the $x$ axis and subject to a constant force $F_0$ ,

$$
\ddot {x} (t) = \frac {F _ {\mathrm{o}}}{m}.
$$

This is a second-order differential equation for $x(t)$ as a function of $t$ . (Second-order because it involves derivatives of second order, but none of higher order.) To solve it one has only to integrate it twice. The first integration gives the velocity

$$
\dot {x} (t) = \int \ddot {x} (t) d t = v _ {\mathrm{o}} + \frac {F _ {\mathrm{o}}}{m} t
$$

where the constant of integration is the particle's initial velocity, and a second integration gives the position

$$
x (t) = \int \dot {x} (t) d t = x _ {\mathrm{o}} + v _ {\mathrm{o}} t + \frac {F _ {\mathrm{o}}}{2 m} t ^ {2}
$$

where the second constant of integration is the particle's initial position. Solving this differential equation was so easy that we certainly needed no knowledge of the theory of differential equations. On the other hand, we shall meet lots of differential equations that do require knowledge of this theory, and I shall present the necessary theory as we need it. Obviously, it will be an advantage if you have already studied some of the theory of differential equations, but you should have no difficulty picking it up as we go along. Indeed, many of us find that the best way to learn this kind of mathematical theory is in the context of its physical applications.

## Inertial Frames

On the face of it, Newton's second law includes his first: If there are no forces on an object, then $\mathbf{F} = 0$ and the second law (1.17) implies that $\mathbf{a} = 0$ , which is the first law. There is, however, an important subtlety, and the first law has an important role to play. Newton's laws cannot be true in all conceivable reference frames. To see this, consider just the first law and imagine a reference frame — we'll call it $S$ — in which the first law is true. For example, if the frame $S$ has its origin and axes fixed relative to the earth's surface, then, to an excellent approximation, the first law (the law of inertia) holds with respect to the frame $S$ : A frictionless puck placed on a smooth horizontal surface is subject to zero force and, in accordance with the first law, it moves with constant velocity. Because the law of inertia holds, we call $S$ an inertial frame. If we consider a second frame $S'$ which is moving relative to $S$ with constant velocity and is not rotating, then the same puck will also be observed to move with constant velocity relative to $S'$ . That is, the frame $S'$ is also inertial.

If, however, we consider a third frame $S''$ that is accelerating relative to S, then, as viewed from $S''$ , the puck will be seen to be accelerating (in the opposite direction). Relative to the accelerating frame $S''$ the law of inertia does not hold, and we say that $S''$ is noninertial. I should emphasize that there is nothing mysterious about this result. Indeed it is a matter of experience. The frame $S'$ could be a frame attached to a high-speed train traveling smoothly at constant speed along a straight track, and the frictionless puck, an ice cube placed on the floor of the train, as in Figure 1.4. As seen from the train (frame $S'$ ), the ice cube is at rest and remains at rest, in accord with the first law. As seen from the ground (frame S), the ice cube is moving with the same velocity as the train and continues to do so, again in obedience to the first law. But now consider conducting the same experiment on a second train (frame $S''$ ) that is accelerating forward. As this train accelerates forward, the ice cube is left behind, and, relative to $S''$ , the ice cube accelerates backward, even though subject to no net force. Clearly the frame $S''$ is noninertial, and neither of the first two laws can hold in $S''$ . A similar conclusion would hold if the frame $S''$ had been attached to a rotating merry-go-round. A frictionless puck, subject to zero net force, would not move in a straight line as seen in $S''$ , and Newton's laws would not hold.

![](images/28ae6e851de5031e09f57323399626dd5df82d8f8d61619752aeefc33e26f687.jpg)  
Figure 1.4 The frame S is fixed to the ground, while $S'$ is fixed to a train traveling at constant velocity $v'$ relative to S. An ice cube placed on the floor of the train obeys Newton's first law as seen from both S and $S'$ . If the train to which $S''$ is attached is accelerating forward, then, as seen in $S''$ , an ice cube placed on the floor will accelerate backward, and the first law does not hold in $S''$ .

Evidently Newton's two laws hold only in the special, inertial (nonaccelerating and nonrotating) reference frames. Most philosophers of science take the view that the first law should be used to identify these inertial frames — a reference frame $\mathcal{S}$ is inertial if objects that are clearly subject to no forces are seen to move with constant velocity relative to $\mathcal{S}$ . $^{6}$ Having identified the inertial frames by means of Newton's first law, we can then claim as an experimental fact that the second law holds in these same inertial frames. $^{7}$

Since the laws of motion hold only in inertial frames, you might imagine that we would confine our attention exclusively to inertial frames, and, for a while, we shall do just that. Nevertheless, you should be aware that there are situations where it is necessary, or at least very convenient, to work in noninertial frames. The most important example of a noninertial frame is in fact the earth itself. To an excellent approximation, a reference frame fixed to the earth is inertial — a fortunate circumstance for students of physics! Nevertheless, the earth rotates on its axis once a day and circles around the sun once a year, and the sun orbits slowly around the center of the Milky Way galaxy. For all of these reasons, a reference frame fixed to the earth is not exactly inertial. Although these effects are very small, there are several phenomena — the tides and the trajectories of long-range projectiles are examples — that are most simply explained by taking into account the noninertial character of a frame fixed to the earth. In Chapter 9 we shall examine how the laws of motion must be modified for use in noninertial frames. For the moment, however, we shall confine our discussion to inertial frames.

## Validity of the First Two Laws

Since the advent of relativity and quantum mechanics, we have known that Newton's laws are not universally valid. Nevertheless, there is an immense range of phenomena—the phenomena of classical physics—where the first two laws are for all practical purposes exact. Even as the speeds of interest approach c, the speed of light, and relativity becomes important, the first law remains exactly true. (In relativity, just as in classical mechanics, an inertial frame is defined as one where the first law holds.) $^{8}$ As we shall see in Chapter 15, the two forms of the second law, F = ma and F = $\dot{p}$ , are no longer equivalent in relativity, although with F and p suitably defined the second law in the form F = $\dot{p}$ is still valid. In any case, the important point is this: In the classical domain, we can and shall assume that the first two laws (the second in either form) are universally and precisely valid. You can, if you wish, regard this assumption as defining a model—the classical model—of the natural world. The model is logically consistent and is such a good representation of many phenomena that it is amply worthy of our study.

## 1.5 The Third Law and Conservation of Momentum

Newton's first two laws concern the response of a single object to applied forces. The third law addresses a quite different issue: Every force on an object inevitably involves a second object—the object that exerts the force. The nail is hit by the hammer, the cart is pulled by the horse, and so on. While this much is no doubt a matter of common sense, the third law goes considerably beyond our everyday experience. Newton realized that if an object 1 exerts a force on another object 2, then object 2 always exerts a force (the “reaction” force) back on object 1. This seems quite natural: If you push hard against a wall, it is fairly easy to convince yourself that the wall is exerting a force back on you, without which you would undoubtedly fall over. The aspect of the third law which certainly goes beyond our normal perceptions is this: According to the third law, the reaction force of object 2 on object 1 is always equal and opposite to the original force of 1 on 2. If we introduce the notation $\mathbf{F}_{21}$ to denote the force exerted on object 2 by object 1, Newton's third law can be stated very compactly:

![](images/09544e35251fc96c8c3060aea397284b9d813e20e7adee739bdf2cda2ead50c7.jpg)  
Figure 1.5 Newton's third law asserts that the reaction force exerted on object 1 by object 2 is equal and opposite to the force exerted on 2 by 1, that is, $\mathbf{F}_{12} = -\mathbf{F}_{21}$ .

## Newton's Third Law

If object 1 exerts a force $F_{21}$ on object 2, then object 2 always exerts a reaction force $F_{12}$ on object 1 given by

$$
\mathbf {F} _ {1 2} = - \mathbf {F} _ {2 1}.\tag{1.20}
$$

This statement is illustrated in Figure 1.5, which you could think of as showing the force of the earth on the moon and the reaction force of the moon on the earth (or a proton on an electron and the electron on the proton). Notice that this figure actually goes a little beyond the usual statement (1.20) of the third law: Not only have I shown the two forces as equal and opposite; I have also shown them acting along the line joining 1 and 2. Forces with this extra property are called central forces. (They act along the line of centers.) The third law does not actually require that the forces be central, but, as I shall discuss later, most of the forces we encounter (gravity, the electrostatic force between two charges, etc.) do have this property.

As Newton himself was well aware, the third law is intimately related to the law of conservation of momentum. Let us focus, at first, on just two objects as shown in Figure 1.6, which might show the earth and the moon or two skaters on the ice. In addition to the force of each object on the other, there may be “external” forces exerted by other bodies. The earth and moon both experience forces exerted by the sun, and both skaters could experience the external force of the wind. I have shown the net external forces on the two objects as $F_{1}^{ext}$ and $F_{2}^{ext}$ . The total force on object 1 is then

$$
(\text { net   force   on } 1) \equiv \mathbf {F} _ {1} = \mathbf {F} _ {1 2} + \mathbf {F} _ {1} ^ {\text { ext }}
$$

and similarly

$$
(\text { net   force   on } 2) \equiv \mathbf {F} _ {2} = \mathbf {F} _ {2 1} + \mathbf {F} _ {2} ^ {\text { ext }}.
$$

We can compute the rates of change of the particles' momenta using Newton's second law:

$$
\dot {\mathbf {p}} _ {1} = \mathbf {F} _ {1} = \mathbf {F} _ {1 2} + \mathbf {F} _ {1} ^ {\text { ext }}\tag{1.21}
$$

![](images/27e981abd2ccb6d7c1ffb100a049e83a95d22d93c6ef5d0067d8b0a9690b2b4b.jpg)  
Figure 1.6 Two objects exert forces on each other and may also be subject to additional “external” forces from other objects not shown.

and

$$
\dot {\mathbf {p}} _ {2} = \mathbf {F} _ {2} = \mathbf {F} _ {2 1} + \mathbf {F} _ {2} ^ {\mathrm{ext}}.\tag{1.22}
$$

If we now define the total momentum of our two objects as

$$
\mathbf {P} = \mathbf {p} _ {1} + \mathbf {p} _ {2},
$$

then the rate of change of the total momentum is just

$$
\dot {\mathbf {P}} = \dot {\mathbf {p}} _ {1} + \dot {\mathbf {p}} _ {2}.
$$

To evaluate this, we have only to add Equations (1.21) and (1.22). When we do this, the two internal forces, $\mathbf{F}_{12}$ and $\mathbf{F}_{21}$ , cancel out because of Newton's third law, and we are left with

$$
\dot {\mathbf {P}} = \mathbf {F} _ {1} ^ {\mathrm{ext}} + \mathbf {F} _ {2} ^ {\mathrm{ext}} \equiv \mathbf {F} ^ {\mathrm{ext}},\tag{1.23}
$$

where I have introduced the notation $F^{ext}$ to denote the total external force on our two-particle system.

The result (1.23) is the first in a series of important results that let us construct a theory of many-particle systems from the basic laws for a single particle. It asserts that as far as the total momentum of a system is concerned, the internal forces have no effect. A special case of this result is that if there are no external forces ( $F^{ext} = 0$ ) then $\dot{P} = 0$ . Thus we have the important result:

$$
\mathrm{If} \qquad \mathbf {F} ^ {\mathrm{ext}} = 0, \qquad \mathrm{then} \qquad \mathbf {P} = \mathrm{const.}\tag{1.24}
$$

In the absence of external forces, the total momentum of our two-particle system is constant — a result called the principle of conservation of momentum.

## Multiparticle Systems

We have proved the conservation of momentum, Equation (1.24), for a system of two particles. The extension of the result to any number of particles is straightforward in principle, but I would like to go through it in detail, because it lets me introduce some important notation and will give you some practice using the summation notation. Let us consider then a system of N particles. I shall label the typical particle with a Greek index $\alpha$ or $\beta$ , either of which can take any of the values 1, 2, $\cdots$ , N. The mass of particle $\alpha$ is $m_{\alpha}$ and its momentum is $p_{\alpha}$ . The force on particle $\alpha$ is quite complicated: Each of the other (N - 1) particles can exert a force which I shall call $F_{\alpha\beta}$ , the force on $\alpha$ by $\beta$ , as illustrated in Figure 1.7. In addition there may be a net external force on particle $\alpha$ , which I shall call $F_{\alpha}^{ext}$ . Thus the net force on particle $\alpha$ is

![](images/0fac2a9985b7fa3e772c8afab18fc37372f35bf800b3dca0018d03b64d0db05f.jpg)  
Figure 1.7 A five-particle system with particles labelled by $\alpha$ or $\beta = 1, 2, \cdots, 5$ . The particle $\alpha$ is subject to four internal forces, shown by solid arrows and denoted $F_{\alpha\beta}$ (the force on $\alpha$ by $\beta$ ). In addition particle $\alpha$ may be subject to a net external force, shown by the dashed arrow and denoted $F_{\alpha}^{ext}$ .

$$
(\text { net   force   on   particle } \alpha) = \mathbf {F} _ {\alpha} = \sum_ {\beta \neq \alpha} \mathbf {F} _ {\alpha \beta} + \mathbf {F} _ {\alpha} ^ {\text { ext }}.\tag{1.25}
$$

Here the sum runs over all values of $\beta$ not equal to $\alpha$ . (Remember there is no force $F_{\alpha\alpha}$ because particle $\alpha$ cannot exert a force on itself.) According to Newton's second law, this is the same as the rate of change of $p_{\alpha}$ :

$$
\dot {\mathbf {p}} _ {\alpha} = \sum_ {\beta \neq \alpha} \mathbf {F} _ {\alpha \beta} + \mathbf {F} _ {\alpha} ^ {\mathrm{ext}}.\tag{1.26}
$$

This result holds for each $\alpha = 1, \cdots, N$ .

Let us now consider the total momentum of our N-particle system,

$$
\mathbf {P} = \sum_ {\alpha} \mathbf {p} _ {\alpha}
$$

where, of course, this sum runs over all N particles, $\alpha = 1, 2, \cdots, N$ . If we differentiate this equation with respect to time, we find

$$
\dot {\mathbf {P}} = \sum_ {\alpha} \dot {\mathbf {p}} _ {\alpha}
$$

or, substituting for $\dot{p}_{\alpha}$ from (1.26),

$$
\dot {\mathbf {P}} = \sum_ {\alpha} \sum_ {\beta \neq \alpha} \mathbf {F} _ {\alpha \beta} + \sum_ {\alpha} \mathbf {F} _ {\alpha} ^ {\text { ext }}.\tag{1.27}
$$

The double sum here contains $N(N - 1)$ terms in all. Each term $F_{\alpha\beta}$ in this sum can be paired with a second term $F_{\beta\alpha}$ (that is, $F_{12}$ paired with $F_{21}$ , and so on), so that

$$
\sum_ {\alpha} \sum_ {\beta \neq \alpha} \mathbf {F} _ {\alpha \beta} = \sum_ {\alpha} \sum_ {\beta > \alpha} (\mathbf {F} _ {\alpha \beta} + \mathbf {F} _ {\beta \alpha}).\tag{1.28}
$$

The double sum on the right includes only values of $\alpha$ and $\beta$ with $\alpha < \beta$ and has half as many terms as that on the left. But each term is the sum of two forces, $(\mathbf{F}_{\alpha \beta} + \mathbf{F}_{\beta \alpha})$ , and, by the third law, each such sum is zero. Therefore the whole double sum in (1.28) is zero, and returning to (1.27) we conclude that

$$
\dot {\mathbf {P}} = \sum_ {\alpha} \mathbf {F} _ {\alpha} ^ {\mathrm{ext}} \equiv \mathbf {F} ^ {\mathrm{ext}}.\tag{1.29}
$$

The result (1.29) corresponds exactly to the two-particle result (1.23). Like the latter, it says that the internal forces have no effect on the evolution of the total momentum P — the rate of change of P is determined by the net external force on the system. In particular, if the net external force is zero, we have the

## Principle of Conservation of Momentum

If the net external force $\mathbf{F}^{\mathrm{ext}}$ on an $N$ -particle system is zero, the system's total momentum $\mathbf{P}$ is constant.

As you are certainly aware, this is one of the most important results in classical physics and is, in fact, also true in relativity and quantum mechanics. If you are not very familiar with the sorts of manipulations of sums that we used, it would be a good idea to go over the argument leading from (1.25) to (1.29) for the case of three or four particles, writing out all the sums explicitly (Problems 1.28 or 1.29). You should also convince yourself that, conversely, if the principle of conservation of momentum is true for all multiparticle systems, then Newton's third law must be true (Problem 1.31). In other words, conservation of momentum and Newton's third law are equivalent to one another.

## Validity of Newton's Third Law

Within the domain of classical physics, the third law, like the second, is valid with such accuracy that it can be taken to be exact. As speeds approach the speed of light, it is easy to see that the third law cannot hold: The point is that the law asserts that the action and reaction forces, $\mathbf{F}_{12}(t)$ and $\mathbf{F}_{21}(t)$ , measured at the same time t, are equal and opposite. As you certainly know, once relativity becomes important the concept of a single universal time has to be abandoned — two events that are seen as simultaneous by one observer are, in general, not simultaneous as seen by a second observer. Thus, even if the equality $\mathbf{F}_{12}(t) = -\mathbf{F}_{21}(t)$ (with both times the same) were true for one observer, it would generally be false for another. Therefore, the third law cannot be valid once relativity becomes important.

![](images/41afdb00bb16012e497efedc723a251f4f4d23b0d44b37c89e8f7857cf32ce22.jpg)  
Figure 1.8 Each of the positive charges $q_{1}$ and $q_{2}$ produces a magnetic field that exerts a force on the other charge. The resulting magnetic forces $\mathbf{F}_{12}$ and $\mathbf{F}_{21}$ do not obey Newton's third law.

Rather surprisingly, there is a simple example of a well-known force — the magnetic force between two moving charges — for which the third law is not exactly true, even at slow speeds. To see this, consider the two positive charges of Figure 1.8, with $q_{1}$ moving in the x direction and $q_{2}$ moving in the y direction, as shown. The exact calculation of the magnetic field produced by each charge is complicated, but a simple argument gives the correct directions of the two fields, and this is all we need. The moving charge $q_{1}$ is equivalent to a current in the x direction. By the right-hand rule for fields, this produces a magnetic field which points in the z direction in the vicinity of $q_{2}$ . By the right-hand rule for forces, this field produces a force $F_{21}$ on $q_{2}$ that is in the x direction. An exactly analogous argument (check it yourself) shows that the force $F_{12}$ on $q_{1}$ is in the y direction, as shown. Clearly these two forces do not obey Newton's third law!

This conclusion is especially startling since we have just seen that Newton's third law is equivalent to the conservation of momentum. Apparently the total momentum $m_{1}v_{1} + m_{2}v_{2}$ of the two charges in Figure 1.8 is not conserved. This conclusion, which is correct, serves to remind us that the “mechanical” momentum mv of particles is not the only kind of momentum. Electromagnetic fields can also carry momentum, and in the situation of Figure 1.8 the mechanical momentum being lost by the two particles is going to the electromagnetic momentum of the fields.

Fortunately, if both speeds in Figure 1.8 are much less than the speed of light $(v\ll c)$ , the loss of mechanical momentum and the concomitant failure of the third law are completely negligible. To see this, note that in addition to the magnetic force between $q_{1}$ and $q_{2}$ there is the electrostatic Coulomb force $^{9}kq_{1}q_{2} / r^{2}$ , which does obey Newton's third law. It is a straightforward exercise (Problem 1.32) to show that the magnetic force is of order $v^2 /c^2$ times the Coulomb force. Thus only as $v$ approaches $c$ — and classical mechanics must give way to relativity anyway — is the violation of the third law by the magnetic force important. $^{10}$ We see that the unexpected situation of Figure 1.8 does not contradict our claim that in the classical domain Newton's third law is valid, and this is what we shall assume in our discussions of nonrelativistic mechanics.

## 1.6 Newton's Second Law in Cartesian Coordinates

Of Newton's three laws, the one that we actually use the most is the second, which is often described as the equation of motion. As we have seen, the first is theoretically important to define what we mean by inertial frames but is usually of no practical use beyond this. The third law is crucially important in sorting out the internal forces in a multiparticle system, but, once we know the forces involved, the second law is what we actually use to calculate the motion of the object or objects of interest. In particular, in many simple problems the forces are known or easily found, and, in this case, the second law is all we need for solving the problem.

As we have already noted, the second law,

$$
\mathbf {F} = m \ddot {\mathbf {r}},\tag{1.30}
$$

is a second-order, differential equation $^{11}$ for the position vector r as a function of the time t. In the prototypical problem, the forces that comprise F are given, and our job is to solve the differential equation (1.30) for $\mathbf{r}(t)$ . Sometimes we are told about $\mathbf{r}(t)$ , and we have to use (1.30) to find some of the forces. In any case, the equation (1.30) is a vector differential equation. And the simplest way to solve such equations is almost always to resolve the vectors into their components relative to a chosen coordinate system.

Conceptually the simplest coordinate system is the Cartesian (or rectangular), with unit vectors $\hat{x}$ , $\hat{y}$ , and $\hat{z}$ , in terms of which the net force F can then be written as

$$
\mathbf {F} = F _ {x} \hat {\mathbf {x}} + F _ {y} \hat {\mathbf {y}} + F _ {z} \hat {\mathbf {z}}\tag{1.31}
$$

and the position vector r as

$$
\mathbf {r} = x \hat {\mathbf {x}} + y \hat {\mathbf {y}} + z \hat {\mathbf {z}}.\tag{1.32}
$$

As we noted in Section 1.2, this expansion of $\mathbf{r}$ in terms of its Cartesian components is especially easy to differentiate because the unit vectors $\hat{\mathbf{x}},\hat{\mathbf{y}},\hat{\mathbf{z}}$ are constant. Thus we can differentiate (1.32) twice to get the simple result

$$
\ddot {\mathbf {r}} = \ddot {x} \hat {\mathbf {x}} + \ddot {y} \hat {\mathbf {y}} + \ddot {z} \hat {\mathbf {z}}.\tag{1.33}
$$

That is, the three Cartesian components of $\ddot{\mathbf{r}}$ are just the appropriate derivatives of the three coordinates $x, y, z$ of $\mathbf{r}$ , and the second law (1.30) becomes

$$
F _ {x} \hat {\mathbf {x}} + F _ {v} \hat {\mathbf {y}} + F _ {z} \hat {\mathbf {z}} = m \ddot {x} \hat {\mathbf {x}} + m \ddot {y} \hat {\mathbf {y}} + m \ddot {z} \hat {\mathbf {z}}.\tag{1.34}
$$

Resolving this equation into its three separate components, we see that $F_{x}$ has to equal $m\ddot{x}$ and similarly for the y and z components. That is, in Cartesian coordinates, the single vector equation (1.30) is equivalent to the three separate equations:

$$
\mathbf {F} = m \ddot {\mathbf {r}} \quad \Longleftrightarrow \quad \left\{ \begin{array}{l} F _ {x} = m \ddot {x} \\ F _ {y} = m \ddot {y} \\ F _ {z} = m \ddot {z}. \end{array} \right.\tag{1.35}
$$

This beautiful result, that, in Cartesian coordinates, Newton's second law in three dimensions is equivalent to three one-dimensional versions of the same law, is the basis of the solution of almost all simple mechanics problems in Cartesian coordinates. Here is an example to remind you of how such problems go.

## EXAMPLE 1.1 A Block Sliding down an Incline

A block of mass m is observed accelerating from rest down an incline that has coefficient of friction $\mu$ and is at angle $\theta$ from the horizontal. How far will it travel in time t?

Our first task is to choose our frame of reference. Naturally, we choose our spatial origin at the block's starting position and the origin of time $(t = 0)$ at the moment of release. As you no doubt remember from your introductory physics course, the best choice of axes is to have one axis (x say) point down the slope, one (y) normal to the slope, and the third (z) across it, as shown in Figure 1.9. This choice has two advantages: First, because the block slides straight down the slope, the motion is entirely in the x direction, and only x varies. (If we had chosen the x axis horizontal and the y axis vertical, then both x and y would vary.) Second, two of the three forces on the block are unknown (the normal force N and friction f; the weight, w = mg, we treat as known), and with our choice of axes, each of the unknowns has only one nonzero component, since N is in the y direction and f is in the (negative) x direction.

We are now ready to apply Newton's second law. The result (1.35) means that we can analyse the three components separately, as follows:

There are no forces in the z direction, so $F_{z}=0$ . Since $F_{z}=m\ddot{z}$ , it follows that $\ddot{z}=0$ , which implies that $\dot{z}$ (or $v_{z}$ ) is constant. Since the block starts from rest, this means that $\dot{z}$ is actually zero for all t. With $\dot{z}=0$ , it follows that z is constant, and, since it too starts from zero, we conclude that z=0 for all t. As we would certainly have guessed, the motion remains in the xy plane.

Since the block does not jump off the incline, we know that there is no motion in the y direction. In particular, $\ddot{y}=0$ . Therefore, Newton's second law implies that the y component of the net force is zero; that is, $F_{y}=0$ . From Figure 1.9 we see that this implies that

$$
F _ {y} = N - m g \cos \theta = 0.
$$

![](images/7a4778edf7e183941aa09d6013ba302872382bee127a0d577e26587b6ca1b6ea.jpg)  
Figure 1.9 A block slides down a slope of incline $\theta$ . The three forces on the block are its weight, w = mg, the normal force of the incline, N, and the frictional force f, whose magnitude is $f = \mu N$ . The z axis is not shown but points out of the page, that is, across the slope.

Thus the y component of the second law has told us that the unknown normal force is $N = mg \cos \theta$ . Since $f = \mu N$ , this tells us the frictional force, $f = \mu mg \cos \theta$ , and all the forces are now known. All that remains is to use the remaining component (the x component) of the second law to solve for the actual motion.

The $x$ component of the second law, $F_{x} = m\ddot{x}$ , implies (see Figure 1.9) that

$$
w _ {x} - f = m \ddot {x}
$$

or

$$
m g \sin \theta - \mu m g \cos \theta = m \ddot {x}.
$$

The $m$ 's cancel, and we find for the acceleration down the slope

$$
\ddot {x} = g (\sin \theta - \mu \cos \theta).\tag{1.36}
$$

Having found $\ddot{x}$ , and found it to be constant, we have only to integrate it twice to find x as a function of t. First

$$
\dot {x} = g (\sin \theta - \mu \cos \theta) t.
$$

(Remember that $\dot{x}=0$ initially, so the constant of integration is zero.) Finally,

$$
x (t) = \frac {1}{2} g (\sin \theta - \mu \cos \theta) t ^ {2}
$$

(again the constant of integration is zero) and our solution is complete.

![](images/5afce53da859c22c4a41663e7aa8581d6d12ad53a76f14606f914ace5c15386f.jpg)  
Figure 1.10 The definition of the polar coordinates r and $\phi$ .

## 1.7 Two-Dimensional Polar Coordinates

While Cartesian coordinates have the merit of simplicity, we are going to find that it is almost impossible to solve certain problems without the use of various non-Cartesian coordinate systems. To illustrate the complexities of non-Cartesian coordinates, let us consider the form of Newton's second law in a two-dimensional problem using polar coordinates. These coordinates are defined in Figure 1.10. Instead of using the two rectangular coordinates x, y, we label the position of a particle with its distance r from O and the angle $\phi$ measured up from the x axis. Given the rectangular coordinates x and y, you can calculate the polar coordinates r and $\phi$ , or vice versa, using the following relations. (Make sure you understand all four equations. $^{12}$ )

$$
\left. \begin{array}{l} x = r \cos \phi \\ y = r \sin \phi \end{array} \right\} \longleftrightarrow \left\{ \begin{array}{l} r = \sqrt {x ^ {2} + y ^ {2}} \\ \phi = \arctan (y / x) \end{array} \right.\tag{1.37}
$$

Just as with rectangular coordinates, it is convenient to introduce two unit vectors, which I shall denote by $\hat{\mathbf{r}}$ and $\hat{\phi}$ . To understand their definitions, notice that we can define the unit vector $\hat{\mathbf{x}}$ as the unit vector that points in the direction of increasing $x$ when $y$ is fixed, as shown in Figure 1.11(a). In the same way we shall define $\hat{\mathbf{r}}$ as the unit vector that points in the direction we move when $r$ increases with $\phi$ fixed; likewise, $\hat{\phi}$ is the unit vector that points in the direction we move when $\phi$ increases with $r$ fixed. Figure 1.11 makes clear a most important difference between the unit vectors $\hat{\mathbf{x}}$ and $\hat{\mathbf{y}}$ of rectangular coordinates and our new unit vectors $\hat{\mathbf{r}}$ and $\hat{\phi}$ . The vectors $\hat{\mathbf{x}}$ and $\hat{\mathbf{y}}$ are the same at all points in the plane, whereas the new vectors $\hat{\mathbf{r}}$ and $\hat{\phi}$ change their directions as the position vector $\mathbf{r}$ moves around. We shall see that this complicates the use of Newton's second law in polar coordinates.

Figure 1.11 suggests another way to write the unit vector $\hat{\mathbf{r}}$ . Since $\hat{\mathbf{r}}$ is in the same direction as $\mathbf{r}$ , but has magnitude 1, you can see that

$$
\hat {\mathbf {r}} = \frac {\mathbf {r}}{| \mathbf {r} |}.\tag{1.38}
$$

This result suggests a second role for the “hat” notation. For any vector $\mathbf{a}$ , we can define $\hat{\mathbf{a}}$ as the unit vector in the direction of $\mathbf{a}$ , namely $\hat{\mathbf{a}} = \mathbf{a} / |\mathbf{a}|$ .

![](images/d494f7f24bdc6dbfd35de8fe746b59b50aaf2448e87a6632198cfba0cd2d4393.jpg)  
Figure 1.11 (a) The unit vector $\hat{x}$ points in the direction of increasing x with y fixed. (b) The unit vector $\hat{r}$ points in the direction of increasing r with $\phi$ fixed; $\hat{\phi}$ points in the direction of increasing $\phi$ with r fixed. Unlike $\hat{x}$ , the vectors $\hat{r}$ and $\hat{\phi}$ change as the position vector r moves.

Since the two unit vectors $\hat{r}$ and $\phi$ are perpendicular vectors in our two-dimensional space, any vector can be expanded in terms of them. For instance, the net force F on an object can be written

$$
\mathbf {F} = F _ {r} \hat {\mathbf {r}} + F _ {\phi} \hat {\boldsymbol {\phi}}.\tag{1.39}
$$

If, for example, the object in question is a stone that I am twirling in a circle on the end of a string (with my hand at the origin), then $F_{r}$ would be the tension in the string and $F_{\phi}$ the force of air resistance retarding the stone in the tangential direction. The expansion of the position vector itself is especially simple in polar coordinates. From Figure 1.11(b) it is clear that

$$
\mathbf {r} = r \hat {\mathbf {r}}.\tag{1.40}
$$

We are now ready to ask about the form of Newton's second law, $\mathbf{F} = m\ddot{\mathbf{r}}$ , in polar coordinates. In rectangular coordinates, we saw that the $x$ component of $\ddot{\mathbf{r}}$ is just $\ddot{x}$ , and this is what led to the very simple result (1.35). We must now find the components of $\ddot{\mathbf{r}}$ in polar coordinates; that is, we must differentiate (1.40) with respect to $t$ . Although (1.40) is very simple, the vector $\hat{\mathbf{r}}$ changes as $\mathbf{r}$ moves. Thus when we differentiate (1.40), we shall pick up a term involving the derivative of $\hat{\mathbf{r}}$ . Our first task is to find this derivative of $\hat{\mathbf{r}}$ .

Figure 1.12(a) shows the position of the particle of interest at two successive times, $t_1$ and $t_2 = t_1 + \Delta t$ . If the corresponding angles $\phi(t_1)$ and $\phi(t_2)$ are different, then the two unit vectors $\hat{\mathbf{r}}(t_1)$ and $\hat{\mathbf{r}}(t_2)$ point in different directions. The change in $\hat{\mathbf{r}}$ is shown in Figure 1.12(b), and (provided $\Delta t$ is small) is approximately

$$
\begin{array}{r} \Delta \hat {\mathbf {r}} \approx \Delta \phi   \hat {\boldsymbol {\phi}} \\ \approx \dot {\phi}   \Delta t   \hat {\boldsymbol {\phi}}. \end{array}\tag{1.41}
$$

(Notice that the direction of $\Delta \hat{\mathbf{r}}$ is perpendicular to $\hat{\mathbf{r}}$ , namely the direction of $\hat{\boldsymbol{\phi}}$ .) If we divide both sides by $\Delta t$ and take the limit as $\Delta t \to 0$ , then $\Delta \hat{\mathbf{r}} / \Delta t \to d\hat{\mathbf{r}} / dt$ and we find that

$$
\frac {d \hat {\mathbf {r}}}{d t} = \dot {\phi} \hat {\boldsymbol {\phi}}.\tag{1.42}
$$

![](images/c393474898f9bfa6b79b89e1545d776c49f010b2f6cc5b3384046f42773cc196.jpg)  
Figure 1.12 (a) The positions of a particle at two successive times, $t_{1}$ and $t_{2}$ . Unless the particle is moving exactly radially, the corresponding unit vectors $\hat{\mathbf{r}}(t_{1})$ and $\hat{\mathbf{r}}(t_{2})$ point in different directions. (b) The change $\Delta\hat{r}$ in $\hat{r}$ is given by the triangle shown.

(For an alternative proof of this important result, see Problem 1.43.) Notice that $d\hat{\mathbf{r}} / dt$ is in the direction of $\hat{\phi}$ and is proportional to the rate of change of the angle $\phi$ — both of which properties we would expect based on Figure 1.12.

Now that we know the derivative of $\hat{r}$ , we are ready to differentiate Equation (1.40). Using the product rule, we get two terms:

$$
\dot {\mathbf {r}} = \dot {r} \hat {\mathbf {r}} + r \frac {d \hat {\mathbf {r}}}{d t},
$$

and, substituting (1.42), we find for the velocity $\dot{r}$ , or v,

$$
\mathbf {v} \equiv \dot {\mathbf {r}} = \dot {r} \hat {\mathbf {r}} + r \dot {\phi} \hat {\boldsymbol {\phi}}.\tag{1.43}
$$

From this we can read off the polar components of the velocity:

$$
v _ {r} = \dot {r} \quad \text { and } \quad v _ {\phi} = r \dot {\phi} = r \omega\tag{1.44}
$$

where in the second equation I have introduced the traditional notation $\omega$ for the angular velocity $\dot{\phi}$ . While the results in (1.44) should be familiar from your introductory physics course, they are undeniably more complicated than the corresponding results in Cartesian coordinates ( $v_{x} = \dot{x}$ and $v_{y} = \dot{y}$ ).

Before we can write down Newton's second law, we have to differentiate a second time to find the acceleration:

$$
\mathbf {a} \equiv \ddot {\mathbf {r}} = \frac {d}{d t} \dot {\mathbf {r}} = \frac {d}{d t} (\dot {r} \hat {\mathbf {r}} + r \dot {\phi} \hat {\boldsymbol {\phi}}),\tag{1.45}
$$

where the final expression comes from substituting (1.43) for $\dot{\mathbf{r}}$ . To complete the differentiation in (1.45), we must calculate the derivative of $\hat{\phi}$ . This calculation is completely analogous to the argument leading to (1.42) and is illustrated in Figure 1.13. By inspecting this figure, you should be able to convince yourself that

$$
\frac {d \hat {\phi}}{d t} = - \dot {\phi} \hat {\mathbf {r}}.\tag{1.46}
$$

(a)

![](images/e717237e0ac3f411dfa9c156221798934a1db4ea7eb931a73e7f2d3421678084.jpg)

![](images/62b490f738930275ee8620225be875d11dad1d30f63eec91b407ad5a74568a14.jpg)  
(b)  
Figure 1.13 (a) The unit vector $\hat{\phi}$ at two successive times $t_1$ and $t_2$ . (b) The change $\Delta \hat{\phi}$ .

Returning to Equation (1.45), we can now carry out the differentiation to give the following five terms:

$$
\mathbf {a} = \left(\ddot {r} \hat {\mathbf {r}} + \dot {r} \frac {d \hat {\mathbf {r}}}{d t}\right) + \left((\dot {r} \dot {\phi} + r \ddot {\phi}) \hat {\boldsymbol {\phi}} + r \dot {\phi} \frac {d \hat {\boldsymbol {\phi}}}{d t}\right)
$$

or, if we use (1.42) and (1.46) to replace the derivatives of the two unit vectors,

$$
\mathbf {a} = \left(\ddot {r} - r \dot {\phi} ^ {2}\right) \hat {\mathbf {r}} + \left(r \ddot {\phi} + 2 \dot {r} \dot {\phi}\right) \hat {\boldsymbol {\phi}}.\tag{1.47}
$$

This horrible result is a little easier to understand if we consider the special case that $r$ is constant, as is the case for a stone that I twirl on the end of a string of fixed length. With $r$ constant, both derivatives of $r$ are zero, and (1.47) has just two terms:

$$
\mathbf {a} = - r \dot {\phi} ^ {2} \hat {\mathbf {r}} + r \ddot {\phi} \hat {\boldsymbol {\phi}}
$$

or

$$
\mathbf {a} = - r \omega^ {2} \hat {\mathbf {r}} + r \alpha \hat {\boldsymbol {\phi}},
$$

where $\omega = \dot{\phi}$ denotes the angular velocity and $\alpha = \ddot{\phi}$ is the angular acceleration. This is the familiar result from elementary physics that when a particle moves around a fixed circle, it has an inward “centripetal” acceleration $r\omega^{2}$ (or $v^{2}/r$ ) and a tangential acceleration, $r\alpha$ . Nevertheless, when r is not constant, the acceleration includes all four of the terms in (1.47). The first term, $\ddot{r}$ in the radial direction is what you would probably expect when r varies, but the final term, $2\dot{r}\dot{\phi}$ in the $\phi$ direction, is harder to understand. It is called the Coriolis acceleration, and I shall discuss it in detail in Chapter 9.

Having calculated the acceleration as in (1.47), we can finally write down Newton's second law in terms of polar coordinates:

$$
\mathbf {F} = m \mathbf {a} \qquad \Longleftrightarrow \qquad \left\{ \begin{array}{l} F _ {r} = m (\ddot {r} - r \dot {\phi} ^ {2}) \\ F _ {\phi} = m (r \ddot {\phi} + 2 \dot {r} \dot {\phi}). \end{array} \right.\tag{1.48}
$$

These equations in polar coordinates are a far cry from the beautifully simple equations (1.35) for rectangular coordinates. In fact, one of the main reasons for taking the trouble to recast Newtonian mechanics in the Lagrangian formulation (Chapter 7) is that the latter is able to handle nonrectangular coordinates just as easily as rectangular.

You may justifiably be feeling that the second law in polar coordinates is so complicated that there could be no occasion to use it. In fact, however, there are many problems which are most easily solved using polar coordinates, and I conclude this section with an elementary example.

## EXAMPLE 1.2 An Oscillating Skateboard

A “half-pipe” at a skateboard park consists of a concrete trough with a semicircular cross section of radius $R = 5 \, m$ , as shown in Figure 1.14. I hold a frictionless skateboard on the side of the trough pointing down toward the bottom and release it. Discuss the subsequent motion using Newton’s second law. In particular, if I release the board just a short way from the bottom, how long will it take to come back to the point of release?

Because the skateboard is constrained to move on a circular path, this problem is most easily solved using polar coordinates with origin O at the center of the pipe as shown. (At some point in the following calculation, try writing the second law in rectangular coordinates and observe what a tangle you get.) With this choice of polar coordinates, the coordinate r of the skateboard is constant, r = R, and the position of the skateboard is completely specified by the angle $\phi$ . With r constant, the second law (1.48) takes the relatively simple form

$$
F _ {r} = - m R \dot {\phi} ^ {2}\tag{1.49}
$$

and

$$
F _ {\phi} = m R \ddot {\phi}.\tag{1.50}
$$

The two forces on the skateboard are its weight w = mg and the normal force N of the wall, as shown in Figure 1.14. The components of the net force $F = w + N$ are easily seen to be

$$
F _ {r} = m g \cos \phi - N \quad \text { and } \quad F _ {\phi} = - m g \sin \phi .
$$

![](images/d5b7ddea6f9370fe118b77eee586b69efd253af0f88aeed4d71a7465fe84870e.jpg)  
Figure 1.14 A skateboard in a semicircular trough of radius R. The board's position is specified by the angle $\phi$ measured up from the bottom. The two forces on the skateboard are its weight w = mg and the normal force N.

Substituting for $F_{r}$ into (1.49) we get an equation involving N, $\phi$ , and $\dot{\phi}$ . Fortunately, we are not really interested in N, and—even more fortunately—when we substitute for $F_{c}$ into (1.50), we get an equation that does not involve N at all:

$$
- m g \sin \phi = m R \ddot {\phi}
$$

or, canceling the m's and rearranging,

$$
\ddot {\phi} = - \frac {g}{R} \sin \phi .\tag{1.51}
$$

Equation (1.51) is the differential equation for $\phi(t)$ that determines the motion of the skateboard. Qualitatively, we can easily see the kind of motion that it implies. First, if $\phi = 0$ , (1.51) says that $\ddot{\phi} = 0$ . Therefore, if we place the board at rest ( $\dot{\phi} = 0$ ) at the point $\phi = 0$ , the board will never move (unless someone pushes it); that is, $\phi = 0$ is an equilibrium position, as you would certainly have guessed. Next, suppose that at some time, $\phi$ is not zero and, to be definite, suppose that $\phi > 0$ ; that is, the skateboard is on the right-hand side of the half-pipe. In this case, (1.51) implies that $\ddot{\phi} < 0$ , so the acceleration is directed to the left. If the board is moving to the right it must slow down and eventually start moving to the left. $^{15}$ Once it is moving toward the left, it speeds up and returns to the bottom, where it moves over to the left. As soon as the board is on the left, the argument reverses ( $\phi < 0$ , so $\ddot{\phi} > 0$ ) and the board must eventually return to the bottom and move over to the right again. In other words, the differential equation (1.51) implies that the skateboard oscillates back and forth, from right to left and back to the right.

The equation of motion (1.51) cannot be solved in terms of elementary functions, such as polynomials, trigonometric functions, or logs and exponentials. $^{14}$ Thus, if we want more quantitative information about the motion, the simplest course is to use a computer to solve it numerically (see Problem 1.50). However, if the initial angle $\phi_{o}$ is small, we can use the small angle approximation

$$
\sin \phi \approx \phi\tag{1.52}
$$

and, within this approximation, (1.51) becomes

$$
\ddot {\phi} = - \frac {g}{R} \phi\tag{1.53}
$$

which can be solved using elementary functions. [By this stage, you have almost certainly recognized that our discussion of the skateboard problem closely parallels the analysis of the simple pendulum. In particular, the small-angle approximation (1.52) is what let you solve the simple pendulum in your introductory physics course. This parallel is, of course, no accident. Mathematically the two problems are exactly equivalent.] If we define the parameter

$$
\omega = \sqrt {\frac {g}{R}},\tag{1.54}
$$

then (1.53) becomes

$$
\ddot {\phi} = - \omega^ {2} \phi .\tag{1.55}
$$

This is the equation of motion for our skateboard in the small-angle approximation. I would like to discuss its solution in some detail to introduce several ideas that we'll be using again and again in what follows. (If you've studied differential equations before, just see the next three paragraphs as a quick review.)

We first observe that it is easy to find two solutions of the equation (1.55) by inspection (that is, by inspired guessing). The function $\phi(t) = A\sin(\omega t)$ is clearly a solution for any value of the constant $A$ . [Differentiating $\sin(\omega t)$ brings out a factor of $\omega$ and changes the sin to a cos; differentiating it again brings out another $\omega$ and changes the cos back to $-\sin$ . Thus the proposed solution does satisfy $\ddot{\phi} = -\omega^2\phi$ .] Similarly, the function $\phi(t) = B\cos(\omega t)$ is another solution for any constant $B$ . Furthermore, as you can easily check, the sum of these two solutions is itself a solution. Thus we have now found a whole family of solutions:

$$
\phi (t) = A \sin (\omega t) + B \cos (\omega t)\tag{1.56}
$$

is a solution for any values of the two constants A and B.

I now want to argue that every solution of the equation of motion (1.55) has the form (1.56). In other words, (1.56) is the general solution — we have found all solutions, and we need seek no further. To get some idea of why this is, note that the differential equation (1.55) is a statement about the second derivative $\ddot{\phi}$ of the unknown $\phi$ . Now, if we had actually been told what $\ddot{\phi}$ is, then we know from elementary calculus that we could find $\phi$ by two integrations, and the result would contain two unknown constants — the two constants of integration — that would have to be determined by looking (for example) at the initial values of $\phi$ and $\dot{\phi}$ . In other words, knowledge of $\ddot{\phi}$ would tell us that $\phi$ itself is one of a family of functions containing precisely two undetermined constants. Of course, the differential equation (1.55) does not actually tell us $\ddot{\phi}$ — it is an equation for $\ddot{\phi}$ in terms of $\phi$ . Nevertheless, it is plausible that such an equation would imply that $\phi$ is one of a family of functions that contain precisely two undetermined constants. If you have studied differential equations, you know that this is the case; if you have not, then I must ask you to accept it as a plausible fact: For any given second-order differential equation [in a large class of “reasonable” equations, including (1.55) and all of the equations we shall encounter in this book], the solutions all belong to a family of functions containing precisely two independent constants — like the constants A and B in (1.56). (More generally, the solutions of an nth-order equation contain precisely n independent constants.)

This theorem sheds a new light on our solution (1.56). We already knew that any function of the form (1.56) is a solution of the equation of motion. Our theorem now guarantees that every solution of the equation of motion is of this form. This same argument applies to all the second-order differential equations we shall encounter. If, by hook or by crook, we can find a solution like (1.56) involving two arbitrary constants, then we are guaranteed that we have found the general solution of our equation.

All that remains is to pin down the two constants A and B for our skateboard. To do so, we must look at the initial conditions. At t = 0, Equation (1.56) implies that $\phi = B$ . Therefore B is just the initial value of $\phi$ , which we are calling $\phi_{0}$ , so $B = \phi_{0}$ . At t = 0, Equation (1.56) implies that $\dot{\phi} = \omega A$ . Since I released the board from rest, this means that A = 0, and our solution is

$$
\phi (t) = \phi_ {0} \cos (\omega t).\tag{1.57}
$$

The first thing to note about this solution is that, as we anticipated on general grounds, $\phi(t)$ oscillates, moving from positive to negative and back to positive periodically and indefinitely. In particular, the board first returns to its initial position $\phi_{0}$ when $\omega t = 2\pi$ . The time that this takes is called the period of the motion and is denoted $\tau$ . Thus our conclusion is that the period of the skateboard's oscillations is

$$
\tau = \frac {2 \pi}{\omega} = 2 \pi \sqrt {\frac {R}{g}}.\tag{1.58}
$$

We were given that R = 5 m, and $g = 9.8 \, m/s^{2}$ . Substituting these numbers, we conclude that the skateboard returns to its starting point in a time $\tau = 4.5$ seconds.

## Principal Definitions and Equations of Chapter 1

Dot and Cross Products

$$
\mathbf {r} \cdot \mathbf {s} = r s \cos \theta = r _ {x} s _ {x} + r _ {y} s _ {y} + r _ {z} s _ {z} \quad [ \text { Eqs. } (1. 6) \& (1. 7) ]
$$

$$
\mathbf {r} \times \mathbf {s} = \left(r _ {y} s _ {z} - r _ {z} s _ {y}, r _ {z} s _ {x} - r _ {x} s _ {z}, r _ {x} s _ {x} - r _ {y} s _ {x}\right) = \det \left[ \begin{array}{c c c} \hat {\mathbf {x}} & \hat {\mathbf {y}} & \hat {\mathbf {z}} \\ r _ {x} & r _ {y} & r _ {z} \\ s _ {1} & s _ {2} & s _ {z} \end{array} \right]\tag{[Eq. (1.9)]}
$$

## Inertial Frames

An inertial frame is any reference frame in which Newton's first law holds, that is, a nonaccelerating, nonrotating frame.

## Unit Vectors of a Coordinate System

If $(\xi, \eta, \zeta)$ are an orthogonal system of coordinates, then

$\hat{\xi}=$ unit vector in direction of increasing $\xi$ with $\eta$ and $\zeta$ fixed and so on, and any vector s can be expanded as $s=s_{\xi}\hat{\xi}+s_{\eta}\hat{\eta}+s_{\zeta}\hat{\zeta}$ .

Newton's Second Law in Various Coordinate Systems

<table><tr><td>Vector Form</td><td>Cartesian $(x, y, z)$ </td><td>2D Polar $(r, \phi)$ </td><td>Cylindrical Polar $(\rho, \phi, z)$ </td></tr><tr><td> $\mathbf{F} = m\ddot{\mathbf{r}}$ </td><td> $\begin{cases} F_{1} = m\ddot{x} \\ F_{y} = m\ddot{y} \\ F_{z} = m\ddot{z} \end{cases}$ Eq. (1.35)</td><td> $\begin{cases} F_{r} = m(\ddot{r} - r\dot{\phi}^{2}) \\ F_{\phi} = m(r\ddot{\phi} + 2\dot{r}\dot{\phi}) \end{cases}$ Eq. (1.48)</td><td> $\begin{cases} F_{r} = m(\ddot{\rho} - \rho\dot{\phi}^{2}) \\ F_{\phi} = m(\rho\ddot{\phi} + 2\dot{\rho}\dot{\phi}) \\ F_{z} = m\ddot{z} \end{cases}$ Problem 1.47 or 1.48</td></tr></table>

## Problems for Chapter 1

The problems for each chapter are arranged according to section number. A problem listed for a given section requires an understanding of that section and earlier sections, but not of later sections. Within each section problems are listed in approximate order of difficulty. A single star ( $\star$ ) indicates straightforward problems involving just one main concept. Two stars ( $\star\star$ ) identify problems that are slightly more challenging and usually involve more than one concept. Three stars ( $\star\star\star$ ) indicate problems that are distinctly more challenging, either because they are intrinsically difficult or involve lengthy calculations. Needless to say, these distinctions are hard to draw and are only approximate.

Problems that need the use of a computer are flagged thus: [Computer]. These are mostly classified as ★★★ on the grounds that it usually takes a long time to set up the necessary code — especially if you're just learning the language.

## SECTION 1.2 Space and Time

1.1 ★ Given the two vectors $b = \hat{x} + \hat{y}$ and $c = \hat{x} + \hat{z}$ find $b + c, 5b + 2c, b \cdot c$ , and $b \times c$ .

1.2 \* Two vectors are given as $\mathbf{b} = (1, 2, 3)$ and $\mathbf{c} = (3, 2, 1)$ . (Remember that these statements are just a compact way of giving you the components of the vectors.) Find $\mathbf{b} + \mathbf{c}, 5\mathbf{b} - 2\mathbf{c}, \mathbf{b} \cdot \mathbf{c}$ , and $\mathbf{b} \times \mathbf{c}$ .

1.3 $\star$ By applying Pythagoras's theorem (the usual two-dimensional version) twice over, prove that the length $r$ of a three-dimensional vector $\mathbf{r} = (x,y,z)$ satisfies $r^2 = x^2 +y^2 +z^2$ .

1.4 \* One of the many uses of the scalar product is to find the angle between two given vectors. Find the angle between the vectors b = (1, 2, 4) and c = (4, 2, 1), by evaluating their scalar product.

1.5 • Find the angle between a body diagonal of a cube and any one of its face diagonals. [Hint: Choose a cube with side 1 and with one corner at O and the opposite corner at the point (1, 1, 1). Write down the vector that represents a body diagonal and another that represents a face diagonal, and then find the angle between them as in Problem 1.4.]

1.6 By evaluating their dot product, find the values of the scalar s for which the two vectors b x y and c x y are orthogonal. (Remember that two vectors are orthogonal if and only if their dot product is zero.) Explain your answers with a sketch.

1.7 Prove that the two definitions of the scalar product $\mathbf{r} \cdot \mathbf{s}$ as $r$ is cos $\theta(1.6)$ and $\sum r, s(1.7)$ are equal. One way to do this is to choose your $x$ axes along the direction of $\mathbf{r}$ . [Strictly speaking you should first make sure that the definition (1.7) is independent of the choice of axes. If you like to worry about such niceties, see Problem 1.16.]

1.8 \* (a) Use the definition (1.7) to prove that the scalar product is distributive, that is, $\mathbf{r} \cdot (\mathbf{u} - \mathbf{v}) = \mathbf{r} \cdot \mathbf{u} \cdot \mathbf{r} \cdot \mathbf{v}$ . (b) If $\mathbf{r}$ and $\mathbf{s}$ are vectors that depend on time, prove that the product rule for differentiating products applies to $\mathbf{r} \cdot \mathbf{s}$ , that is, that

$$
\frac {d}{d t} (\mathbf {r} \cdot \mathbf {s}) = \mathbf {r} \cdot \frac {d \mathbf {s}}{d t} + \frac {d \mathbf {r}}{d t} \cdot \mathbf {s}.
$$

1.9 In elementary trigonometry, you probably learned the law of cosines for a triangle of sides $a$ , $b$ , and $c$ , that $c^2 = a^2 + b^2 - 2ab\cos \theta$ , where $\theta$ is the angle between the sides $a$ and $b$ . Show that the law of cosines is an immediate consequence of the identity $(\mathbf{a} + \mathbf{b})^2 = a^2 + b^2 + 2\mathbf{a} \cdot \mathbf{b}$ .

1.10 \* A particle moves in a circle (center O and radius R) with constant angular velocity ω counterclockwise. The circle lies in the xy plane and the particle is on the x axis at time t = 0. Show that the particle's position is given by

$$
\mathbf {r} (t) = \hat {\mathbf {x}} R \cos (\omega t) + \hat {\mathbf {y}} R \sin (\omega t).
$$

Find the particle's velocity and acceleration. What are the magnitude and direction of the acceleration? Relate your results to well-known properties of uniform circular motion.

1.11 \* The position of a moving particle is given as a function of time t to be

$$
\mathbf {r} (t) = \hat {\mathbf {x}} b \cos (\omega t) + \hat {\mathbf {y}} c \sin (\omega t),
$$

where $b, c$ , and $\omega$ are constants. Describe the particle's orbit.

1.12 \* The position of a moving particle is given as a function of time t to be

$$
\mathbf {r} (t) = \hat {\mathbf {x}} b \cos (\omega t) + \hat {\mathbf {y}} c \sin (\omega t) + \hat {\mathbf {z}} v _ {0} t
$$

where $b, c, v_{0}$ and $\omega$ are constants. Describe the particle's orbit.

1.13 $\star$ Let $\mathbf{u}$ be an arbitrary fixed unit vector and show that any vector $\mathbf{b}$ satisfies

$$
b ^ {2} = (\mathbf {u} \cdot \mathbf {b}) ^ {2} + (\mathbf {u} \times \mathbf {b}) ^ {2}.
$$

Explain this result in words, with the help of a picture.

1.14 \* Prove that for any two vectors a and b,

$$
| \mathbf {a} + \mathbf {b} | \leq (a + b).
$$

[Hint: Work out $|a + b|^{2}$ and compare it with $(a + b)^{2}$ .] Explain why this is called the triangle inequality.

1.15 \* Show that the definition (1.9) of the cross product is equivalent to the elementary definition that $\mathbf{r} \times \mathbf{s}$ is perpendicular to both $\mathbf{r}$ and $\mathbf{s}$ , with magnitude $rs\sin\theta$ and direction given by the right-hand rule. [Hint: It is a fact (though quite hard to prove) that the definition (1.9) is independent of your choice of axes. Therefore you can choose axes so that $\mathbf{r}$ points along the $x$ axis and $\mathbf{s}$ lies in the $xy$ plane.]

1.16\*\* (a) Defining the scalar product $\mathbf{r} \cdot \mathbf{s}$ by Equation (1.7), $\mathbf{r} \cdot \mathbf{s} = \sum r_i s_i$ , show that Pythagoras's theorem implies that the magnitude of any vector $\mathbf{r}$ is $r = \sqrt{\mathbf{r} \cdot \mathbf{r}}$ . (b) It is clear that the length of a vector does not depend on our choice of coordinate axes. Thus the result of part (a) guarantees that the scalar product $\mathbf{r} \cdot \mathbf{r}$ , as defined by (1.7), is the same for any choice of orthogonal axes. Use this to prove that $\mathbf{r} \cdot \mathbf{s}$ , as defined by (1.7), is the same for any choice of orthogonal axes. [Hint: Consider the length of the vector $\mathbf{r} + \mathbf{s}$ .]

1.17 \*\* (a) Prove that the vector product $\mathbf{r} \times \mathbf{s}$ as defined by (1.9) is distributive; that is, that $\mathbf{r} \times (\mathbf{u} + \mathbf{v}) = (\mathbf{r} \times \mathbf{u}) + (\mathbf{r} \times \mathbf{v})$ . (b) Prove the product rule

$$
\frac {d}{d t} (\mathbf {r} \times \mathbf {s}) = \mathbf {r} \times \frac {d \mathbf {s}}{d t} + \frac {d \mathbf {r}}{d t} \times \mathbf {s}.
$$

Be careful with the order of the factors.

1.18 \*\* The three vectors a, b, c are the three sides of the triangle $ABC$ with angles $\alpha, \beta, \gamma$ as shown in Figure 1.15. (a) Prove that the area of the triangle is given by any one of these three expressions:

$$
\text { area } = \frac {1}{2} | \mathbf {a} \times \mathbf {b} | = \frac {1}{2} | \mathbf {b} \times \mathbf {c} | = \frac {1}{2} | \mathbf {c} \times \mathbf {a} |.
$$

(b) Use the equality of these three expressions to prove the so-called law of sines, that

$$
\frac {a}{\sin \alpha} = \frac {b}{\sin \beta} = \frac {c}{\sin \gamma}.
$$

![](images/c8c3a05b5b7b40cba69ab7ab2b127f0e0b6358bac68391f6a23e740d8a5b4514.jpg)  
Figure 1.15 Triangle for Problem 1.18.

1.19 $\star \star$ If $\mathbf{r},\mathbf{v},\mathbf{a}$ denote the position, velocity, and acceleration of a particle, prove that

$$
\frac {d}{d t} [ \mathbf {a} \cdot (\mathbf {v} \times \mathbf {r}) ] = \dot {\mathbf {a}} \cdot (\mathbf {v} \times \mathbf {r}).
$$

1.20 \*\* The three vectors A, B, C point from the origin O to the three corners of a triangle. Use the result of Problem 1.18 to show that the area of the triangle is given by

$$
\text {(area of triangle)} = \frac {1}{2} | (\mathbf {B} \times \mathbf {C}) + (\mathbf {C} \times \mathbf {A}) + (\mathbf {A} \times \mathbf {B}) |.
$$

1.21 \*\* A parallelepiped (a six-faced solid with opposite faces parallel) has one corner at the origin O and the three edges that emanate from O defined by vectors a, b, c. Show that the volume of the parallelepiped is $|\mathbf{a} \cdot (\mathbf{b} \times \mathbf{c})|$ .

1.22 $\star \star$ The two vectors $\mathbf{a}$ and $\mathbf{b}$ lie in the $xy$ plane and make angles $\alpha$ and $\beta$ with the $x$ axis. (a) By evaluating $\mathbf{a} \cdot \mathbf{b}$ in two ways [namely using (1.6) and (1.7)] prove the well-known trig identity

$$
\cos (\alpha - \beta) = \cos \alpha \cos \beta + \sin \alpha \sin \beta .
$$

(b) By similarly evaluating $a \times b$ prove that

$$
\sin (\alpha - \beta) = \sin \alpha \cos \beta - \cos \alpha \sin \beta .
$$

1.23 \*\* The unknown vector v satisfies $b \cdot v = \lambda$ and $b \times v = c$ , where $\lambda$ , b, and c are fixed and known. Find v in terms of $\lambda$ , b, and c.

## SECTION 1.4 Newton's First and Second Laws; Inertial Frames

1.24 \* In case you haven't studied any differential equations before, I shall be introducing the necessary ideas as needed. Here is a simple exercise to get you started: Find the general solution of the first-order equation $df/dt = f$ for an unknown function $f(t)$ . [There are several ways to do this. One is to rewrite the equation as $df/f = dt$ and then integrate both sides.] How many arbitrary constants does the general solution contain? [Your answer should illustrate the important general theorem that the solution to any nth-order differential equation (in a very large class of “reasonable” equations) contains $n$ arbitrary constants.]

## 1.25 ★ Answer the same questions as in Problem 1.24, but for the differential equation df/dt = -3f.

1.26 $\star\star$ The hallmark of an inertial reference frame is that any object which is subject to zero net force will travel in a straight line at constant speed. To illustrate this, consider the following: I am standing on a level floor at the origin of an inertial frame $S$ and kick a frictionless puck due north across the floor. (a) Write down the $x$ and $y$ coordinates of the puck as functions of time as seen from my inertial frame. (Use $x$ and $y$ axes pointing east and north respectively.) Now consider two more observers, the first at rest in a frame $S'$ that travels with constant velocity $v$ due east relative to $S$ , the second at rest in a frame $S''$ that travels with constant acceleration due east relative to $S$ . (All three frames coincide at the moment when I kick the puck, and $S''$ is at rest relative to $S$ at that same moment.) (b) Find the coordinates $x'$ , $y'$ of the puck and describe the puck's path as seen from $S'$ . (c) Do the same for $S''$ . Which of the frames is inertial?

1.27 \*\* The hallmark of an inertial reference frame is that any object which is subject to zero net force will travel in a straight line at constant speed. To illustrate this, consider the following experiment: I am standing on the ground (which we shall take to be an inertial frame) beside a perfectly flat horizontal turntable, rotating with constant angular velocity $\omega$ . I lean over and shove a frictionless puck so that it slides across the turntable, straight through the center. The puck is subject to zero net force and, as seen from my inertial frame, travels in a straight line. Describe the puck's path as observed by someone sitting at rest on the turntable. This requires careful thought, but you should be able to get a qualitative picture. For a quantitative picture, it helps to use polar coordinates; see Problem 1.46.

## SECTION 1.5 The Third Law and Conservation of Momentum

1.28 \* Go over the steps from Equation (1.25) to (1.29) in the proof of conservation of momentum, but treat the case that $N = 3$ and write out all the summations explicitly to be sure you understand the various manipulations.

1.29 \* Do the same tasks as in Problem 1.28 but for the case of four particles (N = 4).

1.30 ★ Conservation laws, such as conservation of momentum, often give a surprising amount of information about the possible outcome of an experiment. Here is perhaps the simplest example: Two objects of masses $m_{1}$ and $m_{2}$ are subject to no external forces. Object 1 is traveling with velocity v when it collides with the stationary object 2. The two objects stick together and move off with common velocity $v'$ . Use conservation of momentum to find $v'$ in terms of v, $m_{1}$ , and $m_{2}$ .

1.31 \* In Section 1.5 we proved that Newton's third law implies the conservation of momentum. Prove the converse, that if the law of conservation of momentum applies to every possible group of particles, then the interparticle forces must obey the third law. [Hint: However many particles your system contains, you can focus your attention on just two of them. (Call them 1 and 2.) The law of conservation of momentum says that if there are no external forces on this pair of particles, then their total momentum must be constant. Use this to prove that $\mathbf{F}_{12} = -\mathbf{F}_{21}$ .]

1.32 \*\* If you have some experience in electromagnetism, you could do the following problem concerning the curious situation illustrated in Figure 1.8. The electric and magnetic fields at a point $\mathbf{r}_1$ due to a charge $q_2$ at $\mathbf{r}_2$ moving with constant velocity $\mathbf{v}_2$ (with $v_2 \ll c$ ) are $^{15}$

$$
\mathbf {E} \left(\mathbf {r} _ {1}\right) = \frac {1}{4 \pi \epsilon_ {0}} \frac {q _ {2}}{s ^ {2}} \hat {\mathbf {s}} \quad \text { and } \quad \mathbf {B} \left(\mathbf {r} _ {1}\right) = \frac {\mu_ {0}}{4 \pi} \frac {q _ {2}}{s ^ {2}} \mathbf {v} _ {2} \times \hat {\mathbf {s}}
$$

where $s = r_{1} - r_{2}$ is the vector pointing from $r_{2}$ to $r_{1}$ . (The first of these you should recognize as Coulomb's law.) If $F_{12}^{el}$ and $F_{12}^{mag}$ denote the electric and magnetic forces on a charge $q_{1}$ at $r_{1}$ with velocity $v_{1}$ , show that $F_{12}^{mag} \leq (v_{1}v_{2}/c^{2})F_{12}^{el}$ . This shows that in the non-relativistic domain it is legitimate to ignore the magnetic force between two moving charges.

1.33 \*\*\* If you have some experience in electromagnetism and with vector calculus, prove that the magnetic forces, $F_{12}$ and $F_{21}$ , between two steady current loops obey Newton's third law. [Hints: Let the two currents be $I_{1}$ and $I_{2}$ and let typical points on the two loops be $r_{1}$ and $r_{2}$ . If $dr_{1}$ and $dr_{2}$ are short segments of the loops, then according to the Biot–Savart law, the force on $dr_{1}$ due to $dr_{2}$ is

$$
\frac {\mu_ {0}}{4 \pi} \frac {I _ {1} I _ {2}}{s ^ {2}} d \mathbf {r} _ {1} \times (d \mathbf {r} _ {2} \times \hat {\mathbf {s}})
$$

where $s = r_{1} - r_{2}$ . The force $F_{12}$ is found by integrating this around both loops. You will need to use the “BAC - CAB” rule to simplify the triple product.]

1.34 \*\*\* Prove that in the absence of external forces, the total angular momentum (defined as $L = \sum_{\alpha} r_{\alpha} \times p_{\alpha}$ ) of an N-particle system is conserved. [Hints: You need to mimic the argument from (1.25) to (1.29). In this case you need more than Newton's third law: In addition you need to assume that the interparticle forces are central; that is, $F_{\alpha\beta}$ acts along the line joining particles $\alpha$ and $\beta$ . A full discussion of angular momentum is given in Chapter 3.]

## SECTION 1.6 Newton's Second Law in Cartesian Coordinates

1.35 \* A golf ball is hit from ground level with speed $v_{0}$ in a direction that is due east and at an angle $\theta$ above the horizontal. Neglecting air resistance, use Newton's second law (1.35) to find the position as a function of time, using coordinates with $x$ measured east, $y$ north, and $z$ vertically up. Find the time for the golf ball to return to the ground and how far it travels in that time.

1.36 $\star$ A plane, which is flying horizontally at a constant speed $v_{0}$ and at a height $h$ above the sea, must drop a bundle of supplies to a castaway on a small raft. (a) Write down Newton's second law for the bundle as it falls from the plane, assuming you can neglect air resistance. Solve your equations to give the bundle's position in flight as a function of time $t$ . (b) How far before the raft (measured horizontally) must the pilot drop the bundle if it is to hit the raft? What is this distance if $v_{0} = 50~\mathrm{m / s}$ , $h = 100~\mathrm{m}$ , and $g \approx 10~\mathrm{m / s^2}$ ? (c) Within what interval of time ( $\pm \Delta t$ ) must the pilot drop the bundle if it is to land within $\pm 10~\mathrm{m}$ of the raft?

1.37 $\star$ A student kicks a frictionless puck with initial speed $v_{0}$ , so that it slides straight up a plane that is inclined at an angle $\theta$ above the horizontal. (a) Write down Newton's second law for the puck and solve to give its position as a function of time. (b) How long will the puck take to return to its starting point?

1.38 $\star$ You lay a rectangular board on the horizontal floor and then tilt the board about one edge until it slopes at angle $\theta$ with the horizontal. Choose your origin at one of the two corners that touch the floor, the $x$ axis pointing along the bottom edge of the board, the $y$ axis pointing up the slope, and the $z$ axis normal to the board. You now kick a frictionless puck that is resting at $O$ so that it slides across the board with initial velocity $(v_{ox}, v_{oy}, 0)$ . Write down Newton's second law using the given coordinates and then find how long the puck takes to return to the floor level and how far it is from $O$ when it does so.

1.39\*\* A ball is thrown with initial speed $v_{\mathrm{o}}$ up an inclined plane. The plane is inclined at an angle $\phi$ above the horizontal, and the ball's initial velocity is at an angle $\theta$ above the plane. Choose axes with $x$ measured up the slope, $y$ normal to the slope, and $z$ across it. Write down Newton's second law using these axes and find the ball's position as a function of time. Show that the ball lands a distance $R = 2v_{\mathrm{o}}^{2}\sin \theta \cos (\theta +\phi) / (g\cos^{2}\phi)$ from its launch point. Show that for given $v_{\mathrm{o}}$ and $\phi$ , the maximum possible range up the inclined plane is $R_{\mathrm{max}} = v_{\mathrm{o}}^{2} / [g(1 + \sin \phi)]$ .

1.40 \*\*\* A cannon shoots a ball at an angle $\theta$ above the horizontal ground. (a) Neglecting air resistance, use Newton's second law to find the ball's position as a function of time. (Use axes with $x$ measured horizontally and $y$ vertically.) (b) Let $r(t)$ denote the ball's distance from the cannon. What is the largest possible value of $\theta$ if $r(t)$ is to increase throughout the ball's flight? [Hint: Using your solution to part (a) you can write down $r^2$ as $x^2 + y^2$ , and then find the condition that $r^2$ is always increasing.]

## SECTION 1.7 Two-Dimensional Polar Coordinates

1.41 \* An astronaut in gravity-free space is twirling a mass $m$ on the end of a string of length $R$ in a circle, with constant angular velocity $\omega$ . Write down Newton's second law (1.48) in polar coordinates and find the tension in the string.

1.42 \* Prove that the transformations from rectangular to polar coordinates and vice versa are given by the four equations (1.37). Explain why the equation for $\phi$ is not quite complete and give a complete version.

1.43★ (a) Prove that the unit vector $\hat{r}$ of two-dimensional polar coordinates is equal to

$$
\hat {\mathbf {r}} = \hat {\mathbf {x}} \cos \phi + \hat {\mathbf {y}} \sin \phi\tag{1.59}
$$

and find a corresponding expression for $\hat{\phi}$ . (b) Assuming that $\phi$ depends on the time $t$ , differentiate your answers in part (a) to give an alternative proof of the results (1.42) and (1.46) for the time derivatives $\hat{\mathbf{r}}$ and $\hat{\phi}$ .

1.44★ Verify by direct substitution that the function $\phi(t)=A\sin(\omega t)+B\cos(\omega t)$ of (1.56) is a solution of the second-order differential equation (1.55), $\ddot{\phi}=-\omega^{2}\phi$ . (Since this solution involves two arbitrary constants—the coefficients of the sine and cosine functions—it is in fact the general solution.)

1.45\*\* Prove that if $\mathbf{v}(t)$ is any vector that depends on time (for example the velocity of a moving particle) but which has constant magnitude, then $\dot{\mathbf{v}}(t)$ is orthogonal to $\mathbf{v}(t)$ . Prove the converse that if $\dot{\mathbf{v}}(t)$ is orthogonal to $\mathbf{v}(t)$ , then $|\mathbf{v}(t)|$ is constant. [Hint: Consider the derivative of $\mathbf{v}^2$ .] This is a very handy result. It explains why, in two-dimensional polars, $d\hat{\mathbf{r}} / dt$ has to be in the direction of $\hat{\phi}$ and vice versa. It also shows that the speed of a charged particle in a magnetic field is constant, since the acceleration is perpendicular to the velocity.

1.46 \*\* Consider the experiment of Problem 1.27, in which a frictionless puck is slid straight across a rotating turntable through the center O. (a) Write down the polar coordinates r, $\phi$ of the puck as functions of time, as measured in the inertial frame S of an observer on the ground. (Assume that the puck was launched along the axis $\phi = 0$ at t = 0.) (b) Now write down the polar coordinates $r'$ , $\phi'$ of the puck as measured by an observer (frame $S'$ ) at rest on the turntable. (Choose these coordinates so that $\phi$ and $\phi'$ coincide at t = 0.) Describe and sketch the path seen by this second observer. Is the frame $S'$ inertial?

1.47\*\* Let the position of a point $P$ in three dimensions be given by the vector $\mathbf{r} = (x, y, z)$ in rectangular (or Cartesian) coordinates. The same position can be specified by cylindrical polar coordinates, $\rho, \phi, z$ , which are defined as follows: Let $P'$ denote the projection of $P$ onto the $xy$ plane; that is, $P'$ has Cartesian coordinates $(x, y, 0)$ . Then $\rho$ and $\phi$ are defined as the two-dimensional polar coordinates of $P'$ in the $xy$ plane, while $z$ is the third Cartesian coordinate, unchanged. (a) Make a sketch to illustrate the three cylindrical coordinates. Give expressions for $\rho, \phi, z$ in terms of the Cartesian coordinates $x, y, z$ . Explain in words what $\rho$ is (" $\rho$ is the distance of $P$ from \_\_\_\_)". There are many variants in notation. For instance, some people use $r$ instead of $\rho$ . Explain why this use of $r$ is unfortunate. (b) Describe the three unit vectors $\hat{\rho}, \hat{\phi}, \hat{z}$ and write the expansion of the position vector $r$ in terms of these unit vectors. (c) Differentiate your last answer twice to find the cylindrical components of the acceleration $a = \ddot{r}$ of the particle. To do this, you will need to know the time derivatives of $\hat{\rho}$ and $\hat{\phi}$ . You could get these from the corresponding two-dimensional results (1.42) and (1.46), or you could derive them directly as in Problem 1.48.

1.48 \*\* Find expressions for the unit vectors $\hat{\rho}$ , $\hat{\phi}$ , and $\hat{z}$ of cylindrical polar coordinates (Problem 1.47) in terms of the Cartesian $\hat{x}$ , $\hat{y}$ , $\hat{z}$ . Differentiate these expressions with respect to time to find $d\hat{\rho}/dt$ , $d\hat{\phi}/dt$ , and $d\hat{z}/dt$ .

1.49 $\star \star$ Imagine two concentric cylinders, centered on the vertical $z$ axis, with radii $R \pm \epsilon$ , where $\epsilon$ is very small. A small frictionless puck of thickness $2\epsilon$ is inserted between the two cylinders, so that it can be considered a point mass that can move freely at a fixed distance from the vertical axis. If we use cylindrical polar coordinates $(\rho, \phi, z)$ for its position (Problem 1.47), then $\rho$ is fixed at $\rho = R$ , while $\phi$ and $z$ can vary at will. Write down and solve Newton's second law for the general motion of the puck, including the effects of gravity. Describe the puck's motion.

1.50 \*\*\* [Computer] The differential equation (1.51) for the skateboard of Example 1.2 cannot be solved in terms of elementary functions, but is easily solved numerically. (a) If you have access to software, such as Mathematica, Maple, or Matlab, that can solve differential equations numerically, solve the differential equation for the case that the board is released from $\phi_{\mathrm{o}} = 20$ degrees, using the values $R = 5\mathrm{m}$ and $g = 9.8\mathrm{m / s^2}$ . Make a plot of $\phi$ against time for two or three periods. (b) On the same picture, plot the approximate solution (1.57) with the same $\phi_{\mathrm{o}} = 20^{\circ}$ . Comment on your two graphs. Note: If you haven't used the numerical solver before, you will need to learn the necessary syntax. For example, in Mathematica you will need to learn the syntax for "NDSolve" and how to plot the solution that it provides. This takes a bit of time, but is something that is very well worth learning.

1.51 \*\*\* [Computer] Repeat all of Problem 1.50 but using the initial value $\phi_0 = \pi /2$ .