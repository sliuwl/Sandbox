## The Lagrangian Formalism

In principle, Newton's laws of motion allow us to solve any problem in classical mechanics. We just need to figure out the forces at play, solve the famous $\mathbf{F} = m\mathbf{a}$ , and we're done. 

However, there are good reasons not to proceed in this manner. First, it would appear to doom us to a life of solving ever more difficult differential equations, and that doesn't sound like much fun. Second, when we look back over the past few chapters, the big successes tended not to come from blindly solving $\mathbf{F} = m\mathbf{a}$ . Instead, we found clever ways to simplify problems, most notably by employing conservation laws. This suggests that it may be fruitful to focus our attention on these conservation laws, not necessarily to find new ones (they are, after all, rather rare) but instead to understand where they come from in the first place. To do this, we will look at the whole structure of classical mechanics with a fresh pair of eyes. 

There are, it turns out, two different ways of reformulating classical mechanics. The first of these is due to Joseph-Louis Lagrange and dates to 1788, the second to William Hamilton from the 1830s. We describe the Lagrangian formulation in this chapter and the Hamiltonian formulation in Chapter 10. In each, the concept of force, which is so dominant in the Newtonian prescription, is largely absent, recognised for the archaic seventeenth-century concept that it truly is and rightly consigned to the waste bin. Instead, other ideas, such as energy and symmetry, play a more central role. 

There are some practical advantages to these new formulations of classical mechanics, in the sense that they allow us to solve certain complicated problems with relative ease. For example, the Lagrangian framework will serve us well in Chapter 9 where we discuss the spinning motion of extended objects. It’s not that we couldn’t do this in the older Newtonian language if we wished, but there’s certainly some advantage to working with the Lagrangian picture. 

However, these practical advantages are not the real reason why we embrace the Lagrangian and Hamiltonian frameworks. More important is the light that they shed on classical mechanics. They allow us to prise open $F = ma$ , revealing the basic principles and structures that lie beneath. 

Moreover, these new formulations are an investment in the future. Every theory of nature, from electromagnetism and general relativity to the standard model of particle physics and more speculative pursuits such as string theory, is best formulated using Lagrangian and Hamiltonian ideals. In large part, this is because these new formulations provide a bridge between the classical and quantum worlds. Many of the equations of quantum mechanics that appear so strange and daunting when you first meet them have a classical counterpart where we can build intuition for what they're telling us. 

While these new formulations of classical mechanics work wonderfully for the fundamental laws of physics, they are not so well suited to systems that exhibit friction and dissipation. That means that Lagrangian and Hamiltonian techniques will play a starring role in all the books that follow this one, with just a single exception. If you want to study Fluid Mechanics, then you can get by without learning these new methods. Otherwise, strap in. 

## 7.1 Calculus of Variations

We start in this chapter by setting down the mathematical framework that we will need to describe the Lagrangian approach to classical mechanics. This framework goes by the name of the “calculus of variations”. 

The main character in our story is a mathematical object known as a functional. This is a generalisation of the idea of a function. If we have a function of a single variable $f(y)$ , that means that you feed it a number $y \in R$ and it spits back another number $f(y) \in \mathbb{R}$ . We could generalise this to think about a function of several variables, $f(y_{1}, \ldots, y_{n})$ . This means that you feed the function n different $y_{i} \in R$ and in return you get back just a single number. 

A functional is a function of a function. This means that you have to feed it an entire function $y(x)$ and, in return, you get back just a single number. We will denote the functional as $F[y(x)] \in \mathbb{R}$ , with the square brackets there as a subtle reminder that it eats more than a common-or-garden function. Comparing to a function of many variables, $f(y_{1}, \ldots, y_{n})$ , we see that the x in $y(x)$ is like the $i = 1, \ldots, n$ label on $y_{i}$ . 

How can we turn a function into a single number? The obvious way is to integrate. For example, the functional 

$$
F [ y (x) ] = \int_ {a} ^ {b} d x y (x)\tag{7.1}
$$

computes the area under the curve $y(x)$ between x = a and x = b. All the functionals that we discuss in this chapter will be integrals of this kind, but the integrand can be more interesting than just $y(x)$ . We might, for example, wish to integrate $y(x)$ against some other function of x. For example, if a rod has mass density $\rho(x)$ then the functional 

$$
F [ \rho (x) ] = \int_ {a} ^ {b} d x x \rho (x)\tag{7.2}
$$

computes the centre of mass of the rod. 

It's also useful to consider integrands that depend on the derivative $y'(x) = dy / dx$ . For example, suppose that we want to know the length of a curve $y(x)$ between two fixed points $(x, y) = (a, A)$ and $(x, y) = (b, B)$ . Then, summing up the hypotenuse of many small triangles, as shown in the figure, the length is given by the functional 

$$
F [ y (x) ] = \int_ {a} ^ {b} d x \sqrt {1 + y ^ {\prime} (x) ^ {2}}.\tag{7.3}
$$

In what follows, we will consider functionals that include all these ingredients, taking the form 

$$
F [ y (x) ] = \int_ {a} ^ {b} d x L (y (x), y ^ {\prime} (x), x).\tag{7.4}
$$

This means that the integrand is some function $L(y, y', x)$ of x, $y(x)$ and $y'(x)$ . Clearly this is not the most general form imaginable: we could also have the integrand depend on higher derivatives of y. But it turns out that functionals of the form (7.4) will serve our purpose. 

## 7.1.1 The Euler–Lagrange Equations

Given some functional $F[y(x)] \in \mathbb{R}$ , it's natural to ask: For which functions $y(x)$ does $F[y(x)]$ take its maximum value? And for which does it take its minimum value? 

The answer to these questions comes from taking some trial function $y(x)$ and then varying it to some nearby path $y(x) + \delta y(x)$ to see if the functional $F[y(x)]$ increases or decreases in value. This is where the name “calculus of variations” comes from. 

To see how this works in practice, let's first remind ourselves of the situation when we have a function $f(y_{1},\ldots ,y_{n})$ of several variables. We consider the value of the function at some point $\mathbf{y} = (y_{1},\dots ,y_{n})$ and then compare to a neighbouring point $\mathbf{y} + \delta \mathbf{y}$ . If we Taylor expand, we have 

$$
f (\mathbf {y} + \delta \mathbf {y}) = f (\mathbf {y}) + \frac {\partial f}{\partial y _ {i}} (\mathbf {y}) \delta y _ {i} + \frac {1}{2} \frac {\partial^ {2} f}{\partial y _ {i} \partial y _ {j}} (\mathbf {y}) \delta y _ {i} \delta y _ {j} + \dots .
$$

We say that the original point y is a stationary point if the function does not change to leading order in $\delta y$ , so that 

$$
\frac {\partial f}{y _ {i}} (\mathbf {y}) = 0 \text { for   all } i = 1, \dots , n.\tag{7.6}
$$

We've not yet determined whether this stationary point is a maximum or a minimum or something else. For that, we need to look at the second-order term in the expansion. We'll postpone this to Section 7.1.3. 

Now we repeat this story for functionals rather than functions. Consider a functional $F[y(x)]$ given by the general form 

$$
F [ y (x) ] = \int_ {a} ^ {b} d x L (y (x), y ^ {\prime} (x), x).\tag{7.7}
$$

We evaluate this on two nearby functions, $y(x)$ and $y(x) + \delta y(x)$ . We're interested in the difference between them 

$$
\delta F [ y ] = F [ y + \delta y ] - F [ y ].\tag{7.8}
$$

Working to leading order in $\delta y(x)$ , we have 

$$
\begin{array}{l} \delta F [ y ] = = \int_ {a} ^ {b} d x L (y + \delta y, y ^ {\prime} + \delta y ^ {\prime}, x) - \int_ {a} ^ {b} d x L (y, y ^ {\prime}, x) \\ \qquad = \int_ {a} ^ {b} d x \left[ \frac {\partial L}{\partial y} \delta y + \frac {\partial L}{\partial y ^ {\prime}} \delta y ^ {\prime} \right] + \ldots . \end{array}
$$

Here the $\cdots$ are terms that we've neglected of order $\delta y^2$ . We see that, to leading order, $\delta F[y]$ depends on two terms, one proportional to $\delta y$ and the other to $\delta y'$ . We can put these on the same footing by integrating the second term by parts 

$$
\delta F [ y ] = \int_ {a} ^ {b} d x \left[ \frac {\partial L}{\partial y} - \frac {d}{d x} \left(\frac {\partial L}{\partial y ^ {\prime}}\right) \right] \delta y (x) + \left[ \frac {\partial L}{\partial y ^ {\prime}} \delta y \right] _ {a} ^ {b}.
$$

We will ask that the boundary term vanishes. We can achieve this in one of two ways: 

- We could fix the value of $y(x)$ at $x = a$ and $x = b$ . This means that we only evaluate the functional $F[y(x)]$ on the curves with certain specified boundary conditions, $y(a)$ and $y(b)$ , which ensures that, when varying the curves, we must have $\delta y(a) = \delta y(b) = 0$ . 

- Alternatively, we could require that $\partial L / \partial y' = 0$ at $x = a$ and $x = b$ . For many purposes, $L(y, y', x)$ is quadratic or higher in $y'$ , in which case we can ensure this boundary condition by requiring $y'(a) = y'(b) = 0$ . These are usually referred to as free boundary conditions. 

- We could have a mixed boundary condition, fixed at one end and free at the other. 

If the boundary term vanishes, then the variation of the functional $F[y(x)]$ is given by the first integral term in (7.10). We will say that the initial function $y(x)$ is a stationary point or extremum of $F[y(x)]$ if $\delta F[y(x)] = 0$ for all variations $\delta y(x)$ that satisfy the required boundary condition. (The term “stationary point” is slightly misleading here because the “point” in question is now an entire function $y(x)$ .) 

The fact that $\delta F[y(x)]$ must vanish for all variations $\delta y(x)$ is important. The only way that this can happen is if the term in square brackets in the integrand of $(7.10)$ itself vanishes, meaning 

$$
\frac {\partial L}{\partial y} - \frac {d}{d x} \left(\frac {\partial L}{\partial y ^ {\prime}}\right) = 0.\tag{7.11}
$$

This is the Euler-Lagrange equation. Functions $y(x)$ that obey this equation are extrema of the functional $F[y(x)]$ . 

## An Example: Geodesics on a Plane

Here's a simple, and trivial, application of this result. We will determine the shortest path that connects two points on a plane, say $(x,y) = (a,A)$ and $(x,y) = (b,B)$ . The name given to a shortest path on some space is a geodesic. 

The length of a curve $y(x)$ in the plane is given by the functional (7.3) 

$$
F [ y (x) ] = \int_ {a} ^ {b} d x \sqrt {1 + y ^ {\prime} (x) ^ {2}}.\tag{7.12}
$$

In this case, we minimise over all curves with fixed end points, which means that we have the boundary conditions $\delta y(a) = \delta y(b) = 0$ . The integrand of the functional $L = \sqrt{1 + y'^{2}}$ depends only on $y'$ and so $\partial L / \partial y = 0$ and the Euler–Lagrange equation reads 

$$
{\frac {d}{d x}} \left({\frac {\partial L}{\partial y ^ {\prime}}}\right) = {\frac {d}{d x}} \left({\frac {y ^ {\prime}}{\sqrt {1 + {y ^ {\prime}} ^ {2}}}}\right) = 0 .\tag{7.13}
$$

This is solved by curves $y(x)$ such that $y'(x) = \text{constant}$ . Imposing the boundary conditions $y(a) = A$ and $y(b) = B$ , we have the unique solution 

$$
y = \alpha x + \beta \quad \mathrm{with} \quad \alpha = \frac {B - A}{b - a} \quad \mathrm{and} \quad \beta = \frac {b A - B a}{b - a}.
$$

We learn that the shortest path between two points on the plane is a straight line. That, of course, is deeply unsurprising. 

## Another Example: Geodesics on a Sphere

As another example, we can determine the shortest distance between two points on a sphere. This time the story is a little more intricate. The first thing that we need to do is to write down the functional that describes the length of a general curve on a sphere. 

We embed our sphere in $R^{3}$ with the usual spherical polar coordinates 

$$
x = R \sin \theta \cos \phi , y = R \sin \theta \sin \phi , z = R \cos \theta .
$$

Consider two nearby points on the sphere, $(\theta,\phi)$ and $(\theta+\delta\theta,\phi+\delta\phi)$ . What is the distance $\delta s$ between these two points? We can determine this by substituting the polar decomposition above into the usual Pythagorean distance $\delta s^{2}=\delta x^{2}+\delta y^{2}+\delta z^{2}$ , keeping the radius R fixed. We have 

$$
\delta s ^ {2} = \delta \theta^ {2} + \sin^ {2} \theta \delta \phi^ {2}.\tag{7.16}
$$

At this point, there are various ways to proceed. We could, for example, think of a path on the sphere as given by $\phi = \phi(\theta)$ . Then the analog of our flat-plane functional (7.12) for the length of the path is 

$$
F [ \phi (\theta) ] = \int_ {\theta_ {1}} ^ {\theta_ {2}} d \theta \sqrt {1 + \sin^ {2} \theta \phi^ {\prime} (\theta) ^ {2}}.\tag{7.17}
$$

We could then proceed to solve the corresponding Euler-Lagrange equation. However, it turns out to be a little cumbersome and there's a slicker way forward. To this end, instead of thinking of $\phi = \phi(\theta)$ , we will instead consider a path on the sphere to be given by $\theta(t)$ and $\phi(t)$ , where $t$ is some parameter along the path. The length of such a parameterised path is given by 

$$
F [ \theta (t), \phi (t) ] = \int_ {t _ {1}} ^ {t _ {2}} d t \sqrt {\dot {\theta} ^ {2} + \sin^ {2} \theta \dot {\phi} ^ {2}}\tag{7.18}
$$

with $\dot{\theta}=d\theta/dt$ and $\dot{\phi}=d\phi/dt$ . This is a generalisation of what we had previously: now it is a functional of two functions $\theta(t)$ and $\phi(t)$ , rather than just one. Correspondingly, there are two Euler–Lagrange equations, one for each function. However, there's a more direct way to minimise this functional that doesn't require us to derive the Euler–Lagrange equations. For this, we first use the rotational symmetry of the sphere to align our polar coordinates so that both the start and end points of the curve have the same $\phi$ value, as shown on the figure. This $\phi = constant$ curve is a great circle. We then note the following chain of inequalities 

$$
F [ \theta (t), \phi (t) ] \geq \int_ {t _ {1}} ^ {t _ {2}} d t | \dot {\theta} | \geq | \theta_ {2} - \theta_ {1} |\tag{7.19}
$$

The first inequality is saturated whenever $\dot{\phi} = 0$ , so that the path is along the great circle that joins the two points. The second inequality is saturated whenever $\theta(t)$ is monotonic, so that the path doesn't double back on itself. When both of these conditions are met, the inequalities are equalities and the distance along the path is $F = |\theta_2 - \theta_1|$ . We learn that the geodesics that minimise the functional $F[\theta(t), \phi(t)]$ are great circles between the two points. Note that this argument doesn't tell us which direction around the sphere we should go. In one direction, the geodesic is a global minimum of $F$ ; in the other direction, going the long way around the back of the sphere, the geodesic is a local minimum. 

## 7.1.2 Fermat's Principle

Ultimately, all fundamental laws of physics can be expressed using the calculus of variations. One of the first examples was a suggestion by 

Fermat, in 1662, that a light ray travels the path that takes the least time. This is known as Fermat's principle. 

For a light ray moving in a vacuum, Fermat's principle just reaffirms the obvious statement that light travels in a straight line between any two points. But things become more interesting when we consider light travelling in some material, where it no longer travels at speed $c$ , but instead at the lower speed $v = c / n$ where $n$ is called the refractive index. 

Suppose that a light ray moves between two different materials, the first with an index of refraction $n_{1}$ , the second with $n_{2}$ as shown in the figure. The light ray travels a total distance L in the horizontal direction, and a distance 2d in the vertical direction, but we suppose that it has a choice about the point x where it transitions from one material to the other. We can think of the total time taken T to be a function of x: it is 

$$
T (x) = \frac {\sqrt {d ^ {2} + x ^ {2}}}{v _ {1}} + \frac {\sqrt {d ^ {2} + (L - x) ^ {2}}}{v _ {2}}.
$$

To minimize this, we don't need any fancy calculus of variations. We just need to differentiate 

$$
{\frac {d T}{d x}} = {\frac {x}{v _ {1} \sqrt {d ^ {2} + x ^ {2}}}} - {\frac {L - x}{v _ {2} \sqrt {d ^ {2} + (L - x) ^ {2}}}} = 0 .\tag{7.20}
$$

This has a nice geometrical interpretation in terms of the angles shown in the figure: we have 

$$
\frac {\sin \theta_ {1}}{v _ {1}} = \frac {\sin \theta_ {2}}{v _ {2}} \quad \Longrightarrow \quad n _ {1} \sin \theta_ {1} = n _ {2} \sin \theta_ {2}.\tag{7.21}
$$

This is Snell's law for refraction. 

In more complicated situations, Fermat's principle gives a problem that falls very much in the camp of calculus of variations. Suppose that light moves in the $(x,y)$ -plane with the refractive index varying continuously as $n(y)$ . An example of this happens for the air above a hot, shimmering road, where refraction causes a mirage to appear as light from the sky bends. 

We consider light travelling from $(x,y)=(a,A)$ to $(x,y)=(b,B)$ . The time taken along a general path $y(x)$ is given by 

$$
T = \frac {1}{c} \int_ {a} ^ {b} d x n (y) \sqrt {1 + y ^ {\prime} (x) ^ {2}}.\tag{7.22}
$$

The Euler–Lagrange equation is 

$$
{\frac {\partial L}{\partial y}} - {\frac {d}{d x}} \left({\frac {\partial L}{\partial y ^ {\prime}}}\right) = {\sqrt {1 + y ^ {\prime} (x) ^ {2}}} {\frac {\partial n}{\partial y}} - {\frac {d}{d x}} \left({\frac {n (y) y ^ {\prime} (x)}{\sqrt {1 + y ^ {\prime} (x) ^ {2}}}}\right) = 0
$$

That's rather a mess. But there is, it turns out, a hidden simplification. You can show that the Euler–Lagrange equation (7.23) implies that 

$$
\frac {n (y)}{\sqrt {1 + y ^ {2}}} = \mathrm{constant}.\tag{7.24}
$$

Showing this directly is straightforward, but laborious: just use the chain rule to get an explicit expression for that $d / dx$ term in the Euler-Lagrange equation (7.23) and then show that the same Euler-Lagrange equation appears when you differentiate the combination $n(y) / \sqrt{1 + y'^2}$ . Later in this chapter, we'll give a more direct way to see why (7.24) is constant. (It is related to the conservation of energy in classical mechanics.) 

For a given profile $n(y)$ , we can go ahead and solve $(7.24)$ . For example, we take the refractive index to be 

$$
n (y) = \sqrt {a - b y}.\tag{7.25}
$$

Then (7.24) becomes 

$$
\frac {a - b y}{1 + y ^ {\prime 2}} = k ^ {2} \quad \Longrightarrow \quad y ^ {\prime} (x) ^ {2} = \frac {b}{k ^ {2}} (y _ {0} - y (x)).\tag{7.26}
$$

Here k is the constant on the right-hand side of $(7.24)$ and $y_{0} = (a - k^{2})/b$ . The solution to this equation is 

$$
y (x) = y _ {0} - \frac {b}{4 k ^ {2}} (x - x _ {0}) ^ {2}.\tag{7.27}
$$

We see that, with the refractive index (7.25), light doesn't travel in a straight line at all. Instead, it travels in a parabola! That's rather striking, not least because a ball thrown under the influence of gravity also travels in a parabola. It might make you wonder if perhaps we can phrase more general mechanics problems in a similar way. And, indeed, we can. Although, as we'll see shortly, it's typically not the time that we want to minimise. 

## 7.1.3 The Second Variation

Before we apply the calculus of variations to problems in classical mechanics, there is one thread that we left hanging. We know that the Euler–Lagrange equation is the requirement for a function to be an extremum. But how do we tell if it's a maximum or minimum or something else? It turns out that this information won't actually be needed for our applications to classical mechanics, but we include it here for completeness. 

To set the scene, we again return to a function of several variables $f(y_{1},\ldots,y_{n})$ . Taylor expanding about a given point y, we have 

$$
f (\mathbf {y} + \delta \mathbf {y}) - f (\mathbf {y}) = \frac {\partial f}{\partial y _ {i}} (\mathbf {y}) \delta y _ {i} + \frac {1}{2} \frac {\partial^ {2} f}{\partial y _ {i} \partial y _ {j}} (\mathbf {y}) \delta y _ {i} \delta y _ {j} + \dots .
$$

We assume that y is a stationary point, so $\partial f/\partial y_{i}(\mathbf{y})=0$ . That leaves us with the second order variation which is determined by the Hessian matrix 

$$
H _ {i j} (\mathbf {y}) = \frac {\partial^ {2} f}{\partial y _ {i} \partial y _ {j}} (\mathbf {y}).\tag{7.29}
$$

Because this matrix is symmetric, it can always be diagonalised. This means that there exists a rotation matrix $R \in O(n)$ such that $H' = R^{T} HR$ is diagonal, with the elements given by the eigenvalues $\lambda_{i}$ of H 

$$
H ^ {\prime} = \operatorname{diag} \left(\lambda_ {1}, \dots , \lambda_ {n}\right).\tag{7.30}
$$

The nature of the stationary point is determined by the signs of these eigenvalues: 

- If $\lambda_{i} > 0$ for all $i = 1, \ldots, n$ , then the stationary point is a minimum. 

- If $\lambda_{i} < 0$ for all $i = 1, \ldots, n$ , then the stationary point is a maximum. 

- If $\lambda_{i}$ are a collection of positive and negative numbers then the stationary point is a saddle point. 

- If some $\lambda_{i} = 0$ then we have to work harder and look to higher orders to understand what's going on in those directions. 

Now we extend this to functionals $F[y(x)]$ . We vary the path from $y(x)$ to $y(x) + \delta y(x)$ and write 

$$
\delta y (x) = \epsilon \eta (x)\tag{7.31}
$$

with $\epsilon\ll1$ . We then expand the functional (7.7) to second order 

$$
\begin{array}{l} \delta F [ y (x) ] = \epsilon \left\{\int_ {a} ^ {b} d x \left[ \frac {\partial L}{\partial y} - \frac {d}{d x} \left(\frac {\partial L}{\partial y ^ {\prime}}\right) \right] \eta (x) + \left[ \frac {\partial L}{\partial y ^ {\prime}} \eta \right] _ {a} ^ {b} \right\} \\ \qquad + \frac {1}{2} \epsilon^ {2} \int_ {a} ^ {b} d x \left\{\frac {\partial^ {2} L}{\partial y ^ {2}} \eta^ {2} + 2 \frac {\partial^ {2} L}{\partial y \partial y ^ {\prime}} \eta \eta^ {\prime} + \frac {\partial^ {2} L}{\partial y ^ {\prime 2}} \eta^ {\prime 2} \right. \end{array}
$$

The first line is what we had before in (7.10). The second line is new. We consider paths between $x = a$ and $x = b$ with fixed end points, so that $\eta(a) = \eta(b) = 0$ . Moreover, we'll take a path that solves the Euler-Lagrange equation. This means that the first line vanishes and we're left just with the second-order term. 

We have three terms, proportional to $\eta^2$ , $\eta \eta'$ , and $\eta'^2$ . Unfortunately, we don't get to integrate by parts to make all of these look the same. We can, however, use the fact that $2\eta \eta' = (\eta^2)'$ to integrate the second by parts. For an extremum of the action, the second variation is then 

$$
\delta^ {2} F [ y (x) ] = \frac {1}{2} \epsilon^ {2} \int_ {a} ^ {b} d x \left\{\left[ \frac {\partial^ {2} L}{\partial y ^ {2}} - \frac {d}{d x} \left(\frac {\partial^ {2} L}{\partial y \partial y ^ {\prime}}\right) \right] \eta^ {2} + \frac {\partial^ {2} L}{\partial y ^ {\prime 2}} \eta^ {\prime 2} \right\}
$$

Here we've thrown away the boundary term on the grounds that $\eta(a) = \eta(b) = 0$ . We've also renamed this term $\delta^2 F$ to emphasise that it is 

the second-order variation. 

The variation (7.33) depends both on the path $y(x)$ that solves the Euler-Lagrange equation, and also on the variation $\eta(x)$ . At this point, the story is a more complicated version of what we saw for a function of several variables. Suppose, for example, that, when evaluated on our extremum path $y(x)$ , the second-order variation (7.33) is strictly positive: 

$$
\delta^ {2} F [ y (x) ] > 0 \text { for   all } \eta (x).\tag{7.34}
$$

In this case, our extremum was a minimum of the functional. However, it may not be so easy to check that $(7.34)$ holds because we have to do it for all functions $\eta(x)$ . There is, however, a simple test that we can perform. If the path $y(x)$ is a local minimum, then it necessarily obeys 

$$
\frac {\partial^ {2} L}{\partial y ^ {2}} \geq 0 \text {   for   all   } x .\tag{7.35}
$$

This is known as the Legendre condition. We recognise $\partial^{2}L/\partial y'^{2}$ as the final term in (7.33). The idea behind the Legendre condition is that if (7.35) does not hold, so that $\partial^{2}L/\partial y'^{2}<0$ for some region, then we can always find a test function so that $\eta$ is small in that region while $\eta'$ is large and make the final term in (7.33) arbitrarily negative so that $\delta^{2}F<0$ . The Legendre condition is therefore necessary for the path to be a minimum. It is not, however, sufficient. 

## 7.2 The Principle of Least Action

When I was in high school, my physics teacher called me down one day after class and said, 'You look bored, I want to tell you something interesting.' Then he told me something I have always found fascinating. Every time the subject comes up I work on it. 

## Richard Feynman

Feynman's teacher told him about the principle of least action, one of the most profound and beautiful results in physics. 

We start by discussing just a single particle, with mass $m$ and position $\mathbf{x}(t)$ , moving in a potential $V(\mathbf{x})$ . Newton's law of motion is, of course 

$$
\dot {\mathbf {p}} = - \nabla V\tag{7.36}
$$

where $p = m \dot{x}$ is the momentum. We've already seen that the energy E is conserved for this system, with 

$$
E (\mathbf {x}, \dot {\mathbf {x}}) = T (\dot {\mathbf {x}}) + V (\mathbf {x}) \quad \mathrm{where} \quad T = \frac {1}{2} m \dot {\mathbf {x}} ^ {2}.\tag{7.37}
$$

Clearly the energy is the sum of the kinetic energy T and potential energy V. For this simple situation, we define the Lagrangian to be the difference between the two 

$$
L (\mathbf {x}, \dot {\mathbf {x}}) = T (\dot {\mathbf {x}}) - V (\mathbf {x}).\tag{7.38}
$$

The principle of least action then invites us to expand our horizons. Usually in classical mechanics, we solve Newton's equation to determine the path $\mathbf{x}(t)$ that the particle takes. Here, in contrast, we will consider all possible paths at once. We will not restrict to the one, true path that solves Newton's equations. We'll literally consider every possibility. Hopefully it's clear that this is a fairly radical step to take. 

We'll ask only that these paths are continuous and differentiable and that they have some fixed beginning point at time $t_i$ and some fixed end point at some later time $t_f$ , so that 

$$
\mathbf {x} (t _ {i}) = \mathbf {x} _ {\mathrm{initial}} \text { and } \mathbf {x} (t _ {f}) = \mathbf {x} _ {\mathrm{final}}.\tag{7.39}
$$

When I say that we consider all paths with these boundary conditions, I really mean all paths. We consider the path that heads in a straight line from $x_{initial}$ to $x_{final}$ and travels at a constant speed. We consider the path that flies off to the far flung reaches of the galaxy, does a few fly-bys of local exoplanets, and then heads back. We consider the path that lingers near $x_{initial}$ , procrastinating until the last second, before finally realising it's late and rushing towards $x_{final}$ , getting there just in time. We consider all paths. 

Of all these paths, the question is: which one is right? Which one actually obeys the equation of motion (7.36)? To answer this, we assign a number to each path. This number is called the action S, 

$$
S [ \mathbf {x} (t) ] = \int_ {t _ {i}} ^ {t _ {f}} d t L (\mathbf {x} (t), \dot {\mathbf {x}} (t)).\tag{7.40}
$$

This is the kind of functional that we considered in Section 7.1. We then have the following result: 

Principle of Least Action: The actual path taken by the particle is an extremum of the action S. 

Proof: The proof is essentially a rerun of the derivation of the Euler-Lagrange equation from Section 7.1. However, because this is an important result, it's worth redoing again. We start by considering some trajectory $\mathbf{x}(t)$ . To see if this is an extremum of the action, we compare its value to that of nearby trajectories. This means that we vary the path slightly, and look at a neighbouring path of the form 

$$
\mathbf {x} (t) \rightarrow \mathbf {x} (t) + \delta \mathbf {x} (t).\tag{7.41}
$$

We still want this neighbouring path to obey the same boundary conditions (7.39), so we insist that the variation satisfies 

$$
\delta \mathbf {x} (t _ {i}) = \delta \mathbf {x} (t _ {f}) = 0.\tag{7.42}
$$

We then ask how the action of this new trajectory compares to the original. The change in the action is 

$$
\begin{array}{l} \delta S = \delta \left[ \int_ {t _ {i}} ^ {t _ {f}} L d t \right] \\ = \int_ {t _ {i}} ^ {t _ {f}} \delta L d t \\ = \int_ {t _ {i}} ^ {t _ {f}} \left(\frac {\partial L}{\partial x ^ {i}} \delta x ^ {i} + \frac {\partial L}{\partial \dot {x} ^ {i}} \delta \dot {x} ^ {i}\right) d t \end{array}\tag{7.43}
$$

where, in the final line, we've reverted to index notation $x^{i}$ for the vector x and we're using the summation convention in which we sum over i = 1, 2, 3. At this point we integrate the second term by parts. In doing so, we pick up a boundary term, 

$$
\delta S = \int_ {t _ {i}} ^ {t _ {f}} \left(\frac {\partial L}{\partial x ^ {i}} - \frac {d}{d t} \left(\frac {\partial L}{\partial \dot {x} ^ {i}}\right)\right) \delta x ^ {i} d t + \left[ \frac {\partial L}{\partial \dot {x} ^ {i}} \delta x ^ {i} \right] _ {t _ {i}} ^ {t _ {f}}.
$$

But the final, boundary term vanishes because we have fixed the end points to obey $(7.42)$ . 

The requirement that our original path is an extremum means that $\delta S = 0$ for all changes in the path $\delta\mathbf{x}(t)$ . We see that this holds if and only if 

$$
\frac {\partial L}{\partial x ^ {i}} - \frac {d}{d t} \left(\frac {\partial L}{\partial \dot {x} ^ {i}}\right) = 0, i = 1, 2, 3.\tag{7.45}
$$

These are known as the Euler–Lagrange equations (or sometimes just as Lagrange's equations). To finish the proof, we need only show that the Euler–Lagrange equations are equivalent to Newton's. From the definition of the Lagrangian $L = \frac{1}{2} m \dot{\mathbf{x}}^{2} - V(\mathbf{x})$ , we have $\partial L / \partial x^{i} = -\partial V / \partial x^{i}$ , while $\partial L / \partial \dot{x}^{i} = p_{i}$ . It's then easy to see that the Euler–Lagrange equations are indeed equivalent to Newton's equation of motion (7.36). 

The principle of least action is a slight misnomer. The proof only requires that $\delta S = 0$ , and does not specify whether it is a maximum or minimum of S. Since L = T - V, we can always increase S by taking a very fast, wiggly path with $T \gg 0$ , so the true path is never a maximum. However, it may be either a minimum or a saddle point. So “principle of stationary action” would be a more accurate, but less catchy, name. It is sometimes called Hamilton’s principle. 

The principle of least action gives us a very different perspective on classical mechanics. In particular, it naively seems that we have done away with the whole idea of cause and effect, replacing our view of the dynamics with something more teleological. We're not setting things up by specifying the initial conditions of the particle, and then watching moment by moment as it's buffeted by a force which determines its subsequent acceleration. Instead, our two initial conditions on position and velocity are replaced by one initial condition and one final condition. It's a remarkable statement that the laws of physics can be reformulated in this way. 

To highlight this, it's worth stressing again that not all Newtonian forces admit a Lagrangian description. The most obvious counterexample is a friction force with, say, $\mathbf{F} = -\gamma \dot{\mathbf{x}}$ . There is no way to recast this force using Lagrangians. Moreover, these kind of friction forces are the ones that most clearly have an arrow of time built into them since they cause the particle to slow down, never to speed up. This is closely related to why they don't have a Lagrangian version. (A better way of making the distinction between things that can and can't have a Lagrangian formulation invokes Liouville's theorem that we will meet in Chapter 10.) 

However, friction is not a fundamental force. Instead it arises through the interaction of our particle with around $10^{23}$ atoms whose individual motions we choose to ignore. It is striking that, at the fundamental level, all laws of physics can be formulated using the principle of least action. The Lagrangian paradigm is telling us that, at a fundamental level, there's nothing that obliges you to think in terms of initial conditions and their subsequent evolution. You are quite at liberty to view the universe in a more global fashion, with the beginning and end set in place, and the only question being how you get from one to the other. 

## 7.2.1 Systems of Particles

The principle of least action that we derived above holds for a single particle. But the flexibility of this idea is a large part of its charm. Here we'll show that it's extremely simple to generalise to multiple particles. 

To do this, we simply need to adapt our notation. We consider N particles, each moving in $R^{3}$ . We write the positions of these particles as 

$$
x ^ {A} \quad \text { with } \quad A = 1, \ldots , 3 N  .\tag{7.46}
$$

So, in this notation $(x^{1}, x^{2}, x^{3})$ is the position of the first particle, and $(x^{4}, x^{5}, x^{6})$ is the position of the second and so on. In many other circumstances, you may think this is a bad idea: it mixes up the label that tells you what particle you're dealing with and the i = 1, 2, 3 label that tells you the coordinates of a given particle. Nonetheless, it will prove a useful device here. 

We introduce a potential energy $V(x^{A})$ that governs the motion of these particles through Newton's law 

$$
\dot {p} _ {A} = - \frac {\partial V}{\partial x ^ {A}}\tag{7.47}
$$

where $p_{A} = m_{A}\dot{x}^{A}$ . (Here there's no sum over A and $m_{A}$ is the mass of the appropriate particle.) We haven't put any constraint on the kind of potential $V(x^{A})$ that we write down. In particular, there's no restriction to the sort of pairwise potentials that we saw are most useful in Chapter 4, although there's certainly no reason that we can't consider them. 

Each coordinate that's needed to describe a given classical system is associated to a degree of freedom. Roughly speaking, the number of degrees of freedom is the number of different ways in which the system can move. Our $N$ particles, each roaming around in $\mathbb{R}^3$ , collectively have $3N$ degrees of freedom. As we proceed, we'll come across systems where the number of degrees of freedom differs because, for example, the motion of the particles is constrained in some way. In each case, the number of degrees of freedom provides the crudest characterisation of a system. 

We codify this by introducing the configuration space C. Each point in C specifies a possible configuration of the system which, for us, is the combined set of instantaneous positions of all N particles. This means that the dimension of C is equal to the number of degrees of freedom, which is 3N in the current example. Time evolution, governed by $(7.47)$ , then traces out a curve in C. 

This gives a novel way of viewing the dynamics of the system. Instead of thinking about N trajectories in $R^{3}$ , we instead think of just a single trajectory in configuration space $C = R^{3N}$ . This is shown in the figure where three particles, each moving in $R^{3}$ , are replaced by a single trajectory in $R^{9}$ . (Admittedly, not all these dimensions are shown.) 

The principle of least action for N particles now runs in parallel with the story for a single particle. We define the Lagrangian 

$$
L (x ^ {A}, \dot {x} ^ {A}) = T (\dot {x} ^ {A}) - V (x ^ {A}) \quad \mathrm{with} \quad T = \frac {1}{2} \sum_ {A} m _ {A} (\dot {x} ^ {A}) ^ {2}
$$

and the action 

$$
S [ x ^ {A} (t) ] = \int_ {t _ {i}} ^ {t _ {f}} d t L (x ^ {A} (t), \dot {x} ^ {A} (t)).\tag{7.49}
$$

We now consider all paths in configuration space with fixed end points, $x^{A}(t_{i}) = x_{\text{initial}}^{A}$ and $x^{A}(t_{f}) = x_{\text{final}}^{A}$ . The principle of least action states that the true path in configuration space, meaning the one that obeys (7.47), is an extremum of the action with $\delta S = 0$ . The proof is identical to that given above. Indeed, all you have to do is replace the $i = 1,2,3$ index in (7.43) and (7.44) with an $A = 1,\dots ,3N$ index to find the Euler-Lagrange equations, 

$$
\frac {\partial L}{\partial x ^ {A}} - \frac {d}{d t} \left(\frac {\partial L}{\partial \dot {x} ^ {A}}\right) = 0 A = 1, \ldots , 3 N.\tag{7.50}
$$

It's again straightforward to show that these coincide with Newton's equations (7.47). 

Above we employed the principle of least action for Lagrangians which split nicely into $L = T - V$ , with $T = T(\dot{\mathbf{x}})$ , and $V = V(\mathbf{x})$ . With such a split, we get the familiar Newtonian equation of motion for a particle moving in a potential. But there is nothing that stops us writing down a more general Lagrangian $L(\dot{\mathbf{x}},\mathbf{x})$ with terms that mix up $\dot{\mathbf{x}}$ and $\mathbf{x}$ . Later, as this chapter progresses, we'll see that there is much interesting physics to be found in such Lagrangians. We will also see many further generalisations of Lagrangians in subsequent books in this series. 

## The Lagrangian is Not Unique

The Lagrangian L is not unique. For example, if we rescale the Lagrangian by an overall constant, so that 

$$
L ^ {\prime} = \alpha L\tag{7.51}
$$

with $\alpha \in R$ , then the equations of motion remain unchanged. Moreover, the equations of motion also remain unchanged if we add a total derivative to the Lagrangian, so that 

$$
L ^ {\prime} = L + \frac {d f}{d t}\tag{7.52}
$$

for any function $f(\mathbf{x}, t)$ . (For multiple particles, this can be a function $f(x^A, t)$ .) There are two ways to see that the addition of a total derivative doesn't change the equations of motion. We could just plug $L'$ into the Euler-Lagrange equations and check. But a slicker proof is to note that the action changes only by a constant under the transformation (7.52) and so its stationary points remain the same. It's important that the function $f(\mathbf{x}, t)$ depends only on $\mathbf{x}$ and $t$ , and not on $\dot{\mathbf{x}}$ , because the former are held fixed at the end points while $\dot{\mathbf{x}}$ can vary and, hence, affect the value of the action. 

## 7.2.2 Galilean Relativity Revisited

As this chapter proceeds, we'll look more closely at the idea of symmetry in the Lagrangian framework. But we can make a quick and simple remark here. We consider a Lagrangian $L(\mathbf{x}, \dot{\mathbf{x}})$ for a single particle and ask: when is the resulting action invariant under the Galilean symmetries that we met in Chapter 1? 

Recall that the Galilean symmetries are translations, rotations, and boosts. Is it possible to write down an action that is invariant under such symmetries? 

First, translations. Can we write down a Lagrangian that doesn't change if we shift $\mathbf{x} \to \mathbf{x} + \mathbf{n}$ for any constant $\mathbf{n}$ ? That would ensure translational symmetry because the path $\mathbf{x}(t)$ and $\mathbf{x}(t) + \mathbf{n}$ would have the same action. It's not hard to convince yourself that the only way to do this is if the action doesn't depend on $\mathbf{x}$ . That's not too surprising. Any non-constant potential $V(\mathbf{x})$ clearly isn't invariant under translations. More interesting possibilities arise when we have two or more particles because then we can have potentials that depend on, e.g. $V(\mathbf{x}_1 - \mathbf{x}_2)$ , which is invariant under translational symmetry. It's just the one particle case that is more restrictive. We'll look at the consequences of this in Section 7.5. 

Next, boosts. Can we write down an action that doesn't change if we shift $\dot{\mathbf{x}} \rightarrow \dot{\mathbf{x}} + \mathbf{u}$ for some constant $\mathbf{u}$ ? This situation is more subtle than the case of translations because that extra time derivative makes all the difference. To see this, look at the action involving the usual kinetic energy 

$$
S = \int d t \frac {1}{2} m \dot {\mathbf {x}} ^ {2}.\tag{7.53}
$$

Under a boost, this changes to 

$$
S = \int d t \frac {1}{2} m (\dot {\mathbf {x}} + \mathbf {u}) ^ {2} = \int d t \frac {1}{2} m \left(\dot {\mathbf {x}} ^ {2} + 2 \dot {\mathbf {x}} \cdot \mathbf {u} + \mathbf {u} ^ {2}\right).
$$

Clearly the Lagrangian is not invariant under boosts. But the $\mathbf{u}^2$ term is just a constant so doesn't change the equation of motion. Moreover, the $\dot{\mathbf{x}} \cdot \mathbf{u}$ term is a total derivative of the form (7.52), so that too shifts the action by a constant and doesn't change the equations of motion. So while the action isn't invariant under boosts, it just picks up an additive constant, ensuring that the resulting equation of motion is invariant under boosts. 

Moreover, this property only holds for a Lagrangian of the form $L = \frac{1}{2} m \dot{x}^{2}$ . You could, for example, try replacing this kinetic term with something different, like $L \sim (\dot{\mathbf{x}} \cdot \dot{\mathbf{x}})^{2}$ . This is still rotationally invariant, but it is not invariant under boosts. 

So far in this book, we've thought of the kinetic energy $T = \frac{1}{2} m\dot{\mathbf{x}}^2$ as coming from Newton's equation of motion, which happens to be invariant under Galilean boosts. But the argument above suggests that we might want to turn this on its head. The requirement that the laws of physics are invariant under Galilean boosts restricts the form of the kinetic energy to be $T = \frac{1}{2} m\dot{\mathbf{x}}^2$ and this, in turn, leads to Newton's equation of motion. This, it turns out, is closer to the right way of looking at things, although there will be plenty more twists and turns before we are finally able to write down Lagrangians for the fundamental laws of physics and appreciate their symmetries. 

## 7.2.3 Looking Forwards: Quantum Mechanics and Beyond

The action has dimensions $[S] = ML^{2}T^{-1}$ . These are the same as the dimensions of angular momentum. More importantly, they are the same as the dimensions of Planck's constant $\hbar$ . This last statement underlies a beautiful generalisation of the action principle to quantum mechanics, due to Feynman, in which the particle takes all paths with the probability of each determined by $S/\hbar$ . We will describe this in Chapter 10. 

As an aside, neither of the transformations (7.51) and (7.52) leave the physics invariant in the quantum world. The first transformation (7.51) rescales Planck's constant, while the second transformation (7.52) is related to rather subtle and interesting topological effects. 

Finally, as we mentioned previously, it turns out that all the fundamental laws of physics can be written in terms of an action principle. As a shameless advertisement for what's to come, nearly everything we know about the universe is captured in the Lagrangian 

$$
L = \sqrt {g} \left[ R - \frac {1}{2} F _ {\mu \nu} F ^ {\mu \nu} + \bar {\psi}   \not D \psi + | \mathcal {D} h | ^ {2} + h \bar {\psi} \psi - V (h) \right]
$$

where the terms carry the names of Einstein, Maxwell (or Yang and Mills), Dirac, Higgs, and Yukawa respectively, and describe gravity, the forces of nature (electromagnetism and the nuclear forces), the dynamics of particles like electrons and quarks, and the dynamics of the Higgs boson. All of this will eventually be discussed in great detail in subsequent volumes in the series. 

Back to more down-to-earth pursuits, there are three very important reasons for working with the Euler–Lagrange equations rather than Newton's. The first is that the Euler–Lagrange equations hold in any coordinate system, while Newton's are restricted to an inertial frame. The second is the ease with which we can deal with constraints in the Lagrangian system. And the third is that the Lagrangian approach reveals a deep connection between symmetries and conservation laws. In the rest of this chapter, we look at each of these in turn, illustrated with plenty of examples. 

## 7.3 Generalised Coordinates

When we first met Newton's equations, back in Chapter 1, we made a big deal of the fact that they only hold in inertial frames. The principle of least action is more flexible. We can formulate it in any coordinate system that we like and it will give the right answer. 

This flexibility follows immediately from the action principle, which is a statement about paths and not about coordinates. But here we shall be a little more pedestrian in order to explain exactly what we mean by changing coordinates, and why it's useful. We start with our coordinates $x^{A}$ on a 3N-dimensional configuration space and define some new coordinate system 

$$
q ^ {i} = q ^ {i} (x ^ {1}, \dots , x ^ {3 N}, t) \text {with} i = 1, \dots , 3 N.\tag{7.56}
$$

Here we've allowed for the possibility that this new coordinate system changes with time $t$ . Then, by the chain rule, we can write 

$$
\dot {q} ^ {i} = \frac {d q ^ {i}}{d t} = \frac {\partial q ^ {i}}{\partial x ^ {A}} \dot {x} ^ {A} + \frac {\partial q ^ {i}}{\partial t}.\tag{7.57}
$$

To be a good coordinate system, we should be able to invert the relationship so that $x^{A} = x^{A}(q^{i}, t)$ , which we can do as long as we have $\det\left(\partial x^{A}/\partial q^{i}\right) \neq 0$ . Then we have 

$$
\dot {x} ^ {A} = \frac {\partial x ^ {A}}{\partial q ^ {i}} \dot {q} ^ {i} + \frac {\partial x ^ {A}}{\partial t}.\tag{7.58}
$$

Now we can look at what becomes of the Lagrangian $L(x^{A}, \dot{x}^{A})$ when we substitute in $x^{A} = x^{A}(q^{i}, t)$ . Using (7.58) we have 

$$
\frac {\partial L}{\partial q ^ {i}} = \frac {\partial L}{\partial x ^ {A}} \frac {\partial x ^ {A}}{\partial q ^ {i}} + \frac {\partial L}{\partial \dot {x} ^ {A}} \left(\frac {\partial^ {2} x ^ {A}}{\partial q ^ {i} \partial q ^ {j}} \dot {q} ^ {j} + \frac {\partial^ {2} x ^ {A}}{\partial q ^ {i} \partial t}\right)\tag{7.59}
$$

while 

$$
\frac {\partial L}{\partial \dot {q} ^ {i}} = \frac {\partial L}{\partial \dot {x} ^ {A}} \frac {\partial \dot {x} ^ {A}}{\partial \dot {q} ^ {i}} = \frac {\partial L}{\partial \dot {x} ^ {A}} \frac {\partial x ^ {A}}{\partial q ^ {i}}.\tag{7.60}
$$

In the second equality, we “cancelled the dots” to write 

$\partial\dot{x}^{A}/\partial\dot{q}^{i}=\partial x^{A}/\partial q^{i}$ which we can prove by differentiating the expression (7.58) with respect to $\dot{q}^{i}$ . Taking the time derivative of (7.60) gives us 

$$
\frac {d}{d t} \left(\frac {\partial L}{\partial \dot {q} ^ {i}}\right) = \frac {d}{d t} \left(\frac {\partial L}{\partial \dot {x} ^ {A}}\right) \frac {\partial x ^ {A}}{\partial q ^ {i}} + \frac {\partial L}{\partial \dot {x} ^ {A}} \left(\frac {\partial^ {2} x ^ {A}}{\partial q ^ {i} \partial q ^ {j}} \dot {q} ^ {j} + \frac {\partial^ {2} x ^ {A}}{\partial q ^ {i} \partial t}\right).
$$

So combining $(7.59)$ with $(7.61)$ we find 

$$
\frac {d}{d t} \left(\frac {\partial L}{\partial \dot {q} ^ {i}}\right) - \frac {\partial L}{\partial q ^ {i}} = \left[ \frac {d}{d t} \left(\frac {\partial L}{\partial \dot {x} ^ {A}}\right) - \frac {\partial L}{\partial x ^ {A}} \right] \frac {\partial x ^ {A}}{\partial q ^ {i}}.\tag{7.62}
$$

Equation (7.62) is our final result. We see that if the Euler–Lagrange equations (7.50) are solved in the $x^{A}$ coordinate system, so that $[\ldots]$ on the right-hand side vanishes, then they are also solved in the $q^{i}$ coordinate system, with 

$$
\frac {d}{d t} \left(\frac {\partial L}{\partial \dot {q} ^ {i}}\right) - \frac {\partial L}{\partial q ^ {i}} = 0\tag{7.63}
$$

Conversely, if (7.63) holds, then the Euler–Lagrange equations (7.50) are also satisfied in the $x^{A}$ coordinate system as long as our choice of coordinates is invertible, so that $\det\left(\partial x^{A}/\partial q^{i}\right) \neq 0$ . The upshot is that if the Euler–Lagrange equations hold in one coordinate system, then they hold in any coordinate system. 

In our original Cartesian coordinates, the momentum $p_{A} = m_{A} \dot{x}_{A}$ could be derived from the Lagrangian by differentiating the Lagrangian with respect to the velocity, 

$$
p _ {A} = \frac {\partial L}{\partial \dot {x} ^ {A}}.\tag{7.64}
$$

Now we have a more general set of coordinates at our disposal.
Nonetheless, the analogous quantity plays an important role. We define 

$$
p _ {i} = \frac {\partial L}{\partial \dot {q} ^ {i}}.\tag{7.65}
$$

This is known as the generalised momentum or canonical momentum conjugate to $q^i$ . Our notation has become a little subtle here: $p_A$ and $p_i$ can be very different objects, but are distinguished only by the letter we've chosen to label the index. In practice, this won't lead to much ambiguity when solving specific problems. In terms of the generalised momentum $p_i$ , the Euler-Lagrange equations become 

$$
\frac {\partial p _ {i}}{\partial t} - \frac {\partial L}{\partial q ^ {i}} = 0.\tag{7.66}
$$

We'll meet many examples of generalised coordinates in this book. But to get us going, here are two examples that we've seen before, but now phrased in the Lagrangian language. 

## An Example: Polar Coordinates

Consider a particle moving in $R^{3}$ with Cartesian coordinates $\mathbf{x} = (x, y, z)$ and a general potential $V(\mathbf{x})$ . The Lagrangian is 

$$
L = \frac {1}{2} m \dot {\mathbf {x}} ^ {2} - V (\mathbf {x}).\tag{7.67}
$$

We can work instead in spherical polar coordinates, defined by 

$$
x = r \sin \theta \cos \phi , y = r \sin \theta \sin \phi , z = r \cos \theta .\tag{7.}
$$

where $0 \leq \theta \leq \pi$ and $0 \leq \phi < 2\pi$ . We can substitute this change of variables directly into the Lagrangian to get 

$$
{\cal L} = \frac {1}{2} m (\dot {r} ^ {2} + r ^ {2} \dot {\theta} ^ {2} + r ^ {2} \sin^ {2} \theta \dot {\phi} ^ {2}) - V (r, \theta , \phi) .\tag{7.69}
$$

The generalised momenta (7.65) are 

$$
p _ {r} = m \dot {r}, p _ {\theta} = m r ^ {2} \dot {\theta}, p _ {\phi} = m r ^ {2} \sin^ {2} \theta \dot {\phi}.\tag{7.70}
$$

We can use this form of the Lagrangian to immediately derive the equations of motion in polar coordinates. We'll see a number of uses for this as we proceed. 

## 7.3.1 Rotating Coordinate Systems

We spent some time in Chapter 6 looking at how Newton's laws of motion appear in a rotating frame, complete with the fictitious centrifugal, Coriolis, and Euler forces. Here we can see the same calculation in the Lagrangian framework. 

We take a free particle moving in $R^{3}$ , with Lagrangian 

$$
L = \frac {1}{2} m \dot {\mathbf {x}} ^ {2}\tag{7.71}
$$

with $\mathbf{x} = (x, y, z)$ . Now measure the motion of the particle with respect to a coordinate system that is rotating with angular velocity $\omega = (0, 0, \omega)$ about the $z$ -axis. We'll take $\dot{\omega} = 0$ , which means that we won't recover the Euler force here. (It's not too difficult to include it if you wish.) 

If $\mathbf{x}^{\prime}=(x^{\prime},y^{\prime},z^{\prime})$ are the coordinates in the rotating system, we have the relationship 

$$
x ^ {\prime} = x \cos \omega t + y \sin \omega t, y ^ {\prime} = y \cos \omega t - x \sin \omega t, z ^ {\prime} = z
$$

We can substitute these expressions into the Lagrangian to find L in terms of the rotating coordinates, 

$$
L = \frac {m}{2} \left[ (\dot {x} ^ {\prime} - \omega y ^ {\prime}) ^ {2} + (\dot {y} ^ {\prime} + \omega x ^ {\prime}) ^ {2} + \dot {z} ^ {2} \right] = \frac {m}{2} (\dot {\mathbf {x}} ^ {\prime} + \pmb {\omega} \times \mathbf {x} ^ {\prime}) ^ {2}.
$$

In this rotating frame, we can use the Euler–Lagrange equations to derive the equations of motion. Taking derivatives, we have 

$$
\begin{array}{l l} & \frac {\partial L}{\partial \mathbf {x} ^ {\prime}} = m (\dot {\mathbf {x}} ^ {\prime} \times \boldsymbol {\omega} - \boldsymbol {\omega} \times (\boldsymbol {\omega} \times \mathbf {x} ^ {\prime})) \\ \text { and } & \frac {d}{d t} \left(\frac {\partial L}{\partial \dot {\mathbf {x}} ^ {\prime}}\right) = m (\ddot {\mathbf {x}} ^ {\prime} + \boldsymbol {\omega} \times \dot {\mathbf {x}} ^ {\prime}) . \end{array}\tag{7.74}
$$

The Euler–Lagrange equations then read 

$$
\frac {d}{d t} \left(\frac {\partial L}{\partial \dot {\mathbf {x}} ^ {\prime}}\right) - \frac {\partial L}{\partial \mathbf {x} ^ {\prime}} = 0 \quad \Longrightarrow \quad m \ddot {\mathbf {x}} ^ {\prime} = - m \boldsymbol {\omega} \times (\boldsymbol {\omega} \times \mathbf {x} ^ {\prime}) - 2 m \boldsymbol {\omega} \times
$$

This is the same as equation (6.15) that we derived previously, with the centrifugal force and Coriolis force appearing on the right-hand side. Note that the derivation using the Lagrangian is somewhat easier, largely because we have to think less. There's no worrying about which basis we're working in; we just plug in the coordinate substitution (7.72) and go, with all the subtleties automatically dealt with by the formalism. This is a recurring theme of the Lagrangian approach: you have to think less! It does a lot of the heavy lifting for you. 

## 7.3.2 Joseph-Louis Lagrange (1736–1813)

His voice is very feeble, at least in that he does not become heated; he has a very pronounced Italian accent and pronounces the s like z ... The students, of whom the majority are incapable of appreciating him, give him little welcome, but the professors make amends for it. 

## Fourier analysis of Lagrange

Lagrange started off life studying law but changed his mind and turned to mathematics after reading a book on optics by Halley (of comet fame). Despite being mostly self-taught, by the age of 19 he was a professor in his home town of Turin. 

He stayed in Italy, somewhat secluded, for the next 11 years, although he communicated often with Euler and, in 1766, moved to Berlin to take up Euler's recently vacated position. It was there he did his famous work on mechanics and the calculus of variations. In 1787 he moved once again, this time to Paris. He was just in time for the French revolution and only survived a law ordering the arrest of all foreigners after the intervention of the chemist Lavoisier who was a rather powerful political figure. (One year later, Lavoisier lost his power, followed quickly by his head.) 

Lagrange published his collected works on mechanics in 1788 in a book called Mechanique Analytique. He considered the work to be pure mathematics and boasts in the introduction that it contains no figures, thereby putting the anal in analytique. 

## 7.4 Constraints

In many of the more mechanical examples of Newtonian physics, we have to include various constraint forces. These are things like the tension of ropes, or normal forces applied by surfaces, all of which typically restrict the motion in some way. As we now explain, these things are particularly easy to incorporate in the Lagrangian setting, largely because we can just ignore them. 

## An Example: The Pendulum

We can illustrate the basics by looking at a pendulum of length l. This has a single dynamical degree of freedom $\theta$ , the angle the pendulum makes with the vertical. 

The position of the mass m in the plane is described by two cartesian coordinates x and y subject to a constraint $x^{2} + y^{2} = l^{2}$ . We can solve this constraint and parameterise the general configuration of the pendulum by an angle $\theta$ , 

$$
x = l \sin \theta \quad \text { and } \quad y = l \cos \theta .\tag{7.76}
$$

If we were to employ the Newtonian method to solve this system, we would first introduce the tension T, as shown in the figure, and resolve the force vectors to find 

$$
m \ddot {x} = - \frac {T x}{l} \quad \mathrm{and} \quad m \ddot {y} = m g - \frac {T y}{l}.\tag{7.77}
$$

To determine the motion of the system, we substitute in the constrained coordinates $(7.76)$ to get 

$$
\ddot {\theta} = - \frac {g}{l} \sin \theta \quad \mathrm{and} \quad T = m l \dot {\theta} ^ {2} + m g \cos \theta .\tag{7.78}
$$

While it's was pretty straightforward to derive the equation of motion using Newtonian methods for this example, things get rapidly harder when we consider more complicated constraints (and we'll see plenty presently). Moreover, you may have noticed that half of the work of the calculation went into computing the tension $T$ . On occasion we'll be interested in this. For example, we might want to know how fast we can spin the pendulum before it breaks. But often we won't care about these constraint forces, but will only want to know how they affect the equation of motion. In this case it seems like a waste of effort to go through the motions of computing $T$ . We'll now see how we can avoid this extra work in the Lagrangian formulation. First, we define what we mean by constraints more rigorously. 

## 7.4.1 Holonomic Constraints

We take as our starting point $N$ particles, each of which can move freely in $\mathbb{R}^3$ . This means that our configuration space is parameterised by Cartesian coordinates $x^A$ , with $A = 1, \ldots, 3N$ . This isn't the most general starting point, but it will serve our purposes. 

Holonomic constraints are relationships between the coordinates of the form 

$$
f _ {\alpha} (x ^ {A}, t) = 0 \qquad \alpha = 1, \ldots , 3 N - n.\tag{7.79}
$$

In general the constraints can be time dependent and our notation above allows for this. Holonomic constraints can be solved in terms of n generalised coordinates $q^{i}, i = 1, \ldots, n$ . So 

$$
x ^ {A} = x ^ {A} (q ^ {1}, \dots , q ^ {n}).\tag{7.80}
$$

The system is said to have n degrees of freedom. For the pendulum example above, the system has a single degree of freedom, $q = \theta$ . 

Now let's see how the Lagrangian formulation deals with constraints of this form. We introduce $3N - n$ new dynamical degrees of freedom, $\lambda^{\alpha}(t)$ . These are called Lagrange multipliers. Each of them sits on the same footing as the original $x^{A}(t)$ in the sense that the Lagrange multipliers are also dynamical functions of time. We now define a new Lagrangian 

$$
L ^ {\prime} = L (x ^ {A}, \dot {x} ^ {A}) + \lambda^ {\alpha} f _ {\alpha} (x ^ {A}, t)\tag{7.81}
$$

where, in the second term, the repeated index means that we're summing over all $\alpha = 3N - n$ . We now treat $\lambda^{\alpha}$ like new coordinates. Since $L'$ doesn't depend on $\dot{\lambda}^{\alpha}$ , the Euler-Lagrange equations for $\lambda^{\alpha}$ are 

$$
\frac {\partial L ^ {\prime}}{\partial \lambda^ {\alpha}} = f _ {\alpha} (x ^ {A}, t) = 0.\tag{7.82}
$$

But this is precisely the constraints that we want. We see that, by extremising $L'$ , we are indeed solving a problem with the constraints imposed. However, this comes with a price, because the Euler–Lagrange equation for $x^{A}$ is now 

$$
\frac {d}{d t} \left(\frac {\partial L}{\partial \dot {x} ^ {A}}\right) - \frac {\partial L}{\partial x ^ {A}} = \lambda^ {\alpha} \frac {\partial f _ {\alpha}}{\partial x ^ {A}}.\tag{7.83}
$$

The left-hand side is the equation of motion for the unconstrained system. The right-hand side is novel and captures the constraint forces in the system. We can now solve these equations as we did in the Newtonian formulation. 

## The Pendulum Example Again

The Lagrangian for the pendulum is that of a particle moving in the $(x, y)$ -plane under gravity, augmented by the Lagrange multiplier term for the constraint. It is 

$$
L ^ {\prime} = \frac {1}{2} m (\dot {x} ^ {2} + \dot {y} ^ {2}) + m g y + \frac {1}{2} \lambda (x ^ {2} + y ^ {2} - l ^ {2}).\tag{7.84}
$$

From this we can calculate the two equations of motion for x and y 

$$
m \ddot {x} = \lambda x \quad \text { and } \quad \ddot {y} = m g + \lambda y\tag{7.85}
$$

while the equation of motion for $\lambda$ reproduces the constraint $x^{2} + y^{2} - l^{2} = 0$ . Comparing with the Newtonian approach (7.77), we find that the Lagrange multiplier $\lambda$ is proportional to the tension: $\lambda = -T/l$ . 

## Generalised Coordinates for Constrained Systems

The discussion above tells us that we can easily incorporate constraint forces into the Lagrangian setup using Lagrange multipliers. But the big news is that we don't have to! Often we don't care about the tension $T$ or other constraint forces, but only want to know what the generalised coordinates $q^i$ are doing. In this case we have the following useful theorem. 

Theorem: For constrained systems, we may derive the equations of motion directly using generalised coordinates $q^{i}$ and the Lagrangian 

$$
L [ q ^ {i}, \dot {q} ^ {i}, t ] = L [ x ^ {A} (q ^ {i}, t), \dot {x} ^ {A} (q ^ {i}, \dot {q} ^ {i}, t) ].\tag{7.86}
$$

This just means that we substitute the expressions $x^{A}(q)$ into the original Lagrangian, and off we go, now treating $q^{i}$ as the only coordinates of interest. 

Proof: Let's work with $L' = L + \lambda^{\alpha} f_{\alpha}$ and change coordinates to 

$$
x _ {A} \to \left\{ \begin{array}{l l} q ^ {i} & i = 1, \ldots , n \\ f _ {\alpha} & \alpha = 1, \ldots 3 N - n \end{array} \right.\tag{7.87}
$$

Here, the novelty is that we're treating the constraints $f_{\alpha}(x^{A}, t)$ as coordinates of the original system. We know from our discussion in Section 7.3 that the Euler-Lagrange equations take the same form in these new coordinates. In particular, we may look at the equations for $q^{i}$ , 

$$
\frac {d}{d t} \left(\frac {\partial L}{\partial \dot {q} ^ {i}}\right) - \frac {\partial L}{\partial q ^ {i}} = \lambda_ {\alpha} \frac {\partial f _ {\alpha}}{\partial q ^ {i}}.\tag{7.88}
$$

But, by definition, $\partial f_{\alpha} / \partial q^i = 0$ because now we're viewing them as independent coordinates. So we are left with the Euler-Lagrange equations purely in terms of $q^i$ , with no sign of the constraint forces, 

$$
\frac {d}{d t} \left(\frac {\partial L}{\partial \dot {q} ^ {i}}\right) - \frac {\partial L}{\partial q ^ {i}} = 0 \quad i = 1, \ldots , n.\tag{7.89}
$$

This means that if we are only interested in the dynamics of the generalised coordinates $q^{i}$ , we may ignore the Lagrange multipliers and work entirely with the unconstrained Lagrangian $L(q^{i}, \dot{q}^{i}, t)$ defined in (7.86) where we just substitute in $x_{A} = x_{A}(q^{i}, t)$ . The resulting equations of motion are then given by (7.89). 

## The Pendulum Example for the Last Time

Let's see how this works in the simple example of the pendulum. We can parameterise the constraints in terms of the generalised coordinate $\theta$ so that $x = l\sin \theta$ and $y = l\cos \theta$ . We now substitute this directly into the Lagrangian for a particle moving in the plane under the effect of gravity, to get 

$$
L = \frac {1}{2} m (\dot {x} ^ {2} + \dot {y} ^ {2}) + m g y = \frac {1}{2} m l ^ {2} \dot {\theta} ^ {2} + m g l \cos \theta .\tag{7.90}
$$

From this we may derive the Euler–Lagrange equation using the coordinate $\theta$ directly 

$$
\frac {d}{d t} \left(\frac {\partial L}{\partial \dot {\theta}}\right) - \frac {\partial L}{\partial \theta} = m l ^ {2} \ddot {\theta} + m g l \sin \theta = 0\tag{7.91}
$$

which indeed reproduces the equation of motion for the pendulum (7.78). As promised, we haven't calculated the tension $T$ using this method. This has the advantage that we've needed to do less work. If we need to figure out the tension, we have to go back to the more laborious Lagrange multiplier method. 

## Non-Holonomic Constraints

Before we turn to various examples of holonomic constraints, it's worth flagging up that there are plenty of other kinds of constraints that can't be written in holonomic form $f_{\alpha}(x^{A}, t) = 0$ . Systems with non-holonomic constraints may be straightforward to solve, or they may be more complicated. But there's no general theory that covers them and you'll need to develop different methods for each problem. 

Here's a simple example of a non-holonomic constraint. Consider a particle moving under gravity, constrained to move on the outside of a sphere of radius $R$ . This means that the position of the particle is constrained by the inequality $x^{2} + y^{2} + z^{2} \geq R^{2}$ . Because this is an inequality, rather than an equality, it is a kind of non-holonomic constraint. We might, for example, start the particle perched on the top of the sphere, give it a slight nudge, and want to know when it falls off. It's straightforward to solve this: the particle falls off when the normal, contact force vanishes. But the theory of holonomic constraints won't help you. 

Here's a second example. A coin, of radius $R$ , is balanced on its edge and rolls along the ground. The position of the centre of the coin in the plane is described by Cartesian coordinates $x$ and $y$ . 

The coin has two, further degrees of freedom. This is the angle $\theta$ that it makes with the x-axis, and the angle $\phi$ that some chosen point on the rim makes with the ground. If the coin rolls without slipping, then the velocity of the rim is $v_{rim} = R\dot{\phi}$ . So, in terms of our four coordinates, we have the constraint 

$$
\dot {x} = R \dot {\phi} \sin \theta \quad \text { and } \quad \dot {y} = R \dot {\phi} \cos \theta .
$$

Now we have a velocity-dependent constraint. It is non-holonomic because it can't be integrated to give a constraint of the form $f(x, y, \theta, \phi) = 0$ . Again, this particular example isn't hard to solve and we'll look at something very similar in Chapter 9. 

## 7.4.2 A Bead on a Rotating Hoop

Take a hoop of radius a that rotates about the vertical axis with frequency $\omega$ . A bead of mass m is threaded on the hoop and moves without friction, as shown in the figure below. We want to determine the motion of this bead. 

This is an example of a system with a time-dependent holonomic constraint. There is a single degree of freedom $\psi(t)$ , the angle the bead makes with the vertical. In terms of Cartesian coordinates $(x, y, z)$ , the position of the bead is 

$$
\begin{array}{l} {x = a \sin \psi \cos \omega t,} \\ {y = a \sin \psi \sin \omega t ^ {\prime},} \\ {z = a - a \cos \psi .} \end{array}\tag{7.92}
$$

To determine the Lagrangian in terms of the generalised coordinate $\psi$ , we simply substitute these expressions into the Lagrangian for an unconstrained particle moving in a gravitational field. For the kinetic energy T we have 

$$
T = \frac {1}{2} m (\dot {x} ^ {2} + \dot {y} ^ {2} + \dot {z} ^ {2}) = \frac {1}{2} m a ^ {2} [ \dot {\psi} ^ {2} + \omega^ {2} \sin^ {2} \psi ].\tag{7.93}
$$

The potential energy V is given by (ignoring an overall constant) 

$$
V = m g z = - m g a \cos \psi .\tag{7.94}
$$

This means that our Lagrangian, as a function of $\psi$ and $\dot{\psi}$ , is given by 

$$
L = m a ^ {2} \left(\frac {1}{2} \dot {\psi} ^ {2} - V _ {\mathrm{eff}}\right)\tag{7.95}
$$

where the effective potential is 

$$
V _ {\mathrm{eff}} = \frac {1}{m a ^ {2}} \left(- m g a \cos \psi - \frac {1}{2} m a ^ {2} \omega^ {2} \sin^ {2} \psi\right).\tag{7.96}
$$

The additional term (that is independent of g) can be thought of as the angular momentum barrier that we met in Chapter 5. We can now derive the equation of motion for the bead from the Euler–Lagrange equation which reads 

$$
\ddot {\psi} = - \frac {\partial V _ {\mathrm{eff}}}{\partial \psi}.\tag{7.97}
$$

We can look for stationary solutions to this equation in which the bead doesn't move, i.e. solutions of the form $\ddot{\psi} = \dot{\psi} = 0$ . From the equation of motion, we must solve $\partial V_{eff} / \partial \psi = 0$ to find that the bead can remain stationary at points satisfying 

$$
g \sin \psi = a \omega^ {2} \sin \psi \cos \psi .\tag{7.98}
$$

The number of solutions depends on how fast the hoop is spinning. There are always two such solutions, given by $\psi = 0$ and $\psi = \pi$ , while, if the hoop is spinning fast enough, so that $\omega^{2} \geq g/a$ , then a third stationary point exists at $\cos \psi = g/a\omega^{2}$ . Which of these stationary points is stable depends on whether $V_{\mathrm{eff}}(\psi)$ has a local minimum (stable) or maximum (unstable). This in turn depends on the value of $\omega$ . 

The effective potential $V_{eff}$ is drawn in Figure 7.1 for two values of $\omega$ , the first below the critical value, the second above. For all values of $\omega$ , the bead perched at the top of the hoop at $\psi = \pi$ is unstable. For $\omega^{2} < g/a$ , the stable equilibrium point is at the bottom of the hoop at $\psi = 0$ . But, as the hoop spins faster, this position becomes unstable. For $\omega^{2} > g/a$ , the bead is still in equilibrium at $\psi = 0$ , but it's an unstable equilibrium. Instead, a new minimum of $V_{eff}$ appears at $\cos \psi = g/a\omega^{2}$ and this is the stable point. 

Fig. 7.1 The effective potential for the bead depends on how fast the hoop is rotating 

## 7.4.3 The Double Pendulum

A double pendulum is drawn in the figure to the right. It consists of two particles of mass $m_{1}$ and $m_{2}$ , connected by light rods of length $l_{1}$ and $l_{2}$ . For the first particle, the kinetic energy $T_{1}$ and the potential energy $V_{1}$ are the same as for a simple pendulum (7.90) 

$$
\begin{array}{r} T _ {1} = \frac {1}{2} m _ {1} l _ {1} ^ {2} \dot {\theta} _ {1} ^ {2} \\ \mathrm{and} V _ {1} = - m _ {1} g l _ {1} \cos \theta_ {1}. \end{array}\tag{7.99}
$$

For the second particle, things are a little more involved. Consider the position of the second particle in the plane of the pendulum swings. We use Cartesian coordinates $(x, y)$ , with y pointing downwards and take the origin to be the pivot of the first pendulum. We then have 

$$
x _ {2} = l _ {1} \sin \theta_ {1} + l _ {2} \sin \theta_ {2} \quad \text { and } \quad y _ {2} = l _ {1} \cos \theta_ {1} + l _ {2} \cos \theta_ {2}.
$$

We can substitute this into the kinetic energy for the second particle 

$$
\begin{array}{l} T _ {2} = \frac {1}{2} m _ {2} (\dot {x} ^ {2} + \dot {y} ^ {2}) \\ = \frac {1}{2} m _ {2} \left(l _ {1} ^ {2} \dot {\theta} _ {1} ^ {2} + l _ {2} ^ {2} \dot {\theta} _ {2} ^ {2} + 2 l _ {1} l _ {2} \cos (\theta_ {1} - \theta_ {2}) \dot {\theta} _ {1} \dot {\theta} _ {2}\right) \end{array}\tag{7.101]}
$$

while the potential energy is given by 

$$
V _ {2} = - m _ {2} g y _ {2} = - m _ {2} g \left(l _ {1} \cos \theta_ {1} + l _ {2} \cos \theta_ {2}\right).\tag{7.102}
$$

The Lagrangian is then the sum of the kinetic energies, minus the sum of the potential energies 

$$
\begin{array}{r} L = \frac {1}{2} (m _ {1} + m _ {2}) l _ {1} ^ {2} \dot {\theta} _ {1} ^ {2} + \frac {1}{2} m _ {2} l _ {2} ^ {2} \dot {\theta} _ {2} ^ {2} + m _ {2} l _ {1} l _ {2} \cos (\theta_ {1} - \theta_ {2}) \dot {\theta} _ {1} \dot {\theta} _ {2} \\ + (m _ {1} + m _ {2}) g l _ {1} \cos \theta_ {1} + m _ {2} g l _ {2} \cos \theta_ {2}. \end{array}
$$

The equations of motion now follow in the usual way by computing the two Euler–Lagrange equations, one for $\theta_{1}$ and one for $\theta_{2}$ . It turns out that the solutions to these equations are complicated and, above a certain energy, the motion is chaotic. In fact, for high energies the double pendulum goes completely nuts, swinging back and forth like a demented banshee. We’ll return briefly to the double pendulum in Chapter 8 where we look at the decidedly non-chaotic motion when the energy is very small. 

## 7.4.4 The Spherical Pendulum

A spherical pendulum consists of a heavy particle, attached to a light, rigid rod that is free to rotate in three dimensions, as shown in the figure. The system has two degrees of freedom which are the angles of spherical polar coordinates, living in the range $0 \leq \theta \leq \pi$ and $0 \leq \phi < 2\pi$ . In terms of cartesian coordinates, we have 

$$
\begin{array}{l} x = l \cos \phi \sin \theta \\ y = l \sin \phi \sin \theta \\ z = - l \cos \theta . \end{array}\tag{7.104}
$$

We substitute these constraints into the Lagrangian for a free particle to get 

$$
\begin{array}{r l} & L = \frac {1}{2} m (\dot {x} ^ {2} + \dot {y} ^ {2} + \dot {z} ^ {2}) - m g z \\ & \quad = \frac {1}{2} m l ^ {2} (\dot {\theta} ^ {2} + \dot {\phi} ^ {2} \sin^ {2} \theta) + m g l \cos \theta . \end{array}\tag{7.105}
$$

The first thing to note is that the coordinate $\phi$ appears in the Lagrangian only in the kinetic term with $\dot{\phi}$ . In Section 7.5, we will learn that any generalised coordinate with this property is special. Here we get a glimpse of why this is the case. The Euler–Lagrange equation for $\phi$ is 

$$
\frac {d}{d t} \left(\frac {\partial L}{\partial \dot {\phi}}\right) = m l ^ {2} \frac {d}{d t} \left(\dot {\phi} \sin^ {2} \theta\right) = 0.\tag{7.106}
$$

This is telling us that we've got a conserved quantity on our hands, given by 

$$
J = m l ^ {2} \dot {\phi} \sin^ {2} \theta .\tag{7.107}
$$

The Euler–Lagrange equation (7.106) tells us that J doesn't change with time. This is the component of angular momentum in the $\phi$ direction. Meanwhile, the equation of motion for $\theta$ follows from the Euler–Lagrange equation. It is 

$$
m l ^ {2} \ddot {\theta} = m l ^ {2} \dot {\phi} ^ {2} \sin \theta \cos \theta - m g l \sin \theta .\tag{7.108}
$$

We can substitute $\dot{\phi}$ for the constant J in this expression to get an equation entirely in terms of $\theta$ which we chose to write as 

$$
\ddot {\theta} = - \frac {\partial V _ {\mathrm{eff}}}{\partial \theta}\tag{7.109}
$$

where the effective potential is defined to be 

$$
V _ {\mathrm{eff}} (\theta) = - \frac {g}{l} \cos \theta + \frac {J ^ {2}}{2 m ^ {2} l ^ {4}} \frac {1}{\sin^ {2} \theta}.\tag{7.110}
$$

There is an important point here: we must substitute the conserved quantity $J$ into the equations of motion. If you substitute $J$ for $\dot{\phi}$ directly into the Lagrangian (7.105), you will derive an equation that looks like the one above, but you'll get a minus sign wrong! This is because the Euler-Lagrange equations are derived under the assumption that $\theta$ and $\phi$ are independent and this is no longer the case if you impose at the Lagrangian level that $\theta$ and $\phi$ are related by (7.107). 

The spherical pendulum also has a conserved energy, given by 

$$
E = \frac {1}{2} \dot {\theta} ^ {2} + V _ {\mathrm{eff}} (\theta) .\tag{7.111}
$$

Here E is a constant. (We will see in the next section how to deduce the conservation of energy directly from the Lagrangian.) We can invert this equation for E to solve for $\theta$ in terms of an integral 

$$
t - t _ {0} = \frac {1}{\sqrt {2}} \int \frac {d \theta}{\sqrt {E - V _ {\mathrm{eff}} (\theta)}}.\tag{7.112}
$$

Once we have an expression for $\theta(t)$ we can solve for $\phi(t)$ using the expression for J, 

$$
\phi = \int {\frac {J}{m l ^ {2}}} {\frac {1}{\sin^ {2} \theta}} d t = \frac {J}{\sqrt {2} m l ^ {2}} \int {\frac {1}{\sqrt {E - V _ {\mathrm{eff}} (\theta)}}} {\frac {1}{\sin^ {2} \theta}} d \theta
$$

which gives us $\phi (\theta)$ . 

To get more of a handle on what these solutions look like, we plot the function $V_{eff}$ in Figure 7.2. For a given energy E, the particle is restricted to the region $V_{eff} \leq E$ (a fact which follows from (7.111)). So from Figure 7.2, we see that the motion is pinned between two points $\theta_{1}$ and $\theta_{2}$ . If we draw the motion of the pendulum in real space, it must therefore look 

something like the figure to the right, in which the bob oscillates between the two extremes, $\theta_{1} \leq \theta \leq \theta_{2}$ . 

Fig. 7.2 The effective potential for the spherical pendulum. 

We could make more progress in understanding the motion of the spherical pendulum than for the double pendulum, where we essentially stopped after writing down the Lagrangian. Both of these systems have two degrees of freedom, but the spherical pendulum has two conserved quantities (angular momentum and energy), while the double pendulum has just one (energy). The reason that we can essentially solve the spherical pendulum is that we have one conserved quantity for each degree of freedom. 

There is a stable orbit which lies between the two extremal points at $\theta = \theta_{0}$ , corresponding to the minimum of $V_{eff}$ . This occurs if we balance the angular momentum J and the energy E just right. We can look at small oscillations around this point by expanding $\theta = \theta_{0} + \delta\theta$ . Substituting into the equation of motion (7.109), we have 

$$
\delta \ddot {\theta} = - \left(\frac {\partial^ {2} V _ {\mathrm{eff}}}{\partial \theta^ {2}} \Big | _ {\theta = \theta_ {0}}\right) \delta \theta + \mathcal {O} (\delta \theta^ {2})\tag{7.114}
$$

so small oscillations about $\theta = \theta_{0}$ have frequency $\omega^{2} = (\partial^{2} V_{\mathrm{eff}} / \partial \theta^{2})$ evaluated at $\theta = \theta_{0}$ . 

## 7.5 Symmetries and Conservation Laws

When approaching any problem in physics, the first thing that you should do is look for conserved quantities. One of the advantages of the Lagrangian approach is that conservation laws are intimately tied to symmetries. The link, as we now explain, is through an important and beautiful theorem due to Emmy Noether. 

We start with a definition. A function $F(q^{i}, \dot{q}^{i}, t)$ of the coordinates, their time derivatives, and (possibly) time t is called a conserved quantity if the total time derivative vanishes 

$$
\frac {d F}{d t} = \sum_ {j = 1} ^ {n} \left(\frac {\partial F}{\partial q ^ {j}} \dot {q} ^ {j} + \frac {\partial F}{\partial \dot {q} ^ {j}} \ddot {q} ^ {j}\right) + \frac {\partial F}{\partial t} = 0\tag{7.115}
$$

whenever $q^{i}(t)$ satisfy the Euler–Lagrange equations. Conserved quantities are also called constants of motion, because F remains constant as the system evolves. 

We've already met a number of conserved quantities in earlier chapters. Here we see how they arise in the Lagrangian formalism. 

## Conservation of (Generalised) Momentum

Suppose that the Lagrangian L depends only on the time derivative of some coordinate but not on the coordinate itself, meaning that $\partial L/\partial q^{j}=0$ for some $q^{j}$ . Then $q^{j}$ is said to be ignorable. (Sometimes $q^{j}$ is said to be cyclic.) Then the corresponding generalised momentum 

$$
p _ {j} = \frac {\partial L}{\partial \dot {q} ^ {j}}\tag{7.116}
$$

is conserved. 

The proof of this statement is straightforward. We have 

$$
\frac {d p _ {j}}{d t} = \frac {d}{d t} \left(\frac {\partial L}{\partial \dot {q} ^ {j}}\right) = \frac {\partial L}{\partial q ^ {j}} = 0\tag{7.117}
$$

where, in the second equality, we have used the Euler–Lagrange equation $(7.63)$ . 

If our coordinates $q^i$ coincide with our original Cartesian coordinates $x^A$ , then the conservation law described above is very intuitive. Suppose that a particle moves in $\mathbb{R}^2$ in a potential $V(\mathbf{x})$ , with $\mathbf{x} = (x, y)$ . Then, if $V(\mathbf{x})$ is independent of, say, the $y$ -coordinate, then the momentum in that direction $p_y$ will be conserved. This is simply because the force is $\mathbf{F} = -\nabla V$ and if $\partial V / \partial y = 0$ then there's no force in the $y$ -direction. 

However, the conservation law above is more general since it applies to generalised coordinates, not just Cartesian coordinates. Here is another simple example to illustrate the basic idea. We'll stick with a particle moving in $\mathbb{R}^2$ , but now we work in polar coordinates, defined by 

$$
x = r \cos \theta \quad \text { and } \quad y = r \sin \theta .\tag{7.118}
$$

Following our discussion of generalised coordinates in Section 7.3, we can simply substitute this into the Lagrangian to get 

$$
\begin{array}{r l} & L = \frac {1}{2} m (\dot {x} ^ {2} + \dot {y} ^ {2}) - V (\mathbf {x}) \\ & \quad = \frac {1}{2} m (\dot {r} ^ {2} + r ^ {2} \dot {\theta} ^ {2}) - V (r, \theta). \end{array}\tag{7.119}
$$

Suppose now that the potential is rotationally invariant, so $\partial V/\partial\theta = 0$ . Then the result above tells us that the generalised momentum $p_{\theta}$ is conserved, where 

$$
p _ {\theta} = \frac {\partial L}{\partial \dot {\theta}} = m r ^ {2} \dot {\theta}.\tag{7.120}
$$

But this is something very familiar: it is just the angular momentum about the origin, in a form that we previously met in $(5.22)$ . 

## Conservation of Energy

Another example arises when L does not depend explicitly on time t, so that $\partial L/\partial t = 0$ . In this case, we have the constant of motion 

$$
E = \dot {q} ^ {j} \frac {\partial L}{\partial \dot {q} ^ {j}} - L\tag{7.121}
$$

where, as always, we're employing the summation convention in the first term. This constant of motion is identified as the energy of the system. 

The proof that E is conserved is again of the plug-it-in-and-see variety. We have 

$$
\begin{array}{c} \frac {d E}{d t} = \ddot {q} ^ {j} \frac {\partial L}{\partial \dot {q} ^ {j}} + \dot {q} ^ {j} \frac {d}{d t} \left(\frac {\partial L}{\partial \dot {q} ^ {j}}\right) - \frac {\partial L}{\partial q ^ {j}} \dot {q} ^ {j} - \frac {\partial L}{\partial \dot {q} ^ {j}} \ddot {q} ^ {j} \\ = \left[ \frac {d}{d t} \left(\frac {\partial L}{\partial \dot {q} ^ {j}}\right) - \frac {\partial L}{\partial q ^ {j}} \right] \dot {q} ^ {j} \end{array}\tag{7.122}
$$

where, by assumption, a would-be $\partial L/\partial t$ term does not appear in the first line. We see that the final expression in square brackets vanishes whenever the Euler–Lagrange equations (7.63) hold. 

As we proceed, we'll get more intuition for why $E$ should be identified as energy. But, for now, we can just look at our simple example of a particle moving in the presence of a potential 

$$
L = \frac {1}{2} m \dot {\mathbf {x}} ^ {2} - V (\mathbf {x}) \quad \Longrightarrow \quad E = m \dot {\mathbf {x}} ^ {2} - L = \frac {1}{2} m \dot {\mathbf {x}} ^ {2} + V (\mathbf {x}).
$$

We see that we do indeed recover the familiar expression for energy. 

## 7.5.1 Noether's Theorem

Noether's theorem relates symmetries to conservation laws. To understand this, we first need to think more carefully about what we mean by a symmetry. 

Roughly speaking, a symmetry is a way to change the dynamical variables so that the value of the action remains unchanged. To make contact with examples that we've seen above, if the Lagrangian depends on $\dot{\mathbf{x}}$ but not $\mathbf{x}$ , then the Lagrangian will be invariant under the translational symmetry 

$$
\mathbf {x} \rightarrow \mathbf {x} + s \hat {\mathbf {n}}\tag{7.124}
$$

for any $s \in R$ and any constant unit vector $\hat{n}$ . 

Alternatively, if a single particle moves in a central potential, of the form $V(r)$ with $r^{2} = x \cdot x$ , then the Lagrangian will be invariant under rotational symmetry. This includes, for example, rotations about the z-axis 

$$
\left( \begin{array}{c} x \\ y \\ z \end{array} \right) \to \left( \begin{array}{c c c} \cos (s) & \sin (s) & 0 \\ - \sin (s) & \cos (s) & 0 \\ 0 & 0 & 1 \end{array} \right) \left( \begin{array}{c} x \\ y \\ z \end{array} \right)\tag{7.125}
$$

where, slightly unusually, we've written the angle as $s$ rather than a more traditional Greek letter. 

More generally, to describe a symmetry we introduce the idea of a one-parameter family of maps 

$$
q ^ {i} (t) \rightarrow q ^ {i} (s; t) \quad \text { with } \quad s \in \mathbb {R}\tag{7.126}
$$

such that $q^{i}(0;t)=q^{i}(t)$ . This transformation is said to be a continuous symmetry if the action is the same for all values of s. This happens if the Lagrangian $L(q^{i}(s;t),\dot{q}^{i}(s;t),t)$ is independent of s or, equivalently, 

$$
\frac {\partial}{\partial s} L (q ^ {i} (s; t), \dot {q} ^ {i} (s; t), t) = 0.\tag{7.127}
$$

The intuition behind this is that you can change a path in some way – maybe by translating the particle, maybe by rotating the particle, maybe by doing something else entirely – and the Lagrangian remains unaffected. For the transformation to be a symmetry, the Lagrangian should be independent of s when evaluated on any path $q^{i}(s;t)$ , not just those that obey the equations of motion. 

This brings us to Noether's theorem, which states that for each such continuous symmetry there exists a conserved quantity. Moreover, it tells you what this conserved quantity is... 

Noether's Theorem: For any continuous symmetry $q^i(s; t)$ , the quantity 

$$
Q = \frac {\partial L}{\partial \dot {q} ^ {i}} \left. \frac {\partial q ^ {i}}{\partial s} \right| _ {s = 0}\tag{7.128}
$$

is conserved. 

Proof: The proof is straightforward once you know what you're looking for. Differentiating the Lagrangian with respect to the 

parameter s, we have 

$$
\frac {\partial L}{\partial s} = \frac {\partial L}{\partial q ^ {i}} \frac {\partial q ^ {i}}{\partial s} + \frac {\partial L}{\partial \dot {q} ^ {i}} \frac {\partial \dot {q} ^ {i}}{\partial s}.\tag{7.129}
$$

Evaluating this at s = 0, and using the fact that the parameter s labels a symmetry, we have 

$$
\begin{array}{r l} & 0 = \left. \frac {\partial L}{\partial s} \right| _ {s = 0} = \frac {\partial L}{\partial q ^ {i}} \left. \frac {\partial q ^ {i}}{\partial s} \right| _ {s = 0} + \frac {\partial L}{\partial \dot {q} ^ {i}} \left. \frac {\partial \dot {q} ^ {i}}{\partial s} \right| _ {s = 0} \\ & \qquad = \frac {d}{d t} \left(\frac {\partial L}{\partial \dot {q} ^ {i}}\right) \left. \frac {\partial q ^ {i}}{\partial s} \right| _ {s = 0} + \frac {\partial L}{\partial \dot {q} ^ {i}} \left. \frac {\partial \dot {q} ^ {i}}{\partial s} \right| _ {s = 0} \\ & \qquad = \frac {d}{d t} \left(\frac {\partial L}{\partial \ddot {q} ^ {i}} \left. \frac {\partial q ^ {i}}{\partial s} \right| _ {s = 0}\right) \end{array}
$$

where, in the second line, we've used the Euler–Lagrange equation. This tells us that the quantity 

$$
Q = \left. \frac {\partial L}{\partial \dot {q} ^ {i}} \frac {\partial q ^ {i}}{\partial s} \right| _ {s = 0}\tag{7.131}
$$

is constant when evaluated on a solution to the equations of motion. This is what we want from a conserved quantity. $\square$ 

Noether's theorem links two rather different ideas: symmetry and conservation. Moreover, the theorem is constructive. It doesn't just tell us there there is some conserved quantity associated to a symmetry. It gives us an explicit expression for it, namely $(7.131)$ . Therein lies its power. 

The version of Noether's theorem described above is not quite the most general. In (7.127), we required that the Lagrangian is invariant under the symmetry. In fact, that's slightly too strong. It would suffice for the Lagrangian to change up to a time derivative, so that (7.127) is replaced by 

$$
\frac {\partial}{\partial s} L (q ^ {i} (s; t), \dot {q} ^ {i} (s; t), t) = \frac {d G}{d t}\tag{7.132}
$$

for some function $G(q^{i}(s;t), \dot{q}^{i}(s;t), t; s)$ . We then repeat all the steps of the proof, but note that the zero that kicks off the whole expression (7.130) is replaced by dG/dt. We then get the conserved quantity 

$$
Q = \left(\frac {\partial L}{\partial \dot {q} ^ {i}} \frac {\partial q ^ {i}}{\partial s} - G\right) \bigg | _ {s = 0}.\tag{7.133}
$$

Below, we will explain how Noether's theorem relates to the conservation of momentum, angular momentum, and energy. At heart, these results are only mildly different from the stories of conservation of (generalised) momentum and energy that we've already seen, albeit highlighting the symmetry aspect more. First, however, we make some comments: 

- As we proceed deeper into the laws of physics, we will see more intricate and subtle examples of Noether's theorem at play. In fact, it turns out that all conservation laws that we know of in the Standard 

Model are related to symmetries through Noether's theorem. This includes the conservation of electric charge and the conservation of particles such as protons and neutrons. 

- Noether's theorem holds for continuous symmetries, meaning those that are parameterised by a parameter $s \in \mathbb{R}$ . There are also discrete symmetries in nature which don't depend on a continuous parameter. For example, many theories are invariant under reflection, also known as parity, which acts as $\mathbf{x}(t) \to -\mathbf{x}(t)$ . These types of symmetries do not give rise to conservation laws in classical physics (although they do in quantum physics). 

With these comments in place, let's now turn to some simple applications of Noether's theorem. 