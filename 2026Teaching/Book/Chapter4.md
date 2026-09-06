## 4.1 Kinetic Energy and Work

As I have said, there are many different kinds of energy. Perhaps the most basic is kinetic energy (or KE), which for a single particle of mass $m$ traveling with speed $v$ is defined to be

$$
T = \frac {1}{2} m v ^ {2}.\tag{4.1}
$$

Let us imagine the particle moving through space and examine the change in its kinetic energy as it moves between two neighboring points $r_{1}$ and $r_{1} + dr$ on its path as shown in Figure 4.1. The time derivative of T is easily evaluated if we note that $v^{2} = v \cdot v$ , so that

$$
\frac {d T}{d t} = \frac {1}{2} m \frac {d}{d t} (\mathbf {v} \cdot \mathbf {v}) = \frac {1}{2} m (\dot {\mathbf {v}} \cdot \mathbf {v} + \mathbf {v} \cdot \dot {\mathbf {v}}) = m \dot {\mathbf {v}} \cdot \mathbf {v}.\tag{4.2}
$$

![](images/4b48bb9ef76e4f109ab62b8a301cbc062bcdad78407e58f801c3019b785bb19f.jpg)  
Figure 4.1 Three points on the path of a particle: $r_{1}, r_{1} + dr$ (with dr infinitesimal) and $r_{2}$ .

By the second law, the factor $m\dot{v}$ is equal to the net force F on the particle, so that

$$
\frac {d T}{d t} = \mathbf {F} \cdot \mathbf {v}.\tag{4.3}
$$

If we multiply both sides by dt, then since v dt is the displacement dr we find

$$
d T = \mathbf {F} \cdot d \mathbf {r}.\tag{4.4}
$$

The expression on the right, $F \cdot dr$ , is defined to be the work done by the force F in the displacement dr. Thus we have proved the Work–KE theorem, that the change in the particle's kinetic energy between two neighboring points on its path is equal to the work done by the net force as it moves between the two points. $^{1}$

So far we have proved the Work–KE theorem only for an infinitesimal displacement $d\mathbf{r}$ , but it generalizes easily to larger displacements. Consider the two points shown as $\mathbf{r}_1$ and $\mathbf{r}_2$ in Figure 4.1. We can divide the path between these points 1 and 2 into a large number of very small segments, to each of which we can apply the infinitesimal result (4.4). Adding all of these results, we find that the total change in $T$ going from 1 to 2 is the sum $\sum \mathbf{F} \cdot d\mathbf{r}$ of all the infinitesimal works done in all the infinitesimal displacements between points 1 and 2:

$$
\Delta T \equiv T _ {2} - T _ {1} = \sum \mathbf {F} \cdot d \mathbf {r}.\tag{4.5}
$$

In the limit that all the displacements dr go to zero, this sum becomes an integral:

$$
\sum \mathbf {F} \cdot d \mathbf {r} \rightarrow \int_ {1} ^ {2} \mathbf {F} \cdot d \mathbf {r}.\tag{4.6}
$$

This integral, called a line integral, $^{2}$ is a generalization of the integral $f(f(x))dx$ over a single variable x, and its definition as the limit of the sum of many small pieces is closely analogous. If you feel any doubt about the symbol $\int_{1}^{2}\mathbf{F}\cdot dr$ on the right of (4.6), think of it as being just the sum on the left (with all the displacements infinitesimally small). In evaluating a line integral, it is usually possible to convert it into an ordinary integral over a single variable, as the following examples show. Notice that, as the name implies, the line integral depends (in general) on the path that the particle followed from point 1 to point 2. For any force F, the line integral on the right of (4.6) is called the work done by the force F moving between points 1 and 2 along the path concerned.

## EXAMPLE 4.1 Three Line Integrals

Evaluate the line integral for the work done by the two-dimensional force $\mathbf{F} = (y, 2x)$ going from the origin O to the point $P = (1, 1)$ along each of the three paths shown in Figure 4.2. Path a goes from O to $Q = (1, 0)$ along the x axis and then from Q straight up to P, path b goes straight from O to P along the line y = x, and path c goes round a quarter circle centered on Q.

The integral along path a is easily evaluated in two parts, if we note that on OQ the displacements have the form $d\mathbf{r} = (dx, 0)$ , while on QP they are $d\mathbf{r} = (0, dy)$ . Thus

$$
\begin{array}{c} W _ {a} = \int_ {a} \mathbf {F} \cdot d \mathbf {r} = \int_ {O} ^ {Q} \mathbf {F} \cdot d \mathbf {r} + \int_ {Q} ^ {P} \mathbf {F} \cdot d \mathbf {r} = \int_ {0} ^ {1} F _ {x} (x, 0) d x + \int_ {0} ^ {1} F _ {y} (1, y) d y \\ = 0 + 2 \int_ {0} ^ {1} d y = 2. \end{array}
$$

![](images/be3315e198794f77761347875cd735ec8e83effeef050a47aaa42dc9b64f59cf.jpg)  
Figure 4.2 Three different paths, a, b, and c, from the origin to the point $P = (1, 1)$ .

On the path $b, x = y$ , so that $dx = dy$ , and

$$
W _ {b} = \int_ {b} \mathbf {F} \cdot d \mathbf {r} = \int_ {b} (F _ {x} d x + F _ {y} d y) = \int_ {0} ^ {1} (x + 2 x) d x = 1. 5.
$$

Path $c$ is conveniently expressed parametrically as

$$
\mathbf {r} = (x, y) = (1 - \cos \theta , \sin \theta)
$$

where $\theta$ is the angle between OQ and the line from Q to the point $(x, y)$ , with $0 \leq \theta \leq \pi/2$ . Thus on path c

$$
d \mathbf {r} = (d x, d y) = (\sin \theta , \cos \theta) d \theta
$$

and

$$
\begin{array}{l} W _ {c} = \int_ {c} \mathbf {F} \cdot d \mathbf {r} = \int_ {c} (F _ {x} d x + F _ {y} d y) \\ = \int_ {0} ^ {\pi / 2} \left[ \sin^ {2} \theta + 2 (1 - \cos \theta) \cos \theta \right] d \theta = 2 - \pi / 4 = 1. 2 1. \end{array}
$$

Some more examples can be found in Problems 4.2 and 4.3 and, if you have never studied line integrals, you may want to try some of these.

With the notation of the line integral, we can rewrite the result (4.5) as

$$
\Delta T \equiv T _ {2} - T _ {1} = \int_ {1} ^ {2} \mathbf {F} \cdot d \mathbf {r} \equiv W (1 \rightarrow 2)\tag{4.7}
$$

where I have introduced the notation $W(1 \rightarrow 2)$ for the work done by F moving from point 1 to point 2. The result is the Work–KE theorem for arbitrary displacements, large or small: The change in a particle's KE as it moves between points 1 and 2 is the work done by the net force.

It is important to remember that the work that appears on the right of (4.7) is the work done by the net force F on the particle. In general, F is the vector sum of various separate forces

$$
\mathbf {F} = \mathbf {F} _ {1} + \dots + \mathbf {F} _ {n} \equiv \sum_ {i = 1} ^ {n} \mathbf {F} _ {i}.
$$

(For example, the net force on a projectile is the sum of two forces, the weight and air resistance.) It is a most convenient fact that to evaluate the work done by the net force F, we can simply add up the works done by the separate forces $F_{1}, \cdots, F_{n}$ . This claim is easily proved as follows:

$$
\begin{array}{l} W (1 \to 2) = \int_ {1} ^ {2} \mathbf {F} \cdot d \mathbf {r} = \int_ {1} ^ {2} \sum_ {i} \mathbf {F} _ {i} \cdot d \mathbf {r} \\ = \sum_ {i} \int_ {1} ^ {2} \mathbf {F} _ {i} \cdot d \mathbf {r} = \sum_ {i} W _ {i} (1 \to 2). \end{array}\tag{4.8}
$$

The crucial step, from the first line to the second, is justified because the integral of a sum of n terms is the same as the sum of the n individual integrals. The Work–KE theorem can therefore be rewritten as

$$
T _ {2} - T _ {1} = \sum_ {i = 1} ^ {n} W _ {i} (1 \rightarrow 2).\tag{4.9}
$$

In practice, one almost always uses the theorem in this way: Calculate the work $W_{i}$ done by each of the $n$ separate forces on the particle and then set $\Delta T$ equal to the sum of all the $W_{i}$ .

If the net force on a particle is zero, then the Work–KE theorem tells us that the particle's kinetic energy is constant. This simply says that the speed v is constant, which, though true, is not very interesting, since it already follows from Newton's first law.

## 4.2 Potential Energy and Conservative Forces

The next step in the development of the energy formalism is to introduce the notion of potential energy (or PE) corresponding to the forces on an object. As you probably recall, not every force lends itself to the definition of a corresponding potential energy. Those special forces that do have a corresponding potential energy (with the required properties) are called conservative forces, and we must discuss the properties that distinguish conservative from nonconservative forces. Specifically, we shall find that there are two conditions that a force must satisfy to be considered conservative.

To simplify our discussion, let us assume at first that there is only one force acting on the object of interest — the gravitational force on a planet by its sun, or the electric force $q\mathbf{E}$ on a charge in an electric field (with no other forces present). The force $\mathbf{F}$ may depend on many different variables: It may depend on the object's position $\mathbf{r}$ . (The farther the planet is from the sun, the weaker the gravitational pull.) It may depend on the object's velocity, as is the case with air resistance; and it may depend on the time $t$ , as would be the case for a charge in a time-varying electric field. Finally, if the force is exerted by humans, it will depend on a host of imponderables — how tired they are feeling, how conveniently they are situated to push, and so on.

The first condition for a force F to be conservative is that F depends only on the position r of the object on which it acts; it must not depend on the velocity, the time, or any variables other than r. This sounds, and is, quite restrictive, but there are plenty of forces that have this property: The gravitational force of the sun on a planet (position r relative to the sun) can be written as

$$
\mathbf {F} (\mathbf {r}) = - \frac {G m M}{r ^ {2}} \hat {\mathbf {r}}
$$

which evidently depends only on the variable $\mathbf{r}$ . (The parameters $m$ and $M$ — and, of course, the gravitational constant $G$ — are constant for a given planet and given sun.) Similarly, the electrostatic force $\mathbf{F}(\mathbf{r}) = q\mathbf{E}(\mathbf{r})$ on a charge $q$ by a static electric field $\mathbf{E}(\mathbf{r})$ has this property. Forces that do not satisfy this condition include the force of air resistance (which depends on the velocity), friction (which depends on the direction of motion), the magnetic force (which depends on the velocity), and the force of a time-varying electric field $\mathbf{E}(\mathbf{r}, t)$ (which obviously depends on time).

![](images/a1b9612846789b221744932090bc8608475e85939ff73b3ce9b2b4645fc4e108.jpg)  
Figure 4.3 Three different paths, a, b, and c, joining the same two points 1 and 2.

The second condition that a force must satisfy to be called conservative concerns the work done by the force as the object on which it acts moves between two points $r_{1}$ and $r_{2}$ (or just 1 and 2 for short),

$$
W (1 \rightarrow 2) = \int_ {1} ^ {2} \mathbf {F} \cdot d \mathbf {r}.\tag{4.10}
$$

Figure 4.3 shows two points, 1 and 2, and three different paths connecting them. It is entirely possible that the work done between points 1 and 2, as defined by the integral (4.10), has different values depending on which of the three paths, a, b, or c, the particle happens to follow. For example, consider the force of sliding friction as I push a heavy crate across the floor. This force has a constant magnitude, $F_{fric}$ say, and is always opposite to the direction of motion. Thus the work done by friction as the crate moves from 1 to 2 is given by (4.10) to be

$$
W _ {\mathrm{fric}} (1 \rightarrow 2) = - F _ {\mathrm{fric}} L,
$$

where L denotes the length of the path followed. The three paths of Figure 4.3 have different lengths, and $W_{\mathrm{fric}}(1 \rightarrow 2)$ will have a different value for each of the three paths.

On the other hand, there are forces with the property that the work $W(1 \rightarrow 2)$ is the same for any path connecting the same two points 1 and 2. An example of a force with this property is the gravitational force, $F_{grav} = mg$ , of the earth on an object close to the earth's surface. It is easy to show (Problem 4.5) that, because g is a constant vector pointing vertically down, the work done in this case is

$$
W _ {\mathrm{grav}} (1 \rightarrow 2) = - m g h,\tag{4.11}
$$

where h is just the vertical height gained between points 1 and 2. This work is the same for any two paths between the given points 1 and 2. This property, the path independence of the work it does, is the second condition that a force must satisfy to be considered conservative, and we are now ready to state the two conditions:

## Conditions for a Force to be Conservative

A force F acting on a particle is conservative if and only if it satisfies two conditions:

(i) $\mathbf{F}$ depends only on the particle's position $\mathbf{r}$ (and not on the velocity $\mathbf{v}$ , or the time $t$ , or any other variable); that is, $\mathbf{F} = \mathbf{F}(\mathbf{r})$ .

(ii) For any two points 1 and 2, the work $W(1 \to 2)$ done by $\mathbf{F}$ is the same for all paths between 1 and 2.

The reason for the name “conservative” and for the importance of the concept is this: If all forces on an object are conservative, we can define a quantity called the potential energy (or just PE), denoted $U(\mathbf{r})$ , a function only of position, with the property that the total mechanical energy

$$
E = \mathrm{KE} + \mathrm{PE} = T + U (\mathbf {r})\tag{4.12}
$$

is constant; that is, E is conserved.

To define the potential energy $U(\mathbf{r})$ corresponding to a given conservative force, we first choose a reference point $\mathbf{r}_0$ at which $U$ is defined to be zero. (For example, in the case of gravity near the earth's surface, we often define $U$ to be zero at ground level.) We then define $U(\mathbf{r})$ , the potential energy at an arbitrary point $\mathbf{r}$ , to be $^3$

$$
U (\mathbf {r}) = - W \left(\mathbf {r} _ {0} \rightarrow \mathbf {r}\right) \equiv - \int_ {\mathbf {r} _ {0}} ^ {\mathbf {r}} \mathbf {F} \left(\mathbf {r} ^ {\prime}\right) \cdot d \mathbf {r} ^ {\prime}.\tag{4.13}
$$

In words, $U(\mathbf{r})$ is minus the work done by F if the particle moves from the reference point $r_{o}$ to the point of interest r, as in Figure 4.4. (We shall see the reason for the minus sign shortly.) Notice that the definition (4.13) only makes sense because of the property (ii) of conservative forces. If the work integral in (4.13) were different for different paths, then (4.13) would not define a unique function $^{4}$ $U(\mathbf{r})$ .

![](images/318ca6ba73d1694e408bd6d5a3c8a07805dad8e94dd620f7c6e327ede2dd5410.jpg)  
Figure 4.4 The potential energy $U(\mathbf{r})$ at any point r is defined as minus the work done by F if the particle moves from the reference point $r_{0}$ to r. This gives a well-defined function $U(\mathbf{r})$ only if this work is independent of the path followed — that is, the force is conservative.

## EXAMPLE 4.2 Potential Energy of a Charge in a Uniform Electric Field

A charge q is placed in a uniform electric field pointing in the x direction with strength $E_{o}$ , so that the force on q is $F = qE = qE_{o}\hat{x}$ . Show that this force is conservative and find the corresponding potential energy.

The work done by F going between any two points 1 and 2 along any path is

$$
W (1 \rightarrow 2) = \int_ {1} ^ {2} \mathbf {F} \cdot d \mathbf {r} = q E _ {\mathrm{o}} \int_ {1} ^ {2} \hat {\mathbf {x}} \cdot d \mathbf {r} = q E _ {\mathrm{o}} \int_ {1} ^ {2} d x = q E _ {\mathrm{o}} \left(x _ {2} - x _ {1}\right).\tag{4.14}
$$

This depends only on the two end points 1 and 2. (In fact it depends only on their $x$ coordinates $x_{1}$ and $x_{2}$ .) Certainly, it is independent of the path, and the force is conservative. To define the corresponding potential energy $U(\mathbf{r})$ , we must first pick a reference point $\mathbf{r}_{0}$ at which $U$ will be zero. A natural choice is the origin, $\mathbf{r}_{0} = 0$ , in which case the potential energy is $U(\mathbf{r}) = -W(0 \to \mathbf{r})$ or, according to (4.14),

$$
U (\mathbf {r}) = - q E _ {0} x.
$$

We can now derive a crucial expression for the work done by F in terms of the potential energy $U(\mathbf{r})$ . Let $r_{1}$ and $r_{2}$ be any two points as in Figure 4.5. If $r_{0}$ is the reference point at which U is zero, then it is clear from Figure 4.5 that

$$
W (\mathbf {r} _ {0} \rightarrow \mathbf {r} _ {2}) = W (\mathbf {r} _ {0} \rightarrow \mathbf {r} _ {1}) + W (\mathbf {r} _ {1} \rightarrow \mathbf {r} _ {2})
$$

and hence

$$
W (\mathbf {r} _ {1} \rightarrow \mathbf {r} _ {2}) = W (\mathbf {r} _ {0} \rightarrow \mathbf {r} _ {2}) - W (\mathbf {r} _ {0} \rightarrow \mathbf {r} _ {1}).\tag{4.15}
$$

Each of the two terms on the right is (minus) the potential energy at the corresponding point. Thus we have proved that the work on the left is just the difference of these two potential energies:

$$
W (\mathbf {r} _ {1} \rightarrow \mathbf {r} _ {2}) = - [ U (\mathbf {r} _ {2}) - U (\mathbf {r} _ {1}) ] = - \Delta U.\tag{4.16}
$$

![](images/9ae94f5b505f89fa6e79538c4376033501b8642b7b56375574658166a2aab1e0.jpg)  
Figure 4.5 The work $W(\mathbf{r}_{1} \rightarrow \mathbf{r}_{2})$ going from $r_{1}$ to $r_{2}$ is the same as $W(\mathbf{r}_{0} \rightarrow \mathbf{r}_{2})$ minus $W(\mathbf{r}_{0} \rightarrow \mathbf{r}_{1})$ . This result is independent of what path we use for either limb of the journey, provided the force concerned is conservative.

The usefulness of this result emerges when we combine it with the Work–KE theorem (4.7):

$$
\Delta T = W (\mathbf {r} _ {1} \rightarrow \mathbf {r} _ {2}).\tag{4.17}
$$

Comparing this with (4.16), we see that

$$
\Delta T = - \Delta U\tag{4.18}
$$

or, moving the right side across to the left, $^{5}$

$$
\Delta (T + U) = 0.\tag{4.19}
$$

That is, the mechanical energy

$$
E = T + U\tag{4.20}
$$

does not change as the particle moves from $r_{1}$ to $r_{2}$ . Since the points $r_{1}$ and $r_{2}$ were any two points on the particle's trajectory, we have the important conclusion: If the force on a particle is conservative, then the particle's mechanical energy never changes; that is, the particle's energy is conserved, which explains the use of the adjective "conservative."

## Several Forces

So far we have established the conservation of energy for a particle subject to a single conservative force. If the particle is subject to several forces, all of them conservative, our result generalizes easily. For instance, imagine a mass suspended from the ceiling by a spring. This mass is subject to two forces, the forces of gravity ( $F_{grav}$ ) and the spring ( $F_{spr}$ ). The force of gravity is certainly conservative (as I've already argued), and, provided the spring obeys Hooke's law, $F_{spr}$ is likewise (see Problem 4.42). We can define separate potential energies for each force, $U_{grav}$ for $F_{grav}$ and $U_{spr}$ for $F_{spr}$ , each with the crucial property (4.16) that the change in U gives (minus) the work done by the corresponding force. According to the Work–KE theorem, the change in the mass's kinetic energy is

$$
\begin{array}{r l} \Delta T & = W _ {\mathrm{grav}} + W _ {\mathrm{spr}} \\ & = - \left(\Delta U _ {\mathrm{grav}} + \Delta U _ {\mathrm{spr}}\right), \end{array}\tag{4.21}
$$

where the second line follows from the properties of the two separate potential energies. Rearranging this equation, we see that $\Delta(T + U_{\mathrm{grav}} + U_{\mathrm{spr}}) = 0$ . That is, the total mechanical energy, defined as $E = T + U_{grav} + U_{spr}$ , is conserved.

The argument just given extends immediately to the case of n forces on a particle, so long as they are all conservative. If for each force $F_{i}$ we define a corresponding potential energy $U_{i}$ , then we have the

## Principle of Conservation of Energy for One Particle

If all of the n forces $\mathbf{F}_{i}\;(i=1,\cdots,n)$ acting on a particle are conservative, each with its corresponding potential energy $U_{i}(\mathbf{r})$ , the total mechanical energy, defined as

$$
E \equiv T + U \equiv T + U _ {1} (\mathbf {r}) + \dots + U _ {n} (\mathbf {r}),\tag{4.22}
$$

is constant in time.

## Nonconservative Forces

If some of the forces on our particle are nonconservative, then we cannot define corresponding potential energies; nor can we define a conserved mechanical energy. Nevertheless, we can define potential energies for all of the forces that are conservative, and then recast the Work–KE theorem in a form that shows how the nonconservative forces change the particle's mechanical energy. First, we divide the net force on the particle into two parts, the conservative part $F_{cons}$ and the nonconservative part $F_{nc}$ . For $F_{cons}$ , we can define a potential energy, which we'll call just U. By the Work–KE theorem, the change in kinetic energy between any two times is

$$
\Delta T = W = W _ {\mathrm{cons}} + W _ {\mathrm{nc}}.\tag{4.23}
$$

The first term on the right is just $-\Delta U$ and can be moved to the left side to give $\Delta(T + U) = W_{\mathrm{nc}}$ . If we define the mechanical energy as $E = T + U$ , then we see that

$$
\Delta E \equiv \Delta (T + U) = W _ {\mathrm{nc}}.\tag{4.24}
$$

Mechanical energy is no longer conserved, but we have the next best thing. The mechanical energy changes to precisely the extent that the nonconservative forces do work on our particle. In many problems the only nonconservative force is the force of sliding friction, which usually does negative work. (The frictional force f is in the direction opposite to the motion, so the work $f \cdot dr$ is negative.) In this case $W_{nc}$ is negative and (4.24) tells us that the object loses mechanical energy in the amount “stolen” by friction. All of these ideas are illustrated by the following simple example.

## EXAMPLE 4.3 Block Sliding Down an Incline

Consider again the block of Example 1.1 and find its speed v when it reaches the bottom of the slope, a distance d from its starting point.

The setup and the forces on the block are shown in Figure 4.6. The three forces on the block are its weight, w = mg, the normal force of the incline, N, and the frictional force f, whose magnitude we found in Example 1.1 to be $f = \mu mg \cos \theta$ . The weight mg is conservative, and the corresponding potential energy is (as you certainly recall from introductory physics, but see Problem 4.5)

$$
U = m g y
$$

where $y$ is the block's vertical height above the bottom of the slope (if we choose the zero of PE at the bottom). The normal force does no work, since it is perpendicular to the direction of motion, so will not contribute to the energy balance. The frictional force does work $W_{\mathrm{fric}} = -fd = -\mu mgd\cos \theta$ . The change in kinetic energy is $\Delta T = T_{\mathrm{f}} - T_{\mathrm{i}} = \frac{1}{2} mv^2$ and the change in potential energy is $\Delta U = U_{\mathrm{f}} - U_{\mathrm{i}} = -mgh = -mgd\sin \theta$ . Thus (4.24) reads

$$
\Delta T + \Delta U = W _ {\mathrm{fric}}
$$

or

$$
\frac {1}{2} m v ^ {2} - m g d \sin \theta = - \mu m g d \cos \theta .
$$

Solving for v we find

$$
v = \sqrt {2 g d (\sin \theta - \mu \cos \theta)}.
$$

![](images/3e099867defeddf309109dcaed413bc534a6a269f32304fbe7c1d1e147ac538a.jpg)  
Figure 4.6 A block on an incline of angle $\theta$ . The length of the slope is $d$ , and the height is $h = d \sin \theta$ .

As usual, you should check that this answer agrees with common sense. For example, does it give the expected answer when $\theta = 90^{\circ}$ ? What about $\theta = 0$ ? (The case $\theta = 0$ is a bit subtler.)

## 4.3 Force as the Gradient of Potential Energy

We have seen that the potential energy $U(\mathbf{r})$ corresponding to a force $\mathbf{F}(\mathbf{r})$ can be expressed as an integral of $\mathbf{F}(\mathbf{r})$ as in (4.13). This suggests that we should be able to write $\mathbf{F}(\mathbf{r})$ as some kind of derivative of $U(\mathbf{r})$ . This suggestion proves correct, though to implement it we shall need some mathematics that you may not have met before. Specifically, since $\mathbf{F}(\mathbf{r})$ is a vector [while $U(\mathbf{r})$ is a scalar] we shall be involved in some vector calculus.

Let us consider a particle acted on by a conservative force $\mathbf{F}(\mathbf{r})$ , with corresponding potential energy $U(\mathbf{r})$ , and examine the work done by $\mathbf{F}(\mathbf{r})$ in a small displacement from r to $r + dr$ . We can evaluate this work in two ways. On the one hand, it is, by definition,

$$
\begin{array}{c} W (\mathbf {r} \to \mathbf {r} + d \mathbf {r}) = \mathbf {F} (\mathbf {r}) \cdot d \mathbf {r} \\ = F _ {x} d x + F _ {y} d y + F _ {z} d z, \end{array}\tag{4.25}
$$

for any small displacement dr with components (dx, dy, dz).

On the other hand, we have seen that the work $W(\mathbf{r} \rightarrow \mathbf{r} + d\mathbf{r})$ is the same as (minus) the change in PE in the displacement:

$$
\begin{array}{c} W (\mathbf {r} \to \mathbf {r} + d \mathbf {r}) = - d U = - [ U (\mathbf {r} + d \mathbf {r}) - U (\mathbf {r}) ] \\ = - [ U (x + d x, y + d y, z + d z) - U (x, y, z) ]. \end{array}\tag{4.26}
$$

In the second line, I have replaced the position vector $\mathbf{r}$ by its components to emphasize that $U$ is really a function of the three variables $(x, y, z)$ . Now, for functions of one variable, a difference like that in (4.26) can be expressed in terms of the derivative:

$$
d f = f (x + d x) - f (x) = \frac {d f}{d x} d x.\tag{4.27}
$$

This is really no more than the definition of the derivative. $^{6}$ For a function of three variables, such as $U(x, y, z)$ , the corresponding result is

$$
\begin{array}{r l} d U & = U (x + d x, y + d y, z + d z) - U (x, y, z) \\ & = \frac {\partial U}{\partial x} d x + \frac {\partial U}{\partial y} d y + \frac {\partial U}{\partial z} d z \end{array}\tag{4.28}
$$

where the three derivatives are the partial derivatives with respect to the three independent variables $(x, y, z)$ . [For example, $\partial U/\partial x$ is the rate of change of U as x changes, with $y$ and $z$ fixed, and is found by differentiating $U(x, y, z)$ with respect to $x$ treating $y$ and $z$ as constants. See Problems 4.10 and 4.11 for some examples.] Substituting (4.28) into (4.26), we find that the work done in the small displacement from $\mathbf{r}$ to $\mathbf{r} + d\mathbf{r}$ is

$$
W (\mathbf {r} \rightarrow \mathbf {r} + d \mathbf {r}) = - \left[ \frac {\partial U}{\partial x} d x + \frac {\partial U}{\partial y} d y + \frac {\partial U}{\partial z} d z \right].\tag{4.29}
$$

The two expressions (4.25) and (4.29) are both valid for any small displacement $dr$ . In particular, we can choose $dr$ to point in the $x$ direction, in which case $dy = dz = 0$ and the last two terms in both (4.25) and (4.29) are zero. Equating the remaining terms, we see that $F_{x} = -\partial U / \partial x$ . By choosing $dr$ to point in the $y$ or $z$ directions, we get corresponding results for $F_{y}$ and $F_{z}$ , and we conclude that

$$
F _ {x} = - \frac {\partial U}{\partial x}, \quad F _ {y} = - \frac {\partial U}{\partial y}, \quad F _ {z} = - \frac {\partial U}{\partial z}.\tag{4.30}
$$

That is, F is the vector whose three components are minus the three partial derivatives of U with respect to x, y, and z. A slightly more compact way to write this result is this:

$$
\mathbf {F} = - \hat {\mathbf {x}} \frac {\partial U}{\partial x} - \hat {\mathbf {y}} \frac {\partial U}{\partial y} - \hat {\mathbf {z}} \frac {\partial U}{\partial z}.\tag{4.31}
$$

Relationships like (4.31) between a vector (F) and a scalar (U) come up over and over again in physics. For example, the electric field E is related to the electrostatic potential V in exactly the same way. More generally, given any scalar $f(\mathbf{r})$ , the vector whose three components are the partial derivatives of $f(\mathbf{r})$ is called the gradient of f, denoted $\nabla f$ :

$$
\nabla f = \hat {\mathbf {x}} \frac {\partial f}{\partial x} + \hat {\mathbf {y}} \frac {\partial f}{\partial y} + \hat {\mathbf {z}} \frac {\partial f}{\partial z}.\tag{4.32}
$$

The symbol $\nabla f$ is pronounced “grad f.” The symbol $\nabla$ by itself is called “grad,” or “del,” or “nabla.” With this notation, (4.31) is abbreviated to

$$
\mathbf {F} = - \nabla U. \tag {4.33}
$$

This important relation gives us the force F in terms of derivatives of U, just as the definition (4.13) gave U as an integral of F. When a force F can be expressed in the form (4.33), we say that F is derivable from a potential energy. Thus, we have shown that any conservative force is derivable from a potential energy. $^{7}$

## EXAMPLE 4.4 Finding F from U

The potential energy of a certain particle is $U = Axy^{2} + B \sin Cz$ , where A, B and C are constants. What is the corresponding force?

To find F we have only to evaluate the three partial derivatives in (4.31). In doing this, you must remember that $\partial U/\partial x$ is found by differentiating with respect to x, treating y and z as constant, and so on. Thus $\partial U/\partial x = Ay^{2}$ , and so on, and the final result is

$$
\mathbf {F} = - (\hat {\mathbf {x}} A y ^ {2} + \hat {\mathbf {y}} 2 A x y + \hat {\mathbf {z}} B C \cos C z).
$$

It is sometimes convenient to remove the $f$ from (4.32) and to write

$$
\nabla = \hat {\mathbf {x}} \frac {\partial}{\partial x} + \hat {\mathbf {y}} \frac {\partial}{\partial y} + \hat {\mathbf {z}} \frac {\partial}{\partial z}.\tag{4.34}
$$

In this view, $\nabla$ is a vector differential operator that can be applied to any scalar f and produces the vector given in (4.32).

A very useful application of the gradient is given by (4.28), whose right-hand side you will recognize as $\nabla U \cdot dr$ . Thus, if we replace U by an arbitrary scalar f, we see that the change in f resulting from a small displacement dr is just

$$
d f = \nabla f \cdot d \mathbf {r}.\tag{4.35}
$$

This useful relation is the three-dimensional analog of Equation (4.27) for a function of one variable. It shows the sense in which the gradient is the three-dimensional equivalent of the ordinary derivative in one dimension.

If you have never met the $\nabla$ notation before, it will take a little getting used to. Meanwhile, you can just think of (4.33) as a convenient shorthand for the three equations (4.30). For practice using the gradient, you could look at Problems 4.12 through 4.19.

## 4.4 The Second Condition that F be Conservative

We have seen that one of the two conditions that a force $\mathbf{F}$ be conservative is that the work $\int_1^2\mathbf{F}\cdot dr$ which it does moving between any two points 1 and 2 must be independent of the path followed. You are certainly to be excused if you don't see how we could test whether a given force has this property. Checking the value of the integral for every pair of points and every path joining those points is indeed a formidable prospect! Fortunately, we never need to do this. There is a simple test, which can be quickly applied to any force that is given in analytic form. This test involves another of the basic concepts of vector calculus, this time the so-called curl of a vector.

It can be shown (though I shall not do so here $^{8}$ ) that a force F has the desired property, that the work it does is independent of path, if and only if

$$
\nabla \times \mathbf {F} = 0\tag{4.36}
$$

everywhere. The quantity $\nabla \times F$ is called the curl of F, or just “curl F,” or “del cross F.” It is defined by taking the cross product of $\nabla$ and F just as if the components of $\nabla$ , namely $(\partial/\partial x, \partial/\partial y, \partial/\partial z)$ , were ordinary numbers. To see what this means, consider first the cross product of two ordinary vectors A and B. In the table below, I have listed the components of A, B, and $A \times B$ :

<table><tr><td>vector</td><td>x component</td><td>y component</td><td>z component</td></tr><tr><td>A</td><td> $A_x$ </td><td> $A_y$ </td><td> $A_z$ </td></tr><tr><td>B</td><td> $B_x$ </td><td> $B_y$ </td><td> $B_z$ </td></tr><tr><td>A × B</td><td> $A_y B_z - A_z B_y$ </td><td> $A_z B_x - A_x B_z$ </td><td> $A_x B_y - A_y B_x$ </td></tr></table>

(4.37)

The components of $\nabla \times F$ are found in exactly the same way, except that the entries in the first row are differential operators. Thus,

$$
\begin{array}{c c c c} \text {vector} & x \text {component} & y \text {component} & z \text {component} \\ \hline \nabla & \partial / \partial x & \partial / \partial y & \partial / \partial z \\ \mathbf {F} & F _ {x} & F _ {y} & F _ {z} \\ \nabla \times \mathbf {F} & \frac {\partial}{\partial y} F _ {z} - \frac {\partial}{\partial z} F _ {y} & \frac {\partial}{\partial z} F _ {x} - \frac {\partial}{\partial x} F _ {z} & \frac {\partial}{\partial x} F _ {y} - \frac {\partial}{\partial y} F _ {x} \end{array}\tag{4.38}
$$

No one would claim that (4.36) is obviously equivalent to the condition that $\int_{1}^{2}F\cdot dr$ is path-independent, but it is, and it provides an easily applied test for the path-independence property, as the following example shows.

## EXAMPLE 4.5 Is the Coulomb Force Conservative?

Consider the force F on a charge q due to a fixed charge Q at the origin. Show that it is conservative and find the corresponding potential energy U. Check that $-\nabla U = F$ .

The force in question is the Coulomb force, as shown in Figure 4.7(a),

$$
\mathbf {F} = \frac {k q Q}{r ^ {2}} \hat {\mathbf {r}} = \frac {\gamma}{r ^ {3}} \mathbf {r}\tag{4.39}
$$

where k denotes the Coulomb force constant, often written as $1/(4\pi\epsilon_{0})$ , and $\gamma$ is just an abbreviation for the constant kqQ. From the last expression we can read off the components of F, and using (4.38) we can calculate the components of $\nabla\times F$ . For example, the x component is

$$
(\nabla \times \mathbf {F}) _ {x} = \frac {\partial}{\partial y} F _ {z} - \frac {\partial}{\partial z} F _ {y} = \frac {\partial}{\partial y} \left(\frac {\gamma z}{r ^ {3}}\right) - \frac {\partial}{\partial \dot {z}} \left(\frac {\gamma y}{r ^ {3}}\right).\tag{4.40}
$$

![](images/a4e4ad910d33dddeb4aee21f810b76115127baaca8164c439435e59c2020400c.jpg)  
Figure 4.7 (a) The Coulomb force $\mathbf{F} = \gamma \hat{\mathbf{r}} / r^2$ of the fixed charge $Q$ on the charge $q$ . (b) The work done by $\mathbf{F}$ as $q$ moves from $\mathbf{r}_0$ to $\mathbf{r}$ can be evaluated following a path that goes radially outward to $P$ and then around a circle to $\mathbf{r}$ .

The two derivatives here are easily evaluated: First, since $\partial z/\partial y = \partial y/\partial z = 0$ , we can rewrite (4.40) as

$$
(\nabla \times \mathbf {F}) _ {x} = \gamma z \left(\frac {\partial}{\partial y} r ^ {- 3}\right) - \gamma y \left(\frac {\partial}{\partial z} r ^ {- 3}\right).\tag{4.41}
$$

Next recall that

$$
r = (x ^ {2} + y ^ {2} + z ^ {2}) ^ {1 / 2},
$$

so that, for example,

$$
\frac {\partial r}{\partial y} = \frac {y}{r}.\tag{4.42}
$$

(Check this one using the chain rule.) We can now evaluate the two remaining derivatives in (4.41) to give (remember the chain rule again)

$$
(\nabla \times \mathbf {F}) _ {x} = \gamma z \left(\frac {- 3}{r ^ {4}} \cdot \frac {y}{r}\right) - \gamma y \left(\frac {- 3}{r ^ {4}} \cdot \frac {z}{r}\right) = 0.
$$

The other two components work in exactly the same way (check it, if you don't believe me), and we conclude that $\nabla \times \mathbf{F} = 0$ . According to the result (4.36), this guarantees that $\mathbf{F}$ satisfies the second condition to be conservative. Since it certainly satisfies the first condition (it depends only on the variable $\mathbf{r}$ ), we have proved that $\mathbf{F}$ is conservative. (The proof that $\nabla \times \mathbf{F} = 0$ is considerably quicker in spherical polar coordinates. See Problem 4.22.)

The potential energy is defined by the work integral (4.13),

$$
U (\mathbf {r}) = - \int_ {\mathbf {r} _ {0}} ^ {\mathbf {r}} \mathbf {F} (\mathbf {r} ^ {\prime}) \cdot d \mathbf {r} ^ {\prime}\tag{4.43}
$$

where $r_{o}$ is the (as yet unspecified) reference point where $U(\mathbf{r}_{\mathrm{o}})=0$ . Fortunately, we know that this integral is independent of path, so we can choose whatever path is most convenient. One possibility is shown in Figure 4.7(b), where I have chosen a path that goes radially outward to the point labeled P and then around a circle (centered on Q) to r. On the first segment, $\mathbf{F}(\mathbf{r}')$ and $d\mathbf{r}^{\prime}$ are collinear, and $\mathbf{F}(\mathbf{r}^{\prime}) \cdot d\mathbf{r}^{\prime} = (\gamma / r'^{2})dr^{\prime}$ . On the second, $\mathbf{F}(\mathbf{r}^{\prime})$ and $dr^{\prime}$ are perpendicular, so no work is done along this segment, and the total work is just that of the first segment,

$$
U (\mathbf {r}) = - \int_ {r _ {0}} ^ {r} \frac {\gamma}{r ^ {\prime 2}} d r ^ {\prime} = \frac {\gamma}{r} - \frac {\gamma}{r _ {0}}.\tag{4.44}
$$

Finally, it is usual in this problem to choose the reference point $r_{0}$ at infinity, so that the second term here is zero. With this choice (and replacing $\gamma$ by kqQ) we arrive at the well-known formula for the potential energy of the charge q due to Q,

$$
U (\mathbf {r}) = U (r) = \frac {k q Q}{r}.\tag{4.45}
$$

Notice that the answer depends only on the magnitude r of the position vector r and not on the direction.

To check $\nabla U$ let us evaluate the x component:

$$
(\nabla U) _ {x} = \frac {\partial}{\partial x} \left(\frac {k q Q}{r}\right) = - \frac {k q Q}{r ^ {2}} \cdot \frac {\partial r}{\partial x}\tag{4.46}
$$

where the last expression follows from the chain rule. The derivative $\partial r / \partial x$ is $x / r$ [compare Equation (4.42)], so

$$
(\nabla U) _ {x} = - k q Q \frac {x}{r ^ {3}} = - F _ {x},
$$

as given by (4.39). The other two components work in exactly the same way, and we have shown that

$$
\nabla U = - \mathbf {F}\tag{4.47}
$$

as required.

## 4.5 Time-Dependent Potential Energy

We sometimes have occasion to study a force $\mathbf{F}(\mathbf{r},t)$ that satisfies the second condition to be conservative ( $\nabla \times F = 0$ ), but, because it is time-dependent, does not satisfy the first condition. In this case, we can still define a potential energy $U(\mathbf{r},t)$ with the property that $F = -\nabla U$ , but it is no longer the case that total mechanical energy, $E = T + U$ , is conserved. Before I justify these claims, let me give an example of this situation. Figure 4.8 shows a small charge q in the vicinity of a charged conducting sphere (for example, a Van de Graaff generator) with a charge $Q(t)$ that is slowly leaking away through the moist air to ground. Because $Q(t)$ changes with time, the force that it exerts on the small charge q is explicitly time-dependent. Nevertheless, the spatial dependence of the force is the same as for the time-independent Coulomb force of Example 4.5 (page 119). Exactly the same analysis as in that example shows that $\nabla \times F = 0$ .

![](images/31e98415d08c507d27cc72683a3dcc3c5a0b9452241369d228a5fc54d5ca6156.jpg)  
Figure 4.8 The charge $Q(t)$ on the conducting sphere is slowly leaking away, so the force on the small charge q varies with time, even if its position r is constant.

Let me now justify the claims made above. First, since $\nabla \times \mathbf{F}(\mathbf{r}, t) = 0$ , the same mathematical theorem quoted in connection with Equation (4.36) guarantees that the work integral $\int_{1}^{2} \mathbf{F}(\mathbf{r}, t) \cdot d\mathbf{r}$ (evaluated at any one time t) is path independent. This means we can define a function $U(\mathbf{r}, t)$ by an integral exactly analogous to (4.13),

$$
U (\mathbf {r}, t) = - \int_ {\mathbf {r} _ {0}} ^ {\mathbf {r}} \mathbf {F} (\mathbf {r} ^ {\prime}, t) \cdot d \mathbf {r} ^ {\prime},\tag{4.48}
$$

and, for the same reasons as before, $\mathbf{F}(\mathbf{r},t) = -\nabla U(\mathbf{r},t)$ . (See Problem 4.27.) In this case, we can say the force F is derivable from the time-dependent potential energy $U(\mathbf{r},t)$ .

So far everything has gone through just as before, but now the story changes. We can define the mechanical energy as $E = T + U$ , but it is no longer true that E is conserved. If you review carefully the argument leading to Equation (4.19), you may be able to see what goes wrong, but we can in any case show directly that $E = T + U$ changes as the particle moves on its path. As before, consider any two neighboring points on the particle's path at times t and $t + dt$ . Exactly as in (4.4), the change in kinetic energy is

$$
d T = \frac {d T}{d t} d t = (m \dot {\mathbf {v}} \cdot \mathbf {v}) d t = \mathbf {F} \cdot d \mathbf {r}.\tag{4.49}
$$

Meanwhile, $U(\mathbf{r}, t) = U(x, y, z, t)$ is a function of four variables $(x, y, z, t)$ and

$$
d U = \frac {\partial U}{\partial x} d x + \frac {\partial U}{\partial y} d y + \frac {\partial U}{\partial z} d z + \frac {\partial U}{\partial t} d t.\tag{4.50}
$$

You will recognize the first three terms on the right as $\nabla U \cdot dr = -F \cdot dr$ . Thus

$$
d U = - \mathbf {F} \cdot d \mathbf {r} + \frac {\partial U}{\partial t} d t.\tag{4.51}
$$

When we add this to Equation (4.49) the first two terms cancel, and we are left with

$$
d (T + U) = \frac {\partial U}{\partial t} d t.\tag{4.52}
$$

Clearly it is only when U is independent of t (that is, $\partial U/\partial t = 0$ ) that the mechanical energy $E = T + U$ is conserved.

Returning to the example of Figure 4.8, we can understand this conclusion and see what has happened to conservation of energy. Imagine that I hold the charge $q$ stationary at the position of Figure 4.8, while the charge on the sphere leaks away. Under these conditions, the KE of $q$ doesn't change, but the potential energy $kqQ(t) / r$ slowly diminishes to zero. Clearly $T + U$ is not constant. However, while mechanical energy is not conserved, total energy is conserved: The loss of mechanical energy is exactly balanced by the gain of thermal energy as the discharge current heats up the surrounding air. This example suggests, what is true, that the potential energy depends explicitly on time in precisely those situations where mechanical energy gets transformed to some other form of energy or to mechanical energy of other bodies external to the system of interest.

## 4.6 Energy for Linear One-Dimensional Systems

So far we have discussed the energy of a particle that is free to move in all three dimensions. Many interesting problems involve an object that is constrained to move in just one dimension, and the analysis of such problems is remarkably simpler than the general case. Oddly enough, there is some ambiguity in what a physicist means by a “one-dimensional system.” Many introductory physics texts start out discussing the motion of a one-dimensional system, by which they mean an object (a railroad car, for instance) that is confined to move on a perfectly straight, or linear, track. In discussing such linear systems, we naturally take the x axis to coincide with the track, and the position of the object is then specified by the single coordinate x. In this section I shall focus on linear one-dimensional systems. However, there are much more complicated systems, such as a roller coaster on its curving track, that are also one-dimensional, inasmuch as their position can be specified by a single parameter (such as the distance of the roller coaster along its track). As I shall discuss in the next section, energy conservation for such curvilinear one-dimensional systems is just as straightforward as for a perfectly straight track.

To begin, let us consider an object constrained to move along a perfectly straight track, which we take to be the x axis. The only component of any force F that can do work is the x component, and we can simply ignore the other two components. Therefore the work done by F is the one-dimensional integral

$$
W (x _ {1} \rightarrow x _ {2}) = \int_ {x _ {1}} ^ {x _ {2}} F _ {x} (x) d x.\tag{4.53}
$$

If the force is to be conservative, $F_{\gamma}$ must satisfy the two usual conditions: (i) It must depend only on the position $x$ [as I have already implied in writing the integral (4.53)]. (ii) The work (4.53) must be independent of path. The remarkable feature of one-dimensional systems is that the first condition already guarantees the second, so the latter is superfluous. To understand this property, you have only to recognize that in one dimension there is only a small choice of paths connecting any two points. Consider, for example, the two points $A$ and $B$ shown in Figure 4.9. The obvious path between points $A$ and $B$ is the path that goes from $A$ directly to $B$ (let's call this path “AB”). Another possibility, shown in the figure, is to go from A past B to C and then back to B (let's call this one “ABC B”). The work done along this path can be broken up as follows:

![](images/2ccb44293f02dba33331aad1ab519ae015529d8a615adc7110825d735ece6bf4.jpg)  
Figure 4.9 The path called ABCB goes from A past B and on to C, then back to B.

$$
W (A B C B) = W (A B) + W (B C) + W (C B).
$$

Now, provided the force depends only on the position x [condition (i)] each increment of work going from B to C is exactly equal (but of opposite sign) to the corresponding contribution going from C to B. That is, the last two terms on the right cancel, and we conclude that

$$
W (A B C B) = W (A B),
$$

as required. One can of course concoct a path from A to B that doubles back and forth many times, but a little thought should convince you that any such path can be broken into a number of segments some of which together traverse the direct path AB exactly once, and all the rest of which cancel in pairs. Thus the work done on any path between A and B is the same as that on the direct path AB, and we have proved that in one dimension the first condition for a force to be conservative guarantees the second.

## Graphs of the Potential Energy

A second useful feature of one-dimensional systems is that with only one independent variable $(x)$ we can plot the potential energy $U(x)$ , and, as we shall see, this makes it easy to visualize the behavior of the system. Assuming all forces on the object are conservative, we define the potential energy as

$$
U (x) = - \int_ {x _ {0}} ^ {x} F _ {x} (x ^ {\prime}) d x ^ {\prime}\tag{4.54}
$$

where $F_{x}$ is the x component of the net force on the particle. For example, for a mass on the end of a spring obeying Hooke's law, the force is $F_{x} = -kx$ , and, if we choose the reference point $x_{0} = 0$ , Equation (4.54) gives the celebrated result

$$
U = \frac {1}{2} k x ^ {2}
$$

for any spring obeying Hooke's law.

Corresponding to the three-dimensional result $F = -\nabla U$ , we have the simpler result in one dimension

$$
F _ {x} = - \frac {d U}{d x}.\tag{4.55}
$$

![](images/958875605d93942f7e83f1b01bd611e1eb61a968143ee83c62fdd8d969da7441.jpg)  
Figure 4.10 The graph of potential energy $U(x)$ against x for any one-dimensional system can be thought of as a picture of a roller coaster track. The force $F_{x} = -dU/dx$ tends to push the object “downhill” as at $x_{1}$ and $x_{2}$ . At the points $x_{3}$ and $x_{4}$ , where $U(x)$ is minimum or maximum, dU/dx = 0 and the force is zero; such points are therefore points of equilibrium.

If we plot the potential energy against x as in Figure 4.10, we can easily see qualitatively how the object has to behave. The direction of the net force is given by (4.55) as “downhill” on the graph of $U(x)$ — to the left at $x_{1}$ and to the right at $x_{2}$ . It follows that the object always accelerates in the “downhill” direction — a property that reminds one of the motion of a roller coaster, which also always accelerates downhill. This analogy is not an accident: For a roller coaster, $U(x)$ is mgh (where h is the height above ground) and the graph of $U(x)$ against x has the same shape as a graph of h against x, which is just a picture of the track. For any one-dimensional system, we can always think about the graph of $U(x)$ as a picture of a roller coaster, and common sense will generally tell us the kind of motion that is possible at different places, as I now describe.

At points, such as $x_{3}$ and $x_{4}$ , where dU/dx = 0 and $U(x)$ is minimum or maximum, the net force is zero, and the object can remain in equilibrium. That is, the condition dU/dx = 0 characterizes points of equilibrium. At $x_{3}$ , where $d^{2}U/dx^{2} > 0$ and $U(x)$ is minimum, a small displacement from equilibrium causes a force which pushes the object back to equilibrium (back to the left on the right of $x_{3}$ , back to the right on the left of $x_{3}$ ). In other words, equilibrium points where $d^{2}U/dx^{2} > 0$ and $U(x)$ is minimum are points of stable equilibrium. At equilibrium points like $x_{4}$ where $d^{2}U/dx^{2} < 0$ and $U'(x)$ is maximum, a small displacement leads to a force away from equilibrium, and the equilibrium is unstable.

If the object is moving then its kinetic energy is positive and its total energy is necessarily greater than $U(x)$ . For example, suppose the object is moving somewhere near the equilibrium point x = b in Figure 4.11. Its total energy has to be greater than $U(b)$ and could, for example, equal the value shown as E in that figure. If the object happens to be on the right of b and moving toward the right, its PE will increase and its KE must therefore decrease until the object reaches the turning point labeled c, where $U(c) = E$ and the KE is zero. At x = c the object stops and, with the force back to the left, it accelerates back toward x = b. It cannot now stop until once again the KE is zero, and this occurs at the turning point a, where $U(a) = E$ and the object accelerates back to the right. Since the whole cycle now repeats itself, we see that if the object starts out between two hills and its energy is lower than the crest of both hills, then the object is trapped in the valley or "well" and oscillates indefinitely between the two turning points where $U(x) = E$ .

![](images/46af08e2e44db9c4ec0068f6d838de982ea57fc6b6d0f3fb7e560781c4e0255c.jpg)  
Figure 4.11 If an object starts out near x = b with the energy E shown, it is trapped in the valley or “well” between the two hills and oscillates between the turning points at x = a and c where $U(x) = E$ and the kinetic energy is zero.

Suppose the object again starts out between the two hills but with energy higher than the crest of the right hill though still lower than the left. In this case, it will escape to the right since $E > U(x)$ everywhere on the right, and it can never stop once it is moving in that direction. Finally, if the energy is higher than both hills, the object can escape in either direction.

These considerations play an important role in many fields. An example from molecular physics is illustrated in Figure 4.12, which shows the potential energy of a typical diatomic molecule, such as HCl, as a function of the distance between the two atoms. This potential energy function governs the radial motion of the hydrogen atom (in the case of HCl) as it vibrates in and out from the much heavier chlorine atom. The zero of energy has been chosen where the two atoms are far apart (at infinity) and at rest. Notice that the independent variable is the interatomic distance r which, by its definition, is always positive, $0 \leq r < \infty$ . As $r \rightarrow 0$ , the potential energy gets very large, indicating that the two atoms repel one another when very close together (because of the Coulomb repulsion of the nuclei). If the energy is positive (E > 0) the H atom can escape to infinity, since there is no “hill” to trap it; the H atom can come in from infinity, but it will stop at the turning point r = a and (in the absence of any mechanism to take up some of its energy) it will move away to infinity again. On the other hand, if E < 0, the H atom is trapped and will oscillate in and out between the two turning points shown at r = b and r = d. The equilibrium separation of the molecule is at the point shown as r = c. It is the states with E < 0 that correspond to what we normally regard as the HCl molecule. To form such a molecule, two separate atoms (with E > 0) must come together to a separation somewhere near r = c, and some process, such as emission of light, must remove enough energy to leave the two atoms trapped with E < 0.

![](images/0815a58bff9dd06e20d5b73b6c2bae174a6a0fec2b97e0d9ef3801135ddbdb2b.jpg)  
Figure 4.12 The potential energy for a typical diatomic molecule such as HCl, plotted as a function of the distance r between the two atoms. If E > 0, the two atoms cannot approach closer than the turning point r = a, but they can move apart to infinity. If E < 0, they are trapped between the turning points at b and d and form a bound molecule. The equilibrium separation is r = c.

## Complete Solution of the Motion

A third remarkable feature of one-dimensional conservative systems is that we can — at least in principle — use the conservation of energy to obtain a complete solution of the motion, that is, to find the position x as a function of time t. Since $E = T + U(x)$ is conserved, with $U(x)$ a known function (in the context of a given problem) and E determined by the initial conditions, we can solve for $T = \frac{1}{2}m\dot{x}^{2} = E - U(x)$ and hence for the velocity $\dot{x}$ as a function of x:

$$
\dot {x} (x) = \pm \sqrt {\frac {2}{m}} \sqrt {E - U (x)}.\tag{4.56}
$$

(Notice that there is an ambiguity in the sign since energy considerations cannot determine the direction of the velocity. For this reason, the method described here usually does not work in a truly three-dimensional problem. In one dimension, you can almost always decide the sign of $\dot{x}$ by inspection, though you must remember to do so.)

Knowing the velocity as a function of $x$ , we can now find $x$ as a function of $t$ , using separation of variables, as follows: We first rewrite the definition $\dot{x} = dx / dt$ as

$$
d t = \frac {d x}{\dot {x}}.
$$

[Since $\dot{x} = \dot{x}(x)$ , this separates the variables $t$ and $x$ .] Next, we can integrate between any initial and final points to give

$$
t _ {\mathrm{f}} - t _ {\mathrm{i}} = \int_ {x _ {\mathrm{i}}} ^ {x _ {\mathrm{f}}} \frac {d x}{\dot {x}}.\tag{4.57}
$$

This gives the time for travel between any initial and final positions of interest. If we substitute for $\dot{x}$ from (4.56) (and assume, to be definite, that $\dot{x}$ is positive) then the time to go from the initial $x_0$ at time 0 to an arbitrary $x$ at time $t$ is

$$
t = \int_ {x _ {0}} ^ {x} \frac {d x ^ {\prime}}{\dot {x} (x ^ {\prime})} = \sqrt {\frac {m}{2}} \int_ {x _ {0}} ^ {x} \frac {d x ^ {\prime}}{\sqrt {E - U (x ^ {\prime})}}.\tag{4.58}
$$

(As usual, I've renamed the variable of integration as $x'$ to avoid confusion with the upper limit $x$ .) The integral (4.58) depends on the particular form of $U(x)$ in the problem at hand. Assuming we can do the integral [and we can at least do it numerically for any given $U(x)$ ], it gives us $t$ as a function of $x$ . Finally we can solve to give $x$ as a function of $t$ , and our solution is complete, as the following simple example illustrates.

## EXAMPLE 4.6 Free Fall

I drop a stone from the top of a tower at time t = 0. Use conservation of energy to find the stone's position x (measured down from the top of the tower, where x = 0) as a function of t. Neglect air resistance.

The only force on the stone is gravity, which is, of course, conservative. The corresponding potential energy is

$$
U (x) = - m g x.
$$

(Remember x is measured downward.) Since the stone is at rest when x = 0, the total energy is E = 0, and according to (4.56) the velocity is

$$
\dot {x} (x) = \sqrt {\frac {2}{m}} \sqrt {E - U (x)} = \sqrt {2 g x}
$$

(a result that is well known from elementary kinematics). Thus

$$
t = \int_ {0} ^ {x} \frac {d x ^ {\prime}}{\dot {x} (x ^ {\prime})} = \int_ {0} ^ {x} \frac {d x ^ {\prime}}{\sqrt {2 g x ^ {\prime}}} = \sqrt {\frac {2 x}{g}}.
$$

As anticipated, this gives $t$ as a function of $x$ , and we can solve to give the familiar result

$$
x = \frac {1}{2} g t ^ {2}.
$$

This simple example, involving the gravitational potential energy $U(x) = -mgx$ , can be solved many different (and some simpler) ways, but the energy method used here can be used for any potential energy function $U(x)$ . In some cases, the integral (4.58) can be evaluated in terms of elementary functions, and we obtain an analytic solution of the problem; for example, if $U(x) = \frac{1}{2}kx^{2}$ (as for a mass on the end of a spring), the integral turns out to be an inverse sine function, which implies that x oscillates sinusoidally with time, as we should expect (see Problem 4.28). For some potential energies, the integral cannot be done in terms of elementary functions, but can nonetheless be related to functions that are tabulated (see Problem 4.38). For some problems, the only way to do the integral (4.58) is to do it numerically.

## 4.7 Curvilinear One-Dimensional Systems

So far the only one-dimensional system I have discussed is an object constrained to move along a linear path, with position specified by the coordinate x. There are other, more general, systems that can equally be said to be one-dimensional, inasmuch as their position is specified by a single number. An example of such a one-dimensional system is a bead threaded on a curved rigid wire as illustrated in Figure 4.13. (Another is a roller coaster confined to a curved track.) The position of the bead can be specified by a single parameter, which we can choose as the distance s, measured along the wire, from a chosen origin O. With this choice of coordinate, the discussion of the curved one-dimensional track parallels closely that of the straight track, as I now show.

The coordinate s of our bead corresponds, of course, to x for a cart on a straight track. The speed of the bead is easily seen to be $\dot{s}$ , and the kinetic energy is therefore just

$$
T = \frac {1}{2} m \dot {s} ^ {2}
$$

as compared to the familiar $\frac{1}{2}m\dot{x}^{2}$ for the straight track. The force is a little more complicated. As our bead moves on the curved wire the net normal force is not zero; on the contrary, the normal force is what constrains the bead to follow its assigned curving path. (For this reason, the normal force is called the force of constraint.) On the other hand, the normal force does no work, and it is the tangential component $F_{tang}$ of the net force that is our chief concern. In particular, it is fairly easy to show (Problem 4.32) that

$$
F _ {\mathrm{tang}} = m \ddot {s}
$$

![](images/121e997c37d360926639172beac4a939ef9db82a8c9587b2e7c22a887e90cb9e.jpg)  
Figure 4.13 An object constrained to move on a curved track can be considered to be a one-dimensional system, with the position specified by the distance s (measured along the track) of the object from an origin O. The system shown is a bead threaded on a stiff wire, bent into a double loop-the-loop.

(just as $F_{\lambda}=m\ddot{x}$ on a straight track). Further, if all the forces on the bead that have a tangential component are conservative, we can define a corresponding potential energy $U(s)$ such that $F_{tang}=-dU/ds$ , and the total mechanical energy $E=T+U(s)$ is constant. The whole discussion of Section 4.6 can now be applied to the bead on a curved wire (or any other object constrained to move on a one-dimensional path). In particular, those points where $U(s)$ is a minimum are points of stable equilibrium, and those where $U(s)$ is maximum are points of unstable equilibrium.

There are many systems that appear to be much more complicated than the bead on a wire, but are nonetheless one-dimensional and can be treated in much the same way. Here is an example.

## EXAMPLE 4.7 Stability of a Cube Balanced on a Cylinder

A hard rubber cylinder of radius $r$ is held fixed with its axis horizontal, and a wooden cube of mass $m$ and side $2b$ is balanced on top of the cylinder, with its center vertically above the cylinder's axis and four of its sides parallel to the axis. The cube cannot slip on the rubber of the cylinder, but it can of course rock from side to side, as shown in Figure 4.14. By examining the cube's potential energy, find out if the equilibrium with the cube centered above the cylinder is stable or unstable.

Let us first note that the system is one-dimensional, since its position as it rocks from side to side can be specified by a single coordinate, for instance the angle $\theta$ through which it has turned. (We could also specify it by the distance s of the cube's center from equilibrium, but the angle is a little more convenient. Either way the system's position is specified by a single coordinate, and our problem is definitely one-dimensional.) The constraining forces are the normal and frictional forces of the cylinder on the cube; that is, these two forces constrain the cube to move only as shown in Figure 4.14. Since neither of these does any work we need not consider them explicitly. The only other force on the cube is gravity, and we know from elementary physics that this is conservative and that the gravitational potential energy is the same as for a point mass at the center of the cube; that is, U = mgh, where h is the height of C above the origin, as shown in Figure 4.14. (See Problem 4.6.) The length of the line shown as OB is just $r + b$ , while the length BC is the distance the cube has rolled around the cylinder, namely $r\theta$ . Therefore $h = (r + b)\cos\theta + r\theta\sin\theta$ and the potential energy is

![](images/24afed55ca990ae988e525d63d562b6603288f457256ec6433bf086252fee292.jpg)  
Figure 4.14 A cube, of side 2b and center C, is placed on a fixed horizontal cylinder of radius r and center O. It is originally put so that C is centered above O, but it can roll from side to side without slipping.

$$
U (\theta) = m g h = m g [ (r + b) \cos \theta + r \theta \sin \theta ].\tag{4.59}
$$

To find the equilibrium position (or positions) we must find the points where $dU/d\theta$ vanishes. (Strictly speaking I haven't proved this very plausible claim yet for this kind of constrained system; I'll discuss it shortly.) The derivative is easily seen to be (check this for yourself)

$$
\frac {d U}{d \theta} = m g [ r \theta \cos \theta - b \sin \theta ].
$$

This vanishes at $\theta = 0$ , confirming the obvious—that $\theta = 0$ is a point of equilibrium. To decide whether this equilibrium is stable, we have only to differentiate again and find the value of $d^{2}U/d\theta^{2}$ at the equilibrium position. This gives (as you should check)

$$
\frac {d ^ {2} U}{d \theta^ {2}} = m g (r - b)\tag{4.60}
$$

(at $\theta = 0$ ). If the cube is smaller than the cylinder (that is, b < r), this second derivative is positive, which means that $U(\theta)$ has a minimum at $\theta = 0$ and the equilibrium is stable; if the cube is balanced on the cylinder, it will remain there indefinitely. On the other hand, if the cube is larger than the cylinder (b > r), the second derivative (4.60) is negative, the equilibrium is unstable, and the smallest disturbance will cause the cube to roll and fall off the cylinder.

## Further Generalizations

There are many other, more complicated systems that are still legitimately described as one dimensional. Such systems may comprise several bodies, but the bodies are joined by struts or strings in such a way that just one parameter is needed to describe the system's position. An example of such a system is the Atwood machine shown in Figure 4.15, which consists of two masses, $m_1$ and $m_2$ , suspended from opposite ends of a massless, inextensible string that passes over a frictionless pulley. (To simplify the discussion, I shall assume the pulley is massless, although it is easy to allow for a mass of the pulley.) The two masses can move up and down, but the forces of the pulley on the string and the string on the masses constrain matters so that the mass $m_2$ can move up only to the extent that $m_1$ moves down by exactly the same distance.

![](images/8795b44a6c06c537a0eb348d057f7034adf3ca6127c21d79c94b2fd364ad0d39.jpg)  
Figure 4.15 An Atwood machine consisting of two masses, $m_{1}$ and $m_{2}$ , suspended by a massless inextensible string that passes over a massless, frictionless pulley. Because the string's length is fixed, the position of the whole system is specified by the distance $x$ of $m_{1}$ below any convenient fixed level. The forces on the two masses are their weights $m_{1}g$ and $m_{2}g$ , and the tension forces $F_{\mathrm{T}}$ (which are equal since the pulley and string are massless).

Thus the position of the whole system can be specified by a single parameter, for example the height x of $m_{1}$ below the pulley's center as shown, and the system is again one-dimensional. $^{9}$

Let us consider the energies of the masses $m_{1}$ and $m_{2}$ . The forces acting on them are gravity and the tension in the string. Since gravity is conservative, we can introduce potential energies $U_{1}$ and $U_{2}$ for the gravitational forces, and our previous considerations imply that in any displacement of the system,

$$
\Delta T _ {1} + \Delta U _ {1} = W _ {1} ^ {\text { ten }}\tag{4.61}
$$

and

$$
\Delta T _ {2} + \Delta U _ {2} = W _ {2} ^ {\text { ten }}.\tag{4.62}
$$

where the terms $W^{ten}$ denote the work done by the tension on $m_{1}$ and $m_{2}$ . Now, in the absence of friction, the tension is the same all along the string. Thus, although the tension certainly does work on the two individual masses, the work done on $m_{1}$ is equal and opposite to that done on $m_{2}$ , when $m_{1}$ moves down and $m_{2}$ moves an equal distance up (or vice versa). That is,

$$
W _ {1} ^ {\text {ten}} = - W _ {2} ^ {\text {ten}}.\tag{4.63}
$$

Thus, if we add the two energy equations (4.61) and (4.62), the terms involving the tension in the string cancel and we are left with

$$
\Delta (T _ {1} + U _ {1} + T _ {2} + U _ {2}) = 0.
$$

That is, the total mechanical energy

$$
E = T _ {1} + U _ {1} + T _ {2} + U _ {2}\tag{4.64}
$$

is conserved. The beauty of this result is that all reference to the constraining forces of the string and pulley has disappeared.

It turns out that many systems which contain several particles that are constrained in some way (by strings, struts, or a track on which they must move, etc.) can be treated in this same way: The constraining forces are crucially important in determining how the system moves, but they do no work on the system as a whole. Thus in considering the total energy of the system, we can simply ignore the constraining forces. In particular, if all other forces are conservative (as with our example of the Atwood machine), we can define a potential energy $U_{\alpha}$ for each particle $\alpha$ , and the total energy

$$
E = \sum_ {\alpha = 1} ^ {N} (T _ {\alpha} + U _ {\alpha})
$$

is constant. If the system is also one-dimensional (position specified by just one parameter, as with the Atwood machine), then all of the considerations of Section 4.6 apply.

A careful discussion of constrained systems is far easier in the Lagrangian formulation of mechanics than in the Newtonian. Thus I shall postpone any further discussion to Chapter 7. In particular, the proof that a stable equilibrium normally corresponds to a minimum of the potential energy (for a large class of constrained systems) is sketched in Problem 7.47.

## 4.8 Central Forces

A three-dimensional situation that has some of the simplicity of one-dimensional problems is a particle that is subject to a central force, that is, a force that is everywhere directed toward or away from a fixed “force center.” If we take the force center to be the origin, a central force has the form

$$
\mathbf {F} (\mathbf {r}) = f (\mathbf {r}) \hat {\mathbf {r}}\tag{4.65}
$$

where the function $f(\mathbf{r})$ gives the magnitude of the force (and is positive if the force is outward and negative if it is inward). An example of a central force is the Coulomb force on a charge $q$ due to a second charge $Q$ at the origin; this has the familiar form

$$
\mathbf {F} (\mathbf {r}) = \frac {k q Q}{r ^ {2}} \hat {\mathbf {r}},\tag{4.66}
$$

which is obviously an example of (4.65), with the magnitude function given by $f(\mathbf{r}) = kqQ/r^{2}$ . The Coulomb force has two additional properties not shared by all central forces: First, as we have proved, it is conservative. Second, it is spherically symmetric or rotationally invariant; that is, the magnitude function $f(\mathbf{r})$ in (4.65) is independent of the direction of r and, hence, has the same value at all points at the same distance from the origin. A compact way to express this second property of spherical symmetry is to observe that the magnitude function $f(\mathbf{r})$ depends only on the magnitude of the vector r and not its direction, so can be written as

$$
f (\mathbf {r}) = f (r).\tag{4.67}
$$

A remarkable feature of central forces is that the two properties just mentioned always go together: A central force that is conservative is automatically spherically symmetric, and, conversely, a central force that is spherically symmetric is automatically conservative. These two results can be proved in several ways, but the most direct proofs involve the use of spherical polar coordinates. Therefore, before offering any proofs, I shall briefly review the definition of these coordinates.

## Spherical Polar Coordinates

The position of any point P is, of course, identified by the vector r pointing from the origin O to P. The vector r can be specified by its Cartesian coordinates $(x, y, z)$ , but in problems involving spherical symmetry it is almost always more convenient to specify r by its spherical polar coordinates $(r, \theta, \phi)$ , as defined in Figure 4.16. The first coordinate r is just the distance of P from the origin; that is, $r = |r|$ , as usual. The angle $\theta$ is the angle between r and the z axis. The angle $\phi$ , often called the azimuth, is the angle from the x axis to the projection of r on the xy plane, as shown. $^{10}$ It is a simple exercise (Problem 4.40) to relate the Cartesian coordinates $(x, y, z)$ to the polar coordinates $(r, \theta, \phi)$ and vice versa. For example, by inspecting Figure 4.16 you should be able to convince yourself that

$$
x = r \sin \theta \cos \phi , \quad y = r \sin \theta \sin \phi , \quad \text { and } \quad z = r \cos \theta .\tag{4.68}
$$

A beautiful use of spherical coordinates, which may help you to visualize them, is to specify positions on the surface of the earth. If we choose the origin at the center of the earth, then all points on the surface have the same value of r, namely the radius of the earth. $^{[1]}$ Thus positions on the surface can be specified by giving just the two angles $(\theta, \phi)$ . If we choose our z axis to coincide with the north polar axis, then it is easy to see from Figure 4.16 that $\theta$ gives the latitude of the point P, measured down from the north pole. (Since latitude is traditionally measured up from the equator, our angle $\theta$ is often called the colatitude.) Similarly, $\phi$ is the longitude measured east from the meridian of the x axis.

![](images/ddcabcac5effee765bf91b3c706a11c25f8bce1f4d22d7822cef445fa15968fd.jpg)  
Figure 4.16 The spherical polar coordinates $(r, \theta, \phi)$ of a point P are defined so that r is the distance of P from the origin, $\theta$ is the angle between the line OP and the z axis, and $\phi$ is the angle of the line OQ from the x axis, where Q is the projection of P onto the xy plane.

The statement that a function $f(\mathbf{r})$ is spherically symmetric is simply the statement that, with r expressed in spherical polars, f is independent of $\theta$ and $\phi$ . This is what we mean when we write $f(\mathbf{r}) = f(r)$ , and the test for spherical symmetry is simply that the two partial derivatives $\partial f/\partial\theta$ and $\partial f/\partial\phi$ are both zero everywhere.

The unit vectors $\hat{\mathbf{r}},\hat{\boldsymbol{\theta}}$ , and $\hat{\phi}$ are defined in the usual way: First, $\hat{\mathbf{r}}$ is the unit vector pointing in the direction of movement if $r$ increases with $\theta$ and $\phi$ fixed. Thus, as shown in Figure 4.17, the vector $\hat{\mathbf{r}}$ points radially outward, and is just the unit vector in the direction of $\mathbf{r}$ as usual. (On the surface of the earth, $\hat{\mathbf{r}}$ points upward, in the direction of the local vertical.) Similarly, $\hat{\boldsymbol{\theta}}$ points in the direction of increasing $\theta$ with $r$ and $\phi$ fixed, that is, southward along a line of longitude. Finally, $\hat{\phi}$ points in the direction of increasing $\phi$ with $r$ and $\theta$ fixed, that is, eastward along a circle of latitude.

Since the three unit vectors $\hat{\mathbf{r}},\hat{\boldsymbol{\theta}}$ , and $\hat{\boldsymbol{\phi}}$ are mutually perpendicular, we can evaluate dot products in spherical polars in just the same way as in Cartesians. Thus, if

$$
\mathbf {a} = a _ {r} \hat {\mathbf {r}} + a _ {\theta} \hat {\pmb {\theta}} + a _ {\phi} \hat {\pmb {\phi}}
$$

and

$$
\mathbf {b} = b _ {r} \hat {\mathbf {r}} + b _ {\theta} \hat {\pmb {\theta}} + b _ {\phi} \hat {\pmb {\phi}}
$$

then (make sure you see this)

$$
\mathbf {a} \cdot \mathbf {b} = a _ {r} b _ {r} + a _ {\theta} b _ {\theta} + a _ {\phi} b _ {\phi}.\tag{4.69}
$$

Like the unit vectors of two-dimensional polar coordinates, the unit vectors $\hat{\mathbf{r}},\hat{\boldsymbol{\theta}}$ and $\hat{\phi}$ vary with position, and, as was the case in two dimensions, this variability complicates many calculations involving differentiation, as we shall now see.

## The Gradient in Spherical Polar Coordinates

In Cartesian coordinates, we have seen that the components of $\nabla f$ are precisely the partial derivatives of f with respect to x, y, and z,

$$
\nabla f = \hat {\mathbf {x}} \frac {\partial f}{\partial x} + \hat {\mathbf {y}} \frac {\partial f}{\partial y} + \hat {\mathbf {z}} \frac {\partial f}{\partial z}.\tag{4.70}
$$

The corresponding expression for $\nabla f$ in polar coordinates is not so straightforward. To find it, recall from (4.35) that, in a small displacement dr, the change in any function $f(\mathbf{r})$ is

$$
d f = \nabla f \cdot d \mathbf {r}.\tag{4.71}
$$

To evaluate the small vector $dr$ in polar coordinates, we must examine carefully what happens to the point $r$ when we change $r, \theta$ , and $\phi$ : A small change $dr$ in $r$ moves the point a distance $dr$ radially out, in the direction of $\hat{r}$ . As you can see from Figure 4.17, a small change $d\theta$ in $\theta$ moves the point around a circle of longitude (radius $r$ ) through a distance $r \, d\theta$ in the direction of $\hat{\theta}$ . (Note well the factor of $r$ — the distance is not just $d\theta$ .) Similarly, a small change $d\phi$ in $\phi$ moves the point around a circle of latitude (radius $r \sin \theta$ ) through a distance $r \sin \theta \, d\phi$ . Putting all this together, we see that

$$
d \mathbf {r} = d r \hat {\mathbf {r}} + r d \theta \hat {\boldsymbol {\theta}} + r \sin \theta d \phi \hat {\boldsymbol {\phi}}.
$$

Knowing the components of dr, we can now evaluate the dot product in (4.71) in terms of the unknown components of $\nabla f$ ,

$$
d f = (\nabla f) _ {r} d r + (\nabla f) _ {\theta} r d \theta + (\nabla f) _ {\phi} r \sin \theta d \phi .\tag{4.72}
$$

![](images/5596a938d548108dd92b4bcdbb46e9e5fbee75b1cd9392f2652f8306ebdb2336.jpg)  
Figure 4.17 The three unit vectors of spherical polar coordinates at the point P. The vector $\hat{r}$ points radially out, $\hat{\theta}$ points “south” along a line of longitude, and $\hat{\phi}$ points “east” around a circle of latitude.

Meanwhile, since $f$ is a function of the three variables $r, \theta, \phi$ , the change in $f$ is, of course,

$$
\dot {d f} = \frac {\partial f}{\partial r} d r + \frac {\partial f}{\partial \theta} d \theta + \frac {\partial f}{\partial \phi} d \phi .\tag{4.73}
$$

Comparing (4.72) and (4.73), we conclude that the components of $\nabla f$ in spherical polars are

$$
(\nabla f) _ {r} = \frac {\partial f}{\partial r}, \qquad (\nabla f) _ {\theta} = \frac {1}{r} \frac {\partial f}{\partial \theta}, \qquad \text { and } \qquad (\nabla f) _ {\phi} = \frac {1}{r \sin \theta} \frac {\partial f}{\partial \phi}\tag{4.74}
$$

or, a little more compactly,

$$
\nabla f = \hat {\mathbf {r}} \frac {\partial f}{\partial r} + \hat {\boldsymbol {\theta}} \frac {1}{r} \frac {\partial f}{\partial \theta} + \hat {\boldsymbol {\phi}} \frac {1}{r \sin \theta} \frac {\partial f}{\partial \phi}.\tag{4.75}
$$

Similar considerations apply to the curl and other operators of vector calculus, all of which are markedly more complicated in spherical polar coordinates (and all other non-Cartesian coordinates) than in Cartesian coordinates. Since the formulas for these operators are very hard to remember, I have listed the more important ones inside the back cover. Proofs can be found in any textbook of vector calculus. $^{12}$ Armed with these ideas, let us return to central forces.

## Conservative and Spherically Symmetric, Central Forces

I claimed earlier that a central force is conservative if and only if it is spherically symmetric. This claim can be proved several different ways. The quickest proofs (though not necessarily the most insightful) use spherical polar coordinates. Let us assume first that the central force $\mathbf{F}(\mathbf{r})$ is conservative and try to prove that it must be spherically symmetric. Since it is conservative, it can be expressed in the form $-\nabla U$ , which according to (4.75), has the form

$$
\mathbf {F} (\mathbf {r}) = - \nabla U = - \hat {\mathbf {r}} \frac {\partial U}{\partial r} - \hat {\boldsymbol {\theta}} \frac {1}{r} \frac {\partial U}{\partial \theta} - \hat {\boldsymbol {\phi}} \frac {1}{r \sin \theta} \frac {\partial U}{\partial \phi}.\tag{4.76}
$$

Since $\mathbf{F}(\mathbf{r})$ is central, only its radial component can be nonzero, and the last two terms in (4.76) must be zero. This requires that $\partial U/\partial\theta = \partial U/\partial\phi = 0$ ; that is, $U(\mathbf{r})$ is spherically symmetric, and (4.76) reduces to

$$
\mathbf {F} (\mathbf {r}) = - \hat {\mathbf {r}} \frac {\partial U}{\partial r}.
$$

Since U is spherically symmetric (depends only on r), the same is true of $\partial U/\partial r$ , and we see that the central force $\mathbf{F}(\mathbf{r})$ is indeed spherically symmetric. I shall leave the proof of the converse result, that a central force which is spherically symmetric is necessarily conservative, to the problems at the end of this chapter. (See Problems 4.43 and 4.44, but the simplest proof mimics almost exactly the analysis of the Coulomb force in Example 4.5.)

The importance of these results is this: First, because a force $\mathbf{F}(\mathbf{r})$ that is central and spherically symmetric has a magnitude that depends only on r, it is nearly as simple as a one-dimensional force. Second, although $\mathbf{F}(\mathbf{r})$ is certainly not actually a one-dimensional force (its direction still depends on $\theta$ and $\phi$ ), we shall see in Chapter 8 that any problem involving this kind of force is mathematically equivalent to a certain related one-dimensional problem.

## 4.9 Energy of Interaction of Two Particles

Almost all of our discussion of energy has focused on the energy of a single particle (or any larger object that can be approximated as a particle). It is now time to extend the discussion to systems of several particles, and I shall naturally start with just two particles. In this section, I shall suppose that the two particles interact via forces $F_{12}$ (on particle 1 by particle 2) and $F_{21}$ (on particle 2 by particle 1), but that there are no other, external, forces. In general, the force $F_{12}$ could depend on the positions of both particles, so can be written as

$$
\mathbf {F} _ {1 2} = \mathbf {F} _ {1 2} (\mathbf {r} _ {1}, \mathbf {r} _ {2}),
$$

and by Newton's third law

$$
\mathbf {F} _ {1 2} = - \mathbf {F} _ {2 1}.
$$

As an example of such a two-particle system we could consider an isolated binary star, in which case the only two forces are the gravitational attraction of each star for the other. If we denote the vector pointing to star 1 from star 2 by r, as in Figure 4.18, the force $F_{12}$ is just the familiar

$$
\mathbf {F} _ {1 2} = - \frac {G m _ {1} m _ {2}}{r ^ {2}} \hat {\mathbf {r}} = - \frac {G m _ {1} m _ {2}}{r ^ {3}} \mathbf {r}.
$$

![](images/620734b939ce1571b35b4e7df13fa6b6e5bd12c5dc1a2853be2e9292e0a9afea.jpg)  
Figure 4.18 The vector r pointing to particle 1 from particle 2 is just $\mathbf{r} = (\mathbf{r}_{1} - \mathbf{r}_{2})$ .

The vector $\mathbf{r}$ can be written in terms of the two positions $\mathbf{r}_1$ and $\mathbf{r}_2$ . In fact, as can be seen in Figure 4.18,

$$
\mathbf {r} = \mathbf {r} _ {1} - \mathbf {r} _ {2}.
$$

Thus the force $F_{12}$ , expressed as a function of $r_{1}$ and $r_{2}$ , is

$$
\mathbf {F} _ {1 2} = - \frac {G m _ {1} m _ {2}}{\left| \mathbf {r} _ {1} - \mathbf {r} _ {2} \right| ^ {3}} \left(\mathbf {r} _ {1} - \mathbf {r} _ {2}\right).\tag{4.77}
$$

A striking property of the force (4.77) is that it depends on the two positions $r_{1}$ and $r_{2}$ only through the particular combination $r_{1}-r_{2}$ . This property is not an accident, and is in fact true of any isolated two-particle system. The reason is that any isolated system must be translationally invariant: If we bodily translate the system to a new position, without changing the relative positions of the particles, the interparticle forces should remain the same. This is illustrated in Figure 4.19, which shows a pair of points $r_{1}$ and $r_{2}$ and a second pair of points $s_{1}$ and $s_{2}$ , with $s_{1}-s_{2}=r_{1}-r_{2}$ . Since the two points $r_{1}$ and $r_{2}$ could be simultaneously translated to $s_{1}$ and $s_{2}$ , the force $\mathbf{F}_{12}(\mathbf{r}_{1},\mathbf{r}_{2})$ must be the same as $\mathbf{F}_{12}(\mathbf{s}_{1},\mathbf{s}_{2})$ for any points satisfying $r_{1}-r_{2}=s_{1}-s_{2}$ . In other words, $\mathbf{F}_{12}(\mathbf{r}_{1},\mathbf{r}_{2})$ depends only on $r_{1}-r_{2}$ , as claimed, and we can write

$$
\mathbf {F} _ {1 2} = \mathbf {F} _ {1 2} (\mathbf {r} _ {1} - \mathbf {r} _ {2}).\tag{4.78}
$$

The result (4.78) greatly simplifies our discussion. We can learn almost everything about the force $F_{12}$ by fixing $r_{2}$ at any convenient point. In particular, let us temporarily fix $r_{2}$ at the origin, in which case (4.78) reduces to just $\mathbf{F}_{12}(\mathbf{r}_{1})$ . (This maneuver amounts to translating both particles until particle 2 is at the origin, and we know that the force is unaffected by any such translation.) With $r_{2}$ fixed, our discussion of the force on a single particle now applies. For example, if the force $F_{12}$ on particle 1 is to be conservative, then it must satisfy

$$
\nabla_ {1} \times \mathbf {F} _ {1 2} = 0\tag{4.79}
$$

![](images/6fcf7115d2a250b8200e73e744a293a18b49b743b7a3b8ff9817807e1e51e96f.jpg)

![](images/6d7b08e672ec76b394987f2accf485893a4666ae8af0e56a535852cd179a37e4.jpg)

Figure 4.19 If $\mathbf{r}_1 - \mathbf{r}_2 = \mathbf{s}_1 - \mathbf{s}_2$ , then two particles at $\mathbf{r}_1$ and $\mathbf{r}_2$ could be bodily translated to $\mathbf{s}_1$ and $\mathbf{s}_2$ without affecting their relative positions. This means that the force between the particles at $\mathbf{r}_1$ and $\mathbf{r}_2$ must be the same as that at $\mathbf{s}_1$ and $\mathbf{s}_2$ .

where $\nabla_{1}$ is the differential operator

$$
\nabla_ {1} = \hat {\mathbf {x}} \frac {\partial}{\partial x _ {1}} + \hat {\mathbf {y}} \frac {\partial}{\partial y _ {1}} + \hat {\mathbf {z}} \frac {\partial}{\partial z _ {1}}
$$

with respect to the coordinates $(x_{1}, y_{1}, z_{1})$ of particle 1. If (4.79) is satisfied, we can define a potential energy $U(\mathbf{r}_{1})$ such that the force on particle 1 is

$$
\mathbf {F} _ {1 2} = - \nabla_ {1} U (\mathbf {r} _ {1}).
$$

This gives the force $F_{12}$ for the case that particle 2 is at the origin. To find it for particle 2 anywhere else we have only to translate back to an arbitrary position by replacing $r_{1}$ with $r_{1}-r_{2}$ to give

$$
\mathbf {F} _ {1 2} = - \nabla_ {1} U (\mathbf {r} _ {1} - \mathbf {r} _ {2}).\tag{4.80}
$$

Notice that I don't have to change the operator $\nabla_{1}$ , since an operator like $\partial/\partial x_{1}$ is unchanged by addition of a constant to $x_{1}$ .

To find the reaction force $\mathbf{F}_{21}$ on particle 2, we have only to invoke Newton's third law, which says that $\mathbf{F}_{21} = -\mathbf{F}_{12}$ . That is, we have only to change the sign of (4.80). We can re-express this by noticing that

$$
\nabla_ {1} U (\mathbf {r} _ {1} - \mathbf {r} _ {2}) = - \nabla_ {2} U (\mathbf {r} _ {1} - \mathbf {r} _ {2}),\tag{4.81}
$$

where $\nabla_{2}$ denotes the gradient with respect to the coordinates of particle 2. (To prove this, invoke the chain rule. See Problem 4.50.) So, instead of changing the sign of (4.80) to find $F_{21}$ , we can simply replace $\nabla_{1}$ by $\nabla_{2}$ to give

$$
\mathbf {F} _ {2 1} = - \nabla_ {2} U (\mathbf {r} _ {1} - \mathbf {r} _ {2}).\tag{4.82}
$$

Equations (4.80) and (4.82) are a beautiful result that generalizes to multiparticle systems. To emphasize what they say, let me rewrite them as

$$
\left. \begin{array}{l} (\text { Force   on   particle   1 }) = - \nabla_ {1} U \\ (\text { Force   on   particle   2 }) = - \nabla_ {2} U. \end{array} \right\}\tag{4.83}
$$

There is a single potential energy function U, from which we can derive both forces. To find the force on particle 1, we just take the gradient of U with respect to the coordinates of particle 1; to find the force on particle 2, we take the gradient with respect to the coordinates of particle 2.

Before generalizing this result to multiparticle systems, let us consider the conservation of energy for our two-particle system. Figure 4.20 shows the orbits of the two particles. During a short time interval dt, particle 1 moves through $dr_{1}$ and particle 2 through $dr_{2}$ , and work is done on both particles by the corresponding forces. By the work–KE theorem

$$
d T _ {1} = (\text { work   on } 1) = d \mathbf {r} _ {1} \cdot \mathbf {F} _ {1 2}
$$

and similarly

$$
d T _ {2} = (\text { work   on   2 }) = d \mathbf {r} _ {2} \cdot \mathbf {F} _ {2 1}.
$$

![](images/5cc4ad2de319cd450f04ee550f5e34cccec759412bbb9cf138c3aad276ccaccd.jpg)  
Figure 4.20 Motion of two interacting particles. During a short time interval dt, particle 1 moves from $r_{1}$ to $r_{1} + dr_{1}$ and particle 2 from $r_{2}$ to $r_{2} + dr_{2}$ .

Adding these, we find for the change in the total kinetic energy $T = T_{1} + T_{2}$ ,

$$
\begin{array}{r l} d T & = d T _ {1} + d T _ {2} = (\text { work   on   1 }) + (\text { work   on   2 }) \\ & = W _ {\text { tot }} \end{array}\tag{4.84}
$$

where

$$
W _ {\mathrm{tot}} = d \mathbf {r} _ {1} \cdot \mathbf {F} _ {1 2} + d \mathbf {r} _ {2} \cdot \mathbf {F} _ {2 1}
$$

denotes the total work done on both particles. Replacing $F_{21}$ by $-F_{12}$ and then replacing $F_{12}$ with (4.80), we can rewrite $W_{tot}$ as

$$
W _ {\mathrm{tot}} = (d \mathbf {r} _ {1} - d \mathbf {r} _ {2}) \cdot \mathbf {F} _ {1 2} = d (\mathbf {r} _ {1} - \mathbf {r} _ {2}) \cdot [ - \nabla_ {1} U (\mathbf {r} _ {1} - \mathbf {r} _ {2}) ].\tag{4.85}
$$

If we rename $(\mathbf{r}_{1}-\mathbf{r}_{2})$ as r, then the right side of this equation can be seen to be just (minus) the change in the potential energy, and we find that $^{13}$

$$
W _ {\mathrm{tot}} = - d \mathbf {r} \cdot \nabla U (\mathbf {r}) = - d U\tag{4.86}
$$

where the last step follows from the property (4.35) of the gradient operator. It is worth pausing to appreciate this important result. The total work $W_{tot}$ is the sum of two terms, the work done by $F_{12}$ as particle 1 moves through $dr_{1}$ plus the work done by $F_{21}$ as particle 2 moves through $dr_{2}$ . According to (4.86), the potential energy U takes both of these terms into account and $W_{tot}$ is simply -dU.

Returning to the total kinetic energy, we now see that according to (4.84) the change dT is just -dU. Moving the term dU to the other side, we conclude that

$$
d (T + U) = 0.
$$

That is, the total energy,

$$
E = T + U = T _ {1} + T _ {2} + U,\tag{4.87}
$$

of our two-particle system is conserved. Note well that the total energy of our two particles contains two kinetic terms (of course), but only one potential term, since U accounts for the work done by both of the forces $F_{12}$ and $F_{21}$ .

## Elastic Collisions

Elastic collisions give a simple application of these ideas. An elastic collision is a collision between two particles (or bodies that can be treated as particles) that interact via a conservative force that goes to zero as their separation $r_{1}-r_{2}$ increases. Since the force goes to zero as $|r_{1}-r_{2}| \rightarrow \infty$ , the potential energy $U(\mathbf{r}_{1}-\mathbf{r}_{2})$ approaches a constant, which we may as well take to be zero. For example, the two particles could be an electron and a proton, or they could be two billiard balls. That the force between two billiard balls is conservative is not obvious, but it is a fact that billiard balls are manufactured so that they behave like almost perfect (that is, conservative) springs when they are forced together. It is certainly easy to think of other objects (such as lumps of putty), for which the interobject force is nonconservative, and the collisions of such objects are not elastic.

In a collision, the two particles start out far apart, approach one another, and then move apart again. Because the forces are conservative, the total energy is conserved; that is, $T + U = constant$ (where, of course, $T = T_{1} + T_{2}$ ). But when the particles are far apart, U is zero. Thus if we use the subscripts “in” and “fin” to label the situations well before and well after the particles come together, then conservation of energy implies that

$$
T _ {\mathrm{in}} = T _ {\mathrm{fin}}.\tag{4.88}
$$

In other words, an elastic collision can be characterized as a collision in which two particles come together and re-emerge with their total kinetic energy unchanged. However, it is important to remember that there is no principle of conservation of kinetic energy. On the contrary, while the particles are close together their PE is nonzero and their KE certainly is changing. It is only when they are well separated that the PE is negligible and conservation of energy leads to the result (4.88).

The foregoing discussion may suggest that elastic collisions should be a very common occurrence. All that is needed is two particles whose interaction is conservative. In practice, elastic collisions are not as widespread as this seems to imply. The trouble comes from the requirement that it be two particles that enter and leave the collision. For example, if we fire one billiard ball at a second with sufficient energy, the two balls may shatter. Similarly, if we fire an electron with sufficient energy at an atom, the atom may fall apart or, at least, change the internal motion of its constituents. Even in the collision of two genuine particles, such as an electron and a proton, relativity tells us that, with sufficient energy, new particles can be created. Clearly, at high enough energy, the assumption that the two objects entering a collision can be approximated as indivisible particles eventually breaks down, and we cannot assume that collisions will be elastic, even if all the underlying forces are conservative. Nevertheless, at reasonably low energies there are many situations where collisions are perfectly elastic:

At sufficiently low energy, collisions of an electron with an atom always are, and to a good approximation, the same is true of billiard balls.

Elastic collisions provide several simple illustrations of the uses of conservation of energy and momentum, of which the following is one.

## EXAMPLE 4.8 An Equal-Mass, Elastic Collision

Consider an elastic collision between two particles of equal mass, $m_{1}=m_{2}=m$ (for example, two electrons, or two billiard balls), as shown in Figure 4.21. Prove that if particle 2 is initially at rest then the angle between the two outgoing velocities is $\theta=90^{\circ}$ .

Conservation of momentum implies that $mV_{1}=mV_{1}^{\prime}+mV_{2}^{\prime}$ or

$$
\mathbf {v} _ {1} = \mathbf {v} _ {1} ^ {\prime} + \mathbf {v} _ {2} ^ {\prime}.\tag{4.89}
$$

That the collision is elastic implies that $\frac{1}{2} m\mathbf{v}_1^2 = \frac{1}{2} m\mathbf{v}_1'^2 +\frac{1}{2} m\mathbf{v}_2'^2$ or

$$
\mathbf {v} ^ {2} - \mathbf {v} ^ {\prime 2} + \mathbf {v} ^ {\prime 2}.
$$

Squaring (4.89), we find that

$$
\mathbf {v} _ {1} ^ {2} - \mathbf {v} _ {1} ^ {\prime 2} + 2 \mathbf {v} _ {1} ^ {\prime} \cdot \mathbf {v} _ {2} ^ {\prime} + \mathbf {v} _ {2} ^ {\prime 2}.
$$

and comparing the last two equations we see that

$$
\mathbf {v} _ {1} ^ {\prime} \cdot \mathbf {v} _ {2} ^ {\prime} = ()
$$

that is, $v_{1}^{\prime}$ and $v_{2}^{\prime}$ are perpendicular (unless one of them is zero, in which case the angle between them is undefined). This result was useful in atomic and nuclear physics; when an unknown projectile hit a stationary target particle, the fact that the two emerged traveling at $90^{\circ}$ was taken as evidence that the collision was elastic and the two particles had equal masses.

![](images/458821fed7381532211c29d972aee290927b2e7074a1c201c5edae424e8bfbdd.jpg)  
Figure 4.21 Elastic collision between two equal-mass particles. Particle 1 enters with velocity $v_{1}$ and collides with the stationary particle 2. The angle between the two final velocities $v_{1}^{\prime}$ and $v_{2}^{\prime}$ is $\theta$ .

## 4.10 The Energy of a Multiparticle System

We can extend our discussion of two particles to N particles fairly easily. The main complication is notational: The large number of $\sum$ signs can make it hard to see clearly what is going on. For this reason, I shall start by considering the case of four particles (N = 4) and write out all of the various sums explicitly.

## Four Particles

Let us consider, then, four particles, as shown in Figure 4.22. The particles can interact with each other (for example, they could be charged, so that each particle experiences the Coulomb force from the three others), and they may be subject to external forces, such as gravity or the Coulomb force of nearby charged bodies. In defining the energy of this system, the easy part is the kinetic energy T, which is, of course, the sum of four terms,

$$
T = T _ {1} + T _ {2} + T _ {3} + T _ {4},\tag{4.90}
$$

one term $T_{\alpha} = \frac{1}{2} m_{\alpha}v_{\alpha}^{2}$ for each particle.

To define the potential energy, we must examine the forces on the particles. First, there are the internal forces of the four particles interacting with each other. For each pair of particles there is an action–reaction pair of forces; for example, particles 3 and 4 produce the forces $F_{34}$ and $F_{43}$ shown in Figure 4.22. I shall take for granted that each of these interparticle forces $F_{\alpha\beta}$ is unaffected by the presence of the other particles and any external bodies. For example, $F_{34}$ is just the same as if particles 1 and 2 and all external bodies were removed. $^{14}$ Thus, we can treat the two forces $F_{34}$ and $F_{43}$ exactly as in Section 4.9. Provided the forces are conservative, we can define a potential energy

![](images/b2822077734469e54fa1ec894efef3886d37aec4741e81f5c17d0270827dd5cb.jpg)  
Figure 4.22 A system of four particles $\alpha = 1, 2, 3, 4$ . For each pair of particles, $\alpha\beta$ , there is an action–reaction pair of forces, $\mathbf{F}_{\alpha\beta}$ and $\mathbf{F}_{\beta\alpha}$ , such as the pair $\mathbf{F}_{34}$ and $\mathbf{F}_{43}$ shown. In addition, each particle $\alpha$ may be subject to an external net force $\mathbf{F}_{\alpha}^{\mathrm{ext}}$ . The four particles could be charged dust motes floating in the air, with the forces $\mathbf{F}_{\alpha\beta}$ being electrostatic and $\mathbf{F}_{\alpha}^{\mathrm{ext}}$ being gravity plus buoyancy of the air.

$$
U _ {3 4} = U _ {3 4} \left(\mathbf {r} _ {3} - \mathbf {r} _ {4}\right)\tag{4.91}
$$

and the corresponding forces are the appropriate gradients as in (4.83)

$$
\mathbf {F} _ {3 4} = - \nabla_ {3} U _ {3 4} \quad \text { and } \quad \mathbf {F} _ {4 3} = - \nabla_ {4} U _ {3 4}.\tag{4.92}
$$

There are in all six distinct pairs of particles, 12, 13, 14, 23, 24, 34, and for each pair we can define a corresponding potential energy $U_{12}, \cdots, U_{34}$ from which the corresponding forces are obtained in the same way.

Each of the external forces $F_{\alpha}^{ext}$ depends only on the corresponding position $r_{\alpha}$ . (The force $F_{1}^{ext}$ , for instance, depends on the position $r_{1}$ , but not on $r_{2}$ , $r_{3}$ , $r_{4}$ .) Therefore, we can handle $F_{\alpha}^{ext}$ exactly as we did the force on a single particle. In particular, if $F_{\alpha}^{ext}$ is conservative, we can introduce a potential energy $U_{\alpha}^{\mathrm{ext}}(\mathbf{r}_{\alpha})$ and the corresponding force is given by

$$
\mathbf {F} _ {\alpha} ^ {\mathrm{ext}} = - \nabla_ {\alpha} U _ {\alpha} ^ {\mathrm{ext}} (\mathbf {r} _ {\alpha})\tag{4.93}
$$

where, of course, $\nabla_{\alpha}$ denotes differentiation with respect to the coordinates of particle $\alpha$ .

We can now put all the potential energies together and define the total potential energy as the sum

$$
\begin{array}{c} U = U ^ {\text {int}} + U ^ {\text {ext}} = (U _ {1 2} + U _ {1 3} + U _ {1 4} + U _ {2 3} + U _ {2 4} + U _ {3 4}) \\ \qquad + (U _ {1} ^ {\text {ext}} + U _ {2} ^ {\text {ext}} + U _ {3} ^ {\text {ext}} + U _ {4} ^ {\text {ext}}). \end{array}\tag{4.94}
$$

In this definition, $U^{int}$ is the sum over all six pairs of particles of the pairwise potential energies, $U_{12}, \cdots, U_{34}$ , and $U^{ext}$ is the sum of the four potential energies, $U_{1}^{ext}, \cdots, U_{4}^{ext}$ arising from the external forces.

It is a fairly straightforward matter to show (see Problem 4.51 for more details) that the force on particle $\alpha$ is just (minus) the gradient of $U$ with respect to the coordinates $(x_{\alpha},y_{\alpha},z_{\alpha})$ . Consider, for instance, the gradient $-\nabla_1U$ . When $-\nabla_1$ acts on the first line of (4.94), its action on the first three terms, $U_{12} + U_{13} + U_{14}$ gives precisely the three internal forces, $\mathbf{F}_{12} + \mathbf{F}_{13} + \mathbf{F}_{14}$ . Acting on the last three terms, $U_{23} + U_{24} + U_{34}$ , it produces zero, since none of these depend on $\mathbf{r}_1$ . When $-\nabla_1$ acts on the second line of (4.94), its action on the first term, $U_1^{\mathrm{ext}}$ , produces the external force $F_{1}^{ext}$ . Acting on the last three terms it produces zero, since none of them depend on $r_{1}$ . Accordingly,

$$
\begin{array}{l} - \nabla_ {1} U = \mathbf {F} _ {1 2} + \mathbf {F} _ {1 3} + \mathbf {F} _ {1 4} + \mathbf {F} _ {1} ^ {\text {ext}} \\ = (\text {net force on particle 1}). \end{array}\tag{4.95}
$$

In exactly the same way, we can prove that in general

$$
- \nabla_ {\alpha} U = (\text { net   force   on   particle } \alpha)\tag{4.96}
$$

as expected.

The second crucial property of our definition of potential energy U is that (provided all the forces concerned are conservative, so we can define U), the total energy, defined as $E = T + U$ , is conserved. We prove this in the now familiar way (for more details, see Problem 4.52): Apply the work–KE theorem to each of the four particles and add the results to show that, in any short time interval, $dT = W_{tot}$ where $W_{tot}$ denotes the total work done by all forces on all particles. Next show that $W_{tot} = -dU$ , and conclude that $dT = -dU$ , and hence

$$
d E = d T + d U = 0.
$$

That is, energy is conserved.

## N Particles

The extension of these ideas to an arbitrary number of particles is now quite straightforward, and I shall just write down the principal formulas. For N particles, labeled $\alpha = 1, \cdots, N$ , the total kinetic energy is just the sum of the N separate kinetic energies

$$
T = \sum_ {\alpha} T _ {\alpha} = \sum_ {\alpha} \frac {1}{2} m _ {\alpha} v _ {\alpha} ^ {2}.
$$

Assuming that all forces are conservative, for each pair of particles, $\alpha\beta$ , we introduce the potential energy $U_{\alpha\beta}$ that describes their interaction, and for each particle $\alpha$ we introduce the potential energy $U_{\alpha}^{ext}$ that describes the net external force on that particle. The total potential energy is then

$$
U = U ^ {\text { int }} + U ^ {\text { ext }} = \sum_ {\alpha} \sum_ {\beta > \alpha} U _ {\alpha \beta} + \sum_ {\alpha} U _ {\alpha} ^ {\text { ext }}.\tag{4.97}
$$

(Here the condition $\beta > \alpha$ in the double sum makes sure we don't double count the internal interactions $U_{\alpha \beta}$ . For instance, we include $U_{12}$ but not $U_{21}$ .)

With the potential energy U defined in this way, the net force on any particle $\alpha$ is given by $-\nabla_{\alpha}U$ , as in Equation (4.96), and total energy $E = T + U$ is conserved. Finally, if any forces are nonconservative, we can define U as the potential energy pertaining to the conservative forces and then show that, in this case, $dE = W_{nc}$ where $W_{nc}$ is the work done by the nonconservative forces.

## Rigid Bodies

While the formalism of the last two sections is fairly general and complicated, you can perhaps take some comfort that most applications of the formalism are much simpler than the formalism itself. As one simple example, consider a rigid body, such as a golf ball or a meteorite, made up of $N$ atoms. The number $N$ is typically very large, but the energy formalism just developed usually turns out to be very simple. As you probably recall from elementary physics, the total kinetic energy of the $N$ particles rigidly bound together is just the kinetic energy of the center-of-mass motion plus the kinetic energy of rotation. (I'll be proving this in Chapter 10, but I hope you'll accept it for now.) The potential energy of the internal, interatomic forces as given by (4.97) is

$$
U ^ {\mathrm{int}} = \sum_ {\alpha} \sum_ {\beta > \alpha} U _ {\alpha \beta} (\mathbf {r} _ {\alpha} - \mathbf {r} _ {\beta}).\tag{4.98}
$$

If the interatomic forces are central (as is usually the case), then, as we saw in Section 4.8, the potential energy $U_{\alpha\beta}$ actually depends on just the magnitude of $r_{\alpha} - r_{\beta}$ (not its direction). Thus we can rewrite (4.98) as

$$
U ^ {\text { int }} = \sum_ {\alpha} \sum_ {\beta > \alpha} U _ {\alpha \beta} \left(\left| \mathbf {r} _ {\alpha} - \mathbf {r} _ {\beta} \right|\right).\tag{4.99}
$$

Now, as a rigid body moves, the positions $r_{\alpha}$ of its constituent atoms can, of course, move, but the distance $|r_{\alpha}-r_{\beta}|$ between any two atoms cannot change. (This is, in fact, the definition of a rigid body.) Therefore, if the body concerned is truly rigid, none of the terms in (4.99) can change. That is, the potential energy $U^{int}$ of the internal forces is a constant and can, therefore, be ignored. Thus, in applying energy considerations to a rigid body we can entirely ignore $U^{int}$ and have to worry only about the energy $U^{ext}$ corresponding to the external forces. Since this latter energy is often a very simple function (see the following example), energy considerations as applied to a rigid body are usually very straightforward.

## EXAMPLE 4.9 A Cylinder Rolling down an Incline

A uniform rigid cylinder of radius R rolls without slipping down a sloping track as shown in Figure 4.23. Use energy conservation to find its speed v when it reaches a vertical height h below its point of release.

In accordance with the preceding discussion we can ignore the internal forces that hold the cylinder together. The external forces on the cylinder are the normal and frictional forces of the track and gravity. The first two do no work, and gravity is conservative. As you certainly recall from introductory physics, the gravitational potential energy of an extended body is the same as if all the mass were concentrated at the center of mass. (See Problem 4.6.) Therefore,

$$
U ^ {\mathrm{ext}} = M g Y,
$$

where $Y$ is the height of the cylinder's CM measured up from any convenient reference level. The kinetic energy of the cylinder is $T = \frac{1}{2} M v^2 + \frac{1}{2} I \omega^2$ , where

![](images/927bb692f829c3d5910c28cf7def2243637c7334f31f7c9681f088e5ecf60187.jpg)  
Figure 4.23 A uniform cylinder starts from rest and rolls without slipping down a slope through a total vertical drop $h = Y_{in} - Y_{fin}$ (with the CM coordinate Y measured vertically up).

I is its moment of inertia, $I = \frac{1}{2} MR^{2}$ , and $\omega$ is its angular velocity of rolling, $\omega = v/R$ . Thus the final kinetic energy is

$$
T = \frac {3}{4} M v ^ {2}
$$

and the initial KE is zero. Therefore, conservation of energy in the form $\Delta T = -\Delta U^{ext}$ implies that

$$
\frac {3}{4} M v ^ {2} = - M g (Y _ {\mathrm{fin}} - Y _ {\mathrm{in}}) = M g h
$$

and hence that the final speed is

$$
v = \sqrt {\frac {4 g h}{3}}.
$$

## Principal Definitions and Equations of Chapter 4

## Work-KE Theorem

The change in KE of a particle as it moves from point 1 to point 2 is

$$
\Delta T \equiv T _ {2} - T _ {1} = \int_ {1} ^ {2} \mathbf {F} \cdot d \mathbf {r} \equiv W (1 \rightarrow 2)\tag{[Eq. (4.7)]}
$$

where $T = \frac{1}{2}mv^{2}$ and $W(1 \rightarrow 2)$ is the work which is done by the total force F on the particle and is defined by the preceding integral.

## Conservative Forces and Potential Energy

A force $\mathbf{F}$ on a particle is conservative if (i) it depends only on the particle's position, $\mathbf{F} = \mathbf{F}(\mathbf{r})$ , and (ii) for any two points 1 and 2, the work $W(1 \to 2)$ done by $\mathbf{F}$ is the same for all paths joining 1 and 2 (or equivalently, $\nabla \times \mathbf{F} = 0$ ). [Sections 4.2 & 4.4]

If F is conservative, we can define a corresponding potential energy so that

$$
U (\mathbf {r}) = - W \left(\mathbf {r} _ {0} \rightarrow \mathbf {r}\right) \equiv - \int_ {\mathbf {r} _ {0}} ^ {\mathbf {r}} \mathbf {F} \left(\mathbf {r} ^ {\prime}\right) \cdot d \mathbf {r} ^ {\prime}\tag{[Eq. (4.13)]}
$$

and

$$
\mathbf {F} = - \nabla U.\tag{[Eq. (4.33)]}
$$

If all the forces on a particle are conservative with corresponding potential energies $U_{1}, \cdots, U_{n}$ , then the total mechanical energy

$$
E = T + U _ {1} + \dots + U _ {n}\tag{[Eq. (4.22)]}
$$

is constant. More generally if there are also nonconservative forces, $\Delta E = W_{\mathrm{nc}}$ , the work done by the nonconservative forces.

## Central Forces

A force $\mathbf{F}(\mathbf{r})$ is central if it is everywhere directed toward or away from a “force center.” If we take the latter to be the origin,

$$
\mathbf {F} (\mathbf {r}) = f (\mathbf {r}) \hat {\mathbf {r}}.\tag{[Eq. (4.65)]}
$$

A central force is spherically symmetric $[f(\mathbf{r}) = f(r)]$ if and only if it is conservative.

[Sec. (4.8)]

## Energy of a Multiparticle System

If all forces (internal and external) on a multiparticle system are conservative, the total potential energy,

$$
U = U ^ {\text { int }} + U ^ {\text { ext }} = \sum_ {\alpha} \sum_ {\beta > \alpha} U _ {\alpha \beta} + \sum_ {\alpha} U _ {\alpha} ^ {\text { ext }}\tag{[Eq. (4.97)]}
$$

satisfies

$$
(\text { net   force   on   particle } \alpha) = - \nabla_ {\alpha} U\tag{[Eq. (4.96)]}
$$

and

$$
T + U = \text { constant }.\tag{[Problem 4.52]}
$$

Stars indicate the approximate level of difficulty, from easiest ( $\star$ ) to most difficult ( $\star\star\star$ ).

## SECTION 4.1 Kinetic Energy and Work

4.1 $\star$ By writing $\mathbf{a} \cdot \mathbf{b}$ in terms of components prove that the product rule for differentiation applies to the dot product of two vectors; that is,

$$
\frac {d}{d t} (\mathbf {a} \cdot \mathbf {b}) = \frac {d \mathbf {a}}{d t} \cdot \mathbf {b} + \mathbf {a} \cdot \frac {d \mathbf {b}}{d t}.
$$

4.2 ★★ Evaluate the work done

$$
W = \int_ {O} ^ {P} \mathbf {F} \cdot d \mathbf {r} = \int_ {O} ^ {P} (F _ {x} d x + F _ {y} d y)\tag{4.100}
$$

by the two-dimensional force $\mathbf{F} = (x^{2}, 2xy)$ along the three paths joining the origin to the point P = (1, 1) as shown in Figure 4.24(a) and defined as follows: (a) This path goes along the x axis to Q = (1, 0) and then straight up to P. (Divide the integral into two pieces, $\int_{O}^{P} = \int_{O}^{Q} + \int_{Q}^{P}$ .) (b) On this path $y = x^{2}$ , and you can replace the term dy in (4.100) by dy = 2xdx and convert the whole integral into an integral over x. (c) This path is given parametrically as $x = t^{3}$ , $y = t^{2}$ . In this case rewrite x, y, dx, and dy in (4.100) in terms of t and dt, and convert the integral into an integral over t.

4.3\*\* Do the same as in Problem 4.2, but for the force $\mathbf{F} = (-y, x)$ and for the three paths joining $P$ and $Q$ shown in Figure 4.24(b) and defined as follows: (a) This path goes straight from $P = (1, 0)$ to the origin and then straight to $Q = (0, 1)$ . (b) This is a straight line from $P$ to $Q$ . (Write $y$ as a function of $x$ and rewrite the integral as an integral over $x$ .) (c) This is a quarter-circle centered on the origin. (Write $x$ and $y$ in polar coordinates and rewrite the integral as an integral over $\phi$ .)

4.4\*\* A particle of mass $m$ is moving on a frictionless horizontal table and is attached to a massless string, whose other end passes through a hole in the table, where I am holding it. Initially the particle is moving in a circle of radius $r_0$ with angular velocity $\omega_0$ , but I now pull the string down through the hole until a length $r$ remains between the hole and the particle. (a) What is the particle's angular velocity now? (b) Assuming that I pull the string so slowly that we can approximate the particle's path by a circle of slowly shrinking radius, calculate the work I did pulling the string. (c) Compare your answer to part (b) with the particle's gain in kinetic energy.

![](images/116ac13a9eda856fc10050847dd3a8bb6eeeef9605e0aa69a2bd82dffc622b84.jpg)

![](images/ebc9ce77b16605a64b479fc6c9a0b2e634df422b831c3f80e8aa0411a53db9ab.jpg)  
Figure 4.24 (a) Problem 4.2. (b) Problem 4.3

## SECTION 4.2 Potential Energy and Conservative Forces

4.5★ (a) Consider a mass m in a uniform gravitational field g, so that the force on m is mg, where g is a constant vector pointing vertically down. If the mass moves by an arbitrary path from point 1 to point 2, show that the work done by gravity is $W_{\mathrm{grav}}(1 \rightarrow 2) = -mgh$ where h is the vertical height gained between points 1 and 2. Use this result to prove that the force of gravity is conservative (at least in a region small enough so that g can be considered constant). (b) Show that, if we choose axes with y measured vertically up, the gravitational potential energy is U = mgy (if we choose U = 0 at the origin).

4.6 $\star$ For a system of $N$ particles subject to a uniform gravitational field $\mathbf{g}$ acting vertically down, prove that the total gravitational potential energy is the same as if all the mass were concentrated at the center of mass of the system; that is,

$$
U = \sum_ {\alpha} U _ {\alpha} = M g Y
$$

where $M = \sum m_{\alpha}$ is the total mass and $\mathbf{R} = (X, Y, Z)$ is the position of the CM, with the y coordinate measured vertically up. [Hint: We know from Problem 4.5 that $U_{\alpha} = m_{\alpha}gy_{\alpha}$ .]

4.7★ Near to the point where I am standing on the surface of Planet X, the gravitational force on a mass m is vertically down but has magnitude $m\gamma y^{2}$ where $\gamma$ is a constant and y is the mass's height above the horizontal ground. (a) Find the work done by gravity on a mass m moving from $r_{1}$ to $r_{2}$ , and use your answer to show that gravity on Planet X, although most unusual, is still conservative. Find the corresponding potential energy. (b) Still on the same planet, I thread a bead on a curved, frictionless, rigid wire, which extends from ground level to a height h above the ground. Show clearly in a picture the forces on the bead when it is somewhere on the wire. (Just name the forces so it's clear what they are; don't worry about their magnitude.) Which of the forces are conservative and which are not? (c) If I release the bead from rest at a height h, how fast will it be going when it reaches the ground?

4.8 \*\* Consider a small frictionless puck perched at the top of a fixed sphere of radius $R$ . If the puck is given a tiny nudge so that it begins to slide down, through what vertical height will it descend before it leaves the surface of the sphere? [Hint: Use conservation of energy to find the puck's speed as a function of its height, then use Newton's second law to find the normal force of the sphere on the puck. At what value of this normal force does the puck leave the sphere?]

4.9 \*\* (a) The force exerted by a one-dimensional spring, fixed at one end, is $F = -kx$ , where $x$ is the displacement of the other end from its equilibrium position. Assuming that this force is conservative (which it is) show that the corresponding potential energy is $U = \frac{1}{2} kx^2$ , if we choose $U$ to be zero at the equilibrium position. (b) Suppose that this spring is hung vertically from the ceiling with a mass $m$ suspended from the other end and constrained to move in the vertical direction only. Find the extension $x_0$ of the new equilibrium position with the suspended mass. Show that the total potential energy (spring plus gravity) has the same form $\frac{1}{2} ky^2$ if we use the coordinate $y$ equal to the displacement measured from the new equilibrium position at $x = x_0$ (and redefine our reference point so that $U = 0$ at $y = 0$ ).

## SECTION 4.3 Force as the Gradient of Potential Energy

4.10 \* Find the partial derivatives with respect to $x, y$ , and $z$ of the following functions: (a) $f(x, y, z) = ax^2 + bxy + cy^2$ , (b) $g(x, y, z) = \sin(axyz^2)$ , (c) $h(x, y, z) = ae^{xy/z^2}$ , where $a, b$ , and $c$ are constants. Remember that to evaluate $\partial f_i \partial x$ you differentiate with respect to $x$ treating $y$ and $z$ as constants.

4.11 \* Find the partial derivatives with respect to $x, y$ , and $z$ of the following functions: (a) $f(x, y, z) = ay^2 + 2byz + cz^2$ , (b) $g(x, y, z) = \cos(axy^2z^3)$ , (c) $h(x, y, z) = ar$ , where $a, b$ , and $c$ are constants and $r = \sqrt{x^2 + y^2 + z^2}$ . Remember that to evaluate $\frac{\partial f}{\partial x}$ you differentiate with respect to $x$ treating $y$ and $z$ as constants.

4.12 \* Calculate the gradient $\nabla f$ of the following functions, $f(x, y, z)$ : (a) $f = x^{2} + z^{3}$ . (b) f = ky, where k is a constant. (c) $f = r \equiv \sqrt{x^{2} + y^{2} + z^{2}}$ . [Hint: Use the chain rule.] (d) f = 1/r.

4.13\* Calculate the gradient $\nabla f$ of the following functions, $f(x,y,z)$ : (a) $f = \ln (r)$ , (b) $f = r^n$ , (c) $f = g(r)$ , where $r = \sqrt{x^2 + y^2 + z^2}$ and $g(r)$ is some unspecified function of $r$ . [Hint: Use the chain rule.]

4.14 ★ Prove that if $f(\mathbf{r})$ and $g(\mathbf{r})$ are any two scalar functions of r, then

$$
\nabla (f g) = f \nabla g + g \nabla f
$$

4.15 \* For $f(\mathbf{r}) = x^2 + 2y^2 + 3z^2$ , use the approximation (4.35) to estimate the change in $f$ if we move from the point $\mathbf{r} = (1, 1, 1)$ to (1.01, 1.03, 1.05). Compare with the exact result.

4.16 $\star$ If a particle's potential energy is $U(\mathbf{r}) = k(x^{2} + y^{2} + z^{2})$ , where $k$ is a constant, what is the force on the particle?

4.17 $\star$ A charge $q$ in a uniform electric field $\mathbf{E}_0$ experiences a constant force $\mathbf{F} = q\mathbf{E}_0$ . (a) Show that this force is conservative and verify that the potential energy of the charge at position $\mathbf{r}$ is $U(\mathbf{r}) = -q\mathbf{E}_0 \cdot \mathbf{r}$ . (b) By doing the necessary derivatives, check that $\mathbf{F} = -\nabla U$ .

4.18 \*\* Use the property (4.35) of the gradient to prove the following important results: (a) The vector $\nabla f$ at any point $\mathbf{r}$ is perpendicular to the surface of constant $f$ through $\mathbf{r}$ . (Choose a small displacement $d\mathbf{r}$ that lies in a surface of constant $f$ . What is $df$ for such a displacement?) (b) The direction of $\nabla f$ at any point $\mathbf{r}$ is the direction in which $f$ increases fastest as we move away from $\mathbf{r}$ . (Choose a small displacement $d\mathbf{r} = \epsilon \mathbf{u}$ , where $\mathbf{u}$ is a unit vector and $\epsilon$ is fixed and small. Find the direction of $\mathbf{u}$ for which the corresponding $df$ is maximum, bearing in mind that $\mathbf{a} \cdot \mathbf{b} = ab \cos \theta$ .)

4.19 \*\* (a) Describe the surfaces defined by the equation $f = \text{const}$ , where $f = x^2 + 4y^2$ . (b) Using the results of Problem 4.18, find a unit normal to the surface $f = 5$ at the point (1, 1, 1). In what direction should one move from this point to maximize the rate of change of $f$ ?

## SECTION 4.4 The Second Condition that F be Conservative

4.20 ★ Find the curl. $\nabla \times F$ , for the following forces: (a) F = kr; (b) $\mathbf{F} = (Ax, By^{2}, Cz^{3})$ ; (c) $\mathbf{F} = (Ay^{2}, Bx, Cz)$ , where A, B, C and k are constants.

4.21 ★ Verify that the gravitational force $-GMm\hat{r}/r^{2}$ on a point mass m at r, due to a fixed point mass M at the origin, is conservative and calculate the corresponding potential energy.

4.22 \* The proof in Example 4.5 (page 119) that the Coulomb force is conservative is considerably simplified if we evaluate $\nabla \times \mathbf{F}$ using spherical polar coordinates. Unfortunately, the expression for $\nabla \times \mathbf{F}$ in spherical polar coordinates is quite messy and hard to derive. However, the answer is given inside the back cover, and the proof can be found in any book on vector calculus or mathematical methods. $^{15}$ Taking the expression inside the back cover on faith, prove that the Coulomb force $F = \gamma \hat{r}/r^{2}$ is conservative.

4.23 \*\* Which of the following forces is conservative? (a) $\mathbf{F} = k(x, 2y, 3z)$ where k is a constant. (b) $\mathbf{F} = k(y, x, 0)$ . (c) $\mathbf{F} = k(-y, x, 0)$ . For those which are conservative, find the corresponding potential energy U, and verify by direct differentiation that $F = -\nabla U$ .

4.24 \*\*\* An infinitely long, uniform rod of mass $\mu$ per unit length is situated on the z axis. (a) Calculate the gravitational force F on a point mass m at a distance $\rho$ from the z axis. (The gravitational force between two point masses is given in Problem 4.21.) (b) Rewrite F in terms of the rectangular coordinates $(x, y, z)$ of the point and verify that $\nabla \times F = 0$ . (c) Show that $\nabla \times F = 0$ using the expression for $\nabla \times F$ in cylindrical polar coordinates given inside the back cover. (d) Find the corresponding potential energy U.

4.25 \*\*\* The proof that the condition $\nabla \times \mathbf{F} = 0$ guarantees the path independence of the work $\int_{1}^{2}\mathbf{F} \cdot dr$ done by $\mathbf{F}$ is unfortunately too lengthy to be included here. However, the following three exercises capture the main points: $^{16}$ (a) Show that the path independence of $\int_{1}^{2}\mathbf{F} \cdot dr$ is equivalent to the statement that the integral $f_{\Gamma} \cdot F \cdot dr$ around any closed path $\Gamma$ is zero. (By tradition, the symbol $\oint$ is used for integrals around a closed path — a path that starts and stops at the same point.) [Hint: For any two points 1 and 2 and any two paths from 1 to 2, consider the work done by $\mathbf{F}$ going from 1 to 2 along the first path and then back to 1 along the second in the reverse direction.] (b) Stokes's theorem asserts that $f_{\Gamma} \cdot F \cdot dr = \int (\nabla \times \mathbf{F}) \cdot \hat{\mathbf{n}} dA$ , where the integral on the right is a surface integral over a surface for which the path $\Gamma$ is the boundary, and $\hat{\mathbf{n}}$ and $dA$ are a unit normal to the surface and an element of area. Show that Stokes's theorem implies that if $\nabla \times \mathbf{F} = 0$ everywhere, then $\oint_{\Gamma} \mathbf{F} \cdot dr = 0$ . (c) While the general proof of Stokes's theorem is beyond our scope here, the following special case is quite easy to prove (and is an important step toward the general proof): Let $\Gamma$ denote a rectangular closed path lying in a plane perpendicular to the $z$ direction and bounded by the lines $x = B$ , $x = B + b$ , $y = C$ and $y = C + c$ . For this simple path (traced counterclockwise as seen from above), prove Stokes's theorem that

$$
\oint_ {\Gamma} \mathbf {F} \cdot d \mathbf {r} = \int (\nabla \times \mathbf {F}) \cdot \hat {\mathbf {n}} d A
$$

where $\hat{n}=\hat{z}$ and the integral on the right runs over the flat, rectangular area inside $\Gamma$ . [Hint: The integral on the left contains four terms, two of which are integrals over x and two over y. If you pair them in this way, you can combine each pair into a single integral with an integrand of the form $F_{x}(x,C+c,z)-F_{x}(x,C,z)$ (or a similar term with the roles of x and y exchanged). You can rewrite this integrand as an integral over y of $\partial F_{x}(x,y,z)/\partial y$ (and similarly with the other term), and you're home.]

## SECTION 4.5 Time-Dependent Potential Energy

4.26 $\star$ A mass $m$ is in a uniform gravitational field, which exerts the usual force $F = mg$ vertically down, but with $g$ varying with time, $g = g(t)$ . Choosing axes with $y$ measured vertically up and defining $U = mgy$ as usual, show that $\mathbf{F} = -\nabla U$ as usual, but, by differentiating $E = \frac{1}{2} mv^2 + U$ with respect to $t$ , show that $E$ is not conserved.

![](images/507454b3a672c58438c10ac4728cee9894ffcfcfa7a8aa201c02511efb3eb41b.jpg)  
Figure 4.25 Problem 4.30

4.27\*\* Suppose that the force $\mathbf{F}(\mathbf{r},t)$ depends on the time $t$ but still satisfies $\nabla \times \mathbf{F} = 0$ . It is a mathematical fact (related to Stokes's theorem as discussed in Problem 4.25) that the work integral $\int_1^2\mathbf{F}(\mathbf{r},t)\cdot d\mathbf{r}$ (evaluated at any one time $t$ ) is independent of the path taken between the points 1 and 2. Use this to show that the time-dependent PE defined by (4.48), for any fixed time $t$ , has the claimed property that $\mathbf{F}(\mathbf{r},t) = -\nabla U'(\mathbf{r},t)$ . Can you see what goes wrong with the argument leading to Equation (4.19), that is, conservation of energy?

## SECTION 4.6 Energy for Linear One-Dimensional Systems

4.28 \*\* Consider a mass $m$ on the end of a spring of force constant $k$ and constrained to move along the horizontal $x$ axis. If we place the origin at the spring's equilibrium position, the potential energy is $\frac{1}{2} kx^2$ . At time $t = 0$ the mass is sitting at the origin and is given a sudden kick to the right so that it moves out to a maximum displacement at $x_{\max} = A$ and then continues to oscillate about the origin. (a) Write down the equation for conservation of energy and solve it to give the mass's velocity $\dot{x}$ in terms of the position $x$ and the total energy $E$ . (b) Show that $E = \frac{1}{2} kA^2$ , and use this to eliminate $E$ from your expression for $\dot{x}$ . Use the result (4.58), $t = \int dx' / \dot{x}(x')$ , to find the time for the mass to move from the origin out to a position $x$ . (c) Solve the result of part (b) to give $x$ as a function of $t$ and show that the mass executes simple harmonic motion with period $2\pi \sqrt{m / k}$ .

4.29 \*\* [Computer] A mass $m$ confined to the $x$ axis has potential energy $U = kx^4$ with $k > 0$ . (a) Sketch this potential energy and qualitatively describe the motion if the mass is initially stationary at $x = 0$ and is given a sharp kick to the right at $t = 0$ . (b) Use (4.58) to find the time for the mass to reach its maximum displacement $x_{\max} = A$ . Give your answer as an integral over $x$ in terms of $m, A$ , and $k$ . Hence find the period $\tau$ of oscillations of amplitude $A$ as an integral. (c) By making a suitable change of variables in the integral, show that the period $\tau$ is inversely proportional to the amplitude $A$ . (d) The integral of part (b) cannot be evaluated in terms of elementary functions, but it can be done numerically. Find the period for the case that $m = k = A = 1$ .

## SECTION 4.7 Curvilinear One-Dimensional Systems

4.30 $\star$ Figure 4.25 shows a child's toy, which has the shape of a cylinder mounted on top of a hemisphere. The radius of the hemisphere is $R$ and the CM of the whole toy is at a height $h$ above the floor. (a) Write down the gravitational potential energy when the toy is tipped to an angle $\theta$ from the vertical. [You need to find the height of the CM as a function of $\theta$ . It helps to think first about the height of the hemisphere's center $O$ as the toy tilts.] (b) For what values of $R$ and $h$ is the equilibrium at $\theta = 0$ stable?

![](images/94b9465acb401362f90481f649b774793a84ae846ea61f90928d749b7e9cd112.jpg)  
Figure 4.26 Problem 4.34

4.31★ (a) Write down the total energy E of the two masses in the Atwood machine of Figure 4.15 in terms of the coordinate x and $\dot{x}$ . (b) Show (what is true for any conservative one-dimensional system) that you can obtain the equation of motion for the coordinate x by differentiating the equation E = const. Check that the equation of motion is the same as you would obtain by applying Newton's second law to each mass and eliminating the unknown tension from the two resulting equations.

4.32 \*\* Consider the bead of Figure 4.13 threaded on a curved rigid wire. The bead's position is specified by its distance $s$ , measured along the wire from the origin. (a) Prove that the bead's speed $v$ is just $v = \dot{s}$ . (Write $\mathbf{v}$ in terms of its components, $dx / dt$ , etc., and find its magnitude using Pythagoras's theorem.) (b) Prove that $m\ddot{s} = F_{\mathrm{tang}}$ , the tangential component of the net force on the bead. (One way to do this is to take the time derivative of the equation $v^2 = \mathbf{v} \cdot \mathbf{v}$ . The left side should lead you to $\ddot{s}$ and the right to $F_{\mathrm{tang}}$ .) (c) One force on the bead is the normal force $\mathbf{N}$ of the wire (which constrains the bead to stay on the wire). If we assume that all other forces (gravity, etc.) are conservative, then their resultant can be derived from a potential energy $U$ . Prove that $F_{\mathrm{tang}} = -dU / ds$ . This shows that one-dimensional systems of this type can be treated just like linear systems, with $x$ replaced by $s$ and $F_x$ by $F_{\mathrm{tang}}$ .

4.33 \*\* [Computer] (a) Verify the expression (4.59) for the potential energy of the cube balanced on a cylinder in Example 4.7 (page 130). (b) Make plots of $U(\theta)$ for $b = 0.9r$ and $b = 1.1r$ . (You may as well choose units such that $r, m,$ and $g$ are all equal to 1.) (c) Use your plots to confirm the findings of Example 4.7 concerning the stability of the equilibrium at $\theta = 0$ . Are there any other equilibrium points and are they stable?

4.34 \*\* An interesting one-dimensional system is the simple pendulum, consisting of a point mass $m$ , fixed to the end of a massless rod (length $l$ ), whose other end is pivoted from the ceiling to let it swing freely in a vertical plane, as shown in Figure 4.26. The pendulum's position can be specified by its angle $\phi$ from the equilibrium position. (It could equally be specified by its distance $s$ from equilibrium — indeed $s = l\phi$ —but the angle is a little more convenient.) (a) Prove that the pendulum's potential energy (measured from the equilibrium level) is

$$
U (\phi) = m g l (1 - \cos \phi).\tag{4.101}
$$

Write down the total energy E as a function of $\phi$ and $\dot{\phi}$ . (b) Show that by differentiating your expression for E with respect to t you can get the equation of motion for $\phi$ and that the equation of motion is just the familiar $\Gamma = I\alpha$ (where $\Gamma$ is the torque, I is the moment of inertia, and $\alpha$ is the angular acceleration $\ddot{\phi}$ ). (c) Assuming that the angle $\phi$ remains small throughout the motion, solve for $\phi(t)$ and show that the motion is periodic with period

$$
\tau_ {0} = 2 \pi \sqrt {l / g}.\tag{4.102}
$$

![](images/39e5e6549531e98027768190b9e0743320abd23c331989e41062f2f7debc479e.jpg)  
Figure 4.27 Problem 4.36

(The subscript "o" is to emphasize that this is the period for small oscillations.)

4.35\*\* Consider the Atwood machine of Figure 4.15, but suppose that the pulley has radius $R$ and moment of inertia $I$ . (a) Write down the total energy of the two masses and the pulley in terms of the coordinate $x$ and $\dot{x}$ . (Remember that the kinetic energy of a spinning wheel is $\frac{1}{2} I\omega^2$ .) (b) Show (what is true for any conservative one-dimensional system) that you can obtain the equation of motion for the coordinate $x$ by differentiating the equation $E = \text{const}$ . Check that the equation of motion is the same as you would obtain by applying Newton's second law separately to the two masses and the pulley, and then eliminating the two unknown tensions from the three resulting equations.

4.36\*\* A metal ball (mass $m$ ) with a hole through it is threaded on a frictionless vertical rod. A massless string (length $l$ ) attached to the ball runs over a massless, frictionless pulley and supports a block of mass $M$ , as shown in Figure 4.27. The positions of the two masses can be specified by the one angle $\theta$ . (a) Write down the potential energy $U(\theta)$ . (The PE is given easily in terms of the heights shown as $h$ and $H$ . Eliminate these two variables in favor of $\theta$ and the constants $b$ and $l$ . Assume that the pulley and ball have negligible size.) (b) By differentiating $U(\theta)$ find whether the system has an equilibrium position, and for what values of $m$ and $M$ equilibrium can occur. Discuss the stability of any equilibrium positions.

4.37 \*\*\* [Computer] Figure 4.28 shows a massless wheel of radius R, mounted on a frictionless, horizontal axle. A point mass M is glued to the edge of the wheel, and a mass m hangs from a string wrapped around the perimeter of the wheel. (a) Write down the total PE of the two masses as a function of the angle $\phi$ . (b) Use this to find the values of m and M for which there are any positions of equilibrium. Describe the equilibrium positions, discuss their stability, and explain your answers in terms of torques. (c) Plot $U(\phi)$ for the cases that m = 0.7M and m = 0.8M, and use your graphs to describe the behavior of the system if I release it from rest at $\phi = 0$ . (d) Find the critical value of m/M on one side of which the system oscillates and on the other side of which it does not (if released from rest at $\phi = 0$ ).

4.38 \*\*\* [Computer] Consider the simple pendulum of Problem 4.34. You can get an expression for the pendulum's period (good for large oscillations as well as small) using the method discussed in connection with (4.57), as follows: (a) Using (4.101) for the PE, find $\dot{\phi}$ as a function of $\phi$ . Next use (4.57), in the form $t = \int d\phi/\dot{\phi}$ , to write the time for the pendulum to travel from $\phi = 0$ to its maximum value (the amplitude) $\Phi$ . Because this time is a quarter of the period $\tau$ , you can now write down the period. Show that

![](images/12255eb3b83714991cbae1ae9da256190deb1efe1840def9794c6588f55ff3dd.jpg)  
Figure 4.28 Problem 4.37

$$
\tau = \tau_ {\mathrm{o}} \frac {1}{\pi} \int_ {0} ^ {\Phi} \frac {d \phi}{\sqrt {\sin^ {2} (\Phi / 2) - \sin^ {2} (\phi / 2)}} = \tau_ {\mathrm{o}} \frac {2}{\pi} \int_ {0} ^ {1} \frac {d u}{\sqrt {1 - u ^ {2}} \sqrt {1 - A ^ {2} u ^ {2}}},\tag{4.103}
$$

where $\tau_{0}$ is the period (4.102) (Problem 4.34) for small oscillations and $A = \sin(\Phi/2)$ . [To get the first expression you will need to use the trig identity for $1 - \cos\phi$ in terms of $\sin^{2}(\phi/2)$ . To get the second you need to make the substitution $\sin(\phi/2) = Au.$ ] These integrals cannot be evaluated in terms of elementary functions. However, the second integral is a standard integral called the complete elliptic integral of the first kind, sometimes denoted $K(A^{2})$ , whose values are tabulated $^{17}$ and are known to computer software such as Mathematica [which calls it EllipticK( $A^{2}$ )]. (b) If you have access to computer software that knows this function, make a plot of $\tau/\tau_{0}$ for amplitudes $0 \leq \Phi \leq 3$ rad. Comment. What becomes of $\tau$ as the amplitude of oscillation approaches $\pi?$ Explain.

4.39 \*\*\* (a) If you have not already done so, do Problem 4.38(a). (b) If the amplitude $\Phi$ is small then so is $A = \sin (\Phi /2)$ . If the amplitude is very small, we can simply ignore the last square root in (4.103). Show that this gives the familiar result for the small-amplitude period, $\tau = \tau_{\mathrm{o}} = 2\pi \sqrt{l / g}$ . (c) If the amplitude is small but not very small, we can improve on the approximation of part (b). Use the binomial expansion to give the approximation $1 / \sqrt{1 - A^2u^2}\approx 1 + \frac{1}{2} A^2 u^2$ and show that, in this approximation, (4.103) gives

$$
\tau = \tau_ {0} [ 1 + \frac {1}{4} \sin^ {2} (\Phi / 2) ].
$$

What percentage correction does the second term represent for an amplitude of $45^{\circ}$ ? (The exact answer for $\Phi = 45^{\circ}$ is $1.040 \tau_{0}$ to four significant figures.)

## SECTION 4.8 Central Forces

4.40★ (a) Verify the three equations (4.68) that give x, y, z in terms of the spherical polar coordinates $r, \theta, \phi$ . (b) Find expressions for $r, \theta, \phi$ in terms of x, y, z.

![](images/6fbd5be3db385362ed04cd253f6f23b35e8af8553e943a0bfeeedf6e27747f3c.jpg)  
Figure 4.29 Problem 4.44

4.41 \* A mass $m$ moves in a circular orbit (centered on the origin) in the field of an attractive central force with potential energy $U = kr^n$ . Prove the virial theorem that $T = nU / 2$ .

4.42 \* In one dimension, it is obvious that a force obeying Hooke's law is conservative (since $F = -kx$ depends only on the position $x$ , and this is sufficient to guarantee that $F$ is conservative in one dimension). Consider instead a spring that obeys Hooke's law and has one end fixed at the origin, but whose other end is free to move in all three dimensions. (The spring could be fastened to a point in the ceiling and be supporting a bouncing mass $m$ at its other end, for instance.) Write down the force $\mathbf{F}(\mathbf{r})$ exerted by the spring in terms of its length $r$ and its equilibrium length $r_0$ . Prove that this force is conservative. [Hints: Is the force central? Assume that the spring does not bend.]

4.43 \*\* In Section 4.8, I claimed that a force $\mathbf{F}(\mathbf{r})$ that is central and spherically symmetric is automatically conservative. Here are two ways to prove it: (a) Since $\mathbf{F}(\mathbf{r})$ is central and spherically symmetric, it must have the form $\mathbf{F}(\mathbf{r}) = f(r)\hat{\mathbf{r}}$ . Using Cartesian coordinates, show that this implies that $\nabla \times \mathbf{F} = 0$ . (b) Even quicker, using the expression given inside the back cover for $\nabla \times \mathbf{F}$ in spherical polars, show that $\nabla \times \mathbf{F} = 0$ .

4.44\*\* Problem 4.43 suggests two proofs that a central, spherically symmetric force is automatically conservative, but neither proof makes really clear why this is so. Here is a proof that is less complete but more insightful: Consider any two points $A$ and $B$ and two different paths $ACB$ and $ADB$ connecting them as shown in Figure 4.29. Path $ACB$ goes radially out from $A$ until it reaches the radius $r_B$ of $B$ , and then around a sphere (center $O$ ) to $B$ . Path $ADB$ goes around a sphere of radius $r_A$ until it reaches the line $OB$ , and then radially out to $B$ . Explain clearly why the work done by a central, spherically symmetric force $F$ is the same along both paths. (This doesn't prove that the work is the same along any two paths from $A$ to $B$ . If you want you can complete the proof by showing that any path can be approximated by a series of paths moving radially in or out and paths of constant $r$ .)

4.45 \*\* In Section 4.8, I proved that a force $\mathbf{F}(\mathbf{r}) = f(\mathbf{r})\hat{\mathbf{r}}$ that is central and conservative is automatically spherically symmetric. Here is an alternative proof: Consider the two paths $ACB$ and $ADB$ of Figure 4.29, but with $r_B = r_A + dr$ where $dr$ is infinitesimal. Write down the work done by $\mathbf{F}(\mathbf{r})$ going around both paths, and use the fact that they must be equal to prove that the magnitude function $f(\mathbf{r})$ must be the same at points $A$ and $D$ ; that is, $f(\mathbf{r}) = f(r)$ and the force is spherically symmetric.

## SECTION 4.9 Energy of Interaction of Two Particles

4.46 $\star$ Consider an elastic collision of two particles as in Example 4.8 (page 143), but with unequal masses, $m_{1} \neq m_{2}$ . Show that the angle $\theta$ between the two outgoing velocities satisfies $\theta < \pi/2$ if $m_{1} > m_{2}$ , but $\theta > \pi/2$ if $m_{1} < m_{2}$ .

4.47 $\star$ Consider a head-on elastic collision between two particles. (Since the collision is head-on, the motion is confined to a single straight line and is therefore one-dimensional.) Prove that the relative velocity after the collision is equal and opposite to that before. That is, $v_{1} - v_{2} = -(v_{1}' - v_{2}')$ , where $v_{1}$ and $v_{2}$ are the initial velocities and $v_{1}'$ and $v_{2}'$ the corresponding final velocities.

4.48 \* A particle of mass $m_1$ and speed $v_1$ collides with a second particle of mass $m_2$ at rest. If the collision is perfectly inelastic (the two particles lock together and move off as one) what fraction of the kinetic energy is lost in the collision? Comment on your answer for the cases that $m_1 \ll m_2$ and that $m_2 \ll m_1$ .

4.49 \*\* Both the Coulomb and gravitational forces lead to potential energies of the form $U = \gamma / |\mathbf{r}_1 - \mathbf{r}_2|$ , where $\gamma$ denotes $kq_1q_2$ in the case of the Coulomb force and $-Gm_1m_2$ for gravity, and $\mathbf{r}_1$ and $\mathbf{r}_2$ are the positions of the two particles. Show in detail that $-\nabla_1U$ is the force on particle 1 and $-\nabla_2U$ that on particle 2.

4.50 \*\* The formalism of the potential energy of two particles depends on the claim in (4.81) that

$$
\nabla_ {1} U (\mathbf {r} _ {1} - \mathbf {r} _ {2}) = - \nabla_ {2} U (\mathbf {r} _ {1} - \mathbf {r} _ {2}).
$$

Prove this. (Use the chain rule for differentiation. The proof in three dimensions is notationally awkward, so prove the one-dimensional result that

$$
\frac {\partial}{\partial x _ {1}} f \left(x _ {1} - x _ {2}\right) = - \frac {\partial}{\partial x _ {2}} f \left(x _ {1} - x _ {2}\right)
$$

and then convince yourself that it extends to three dimensions.)

## SECTION 4.10 The Energy of a Multiparticle System

4.51 \*\* Write out the arguments of all the potential energies of the four-particle system in (4.94). For instance $U = U(\mathbf{r}_{1}, \mathbf{r}_{2}, \cdots, \mathbf{r}_{4})$ , whereas $U_{34} = U_{34}(\mathbf{r}_{3} - \mathbf{r}_{4})$ . Show in detail that the net force on particle 3 (for instance) is given by $-\nabla_{3}U$ . [You know that the separate forces, internal and external, are given by (4.92) and (4.93).]

4.52 \*\* Consider the four-particle system of Section 4.10. (a) Write down the work–KE theorem for each of the four particles separately and, by adding these four equations, show that the change in the total KE in a short time interval $dt$ is $dT = W_{\text{tot}}$ where $W_{\text{tot}}$ is the total work done on all particles by all forces. [This shouldn't take more than two or three lines.] (b) Next show that $W_{\text{tot}} = -dU$ where $dU$ is the change in total PE during the same time interval. Deduce that the total mechanical energy $E = T + U$ is conserved.

4.53\*\* (a) Consider an electron (charge -e and mass m) in a circular orbit of radius r around a fixed proton (charge +e). Remembering that the inward Coulomb force $ke^{2}/r^{2}$ is what gives the electron its centripetal acceleration, prove that the electron's KE is equal to $-\frac{1}{2}$ times its PE; that is, $T = -\frac{1}{2}U$ and hence $E = \frac{1}{2}U$ . (This result is a consequence of the so-called virial theorem. See Problem 4.41.) Now consider the following inelastic collision of an electron with a hydrogen atom: Electron number 1 is in a circular orbit of radius r around a fixed proton. (This is the hydrogen atom.) Electron 2 approaches from afar with kinetic energy $T_{2}$ . When the second electron hits the atom, the first electron is knocked free, and the second is captured in a circular orbit of radius $r'$ . (b) Write down an expression for the total energy of the three-particle system in general. (Your answer should contain five terms, three PEs but only two KEs, since the proton is considered fixed.) (c) Identify the values of all five terms and the total energy E long before the collision occurs, and again long after it is all over. What is the KE of the outgoing electron 1 once it is far away? Give your answers in terms of the variables $T_{2}$ , r, and $r'$ .