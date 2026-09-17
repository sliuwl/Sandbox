# CLASSICAL MECHANICS

VOLUME 1 

Any education in theoretical physics begins with the laws of classical mechanics. The basics of the subject were laid down long ago by Galileo and Newton and are enshrined in the famous equation $F = ma$ that we all learn in school. But there is much more to the subject and, in the intervening centuries, the laws of classical mechanics were reformulated to emphasise deeper concepts such as energy, symmetry, and action. This textbook describes these different approaches to classical mechanics, starting with Newton's laws before turning to subsequent developments such as the Lagrangian and Hamiltonian approaches. The book emphasises Noether's profound insights into symmetries and conservation laws, as well as Einstein's vision of spacetime, encapsulated in the theory of special relativity. Classical mechanics is not the last word on theoretical physics. But it is the foundation for all that follows. The purpose of this book is to provide this foundation. 

David Tong is a Professor of Theoretical Physics at the University of Cambridge and a Fellow of Trinity College. He is known for his contributions to quantum field theory and its application to diverse areas of physics, including particle physics, condensed matter, cosmology, and quantum gravity. His lecture notes on theoretical physics have gained a global following due to their clear explanations and easy-going, accessible style. 

## LECTURES ON THEORETICAL PHYSICS

Volume 1: Classical Mechanics 

Volume 2: Electromagnetism 

Volume 3: Quantum Mechanics 

Volume 4: Fluid Mechanics 

Volume 5: You may need to be patient 

# CLASSICAL MECHANICS

# Lectures on Theoretical Physics, Volume 1

David Tong
University of Cambridge 

![](images/3d8bd08d7c04dc32862b0f2e07409dcd8b77d2492bf41df153b2c7c44296fbcf.jpg)


CAMBRIDGE 

UNIVERSITY PRESS 

# CAMBRIDGE UNIVERSITY PRESS

Shaftesbury Road, Cambridge CB2 8EA, United Kingdom 

One Liberty Plaza, 20th Floor, New York, NY 10006, USA 

477 Williamstown Road, Port Melbourne, VIC 3207, Australia 

314–321, 3rd Floor, Plot 3, Splendor Forum, Jasola District Centre, New Delhi – 110025, India 

103 Penang Road, #05-06/07, Visioncrest Commercial, Singapore 238467 

Cambridge University Press is part of Cambridge University Press & Assessment, a department of the University of Cambridge. 

We share the University's mission to contribute to society through the pursuit of education, learning and research at the highest international levels of excellence. 

www.cambridge.org 

Information on this title: www.cambridge.org/highereducation/isbn/9781009594516 

DOI: 10.1017/9781009594530 

© David Tong 2025 

This publication is in copyright. Subject to statutory exception and to the provisions of relevant collective licensing agreements, no reproduction of any part may take place without the written permission of Cambridge University Press & Assessment. 

When citing this work, please include a reference to the DOI 10.1017/9781009594530 

First published 2025 

Printed in the United Kingdom by CPI Group Ltd, Croydon CR0 4YY 

A catalogue record for this publication is available from the British Library 

A Cataloging-in-Publication data record for this book is available from the Library of Congress 

ISBN 978-1-009-59451-6 Hardback 

ISBN 978-1-009-59454-7 Paperback 

Cambridge University Press & Assessment has no responsibility for the persistence or accuracy of URLs for external or third-party internet websites referred to in this publication and does not guarantee that any content on such websites is, or will remain, accurate or appropriate. 

For Mum 

## Contents

Preface
1 Newtonian Mechanics
1.1 Newton's Laws of Motion
1.1.1 Newton's First Law
1.1.2 Galilean Relativity
1.1.3 Newton's Second Law
1.1.4 Looking Forwards: The Validity of Newtonian Mechanics
2 Forces
2.1 Potentials in One Dimension
2.1.1 Moving in a Potential
2.1.2 Why (Almost) Everything is a Harmonic Oscillator
2.2 Potentials in Three Dimensions
2.2.1 Conservative Forces
2.2.2 Work Done
2.2.3 Central Forces and Angular Momentum Conservation
2.3 Gravity
2.3.1 The Gravitational Field
2.3.2 Escape Velocity
2.3.3 Inertial vs Gravitational Mass
2.4 Electromagnetism
2.4.1 Motion in a Constant Magnetic Field
2.4.2 The Electric Field of a Point Charge 

2.5 Friction
2.5.1 The Damped Harmonic Oscillator
2.5.2 The Damped, Driven Harmonic Oscillator
2.5.3 Terminal Velocity
2.5.4 Ohm's Law
2.5.5 Three-Dimensional Motion with Linear Drag
2.6 Appendix: Two Digressions
2.6.1 Line Integrals and Conservative Forces
2.6.2 The Poisson Equation
3 Interlude: Dimensional Analysis
4 Systems of Particles
4.1 Interactions Between Particles
4.1.1 Newton's Third Law
4.1.2 Centre of Mass Motion
4.1.3 Angular Momentum
4.1.4 Energy
4.2 Collisions
4.2.1 Bouncing Balls
4.2.2 More Bouncing Balls and the Digits of π
4.3 Variable Mass Problems
4.3.1 Rockets: Things Fall Apart
4.3.2 Avalanches: Stuff Gathering Other Stuff
5 The Two-Body Problem
5.1 Setting the Scene
5.1.1 The Two-Body Problem is Really a One-Body Problem
5.2 Conservation of Angular Momentum
5.2.1 Polar Coordinates in the Plane
5.3 The Effective Potential 

5.3.1 Getting a Feel for Orbits
5.3.2 The Stability of Circular Orbits
5.4 Orbits
5.4.1 The Kepler Problem
5.4.2 Kepler's Laws of Planetary Motion
5.4.3 The Runge–Lenz Vector
5.4.4 Perihelion Precession in General Relativity
5.5 A Brief History of Newton's Time
5.5.1 What Would Newton Do?
5.6 Scattering: Throwing Stuff at Other Stuff
5.6.1 The Impact Parameter
5.6.2 Rutherford Scattering
5.6.3 A First Look at the Cross-Section
5.6.4 A Bit More History: The Discovery of the Nucleus
6 Rotating Reference Frames
6.1 Rotating Frames
6.1.1 Velocity and Acceleration in a Rotating Frame
6.2 Newton's Equation of Motion in a Rotating Frame
6.3 The Centrifugal Force
6.3.1 An Example: Apparent Gravity.
6.3.2 The Roche Limit
6.4 The Coriolis Force
6.4.1 Particles, Baths, and Hurricanes
6.4.2 Balls and Towers
6.4.3 Foucault's Pendulum
6.4.4 Orbital Precession in a Magnetic Field
7 The Lagrangian Formalism
7.1 Calculus of Variations
7.1.1 The Euler–Lagrange Equations 

7.1.2 Fermat's Principle
7.1.3 The Second Variation
7.2 The Principle of Least Action
7.2.1 Systems of Particles
7.2.2 Galilean Relativity Revisited
7.2.3 Looking Forwards: Quantum Mechanics and Beyond
7.3 Generalised Coordinates
7.3.1 Rotating Coordinate Systems
7.3.2 Joseph-Louis Lagrange (1736–1813).
7.4 Constraints
7.4.1 Holonomic Constraints
7.4.2 A Bead on a Rotating Hoop
7.4.3 The Double Pendulum
7.4.4 The Spherical Pendulum
7.5 Symmetries and Conservation Laws
7.5.1 Noether's Theorem
7.5.2 Emmy Noether (1882–1935).
7.6 Lagrangians for Fundamental Forces
7.6.1 Gravity
7.6.2 Electromagnetism
7.6.3 A Brief Look at Curved Geometry.
8 Small Oscillations
8.1 Examples
8.1.1 The Double Pendulum Revisited
8.1.2 The Linear Triatomic Molecule
8.1.3 The Stability of Lagrange Points
8.1.4 A Lattice of Atoms
8.2 A Brief Look at Perturbation Theory.
8.2.1 The Anharmonic Oscillator 

9 Rigid Bodies
9.1 Kinematics
9.1.1 Angular Velocity
9.1.2 An Aside: Path-Ordered Exponentials
9.2 The Inertia Tensor
9.2.1 Angular Momentum
9.2.2 Computing the Inertia Tensor for Simple Examples
9.2.3 Parallel Axis Theorem
9.3 Motion of a Rigid Body: Preliminaries
9.3.1 Roll, Don't Slip
9.3.2 A Swinging Rod
9.3.3 A Rolling Disc
9.4 Euler's Equations
9.4.1 The Symmetric Top
9.4.2 The Asymmetric Top: Stability
9.4.3 The Poinsot Construction
9.5 Euler Angles
9.5.1 Angular Velocity
9.5.2 The Free Symmetric Top Revisited
9.6 The Heavy Symmetric Top
9.6.1 Uniform Precession
9.6.2 The Sleeping Top
9.6.3 The Precession of the Equinox
9.7 The Motion of Deformable Bodies
9.7.1 Kinematics
9.7.2 Dynamics
10 The Hamiltonian Formalism
10.1 Hamilton's Equations 

10.1.1 The Hamiltonian
10.1.2 The Principle of Least Action
10.1.3 A Particle in a Potential
10.1.4 A Particle in an Electromagnetic Field
10.1.5 William Rowan Hamilton (1805–1865).
10.2 Liouville's Theorem
10.2.1 Liouville's Equation
10.2.2 Poincar'e Recurrence Theorem
10.3 Poisson Brackets
10.3.1 Angular Momentum
10.3.2 A Particle in a Magnetic Field, Revisited
10.3.3 First-Order Vortex Dynamics in the Plane
10.3.4 Spin and a Compact Phase Space
10.4 Canonical Transformations
10.4.1 Infinitesimal Canonical Transformations
10.4.2 The Inverse Noether Theorem
10.4.3 Generating Functions
10.5 Action-Angle Variables
10.5.1 The Harmonic Oscillator
10.5.2 Briefly, Integrable Systems
10.5.3 Action-Angle Variables for One-Dimensional Systems
10.5.4 Action-Angle Variables for Higher-Dimensional Systems
10.6 Adiabatic Invariants
10.6.1 A Particle in a Magnetic Field
10.7 The Hamilton–Jacobi Equation
10.7.1 Action and Angles from Hamilton–Jacobi
10.8 Quantum Mechanics
10.8.1 Hamilton, Jacobi, Schrödinger, and Feynman
Special Relativity 

11.1 Lorentz Transformations
11.1.1 Lorentz Transformations in Three Spatial Dimensions
11.1.2 Spacetime Diagrams
11.1.3 A History of Light Speed
11.2 Relativistic Physics
11.2.1 Simultaneity
11.2.2 Causality
11.2.3 Time Dilation
11.2.4 Length Contraction
11.2.5 Addition of Velocities
11.3 The Geometry of Spacetime
11.3.1 The Invariant Interval
11.3.2 The Lorentz Group
11.3.3 A Rant: Why_c = 1
11.4 Relativistic Kinematics
11.4.1 Proper Time
11.4.2 4-Velocity
11.4.3 4-Momentum
11.4.4 Massless Particles
11.4.5 Newton's Laws of Motion
11.4.6 Acceleration
11.4.7 Indices Up, Indices Down
11.5 Particle Physics
11.5.1 Particle Decay
11.5.2 Particle Collisions
11.6 Lagrangians and Hamiltonians
11.6.1 The Covariant Action
11.6.2 The Hamiltonian for a Relativistic Particle
11.7 The Lorentz Group and SL(2, C)
11.7.1 A New Way of Looking at Spacetime 

11.7.2 What the Observer Actually Observes
11.7.3 Spinors
Further Reading
References
Index 

## Preface

Classical mechanics is an ambitious theory. Its purpose is to predict the future and reconstruct the past, to determine the history of every particle in the universe. 

The fundamental principles of classical mechanics were laid down by Galileo and Newton in the sixteenth and seventeenth centuries. Sitting at the heart of these ideas is a famous equation that we all met in school, 

$$
F = m a.
$$

This equates the force acting on a particle to its mass times acceleration. It means that if we want to predict the future (and we do) then there are two steps that we must take. 

The first step is to stand back, take stock of the situation, and figure out what forces are at play. Usual suspects include gravity, electromagnetism, and friction. The second step is then simply to solve F = ma to understand how the particles move. 

The first purpose of this book is to embark on this two-step programme for all the forces listed above, and many more besides. We will solve F = ma to see what it has to tell about different phenomena in the universe, from the motion of planets, to the scattering of electrons, to the formation of hurricanes, to falling cats. 

Despite its wild successes, it probably won't come as much of a surprise to hear that Newtonian mechanics is not the final word in theoretical physics. It might, however, come as something of a surprise to learn just how quickly we abandon some of the Newtonian ideas that seem, at first, to be so foundational. The concept of “force”, for example, is very seventeenth century and doesn't survive in more modern renderings of the laws of physics. While it's true that physicists still talk of “four fundamental forces of nature”, they mean it as a gentle nod to the language of our forefathers, rather than something that you plug into $F = ma$ and calculate. 

This brings us to the second purpose of this book, which is to reframe our ways of thinking about classical mechanics, stepping away from the Newtonian mindset of $F = ma$ and preparing ourselves for what will come next. As the concept of force falls by the wayside, other ideas, such as energy and symmetry, step to the fore. At the same time we will take a more global perspective, thinking not just of particles buffeted by forces, but instead considering the entire history of the particles, from the far past to the distant future. These developments, which took place in the centuries after Newton, culminate in two reformulations of classical mechanics, the first by Lagrange, the second by Hamilton. It is these Lagrangian and Hamiltonian descriptions of the world that will serve us best as we move forwards on our journey to understand the laws of physics. 

There is a third and final purpose to this book, and this is to start to get to grips with the meaning of space and time. These are concepts that are with us almost from the first page, but we're forced to think deeply about them only when the speeds of particles approach the speed of light. This is the realm of special relativity. It is a realm in which time slows down, and space contracts, and our common sense view of the world, honed through everyday experiences, proves hopelessly inadequate to understand what's actually going on in the universe. In other words, it's a realm where there is a lot of fun to be had. 

Ultimately, classical mechanics fails in its ambition to describe every particle in the universe. This is partly because, at some point, it is replaced by quantum mechanics and other theories, and partly because solving F = ma, or its successor equations, turns out to be really hard when more than a handful of particles are involved. Nonetheless, the lessons that we will learn in this book are necessary preparation for all subsequent developments in physics. Among these lessons sits what is, perhaps, the single most important legacy of Galileo and Newton: the laws of nature are written in the language of mathematics. This is one of the great insights of human civilisation, one that has ushered in scientific, industrial, technological, and information revolutions. It has given us a new way to look at the universe. And, most crucially of all, it means that the power to predict the future was not given to astrologers. It was given to mathematicians and physicists. The real goal of this book is to take the first steps towards grasping this power. 

## How to Read This Book

This book grew out of two courses that I taught at the University of Cambridge. One course was given to first year undergraduates and, roughly speaking, corresponds to the first six chapters, together with Chapter 11 on special relativity. The other was given to third year undergraduates and covers the Lagrangian formulation of Chapter 7, the Hamiltonian formulation of Chapter 10, and the rotation of rigid bodies described in Chapter 9. 

The first five chapters of this book cover the basics of Newtonian mechanics and should be read consecutively, Admittedly, there are a few diversions along the way that you should feel free to ignore. For example, the discussion of how the digits of pi emerge from bouncing balls in Section 4.2, and the geometric proof of Kepler's laws in Section 5.5, are meant only to bring a smile to your face, not as pre-requisites for anything that follows. 

After that, things are a bit more flexible. The two key chapters are 7 on the Lagrangian formulation, and 10 on the Hamiltonian formulation. You will need Lagrange to get going with Hamilton, so these should be read in order. 

Interspersed between these are Chapter 6 on rotating frames, Chapter 8 on small oscillations and Chapter 9 on rigid body motion. These can be read in any order. None of them are necessary for the Lagrangian and Hamiltonian chapters except for a handful of examples 

That leaves special relativity. It is the final chapter of this book but much of it can be read without knowledge of any of the previous chapters. (Alright, maybe it would make sense to read Chapter 1 first since it covers, among other things, Galileo's precursor ideas of relativity.) Moreover, the mathematics of special relativity is significantly easier than that in other parts of the book, even if the underlying concepts are not. So if you're like I was as a student, and are desperate to learn some special relativity, then feel free to jump in anytime. 

## Just One Book Among Many

This book is the first in a series of N, where $N \gg 1$ . The collective goal of these books is to cover a swathe of theoretical physics which, with broad brush, coincides with the material that we teach in the mathematics degree at the University of Cambridge. 

Theoretical physics is a vast subject and there are many paths through it, but there is only one logical place to start and that is with classical mechanics. Even as we embrace new, shinier theories in later books – field theories and quantum theories and quantum field theories – everything ultimately rests on the structure of classical mechanics that we will describe here. A good understanding of classical mechanics is crucial to move forwards. 

Nonetheless, physics isn't a linear subject. Many of the most beautiful learning moments arise when we see connections between seemingly unrelated topics, or when an idea that is familiar in one context makes a cameo appearance somewhere unexpected. For that reason, I wouldn't necessarily recommend starting on page 1 of Volume 1 and reading, uninterrupted, to the end of Volume $N$ . I would, obviously, recommend reading all those pages. Just not necessarily in that order. 

The cross-over between this book and later books is most pronounced in Chapter 10 which covers the Hamiltonian formulation of classical mechanics. One of the primary reasons to study the Hamiltonian formalism is because of its close connections with quantum mechanics. While the material presented in Chapter 10 is self-contained, the 

motivation behind it is likely to make more sense if you already have an appreciation of the basics of quantum mechanics (say, at the level of the first three chapters of Volume 3 of this series). That will offer a greater “aha” moment when you see some of the more mysterious equations of quantum mechanics sitting there all along in the classical world. Section 10.8 of the book you’re holding then throws caution to the wind and makes much more explicit connections with quantum mechanics. I think it’s fair to say that you’ll have no idea what’s going on in that section unless you have some previous quantum exposure. 

Finally, there are two places where ideas from quantum field theory sneak into this book. The first is Section 9.7 on falling cats, the second Section 11.7 on the role of spinors in special relativity. Neither of these sections needs an understanding of quantum field theory, but I suspect that they will bring more joy after you're familiar with non-Abelian gauge theories (for cats) and the Dirac equation. 

## Problems

I have not included any exercises in this series of books. However, the Faculty of Mathematics at the University of Cambridge has long had a policy of making all problems (and, indeed, exam questions) publicly available. 

Problem sheets aligned with the material in this book can be downloaded from: 

www.damtp.cam.ac.uk/user/tong/books/classical.html 

An errata can also be found on this webpage. 

## Acknowledgements

This book, like all the others, owes an enormous debt to both those that taught me physics, and those that taught me how to teach physics. Among the latter are my colleagues in Cambridge who collectively, over many decades, have put together a bulk of resources that is passed down the years, from one lecturer to another. I have taken freely from this material in my own teaching and can only hope that I’ve put back as much as I’ve taken out. 

The first few chapters of this book are based on a course that I inherited from Stephen Siklos who was one of the pedagogical maestros of my department. A number of the examples in these chapters are due to him. Later chapters draw upon lectures by Gary Gibbons, Robin Hudson, and Michael Peskin. I'm also grateful to Sean Hartnoll and David Skinner for discussions on how to teach classical mechanics, and to Tom Hillman for going through an early draft of the book with extraordinary diligence. 

My thanks to Nick Gibbons at Cambridge University Press for his encouragement in writing this series of books and to Malgo Kenyon for the cover photos. The picture on the front cover is Ernest Rutherford's copy of Newton's Principia, with handwritten notes in the margin to make sure that Newton did the maths right. The back cover shows one of the original printing blocks for the second edition of the Principia. These blocks were created by the wonderfully named Mr Lightbody who was accused, in a letter to Newton, of being both a sot and a prankster. Both of these items are housed in the Wren Library of Trinity College Cambridge. (The former has reference number Adv.c.25.88; the latter is famous enough to be un-numbered.) I'm grateful to the Master and Fellows of Trinity College for permission in reproducing these images, and to Nicolas Bell for introducing me to these items. 

Finally, my deepest thanks to Alex Considine Tong for the years of love and support and for putting up with the lost weekends as these books very slowly took shape. 

# Newtonian Mechanics

So few went to hear him, and fewer understood him, that oftimes he did, for want of hearers, read to the walls. He usually stayed about half an hour; when he had no auditors he commonly returned in a quarter of that time. 

Teaching evaluation of a well-known Cambridge lecturer in 

classical mechanics, circa 1690. 

Classical mechanics is all about the motion of particles. We start by explaining the meaning of the word “particle”. 

Definition: A particle is an object of insignificant size. This means that if you want to describe what a particle looks like at a given time, the only information you have to specify is its position. 

In this book, we will treat electrons, tennis balls, falling cats, and planets as particles. In all cases, this means that we only care about the position of the object and our analysis will not, for example, be able to say anything about the look on the cat's face as it falls. It's not immediately obvious that we can meaningfully assign a single position to a complicated object such as a spinning, mewing cat. Should we describe its position as the end of its tail or the tip of its nose? We will not provide an immediate answer to this question, but we will return to it in Chapter 4 where we will show 

that any object can be treated as a point-like particle if we look at the motion of its centre of mass. 

To describe the position of a particle we need a reference frame. This is a choice of origin, together with a set of fixed, orthogonal axes. With respect to this frame, the position of a particle is specified by a vector x, which we denote using bold font. Since the particle moves, the position depends on time, resulting in a trajectory of the particle described by the function 

$$
\mathbf {x} = \mathbf {x} (t) .\tag{1.1}
$$

Sometimes we will find it useful to use the notation $\mathbf{r}(t)$ , instead of $\mathbf{x}(t)$ , to describe the trajectory of a particle. 

The velocity v of a particle is defined to be 

$$
\mathbf {v} = \frac {d \mathbf {x} (t)}{d t}.\tag{1.2}
$$

Throughout these notes, we will often denote differentiation with respect to time by a “dot” above the variable. So we will also write $v = \dot{x}$ . The second derivative with respect to time is 

$$
\mathbf {a} = \ddot {\mathbf {x}} = \frac {d ^ {2} \mathbf {x} (t)}{d t ^ {2}}.\tag{1.3}
$$

This is the acceleration of the particle. 

A sociological aside: the dot-as-derivative was Newton's original notation and, 350 years later, comes with some baggage. In physics, a dot is nearly always used to denote differentiation with respect to time, hence $\dot{\mathbf{x}}$ for velocity and $\ddot{\mathbf{x}}$ for acceleration. Meanwhile, differentiation of a function $f(x)$ that depends on a single spatial coordinate $x$ is usually denoted with a prime, as in $f'(x)$ . This is deeply ingrained in the psyche of physicists, so much so that I get a little shudder if I see something like $x'(t)$ meaning $dx/dt$ . Mathematicians, apparently, have no such cultural hang-ups on this issue and use dot and prime interchangeably. (They reserve their cultural hang-ups for a thousand other issues.) We will use $\mathbf{x}'$ in places throughout this book, including in two pages time, but always to mean some other spatial variable, never to mean differentiation. 

## 1.1 Newton's Laws of Motion

Newtonian mechanics is a framework that allows us to determine the trajectory $\mathbf{x}(t)$ of a particle in any given situation. This framework is usually presented as three axioms known as Newton's laws of motion. They look something like this: 

• N1: Left alone, a particle moves with constant velocity. 

- N2: The acceleration of a particle is proportional to the force acting upon it. 

• N3: Every action has an equal and opposite reaction. 

While it is worthy to try to construct axioms on which the laws of physics rest, the trite, minimalistic attempt above falls somewhat short. For example, at first glance it appears that the first law is nothing more than a special case of the second law. (If the force vanishes, the acceleration vanishes which is the same thing as saying that the velocity is constant.) But that's not the way axioms are supposed to work! You shouldn't be able to derive one from the other. 

In fact, the meaning of the first law is somewhat more subtle than the statement presented above. In what follows we will take a closer look at what really underlies Newtonian mechanics. We start by examining Newton's first and second laws, both of which hold for a single particle, and then illustrate the ideas with many examples. Newton's third law is really to do with the interactions between two or more particles and we postpone its discussion to Chapter 4. 

## 1.1.1 Newton's First Law

Placed in the historical context, it is understandable that Newton wished to stress the first law. It is a rebuttal to the older view of Aristotle who argued that, when left alone, an object will naturally come to rest. The first law stresses that the natural state of an object is to travel with constant velocity, a fact first appreciated by Galileo. This is the essence of what we call inertia. 

However, these days we're not bound to any Aristotelian dogma. Do we really need the first law? The answer is yes, but it has a somewhat different meaning from what we stated above. 

We've already introduced the idea of a frame of reference: a Cartesian coordinate system in which you measure the position of the particle. But for most reference frames that you can think of, Newton's first law is obviously false. For example, suppose that you're measuring the position of a particle while sitting on a merry-go-round. Then, everything will appear to be spinning around you. If you measure a particle's trajectory in these rotating coordinates and insist on calling it $\mathbf{x}(t)$ , then you certainly won't find that $d^2\mathbf{x}/dt^2 = 0$ , even if you leave the particle alone. In rotating frames, particles do not travel at constant velocity. (We will look more closely at what does happen in rotating reference frames in Chapter 6.) 

This means that if we want Newton's first law to fly at all, we must be more careful about the kind of reference frames we're talking about. We define an inertial reference frame to be one in which particles do indeed travel at constant velocity when the force acting on it vanishes. In other words, in an inertial frame, a particle has $\ddot{x} = 0$ when left alone. The true content of Newton's first law can then be better stated as 

• N1 Revisited: Inertial frames exist. 

These inertial frames provide the setting for all that follows. For example, the second law, which we will discuss shortly, should be formulated in inertial frames. 

One way to ensure that you are in an inertial frame is to insist that you yourself have no forces acting on you. Fly out into deep space, far from the effects of gravity and other influences, turn off your engines and sit there. This is an inertial frame. However, for most purposes it will suffice to treat the axes of the room you're sitting in as an inertial frame. Of course, this is an approximation because these axes are stationary with respect to the Earth and the Earth is rotating, both about its own axis and about the Sun. This means that the Earth does not quite provide an inertial frame. We will study the consequences of this in Chapter 6. 

## 1.1.2 Galilean Relativity

Inertial frames are not unique. Given one inertial frame S in which a particle has coordinates $\mathbf{x}(t)$ , we can always construct another inertial frame $S'$ in which the particle has coordinates $\mathbf{x}'(t)$ by any combination of the following transformations, 

- Translations: $\mathbf{x}' = \mathbf{x} + \mathbf{a}$ , for constant $\mathbf{a}$ . 

- Rotations: $\mathbf{x}' = R\mathbf{x}$ , for a $3 \times 3$ orthogonal matrix $R$ obeying $R^T R = 1$ . This also allows for reflections if $\det R = -1$ . 

- Boosts: $\mathbf{x}' = \mathbf{x} + \mathbf{u}t$ , for constant velocity $\mathbf{u}$ . 

Each of these transformations maps one inertial frame to another. To see this, suppose that a particle moves with constant velocity with respect to frame S, so that $d^{2}x/dt^{2}=0$ . Then, for each of the transformations above, we also have $d^{2}x'/dt^{2}=0$ which tells us that the particle also moves at constant velocity in $S'$ . Or, in other words, if S is an inertial frame then so too is $S'$ . 

The three transformations generate an object that mathematicians call a group or, in this specific case, the Galilean group. Roughly speaking, we have a mathematical group on our hands because you can always string different transformations together – say, a translation followed by a boost, followed by a rotation – and that too will take one inertial frame to another. The mathematical structure of groups is how we think about symmetries in physics, and we will meet many, both in this book and in later volumes in the series. 

We have already mentioned that Newton's second law is to be formulated in an inertial frame. But, importantly, it doesn't matter which inertial frame. In fact, this turns out to be true for other laws of physics as well: they are the same in any inertial frame. This is known as the principle of relativity. The three types of transformation that make up the Galilean group map from one inertial frame to another. Combined with the principle of relativity, each is telling us something important about the world we live in: 

- Translations: There is no special point in the universe. 

- Rotations: There is no special direction in the universe. 

- Boosts: There is no special velocity in the universe. 

The first of these tells us that position is relative: there's no well defined origin in the universe that you can measure your distance from. Instead, your position can be measured only relative to the position of others. Of course, some of those other points may have personal significance and you may have a preference to place the origin at, say, your mum's house, or the Sun. But others may disagree with your choice of origin and you shouldn't be offended. The laws of physics do not prefer one choice over another. 

The second is similar in spirit: direction is relative. The universe does not provide us with a preferred direction. The fact that both position and direction are relative continues to be true as we go to more advanced theories of physics. 

The third implication of the principle of relativity needs more explanation, not least because it comes with caveats. It is telling us that there is no such thing as “absolutely stationary”. You can only be stationary with respect to something else. This too continues to hold in all subsequent laws of physics. However, in contrast to translations and rotations, it will ultimately turn out that not all laws of physics are invariant under Galilean boosts, $x' = x + ut$ , and the bold statement that there is no special speed in the universe is not true. The speed of light is special. This doesn’t mean that we should abandon the principle of relativity for boosts entirely, but it does need modifying. This modification is known as special relativity and is the subject of Chapter 11. 

So position, direction, and velocity are relative. But acceleration is not. You do not have to accelerate relative to something else. It makes perfect sense to simply say that you are accelerating or you are not accelerating. In fact, this brings us back to Newton's first law: if you are not accelerating, you are sitting in an inertial frame. 

The principle of relativity is usually associated to Einstein because of the modifications he made in developing special relativity. But the key idea of relativity dates back at least as far as Galileo. In his book, “Dialogue Concerning the Two Chief World Systems”, published in 1632, Galileo has the character Salviati talk eloquently about the relativity of boosts, 

Shut yourself up with some friend in the main cabin below decks on some large ship, and have with you there some flies, butterflies, and other small flying animals. Have a large bowl of water with some fish in it; hang up a bottle that empties drop by drop into a wide vessel beneath it. With the ship standing still, observe carefully how the little animals fly with equal speed to all sides of the cabin. The fish swim indifferently in all directions; the drops fall into the vessel beneath; and, in throwing something to your friend, you need throw it no more strongly in one direction than another, the distances being equal; jumping with your feet together, you pass equal spaces in every direction. 

When you have observed all these things carefully (though doubtless when the ship is standing still everything must happen in this way), have the ship proceed with any speed you like, so long as the motion is uniform and not fluctuating this way and that. You will discover not the least change in all the effects named, nor could you tell from any of them whether the ship was moving or standing still. 

## Absolute Time

There is one last issue that we have left implicit in the discussion above: the choice of time coordinate t. If observers in two inertial frames, S and $S'$ , fix the units – seconds, minutes, hours – in which to measure the duration of time then the only remaining choice they can make is when to start the clock. In other words, the time variables in S and $S'$ differ only by 

$$
t ^ {\prime} = t + t _ {0}.\tag{1.4}
$$

This is sometimes included among the transformations that make up the Galilean group. 

The existence of a uniform time, measured equally in all inertial reference frames, is referred to as absolute time. It is also something that we will have to revisit when we discuss special relativity. As with the other Galilean transformations, the ability to shift the origin of time is reflected in an important property of the laws of physics. The fundamental laws don't care when you start the clock. All evidence suggests that the laws of physics are the same today as they were yesterday. They are time translationally invariant. 

## Cosmology

Notably, the universe itself breaks several of the Galilean transformations. There was a very special time in the universe, around 13.8 billion years ago. This is the time of the Big Bang (which, loosely translated, means “we don’t know what happened here”). 

Similarly, there is one preferred inertial frame in which the universe can be thought of as stationary. This arises due to a sea of photons, known as the cosmic microwave background, or CMB for short, which sits at a temperature of 2.7 K and fills the universe. These photons are the afterglow of the fireball that filled all of space when the universe was much younger. Different inertial frames are moving relative to this background and measure the CMB differently: due to a “redshift” effect that we will describe in Chapter 11, the radiation looks more blue in the direction that you’re travelling, redder in the direction that you’ve come from. There is an inertial frame in which this background radiation is uniform, meaning that it is the same colour in all directions. 

To the best of our knowledge, however, the universe defines neither a special point, nor a special direction. It is, to very good approximation, homogeneous and isotropic. 

It's worth stressing that this discussion of cosmology in no way invalidates the principle of relativity. All laws of physics are the same regardless of which inertial frame you are in. Overwhelming evidence suggests that the laws of physics are the same in far flung reaches of the universe. They were the same in the first few microseconds after the Big Bang as they are now. 

## 1.1.3 Newton's Second Law

The second law is the meat of the Newtonian framework. It is the famous “F = ma”, that tells us how a particle’s motion is affected when subjected to a force. The vector form of the equation is 

$$
m \ddot {\mathbf {x}} = \mathbf {F} (\mathbf {x}, \dot {\mathbf {x}}) .\tag{1.5}
$$

This is usually referred to as the equation of motion. Here m is the mass of the particle or, more precisely, the inertial mass. It is a measure of the reluctance of the particle to change its motion when subjected to a given force F. 

The momentum of the particle, P, is defined to be 

$$
\mathbf {p} = m \dot {\mathbf {x}}.\tag{1.6}
$$

Assuming constant mass, we can also write Newton's second law as 

$$
\dot {\mathbf {p}} = \mathbf {F} (\mathbf {x}, \dot {\mathbf {x}}).\tag{1.7}
$$

As we turn to more advanced situations, such as Hamilton's equations in Chapter 10, or special relativity in Chapter 11, it will turn out that the relationship between velocity and momentum can be more complicated than (1.6). In that case, the form of Newton's equations given in (1.7) is the correct one to use. 

The equation of motion isn't useful until someone tells us what the force $\mathbf{F}$ is in any given situation. We will describe many examples of forces in this book and, for each, solve (1.5) to determine the trajectory of the particle. In general, the force can depend on the position $\mathbf{x}$ and the velocity $\dot{\mathbf{x}}$ of the particle, but does not depend on any higher derivatives. We could also, in principle, consider forces which include an explicit time dependence, $\mathbf{F}(\mathbf{x},\dot{\mathbf{x}},t)$ . Finally, if more than one (independent) force is acting on the particle, then we simply take their sum on the right-hand side of $(1.5)$ . 

Note that we've written the second law in (1.5) as “ma = F”, rather than the more familiar “F = ma”. Obviously these are the same equation mathematically! But the way of writing the equation gives a little psychological nudge about the relation between cause and effect. In physics, we tend to think that the force acts on the particle, causing the particle to accelerate. Hence you can read (1.5) as telling you the acceleration, given the force. However, it's worth mentioning that there's nothing in the mathematics that tells you that force determines acceleration, rather than the other way round. 

The single most important fact about Newton's equation is that it is a second order differential equation. This means that we will have a unique solution only if we specify two initial conditions. These are usually taken to be the position $\mathbf{x}(t_0)$ and the velocity $\dot{\mathbf{x}}(t_0)$ at some initial time $t_0$ . However, exactly what boundary conditions you must choose in order to figure out the trajectory depends on the problem you are trying to solve. For example, in Chapter 7, we'll describe the principle of least action, which requires that we specify the position at some initial and final time to determine the trajectory. 

The fact that the equation of motion is second order is a deep statement about the universe. It carries over, in essence, to all other laws of physics, from quantum mechanics to general relativity to particle physics. Indeed, the fact that all initial conditions must come in pairs – two for each “degree of freedom” in the problem – has important ramifications for 

later formulations of both classical and quantum mechanics. We'll shed more light on this statement in the context of classical mechanics in Chapter 10 when we discuss the Hamiltonian formulation. 

For now, the fact that the equations of motion are second order means the following: if you are given a snapshot of some situation and asked “what happens next?” then there is no way of knowing the answer. It’s not enough just to know the positions of the particles at some point of time; you need to know their velocities too. However, once both of these are specified, the future evolution of the system is fully determined for all time. 

## 1.1.4 Looking Forwards: The Validity of Newtonian Mechanics

Although Newton's laws provide an excellent approximation to many phenomena, when pushed to extreme situations they are found wanting. Broadly speaking, there are three directions in which Newtonian physics needs replacing with a different framework. They are: 

- When particles travel at speeds close to the speed of light, $c \approx 3 \times 10^{8} \mathrm{~ms}^{-1}$ , the Newtonian concept of absolute time breaks down and Newton's laws need modification. The resulting theory is called special relativity and will be described in Chapter 11 of this book. However, as we will see, although the relationship between space and time is altered in special relativity, much of the underlying framework of Newtonian mechanics survives unscathed. 

- On very small scales, much more radical change is needed. Here the whole framework of classical mechanics breaks down so that even the most basic concepts, such as the trajectory of a particle, become ill-defined. The new framework that holds on these small scales is called quantum mechanics and is described in Volume 3 of this series. Nonetheless, there are deep and surprising connections between the classical and quantum worlds. The latter part of this book will lay out classical mechanics in a way that prepares us for the quantum leap. 

- When we try to describe the forces at play between particles, we need to introduce a new concept: the field. This is a function of both space and time. The most familiar examples are the electric and magnetic fields. These too have equations of motion, known as the Maxwell equations. In addition there is an object called the gravitational field that, ultimately, is governed by Einstein's theory of general relativity. We will only briefly touch upon fields in this book, although we'll have plenty to say in subsequent books, starting with Volume 2 on Electromagnetism. For now, we mention only that the equations that govern the dynamics of fields are always second order differential equations, similar in spirit to Newton's equations. 

Eventually, the ideas of special relativity, quantum mechanics, and field theories are combined into the subject of quantum field theory. Here even the concept of a particle gets subsumed into the concept of a field. This is currently the best framework we have to describe the world around us. But we're getting ahead of ourselves. First, we should return to our Newtonian world... 

## 2 Forces

So far, we have described only the framework of Newtonian mechanics, in the guise of the famous equation $F = m\ddot{x}$ . But to do anything with this equation, we need to specify the force F that acts on the particle. In principle, there could be many different possibilities for these forces. In practice, the important forces are relativity few. We will describe some of these forces in this chapter. 

Throughout this chapter, we will restrict our attention to forces acting on a single particle. Obviously, a world with just one particle is rather limiting. Moreover, it means that some of the ideas of Galilean invariance that we stressed in the previous chapter won't be obvious. For example, it's only when we consider the interactions between two or more particles that the laws of physics become manifestly translationally invariant. We will remedy this only in Chapter 4 when we discuss what happens when we have more than one particle. In the meantime, the concepts that we will learn in this chapter, such as the importance of energy conservation, will be constant companions throughout the rest of the book (and, indeed, throughout other books in the series). 

## 2.1 Potentials in One Dimension

To set the scene, we start by considering a simple, idealised situation. We will assume that our particle can move only in one direction, so its position is determined by a single function $x(t)$ . For now, suppose that the force on the particle depends only on the position, not the velocity. This means that $F = F(x)$ . 

We define the potential energy $V(x)$ (also called simply the potential) by the equation 

$$
F (x) = - \frac {d V}{d x}.\tag{2.1}
$$

The potential is only defined up to an additive constant. We can always invert $(2.1)$ by integrating both sides. The integration constant is now determined by the choice of lower limit of the integral 

$$
V (x) = - \int_ {x _ {0}} ^ {x} d x ^ {\prime} F (x ^ {\prime}).\tag{2.2}
$$

Here $x'$ is just a dummy variable. (Do not confuse the prime with differentiation!) With this definition, we can write the equation of motion as 

$$
m \ddot {x} = - \frac {d V}{d x}.\tag{2.3}
$$

For any force in one dimension that depends only on the position, there exists a conserved quantity called the energy 

$$
E = \frac {1}{2} m \dot {x} ^ {2} + V (x).\tag{2.4}
$$

The fact that this is conserved means that $\dot{E}=0$ for any trajectory of the particle that obeys the equation of motion. 

While $V(x)$ is called the potential energy, $T = \frac{1}{2} m \dot{x}^{2}$ is called the kinetic energy. 

It is not hard to prove that E is conserved. We need only differentiate to get 

$$
\dot {E} = m \dot {x} \ddot {x} + \frac {d V}{d x} \dot {x} = \dot {x} \left(m \ddot {x} + \frac {d V}{d x}\right) = 0\tag{2.5}
$$

where the last equality holds courtesy of the equation of motion $(2.3)$ . 

In any dynamical system, conserved quantities of this kind are very precious. We will spend some time in this book fishing them out of the equations, understanding their origin, and showing how they help us simplify various problems. 

## An Example: A Uniform Gravitational Field

In a uniform gravitational field, a particle is subjected to a constant force, $F = -mg$ where $g \approx 9.8 \, \text{m s}^{-2}$ is the acceleration due to gravity near the surface of the Earth. The minus sign arises because the force is downwards while we have chosen to measure position in an upwards direction which we call $z$ . The potential energy is 

$$
V = m g z.\tag{2.6}
$$

Notice that we have chosen to set V = 0 at z = 0. There is nothing that forces us to do this; we could easily add an extra constant to the potential to shift the zero to some other height. 

The equation of motion for uniform acceleration is 

$$
\ddot {z} = - g.\tag{2.7}
$$

This can be trivially integrated to give the velocity at time t, 

$$
\dot {z} = u - g t\tag{2.8}
$$

where u is the initial velocity at time t = 0. (Note that z is measured in the upwards direction, so the particle is moving up if $\dot{z} > 0$ and down if $\dot{z} < 0$ .) Integrating once more gives the position 

$$
z = z _ {0} + u t - \frac {1}{2} g t ^ {2}\tag{2.9}
$$

where $z_{0}$ is the initial height at time t = 0. Many high schools, at least in the UK, teach that $(2.8)$ and $(2.9)$ are the key equations of mechanics. They are not. They are merely the integration of Newton's second law for constant acceleration. 

## Another Example: The Harmonic Oscillator

The harmonic oscillator is, by far, the most important dynamical system in all of theoretical physics. The good news is that it's very easy. In fact, part of the reason that it's so important is precisely because it's easy! The potential energy of the harmonic oscillator is defined to be 

$$
V (x) = \frac {1}{2} k x ^ {2}.\tag{2.10}
$$

Here $k$ is a constant that governs the strength of the potential. The harmonic oscillator is a good model for, among other things, a particle attached to the end of a spring. In this context, the constant $k$ is called the spring constant. The force (2.1) resulting from the energy $V$ is given by $F = -kx$ which, in the context of the spring, is called Hooke's law. The equation of motion is 

$$
m \ddot {x} = - k x.\tag{2.11}
$$

This has the general solution 

$$
x (t) = A \cos (\omega t) + B \sin (\omega t) \quad \mathrm{with} \quad \omega = \sqrt {\frac {k}{m}}.\tag{2.12}
$$

Here $A$ and $B$ are two integration constants and $\omega$ is the angular frequency. Strictly the frequency itself is defined to be $f = \omega / 2\pi$ but, in all areas of physics, it's nearly always the angular frequency $\omega$ that appears and so we, rather lazily, just refer to $\omega$ as the frequency. 

The solution (2.12) tells us that all trajectories are qualitatively the same: they just bounce back and forth around the origin. The coefficients A and B in (2.12) determine the amplitude of the oscillations, together with the phase at which you start the cycle. The general solution can also be written in the alternate form 

$$
x (t) = C \cos (\omega (t - t _ {0}))\tag{2.13}
$$

now with two integration constants C and $t_{0}$ , related to A and B by some simple trigonometric identities. 

The time taken to complete a full cycle is called the period 

$$
T = \frac {2 \pi}{\omega}.\tag{2.14}
$$

The period is independent of the amplitude. Note that, annoyingly, the kinetic energy is also often denoted by T as well. Do not confuse this with the period. It should hopefully be clear from the context. 

If we want to determine the integration constants A and B for a given trajectory, then we need some initial conditions. For example, if we're given the position $x(0)$ and velocity $\dot{x}(0)$ at time t=0, then it's simple to check that $A=x(0)$ and $B\omega=\dot{x}(0)$ . 

## 2.1.1 Moving in a Potential

Let's go back to the general case of a potential $V(x)$ in one dimension. Although the equation of motion is a second order differential equation, the existence of a conserved energy magically allows us to turn this into a first order differential equation 

$$
E = \frac {1}{2} m \dot {x} ^ {2} + V (x) \quad \Longrightarrow \quad \frac {d x}{d t} = \pm \sqrt {\frac {2}{m} (E - V (x))}.
$$

This gives us our first hint of the importance of conserved quantities in helping solve a problem. Of course, to go from a second order equation to a first order equation, we must have chosen an integration constant. In this case, that is the energy E itself. Given a first order equation, we can always write down a formal solution for the dynamics simply by integrating. Providing the velocity in $(2.15)$ has a fixed sign, we have 

$$
t - t _ {0} = \pm \int_ {x _ {0}} ^ {x} \frac {d x ^ {\prime}}{\sqrt {\frac {2}{m} (E - V (x ^ {\prime}))}}.\tag{2.16}
$$

As before, $x'$ is a dummy variable. If we can do the integral, we've solved the problem. If we can't do the integral, you sometimes hear that the problem has been “reduced to quadrature”. This rather old-fashioned phrase is a cute way of saying “I can't do the integral”. But it is often the case that having a solution in this form allows some of its properties to become manifest. And, if nothing else, one can always just evaluate the integral numerically (i.e. on your laptop) if need be. 

## Getting a Feel for the Solutions

Given the potential energy, it is often very simple to figure out the qualitative nature of any trajectory simply by looking at the form of $V(x)$ . This allows us to answer some questions with very little work. For example, we may want to know whether the particle is trapped within some region of space or whether it can escape to infinity. 

We can illustrate this with an example. Consider the cubic potential 

$$
V (x) = m (x ^ {3} - 3 x).\tag{2.17}
$$

If we were to substitute this into the general form (2.16), we'd get a fearsome looking integral (known, for what it's worth, as an elliptic integral). However, we can make plenty of progress even without solving the integral. The potential is plotted in Figure 2.1. Let's start with the 

particle sitting stationary at some position $x_{0}$ . This means that the energy is 

$$
E = V (x _ {0})\tag{2.18}
$$

and this must remain constant during the subsequent motion. What happens next depends only on $x_{0}$ . We can identify the following possibilities: 

- $x_0 = \pm 1$ : These are, respectively, the local minimum and maximum. If we drop the particle at these points, it stays there for all time. 

- $x_0 \in (-1, +2)$ : Here the particle is trapped in the dip. It oscillates backwards and forwards between the two points with potential energy $V(x_0)$ . The particle can't climb to the right because it doesn't have the energy. In principle, it could live off to the left where the potential energy is negative, but to get there it would have to first climb the small bump at $x = -1$ and it doesn't have the energy to do so. (There is an assumption here which is implicit throughout all of classical mechanics: the trajectory of the particle $x(t)$ is a continuous function.) 

- $x_0 > 2$ : When released, the particle falls into the dip, and climbs up and over the bump before falling into the void $x \to -\infty$ . 

- $x_0 < -1$ : The particle just falls off to the left. 

- $x_0 = +2$ : This is a special value, since $E = 2m$ which is the same as the potential energy at the local maximum, $x = -1$ . The particle falls into the dip and starts to climb up towards $x = -1$ . It can never stop before it reaches $x = -1$ because, at its stopping point, it would have only potential energy $V < 2m$ . But, similarly, if it ever arrives at $x = -1$ 

then it must be stationary when it gets there and this means that it can't subsequently leave. The only option is that the particle moves towards $x = -1$ at an ever decreasing speed, only reaching the maximum at time $t \to \infty$ . 

To see that this is indeed the case, we can consider the motion of the particle when it is close to the maximum. We write $x \approx -1 + \epsilon$ with $\epsilon \ll 1$ . Then, dropping the $\epsilon^{3}$ term, the potential is 

$$
V (x = - 1 + \epsilon) \approx 2 m - 3 m \epsilon^ {2} + \ldots\tag{2.19}
$$

Using (2.16), the time taken to reach $x = -1 + \epsilon$ from some starting position $x = -1 + \epsilon_{0}$ , where $\epsilon < \epsilon_{0} \ll 1$ , is 

$$
t - t _ {0} = - \int_ {\epsilon_ {0}} ^ {\epsilon} \frac {d \epsilon^ {\prime}}{\sqrt {6} \epsilon^ {\prime}} = - \frac {1}{\sqrt {6}} \log \left(\frac {\epsilon}{\epsilon_ {0}}\right).\tag{2.20}
$$

The logarithm on the right-hand side gives a divergence as $\epsilon \rightarrow 0$ . This tells us that it indeed takes infinite time to reach the top as promised. 

We can easily play a similar game to that above if the starting speed is not zero. In general, one finds that the particle is trapped in the dip if it sits in $x \in [-1, +2]$ with energy in the interval $E \in [-2m, 2m]$ . 

## Fig. 2.1 The cubic potential

## 2.1.2 Why (Almost) Everything is a Harmonic Oscillator

A particle placed at an equilibrium point will stay there for all time. 

In our last example, with a cubic potential (2.17), we saw two equilibrium points: $x = \pm 1$ . In general, if we want $\dot{x} = 0$ for all time, then clearly we must have $\ddot{x} = 0$ , which, from the form of Newton's equation (2.3), tells us that we can identify the equilibrium points with the critical points of the potential 

$$
\frac {d V}{d x} = 0.\tag{2.21}
$$

What happens to a particle that is close to an equilibrium point, $x_{0}$ ? In this case, we can Taylor expand the potential energy about $x = x_{0}$ . Because, by definition, the first derivative vanishes, we have 

$$
V (x) \approx V (x _ {0}) + \frac {1}{2} V ^ {\prime \prime} (x _ {0}) (x - x _ {0}) ^ {2} + \dots .\tag{2.22}
$$

To continue, we need to know the sign of $V''(x_{0})$ . There are three possibilities: 

- $V''(x_0) > 0$ : In this case, the equilibrium point is a minimum of the potential and the potential energy approximates that of a harmonic oscillator. From our discussion of Section 2.1.2, we know that the particle oscillates backwards and forwards around $x_0$ with frequency 

$$
\omega = \sqrt {\frac {V ^ {\prime \prime} (x _ {0})}{m}}.\tag{2.23}
$$

Such equilibrium points are called stable. This analysis shows that if the amplitude of the oscillations is small enough (so that we may ignore the $(x - x_{0})^{3}$ terms in the Taylor expansion) then all systems oscillating around a stable fixed point look like a harmonic oscillator. 

- $V''(x_0) < 0$ : In this case, the equilibrium point is a maximum of the potential. The equation of motion again reads 

$$
m \ddot {x} = - V ^ {\prime \prime} (x _ {0}) (x - x _ {0}).\tag{2.24}
$$

But with $V'' < 0$ , we have $\ddot{x} > 0$ when $x - x_{0} > 0$ . This means that if we displace the system a little bit away from the equilibrium point, then the acceleration pushes it further away. The general solution is 

$$
x - x _ {0} = A e ^ {\alpha t} + B e ^ {- \alpha t} \quad \mathrm{with} \quad \alpha = \sqrt {\frac {- V ^ {\prime \prime} (x _ {0})}{m}}.
$$

Any solution with the integration constant $A \neq 0$ will rapidly move away from the fixed point. Since our whole analysis started from a Taylor expansion (2.22), neglecting terms of order $(x - x_{0})^{3}$ and higher, our approximation will quickly break down. We say that such equilibrium points are unstable. 

There are solutions around unstable fixed points with A = 0 and $B \neq 0$ which move back towards the maximum at late times. These finely tuned solutions arise in the kind of situation that we described for the cubic potential where you drop the particle at a very special point (in the case of the cubic potential, this point was x = 2) so that it just reaches the top of a hill in infinite time. Clearly these solutions are not generic: they require very special initial conditions. 

- Finally, we could have $V''(x_0) = 0$ . In this case, there is nothing we can say about the dynamics of the system without Taylor expanding the potential further. 

## Yet Another Example: The Pendulum

Consider a particle of mass $m$ attached to the end of a light rod of length $l$ . At first glance, this looks like a two-dimensional system because the pendulum is swinging in the $(x, y)$ -plane. But, in fact, it's really a one-dimensional system because we need only specify a single coordinate to say what the system looks like at a given time. The best coordinate to choose is $\theta$ , the angle that the rod makes with the vertical, with 

$$
\mathbf {x} = l (\sin \theta , \cos \theta).\tag{2.26}
$$

Differentiating this vector with respect to time, and using the chain rule, we have 

$$
\begin{array}{l} \dot {\mathbf {x}} = l \dot {\theta} (\cos \theta , - \sin \theta) \\ \ddot {\mathbf {x}} = l \ddot {\theta} (\cos \theta , - \sin \theta) - l \dot {\theta} ^ {2} (\sin \theta , \cos \theta). \end{array}\tag{2.27}
$$

The forces on the pendulum are gravity, acting downwards as $mg = (0, mg)$ , and the tension T, acting through the rod. So Newton's equation of motion, $m\ddot{x} = mg + T$ , becomes 

$$
m l \ddot {\theta} (\cos \theta , - \sin \theta) - m l \dot {\theta} ^ {2} (\sin \theta , \cos \theta) = m g (0, 1) + T (- \sin \theta , - \cos \theta)
$$

If we now take the inner product of this equation with the vector $(\cos\theta,-\sin\theta)$ , which is perpendicular to x, we get the equation of motion for the pendulum 

$$
\ddot {\theta} = - \frac {g}{l} \sin \theta .\tag{2.29}
$$

The force is proportional to $\sin\theta$ and can be viewed as coming from a potential energy proportional to $\cos\theta$ . Indeed, this is just the gravitational potential energy of the pendulum. The total energy is 

$$
E = \frac {1}{2} m l ^ {2} \dot {\theta} ^ {2} - m g l \cos \theta .\tag{2.30}
$$

Note that because $\theta$ is an angular variable, rather than a linear variable, the kinetic energy is a little different than the usual $\frac{1}{2}m\dot{x}^{2}$ . This follows from a little trigonometry. We will give a careful derivation of this result in Chapter 5. 

There are two qualitatively different motions of the pendulum. The potential energy $V(\theta) = -mgl \cos \theta$ is bounded by V < mgl. This, in turn, means that if E > mgl then the kinetic energy can never be zero. In this case, the pendulum swings all the way around, making complete circles. In contrast, if E < mgl then the pendulum completes only part of the circle before it comes to a stop and swings back the other way. If the highest point of the swing is $\theta_{0}$ , then the energy is 

$$
E = - m g l \cos \theta_ {0}.\tag{2.31}
$$

We can determine the period $T$ of the pendulum in a similar way to our derivation of (2.16). It's actually best to calculate the period by first figuring out the time the pendulum takes to go from $\theta = 0$ to $\theta = \theta_0$ , and then multiplying by four. We have 

$$
\begin{array}{c} T = 4 \int_ {0} ^ {T / 4} d t = 4 \int_ {0} ^ {\theta_ {0}} \frac {d \theta}{\sqrt {2 E / m l ^ {2} + (2 g / l) \cos \theta}} \\ = 4 \sqrt {\frac {l}{g}} \int_ {0} ^ {\theta_ {0}} \frac {d \theta}{\sqrt {2 \cos \theta - 2 \cos \theta_ {0}}}. \end{array}\tag{2.32}
$$

We see that the period is proportional to $\sqrt{l/g}$ multiplied by some dimensionless number given by (4 times) the integral. 

As an aside: the integral looks rather fierce. It's certainly true that it cannot be expressed in terms of elementary functions. Nonetheless, the integral has many nice properties and is an example of an elliptic integral. The study of integrals of this kind resulted in beautiful connections to geometry, through the theory of elliptic functions and elliptic curves. 

Things are much simpler when $\theta_{0} \ll 1$ , so the pendulum swings only slightly. For small $\theta \ll 1$ we can approximate $\sin \theta \approx \theta$ and the equation of motion (2.29) becomes the equation for a harmonic oscillator with frequency $\omega = \sqrt{g/l}$ . We can also look at the period of the pendulum. 

For $\theta \ll 1$ , we can replace each instance of $\cos \theta$ in the daunting integral (2.32) by its Taylor expansion $\cos \theta \approx 1 - \frac{1}{2}\theta^2$ . Then (2.32) becomes 

$$
T = 4 \sqrt {\frac {l}{g}} \int_ {0} ^ {\theta_ {0}} \frac {d \theta}{\sqrt {\theta_ {0} ^ {2} - \theta^ {2}}} = 4 \sqrt {\frac {l}{g}} \int_ {0} ^ {1} \frac {d s}{\sqrt {1 - s ^ {2}}} = 2 \pi \sqrt {\frac {l}{g}}
$$

where we've made the substitution $s = \theta / \theta_0$ . This agrees with our result (2.14) for the harmonic oscillator. 

We'll explore the idea that everything looks like a harmonic oscillator further in Chapter 8, where we'll see that more complicated systems can be described by many coupled harmonic oscillators. 

## 2.2 Potentials in Three Dimensions

Let's now consider a particle moving in three dimensional space $\mathbb{R}^3$ . Here things are more interesting. First, it is possible to have energy conservation even if the force depends on the velocity. We will see how this can happen in Section 2.4. Conversely, forces that depend only on the position do not necessarily conserve energy: we need an extra condition. We start by explaining this extra condition. 

## 2.2.1 Conservative Forces

For now, we restrict attention to forces of the form $\mathbf{F} = \mathbf{F}(\mathbf{x})$ . We will prove the following important result: 

Claim: There exists a conserved energy if the force $\mathbf{F}(\mathbf{x})$ can be written in the form 

$$
\mathbf {F} = - \nabla V\tag{2.34}
$$

for some potential energy function $V(\mathbf{x})$ . This means that the components of the force must be of the form $F_{i} = -\partial V / \partial x^{i}$ . A force that takes this form is said to be conservative. The conserved energy is then given by 

$$
E = \frac {1}{2} m \dot {\mathbf {x}} \cdot \dot {\mathbf {x}} + V (\mathbf {x}).\tag{2.35}
$$

Proof: Just as in the one-dimensional case, we differentiate the energy E with respect to time. With liberal use of the chain rule, we have 

$$
\frac {d E}{d t} = m \dot {\mathbf {x}} \cdot \ddot {\mathbf {x}} + \frac {\partial V}{\partial x ^ {i}} \frac {\partial x ^ {i}}{\partial t} = \dot {\mathbf {x}} \cdot (m \ddot {\mathbf {x}} + \nabla V)\tag{2.36}
$$

where we are invoking the summation convention, meaning that we sum over repeated indices i = 1, 2, 3. If the force is $F = -\nabla V$ , then the equation of motion is $m\ddot{x} = -\nabla V$ and we have $\dot{E} = 0$ . 

There is a converse to this statement. If there is a conserved energy of the form (2.35), so that $\dot{E}=0$ for all trajectories obeying the equation of motion, then, from (2.36), we must have $\dot{\mathbf{x}}\cdot(m\ddot{\mathbf{x}}+\nabla V)=0$ . We conclude that the force must take the form $F=-\nabla V+F_{0}$ where $F_{0}\cdot\dot{x}=0$ . For a force that depends only on position, so $\mathbf{F}=\mathbf{F}(\mathbf{x})$ , the only option is $F=-\nabla V$ . But we will see shortly that we can have interesting $F_{0}$ when the force depends on the velocity. 

## 2.2.2 Work Done

There is another way to illustrate why the conserved energy takes the particular form (2.35). This involves the concept of work, sometimes called work done. If a force F acts on a particle and succeeds in moving it from $\mathbf{x}(t_{1})$ to $\mathbf{x}(t_{2})$ along a trajectory C, then the work done by the force is defined to be 

$$
W = \int_ {C} \mathbf {F} \cdot d \mathbf {x}.\tag{2.37}
$$

This is a line integral. (If you're unfamiliar with line integrals, you can find a refresher course in the Appendices of the book on Electromagnetism.) The scalar product means that we take the component of the force along the direction of the trajectory at each point. We can make this clearer by writing 

$$
W = \int_ {t _ {1}} ^ {t _ {2}} \mathbf {F} \cdot \frac {d \mathbf {x}}{d t} d t.\tag{2.38}
$$

The integrand, which is the rate of doing work, is called the power $P = \mathbf{F} \cdot \dot{\mathbf{x}}$ . Using Newton's second law, we can replace $\mathbf{F} = m\ddot{\mathbf{x}}$ to get 

$$
W = m \int_ {t _ {1}} ^ {t _ {2}} \ddot {\mathbf {x}} \cdot \dot {\mathbf {x}} d t = \frac {1}{2} m \int_ {t _ {1}} ^ {t _ {2}} \frac {d}{d t} (\dot {\mathbf {x}} \cdot \dot {\mathbf {x}}) d t = T (t _ {2}) - T (t _ {1})
$$

where 

$$
T = \frac {1}{2} m \dot {\mathbf {x}} \cdot \dot {\mathbf {x}}\tag{2.40}
$$

is the kinetic energy. (You might think that $K$ is a better variable for kinetic energy. I'm inclined to agree. But $T$ was introduced by Lagrange in 1788 for the quantity that we now call kinetic energy but he called, confusingly, “travail”, and has stuck ever since.) 

So the total work done is equal to the change in kinetic energy. If we want to have a conserved energy, then the change in kinetic energy must be equal to some compensating change in potential energy. This is true if the work done depends only on the end points, $\mathbf{x}(t_{1})$ and $\mathbf{x}(t_{2})$ , meaning that there is some function $V(\mathbf{x})$ so that the work done can be written as 

$$
W = \int_ {C} \mathbf {F} \cdot d \mathbf {x} = V (\mathbf {x} (t _ {1})) - V (\mathbf {x} (t _ {2})).\tag{2.41}
$$

Then, comparing $(2.39)$ and $(2.41)$ , we see that the combination $E = T + V$ is the same at times $t_{1}$ and $t_{2}$ . This, of course, is the statement that the energy $(2.35)$ is conserved. 

This argument prompts the question: under what circumstances does the line integral W depend only on the end points, and is independent of the particular trajectory C? This is answered by a simple result from vector calculus which we prove in Appendix 2.6.1: this result says that $(2.41)$ holds only for conservative forces $\mathbf{F}(\mathbf{x})$ of the form 

$$
\mathbf {F} = - \nabla V.\tag{2.42}
$$

This gives another way of seeing why only conservative forces have a conserved energy. 

## When is a Force Conservative?

Given a force $\mathbf{F}$ , how can we tell if there's a corresponding potential so that we can write $\mathbf{F} = -\nabla V$ ? There's one straightforward way to check: for a conservative force, the components are given by 

$$
F _ {i} = - \frac {\partial V}{\partial x ^ {i}}, \quad i = 1, 2, 3.\tag{2.43}
$$

Differentiating again, we have 

$$
\frac {\partial F _ {i}}{\partial x ^ {j}} = - \frac {\partial^ {2} V}{\partial x ^ {i} x ^ {j}} = \frac {\partial F _ {j}}{\partial x ^ {i}}\tag{2.44}
$$

where the second equality follows from the fact that the order of partial derivatives doesn't matter (at least for suitably well-behaved functions). This means that a necessary condition for $\mathbf{F}$ to be conservative is that $\partial F_j / \partial x^i = \partial F_i / \partial x^j$ . It turns out that this is actually a sufficient condition. Another, more direct, way to say this is that forces that are defined everywhere in $\mathbb{R}^3$ satisfy 

$$
\mathbf {F} = - \nabla V \quad \Longleftrightarrow \quad \nabla \times \mathbf {F} = 0.\tag{2.45}
$$

The implication from left to right is straightforward to prove. The implication from right to left follows from Stokes' theorem, which states that 

$$
\int_ {S} \nabla \times \mathbf {F} \cdot d \mathbf {S} = \oint_ {C} \mathbf {F} \cdot d \mathbf {x}\tag{2.46}
$$

for any surface S bounded by a closed curve C. So if $\nabla \times F = 0$ , then $\oint_{C} F \cdot dx = 0$ for all closed curves C. But the result that we prove in Appendix 2.6.1 shows that whenever $\oint_{C} F \cdot dx = 0$ for all curves C, then the force F is conservative. (This web of different vector calculus results is described in detail in the Appendices of Volume 2 on Electromagnetism.) 

## 2.2.3 Central Forces and Angular Momentum Conservation

A particularly important class of potentials are those which depend only on the distance to a fixed point, which we take to be the origin 

$$
V (\mathbf {x}) = V (r)
$$

where $r = |x|$ . These are known as central potentials and the resulting force $F = -\nabla V$ as a central force. 

As we now explain, the key feature of central forces is that they have an additional conserved quantity, known as angular momentum. This is defined to be 

$$
\mathbf {L} = m \mathbf {x} \times \dot {\mathbf {x}}.\tag{2.47}
$$

Notice that, in contrast to the momentum $p = m \dot{x}$ , the angular momentum L depends on the choice of origin. By construction, L is perpendicular to both the position and the momentum. 

Let's first look at what happens to angular momentum in the presence of a general force $\mathbf{F}$ . When we take the time derivative of $\mathbf{L}$ , we get two terms. But one of these contains $\dot{\mathbf{x}} \times \dot{\mathbf{x}} = 0$ . We're left with 

$$
\frac {d \mathbf {L}}{d t} = m \mathbf {x} \times \ddot {\mathbf {x}} = \mathbf {x} \times \mathbf {F}.\tag{2.48}
$$

The quantity $\pmb{\tau} = \mathbf{x} \times \mathbf{F}$ is called the torque. This gives us an equation for the change of angular momentum that is very similar to Newton's second law for the change of momentum 

$$
\frac {d \mathbf {L}}{d t} = \boldsymbol {\tau}.\tag{2.49}
$$

At this point we restrict to central forces, so the force takes the form $F = -\nabla V$ with $V(\mathbf{x}) = V(r)$ . We have the following result: 

Claim: For a central potential, with $V(\mathbf{x}) = V(r)$ , the gradient $\nabla V$ is always parallel to the position x. 

Proof: This follows from a straightforward application of the chain rule. If we write $\mathbf{x} = (x, y, z)$ , then we have 

$$
\nabla V = \left(\frac {\partial V}{\partial x}, \frac {\partial V}{\partial y}, \frac {\partial V}{\partial z}\right) = \left(\frac {d V}{d r} \frac {\partial r}{\partial x}, \frac {d V}{d r} \frac {\partial r}{\partial y}, \frac {d V}{d r} \frac {\partial r}{\partial z}\right).
$$

The radial distance to the origin is $r^{2} = x^{2} + y^{2} + z^{2}$ , from which we can compute $\partial r/\partial x = x/r$ and similar for y and z. Then (2.50) becomes 

$$
\nabla V = \frac {d V}{d r} \left(\frac {x}{r}, \frac {y}{r}, \frac {z}{r}\right) = \frac {d V}{d r} \hat {\mathbf {r}}\tag{2.51}
$$

with $\hat{r}$ the unit radial vector $\hat{r} = x/r$ . (In this book we will use $\hat{r}$ for this unit vector. Elsewhere, you might see this same vector denoted as $\hat{x}$ or as $e_{r}$ .) ☐ 

Now we can see why central forces conserve angular momentum. When the force F points in the same direction as the position x of the particle, we have $x \times F = 0$ . This means that the torque vanishes and angular momentum is conserved: 

$$
\frac {d \mathbf {L}}{d t} = 0.\tag{2.52}
$$

This simple equation will prove crucial in Chapter 5 when we come to solve for the motion in central forces. 

## 2.3 Gravity

To the best of our knowledge, there are four fundamental forces in nature. They are: 

- Gravity 

- Electromagnetism 

• Strong Nuclear Force 

- Weak Nuclear Force 

The two nuclear forces operate only on small scales, comparable, as the name suggests, to the size of the nucleus ( $r_0 \approx 10^{-15} \mathrm{~m}$ ). We can't really give an honest description of these forces without invoking quantum mechanics and, for this reason, we won't discuss them in this book. For what it's worth, a very rough, and slightly dishonest, classical description of the strong nuclear force can be given by the so-called Yukawa potential $V(r) \sim -\frac{1}{r} e^{-r / r_0}$ . 

In this section we discuss the force of gravity; in the next, electromagnetism. I should warn you that each will be covered in something of a whirlwind tour, giving just the barest of essentials that we need to tell our story. Each of these forces has a subsequent volume in the series devoted to them. 

Ultimately, gravity is a force that acts between any two particles. But for now we are limiting our ambitions and discussing the motion of just a single particle. (We'll describe the dynamics of multiple particles in general in Chapter 4, and of two particles moving under their mutual gravitational attraction in particular in Chapter 5.) To this end, we will consider one heavy particle with mass M sitting fixed at the origin, and the motion of a second, lighter particle with mass m moving under its gravitational influence. 

For example, you could consider the fixed mass M to be the Sun, and the lighter particle to be the orbiting Earth. Or, on a different scale, you could consider the fixed mass M to be the Earth, and the lighter particle to be a falling cat. In this context, the lighter particle is sometimes called a test particle, which reflects the fact that, while it moves under the effect of gravity, we are ignoring the gravitational force that it may impart on anything else. 

Gravity is a conservative force, which means that that force can be described in terms of a potential energy. The test particle of mass m and position x, moving in the presence of a fixed particle of mass M, will experience a potential energy 

$$
V (r) = - \frac {G M m}{r}\tag{2.53}
$$

with $r = |\mathbf{x}|$ . Here $G$ is Newton's constant, a fundamental constant of nature. It determines the strength of the gravitational force and takes the value 

$$
G \approx 6. 6 7 \times 1 0 ^ {- 1 1} \mathrm{m} ^ {3} \mathrm{kg} ^ {- 1} \mathrm{s} ^ {- 2}.\tag{2.54}
$$

From the potential $(2.53)$ , we can calculate the force on the test particle: it is 

$$
\mathbf {F} (\mathbf {x}) = - \nabla V = - \frac {G M m}{r ^ {2}} \hat {\mathbf {r}}\tag{2.55}
$$

where $\hat{r} = x/r$ is the unit vector in the radial direction. This is Newton's famous inverse-square law for gravity. The minus sign means that force points towards the origin and is telling us that gravity is an attractive force. We will devote Chapter 5 to studying the motion of a particle subject to the inverse-square force. 

## 2.3.1 The Gravitational Field

Our real interest in this book is in solving for the trajectories of particles $\mathbf{x}(t)$ subject to some force $\mathbf{F}$ . Here we're going to briefly put that goal on hold while we look a little more closely at the gravitational forces $\mathbf{F}(\mathbf{x})$ that arise from some simple distributions of masses. To do this, we need to take a quick dive into the world of gravitational fields. 

The potential $(2.53)$ contains two masses: one mass M is the fixed particle that gives rise to the gravitational force, and the other mass m is the test particle that moves in the background. Because these different masses are playing somewhat different roles, it's useful to rewrite things in a way that separates the properties of the test particle from the other, much larger mass. We do this by first writing the force on the test particle as 

$$
\mathbf {F} (\mathbf {x}) = m \mathbf {g} (\mathbf {x})\tag{2.56}
$$

where $\mathbf{g}(\mathbf{x})$ is the gravitational field. We then interpret Newton's force law as telling us that a particle of mass $M$ sets up a gravitational field 

$$
\mathbf {g} (\mathbf {x}) = - \frac {G M}{r ^ {2}} \hat {\mathbf {r}}.\tag{2.57}
$$

We also define the gravitational potential $\Phi(\mathbf{x})$ due to a particle of mass M sitting at the origin to be 

$$
\Phi (\mathbf {x}) = - \frac {G M}{r}.\tag{2.58}
$$

The function $\Phi(\mathbf{x})$ is sometimes called the Newtonian gravitational potential to distinguish it from a more sophisticated object later introduced by Einstein. Evidently, the gravitational field and gravitational potential are both functions of the larger mass M only and are related by $g = -\nabla\Phi$ . The potential energy (2.53) of the test mass m, moving in the presence of the fixed mass M, is then given by $V = m\Phi$ . 

One advantage of talking about the gravitational potential $\Phi$ is that there is a natural generalisation to the situation where the test particle moves among many fixed masses. In this case, the gravitational potential is just the sum over all different masses. So if we fix particles with masses $M_{a}$ at positions $X_{a}$ , then the total gravitational field at some other point x is given by 

$$
\Phi (\mathbf {x}) = - G \sum_ {a} \frac {M _ {a}}{| \mathbf {x} - \mathbf {X} _ {a} |}.\tag{2.59}
$$

There is an obvious generalisation of this formula to the situation where we have a continuous mass distribution, with density $\rho(\mathbf{x})$ . In this case, the gravitational potential is given by 

$$
\Phi (\mathbf {x}) = - G \int d ^ {3} x ^ {\prime} \frac {\rho (\mathbf {x} ^ {\prime})}{| \mathbf {x} - \mathbf {x} ^ {\prime} |}.\tag{2.60}
$$

In either case, a test particle of mass m moving among these different masses experiences the force $\mathbf{F}(\mathbf{x}) = -m \nabla \Phi(\mathbf{x})$ . So, for example, for point masses with gravitational potential (2.59), we have 

$$
\mathbf {F} (\mathbf {x}) = - G m \sum_ {a} \frac {M _ {a}}{| \mathbf {x} - \mathbf {X} _ {a} | ^ {3}} \left(\mathbf {x} - \mathbf {X} _ {a}\right).\tag{2.61}
$$

The fact that contributions to the Newtonian gravitational potential add in a simple linear fashion, as in (2.59), is an additional postulate in the Newtonian theory of gravity, sometimes known as the principle of superposition. It has the happy consequence that life is simple and we can solve the equations. (In a later book we will learn that this linear addition no longer holds in Einstein's theory of general relativity. This has the happy consequence that life is complicated and therefore more interesting.) 

## The Gravitational Field of a Planet

A particularly important application of the principle of superposition (2.59) arises when we consider the gravitational potential of a spherically symmetric object, such as a star or a planet. After all, in reality a planet is most definitely not a point-like mass. It has a fairly large spatial extent. It's natural to ask how this affects the gravitational field. 

The beautiful answer is that it doesn't affect the gravitational field at all, at least if you're sitting outside the planet. Or, more precisely, a spherical object of mass $M$ and radius $R$ has the same gravitational field at distance $r > R$ as a point mass $M$ sitting at the centre. 

There are, it turns out, two ways to derive this result. The first attacks the issue head on and is straightforward, if a little messy. The second is more elegant and uses Gauss' divergence theorem in a pretty way that won't be needed for the rest of this book, but will be crucial in later volumes. Here we give the messy approach. We relegate the more elegant method to Appendix 2.6.2. 

Let the planet (or star) have density $\rho(\mathbf{x})$ and radius R. 

The gravitational field is given by $(2.60)$ , integrated over all $|x'| < R$ , 

$$
\Phi (\mathbf {x}) = - G \int_ {| \mathbf {x} ^ {\prime} | \leq R} d ^ {3} x ^ {\prime} \frac {\rho (\mathbf {x} ^ {\prime})}{| \mathbf {x} - \mathbf {x} ^ {\prime} |}.\tag{2.62}
$$

We need not assume that the density $\rho(\mathbf{x}^{\prime})$ is constant, but we will assume that the density is spherically symmetric, so that $\rho(\mathbf{x}^{\prime}) = \rho(r^{\prime})$ where we denote $r' = |x'|$ . The total mass of the planet is then 

$$
M = \int d ^ {3} x ^ {\prime} \rho (\mathbf {x} ^ {\prime}) = 4 \pi \int_ {0} ^ {R} d r ^ {\prime} r ^ {2} \rho (r ^ {\prime}).\tag{2.63}
$$

The integral $(2.62)$ is best performed in spherical polar coordinates. The trick is pick the line $\theta = 0$ to be aligned with the direction of x as shown in the figure. Then $x \cdot x' = r r' \cos \theta$ where $r = |x|$ and $r' = |x'|$ . We can use this to write an expression for the denominator: 

$|\mathbf{x} - \mathbf{x}'|^2 = r^2 + r'^2 - 2rr'\cos \theta$ . The gravitational field then becomes 

$$
\begin{array}{r l} & {\Phi (\mathbf {x}) = - G \int_ {0} ^ {R} d r ^ {\prime} \int_ {0} ^ {\pi} d \theta \int_ {0} ^ {2 \pi} d \phi \frac {r ^ {\prime 2} \sin \theta \rho (r ^ {\prime})}{\sqrt {r ^ {2} + r ^ {\prime 2} - 2 r r ^ {\prime} \cos \theta}}} \\ & {\qquad = - 2 \pi G \int_ {0} ^ {R} d r ^ {\prime} \int_ {0} ^ {\pi} d \theta \frac {r ^ {\prime 2} \sin \theta \rho (r ^ {\prime})}{\sqrt {r ^ {2} + r ^ {\prime 2} - 2 r r ^ {\prime} \cos \theta}}} \\ & {\qquad = - 2 \pi G \int_ {0} ^ {R} d r ^ {\prime} \frac {r ^ {\prime} \rho (r ^ {\prime})}{r} \left[ \sqrt {r ^ {2} + r ^ {\prime 2} - 2 r r ^ {\prime} \cos \theta} \right] _ {\theta = 0} ^ {\theta = \pi}} \\ & {\qquad = - \frac {2 \pi G}{r} \int_ {0} ^ {R} d r ^ {\prime} \rho (r ^ {\prime}) r ^ {\prime} (| r + r ^ {\prime} | - | r - r ^ {\prime} |).} \end{array}
$$

We see that, as expected, for our spherically symmetric planet the gravitational potential depends only on the radial distance $\Phi = \Phi(r)$ . 

So far this calculation has been done for any x, whether inside or outside the planet. At this point, we restrict attention to points external to the 

planet. This means that $r > R$ and so $|r + r'| = r + r'$ and $|r - r'| = r - r'$ for all $r$ . We then have 

$$
\Phi (\mathbf {x}) = - \frac {4 \pi G}{r} \int_ {0} ^ {R} d r ^ {\prime} r ^ {\prime 2} \rho (r ^ {\prime}) = - \frac {G M}{r} \quad \text { for } \quad r > R .
$$

This is the result that we wanted to prove: the gravitational field is the same as that of a point mass M at the origin. A different perspective on this result can be found in Appendix 2.6.2. 

## 2.3.2 Escape Velocity

Let's now return to our main story: the motion of a test particle moving in a gravitational field. We ask the following basic question. Imagine that you're trapped near the surface of a planet of mass $M$ and radius $R$ . (This part should be easy.) What gravitational potential energy you feel? 

We know that the potential energy is given by $V = -GMm / r$ . First, assume that you can only rise a distance $z \ll R$ above the planet's surface, so we can Taylor expand the potential energy 

$$
V (R + z) = - \frac {G M m}{R + z} = - \frac {G M m}{R} \left(1 - \frac {z}{R} + \frac {z ^ {2}}{R ^ {2}} + \dots\right).
$$

If we're only interested in small distances $z \ll R$ , we need focus only on the second term, giving 

$$
V (z) \approx \mathrm{constant} + \frac {G M m}{R ^ {2}} z + \dots .\tag{2.67}
$$

This is the familiar potential energy that gives rise to constant acceleration. Comparing to $(2.6)$ , the gravitational acceleration at the surface is $g = GM/R^{2}$ . As we mentioned previously, for the Earth, $g \approx 9.8 \, m s^{-2}$ . 

Now let's be more ambitious. Suppose that we want to escape our parochial, planet-bound existence. So we decide to jump. How fast do we have to jump if we wish to truly be free? This, it turns out, is the same kind of question that we discussed in Section 2.1.1 in the context of particles moving in one dimension and can be determined very easily using the gravitational potential energy $V = -GMm / r$ . If you jump directly upwards (i.e. radially) with velocity $v$ , then your total energy as you leave the surface is 

$$
E = \frac {1}{2} m v ^ {2} - \frac {G M m}{R}.\tag{2.68}
$$

For any energy E < 0, you will eventually come to a halt at position $r = -GM m / E$ , before falling back. If you want to escape the gravitational attraction of the planet for ever, you will need energy $E \geq 0$ . At the minimum value of E = 0, the associated velocity is 

$$
v _ {\mathrm{escape}} = \sqrt {\frac {2 G M}{R}}.\tag{2.69}
$$

This is the escape velocity. 

We assumed above that you jump directly upwards. But, rather surprisingly, if you jump with speed $v_{escape}$ in any direction (as long as it's not into the Earth!) then you will escape the Earth's pull. At first glance, that seems odd, because it feels like the sideways component of the velocity should be somehow wasted in your attempt to get as high as possible. But that's intuition based on the flat Earth theory. To see that jumping at speed $v_{escape}$ is sufficient to escape, regardless of the direction, first note that if you have this speed then you have total energy E = 0. But in Chapter 5 we will show that all trajectories with E = 0 are parabolas, and all of them reach infinity. 

## Black Holes and the Schwarzschild Radius

We'll now do something a little dodgy. We take the formula above and apply it to light. The reason that this is dodgy is because, as we will see in Chapter 11, the laws of Newtonian physics need modifying for particles close to the speed of light where the effects of special relativity are important, and need modifying yet further when the masses involved become large. Nonetheless, let's ignore this for now and plough ahead regardless. 

Light travels at speed $c \approx 3 \times 10^{8} \, m s^{-1}$ . Suppose that the escape velocity from the surface of a star is greater than or equal to the speed of light. From (2.69), this would happen if the radius of a star of mass M satisfies 

$$
R \leq R _ {S} = \frac {2 G M}{c ^ {2}}.\tag{2.70}
$$

What do we see if this is the case? Well, nothing! The star is so dense that light can't escape from it. It's what we call a black hole. 

Although the derivation above is not trustworthy, by some fortunate coincidence it turns out that the answer is correct. The distance $R_{s} = 2GM/c^{2}$ is called the Schwarzschild radius. If a star is so dense that it lies within its own Schwarzschild radius, then it will form a black hole. We will see the correct derivation of this in the volume on General Relativity. 

For what it's worth, the Schwarzschild radius of the Earth is around 1 cm. The Schwarzschild radius of the Sun is about 3 km. You'll be pleased to hear that, because both objects are much larger than their Schwarzschild radii, neither is in danger of forming a black hole. 

## 2.3.3 Inertial vs Gravitational Mass

We have seen two formulae which involve mass, both due to Newton. These are the second law (1.5) and the inverse-square law for gravity (2.55). Yet the conceptual meaning of mass in these two equations is very different. The mass appearing in the second law represents the reluctance of a particle to accelerate under any force. In contrast, the mass appearing in the inverse-square law tells us the strength of a particular force, namely gravity. Since these are very different concepts, we should really distinguish between the two different masses. The second law involves the inertial mass, $m_{I}$ 

$$
m _ {I} \ddot {\mathbf {x}} = \mathbf {F}.\tag{2.71}
$$

Meanwhile Newton's law of gravity involves the gravitational mass, $m_G$ 

$$
\mathbf {F} = - \frac {G M _ {G} m _ {G}}{r ^ {2}} \hat {\mathbf {r}}.\tag{2.72}
$$

It is then an experimental fact that 

$$
m _ {I} = m _ {G}.\tag{2.73}
$$

Much experimental effort has gone into determining the accuracy of $(2.73)$ , most notably by the Hungarian physicist Eötvös at the turn of the (previous) century. It is, as far as we can tell, true, with our best experimental bounds showing that $m_{I}$ and $m_{G}$ are equal to each other to an accuracy of, at least, one part in $10^{13}$ . A theoretical understanding of the result $(2.73)$ came only with the development of the theory of general relativity. 

## 2.4 Electromagnetism

Throughout the universe, at each point in space, there exist two vectors, $\mathbf{E}(\mathbf{x})$ and $\mathbf{B}(\mathbf{x})$ . These are known as the electric and magnetic fields. Both the magnitude and the direction of these vectors can vary from point to point. Their role – at least for the purposes of this book – is to guide any particle that carries electric charge. 

The force experienced by a particle with electric charge q is called the Lorentz force and is given by 

$$
\mathbf {F} (\mathbf {x}) = q \left(\mathbf {E} (\mathbf {x}) + \dot {\mathbf {x}} \times \mathbf {B} (\mathbf {x})\right).\tag{2.74}
$$

The electric force $qE$ is parallel to the electric field. By convention, particles with positive charge q are accelerated in the direction of the electric field, while those with negative charge are accelerated in the opposite direction. Due to a quirk of history, the electron is taken to have a negative charge, usually denoted as $q_{electron} = -e$ , with value 

$$
e \approx 1. 6 \times 1 0 ^ {- 1 9} \mathrm{C}\tag{2.75}
$$

where C is the unit of coulombs. As far as fundamental physics is concerned, a much better choice is to simply say that the electron has charge -1. All other charges can then be measured relative to this. 

The magnetic force looks rather different. It is a velocity dependent force, with magnitude proportional to the speed of the particle, but with direction perpendicular to the motion of the particle. We will see its effect in simple situations shortly. 

## Motion in a Constant Electric Field

As a particularly simple example, we can turn off the magnetic field so $\mathbf{B} = 0$ , and consider a constant electric field $\mathbf{E} = (0,0,\mathcal{E})$ . (The calligraphic $\mathcal{E}$ is to avoid confusion with the energy.) Writing the position of the particle as $\mathbf{x} = (x,y,z)$ , the Lorentz force law tells us that the velocity in the $x$ -direction and $y$ -direction is constant and unaffected by the electric field, while the particle undergoes constant acceleration in the $z$ -direction 

$$
z = z _ {0} + u t + \frac {q \mathcal {E}}{2 m} t ^ {2}\tag{2.76}
$$

with $z_{0}$ and u integration constants. This is the same behaviour that we saw in a constant gravitational field in (2.9). 

## Energy Conservation with both E and B

In principle, both E and B can change in time. However, here we will consider only situations where they are time independent. In this case it turns out that the electric field can always be written in the form 

$$
\mathbf {E} = - \nabla \phi\tag{2.77}
$$

for some function $\phi (\mathbf{x})$ called the electric potential, or scalar potential, or even just the potential as if we didn't already have enough things with that name. There is deep significance to the fact that $\mathbf{E}$ can be written in the form (2.77) and this will be explained in Volume 2 on Electromagnetism. 

For time-independent electric and magnetic fields, something special happens: energy is conserved. The conserved energy is 

$$
E = \frac {1}{2} m \dot {\mathbf {x}} \cdot \dot {\mathbf {x}} + q \phi (\mathbf {x}).\tag{2.78}
$$

The fact that the energy includes the electric potential $q\phi$ follows immediately from the definitions above. The novelty is that the energy is conserved even when $B \neq 0$ . The energy simply does not depend on the magnetic field. This gives us an example of something we previously promised: a velocity-dependent force with a conserved energy. 

To show the conservation of energy, we just need to take the time derivative 

$$
\dot {E} = m \dot {\mathbf {x}} \cdot \ddot {\mathbf {x}} + q \nabla \phi \cdot \dot {\mathbf {x}} = \dot {\mathbf {x}} \cdot (\mathbf {F} + q \nabla \phi) = q \dot {\mathbf {x}} \cdot (\dot {\mathbf {x}} \times \mathbf {B}) = 0
$$

where, in the penultimate equality, we used $(2.74)$ . The only novel step is the final equality, which follows because $\dot{x} \times B$ is necessarily perpendicular to $\dot{x}$ . This is key: the velocity-dependent part of the Lorentz force is perpendicular to the trajectory of the particle. This 

ensures that that the magnetic force does no work and that's why energy is conserved. 

## 2.4.1 Motion in a Constant Magnetic Field

If there is only a magnetic field, and no electric field, then the equation of motion from the Lorentz force law $(2.74)$ becomes 

$$
m \ddot {\mathbf {x}} = q \dot {\mathbf {x}} \times \mathbf {B}.\tag{2.80}
$$

To get a feel for the effect of the magnetic field, we will now solve this equation for a constant B, oriented in the z-direction so 

$$
\mathbf {B} = (0, 0, B) .\tag{2.81}
$$

In Cartesian coordinates, $\mathbf{x} = (x, y, z)$ , the Lorentz force law (2.80) reads 

$$
m \ddot {x} = q B \dot {y},\tag{2.82}
$$

$$
m \ddot {y} = - q B \dot {x},\tag{2.83}
$$

$$
m \ddot {z} = 0.\tag{2.84}
$$

The last equation is easily solved and tells us that the particle just travels at constant velocity in the z-direction, parallel to B. 

The first two equations (2.82) and (2.83) are more interesting and there are a number of ways to solve them. At the risk of overkill, here we present four different approaches to solving them. We'll see variations of each of these methods as we solve other problems later. 

## Method 1: Eliminate a Variable

We have two equations $(2.82)$ and $(2.83)$ for two variables, $x(t)$ and $y(t)$ . We can reduce this to a single equation for a single variable by differentiating again. This gives 

$$
m \dddot {x} = q B \ddot {y} = - \frac {q ^ {2} B ^ {2}}{m} \dot {x}.\tag{2.85}
$$

This is now a differential equation just for x, albeit with the unfamiliar third derivative $\ddot{x}$ . However, we could alternatively consider it to be a second order equation for the velocity in the x-direction, $u = \dot{x}$ , which obeys 

$$
\ddot {u} = - \omega^ {2} u \quad \mathrm{with} \quad \omega = \frac {q B}{m}.\tag{2.86}
$$

This is very familiar: it is just the equation for the harmonic oscillator, but with the variable u. We can solve it by 

$$
u = \alpha \cos (\omega t) + \beta \sin (\omega t)\tag{2.87}
$$

with $\alpha$ and $\beta$ integration constants. We can now trivially integrate up one more time to get 

$$
x = x _ {0} + \frac {\alpha}{\omega} \sin (\omega t) - \frac {\beta}{\omega} \cos (\omega t)\tag{2.88}
$$

where we've introduced one further integration constant, $x_0$ . Having solved for the motion in the $x$ -direction, it's straightforward to do the same in the $y$ -direction. We just use the equation (2.82) which reads 

$$
\begin{array}{r l} & {\dot {y} = \frac {m}{q B} \ddot {x} = - \alpha \sin (\omega t) + \beta \cos (\omega t)} \\ {\Longrightarrow} & {y = y _ {0} + \frac {\alpha}{\omega} \cos (\omega t) + \frac {\beta}{\omega} \sin (\omega t)} \end{array}\tag{2.89}
$$

where $y_0$ is now our integration constant. Note that we've ended up with four integration constants, $x_0, y_0, \alpha$ and $\beta$ , as expected, as we started from two second order differential equations. 

Equations $(2.88)$ and $(2.89)$ are our final results. It only remains to interpret them. 

The geometrical meaning becomes clear if we look at 

$$
(x - x _ {0}) ^ {2} + (y - y _ {0}) ^ {2} = \frac {\alpha^ {2} + \beta^ {2}}{\omega^ {2}}.\tag{2.90}
$$

This is telling us that the projection of the particle's motion onto the $(x, y)$ -plane, perpendicular to B, traces out a circle. The radius of the circle, $R^{2} = (\alpha^{2} + \beta^{2})/\omega^{2}$ , is set by our choice of integration constants. The time the particle takes to undergo a full circle is fixed, with period 

$$
T = \frac {2 \pi}{\omega} \quad \mathrm{with} \quad \omega = \frac {q B}{m}.\tag{2.91}
$$

Here the frequency $\omega$ is known as the cyclotron frequency. The slight surprise is that this period does not depend on the size of the circle. All particles come back to their starting point at the same time, regardless of whether they trace out very big circles or very small circles. Those that move in bigger circles just go faster. 

We can fix the various integration constants in $(2.88)$ and $(2.89)$ if we are given suitable initial conditions. Suppose, for example, that the particle starts life at t = 0 at the origin with velocity $(\dot{\mathbf{x}}, \dot{\mathbf{y}}) = (0, -v)$ . Then we have $\alpha = 0$ and $\beta = -v$ , so 

$$
x = \frac {v}{\omega} \Big (\cos (\omega t) - 1 \Big) \mathrm{and} y = - \frac {v}{\omega} \sin (\omega t).\tag{2.92}
$$

This shows explicitly that the radius of the circle, $R = v/\omega$ , is proportional to the speed v at which the particle moves, ensuring that the period T is the fixed constant (2.91). 

## Method 2: Complex Variables

Our second method is slightly more elegant: we work with the complex variable on the plane, $\xi = x + iy$ . Then adding (2.82) to i times (2.83) gives 

$$
m \ddot {\xi} = - i q B \dot {\xi}\tag{2.93}
$$

which can be integrated immediately to find 

$$
\xi = \gamma e ^ {- i \omega t} + \xi_ {0}.\tag{2.94}
$$

Here $\gamma$ and $\xi_0$ are complex integration constants and $\omega$ is the cyclotron frequency. This is our previous result (2.88) and (2.89), written in complex coordinates. Clearly we had less work to do. Arguably, it's also more straightforward to see that the particle moves in a circle, since we have immediately $|\xi - \xi_0| = |\gamma|$ which is the equation for a circle of radius $|\gamma|$ in the complex $\xi$ -plane. 

## Method 3: Manipulating Vector Equations

Next, we will show how to solve the vector differential equation without resorting to components. Our starting point is the Lorentz force law (2.80), 

$$
m \ddot {\mathbf {x}} = q \dot {\mathbf {x}} \times \mathbf {B}.\tag{2.95}
$$

To begin, we take the dot product with B. Since the right-hand side vanishes, we're left with 

$$
\ddot {\mathbf {x}} \cdot \mathbf {B} = 0.\tag{2.96}
$$

This tells us that the particle travels with constant velocity in the direction of $\mathbf{B}$ . This is simply a rewriting of our previous result $\ddot{z} = 0$ . For simplicity, let's just assume that the particle doesn't move in the $\mathbf{B}$ direction, remaining at $z = 0$ . The particle then moves in a plane with equation 

$$
\mathbf {x} \cdot \mathbf {B} = 0.\tag{2.97}
$$

However, we're not yet done. We started with (2.95) which was three equations. Taking the dot product with B reduced this to a single equation, so there must be two further equations still lurking in (2.95) that we haven't yet taken into account. To find them, the systematic thing to do would be to take the cross product with B. However, in the present case, it turns out that the simplest way forwards is to simply integrate (2.95) once, to get 

$$
m \dot {\mathbf {x}} = q \mathbf {x} \times \mathbf {B} + \mathbf {c}\tag{2.98}
$$

with c a vector constant of integration. We can now substitute this back into the right-hand side of $(2.95)$ to find 

$$
\begin{array}{r l} m ^ {2} \ddot {\mathbf {x}} & = \mathbf {d} + q ^ {2} (\mathbf {x} \times \mathbf {B}) \times \mathbf {B} \\ & = \mathbf {d} + q ^ {2} ((\mathbf {x} \cdot \mathbf {B}) \mathbf {B} - (\mathbf {B} \cdot \mathbf {B}) \mathbf {x}) \\ & = - q ^ {2} B ^ {2} (\mathbf {x} - \mathbf {d} / q ^ {2} B ^ {2}) \end{array}\tag{2.99}
$$

where the integration constant now sits in $\mathbf{d} = q\mathbf{c}\times \mathbf{B}$ which, by construction, is perpendicular to $\mathbf{B}$ . In the last line, we've used the equation (2.97). (Had we considered a situation in which the particle was moving with constant velocity in the $\mathbf{B}$ direction, then we would have to work a little harder at this point.) The resulting vector equation looks like three harmonic oscillators, displaced by the vector $\mathbf{d} / q^2 B^2$ , oscillating with frequency $\omega = qB / m$ . However, because of the constraint (2.97), the motion is necessarily only in the two directions perpendicular to $\mathbf{B}$ . The end result is 

$$
\mathbf {x} = \frac {\mathbf {d}}{q ^ {2} B ^ {2}} + \boldsymbol {\alpha} _ {1} \cos \omega t + \boldsymbol {\alpha} _ {2} \sin \omega t\tag{2.100}
$$

with $\alpha_{i}, i = 1, 2$ integration constants satisfying $\alpha_{i} \cdot B = 0$ . At first sight, it looks like we have too many integration constants. But we need to substitute this equation back into the Lorentz force law to find a relation between the integration constants $\alpha_{2} = \alpha_{1} \times \hat{B}$ . This coincides with the result (2.88) and (2.89) (or, equivalently, (2.94)) that we found previously. 

Admittedly, in this particular example, manipulating the vector equations was somewhat more cumbersome than working directly with components. But this won't always be the case and, for some problems, 

we'll make more progress by playing the kind of vector manipulation games that we've described above. 

## Method 4: Energy Conservation

Because this is such a simple system, there's a simple way to solve it. This is energy conservation. First note that the two equations of motion (2.82) and (2.83) immediately imply that $\dot{x}^{2} + \dot{y}^{2}$ is a conserved quantity. So we can write 

$$
(\dot {x} (t), \dot {y} (t)) = v (\cos \varphi (t), \sin \varphi (t)).\tag{2.101}
$$

with v a constant. This reduces the problem of motion in the $(x, y)$ -plane to a single variable. Plugging this into $(2.82)$ gives $\dot{\varphi} = -\omega$ , and so $\varphi(t) = \varphi_{0} - \omega t$ . Integrating $\dot{x}$ and $\dot{y}$ then gives us $x(t)$ and $y(t)$ . 

## 2.4.2 The Electric Field of a Point Charge

Charged objects do not only respond to electric fields; they also produce electric fields. This is where the fun of electromagnetism comes in. It's also the part that we're mostly going to sweep under the carpet for now and deal with in Volume 2 of this series. Here, we just give the bare bones. 

Consider a particle of charge Q, fixed at the origin. This gives rise to an electric field 

$$
\mathbf {E} (\mathbf {x}) = \frac {Q}{4 \pi \epsilon_ {0}} \frac {\hat {\mathbf {r}}}{r ^ {2}}\tag{2.102}
$$

with $r = |x|$ and $\hat{r} = x/r$ . The quantity $\epsilon_{0}$ has the grand name permittivity of free space. It is a constant of nature that determines the strength of the electrostatic force between two particles. It takes the value 

$$
\epsilon_ {0} \approx 8. 8 5 \times 1 0 ^ {- 1 2} \mathrm{m} ^ {- 3} \mathrm{kg} ^ {- 1} s ^ {2} \mathrm{C} ^ {2}.\tag{2.103}
$$

The corresponding electric potential, $\phi(\mathbf{r})$ , such that $E = -\nabla\phi$ , takes the form 

$$
\phi (\mathbf {r}) = \frac {Q}{4 \pi \epsilon_ {0} r}.\tag{2.104}
$$

Now consider a second particle, with charge q, moving in the presence of the first. We will treat this second particle as a test particle, meaning that we ignore the force that it imparts on other things and focus only on its motion. The Lorentz force law $(2.74)$ says that it experiences an inverse-square force 

$$
\mathbf {F} (\mathbf {x}) = \frac {q Q}{4 \pi \epsilon_ {0} r ^ {2}} \hat {\mathbf {r}}.\tag{2.105}
$$

This is the Coulomb force. 

Most likely it will not have escaped your attention that the mathematical form of Coulomb's law (2.105) is identical to Newton's gravitational force law (2.55). The property of the particle that we call mass gives rise to the force of gravity, while the property known as electric charge gives rise to the electrostatic force. Newton's constant $G$ is to gravity what $1/4\pi \epsilon_0$ is to electricity. (The extra factor of $4\pi$ reflects the fact that, in the century between Newton and Coulomb, people figured out where factors of $4\pi$ should sit in equations.) We will solve for the trajectories of two particles moving under the influence of this force in Chapter 5, with particular focus on the Coulomb force in Section 5.6. 

There is, however, one crucial difference between the forces of Newton and Coulomb: this is the overall minus sign in $(2.55)$ . Because masses are always positive, so M, m > 0, this tells us that gravity is always attractive. In contrast, electric charges Q and q come with both signs. The lack of an overall minus sign in $(2.105)$ tells us that charges of the same sign repel each other while, famously, opposites attract. 

It's natural to ask: why do the forces of gravity and electromagnetism look so similar? Certainly it's not true that there is any deep connection between gravity and the electrostatic force, at least not one that physicists have uncovered to date. In particular, when masses and charges start to move, both the forces described above are replaced by something more complicated – general relativity in the case of gravity, the full Maxwell equations in the case of the Coulomb force – and the equations of these theories are very different from each other. Yet, when we restrict to the simple, static set-up, the forces take the same form. 

In fact, there is a good explanation for why both forces have the inverse-square form, although it really requires quantum field theory. Roughly speaking, any force that is associated to a massless particle will have the $1/r^{2}$ form. And there are reasons why both the photon (the particle of electromagnetism) and the graviton (the particle of gravity) are massless. Those reasons, sadly, will have to wait. 

## Looking Forwards: The Maxwell's Equations

In the Lorentz force law $(2.74)$ , the only hint that the electric and magnetic fields are related is that they both affect a particle in a manner that is proportional to the electric charge q. 

However, it turns out that there is a much closer connection between electric and magnetic fields, one that only becomes apparent when they start to vary in time. A time-dependent electric field gives rise to a magnetic field and vice versa. The dynamics of the electric and magnetic fields are governed by a set of four, interwoven equations known as the Maxwell equations. In the absence of electric charges and currents, these equations are given by 

$$
\begin{array}{r l} \nabla \cdot \mathbf {E} = 0 & , \quad \nabla \cdot \mathbf {B} = 0 \\ \nabla \times \mathbf {E} = - \frac {\partial \mathbf {B}}{\partial t} & , \quad \nabla \times \mathbf {B} = \frac {1}{c ^ {2}} \frac {\partial \mathbf {E}}{\partial t} \end{array}\tag{2.106}
$$

with c the speed of light. We will have a great deal more to say about the Maxwell equations in Volume 2 on Electromagnetism. 

## 2.5 Friction

Friction is a messy, dirty business. While energy is always conserved on a fundamental level, it doesn't appear to be conserved in most things that you do every day. If you slide along the floor in your socks then you don't keep going for ever. At a microscopic level, your kinetic energy is transferred to the atoms in the floor where it manifests itself as heat. But if we only want to know how far our socks will slide, the details of all these atomic processes are of little interest. Instead, we try to summarise everything in a single, macroscopic force that we call friction. 

Because friction is a way of summarising some complicated, underlying process, there's no hard and fast rule that applies to all situations and, typically, no elegant mathematics underlying it. Instead, different friction forces are at play in different situations. Here we summarise the most important. 

## Dry Friction

Dry friction occurs when two solid objects are in contact. Think of a heavy box being pushed along the floor, or some idiot sliding in his socks. Experimentally, one finds that the complicated dynamics involved in friction is usually summarised by the force $F = \mu R$ where $R$ is the reaction force, normal to the floor, and $\mu$ is a constant called the coefficient of friction. Usually $\mu \approx 0.3$ , although it depends on the kind of materials that are in contact. In many cases, the coefficient $\mu$ is, more or less, independent of the velocity. We won't have much to say about dry friction in this book. In fact, we've already said it all. 

## Fluid Drag

Drag occurs when an object moves through a fluid, which is the name given to either a liquid or a gas. The resistive force is opposite to the direction of the velocity and, typically, falls into one of two categories: 

- Linear drag 

$$
\mathbf {F} = - \gamma \mathbf {v}\tag{2.107}
$$

where the coefficient of friction, $\gamma$ , is a constant and v is the velocity of the particle. We should take $\gamma > 0$ so that the drag force always opposes the direction of motion. This form of linear drag holds for objects moving slowly through very viscous fluids. 

There is a simple reason why the drag force is linear for slowly moving objects. In general, the friction will have terms that are linear in v and terms that are order $v^{2}$ , and so on. But when the velocity is very small, “ $v \gg v^{2}$ ” so the term linear in velocity dominates. (A warning: strictly the equation “ $v \gg v^{2}$ ” can never be correct on dimensional grounds! We give the dimensionally correct version below in $(2.109)$ .) 

There is an impressive formula due to Stokes which gives the drag force for a sphere of radius L, moving through a fluid with viscosity $\mu$ as $\gamma = 6\pi\mu L$ . This formula will be derived in Volume 4 on Fluid Mechanics. 

- Quadratic drag 

$$
\mathbf {F} = - \gamma | \mathbf {v} | \mathbf {v}.\tag{2.108}
$$

Again, $\gamma$ is called the coefficient of friction. Quadratic drag holds for fast-moving objects in less viscous fluids. This includes objects falling in air such as, for example, the various farmyard animals dropped by Galileo from the leaning tower. For quadratic friction, $\gamma$ is usually proportional to the surface area of the object, i.e. $\gamma \sim L^{2}$ for an object of size L. This is in contrast to the coefficient for linear friction where Stokes' formula gives $\gamma \sim L$ . 

Quadratic drag arises because the object is banging into molecules in the fluid, knocking them out the way. There is an intuitive way to see this. The force is proportional to the change of momentum that occurs in each collision. That gives one factor of v. But the force is also proportional to the number of collisions and there's more collisions when the particle moves faster. That gives the second factor of v, resulting in a force that scales as $v^{2}$ . These kind of kinetic theory arguments will also be described in more detail in Volume 4 on Fluid Mechanics. 

One can ask where the cross-over happens between linear and quadratic friction. As we mentioned above, the linear drag must always dominate at low velocities simply because, for any number x, we have $x \gg x^{2}$ whenever $x \ll 1$ . More quantitatively, the type of drag experienced by an object of size L is determined by a dimensionless number called the Reynolds number, 

$$
R e = \frac {\rho v L}{\mu}\tag{2.109}
$$

where $\rho$ is the density of the fluid while $\mu$ is the viscosity. For $Re \ll 1$ , linear drag dominates; for $Re \gg 1$ , quadratic friction dominates. 

## An Aside: What is Viscosity?

Above, we've mentioned the viscosity of the fluid, $\mu$ , without really defining it. For completeness, I will mention here how to measure viscosity. 

Place a fluid between two plates, a distance d apart. Keeping the lower plate still, move the top plate at a constant speed v. This sets up a velocity gradient in the fluid. But the fluid pushes back. To keep the upper plate moving at constant speed, you will have to push with a force per unit area which is proportional to the velocity gradient, 

$$
\frac {F}{A} = \mu \frac {v}{d}.\tag{2.110}
$$

The coefficient of proportionality, $\mu$ , is defined to be the (dynamic) viscosity. We will learn much more about the role that viscosity plays in Volume 4 on Fluid Mechanics. 

## Energy is Not Conserved With Friction

A general feature of systems with friction is that they do not conserve energy. Intuitively, this follows because friction tends to make the particle slow down, and ultimately grind to a halt. This behaviour is not compatible with a conserved energy and is referred to as dissipative. 

We can see this straightforwardly by considering the work done. For concreteness, consider the case with vanishing potential $V(\mathbf{x}) = 0$ but with linear drag, $F = -\gamma\dot{x}$ where $\gamma > 0$ . We can compute the expression for the work done, $W = \int F \cdot dX$ , and compare it to our general expression in terms of the change of kinetic energy (2.39). For a particle following some trajectory C from $\mathbf{x}(t_{1})$ to $\mathbf{x}(t_{2})$ , we have 

$$
W = T (t _ {2}) - T (t _ {1}) = - \gamma \int \dot {\mathbf {x}} \cdot \dot {\mathbf {x}} d t.\tag{2.111}
$$

The integral is positive definite, so that overall minus sign is telling us that $T(t_{2}) < T(t_{1})$ . In other words, the friction causes the particle to lose kinetic energy and slow down. Energy is not conserved. 

Of course, it is perhaps better to say that energy is not conserved in the equations that we’ve chosen to model friction. The conservation of energy is a fundamental law of physics, so what’s really happening is that the kinetic and potential energy is draining away into the motion of underlying atoms where it manifests itself as heat, and that’s not something that we take into account in Newtonian mechanics. Much of the volume on Statistical Physics will be devoted to gaining a better understanding of what’s really happening in situations involving heat. 

## 2.5.1 The Damped Harmonic Oscillator

We start with our favourite system: the harmonic oscillator, now with the addition of a linear drag term which, in this context, is known as damping. The equation of motion is 

$$
m \ddot {x} = - k x - \gamma \dot {x}.\tag{2.112}
$$

Divide through by m to get 

$$
\ddot {x} = - \omega_ {0} ^ {2} x - 2 \alpha \dot {x}\tag{2.113}
$$

where $\omega_{0}^{2}=k/m$ is the frequency of the undamped harmonic oscillator and $\alpha=\gamma/2m$ is our rescaled measure of the friction force. It will be important in what follows to note that the friction force necessarily has positive coefficient $\alpha>0$ . 

There is a useful trick for solving linear equations like 2.113: we pretend that the variable $x(t)$ is complex. Of course, $x(t)$ is decidedly real: it tells us the position of the particle. But because the equation (2.113) is linear, if we find a complex solution then we can always take real and imaginary parts and these too will be solutions. 

The advantage of working with complex solutions is that it captures oscillatory motion and decaying motion all in the same ansatz, namely 

$$
x = A e ^ {i \beta t}.\tag{2.114}
$$

The overall coefficient A will remain undetermined in a linear equation like $(2.113)$ , since each term will be proportional to A. Meanwhile, any solution with $\beta \in R$ will oscillate because, after taking real and imaginary parts, we get the solutions $x \sim \cos(\beta t)$ and $x \sim \sin(\beta t)$ . Conversely, any solution with $\beta$ purely imaginary will either decay or grow exponentially. 

To see how this works for the damped harmonic oscillator, we need only substitute the ansatz $(2.114)$ into the equation of motion $(2.113)$ . This gives a quadratic equation for $\beta$ , 

$$
\beta^ {2} - 2 i \alpha \beta - \omega_ {0} ^ {2} = 0.\tag{2.115}
$$

There are two solutions, 

$$
\beta = \beta_ {\pm} = i \alpha \pm \sqrt {\omega_ {0} ^ {2} - \alpha^ {2}}.\tag{2.116}
$$

The general solution is then of the form 

$$
x = A _ {+} e ^ {i \beta_ {+} t} + A _ {-} e ^ {i \beta_ {-} t}.\tag{2.117}
$$

with $A_{\pm}$ two integration constants. From this result, we identify three different regimes, 

- Underdamped: $\omega_0^2 > \alpha^2$ . Here the solution takes the form, 

$$
x = e ^ {- \alpha t} \left(A _ {+} e ^ {i \omega t} + A _ {-} e ^ {- i \omega t}\right)\tag{2.118}
$$

where $\omega = \sqrt{\omega_{0}^{2} - \alpha^{2}} \in R$ . We see that the friction has two effects: first, it decreases the frequency of oscillation, since $\omega < \omega_{0}$ . Second, and more importantly, the amplitude of the oscillations decays exponentially with time. This is the result advertised above: friction causes things to slow down. A graph of the motion is plotted on the left of Figure 2.2. 

- Overdamped: $\omega_0^2 < \alpha^2$ . Now the roots $\beta_{\pm}$ are purely imaginary and the general solution takes the form, 

$$
x = e ^ {- \alpha t} \left(A _ {+} e ^ {- \lambda t} + A _ {-} e ^ {+ \lambda t}\right)\tag{2.119}
$$

with $\lambda = \sqrt{\alpha^{2} - \omega_{0}^{2}} \in R$ . Now there is no oscillatory behaviour at all: it has been killed by the friction. Because $\alpha > \lambda$ , the overall $e^{-\alpha t}$ out front means that both terms decay exponentially. If you like, the amplitude decays away before the system is able to undergo even a single oscillation. Instead, the position can change sign at most once. This is plotted on the right of Figure 2.2. 

- Critical Damping: $\omega_0^2 = \alpha^2$ . Now the two roots $\beta_{\pm}$ coincide. With a double root of this form, the most general solution takes the form, 

$$
x = (A + B t) e ^ {- \alpha t}\tag{2.120}
$$

with A and B integration constants. Again, there are no oscillations but, with the initial condition $B > \alpha$ , the system does achieve some mild linear growth for times $t < 1/\alpha$ , after which it decays away. 

Fig. 2.2 Typical motion of the underdamped oscillator on the left, and the overdamped oscillator on the right. 

## 2.5.2 The Damped, Driven Harmonic Oscillator

Here is a slight variation on the theme: we keep with the damped harmonic oscillator (2.112), but now introduce an additional, timedependent, driving force $F(t)$ . The equation of motion is 

$$
m \ddot {x} + \gamma \dot {x} + k x = F (t).\tag{2.121}
$$

Obviously the physics depends on the exact form of the driving force $F(t)$ . It is fruitful to consider a periodic driving force 

$$
F (t) = F _ {0} \cos (\Omega t).\tag{2.122}
$$

This attempts to push the harmonic oscillator back and forth with some frequency $\Omega$ . As we'll see, the physics is now all to do with how the frequency $\Omega$ at which you drive the system interacts with the natural frequency of oscillation. 

Again, we solve this by considering the complex version of the equation. The driving force is $F(t) = \operatorname{Re}(F_{0}e^{i\Omega t})$ , which means that we can find a solution to (2.121) by taking the real part of a solution to the complex equation 

$$
\ddot {x} + 2 \alpha \dot {x} + \omega_ {0} ^ {2} x = \frac {F _ {0}}{m} e ^ {i \Omega t}.\tag{2.123}
$$

Here, as in (2.113), we've introduced the rescaled variables $\alpha = \gamma / 2m$ and $\omega_0^2 = k/m$ on the left-hand side. We look for complex solutions to (2.123) of the form $x(t) = Ce^{i\Omega t}$ . Note that, in this ansatz, we're deliberately looking for solutions in which the system oscillates at the same frequency $\Omega$ at which it's forced. We get 

$$
\begin{array}{r l} & C \left(- \Omega^ {2} + 2 i \alpha \Omega + \omega_ {0} ^ {2}\right) = \frac {F _ {0}}{m} \\ \Longrightarrow & C = \frac {F _ {0}}{m} \frac {1}{(\omega_ {0} ^ {2} + 2 i \alpha \Omega - \Omega^ {2})}. \end{array}\tag{2.124}
$$

We see that the equation of motion fixes the overall amplitude C and, because of the friction term $i\alpha\Omega$ , it is necessarily complex. Written in terms of its modulus and complex phase, we have $C = |C|e^{i\phi}$ with 

$$
| C | = \frac {F _ {0}}{m} \frac {1}{\sqrt {(\omega_ {0} ^ {2} - \Omega) ^ {2} + 4 \alpha^ {2} \Omega^ {2}}} \quad \mathrm{and} \quad \tan \phi = - \frac {2 \alpha \Omega}{\omega_ {0} ^ {2} - \Omega^ {2}}.
$$

The upshot is that, when we take the real part $\operatorname{Re}(x) = \operatorname{Re}(Ce^{i\Omega t})$ , we're left with the solution 

$$
x (t) = | C | \cos (\Omega t + \phi).\tag{2.126}
$$

This is the particular solution to $(2.121)$ . We can always augment such a solution with a homogeneous solution which solves $(2.121)$ with $F(t)=0$ . These are the solutions that we derived in the previous section. As we saw then, they always decay away in time because of the overall $e^{-\alpha t}$ factor. For this reason, in this context the homogenous solution is called a transient. If we wait long enough, only the particular solution $(2.126)$ survives. 

There's some interesting physics lurking in the expressions for the amplitude $|C|$ and the phase shift $\phi$ given in (2.125). The functions are plotted in Figure 2.3 for various values of the friction parameter $\alpha / \omega_0$ as a function of $\Omega / \omega_0$ , the ratio of the frequency $\Omega$ of the driving force to the natural frequency $\omega_0$ of the undamped oscillator. 

Fig. 2.3 The amplitude (on the left) and phase shift (on the right) plotted as a function of $\Omega/\omega_{0}$ . From top to bottom, the different curves have $\alpha/\omega_{0}=0.1$ , 0.5, 1, and 2. 

The phase $\phi$ is a lag between the forcing $F(t)$ and the physical oscillation. We see from Figure 2.3 that this lag is very small when $\Omega \ll \omega_0$ . But, as we increase the frequency of the driving force, the phase lag grows. The lag is always equal to $\pi/2$ when $\Omega = \omega_0$ while, for $\Omega > \omega_0$ , the oscillator is more than $\pi/2$ out of phase with the force. Physically, we're shaking the system so fast that it can't keep up. 

The amplitude of the oscillation exhibits even more dramatic behaviour, especially at small values of the friction $\alpha \ll \omega_0$ (the upper line in graph on the left of Figure 2.3). Here we see that the amplitude has a large peak when $\Omega \approx \omega_0$ . More precisely, it's straightforward to show that the amplitude $|C|$ , viewed as a function of the driving frequency $\Omega$ , has a maximum whenever $2\alpha^2 < \omega_0^2$ that occurs at 

$$
\Omega_ {\mathrm{res}} ^ {2} = \omega_ {0} ^ {2} - 2 \alpha^ {2}.\tag{2.127}
$$

This is known as the resonance frequency. It's like petting a dog behind the ears: when you get the frequency just right, the oscillator reacts with 

enthusiasm. 

If there's no friction, so $\alpha = 0$ , then the amplitude $|C|$ in (2.125) diverges as we tune the driving force to resonance: $|C| \to \infty$ and $\Omega \to \omega_{0}$ . In realistic systems, even if friction terms are absent there may be additional non-linear terms that help mitigate this divergence. 

## 2.5.3 Terminal Velocity

You can drop a mouse down a thousand-yard mine shaft; and, on arriving at the bottom, it gets a slight shock and walks away, provided that the ground is fairly soft. A rat is killed, a man is broken, a horse splashes. 

## J.B.S. Haldane

We now turn our attention to various other examples of particles moving in the presence of friction. In this section, we look at air resistance, and how this slows down objects that are dropped. As we mentioned above, in this case the relevant drag force is quadratic: $F = -\gamma |v| v$ . 

We will drop a particle of mass m. We measure its height z to be in the upwards direction, meaning that the particle is going up if the velocity $v = dz/dt > 0$ . The direction of the friction force is always in the opposite direction to the motion, which means that it's useful to separately consider the cases where the particle goes up and when it comes down. 

## Coming Down

Suppose that we drop the particle from some height. The equation of motion is given by 

$$
m \frac {d v}{d t} = - m g + \gamma v ^ {2}.\tag{2.128}
$$

Note the minus signs on the right-hand side: gravity acts downwards, so comes with a minus sign. But because the particle is falling down, friction is acting upwards and so comes with a plus sign. Dividing through by m, we have 

$$
\frac {d v}{d t} = - g + \frac {\gamma v ^ {2}}{m}.\tag{2.129}
$$

We've written this as a first order differential equation for $v = \dot{x}$ , rather than as a second order differential equation for $x$ itself. This makes life easier. If we integrate the equation once, we get 

$$
t = - \int_ {0} ^ {v} \frac {d v ^ {\prime}}{g - \gamma v ^ {\prime 2} / m}.\tag{2.130}
$$

This can be easily solved by the substitution $v' = \sqrt{mg/\gamma} \tanh x$ , giving 

$$
t = - \sqrt {\frac {m}{\gamma g}} \tanh ^ {- 1} \left(\sqrt {\frac {\gamma}{m g}} v\right).\tag{2.131}
$$

Inverting this gives us the speed as a function of time: 

$$
v (t) = - \sqrt {\frac {m g}{\gamma}} \tanh \left(\sqrt {\frac {\gamma g}{m}} t\right).\tag{2.132}
$$

We now see the effect of friction. As time increases, the velocity does not increase without bound. Instead, the particle reaches a maximum speed, 

$$
v \rightarrow - \sqrt {\frac {m g}{\gamma}} \quad \mathrm{as} t \rightarrow \infty .\tag{2.133}
$$

This is the terminal velocity. The sign is negative because the particle is falling downwards. 

In fact, if all we wanted was the terminal velocity, then we don't need to go through the whole calculation above. We can simply look for solutions of $(2.129)$ with constant speed, so dv/dt = 0. This immediately gives us $(2.133)$ . The advantage of going through the full calculation is that we learn how the velocity approaches its terminal value. 

We can now see the origin of the quote we started with. If we compare objects of equal density, then the masses scale as the volume, meaning $m \sim L^{3}$ where L is the linear size of the object. In contrast, the coefficient of quadratic friction usually scales as surface area, $\gamma \sim L^{2}$ . This means 

that the terminal velocity depends on size. For objects of equal density, we expect the terminal velocity to scale as $v \sim \sqrt{L}$ . The bigger you are, the faster you hit the ground. I have no idea if this is genuinely a big enough effect to make a horse splash. (Haldane was a biologist, so he should know what it takes to make an animal splash. But in his essay on this subject he assumed linear, rather than quadratic, drag so maybe not.) 

## Going Up

Now let's re-do the calculation, but where we start by throwing the particle upwards. Since both gravity and friction are now acting downwards, we get a flip of a minus sign in the equation of motion. It becomes 

$$
\frac {d v}{d t} = - g - \frac {\gamma v ^ {2}}{m}.\tag{2.134}
$$

Suppose that we throw the object up with initial speed $u$ and we want to figure out the maximum height $h$ that it reaches. We could follow our earlier calculation and integrate (2.134) to determine $v = v(t)$ . But, if we don't care at all about time, then there's a more useful way to do things. Instead of thinking of $v(t)$ , we can instead consider velocity as a function of distance: $v = v(z)$ . Of course, we also have $z = z(t)$ . Using the chain rule, the equation of motion (2.134) can be written as 

$$
{\frac {d v}{d t}} = {\frac {d v}{d z}} {\frac {d z}{d t}} = v {\frac {d v}{d z}} = - g - {\frac {\gamma v ^ {2}}{m}}\tag{2.135}
$$

or, equivalently, 

$$
\frac {1}{2} \frac {d (v ^ {2})}{d z} = - g - \frac {\gamma v ^ {2}}{m}.\tag{2.136}
$$

Now we can integrate this equation to get velocity as a function of distance. Writing $y = v^{2}$ , we have 

$$
\begin{array}{l l} & \int_ {u ^ {2}} ^ {0} \frac {d y}{g + \gamma y / m} = - 2 \int_ {0} ^ {h} d z \\ \Longrightarrow & \frac {m}{\gamma} \left[ \log \left(g + \frac {\gamma y}{m}\right) \right] _ {y = u ^ {2}} ^ {y = 0} = - 2 h \end{array}\tag{2.137}
$$

which we can rearrange to get the final answer: the maximum height h that the particle reaches is 

$$
h = \frac {m}{2 \gamma} \log \left(1 + \frac {\gamma u ^ {2}}{m g}\right) .\tag{2.138}
$$

It's worth looking at what happens when the friction coefficient in (2.138) is small. Naively, it looks like we're in trouble here because as $\gamma \rightarrow 0$ , the term in front gets very large. But surely the height shouldn't go to infinity just because the friction is small! The resolution to this is that the log is also getting small in this limit. Expanding the log, we have 

$$
h = \frac {u ^ {2}}{2 g} \left(1 - \frac {\gamma u ^ {2}}{2 m g} + \dots\right).\tag{2.139}
$$

Here the leading term is indeed the answer we would get in the absence of friction; the subleading terms tell us how much a little friction lowers the attained height. 

## 2.5.4 Ohm's Law

Our next example is particularly physical. We will calculate the resistance of a wire to conduct electricity. From a microscopic point of view, the electric current is carried by electrons moving in the wire. 

As we've seen in Section 2.4, a constant electric field $E$ applied to the wire causes the electron to accelerate. But they don't accelerate forever: there are typically impurities in the wire that the electrons bounce off. A fairly good model for the resulting physics, known as the Drude mode, treats the electrons as classical particles, with impurities modelled by a linear damping term. The resulting equation of motion is 

$$
m \ddot {x} = - e E - \gamma \dot {x}.\tag{2.140}
$$

where -e is the electric charge of the electron. (Its value was given in $(2.75)$ .) As in the previous example, we can immediately write down the terminal velocity, simply by setting $\ddot{x} = 0$ : it is 

$$
v = - \frac {e E}{\gamma}.\tag{2.141}
$$

In a conductor, the velocity of the electron v is proportional to the electric current density, j, through the relation 

$$
j = - e n v\tag{2.142}
$$

where n is the number density of electrons. The result $(2.141)$ is then interpreted as a relationship between the current density and the electric field 

$$
j = \sigma E \quad \mathrm{with} \quad \sigma = \frac {e ^ {2} n}{\gamma}.\tag{2.143}
$$

The quantity $\sigma$ is called the conductivity and the equation (2.143) is known as Ohm's law. 

If you've done some physics before, then you've probably seen Ohm's law and, most likely, it did not look like (2.143). However, it's easy to massage this expression into something more familiar. If the wire has length $L$ and cross-sectional area $A$ , then the current $I$ is defined as $I = jA$ . Meanwhile, the voltage dropped across the wire is the difference in the electrostatic potential, or $V = EL$ . With this in hand, we can rewrite Ohm's law as (2.143) 

$$
V = I R \quad \text { with } \quad R = \frac {L}{\sigma A} .\tag{2.144}
$$

The quantity $1/\sigma$ is called the resistivity and, after multiplying by the geometrical factors L and 1/A, we get the (electric) resistance R. Hopefully this now looks more familiar. The utility of the calculation above is that we can express the resistance in terms of the microscopic drag force $\gamma$ experienced by the electron. In the volume on Condensed Matter, we will compute $\gamma$ due to various different effects. 

## 2.5.5 Three-Dimensional Motion with Linear Drag

All our frictional examples so far have been effectively one-dimensional. Here we give a three-dimensional example which provides another illustration of how to treat vector differential equations and, specifically, how to work with vector constants of integration. We will consider a projectile, moving under gravity, experiencing linear drag. (Think of a projectile moving very slowly in a viscous liquid.) At time t = 0, we throw the object with velocity u. What is its subsequent motion? 

The equation of motion is 

$$
m \frac {d \mathbf {v}}{d t} = m \mathbf {g} - \gamma \mathbf {v}.\tag{2.145}
$$

We can solve this by introducing the integrating factor $e^{\gamma t/m}$ to write the equation as 

$$
\frac {d}{d t} \left(e ^ {\gamma t / m} \mathbf {v}\right) = e ^ {\gamma t / m} \mathbf {g}.\tag{2.146}
$$

We now integrate, but have to introduce a vector integration constant – let's call it c – for our troubles. We have 

$$
\mathbf {v} = \frac {m}{\gamma} \mathbf {g} + \mathbf {c} e ^ {- \gamma t / m}.\tag{2.147}
$$

We specified above that, at time t = 0, the velocity is v = u, so we can use this information to determine the integration constant c. This gives us 

$$
\mathbf {v} = \frac {m}{\gamma} \mathbf {g} + \left(\mathbf {u} - \frac {m}{\gamma} \mathbf {g}\right) e ^ {- \gamma t / m}.\tag{2.148}
$$

Now we integrate $v = d x / dt$ a second time to determine x as a function of time. This gives us a second integration constant, b, 

$$
\mathbf {x} = \frac {m}{\gamma} \mathbf {g} t - \frac {m}{\gamma} \left(\mathbf {u} - \frac {m}{\gamma} \mathbf {g}\right) e ^ {- \gamma t / m} + \mathbf {b}.\tag{2.149}
$$

To determine this second integration constant, we need some further information about the initial conditions. To this end, we'll take $\mathbf{x} = 0$ at $t = 0$ . Then we have 

$$
\mathbf {x} = \frac {m}{\gamma} \mathbf {g} t + \frac {m}{\gamma} \left(\mathbf {u} - \frac {m}{\gamma} \mathbf {g}\right) \left(1 - e ^ {- \gamma t / m}\right).\tag{2.150}
$$

This is our final result. To get a better idea of what's going on, we can write this expression in terms of its components. We work in Cartesian coordinates $\mathbf{x} = (x,y,z)$ and we send the projectile off with initial velocity $\mathbf{u} = (u\cos \theta ,0,u\sin \theta)$ . With gravity acting downwards, so $\mathbf{g} = (0,0, - g)$ , our vector equation becomes three equations. One is trivial: $y = 0$ . The other two are 

$$
x = \frac {m}{\gamma} u \cos \theta \left(1 - e ^ {- \gamma t / m}\right),\tag{2.151}
$$

$$
z = - \frac {m g t}{\gamma} + \frac {m}{\gamma} \left(u \sin \theta + \frac {m g}{\gamma}\right) \left(1 - e ^ {- \gamma t / m}\right).\tag{2.15}
$$

Notice that the time scale $m/\gamma$ is important. For $t \gg m/\gamma$ , the horizontal position is essentially constant. By this time, the particle is dropping more or less vertically. 

Again, we can do a sanity check on this solution and ask: what happens when friction is small? As in our example of Section 2.5.3, there are a couple of terms that look as if they are going to become singular in the limit $\gamma\rightarrow0$ . But that sounds very unphysical. To resolve this, we should ask what $\gamma$ is small relative to. In the present case, the answer lies in the exponential terms. To say that $\gamma$ is small, really means $\gamma\ll m/t$ or, in other words, it means that we are looking at short times, $t \ll m/\gamma$ . In this limit, we can expand the exponential. Reverting to the vector form of the equation, we find 

$$
\begin{array}{r l} & {\mathbf {x} = \frac {m}{\gamma} \mathbf {g} t + \frac {m}{\gamma} \left(\mathbf {u} - \frac {m}{\gamma} \mathbf {g}\right) \left(1 - 1 + \frac {\gamma t}{m} - \frac {1}{2} \left(\frac {\gamma t}{m}\right) ^ {2} + \dots\right)} \\ & {\quad = \left(\mathbf {u} t + \frac {1}{2} \mathbf {g} t ^ {2}\right) \left(1 + \mathcal {O} \left(\frac {\gamma t}{m}\right)\right).} \end{array}
$$

So we see that, on small time scales, we indeed recover the usual story of a projectile without friction. The friction only becomes relevant when $t \sim m/\gamma$ . 

## 2.6 Appendix: Two Digressions

In this appendix we give some extra details on two results that we elided earlier in the chapter. 

## 2.6.1 Line Integrals and Conservative Forces

In Section 2.2.2, we argued that the only position-dependent forces that conserves energy take the form $F = -\nabla V$ for some potential $V(\mathbf{x})$ . Showing that $F = -\nabla V$ conserves energy was straightforward, but to show that these are the only kinds of forces that conserve energy requires a result from vector calculus. 

To this end, we computed the work done by a force $\mathbf{F}(\mathbf{x})$ when a particle travels along a curve C from point $x_{1}$ to point $x_{2}$ , 

$$
W = \int_ {C} \mathbf {F} \cdot d \mathbf {x}.\tag{2.154}
$$

We saw in $(2.41)$ that the force conserves energy only if the work done depends only on the end points of the curve, $x_{1}$ and $x_{2}$ , and not on the curve C itself. 

There's a more elegant way to state this requirement. Consider two curves $C_1$ and $C_2$ with the same end points, as shown in the figure. If the line integral of $\mathbf{F}$ is the same going along each curve, then we can form a closed loop in which we first go from $\mathbf{x}_1$ to $\mathbf{x}_2$ along $C_1$ , and then return in the opposite direction along $C_2$ . The line integral along the return 

journey has an extra minus sign, so integrating around the loop necessarily gives zero 

$$
\oint \mathbf {F} \cdot d \mathbf {x} = 0.\tag{2.155}
$$

Our argument in Section 2.2.2 can then be restated: any position-dependent force F that conserves energy must obey $(2.155)$ for all closed curves. 

At this point, we invoke a result from vector calculus. A more detailed summary of line integrals and vector calculus can be found in the Appendices of Volume 2 on Electromagnetism. 

A Vector Calculus Result: The line integral of F around any closed curve vanishes if and only if F is conservative, i.e. 

$$
\oint \mathbf {F} \cdot d \mathbf {x} = 0 \quad \Longleftrightarrow \quad \mathbf {F} = - \nabla V\tag{2.156}
$$

for some function $V(\mathbf{x})$ . 

Proof of the Result: As is often the case, proving this statement in one direction is easier than proving it in the other. We start with the easy direction, which is essentially a re-iteration of the calculation that we already saw in Section 2.2.2. 

Consider a conservative force of the form $\mathbf{F} = -\nabla V$ . We integrate this force along a trajectory $\mathbf{x}(t)$ , from point $\mathbf{x}(t_1) = \mathbf{x}_1$ to point $\mathbf{x}(t_2) = \mathbf{x}_2$ . We'll call the curve swept out by this trajectory $C$ . Then we have 

$$
\begin{array}{r l} & {\int_ {C} \mathbf {F} \cdot d \mathbf {x} = - \int_ {C} \nabla V \cdot d \mathbf {x}} \\ & {\qquad = - \int_ {t _ {1}} ^ {t _ {2}} \frac {\partial V}{\partial x ^ {i}} \frac {d x ^ {i}}{d t} d t = - \int_ {t _ {1}} ^ {t _ {2}} \frac {d}{d t} V (\mathbf {x} (t)) d t} \end{array}
$$

where the last equality follows from the chain rule. But now we have the integral of a total derivative, so 

$$
\int_ {C} \mathbf {F} \cdot d \mathbf {x} = - \Big [ V (\mathbf {x} (t)) \Big ] _ {t _ {1}} ^ {t _ {2}} = V (\mathbf {x} _ {1}) - V (\mathbf {x} _ {2})\tag{2.15}
$$

which depends only on the end points as promised. Note that this part of the proof makes it clear that our result for line integrals is closely related to the fundamental theorem of calculus: the line integral of a conservative vector field is the analogue of the integral of a total derivative and so is given by the end points. 

Now to prove the result the other way. Given a force $\mathbf{F}(\mathbf{x})$ whose integral vanishes when taken around any closed curve, we will show that it is always possible to construct a potential $V$ . We first choose a value of $V$ at the origin. There's no unique choice here, reflecting the fact that the potential $V$ is only defined up to an overall constant. 

We can take $V(\mathbf{0}) = 0$ . Then, at any other point, which we call y, we would like to define 

$$
V (\mathbf {y}) = - \int_ {C (\mathbf {y})} \mathbf {F} \cdot d \mathbf {x}\tag{2.159}
$$

where $C(\mathbf{y})$ is some curve that starts at the origin and ends at the point y as shown in the figure. But, for this definition to make sense, we want $V(\mathbf{y})$ to be independent of the choice of curve $C(\mathbf{y})$ . Happily, that follows from the assumption that $\oint F \cdot dX = 0$ around any closed curve because, as we saw above, that means that the line integral must depend only on the end points, and not on the curve C itself. 

It remains only to show that $\nabla V = -F$ . To see this, we need to differentiate (2.159) and, at heart, this requires us to remember what differentiation actually means: it is the change of a function when the argument is varied slightly. For the function V defined in (2.159), this means 

$$
\frac {\partial V}{\partial x ^ {i}} (\mathbf {y}) = - \lim _ {\epsilon \rightarrow 0} \frac {1}{\epsilon} \left[ \int_ {C (\mathbf {y} + \epsilon \mathbf {e} _ {i})} \mathbf {F} \cdot d \mathbf {x} - \int_ {C (\mathbf {y})} \mathbf {F} \cdot d \mathbf {x} \right].
$$

The first integral goes along $C(\mathbf{y})$ , and then continues along the dotted line shown in the figure to the right. Meanwhile, the second integral goes back along $C(\mathbf{y})$ . The upshot is that the difference 

between the two terms involves only the integral along the dotted line 

$$
\frac {\partial V}{\partial x ^ {i}} (\mathbf {y}) = - \lim _ {\epsilon \to 0} \frac {1}{\epsilon} \int_ {\mathrm{dottedline}} \mathbf {F} \cdot d \mathbf {x}.
$$

The dotted line is taken to be the straight line in the $x^{i}$ direction. This means that the line integral projects onto the $F_{i}$ component of the vector F. Since we're integrating this over a small segment of length $\epsilon$ , the integral gives $\int_{\text{dotted line}} F \cdot dX \approx F_{i}\epsilon$ and, after taking the limit $\epsilon \to 0$ , we have 

$$
\frac {\partial V}{\partial x ^ {i}} (\mathbf {y}) = - F _ {i} (\mathbf {y}).\tag{2.161}
$$

This is our desired result $\nabla V = -F$ . 

□ 

## 2.6.2 The Poisson Equation

In this section, we delve a little further into the mathematics underlying the gravitational potential $\Phi$ and the related gravitational field $\mathbf{g} = -\nabla \Phi$ that we met in Section 2.3. The same mathematics also holds for the electric potential $\phi$ and electric field $\mathbf{E} = -\nabla \phi$ . The ideas that we introduce here won't be needed for the rest of this book, but they will 

come into their own in Volume 2 on Electromagnetism where they will be developed more fully. 

As we saw in $(2.58)$ , the gravitational potential for a particle of mass M sitting at the origin is given by 

$$
\Phi (\mathbf {x}) = - \frac {G M}{r}.\tag{2.162}
$$

We start with the following observation: 

Claim: The potential $(2.162)$ obeys the Poisson equation with a three-dimensional delta function source, 

$$
\nabla^ {2} \Phi = 4 \pi G M \delta^ {3} (\mathbf {x}).\tag{2.163}
$$

Here the Laplacian $\nabla^{2}$ is defined to be 

$$
\nabla^ {2} = \partial^ {2} / \partial x ^ {2} + \partial^ {2} / \partial y ^ {2} + \partial^ {2} / \partial z ^ {2}.
$$

Proof: There are two parts to the proof. The first is to look at points away from the origin, so $r \neq 0$ . Here we need the form of the Laplacian $\nabla^{2}$ acting on a spherically symmetric function $\Phi(r)$ . A slightly fiddly calculation (which you can find in Volume 2 on Electromagnetism) shows that the Laplacian can be written as 

$$
\nabla^ {2} \Phi = \frac {d ^ {2} \Phi}{d r ^ {2}} + \frac {2}{r} \frac {d \Phi}{d r} = \frac {1}{r ^ {2}} \frac {d}{d r} \left(r ^ {2} \frac {d \Phi}{d r}\right) = \frac {1}{r} \frac {d ^ {2} (r \Phi)}{d r ^ {2}}.
$$

This tells us that any function $\Phi(r)=A/r+B$ , with A and B constant satisfies the Laplace equation $\nabla^{2}\Phi=0$ . Note that our gravitational potential (2.162) for a point mass takes this form. However, the solution diverges at r=0 so we should be cautious in claiming that it solves the Laplace equation everywhere. Instead, we need to look more carefully at the singular point r=0. 

Looking directly at the singularity is, like staring at the Sun, bad for your health. The trick is to feel the presence of the singularity from a safe distance. To achieve this, we integrate $\nabla^2\Phi$ over a spherical region of some radius $R$ . We then use Gauss' divergence theorem. (A proof of this theorem is provided in Volume 2 on Electromagnetism.) This allows us to write 

$$
\int d ^ {3} x \nabla^ {2} \Phi = \int_ {\mathbf {S} ^ {2}} \nabla \Phi \cdot d \mathbf {S} = - \int_ {\mathbf {S} ^ {2}} \mathbf {g} \cdot d \mathbf {S}\tag{2.165}
$$

where the surface integrals are over a sphere $S^{2}$ of radius R and, in the second equality, we've used the definition of the gravitational field $g = -\nabla\Phi$ . But now something rather nice happens. This is because, as shown in (2.57), the gravitational field drops off as $1/r^{2}$ . Meanwhile, the surface area A of a sphere radius r grows as $r^{2}$ : it is $A = 4\pi r^{2}$ . (As an aside: this is no coincidence. If we lived in a world with d spatial dimensions, the gravitational field would drop off as $1/r^{d-1}$ .) This means that we can easily compute the integral of the gravitational field in (2.165) to find 

$$
\int d ^ {3} x \nabla^ {2} \Phi = 4 \pi G M.\tag{2.166}
$$

Putting this together, we know that $\nabla^{2}\Phi = 0$ everywhere except at r = 0. But, when we integrate $\nabla^{2}\Phi$ over a region that includes the origin, we get the constant $4\pi GM$ as shown in (2.166). This means that $\nabla^{2}\Phi$ must be proportional to a delta function at the origin, with strength (2.163). ☐ 

So far, the fact that $\Phi$ solves the Poisson equation (2.163) hasn't told us anything new. But, the real power comes when we combine this with the principle of superposition which we met previously in the guise of (2.59). This says that the gravitational potential due to many masses is just the sum due to each. For a single point mass $M$ , the right-hand side of the Poisson equation is the singular density $\rho(\mathbf{x}) = M\delta^3(\mathbf{x})$ . For a general distribution of masses with density $\rho(\mathbf{x})$ , the field $\Phi$ obeys the Poisson equation 

$$
\nabla^ {2} \Phi = 4 \pi G \rho (\mathbf {x}).\tag{2.167}
$$

Replaying the game above, if we integrate this formula over any region V, bounded by some surface $S = \partial V$ , then, invoking Gauss' divergence theorem, we have 

$$
\int_ {V} d ^ {3} x \nabla^ {2} \Phi = \int_ {S} \nabla \Phi \cdot d \mathbf {S} = - \int_ {S} \mathbf {g} \cdot d \mathbf {S} = 4 \pi G \int_ {V} d ^ {3} x \rho (\mathbf {x}).
$$

We learn a rather lovely fact: if we integrate the gravitational field g over any closed surface, then it tells us how much mass is contained within that surface. 

$$
\int \mathbf {g} \cdot d \mathbf {S} = - 4 \pi G M\tag{2.169}
$$

where $M$ is now the total mass contained within the region $V$ . This is known as Gauss' law. As we've mentioned already, it's an idea that we'll explore in much greater detail in Volume 2 on Electromagnetism. 

## The Gravitational Field of a Planet Revisited

In Section 2.3.1, we showed that the gravitational field outside a spherical planet is the same as if all the mass was concentrated at the centre. The technology we have developed here gives us a particularly straightforward way to re-derive this result. We again require that the density $\rho(r)$ of the planet is spherically symmetric, but not necessarily constant. The spherical symmetry of the problem then ensures that the gravitational field itself is also spherically symmetric, with $\mathbf{g}(\mathbf{x}) = g(r)\hat{\mathbf{r}}$ . If we integrate the gravitational field over any spherical surface $S$ of radius $r > R$ , we have 

$$
\int_ {S} \mathbf {g} \cdot d \mathbf {S} = \int_ {S} g (r) d S = 4 \pi r ^ {2} g (r)\tag{2.170}
$$

where we recognise $4\pi r^{2}$ as the area of the sphere. From Gauss' law (2.169) we then have 

$$
\mathbf {g} (\mathbf {x}) = - \frac {G M}{r ^ {2}} \hat {\mathbf {r}}.\tag{2.171}
$$

This reproduces the result $(2.65)$ that we previously derived by explicitly performing the integral. 

We can also see what the gravitational field $\mathbf{g}(\mathbf{x})$ looks like inside the planet, where r < R. This follows immediately from the same calculation as above, which now yields 

$$
\mathbf {g} (\mathbf {x}) = - \frac {G M (r)}{r ^ {2}} \hat {\mathbf {r}}\tag{2.172}
$$

where $M(r)$ is the mass contained within radius $r < R$ . This result is rather cute: it says that, at least for spherically symmetric mass distributions, you don't feel the mass outside you. Instead, the gravitational field at any point is determined only by what lies inside a sphere of a given radius. So if, for example, you were able to hollow out the centre of a planet (unlikely, admittedly) then anyone living there would feel no gravitational force from the mass that surrounds them. 

## The Poisson Equation in Electromagnetism

As well as the obvious similarities between the inverse-square laws of gravity and electrostatics, there is also a clear analogy between their attendant fields. The gravitational field $\mathbf{g}(\mathbf{x})$ is analogous to the electric field $\mathbf{E}(\mathbf{x})$ , while the gravitational potential $\Phi(\mathbf{x})$ is analogous to the electric potential $\phi(\mathbf{x})$ . This means that we can rerun the arguments above to learn that the electric potential $\phi$ must also satisfy the Poisson equation (2.167), this time with 

$$
\nabla^ {2} \phi = - \frac {\rho_ {e} (\mathbf {x})}{\epsilon_ {0}}\tag{2.173}
$$

where $\rho_{e}(\mathbf{x})$ is the electric charge density. Correspondingly, in analogy with $(2.169)$ , if we integrate the electric field over a closed surface S then it tells us the total charge Q enclosed within 

$$
\int_ {S} \mathbf {E} \cdot d \mathbf {S} = \frac {Q}{\epsilon_ {0}}.\tag{2.174}
$$

This is known as Gauss' law. These kind of calculations are the jumping off point for the study of electromagnetism. We will see much more of this in Volume 2 of this series. 

## Interlude: Dimensional Analysis

The essence of dimensional analysis is very simple: if you are asked how hot it is outside, the answer is never “2 o'clock”. You’ve got to make sure that the units agree. Quantities which come with units are said to have dimensions. In contrast, pure numbers such as 2 or $\pi$ are said to be dimensionless. 

In all the examples that we met in the previous section, the units are hiding within the variables. Nonetheless, it's worth our effort to dig them out. In many situations, it is useful to identify three fundamental dimensions: length $L$ , mass $M$ , and time $T$ . The dimensions of all other quantities should be expressible in terms of these. We will denote the dimensions of a quantity $Y$ as $[Y]$ . Some basic examples include: 

$$
\begin{array}{c} {\mathrm {[Area] = L^ {2}}} \\ {\mathrm {[Speed] = LT^ {- 1}}} \\ {\mathrm {[Acceleration] = LT^ {- 2}}} \\ {\mathrm {[Force] = MLT^ {- 2}}} \\ {\mathrm {[Energy] = ML^ {2} T^ {- 2}}.} \end{array}
$$

The first three should be obvious. You can quickly derive the last two by thinking of your favourite equation and insisting that the dimensions on both sides are consistent. For example, F = ma immediately gives the dimensions $[F]$ , while $E = \frac{1}{2} mv^2$ will give you the dimensions $[E]$ . This same technique can be used to determine the dimensions of any constants that appear in equations. For example, Newton's gravitational constant appears in the formula $F = -GMm / r^2$ . Matching dimensions on both sides tells us that 

$$
[ G ] = M ^ {- 1} L ^ {3} T ^ {- 2}.\tag{3.1}
$$

You shouldn't be too dogmatic in insisting that there are exactly three dimensions of length, mass, and time. In some problems, it will be useful to introduce further dimensions such as temperature or electric charge. For yet other problems, it could be useful to distinguish between distances in the $x$ -direction and distances in the $z$ -direction. For example, if you're a sailor, you would be foolish to think of vertical distances in the same way as horizontal distances. Your life is very different if you mistakenly travel 10 fathoms (i.e. vertically) instead of 10 nautical miles (i.e. horizontally) and it's useful to introduce different units to reflect this. 

Conversely, when dealing with matters in fundamental physics, we often reduce the number of dimensional quantities. As we will see in Chapter 11, in situations where special relativity is important, time and space sit on the same footing and can be measured in the same unit, with the speed of light providing a conversion factor between the two. (I offer a small rant about this in Section 11.3.3.) Similarly, in statistical mechanics, Boltzmann's constant provides a conversion factor between temperature and energy. 

## Scaling: Bridgman's Theorem

Any equation that we derive must be dimensionally consistent. This simple observation can be a surprisingly powerful tool. First, it provides a way to quickly check whether an answer has a hope of being correct. (And can be used to spot where a mistake has appeared in a calculation.) Moreover, there are certain problems that can be answered using dimensional analysis alone, allowing you to avoid calculations all together. We now look at this in more detail. 

We start by noting that dimensionful quantities such as length L can only appear in equations as powers, e.g. $L^{\alpha}$ for some $\alpha$ . We can never have more complicated functions. One simple way to see this is to Taylor expand. For example, the exponential function has the Taylor expansion 

$$
e ^ {x} = 1 + x + \frac {x ^ {2}}{2} + \dots .\tag{3.2}
$$

The right-hand side contains all powers of $x$ and only makes sense if $x$ is a dimensionless quantity: you can never have $e^x$ appearing in a formula where $x$ is some length, otherwise you'd be adding a length to an area to a volume and so on. A similar statement holds for $\sin x$ and $\log x$ , and for your favourite and least favourite functions. In all cases, the argument must be dimensionless unless the function is simply of the form $x^\alpha$ . (If your favourite function doesn't have a Taylor expansion around $x = 0$ , simply expand around a different point to reach the same conclusion.) 

Suppose that we want to compute some quantity Y. This will have dimensions 

$$
[ Y ] = M ^ {\alpha} L ^ {\beta} T ^ {\gamma}\tag{3.3}
$$

for some $\alpha, \beta$ , and $\gamma$ . There is, in general, no need for these powers to be integers, although they are typically rational. We usually want to determine $Y$ in terms of various other quantities in the game – call them $X_i$ , with $i = 1, \ldots, n$ . These too will have certain dimensions. To start, we pick just three of them, $X_1, X_2$ , and $X_3$ . We'll assume that these three quantities are “dimensionally independent”, meaning that by taking suitable combinations of $X_1, X_2$ , and $X_3$ , we can build quantities with dimensions of length, mass, and time. Then we must be able to express $Y$ as 

$$
Y = C X _ {1} ^ {a _ {1}} X _ {2} ^ {a _ {2}} X _ {3} ^ {a _ {3}}\tag{3.4}
$$

for some $a_{1}$ , $a_{2}$ , and $a_{3}$ such that 

$$
\left[ X _ {1} ^ {a _ {1}} \right] \left[ X _ {2} ^ {a _ {2}} \right] \left[ X _ {3} ^ {a _ {3}} \right] = M ^ {\alpha} L ^ {\beta} T ^ {\gamma}\tag{3.5}
$$

which is simply the requirement that the dimensions agree on both sides. All the difficulty of the problem has been swept into determining C which, by necessity, is dimensionless. In principle, C can depend on all of the $X_{i}$ with $i = 1, \ldots, n$ . However, since C is dimensionless, it can only depend on combinations of $X_{i}$ that are also dimensionless. And this will often greatly restrict the form that the answer can take. 

## An Example: The Pendulum

The above discussion is a little abstract and obscure. We can throw some light with a simple example. We will consider a pendulum. We already discussed the pendulum earlier: it has equation of motion $(2.29)$ 

$$
\ddot {\theta} = - \frac {g}{l} \sin \theta .\tag{3.6}
$$

We'd like to know the period, $T$ . This plays the role of the quantity we called $Y$ above. Clearly $T$ has dimensions of time. (We've picked a slightly annoying choice of notation because we have the equation $[T] = T$ . Hopefully it won't cause too much confusion.) 

What are the variables $X_{i}$ that the period can depend upon? In principle there are four of them: the strength of gravity $g$ , the mass of the pendulum $m$ , the length of the pendulum $l$ , and the initial starting angle $\theta_0$ . (In fact, we could dismiss the mass $m$ immediately since it doesn't actually appear in the equation of motion, but to prove a point we'll keep it in for now.) 

The dimensions of m and l are obviously mass and length respectively. The dimensions of acceleration are $[g] = LT^{-2}$ , while the initial angle is necessarily dimensionless and we write $[\theta_{0}] = 1$ . (This follows from its periodicity, $\theta = \theta + 2\pi$ , because $2\pi$ is dimensionless. Alternatively it follows from the fact that $\theta$ sits as the argument of a sin function.) Therefore, the only dimensionless combination that we can form from our four candidates is $\theta_{0}$ itself. We can then write 

$$
T = C (\theta_ {0}) g ^ {a _ {1}} m ^ {a _ {2}} l ^ {a _ {3}}\tag{3.7}
$$

for some $a_{1}$ , $a_{2}$ , and $a_{3}$ . On dimensional grounds, we must have 

$$
[ T ] = T = \left[ g ^ {a _ {1}} \right] \left[ m ^ {a _ {2}} \right] \left[ l ^ {a _ {3}} \right] = M ^ {a _ {2}} L ^ {a _ {1} + a _ {3}} T ^ {- 2 a _ {1}}.\tag{3.8}
$$

The unique solution is $a_{2}=0$ (so, indeed, the period is independent of the mass) and $a_{1}=-a_{3}=-\frac{1}{2}$ . We learn immediately that the period takes the form 

$$
T = C (\theta_ {0}) \sqrt {\frac {l}{g}}.\tag{3.9}
$$

This agrees with the result (2.32) that we got the hard way by solving the equation of motion. Of course we haven't solved the problem completely because, by using dimensional analysis alone, there's no way to figure out that the function $C(\theta_0)$ is given by the elliptic integral in (2.32). Then again, we never really solved this integral anyway so we haven't lost much. 

Although the form of the solution $(3.9)$ is incomplete, it still contains some important information. For example, suppose that you are given two pendulums, with lengths $l_{1}$ and $l_{2}$ . You release them from the same starting angle and want to know how much faster the first pendulum swings compared to the second. For these kinds of comparative 

questions, the unknown function $C(\theta_{0})$ drops out and we can just immediately write down the result: 

$$
\frac {T _ {1}}{T _ {2}} = \sqrt {\frac {l _ {1}}{l _ {2}}}.\tag{3.10}
$$

As a notational aside, whenever we are interested only in how things scale with some quantity, we will use the symbol $\sim$ . (We could also use the proportional symbol $\alpha$ but it looks a little too much like the Greek letter $\alpha$ for comfort.) So equation (3.9) would be written as $T \sim \sqrt{l/g}$ . 

## The Importance of Dimensionless Quantities

The power of dimensional analysis really depends on how many dimensionless quantities we can construct from the variables at hand. If we can construct r independent dimensionless variables, then the unknown dimensionless quantity C is a function of r variables. In problems where r = 0 and there are no dimensionless combinations of variables, then C is just a number. 

It is a simple matter to count the number of dimensionless parameters in a given problem. If we have n independent variables $X_{i}$ in a problem that requires k independent dimensions then we will be able to form r = n - k dimensionless combinations. (In our discussion above, we had k = 3 corresponding to mass, length, and time.) This intuitive result sometimes goes by the grand name of the Buckingham $\Pi$ theorem, with the slightly weird $\Pi$ appearing because these dimensionless combinations are often called $\Pi_{a}$ for $a = 1, \ldots, r$ . This theorem can be proved formally by setting up a system of linear equations and invoking the rank-nullity theorem of linear algebra. Finally, the dimensionless combinations that you can make in a given problem are not unique: if x and y are both dimensionless, then so are xy and $x^{2}y$ and $x + y$ and, indeed, any function that you want to make out of these two variables. 

There are other reasons to be interested in dimensionless quantities. The first is practical: identifying dimensionless quantities at an early stage in a calculation will save you ink! In a calculation that contains lots of variables, you'll often find the same dimensionless combinations of variables appearing at every stage. In particular, as we've already seen, it is only dimensionless combinations that can appear as the arguments of functions. Often, identifying these combinations at an early stage, and perhaps even giving them a name of their own, will speed up the computation and help in avoiding errors. 

For example, if we look back at Section 2.5.5 to the problem of the 3d projectile with linear drag, we see that the dimensionless combination $\gamma t / m$ appears over and over in all steps of the calculation. In this case, it wasn't too annoying to keep writing $\gamma t / m$ . But if you find yourself doing a calculation where the combination $e^2 / 4\pi \epsilon_0 \hbar c$ appears three times on every line, then it's a good idea to come up with a new name for this object. (The chosen name, as we will see in later books, is the fine structure constant or, more concisely, $\alpha$ .) 

The second reason to be interested in dimensionless quantities is because the answer to a calculation often simplifies in certain regimes. Perhaps this is the regime of long times, or short distances, or high speeds, or some such thing. But only dimensionless numbers can be big. For a dimensionless quantity x, we can write $x \gg 1$ . But it makes no sense to write $Y \gg 1$ if Y is not dimensionless: a dimensionful quantity can only be big or small relative to something else. 

We already saw examples of this in the last chapter. For example, this is the reason that we needed to introduce a dimensionless quantity, the Reynolds number (2.109), to decide whether a system suffers linear or quadratic drag. This same issue will play a key role in Section 8.2 where we introduce the idea of perturbation theory, where the art is all about finding a small dimensionless number in which we can expand the answer. 

## Another Example: The Atomic Bomb

G.I. Taylor was one of the pre-eminent fluid dynamicists of the twentieth century. 

In 1950, he applied dimensional analysis to photographs of the Trinity test, the first atomic explosion. A series of 25 photographs were published, showing the development of the blast over time, usefully embellished by a distance scale and time stamp. One of these photographs is shown on the right. Taken together, these photographs allow a reconstruction of the radius of the shock front $R(t)$ over time. Taylor showed, using dimensional analysis, that the information in the photo was enough to determine the order of magnitude of the energy released in the explosion. 

In principle, the energy E can depend on six different variables: the first two are the radius R and the time t from the explosion. In addition, there is the density and pressure of the gas inside the fireball and of the air 

outside. We denote the density and pressure inside as $\rho$ and P respectively, and the same quantities outside as $\rho_{0}$ and $P_{0}$ . 

What are the dimensionless quantities that we can make from there? With six variables, we expect three dimensionless quantities. The first two are the obvious ratios of the density and pressure, inside and out: 

$$
\Pi_ {1} = \frac {\rho}{\rho_ {0}} \quad \text { and } \quad \Pi_ {2} = \frac {P _ {0}}{P} .\tag{3.11}
$$

But the temperatures inside the fireball are enormous, which means that we have $\rho \ll \rho_{0}$ and $P \gg P_{0}$ . So, for this extreme event, we can happily set $\Pi_{1} = \Pi_{2} = 0$ and, in doing so, effectively eliminate any dependence on $\rho$ and P. 

To find the third dimensionless variable, we need the dimensions of the various objects. We have $[\rho_{0}] = ML^{-3}$ and $[P_{0}] = ML^{-1}T^{-2}$ while, obviously, $[R] = L$ and $[t] = T$ . From these we can construct the dimensionless quantity 

$$
\Pi_ {3} = \frac {P _ {0} t ^ {2}}{\rho_ {0} R ^ {2}}.\tag{3.12}
$$

But this too is very small. The ratio $\sqrt{P_{0}/\rho_{0}}$ is, roughly, the speed of sound in air, a fact that will be derived in Volume 4 on Fluid Mechanics. It's about $300\ m\ s^{-1}$ or so. Meanwhile, R/t is the speed of the fireball which is much larger. From the photograph above, you can see that it travelled about 150 m in 0.025 s, so $R/t \approx 6000\ m\ s^{-1}$ . All of which 

means that we can set $\Pi_{3} \approx 0$ . This allows us to eliminate the air pressure $P_{0}$ from the story. 

Now we're in business. The energy $E$ released in the explosion has dimensions $[E] = ML^2 T^{-2}$ . On dimensional grounds, the only thing we can write down is 

$$
E = C \frac {\rho_ {0} R ^ {5}}{t ^ {2}}\tag{3.13}
$$

where C is an unknown constant. Of course, without knowing C this would seem to be useless. 

In general, there's a good rule of thumb to approximate constants such as $C$ : once you've figured out how many factors of $2\pi$ they contain, what's left is almost always a number that's close to one. With a little bit of experience, it's usually possible to guess the factors of $2\pi$ as well since they usually arise for some geometric reason. All of which means that dimensional analysis is, perhaps, even more unreasonably useful than we might have originally hoped. Here, for example, is Einstein himself weighing in on the issue: 

from the photograph, with $R \approx 150 \, m$ at t = 0.025 s. The density of air is $\rho_{0} \approx 1.3 \, kg \, m^{-3}$ , all of which gives 

$$
E \approx 1. 6 \times 1 0 ^ {1 4} \mathrm{J}.\tag{3.14}
$$

Energy released in explosions is usually measured, rather quaintly, in terms of the equivalent amount of TNT. One kiloton (which is 1000 tons of TNT) releases $4.2 \times 10^{12}$ J of energy. So our estimate (3.14) equates to around 40 kilotons. The actual yield was around 20 kilotons. (Taylor was more careful and got a better estimate. I suspect that I was too sloppy in measuring the radius R in the photograph. The factor of $R^{5}$ in (3.13) means that the end result is rather sensitive to this.) 

The story of Taylor's analysis often undergoes some embellishment with him portrayed as some outsider, humiliating the US government by revealing classified information contained in their publicly available photographs. (I may have been guilty of a little embellishment along these lines myself when teaching dimensional analysis.) The truth is more interesting. Taylor was attached to the Manhattan project and, in 1941, performed a long, arduous calculation to determine the energy yield of the bomb. He published this in 1950, only after it had been declassified by the US army. The dimensional analysis argument from the photographs came only later as a check of this longer calculation. 

This story seems to me to capture something about the spirit of dimensional analysis. There's no doubt that it's an extraordinarily useful tool when checking answers that you've derived through other means. But there is an art to it and it is not so easy to wield dimensional analysis in a clever way to cut through the mist and reveal an answer that you didn't already know. To use dimensional analysis in this way needs insight and boldness and often that only comes after rolling up your sleeves and doing the hard work of the calculation that you're trying to avoid. 

## A Last Example: Rowing

Another classic demonstration of the power of dimensional analysis shows how the speed of a rowing boat depends on the number of rowers. 

A boat travelling at speed v, with cross-sectional area A submerged in the water, experiences a quadratic friction 

$$
F _ {\mathrm{drag}} \sim v ^ {2} A.\tag{3.15}
$$

(On dimensional grounds, we should have $F_{drag} \sim \rho v^{2} A$ where $\rho$ is the density of water. But the density $\rho$ will not play a role in the story and so we choose to drop it.) The power needed to overcome this drag force is then 

$$
P = F _ {\mathrm{drag}} v \sim v ^ {3} A.\tag{3.16}
$$

By Archimedes' principle, the displaced volume increases linearly with mass. We'll assume that the weight of the boat itself is negligible and the weight depends linearly on the number of rowers, $N$ . This means that the submerged volume $V \sim N$ so the submerged area scales as $A \sim N^{2/3}$ . 

Meanwhile, if we further assume that the power supplied by each rower is the same, we have $P \sim N$ . (An important assumption here is that everyone pulls. This means that the boat does not have a cox!) Putting all this together, we have $P \sim N \sim v^{3}N^{2/3}$ . Rearranging, we learn that the velocity increases with the number of rowers in a rather mild way: 

$$
v \sim N ^ {1 / 9}.\tag{3.17}
$$

This simple result apparently agrees pretty well with Olympic rowing times. 

## Dimensional Constants of Nature

The laws of physics provide us with three fundamental, dimensionful constants of nature. We have already met Newton's constant 

$$
G \approx 6. 7 \times 1 0 ^ {- 1 1} \mathrm{m} ^ {3} \mathrm{kg} ^ {- 1} \mathrm{s} ^ {- 2}\tag{3.18}
$$

which appears in both Newton's law of gravity as well as the more refined theory of gravity due to Einstein known as general relativity. The other two fundamental constants are the speed of light, 

$$
c \approx 3 \times 1 0 ^ {8} \mathrm{ms} ^ {- 1}\tag{3.19}
$$

which characterises the relationship between space and time in special relativity, and Planck's constant 

$$
\hbar \approx 1 0 ^ {- 3 4} \mathrm{Js}\tag{3.20}
$$

which determines when quantum effects become important. 

The dimensions of these constants are more important than the values they take. They are 

$$
[ G ] = M ^ {- 1} L ^ {3} T ^ {- 2}, \quad [ c ] = L T ^ {- 1}, \quad [ \hbar ] = M L ^ {2} T ^ {- 1}.
$$

The fundamental constants allow us to convert freely between quantities with dimensions of mass, length, and time. For example, given some length scale L, there is a natural time scale associated to it, given by T = L/c. This is just the time it takes for light to cross the distance L. And given some mass m there is an associated energy scale $E = mc^{2}$ . This, of course, is a rather famous equation relating energy and mass that we will derive in Chapter 11. 

Similarly, given some time scale T there is an associated energy scale $E = \hbar / T$ . The presence of $\hbar$ in this relation tells us that this has something to do with quantum effects. Roughly speaking, a quantum object oscillating with a period T will have an associated energy E. 

One last example: if we're given a mass $M$ , there is an associated distance scale given by $R = GM / c^2$ . But this is almost something that we've seen before: it is roughly the Schwarzschild radius of a black hole (2.70). (In fact, it differs by a factor of 2.) 

There is another story attached to these constants. From them, we can construct characteristic length, time, and mass scales. These are scales that are built into the laws of physics. An attempt along these lines was first made by the Irish physicist George Stoney, but this was before the discovery of Planck's constant. The idea was revived by Max Planck and these now go by the name of Planck units. They are the Planck length, 

$$
L _ {p} = \sqrt {\frac {G \hbar}{c ^ {3}}} \approx 1 0 ^ {- 3 5} \mathrm{m}\tag{3.22}
$$

the Planck time, 

$$
T _ {p} = \frac {L _ {p}}{c} = \sqrt {\frac {G \hbar}{c ^ {5}}} \approx 5 \times 1 0 ^ {- 4 4} \mathrm{s}\tag{3.23}
$$

and the Planck mass, 

$$
M _ {p} = \sqrt {\frac {c \hbar}{G}} \approx 1 0 ^ {- 8} \mathrm{kg}.\tag{3.24}
$$

Each of these characteristic scales combines each of the three constants G, $\hbar$ , and c in different ways. This means that they are telling us something about the scales at which gravity, quantum mechanics, and the structure of spacetime all merge together. 

The first thing to note is that both $L_{p}$ and $T_{p}$ are extremely small. Indeed, it's generally thought that it doesn't make sense to talk about distance 

scales smaller than $L_{p}$ because space itself breaks down when we get to that point. Similarly, there is most likely no meaning to time intervals shorter than the Planck time $T_{p}$ . 

In contrast, the Planck mass $M_p$ is a very reasonable mass scale. It's roughly the mass of a small grain of sand and there are certainly many things that are both lighter and heavier. That's because, when it comes to masses, it's not the total mass that's important but the mass density. It's all about how much mass you can squeeze into a given region. Or, equivalently because $E = mc^2$ , about how much energy you can squeeze into a given region. 

Consider an energy E in a volume $L^{3}$ . Using the idea above, we can replace the length scale L with a corresponding energy scale $E = \hbar c / L$ . This means that we can think of the energy density $E / L^{3}$ equivalently as $E^{4} / \hbar^{3} c^{3}$ . This is what we do in particle physics where we talk about the energy of a particle collider, but what we mean is the energy density. Confusingly, we describe this by just giving the value of E and leaving it implicit that it's the energy density $E^{4} / \hbar^{3} c^{3}$ that's important. 

With this in mind, we can now return to the seemingly mid-range Planck mass (3.24). The corresponding Planck energy is 

$$
E _ {p} = M _ {p} c ^ {2} \approx 1 0 ^ {1 9} \mathrm{GeV}
$$

where we've used the particle physicists' unit of choice for energy, $1\mathrm{GeV} \approx 10^{-10}\mathrm{J}$ . Viewed as an energy, this is nothing special. But viewed as an energy density, it's a huge value. Much like the Planck length and time are extreme values, so too is the Planck energy density $E_{p}^{4} / \hbar^{3} c^{3}$ : it is to be thought of as the maximum energy density that we can squeeze into a region of space. To give you some sense of scale, our current best particle accelerator is the LHC in CERN and it reaches energy densities of $E_{\mathrm{LHC}} \approx 10^{4} \mathrm{GeV}$ . It's still 15 orders of magnitude away from exploring the Planck scale. 

## Systems of Particles

So far, we've only considered the motion of a single particle. If our goal is to understand everything in the universe, that's a little limiting. In this section, we take a small step forwards: we will describe the dynamics of $N$ interacting particles. 

## 4.1 Interactions Between Particles

The first thing that we do is put a label $a = 1, \ldots, N$ on everything. The $a^{th}$ particle has mass $m_{a}$ , position $x_{a}$ , and momentum $p_{a} = m_{a} \dot{x}_{a}$ . (A word of warning: do not confuse the label a on the vectors with index notation for vectors!) Newton's second law should now be written for each particle, 

$$
\dot {\mathbf {p}} _ {a} = \mathbf {F} _ {a}\tag{4.1}
$$

where $F_{a}$ is the force acting on the $a^{th}$ particle. The novelty is that the force $F_{a}$ can be split into two parts: an external force $F_{a}^{ext}$ (for example, if the whole system sits in a gravitational field) and a force due to the presence of the other particles. We write 

$$
\mathbf {F} _ {a} = \mathbf {F} _ {a} ^ {\mathrm{ext}} + \sum_ {b \neq a} \mathbf {F} _ {a b}\tag{4.2}
$$

where $F_{ab}$ is the force on particle a due to particle b. 

## Examples: Gravitational and Coulomb Forces Revisited

In Chapter 2, we described Newton's force of gravity and Coulomb's electrostatic force. In both cases, we thought of these as external forces, set up by some particle that was pinned at the origin, and acting on a second test particle. In reality, it is better to think of these forces as interactions between two particles, both of which are free to move. 

First, the force of gravity. If we have two particles with masses $m_{1}$ and $m_{2}$ , and positions $x_{1}$ and $x_{2}$ , then the first particle experiences a force due to the presence of the second, 

$$
\mathbf {F} _ {1 2} = - \frac {G m _ {1} m _ {2}}{| \mathbf {x} _ {1} - \mathbf {x} _ {2} | ^ {3}} (\mathbf {x} _ {1} - \mathbf {x} _ {2}).\tag{4.3}
$$

This should be viewed as a more correct form of Newton's inverse-square law (2.55). (Despite the slightly jarring cube in the denominator, it is an inverse-square because we haven't normalised the vector $(\mathbf{x}_1 - \mathbf{x}_2)$ in the numerator.) The overall minus sign is such that this force attracts the particle at $\mathbf{x}_1$ towards $\mathbf{x}_2$ . 

Meanwhile, the second particle also experiences a force due to the first. This force is 

$$
\mathbf {F} _ {2 1} = - \frac {G m _ {1} m _ {2}}{| \mathbf {x} _ {1} - \mathbf {x} _ {2} | ^ {3}} (\mathbf {x} _ {2} - \mathbf {x} _ {1}).\tag{4.4}
$$

It takes the same form as $(4.3)$ but with the a = 1, 2 labels switched. This means that the second particle is attracted towards the first. 

The same story holds for the Coulomb force. Two particles, with electric charges $q_{1}$ and $q_{2}$ , and positions $x_{1}$ and $x_{2}$ , impart mutual equal and opposite forces on each other, given by 

$$
\begin{array}{r l} & {\mathbf {F} _ {1 2} = \frac {q _ {1} q _ {2}}{4 \pi \epsilon_ {0} | \mathbf {x} _ {1} - \mathbf {x} _ {2} | ^ {3}} (\mathbf {x} _ {1} - \mathbf {x} _ {2})} \\ {\mathrm{and}} & {\mathbf {F} _ {2 1} = \frac {q _ {1} q _ {2}}{4 \pi \epsilon_ {0} | \mathbf {x} _ {1} - \mathbf {x} _ {2} | ^ {3}} (\mathbf {x} _ {2} - \mathbf {x} _ {1}).} \end{array}\tag{4.5}
$$

This is the correct form of the Coulomb law $(2.105)$ . 

## 4.1.1 Newton's Third Law

Both the gravitational and electrostatic forces have the property that $F_{12} = -F_{21}$ . This is what Newton meant by his third law: every action has an equal and opposite reaction, or, in equations, 

• N3 Revisited: $F_{ab} = -F_{ba}$ 

In elevating this to one of his three laws, Newton was stating that all forces in nature must obey this. To see why this is a sensible proposition we need to look a little closer at the dynamics of a system of particles. 

## 4.1.2 Centre of Mass Motion

The total mass of the system of particles is 

$$
M = \sum_ {a = 1} ^ {N} m _ {a}.\tag{4.6}
$$

We define the centre of mass to be 

$$
\mathbf {R} = \frac {1}{M} \sum_ {a = 1} ^ {N} m _ {a} \mathbf {x} _ {a}.\tag{4.7}
$$

The total momentum of the system, P, can then be written entirely in terms of the centre of mass motion, 

$$
\mathbf {P} = \sum_ {a = 1} ^ {N} \mathbf {p} _ {a} = M \dot {\mathbf {R}}.\tag{4.8}
$$

We can now look at how the centre of mass moves. We have 

$$
\dot {\mathbf {P}} = \sum_ {a} \dot {\mathbf {p}} _ {a} = \sum_ {a} \left(\mathbf {F} _ {a} ^ {\text { ext }} + \sum_ {b \neq a} \mathbf {F} _ {a b}\right) = \sum_ {a} \mathbf {F} _ {a} ^ {\text { ext }} + \sum_ {a <   b} (\mathbf {F} _ {a b} + \mathbf {F} _ {b}
$$

But Newton's third law tells us that $\mathbf{F}_{ab} = -\mathbf{F}_{ba}$ and the last term vanishes, leaving 

$$
\dot {\mathbf {P}} = \sum_ {a} \mathbf {F} _ {a} ^ {\mathrm{ext}}.\tag{4.10}
$$

This is an important formula. If you just want to know the motion of the centre of mass of a system of particles, then only the external forces count. If you throw a wriggling, squealing cat then its internal forces $F_{ab}$ can change its orientation, but they can do nothing to change the path of its centre of mass. That is dictated by gravity alone. (Actually, this statement is only true for conservative forces. The shape of the cat could change friction coefficients which would, in turn, change the external forces.) 

It's hard to overstate this point. Without Newton's third law, the whole Newtonian framework for mechanics would come crashing down. After all, nothing that we really describe is truly a point particle. Certainly not a planet or a cat, but even a seemingly elementary particle like a proton has an extraordinarily complicated internal structure, made up of hundreds of quarks, anti-quarks, and gluons. (If you thought the proton was made of just three quarks, that's because you were lied to.) Yet none of these details matter because everything, regardless of the details, acts as a point particle if we just focus on the position of its centre of mass. 

Put grandly, this is what makes science possible at all. We can figure out the motion of a planet around a star without worrying about any internal geophysical dynamics, or sociology of the inhabitants, because none of those internal forces matter: they all just cancel out due to Newton's third law. Equally, we can figure out the motion of the planets without knowing about the constituent quarks, again because all the interaction forces between the quarks cancel out. Newton's third law tells us that we don't have to sweat the small stuff. We can focus on the big, important things, and work our way down in scale only when we're ready. 

## Momentum Conservation

There is also an important, albeit mathematically trivial, conservation law that follows from $(4.10)$ . If there is no net external force on the system, so $\sum_{a}\mathbf{F}_{a}^{\mathrm{ext}} = 0$ , then the total momentum of the system is conserved: $\dot{\mathbf{P}} = 0$ 

Although this looks just like the conservation law for a single particle, there is a new ingredient: we still have momentum conservation, regardless of any interaction force $F_{ab}$ between particles. It's only the external force $F_{ext}$ that ruins momentum conservation. Ultimately, it turns out, there is no external force in the fundamental laws of physics. There are only interaction forces between particles. This is where the statement that the laws of physics conserve momentum comes from. 

## 4.1.3 Angular Momentum

The total angular momentum of the system about the origin is defined as 

$$
\mathbf {L} = \sum_ {a} \mathbf {x} _ {a} \times \mathbf {p} _ {a}.\tag{4.11}
$$

We can look at how this changes in time, following the calculation from Section 2.2.3. If we take the time derivative, we get 

$$
\frac {d \mathbf {L}}{d t} = \sum_ {a} \left(\dot {\mathbf {x}} _ {a} \times \mathbf {p} _ {a} + \mathbf {x} _ {a} \times \dot {\mathbf {p}} _ {a}\right).\tag{4.12}
$$

But the first term disappears because $P_{a}$ is parallel to $\dot{x}_{a}$ . The change in the total angular momentum is then 

$$
\begin{array}{r} \frac {d \mathbf {L}}{d t} = \sum_ {a} \mathbf {x} _ {a} \times \dot {\mathbf {p}} _ {a} = \sum_ {a} \mathbf {x} _ {a} \times \left(\mathbf {F} _ {a} ^ {\mathrm{ext}} + \sum_ {b \neq a} \mathbf {F} _ {a b}\right) \\ = \boldsymbol {\tau} + \sum_ {a} \sum_ {b \neq a} \mathbf {x} _ {a} \times \mathbf {F} _ {a b} \end{array}\tag{4.13}
$$

where $\tau \equiv \sum_{a} \mathbf{x}_{a} \times \mathbf{F}_{a}^{\mathrm{ext}}$ is the total external torque. The second term in (4.13) involves the internal forces. And that's bad because, as we stressed above, there's a lot riding on the idea that we can treat systems of particles as a single, unified particle if we ignore the internal forces. (It's what makes science possible, remember!) So what are we going to do about it? 

Newton's third law tells us that $\mathbf{F}_{ab} = -\mathbf{F}_{ba}$ , which allows us to write 

$$
\sum_ {a} \sum_ {a \neq b} \mathbf {x} _ {a} \times \mathbf {F} _ {a b} = \sum_ {a <   b} (\mathbf {x} _ {a} - \mathbf {x} _ {b}) \times \mathbf {F} _ {a b}.\tag{4.14}
$$

There's no reason that this has to vanish. But it does vanish if we require one further property of the interaction force between particles. We ask that the force $\mathbf{F}_{ab}$ between the $a^{\text{th}}$ and $b^{\text{th}}$ particle is parallel to the line $(\mathbf{x}_a - \mathbf{x}_b)$ joining the two particles. This is sometimes elevated to a strong form of Newton's third law: 

- N3 Revisited Again: $\mathbf{F}_{ab} = -\mathbf{F}_{ba}$ and is parallel to $(\mathbf{x}_a - \mathbf{x}_b)$ . 

In situations where this strong form of Newton's third law holds, the change in total angular momentum is again due only to external forces, 

$$
\frac {d \mathbf {L}}{d t} = \boldsymbol {\tau}.\tag{4.15}
$$

Both the gravitational (4.3) and electrostatic (4.5) forces obey the strong form of Newton's third law. 

You might sometimes read that there are forces that do not obey Newton's third law, either in weak or strong form. The magnetic force between particles is sometimes hailed as a culprit. One charged, moving particle induces a magnetic field that affects the motion of another. But the second does not reciprocate in the same way. In fact a closer look shows that these “violations” of the third law are kind of fake because they ignore important properties of the electric and magnetic fields themselves, like the fact these fields can carry angular momentum. At heart, these cheap counterexamples are little different from an underwater swimmer who can twist and turn, seemingly violating the conservation of momentum and angular momentum, until you realise that the water itself carries these properties too. 

## 4.1.4 Energy

The total kinetic energy of the system of particles is 

$$
T = \frac {1}{2} \sum_ {a} m _ {a} \dot {\mathbf {x}} _ {a} \cdot \dot {\mathbf {x}} _ {a}.\tag{4.16}
$$

We can decompose the position of each particle as 

$$
\mathbf {x} _ {a} = \mathbf {R} + \mathbf {y} _ {a}\tag{4.17}
$$

where $y_{a}$ is the position of the $a^{th}$ particle relative to the centre of mass. Because the centre of mass is defined as $\sum_{a} m_{a} x_{a} = M R$ , the $y_{a}$ must obey the constraint $\sum_{a} m_{a} y_{a} = 0$ . The kinetic energy can then be written as 

$$
\begin{array}{r l} & T = \frac {1}{2} \sum_ {a} m _ {a} \left(\dot {\mathbf {R}} + \dot {\mathbf {y}} _ {a}\right) ^ {2} \\ & \quad = \frac {1}{2} \sum_ {a} m _ {a} \dot {\mathbf {R}} ^ {2} + \dot {\mathbf {R}} \cdot \sum_ {a} m _ {a} \dot {\mathbf {y}} _ {a} + \frac {1}{2} \sum_ {a} m _ {a} \dot {\mathbf {y}} _ {a} ^ {2}. \end{array}\tag{4.1}
$$

As an aside: the slightly lazy notation of taking the square of a vector simply means the taking inner product with itself $y^{2} = y \cdot y$ (because what else could it mean?). The middle, cross-term, vanishes because of the constraint on the $y_{a}$ and we are left with 

$$
T = \frac {1}{2} M \dot {\mathbf {R}} ^ {2} + \frac {1}{2} \sum_ {a} m _ {a} \dot {\mathbf {y}} _ {a} ^ {2}.\tag{4.19}
$$

That's rather nice. It's telling us that the kinetic energy splits up into the kinetic energy of the centre of mass, together with the kinetic energy of the particles moving around the centre of mass. We'll use this to great effect in Chapter 9 where we discuss the motion of rigid bodies. 

We can repeat the analysis that led to the construction of the potential energy. When the $a^{th}$ particle moves along a trajectory $C_{a}$ , the difference in kinetic energies is given by 

$$
T (t _ {2}) - T (t _ {1}) = \sum_ {a} \int_ {C _ {a}} \mathbf {F} _ {a} ^ {\mathrm{ext}} \cdot d \mathbf {x} _ {a} + \sum_ {a} \sum_ {b \neq a} \int_ {C _ {a}} \mathbf {F} _ {a b} \cdot d \mathbf {x} _ {a}.
$$

If we want to construct a potential energy, we need both the external and internal forces to be conservative. We define these as follows: 

- Conservative External Forces: $\mathbf{F}_a^{\mathrm{ext}} = -\nabla_a V_a(\mathbf{x}_a)$ . 

- Conservative Internal Forces: $\mathbf{F}_{ab} = -\nabla_a V_{ab}(|\mathbf{x}_a - \mathbf{x}_b|)$ . 

Here we are using the notation $\nabla_{a} = \partial/\partial\mathbf{x}_{a}$ and, for once, we're not employing summation convention. (I'm aware that we've only actually invoked the summation convention once so far in this book, with summations otherwise kept largely explicit, so it seems odd to make a big deal of the fact that we're not using this convention above! But as this series of books proceeds, the summation convention will become the default and so it's good to get into a habit of flagging up equations where it's not being used.) 

Potentials of the form $V_{ab}(|\mathbf{x}_{a}-\mathbf{x}_{b}|)$ are rather special and are far from the most general interaction potential that we could imagine. In particular, the force on particle a due to particle b depends only the distance $r = |x_{a} - x_{b}|$ between the two particles, and does not depend at all on the positions of all the other particles. Although restrictive, it turns out that the most interesting forces are indeed of this kind. 

In addition, we take $V_{ab}(r) = V_{ba}(r)$ . This immediately ensures that both the weak and strong versions of Newton's third law are obeyed, since 

$$
\mathbf {F} _ {a b} = - \nabla_ {a} V _ {a b} = - \frac {d V _ {a b}}{d r} \frac {(\mathbf {x} _ {a} - \mathbf {x} _ {b})}{r} = + \nabla_ {b} V _ {a b} = + \nabla_ {b} V _ {b a} = - \mathbf {F}
$$

With these assumptions, we can define a conserved energy given by 

$$
E = T + \sum_ {a} V _ {a} (\mathbf {x} _ {a}) + \sum_ {a <   b} V _ {a b} (| \mathbf {x} _ {a} - \mathbf {x} _ {b} |).\tag{4.22}
$$

Note that we sum over pairs of particles, a < b, in the final term. Taking the time derivative, and using the chain rule, we have the slightly fiddly calculation 

$$
\begin{array}{l} \dot {E} = \sum_ {a} m _ {a} \ddot {\mathbf {x}} _ {a} \cdot \dot {\mathbf {x}} _ {a} + \sum_ {a} \nabla_ {a} V _ {a} \cdot \dot {\mathbf {x}} _ {a} + \sum_ {a <   b} (\nabla_ {a} V _ {a b} \cdot \dot {\mathbf {x}} _ {a} + \nabla_ {b} V _ {a b} \cdot \\ = \sum_ {a} (m _ {a} \ddot {\mathbf {x}} _ {a} - \mathbf {F} _ {a} ^ {\mathrm{ext}}) \cdot \dot {\mathbf {x}} _ {a} - \sum_ {a <   b} (\mathbf {F} _ {a b} \cdot \dot {\mathbf {x}} _ {a} + \mathbf {F} _ {b a} \cdot \dot {\mathbf {x}} _ {b}) \\ = \sum_ {a} (m _ {a} \ddot {\mathbf {x}} _ {a} - \mathbf {F} _ {a} ^ {\mathrm{ext}}) \cdot \dot {\mathbf {x}} _ {a} - \sum_ {a <   b} \mathbf {F} _ {a b} \cdot \dot {\mathbf {x}} _ {a} - \sum_ {b <   a} \mathbf {F} _ {a b} \cdot \dot {\mathbf {x}} _ {a} \\ = \sum_ {a} (m _ {a} \ddot {\mathbf {x}} _ {a} - \mathbf {F} _ {a} ^ {\mathrm{ext}} - \sum_ {b \neq a} \mathbf {F} _ {a b}) \cdot \dot {\mathbf {x}} _ {a} = 0. \end{array}
$$

We see that, as promised, the energy doesn't change when the equation of motion is obeyed. 

## Gravitational and Electrostatic Forces Again

We can illustrate this for our two favourite forces. Two particles with masses $m_{a}$ , charges $q_{a}$ , and positions $x_{a}$ experience a mutual gravitational force, with 

$$
V _ {1 2} = V _ {2 1} = - \frac {G m _ {1} m _ {2}}{| \mathbf {x} _ {1} - \mathbf {x} _ {2} |}\tag{4.24}
$$

and a mutual electrostatic force, with 

$$
V _ {1 2} = V _ {2 1} = \frac {q _ {1} q _ {2}}{4 \pi \epsilon_ {0} | \mathbf {x} _ {1} - \mathbf {x} _ {2} |}.\tag{4.25}
$$

Both are conservative forces. 

Here's a curious fact: if you take a bunch of particles with masses $m_a$ and charges $q_a = \sqrt{4\pi \epsilon_0 G} m_a$ , then the attractive force of gravity exactly cancels the repulsive electromagnetic force and and they have potential $V(\mathbf{x}_a) = 0$ for any position $\mathbf{x}_a$ . This means that such particles will happily sit at any position. Sadly, no such objects are known in nature! 

## In Praise of Conservation Laws

We have introduced three conservation laws so far in this chapter: momentum, angular momentum, and energy. The first two at least appear rather trivial mathematically. For example, (4.10) tells us that if you apply an external force, then the total momentum of a system will change. And if you don't apply an external force, then the total momentum of the 

system won't change. And that's all there is to conservation of momentum. 

In fact, there's something much deeper going on. Each of the conservation laws follows from the symmetries of space and time. This is the result of Noether's theorem that we will meet in Chapter 7. Here we give a brief taster: 

- Conservation of momentum follows from the translational invariance of space. In our formulation, we saw that momentum is conserved if the total external force vanishes. But without an external force pushing the particles one way or another, any point in space is just as good as any other. So why would the particle speed up to go over there when here is just as good? 

- Conservation of angular momentum follows from the rotational invariance of space. We saw hints of this in Chapter 2 where we showed that an external potential that is central, and therefore rotationally invariant, exerts no torque. 

- Conservation of energy is more subtle. This follows from invariance of the laws of physics under time translations. This means you should get the same result no matter whether you do your experiment yesterday or tomorrow. It’s somewhat less intuitive that this gives rise to the quantity that we call energy. But it’s true nonetheless. 

All of this will be fleshed out in much greater detail in Chapter 7. 

## 4.2 Collisions

Take two particles and bounce them off each other. What happens? 

The proper way to deal with these kinds of problems is to understand the interaction potential $V(r)$ between the two particles and solve for the subsequent motion. This we'll do in Section 5.6. But that's rather involved and, for many problems, can be overkill. If you collide two billiard balls, you don't want to be thinking about the inter-atomic forces at play between them. You just want to know what happens after they go "clink". 

Often we can make progress by just considering the basics. Here, the basics mean conservation of energy and conservation of momentum. Collisions in which both kinetic energy and momentum are conserved are called elastic. 

Our discussion here will be brief. We'll cover just enough to prepare ourselves for two future topics. The first of these is in the context of special relativity, where the kinematics of collisions is crucial to understand experiments in particle physics. We'll discuss this in Chapter 11. The second is a gloriously ridiculous result that we present in Section 4.2.2. 

We start with a particularly simple example. Consider a particle travelling with velocity u that collides with a second, stationary particle of the same mass. What happens? After the collision, the two particles have velocities $v_{1}$ and $v_{2}$ . Even without knowing anything else about the interaction, there is a pleasing, simple result that we can derive. Conservation of energy tells us 

$$
\frac {1}{2} m \mathbf {u} ^ {2} = \frac {1}{2} m \mathbf {v} _ {1} ^ {2} + \frac {1}{2} m \mathbf {v} _ {2} ^ {2}\tag{4.26}
$$

while the conservation of momentum reads 

$$
m \mathbf {u} = m \mathbf {v} _ {1} + m \mathbf {v} _ {2}.\tag{4.27}
$$

Squaring this second equation, and comparing to the first, we learn that the cross-term on the right-hand side must vanish. This tells us that 

$$
\mathbf {v} _ {1} \cdot \mathbf {v} _ {2} = 0.\tag{4.28}
$$

In other words, either one of the particles is stationary, or the two particles scatter at right-angles. 

Although the conservation of energy and momentum gives us some information about the collision, it is not enough to uniquely determine the final outcome. It's easy to see why: we have six unknowns in the two velocities $\mathbf{v}_1$ and $\mathbf{v}_2$ , but just four equations in (4.27) and (4.28). This is the usual situation in three dimensions where conservation laws alone are not sufficient to tell us what happens. 

## 4.2.1 Bouncing Balls

We're in a better situation in one dimension. Now there are two conservation laws – one for energy and one for momentum – and typically two unknowns. So we expect that conservation laws are sufficient to tell us everything that we want to know. 

Here's a simple example that illustrates this. Place a small ball of mass $m$ on top of a larger ball of mass $M$ . Then drop them both so that they hit the floor with speed $u$ . How fast does the smaller ball fly back up? 

It's best to think of the small ball as very slightly separated from the larger one. Assuming all collisions are elastic, the big ball then hits the ground first and bounces back up with the same speed $u$ , whereupon it immediately collides with the small ball. After this collision, we'll call the velocity of the small ball $v$ and the velocity of the large ball $V$ . 

Conservation of energy and momentum tell us 

$$
m u ^ {2} + M u ^ {2} = m v ^ {2} + M V ^ {2} \quad \text { and } \quad M u - m u = m v + M V.
$$

Note that we've measured velocity upwards, hence the initial momentum of the small ball is the only one to come with a minus sign. 

Just jumping in and solving these as simultaneous equations will lead to a quadratic and some messy algebra. There's a slightly slicker way to go about things. We write the two equations as 

$$
\begin{array}{l} M (V - u) (V + u) = m (u - v) (u + v) \\ \text { and } \quad M (u - V) = m (v + u)  . \end{array}\tag{4.30}
$$

Dividing one by the other gives $V + u = v - u$ . We can now use this, together with momentum conservation, to eliminate V. We find 

$$
v = \frac {3 M - m}{M + m} u.\tag{4.31}
$$

You can try this at home with a tennis ball and basketball. But trust the maths. It's telling you that the speed v will be almost three times greater than u. This means that the kinetic energy, and therefore the height reached by the tennis ball, will be almost nine times greater. You have been warned! 

## 4.2.2 More Bouncing Balls and the Digits of $\pi$

Here's another example. The question seems a little arbitrary, but the answer is quite extraordinary. Consider the two balls shown in the figure. The rightmost ball has mass $m$ . The leftmost ball is much heavier: it has the rather strange mass 

$$
M = 1 6 \times 1 0 0 ^ {N} \times m\tag{4.32}
$$

where N is an integer. 

We give the heavy ball a small kick so it rolls to the right. It collides elastically with the light ball which then flies off towards the wall. The collision with the wall is also elastic and the light ball bounces off with the same speed it arrived at, heading back towards the heavy ball. The process keeps repeating: the light ball bounces off the heavy one, bounces off the wall, and returns to collide yet again with the heavy ball. Note that the total energy is conserved in all processes but the total momentum is not conserved in the collision with the wall. 

A priori, there are two possible outcomes of this. It may be that the heavy ball moves all the way to the right, ultimately bouncing off the light ball that is now trapped against the wall. Or, it may be that the light ball eventually collides enough times so that the heavy ball turns around and starts moving towards the left. 

Which of these two possibilities occurs will be decided by the dynamics. Below, we'll see that it's actually the latter scenario that takes place: the heavy ball does not reach the wall. The question that we want to ask is: how many times, $p(N)$ , does the heavy ball hit the lighter one before it turns around and starts heading in the opposite direction? 

The answer to this question is one of the most ridiculous things I've seen in physics. It is 

$$
p (N) - 1 = \text { The   first } N + 1 \text { digits   of } \pi .\tag{4.33}
$$

In other words, $p(0) - 1 = 3$ , $p(1) - 1 = 31$ , $p(2) - 1 = 314$ , 

$$
p (3) - 1 = 3 1 4 1 \text {   and   so   on.   }
$$

In case it's not obvious, let me explain why you should also find this result ridiculous. The number $\pi$ is, of course, ubiquitous in physics. But this is very different from the decimal expansion of the number. As the name suggests, the digits of $\pi$ in a decimal expansion have as much to do with biology as mathematics. But we subtly inserted the relevant biological fact in the original question by insisting that the mass of the big ball is $M = 16 \times 10^{2N} \times m$ . This seemingly innocuous factor of 10 will prove to be the reason that the expansion of $\pi$ comes out in base 10. 

Let's now try to prove this unlikely result. Let $u_{n}$ be the velocity of the heavy ball and $v_{n}$ be the velocity of the light ball after the $n^{\text{th}}$ collision between them. Conservation of energy and momentum tell us that 

$$
\begin{array}{l} {M u _ {n + 1} ^ {2} + m v _ {n + 1} ^ {2} = M u _ {n} ^ {2} + m v _ {n} ^ {2}} \\ {M u _ {n + 1} + m v _ {n + 1} = M u _ {n} - m v _ {n}.} \end{array}\tag{4.34}
$$

Rearranging reveals some nice algebraic simplifications. Despite the quadratic nature of the energy conservation equation, the relationship between the velocities before and after is actually linear. This follows by factorising the energy conservation equation in a way similar to $(4.30)$ . We find that 

$$
\binom{u _ {n + 1}}{v _ {n + 1}} = A \binom{u _ {n}}{v _ {n}}\tag{4.35}
$$

where the matrix A depends only on the ratio of masses which we denote as x = m/M and is given by 

$$
A = \frac {1}{1 + x} \left( \begin{array}{c c} 1 - x & - 2 x \\ 2 & 1 - x \end{array} \right)  .\tag{4.36}
$$

Since we start with only the heavy ball moving, we have $(u_{0}, v_{0}) = (u_{0}, 0)$ . The velocities after the $n^{th}$ collision between the balls are 

$$
\binom{u _ {n}}{v _ {n}} = A ^ {n} \binom{u _ {0}}{0}.\tag{4.37}
$$

The smart way to compute the matrix $A^{n}$ is to first diagonalise A. The eigenvalues of A are found to be $e^{\pm i\theta}$ where 

$$
\cos \theta = \frac {1 - x}{1 + x}.\tag{4.38}
$$

Using this, we can write 

$$
A ^ {n} = S \left( \begin{array}{c c} e ^ {i n \theta} & 0 \\ 0 & e ^ {- i n \theta} \end{array} \right) S ^ {- 1} \quad \text { with } S = \left( \begin{array}{c c} i \sqrt {x} & - i \sqrt {x} \\ 1 & 1 \end{array} \right)
$$

and the velocities after the $n^{th}$ collision are given by 

$$
\binom{u _ {n}}{v _ {n}} = \frac {u _ {0}}{\sqrt {x}} \binom{\sqrt {x} \cos n \theta}{\sin n \theta}.\tag{4.40}
$$

We want to know how many collisions, p, it takes before the heavy ball starts moving in the opposite direction. This occurs when $\cos n\theta < 0$ , which means that p must obey 

$$
(p - 1) \theta <   \frac {\pi}{2} \quad \mathrm{while} \quad p \theta > \frac {\pi}{2}.\tag{4.41}
$$

To get a feel for this, we'll make an approximation. Since $x = m / M \ll 1$ , we can expand $\cos \theta \approx 1 - \frac{1}{2}\theta^2 \approx 1 - 2x$ , which gives us $\theta \approx 2\sqrt{x}$ . Using our rather strange choice of mass, $x = 10^{-2N} / 16$ , so $\theta \approx 10^{-N} / 2$ . If the corrections to this approximation are unimportant, the number of collisions $p$ is the largest integer such that $(p - 1) \times 10^{-N} < \pi$ while $p \times 10^{-N} > \pi$ . The answer is 

$$
p (N) - 1 = [ 1 0 ^ {N} \pi ]\tag{4.42}
$$

which means the integer part of $10^{N}\pi$ . This is the same thing as the first $N+1$ digits of $\pi$ . 

Finally, we should check whether the approximations that we made above are valid. Is it possible that the higher-order terms that we neglected can change the answer? The answer is: no one knows! It turns out that if, after the first $N + 1$ digits of $\pi$ , the next N digits are all 9s, then the number 

$p(N) - 1$ doesn't necessarily give the first $N + 1$ digits, but might be one greater! My number theorist friends tell me that no one knows whether or not $\pi$ has this property. 

## 4.3 Variable Mass Problems

So far in this book, we've considered situations in which the mass $m$ of the particle is constant. Here we will discuss two scenarios in which the mass changes. Both are allegories for life. The first of these scenarios is where things fall apart; the second where we pick up baggage on our journey. 

Recall from Chapter 1 that the correct version of Newton's second law is 

$$
\mathbf {F} = \dot {\mathbf {p}}\tag{4.43}
$$

where $p = m \dot{x}$ is the momentum. When the mass of the object is changing, so $m = m(t)$ , you might think that you just plug this into (4.43) to get “ $d(mv)/dt = F$ ”. In fact, this isn’t quite right. The equation (4.43) refers to the momentum of the entire system, while in the scenarios we consider here the mass is just transferred from one part of the system to another. All of which means that we have to think more carefully about what’s going on. 

## 4.3.1 Rockets: Things Fall Apart

A rocket moves in a straight line with velocity $v(t)$ . The mass of the rocket, $m(t)$ , changes with time because it propels itself forward by spitting out fuel behind. Suppose that the fuel is ejected at a speed u relative to the rocket. Our goal is to figure out how the speed of the rocket changes over time. 

To proceed, it's best to go back to first principles and work infinitesimally. At time $t$ , the momentum of the rocket is 

$$
p (t) = m (t) v (t).\tag{4.44}
$$

After a short interval $\delta t$ , this momentum is split between the momentum of the rocket and the momentum of the recently ejected fuel, as shown in Figure 4.1, 

$$
p (t + \delta t) = p _ {\mathrm{rocket}} (t + \delta t) + p _ {\mathrm{fuel}} (t + \delta t).\tag{4.45}
$$

The momentum of the rocket at this later time is given by 

$$
\begin{array}{r l} p _ {\mathrm{rocket}} (t + \delta t) & = m (t + \delta t) v (t + \delta t) \\ & \approx \left(m (t) + \frac {d m}{d t} \delta t\right) \left(v (t) + \frac {d v}{d t} \delta t\right) \\ & \approx m (t) v (t) + \left(v \frac {d m}{d t} + m \frac {d v}{d t}\right) \delta t + \mathcal {O} (\delta t ^ {2}) \end{array}
$$

where we've Taylor expanded the mass and velocity and kept terms up to order $\delta t$ . Similarly, the momentum of the fuel ejected between time $t$ and $t + \delta t$ is 

$$
\begin{array}{r} p _ {\mathrm{fuel}} (t + \delta t) = [ m (t) - m (t + \delta t) ] [ v (t) - u ] \\ \approx - \frac {d m}{d t} \delta t [ v (t) - u ] + \mathcal {O} (\delta t ^ {2}). \end{array}\tag{4.47}
$$

Notice that the speed of the fuel is $v - u$ ; this is because the fuel has speed $u$ relative to the rocket. In fact, there's a small subtlety here. Does the fuel travel at velocity $v(t) - u$ or $v(t + \delta t) - u$ or some average of the two? In fact, it doesn't matter. The difference only shows up at order $\delta t^2$ and doesn't affect our final answer. Adding together these two momenta, we have the result 

$$
p (t + \delta t) = p (t) + \left(m (t) \frac {d v}{d t} + u \frac {d m}{d t}\right) \delta t + \mathcal {O} (\delta t ^ {2}).\tag{4.}
$$

At this stage, we can use Newton's second law in the form (4.43) which, using the definition of the derivative, is given by 

$$
\frac {p (t + \delta t) - p (t)}{\delta t} = F\tag{4.49}
$$

where F is the external force on the rocket. Comparing this to $(4.48)$ , we arrive at: 

$$
m (t) \frac {d v}{d t} + u \frac {d m}{d t} = F.\tag{4.50}
$$

This is the Tsiolkovsky rocket equation. (In the US, it is known as the arugula equation.) Despite its simplicity, apparently this equation was first derived only in 1903. 

Fig. 4.1 On the left, the rocket at time t. On the right, the rocket and its ejected fuel, a time $\delta t$ later. 

## An Example: A Free Rocket in Space

Let's solve the rocket equation when there is no external force, $F = 0$ . We can write it as 

$$
{\frac {d v}{d t}} = - {\frac {u}{m}} {\frac {d m}{d t}}\tag{4.51}
$$

which can be trivially integrated to give 

$$
v (t) = v _ {0} + u \log \left(\frac {m _ {0}}{m (t)}\right).\tag{4.52}
$$

Here we have chosen the rocket to have speed $v_{0}$ when its mass is $m_{0}$ . We see that burning rocket fuel will only increase your speed logarithmically. If we further assume that the rocket burns fuel at a constant rate, 

$$
{\frac {d m}{d t}} = - \alpha\tag{4.53}
$$

( 

then we have $m(t) = m_{0} - \alpha t$ . Note that $\alpha > 0$ means that dm/dt < 0 as it should be. In this case, the velocity of the rocket is 

$$
v (t) = v _ {0} - u \log \left(1 - \frac {\alpha t}{m _ {0}}\right).\tag{4.54}
$$

This solution only makes sense for times $t < m_{0}/\alpha$ . This is because at time $t = m_{0}/\alpha$ , all of the fuel runs out which, in our somewhat silly model, means that the rocket has disappeared entirely. For these times $t < m_{0}/\alpha$ , we can integrate once more to get the position 

$$
x = v _ {0} t + \frac {u m _ {0}}{\alpha} \left[ \left(1 - \frac {\alpha t}{m _ {0}}\right) \log \left(1 - \frac {\alpha t}{m _ {0}}\right) + \frac {\alpha t}{m _ {0}} \right].
$$

assuming $x(0)=0$ . 

## Another Example: A Rocket with Linear Drag

Here's a slightly more involved example. The initial mass of the rocket is $m_0$ and we will still burn fuel at a constant rate, so $\dot{m} = -\alpha$ . But now the rocket is subject to linear drag, $F = -\gamma v$ , presumably because it has encountered some sticky alien intergalactic golden syrup or something. If the rocket starts from rest, how fast is it going after it has burned one half of its mass as fuel? 

With linear drag, the rocket equation $(4.50)$ becomes 

$$
m \dot {v} + u \dot {m} = - \gamma v.\tag{4.56}
$$

We can already get a feel for what's going on by looking at this equation. Since $\dot{m} = -\alpha$ , rearranging we get 

$$
m \dot {v} = \alpha u - \gamma v.\tag{4.57}
$$

This means that we will continue to accelerate through the sticky alien goo if we're travelling slowly and burning fuel fast enough so that $\alpha u > \gamma v$ . But as our speed approaches $v = \alpha u / \gamma$ , the acceleration reduces and we expect this to be the limiting velocity. However, if we were travelling too fast to begin with, so $\gamma v > \alpha u$ , then we will slow down until we again hit the limiting speed $v = \alpha u / \gamma$ . 

Let's now look in more detail at the solution. We could solve the rocket equation (4.56) to get $v(t)$ , but since the question we posed doesn't ask about velocity as a function of time, we'll be much better off thinking of velocity as a function of mass: $v = v(m)$ . Then 

$$
\dot {v} = \frac {d v}{d m} \dot {m} = - \alpha \frac {d v}{d m}.\tag{4.58}
$$

Using this, the rocket equation becomes 

$$
- \alpha m \frac {d v}{d m} - \alpha u = - \gamma v.\tag{4.59}
$$

This can be happily integrated using a few basic steps, 

$$
\frac {d v}{d m} = \frac {\gamma v - \alpha u}{\alpha m} \quad \Longrightarrow \quad \int \frac {d v}{\gamma v - \alpha u} = \int \frac {d m}{\alpha m}.\tag{4}
$$

Before integrating, we need to decide whether the denominator on the left-hand side is positive or negative (because integrating will give us a log and the argument of log has to be positive). We stated above that the rocket starts from rest, so we have $\gamma v < \alpha u$ meaning that the left-hand side is negative. Integrating then gives 

$$
\frac {1}{\gamma} \log \left(\frac {\alpha u - \gamma v}{\alpha u}\right) = \frac {1}{\alpha} \log \left(\frac {m}{m _ {0}}\right).\tag{4.61}
$$

Here, the denominators that we've introduced in the arguments of both logs are there on dimensional grounds. (Remember that the argument of log has to be dimensionless.) The factor of $m_0$ is an integration constant; the factor of $\alpha u$ tells us that the velocity vanishes when $m = m_0$ . Rearranging, we get the final answer 

$$
v = \frac {\alpha u}{\gamma} \left(1 - \left(\frac {m}{m _ {0}}\right) ^ {\gamma / \alpha}\right).\tag{4.62}
$$

We see that the behaviour is in agreement with our discussion after $(4.56)$ . As m decreases, v increases to towards the limiting velocity $v = \alpha u / \gamma$ . But it never reaches this velocity until all the mass of the rocket is burnt as fuel. In particular, we can answer the question posed at the beginning simply by setting $m = m_{0}/2$ . 

## 4.3.2 Avalanches: Stuff Gathering Other Stuff

For completeness, we now discuss a situation where the mass increases. This situation is an avalanche. I should confess up front that avalanches are poorly understood and the model below holds no claim to realism. 

We denote the mass of snow moving in the avalanche as $m(t)$ . We'll further assume that all the snow moving down the hill does so at the same speed $v(t)$ , picking up extra snow as it goes. We can use the rocket equation (4.50), with $u = v$ since the snow lying on the ground has speed $v$ relative to the avalanche. Ignoring friction, but including the force due to gravity on the moving snow, the rocket equation becomes 

$$
m \frac {d v}{d t} + v \frac {d m}{d t} = m g \sin \theta\tag{4.63}
$$

where $\theta$ is the angle that the slope makes with the ground. Because the snow lying on the ground had no previous momentum, we have 

$$
\frac {d}{d t} (m v) = m g \sin \theta .\tag{4.64}
$$

Suppose that the snow has density $\rho$ and cross-sectional area A (i.e. the height of the snow times the width of the mountain). Moreover, assume that all of the snow is picked up as the avalanche passes over. After the avalanche has moved a distance x down the slope, it has picked up a mass $m(t) = \rho Ax(t)$ . The equation of motion is 

$$
\frac {d}{d t} (\rho A x v) = \rho A x g \sin \theta .\tag{4.65}
$$

At this point, it is best to think of velocity as a function of position: $v = v(x)$ . Then we can write d/dt = v d/dx so 

$$
v \frac {d}{d x} (x v) = x g \sin \theta .\tag{4.66}
$$

This is again easily integrated in a few standard manoeuvres. If we first multiply both sides by x, we have 

$$
x v \frac {d}{d x} (x v) = x ^ {2} g \sin \theta \quad \Longrightarrow \quad \frac {1}{2} (x v) ^ {2} = \frac {1}{3} x ^ {3} g \sin \theta
$$

where we've set the integration constant to zero so that $v = 0$ when we start at $x = 0$ . Rearranging now gives the speed as a function of position, 

$$
v = \sqrt {\frac {2}{3} x g \sin \theta}.\tag{4.67}
$$

If we integrate this once more, we get 

$$
x = \frac {1}{6} g t ^ {2} \sin \theta\tag{4.68}
$$

where we again set the integration constant to zero by assuming that $x = 0$ when $t = 0$ . It's worth mentioning that this is smaller by a factor of 3 compared to the result we get for an object that doesn't gather mass as it goes which, taken at face value, suggests that you should be able to outrun an avalanche, at least if you didn't have to worry about friction. 

Personally, I wouldn't bet my life on it. 

# 5 The Two-Body Problem

Solving the dynamics of $N \geq 3$ mutually interacting particles is hard. Here “hard” means that no one knows how to do it unless the forces between the particles are of a very special type, like harmonic oscillators. 

In contrast, the dynamics of N = 2 interacting particles, known as the two-body problem, is eminently solvable. The purpose of this chapter is to solve it. 

We will restrict our attention to potentials of the form $V_{12} = V_{21} = V$ , such that 

$$
V = V \big (| \mathbf {x} _ {1} - \mathbf {x} _ {2} | \big)  .\tag{5.1}
$$

As we saw in the last chapter, this ensures that Newton's third law is obeyed. We will first derive a number of results about the general two-body problem but, ultimately, we will focus on a very special force with potential $V \sim 1 / r$ with $r$ the separation between particles. This, of course, is the potential relevant for both Newton's gravitational force and the Coulomb force of electrostatics. Solving for the motion of particles in such a potential encapsulates two of the most important problems in classical physics, namely: 

- The Kepler Problem: what is the motion of a planet around a star? 

- Rutherford Scattering: what happens when you throw a charged particle at an atom? 

We will present the solutions to both these problems. Along the way, we will also see that the two-body problem in general, and the potential $V \sim 1/|\mathbf{x}_{1} - \mathbf{x}_{2}|$ in particular, have a number of pleasing mathematical properties. 

## 5.1 Setting the Scene

In this section, we will derive a number of preliminary results that will put us on the path to solving the general two-body problem. 

## 5.1.1 The Two-Body Problem is Really a One-Body Problem

Our first step is a significant one. We will see that the case of two particles actually reduces to the kind of one-particle problem that we met in Chapter 2. 

We have already met the definition of the centre of mass 

$$
M \mathbf {R} = m _ {1} \mathbf {x} _ {1} + m _ {2} \mathbf {x} _ {2}.\tag{5.2}
$$

We also define the relative separation 

$$
\mathbf {r} = \mathbf {x} _ {1} - \mathbf {x} _ {2}.\tag{5.3}
$$

Given a potential of the form $(5.1)$ , the equations of motion are 

$$
m _ {1} \ddot {\mathbf {x}} _ {1} = - \frac {\partial V}{\partial \mathbf {x} _ {1}} = - \frac {\partial V}{\partial r} \hat {\mathbf {r}} \quad \mathrm{and} \quad m _ {2} \ddot {\mathbf {x}} _ {2} = - \frac {\partial V}{\partial \mathbf {x} _ {2}} = + \frac {\partial V}{\partial r} \hat {\mathbf {r}}.
$$

If we rewrite these in terms of the centre of mass R and the separation r, we find that something nice happens. First, we have $m\ddot{R}=0$ , so that the centre of mass travels with constant velocity. This reaffirms a result that we saw in Chapter 4: if there is no external force, then the total momentum of the system is conserved. For us, it simply means that we can ignore the centre of mass coordinate. 

The relative separation is more interesting. We have 

$$
\ddot {\mathbf {r}} = \ddot {\mathbf {x}} _ {1} - \ddot {\mathbf {x}} _ {2} = - \left(\frac {1}{m _ {1}} + \frac {1}{m _ {2}}\right) \frac {\partial V}{\partial r} \hat {\mathbf {r}}.\tag{5.5}
$$

We write this as 

$$
\mu \ddot {\mathbf {r}} = - \nabla V\tag{5.6}
$$

where we have defined the reduced mass 

$$
\mu = \frac {m _ {1} m _ {2}}{m _ {1} + m _ {2}}.\tag{5.7}
$$

But $(5.6)$ is exactly the kind of single-particle problem that we looked at in Chapter 2. The only novelty is that the mass m gets replaced with the reduced mass $\mu$ . 

In what follows, we'll sometimes employ the language of one-particle mechanics and talk about the “the particle with mass $\mu$ and position $\mathbf{r}$ ”. 

That's really shorthand for the positions of two particles, with relative separation $\mathbf{r}$ and reduced mass $\mu$ . 

In the limit where one of the particles involved is very heavy, say $m_{2} \gg m_{1}$ , then the reduced mass is approximately equal to the lighter of the two: $\mu \approx m_{1}$ . In this case, the heavy object is essentially fixed, with the lighter object orbiting around it. This was the approximation that we were implicitly invoking in Chapter 2 where we referred to the lighter particle as a “test particle”. It’s a very good approximation for many cases of interest. For example, the centre of mass of the Earth and Sun is very close to the centre of the Sun and it makes sense to think of the Sun as fixed, and the Earth moving in its gravitational field. Even for the Earth and Moon, the centre of mass lies 1000 miles below the surface of the Earth. 

## 5.2 Conservation of Angular Momentum

The kind of two-body potential that we're considering takes the form 

$$
V (| \mathbf {x} _ {1} - \mathbf {x} _ {2} |) = V (r).\tag{5.8}
$$

But these are precisely the central potentials that we previously met in Section 2.2.3. Recall that central potentials have the special property that angular momentum, 

$$
\mathbf {L} = \mu \mathbf {r} \times \dot {\mathbf {r}}\tag{5.9}
$$

is conserved. This follows from taking the time derivative 

$$
\frac {d \mathbf {L}}{d t} = \mu \mathbf {r} \times \ddot {\mathbf {r}} = - \mathbf {r} \times \nabla V\tag{5.10}
$$

and noting that, for a central potential $V = V(r)$ , the gradient $\nabla V$ is parallel to r. (This was shown in Section 2.2.3.) 

The conservation of angular momentum has an important consequence for our two-body problem: all motion takes place in a plane. This follows because L is a fixed, unchanging vector which, by construction, obeys 

$$
\mathbf {L} \cdot \mathbf {r} = 0.\tag{5.11}
$$

So the relative position of the two particles always lies in a plane perpendicular to L. By the same argument, $L \cdot \dot{r} = 0$ so the relative velocity of the particles also lies in the same plane. In this way the three-dimensional dynamics is reduced to dynamics on a plane. 

## 5.2.1 Polar Coordinates in the Plane

We've learned that the motion lies in a plane. It will turn out to be much easier if we work with polar coordinates in the plane rather than Cartesian coordinates. For this reason, we take a brief detour to explain some relevant aspects of polar coordinates. 

To start, we rotate our coordinate system so that the angular momentum points in the z-direction and all motion takes place in the $(x, y)$ -plane. We then define the usual polar coordinates 

$$
x = r \cos \theta \quad \text { and } \quad y = r \sin \theta .\tag{5.12}
$$

Our goal is to express both the velocity and acceleration in polar coordinates. We introduce two unit vectors, $\hat{r}$ and $\hat{\theta}$ in the direction of increasing r and $\theta$ respectively, as shown in the diagram. Written in Cartesian form, these vectors are 

$$
\hat {\mathbf {r}} = \binom{\cos \theta}{\sin \theta} \quad \text { and } \quad \hat {\boldsymbol {\theta}} = \binom{- \sin \theta}{\cos \theta}  .\tag{5.13}
$$

Note that we've had a subtle change of notation, since $\hat{\mathbf{r}}$ is now a 2d vector, rather than the 3d vector that appeared in, say, (5.5). This is appropriate because the motion lies in the a plane. 

The vectors $\hat{\mathbf{r}}$ and $\hat{\boldsymbol{\theta}}$ form an orthornormal basis at every point in the plane. But the basis itself depends on the point $\mathbf{r} = (x, y)$ at which we sit. Or, more specifically, the basis depends on the angle $\theta$ : moving in the radial direction doesn't change the basis, but moving in the angular direction does. We have 

$$
\frac {d \hat {\mathbf {r}}}{d \theta} = \binom{- \sin \theta}{\cos \theta} = \hat {\boldsymbol {\theta}} \quad \text { and } \quad \frac {d \hat {\boldsymbol {\theta}}}{d \theta} = \binom{- \cos \theta}{- \sin \theta} = - \hat {\mathbf {r}} .
$$

This means that if the particle moves in a way such that $\theta$ changes with time, then the basis vectors themselves will also change with time. This has an implication for the velocity when expressed in polar coordinates. To see this, we first write the position of the particle as the simple, if somewhat ugly, equation 

$$
\mathbf {r} = r \hat {\mathbf {r}}.\tag{5.15}
$$

From this we can compute the velocity, remembering that both r and the basis vector $\hat{r}$ can change with time. We get 

$$
\dot {\mathbf {r}} = \dot {r} \hat {\mathbf {r}} + r \frac {d \hat {\mathbf {r}}}{d \theta} \dot {\theta} = \dot {r} \hat {\mathbf {r}} + r \dot {\theta} \hat {\boldsymbol {\theta}}.\tag{5.16}
$$

The second term in the above expression arises because the basis vectors change with time, and is proportional to the angular velocity, $\dot{\theta}$ . 

(Sometimes this is referred to as the angular speed, even though it can be positive or negative, with the term “angular velocity” reserved for a 3d vector that we will meet in Chapter 9.) 

Differentiating once more gives us the expression for acceleration in polar coordinates 

$$
\begin{array}{r} \ddot {\mathbf {r}} = \ddot {r} \hat {\mathbf {r}} + \dot {r} \frac {d \hat {\mathbf {r}}}{d \theta} \dot {\theta} + \dot {r} \dot {\theta} \hat {\pmb {\theta}} + r \ddot {\theta} \hat {\pmb {\theta}} + r \dot {\theta} \frac {d \hat {\pmb {\theta}}}{d \theta} \dot {\theta} \\ = (\ddot {r} - r \dot {\theta} ^ {2}) \hat {\mathbf {r}} + (r \ddot {\theta} + 2 \dot {r} \dot {\theta}) \hat {\pmb {\theta}}. \end{array}\tag{5.17}
$$

The two expressions $(5.16)$ and $(5.17)$ will be important in what follows. 

## An Example: Circular Motion

We can illustrate these expressions with something familiar: circular motion. A particle moving in a circle has $\dot{r} = 0$ . If the particle travels with constant angular velocity $\dot{\theta} = \omega$ then, from (5.16), the velocity in the plane is 

$$
\dot {\mathbf {r}} = r \omega \hat {\pmb {\theta}}.\tag{5.18}
$$

The speed in the plane is then $v = |\dot{r}| = r\omega$ . Similarly, from (5.17), the acceleration in the plane is 

$$
\ddot {\bf r} = - r \omega^ {2} \hat {\bf r}.\tag{5.19}
$$

The magnitude of the acceleration is $a = |\ddot{r}| = r\omega^{2} = v^{2}/r$ . This means that, if we want a particle to travel in a circle, then we need to supply a force $F = mv^{2}/r$ towards the origin. This is known as a centripetal force. 

## 5.3 The Effective Potential

We can now return to our central force problem, armed with polar coordinates. We know that the particle motion takes place in a plane, and we choose to parameterise this by the polar coordinates r and $\theta$ . From our expression (5.17) for acceleration in polar coordinates, the equation of motion (5.6) becomes 

$$
\mu (\ddot {r} - r \dot {\theta} ^ {2}) \hat {\mathbf {r}} + \mu (r \ddot {\theta} + 2 \dot {r} \dot {\theta}) \hat {\pmb {\theta}} = - \frac {d V}{d r} \hat {\mathbf {r}}.\tag{5.20}
$$

The $\hat{\theta}$ component of this equation is particularly simple. It reads 

$$
r \ddot {\theta} + 2 \dot {r} \dot {\theta} = 0 \quad \Longrightarrow \quad \frac {1}{r} \frac {d}{d t} \left(r ^ {2} \dot {\theta}\right) = 0.\tag{5.21}
$$

At first, it looks as if we've found a new conserved quantity, since this equation is telling us that 

$$
l = r ^ {2} \dot {\theta}\tag{5.22}
$$

does not change with time. However, we shouldn't get too excited. This is something that we already know. To see this, let's look again at the angular momentum $\mathbf{L}$ . We already used the fact that the direction of $\mathbf{L}$ is conserved, restricting motion to the plane. But what about the magnitude of $\mathbf{L}$ ? Using (5.16), we have 

$$
\mathbf {L} = \mu \mathbf {r} \times \dot {\mathbf {r}} = \mu r \hat {\mathbf {r}} \times (\dot {r} \hat {\mathbf {r}} + r \dot {\theta} \hat {\boldsymbol {\theta}}) = \mu r ^ {2} \dot {\theta} (\hat {\mathbf {r}} \times \hat {\boldsymbol {\theta}}).\tag{5.}
$$

Since $\hat{r}$ and $\hat{\theta}$ are orthogonal unit vectors, $\hat{r} \times \hat{\theta}$ is also a unit vector, pointing out of the plane. The magnitude of the angular momentum vector is therefore 

$$
| \mathbf {L} | = \mu l.\tag{5.24}
$$

This means that l, given in $(5.22)$ , is identified as the angular momentum per unit mass, although we will often be lazy and refer to l simply as the angular momentum. 

Next, we look at the $\hat{r}$ component of the equation of motion (5.20). It is 

$$
\mu (\ddot {r} - r \dot {\theta} ^ {2}) = - \frac {d V}{d r}.\tag{5.25}
$$

Using the fact that $l = r^{2}\dot{\theta}$ is conserved, we can write this as 

$$
\mu \ddot {r} = - \frac {d V}{d r} + \frac {\mu l ^ {2}}{r ^ {3}}.\tag{5.26}
$$

It's worth pausing to reflect on what's happened here. We started with two particles, each moving in three dimensions. This means that the system was described by six coordinates, $\mathbf{x}_1$ and $\mathbf{x}_2$ . We used momentum 

conservation to reduce this to a problem of just three coordinates, the relative separation $r = x_{1} - x_{2}$ . We then used the direction of the angular momentum to reduce it to a two-dimensional problem, and the magnitude of the angular momentum to reduce it to a one-dimensional problem (5.26), involving only the variable r. 

This should give you some idea of how important conserved quantities are when it comes to solving anything. Roughly speaking, this is also why it's not usually possible to solve problems with many particles when they are mutually interacting. When we have $N \geq 3$ particles, each with a mutual interaction potential, we typically don't get any more conserved quantities beyond those that we've seen for the two-body problem. Without additional constraints, the motion becomes much more complicated. Even the simplest, the so-called three-body problem, exhibits chaotic behaviour. 

Returning to our main storyline, we can write $(5.26)$ in the suggestive form 

$$
\mu \ddot {r} = - \frac {d V _ {\mathrm{eff}}}{d r}\tag{5.27}
$$

where $V_{\mathrm{eff}}(r)$ is called the effective potential and is given by 

$$
V _ {\mathrm{eff}} (r) = V (r) + \frac {\mu l ^ {2}}{2 r ^ {2}}.\tag{5.28}
$$

The extra term, $\mu l^{2}/2r^{2}$ is called the angular momentum barrier (also known as the centrifugal barrier). As you can see, this extra term diverges as $r \rightarrow 0$ and the two particles get close. 

To get more intuition for the effective potential, we can look at the total energy of the system. The same calculation that previously led to $(4.19)$ shows that the kinetic energy of the two particles nicely decomposes into a centre of mass piece and a separation piece 

$$
\begin{array}{r} E = \frac {1}{2} m _ {1} \dot {\mathbf {x}} _ {1} \cdot \dot {\mathbf {x}} _ {1} + \frac {1}{2} m _ {2} \dot {\mathbf {x}} _ {2} \cdot \dot {\mathbf {x}} _ {2} + V (| \mathbf {x} _ {1} - \mathbf {x} _ {2} |) \\ = \frac {1}{2} (m _ {1} + m _ {2}) \dot {\mathbf {R}} ^ {2} + \frac {1}{2} \mu \dot {\mathbf {r}} ^ {2} + V (r). \end{array}\tag{5.29}
$$

We'll ignore the kinetic energy for the centre of mass since that decouples from the interesting dynamics. If we evaluate the remaining energy for some fixed angular momentum $\mathbf{L}$ then, using (5.16) and the fact that the particle moves only in the plane, we have 

$$
\begin{array}{r l} & E = \frac {1}{2} \mu \dot {r} ^ {2} + \frac {1}{2} \mu r ^ {2} \dot {\theta} ^ {2} + V (r) \\ & \quad = \frac {1}{2} \mu \dot {r} ^ {2} + \frac {\mu l ^ {2}}{2 r ^ {2}} + V (r) \\ & \quad = \frac {1}{2} \mu \dot {r} ^ {2} + V _ {\mathrm{eff}} (r). \end{array}\tag{5.30}
$$

We now clearly see that the extra term in the effective potential, the angular momentum barrier, has its origin as the angular part of the kinetic energy. As the particles get close, the conservation of angular momentum means that their angular velocity must increase. And this has the effect of increasing the kinetic energy. We include this “angular kinetic energy” in the effective potential, where it prohibits the particles from getting too close, now by paying a heavy price in “effective potential energy”. 

## 5.3.1 Getting a Feel for Orbits

In writing our equation of motion in the form (5.27), we've succeeded in reducing our original 3d problem to a 1d problem in the radial coordinate $r$ . But we've already seen how to solve 1d problems of this kind in Section 2.1. In particular, we saw that we can understand qualitative aspects of one-dimensional motion simply by plotting the potential energy and thinking about how the particle rolls about. Here we do the same thing for the effective potential. 

We can play this game for any central potential $V(r)$ , but we will focus our attention on the most important 

$$
V (r) = - \frac {\mu k}{r}.\tag{5.31}
$$

The factor of $\mu$ in this expression is for convenience as it ensures that $\mu$ drops out of many subsequent equations. For the mutual gravitational interaction, we should take $k = Gm_{1}m_{2}/\mu = G(m_{1} + m_{2})$ . Meanwhile, for the Coulomb force we should take $k = -q_{1}q_{2}/4\pi\epsilon_{0}\mu$ . In both cases, the resulting inverse square law is attractive for k > 0 and repulsive for k < 0. The effective potential is 

$$
V _ {\mathrm{eff}} (r) = - \frac {\mu k}{r} + \frac {\mu l ^ {2}}{2 r ^ {2}}.\tag{5.32}
$$

This is plotted in Figure 5.1 for k > 0. From this potential, we can easily learn about the motion $r(t)$ in the radial direction. The tricky part is to superpose this with the angular velocity, $\dot{\theta} = l/r^{2}$ , which is fixed (as a function of r) by angular momentum conservation. In this way, we build up the full 3d picture of the particle's trajectory. 

Fig. 5.1 The effective potential arising from the attractive inverse square force law. 

The possible forms of the motion can be characterised by their energy E: 

- $E = E_{\mathrm{min}} = -\mu k^2 / 2l^2$ : Here the particle sits at the minimum of the effective potential, 

$$
r _ {\star} = \frac {l ^ {2}}{k}\tag{5.33}
$$

and stays there for all time. To picture the full 3d motion, we need to remember that the particle also has an angular velocity, given by $\dot{\theta} = l/r_{\star}^{2}$ . So although the particle has a fixed radial position, it is moving in the angular direction at a constant speed. In other words, the trajectory of the particle is a circular orbit about the origin. Notice that the position $r_{\star} = l^{2}/k$ of the minimum depends on the angular momentum l. The higher the angular momentum, the further away the minimum. If there is no angular momentum, and l = 0, then $V_{\mathrm{eff}}(r) = V(r)$ and the potential has no minimum. This is telling us the obvious fact that there is no way that r can be constant unless the particle is moving in the $\theta$ direction. In a similar vein, there is a relationship between the angular velocity $\dot{\theta}$ and the size of the orbit, $r_{\star}$ , which we get by eliminating l to find 

$$
\dot {\theta} ^ {2} = \frac {k}{r _ {\star} ^ {3}} .\tag{5.34}
$$

We'll come back to this relationship shortly when we discuss Kepler's laws of planetary motion. 

- $E_{\min} < E < 0$ : Here the particle sits in the dip of the effective potential, oscillating back and forth between two radial points. Again, because $\dot{\theta} \neq 0$ , the particle also has angular velocity in the plane. This describes an orbit in which the radial distance $r$ depends on time. Although it is not yet obvious, we will soon show that for $V = -\mu k / r$ , this orbit is an ellipse. 

The point on the orbit with the smallest value of r is called the periapsis. The point with the largest value is the apoapsis. Together, these two points are referred to as the apsides. In the case of motion around the Sun, the periapsis is called the perihelion and the apoapsis the aphelion. 

- $E > 0$ . Now the particle can escape to $r \to \infty$ . If you send it in with some velocity from infinity, then it navigates the dip, moves up towards the origin before reaching some minimum distance, and then rolls back out to infinity. We will see later that, for the $V = -\mu k / r$ potential, the resulting trajectory is a hyperbola. 

These three different classes of orbits are sketched in Figure 5.2. 

Fig. 5.2 Three different orbits depending on whether $E = E_{\min}$ (on the left) or $E_{\min} < E < 0$ (in the middle), or E > 0 (on the right). 

## 5.3.2 The Stability of Circular Orbits

Before we learn how to solve for general orbits, we first pause to ask some general questions. Given some potential $V(r)$ , we can ask: when do circular orbits exist? And when are they stable? 

The first question is easy. Circular orbits exist whenever there is a solution with $l \neq 0$ and $\dot{r} = 0$ for all time. The latter condition means that $\ddot{r} = 0$ which, in turn, requires 

$$
V _ {\mathrm{eff}} ^ {\prime} (r _ {\star}) = 0.\tag{5.35}
$$

In other words, circular orbits correspond to critical points, $r_{\star}$ , of the effective potential. 

The orbit is stable if small perturbations return us back to the critical point. This is the same kind of analysis that we did in Section 2.1.2: stability requires that we sit at the minimum of the effective potential. This usually translates to the requirement that 

$$
V _ {\mathrm{eff}} ^ {\prime \prime} (r _ {\star}) > 0.\tag{5.36}
$$

If this condition holds, small radial deviations from the circular orbit will oscillate about $r_{\star}$ with simple harmonic motion. 

Although the criterion for circular orbits is most elegantly expressed in terms of the effective potential, sometimes it's also useful to see what this translates to in terms of our original potential $V(r)$ . The critical point (5.35) sits at 

$$
V ^ {\prime} (r _ {\star}) = \frac {\mu l ^ {2}}{r _ {\star} ^ {3}} .\tag{5.37}
$$

A given critical point obeys (5.36), and so is stable, if 

$$
V ^ {\prime \prime} (r _ {\star}) + \frac {3 \mu l ^ {2}}{r _ {\star} ^ {4}} = V ^ {\prime \prime} (r _ {\star}) + \frac {3}{r _ {\star}} V ^ {\prime} (r _ {\star}) > 0.\tag{5.38}
$$

We can even go right back to basics and express this in terms of the magnitude of the force $F(r) = -V'(r)$ . A circular orbit is stable if $F'(r_{\star}) < -3F(r_{\star})/r_{\star}$ . 

## An Example: Power-Law Potentials

Let's look at this requirement for a power-law central potential of the form 

$$
V (r) = - \frac {\mu k}{r ^ {n}} \quad \text { with } n \geq 1.\tag{5.39}
$$

Clearly there are always circular orbits whenever k > 0, sitting at a radius $r_{\star}^{2-n} = l^{2}/nk$ . But for what powers of n are these circular orbits stable? 

By our criterion (5.38), stability requires 

$$
V ^ {\prime \prime} (r _ {\star}) + \frac {3}{r _ {\star}} V ^ {\prime} (r _ {\star}) = - \Bigl (n (n + 1) - 3 n \Bigr) \frac {\mu k}{r _ {\star} ^ {n + 2}} > 0.\tag{5}
$$

This holds only for $n < 2$ . We can easily see this pictorially in Figure 5.3 where we've plotted the effective potential for $n = 1$ and $n = 3$ . 

Fig. 5.3 The effective potential $V_{eff}$ for V = -1/r (on the left) and for $V = -1/r^{3}$ (on the right). 

Here's a curious fact: in a universe with $d$ spatial dimensions, the law of gravity would be $F \sim 1 / r^{d-1}$ corresponding to a potential energy $V \sim -1 / r^{d-2}$ . This means that in some alternative universe with $d \geq 4$ spatial dimensions, planetary orbits would not be stable. You're safe only in a $d = 3$ dimensional universe, like our own, or in a rather limiting $d = 2$ dimensional flatland universe. We should all take a moment to appreciate our good fortune. 

## 5.4 Orbits

In this section, we will look more closely at the orbits in a general central potential $V_{eff}$ . In some sense, the problem of understanding the radial motion $r(t)$ is essentially already solved because the energy is conserved. This means that we have 

$$
E = \frac {1}{2} \mu \dot {r} ^ {2} + V _ {\mathrm{eff}} (r)\tag{5.41}
$$

with E a constant of the motion. We can view this as a first order differential equation for r and, provided that we consider a period for which $\dot{r}$ has a constant sign, we can integrate to get 

$$
t = \pm \sqrt {\frac {\mu}{2}} \int^ {r} \frac {d r ^ {\prime}}{\sqrt {E - V _ {\mathrm{eff}} (r ^ {\prime})}}.\tag{5.42}
$$

There are a couple of things that are unsatisfactory with this approach. The first is the obvious one: we still have to do the actual integral and, except for a few very special choices of $V_{\mathrm{eff}}(r)$ , that turns out to be something of a pain. But there's a different, more conceptual issue. Even if we can do the integral, often the resulting $t(r)$ (or, after inverting, $r(t)$ ) isn't the most useful way of presenting the solution since we're still left with the challenge of combining it with the angular motion $\theta(t)$ to understand the full, two-dimensional motion of the particle. 

For these reasons, we take a slightly different, more global approach to the problem. We will try to get a handle on the full trajectory of the particle, rather than the position $r(t)$ at some given time. Mathematically, this means that we want to understand the shape of the orbit by computing $r(\theta)$ . 

To proceed, we'll need a little trick. It's trivial, but it turns out to make the resulting equations much simpler. We introduce the new coordinate 

$$
u = \frac {1}{r}.\tag{5.43}
$$

I wish I had a reason to motivate this trick. Unfortunately, I don't. You'll just have to trust me and we'll see that it helps. 

Now we try to write things in terms of $r(\theta)$ (or, more precisely, in terms of $u(\theta)$ ) rather than $r(t)$ . The velocity is 

$$
\frac {d r}{d t} = \frac {d r}{d \theta} \dot {\theta} = \frac {d r}{d \theta} \frac {l}{r ^ {2}} = - l \frac {d u}{d \theta}.\tag{5.44}
$$

Meanwhile, the acceleration is 

$$
\frac {d ^ {2} r}{d t ^ {2}} = \frac {d}{d t} \left(- l \frac {d u}{d \theta}\right) = - l \frac {d ^ {2} u}{d \theta^ {2}} \dot {\theta} = - l ^ {2} \frac {d ^ {2} u}{d \theta^ {2}} \frac {1}{r ^ {2}} = - l ^ {2} u ^ {2} \frac {d ^ {2} u}{d \theta^ {2}}.
$$

The equation of motion for the radial position, which we first derived back in $(5.26)$ , is 

$$
\mu \ddot {r} - \frac {\mu l ^ {2}}{r ^ {3}} = F (r)\tag{5.46}
$$

where we've reverted to expressing the right-hand side in terms of the magnitude of the force, $F(r) = -dV/dr$ . Using (5.45), and doing a little bit of algebra (basically dividing by $\mu l^2 u^2$ ), we get the second order differential equation 

$$
\frac {d ^ {2} u}{d \theta^ {2}} + u = - \frac {1}{\mu l ^ {2} u ^ {2}} F (1 / u).\tag{5.47}
$$

This is the orbit equation. Our goal is to solve this for $u(\theta)$ . If we want to subsequently figure out the time dependence, we can then extract it from the equation $\dot{\theta} = lu^{2}$ . 

## 5.4.1 The Kepler Problem

The Kepler problem is the name given to understanding planetary orbits about a star. It is named after the astronomer Johannes Kepler who, through many years of astronomical observation, uncovered the mathematical patterns evident in our solar system. We will describe Kepler's observations shortly. 

Once again, we focus on the potential that gives rise to the inverse-square law 

$$
V (r) = - \frac {\mu k}{r}\tag{5.48}
$$

For this potential, the orbit equation $(5.47)$ becomes very easy to solve. It is 

$$
\frac {d ^ {2} u}{d \theta^ {2}} + u = \frac {k}{l ^ {2}}.\tag{5.49}
$$

But this is just the equation for a harmonic oscillator, albeit with its centre displaced by $k/l^{2}$ . We can write the most general solution as 

$$
u = C \cos (\theta - \theta_ {0}) + \frac {k}{l ^ {2}}\tag{5.50}
$$

with $C \geq 0$ and $\theta_{0}$ integration constants. (You might be tempted instead to write $u = C \cos \theta + C' \sin \theta + k/l^{2}$ with C and $C'$ as integration constants. This is equivalent to our result above but, as we will now see, it's much more useful to use $\theta_{0}$ as the second integration constant.) 

At the point where the orbit is closest to the origin (the periapsis), u is largest. From our solution, we have $u_{\max} = C + k/l^{2}$ . We will choose to orient our polar coordinates so that the periapsis occurs at $\theta = 0$ . This choice means that we set $\theta_{0} = 0$ . In terms of our original variable r = 1/u, we then have the final expression for the orbit 

$$
r = \frac {r _ {0}}{e \cos \theta + 1}\tag{5.51}
$$

where 

$$
r _ {0} = \frac {l ^ {2}}{k} \quad \text { and } \quad e = \frac {C l ^ {2}}{k} .\tag{5.52}
$$

Notice that $r_{0}$ is fixed by the angular momentum, while the choice of e is now effectively the integration constant in the problem. We necessarily have $e \geq 0$ . 

It turns out that $(5.51)$ is a well-known equation in geometry: it describes a geometrical object called a conic section. These are the curves that you get if you intersect a cone with some plane. As we will now derive in some detail, the resulting curves – which, for us, are orbits – can be either ellipses (including circles as a special case), hyperbolae, or parabolae. Which curve we get is determined by the integration constant e which is called the eccentricity. In particular, it matters a lot whether e < 1 or $e \geq 1$ . We look at these in turn. 

## Ellipses: e < 1

For 0 < e < 1, the radial position is bounded in the interval 

$$
\frac {r _ {0}}{r} \in [ 1 - e, 1 + e ].\tag{5.53}
$$

We can convert (5.51) back to Cartesian coordinates, $x = r \cos \theta$ and $y = r \sin \theta$ , by writing 

$$
r = r _ {0} - e r \cos \theta \quad \Longrightarrow \quad x ^ {2} + y ^ {2} = (r _ {0} - e x) ^ {2}.\tag{5.54}
$$

Multiplying out the square, collecting terms, and rearranging allows us to write this equation as the equation of an ellipse 

$$
\frac {(x - x _ {c}) ^ {2}}{a ^ {2}} + \frac {y ^ {2}}{b ^ {2}} = 1\tag{5.55}
$$

with 

$$
x _ {c} = - \frac {e r _ {0}}{1 - e ^ {2}}, a ^ {2} = \frac {r _ {0} ^ {2}}{(1 - e ^ {2}) ^ {2}}, b ^ {2} = \frac {r _ {0} ^ {2}}{1 - e ^ {2}} <   a ^ {2}.
$$

The ellipse is shown in Figure 5.4. The two semi-axes have lengths a and b, while its centre is shifted from the origin by a distance $x = x_{c} < 0$ . This shift is important. The origin at r = 0 is the centre of attraction of the gravitational potential. 

Fig. 5.4 On the left, the elliptical orbit with the origin at a focus. On the right, the sum of the distances from the two foci to a point on the orbit is constant. 

In general, the origin should be thought of as the centre of mass of the two orbiting particles. But, as we mentioned previously, the centre of mass of the Earth and Sun system is essentially the same as the centre of the Sun. So it's appropriate to think of the origin as the location of the Sun as shown in the first picture in Figure 5.4. But this does not coincide with the centre of the elliptical orbit. Instead, the two differ by 

$$
| x _ {c} | = \frac {r _ {0} e}{1 - e ^ {2}} = e a.\tag{5.57}
$$

The point where the Sun sits has special geometric significance: it is called the focus of the ellipse. In fact, it is one of two foci, one denoted O and the other $O'$ in the right-hand figure, both distance $|x_{c}|$ from the centre along the major axis. A rather nice geometric property of the ellipse is that the distance $OPO'$ , shown in the second picture in Figure 5.4, is the same for all points on the orbit. So $OPO' = OP'O'$ for the points P and $P'$ on the ellipse. (This follows, for example, straightforwardly from some slightly messy algebra. We'll elaborate on this property in Section 5.5.1.) 

When e = 0, the focus sits at the centre of the ellipse and the lengths of the two axes coincide: a = b. This is a circular orbit. 

In the Solar System, nearly all planets have e < 0.1. This means that the difference between the major and minor axes of their orbits are equal to within less than 1% of each other, and so the orbits are very nearly circular. The only exception is Mercury, the closest planet to the Sun, which has $e \approx 0.2$ . 

There are, however, objects that lie on very eccentric orbits. These are comets. The most famous is Halley's comet, with eccentricity $e \approx 0.97$ , a fact that most scientists hold responsible for the Chas and Dave lyric "Halley's comet don't come round every year, the next time it comes into view will be the year 2062". However, according to astronomers, it will be the year 2061. 

## Hyperbolae: e > 1

For e > 1, the orbit is no longer bound. Indeed, there are two values of $\theta$ for which $r \to \infty$ . This occurs when $\cos\theta = -1/e$ . Repeating the algebraic steps that lead to the equation of an ellipse, we now find that the orbit is described by 

$$
\frac {(x - a e) ^ {2}}{a ^ {2}} - \frac {y ^ {2}}{b ^ {2}} = 1\tag{5.58}
$$

with 

$$
a ^ {2} = \frac {r _ {0} ^ {2}}{(e ^ {2} - 1) ^ {2}} \quad \text { and } \quad b ^ {2} = \frac {r _ {0} ^ {2}}{e ^ {2} - 1} .\tag{5.59}
$$

The relative minus signs between the two terms in $(5.58)$ is all important. It means that this is the equation for a hyperbola. It is plotted in the figure, where the dashed lines are the asymptotes. They meet at the point $x = r_{0}e/(e^{2} - 1)$ . Again, the centre of the gravitational attraction sits at the origin denoted by the sun-like disc. 

We've already noted that the orbit goes off to $r \to \infty$ when $\cos \theta = -1 / e$ . Because $-1 / e$ is negative, this must occur for two angles in the range $\pi / 2 < \theta < 3\pi / 2$ . This is one way to see why the orbit sits in the left-hand quadrant as shown in the figure. 

## Parabolae: e = 1

Finally, in the special case of e = 1, the algebra is particularly simple. The orbit is described by 

$$
y ^ {2} = r _ {0} ^ {2} - 2 r _ {0} x.\tag{5.60}
$$

This is the equation for a parabola. 

## The Energy of the Orbit Revisited

We can tally our solutions with the general picture of orbits that we built in Section 5.3.1 by looking at the effective potential. The energy (5.30) of a given orbit is 

$$
\begin{array}{r l} & E = \frac {1}{2} \mu \dot {r} ^ {2} + \frac {\mu l ^ {2}}{2 r ^ {2}} - \frac {k \mu}{r} \\ & \quad = \frac {1}{2} \mu \left(\frac {d r}{d \theta}\right) ^ {2} \dot {\theta} ^ {2} + \frac {\mu l ^ {2}}{2 r ^ {2}} - \frac {k \mu}{r} \\ & \quad = \frac {1}{2} \mu \left(\frac {d r}{d \theta}\right) ^ {2} \frac {l ^ {2}}{r ^ {4}} + \frac {\mu l ^ {2}}{2 r ^ {2}} - \frac {k \mu}{r}. \end{array}\tag{5.61}
$$

Our expression (5.51) for the orbit gives 

$$
\frac {d r}{d \theta} = \frac {r _ {0} e \sin \theta}{(1 + e \cos \theta) ^ {2}}.\tag{5.62}
$$

Substituting in, after a couple of lines of algebra we find that all the $\theta$ dependence vanishes in the energy (as it must, since the energy is a constant of the motion). We are left with the following pleasingly simple result, relating the energy to the eccentricity 

$$
E = \frac {\mu k ^ {2}}{2 l ^ {2}} (e ^ {2} - 1).\tag{5.63}
$$

We can look at what this means for the different types of orbits: 

- $e = 0 \implies E = -\mu k^2 / 2l^2$ . This coincides with the minimum of the effective potential $V_{\text{eff}}$ which, as we previously understood, corresponds to a circular orbit. 

- $0 < e < 1 \implies E < 0$ : These are the trapped, or bound, orbits that we now know are ellipses. If we substitute our expression for the semi-major axis $a$ given in (5.56), together with $l^2 = r_0 k$ from (5.52), we can rewrite the energy as 

$$
E = - \frac {\mu k}{2 a}.\tag{5.64}
$$

This is the archaically named vis-viva equation, latin for “living force”. It tells us that the energy of an elliptic orbit depends only on the semi-major axis, and not on the eccentricity. 

- $e = 1 \implies E = 0$ : This is the special case of a parabola. 

- $e > 1 \implies E > 0$ : These are the unbounded orbits that we now know are hyperbolae. 

## A Repulsive Force

In the analysis above, we assumed that the force is attractive, meaning that $k > 0$ in the potential. But it's straightforward to repeat the analysis for a repulsive potential with $k < 0$ . In this case, we get an analogous solution that we choose to write as 

$$
r = \frac {r _ {0}}{e \cos \theta - 1}\tag{5.65}
$$

where $r_{0} = l^{2}/|k|$ and $e = Cl^{2}/|k|$ with $C \geq 0$ . Note that with this choice of convention, we retain the condition $e \geq 0$ . But, because we must necessarily have r > 0, we only find solutions in the case e > 1. This is nice: we wouldn't expect to find bound orbits between two particles which repel each other. For e > 1, the unbounded orbits are again hyperbolae and look like that shown in the figure above. Notice that the orbits go off to $r \to \infty$ when $\cos\theta = +1/e$ which, since e > 1, must occur at an angle $0 < \theta < \pi/2$ and an angle $3\pi/2 < \theta < \pi$ . This is the reason that the orbit sits in the right-hand quadrant. 

## 5.4.2 Kepler's Laws of Planetary Motion

In 1605, Kepler published three laws which are obeyed by all planets in the Solar System. These laws were the culmination of decades of careful, painstaking observations of the night sky, firstly by Tycho Brahe and later by Kepler himself. They are: 

• K1: Each planet moves in an ellipse, with the Sun at one focus. 

- K2: The line between the planet and the Sun sweeps out equal areas in equal times. 

- K3: The period $T$ of the orbit is proportional to the radius $_{3/2}$ . Or, said more precisely, the period of the orbit is proportional to $a^{3/2}$ , where $a$ is the semi-major axis of the ellipse. In particular, the ratio $T^2 / a^3$ is independent of the eccentricity of the ellipse. 

Before we go on, a cute historical fact. Kepler himself introduced the term “focus” for the geometrical point of an ellipse. He wanted a term to demonstrate where the Sun sits. And, in latin, “focus” means “fireplace”. 

Now that we understand the mathematics behind orbits, we will see how Kepler's laws can be derived from Newton's inverse-square law of gravity. 

Kepler's second law is nothing more than the conservation of angular momentum. It holds for any central potential, not just for the inverse-square law. It follows straightforwardly by looking at the figure on the right. In time $\delta t$ , the area swept out is 

$$
\delta A = \frac {1}{2} r ^ {2} \delta \theta \quad \Longrightarrow \quad \frac {d A}{d t} = \frac {1}{2} r ^ {2} \dot {\theta} = \frac {l}{2}\tag{5.66}
$$

which we know is constant. 

What about Kepler's third law? This law is specific to the inverse-square law and it almost follows on grounds of dimensional analysis alone. Famously, for gravity, the mass $m$ of the particle drops out of the equation of motion. This is due to the equivalence of gravitational and inertial mass that we described in Section 2.3.3. We do, however, have three further dimensionful quantities in the game. These are the parameter $GM$ (rather than $G$ and $M$ individually), some measure $R$ of the size of the orbit, and the angular momentum $l$ . 

The parameter has dimensions 

$$
[ G M ] = L ^ {3} T ^ {- 2}.\tag{5.67}
$$

We can then define a single dimensionless variable $GMR/l^{2}$ . This means that if we want to write down a formula relating the period of an orbit, T to the distance scale R, the most general form is 

$$
T ^ {2} = \frac {R ^ {3}}{G M} f \left(\frac {G M R}{l ^ {2}}\right)\tag{5.68}
$$

with f some arbitrary function. For a circular orbit of radius R, we have $GMR/l^{2}=1$ , so this function f is just a constant. Indeed, we already saw this result in (5.34) where we noted that, for circular orbits, $\dot{\theta}^{2}\sim1/r^{3}$ . 

For an ellipse, the parameter $GMR / l^2$ is related to the eccentricity of the orbit. The more precise claim of Kepler's third law is that if we take our measure of the orbit to be $R = a$ , the semi-major axis, then the function $f$ is just a constant. To see this, note that the area of an ellipse is 

$$
A = \pi a b = \pi a ^ {2} \sqrt {1 - e ^ {2}} = \frac {\pi r _ {0} ^ {2}}{(1 - e ^ {2}) ^ {3 / 2}}.\tag{5.69}
$$

Since area is swept out at a constant rate l/2, the time period is 

$$
T = \frac {2 A}{l} = \frac {2 \pi r _ {0} ^ {2}}{l (1 - e ^ {2}) ^ {3 / 2}} = \frac {2 \pi}{\sqrt {G M}} \left(\frac {r _ {0}}{1 - e ^ {2}}\right) ^ {3 / 2} = \frac {2 \pi}{\sqrt {G M}} a ^ {3 / 2}
$$

This is the precise form of Kepler's third law. 

We see that Kepler's second law and (much of his) third law follow on rather general grounds. It is Kepler's first law, which is seemingly the most simple, that is the most difficult to show. That, of course, is what we spent much of this section demonstrating. 

## 5.4.3 The Runge–Lenz Vector

There is another, more elegant, way to see that the orbit of a planet traces out an ellipse. This is because a particle of mass $\mu$ moving under the inverse-square force 

$$
\mathbf {F} = - \frac {\mu k}{r ^ {2}} \hat {\mathbf {r}}\tag{5.71}
$$

enjoys another conserved quantity, namely 

$$
\mathbf {A} = \frac {\dot {\mathbf {x}} \times \mathbf {L}}{\mu k} - \hat {\mathbf {r}}\tag{5.72}
$$

where $\hat{\mathbf{r}} = \mathbf{x} / r$ and we've reverted to notation that we previously used for a test particle, where the Sun sits at the origin and the planet has position $\mathbf{x}$ . The vector $\mathbf{A}$ is known as the Runge–Lenz Runge–Lenz vector, or sometimes as the Laplace–Runge–Lenz vector. (In fact, with this normalisation $\mathbf{A}$ is more properly called the eccentricity vector.) 

The existence of an additional conserved quantity in the Kepler problem is extremely surprising. It is also very uncommon. Pretty much any other potential does not come with extra conservation laws. But the $V \sim 1/r$ potential is mathematically special. It is a wonderful fact, and one that is repeated throughout physics, that the formulae that have special mathematical properties are also those relevant for nature. 

To see that the Runge–Lenz vector is conserved, we simply need to differentiate. We use the fact that angular momentum is conserved, so $\dot{L}=0$ , to write 

$$
\dot {\mathbf {A}} = \frac {\ddot {\mathbf {x}} \times \mathbf {L}}{\mu k} - \frac {\dot {\mathbf {x}}}{r} + \frac {\dot {r}}{r ^ {2}} \mathbf {x}.\tag{5.73}
$$

Now $r^{2} = x \cdot x$ , from which we learn that $\dot{r} = (\mathbf{x} \cdot \dot{\mathbf{x}})/r$ . The above formula then becomes 

$$
\dot {\mathbf {A}} = \frac {\ddot {\mathbf {x}} \times (\mathbf {x} \times \dot {\mathbf {x}})}{k} - \frac {\dot {\mathbf {x}}}{r} + \frac {\mathbf {x} \cdot \dot {\mathbf {x}}}{r ^ {3}} \mathbf {x} = - \frac {\hat {\mathbf {r}} \times (\mathbf {x} \times \dot {\mathbf {x}})}{r ^ {2}} - \frac {\dot {\mathbf {x}}}{r} + \frac {\mathbf {x} \cdot \dot {\mathbf {x}}}{r ^ {3}} \mathbf {x}
$$

Now it's just a matter of using the triple product formula, $\mathbf{a} \times (\mathbf{b} \times \mathbf{c}) = (\mathbf{a} \cdot \mathbf{c})\mathbf{b} - (\mathbf{a} \cdot \mathbf{b})\mathbf{c}$ to see that the first term cancels the second two. This means that $\dot{\mathbf{A}} = 0$ . 

The conservation of the Runge–Lenz vector has a number of consequences, some of which we'll see in Volume 3 on Quantum Mechanics. But for now we can use it to quickly re-derive our earlier result. The vector A points in some fixed direction in space. Note that $A \cdot L = 0$ , which means that A points in some direction in the plane of the orbit. If we take the inner product with the position vector, we get 

$$
\mathbf {A} \cdot \mathbf {x} = A r \cos \theta .\tag{5.75}
$$

For now, we'll think of this equation as defining the angle $\theta$ in the plane. (We'll shortly see that it coincides with our previous definition.) Using (5.72), we have 

$$
\mathbf {A} \cdot \mathbf {x} = \frac {\mathbf {x} \cdot (\dot {\mathbf {x}} \times \mathbf {L})}{\mu k} - r = \frac {\mathbf {L} \cdot (\mathbf {x} \times \dot {\mathbf {x}})}{\mu k} = \frac {l ^ {2}}{k} - r\tag{5.76}
$$

where, in the second equality, we've used the symmetry of the scalar triple product. Putting this result together with our definition (5.75), we have 

$$
A r \cos \theta = \frac {l ^ {2}}{k} - r \quad \Longrightarrow \quad r = \frac {r _ {0}}{A \cos \theta + 1}\tag{5.77}
$$

where $r_{0} = l^{2}/k$ . This is precisely the equation for a conic section (5.51) that we previously derived by solving the orbit equation. 

There are a few lessons to take away from this. First, comparing (5.77) with (5.51), we see that the magnitude of the Runge–Lenz vector coincides with the eccentricity, $|A| = e$ . (This is the reason that A is sometimes referred to as the eccentricity vector.) Second, we see that the angle $\theta$ is the same in the two formulae. Previously we defined $\theta = 0$ to be the direction of the perihelion, the closest point of the orbit. Here we defined $\theta = 0$ to be the direction in which A points. Combining these, we get a geometrical intuition for the Runge–Lenz vector: it points from the Sun towards the perihelion, and its magnitude is equal to the eccentricity of the orbit. 

The existence of the conserved Runge–Lenz vector explains a fact that is so familiar we didn't even comment on it above: the orbits in the Kepler problem are closed. This means that each time we go around the Sun, the closest point always sits at the same angle $\theta$ . This is a special property of the inverse-square law that doesn't hold in other potentials. 

## 5.4.4 Perihelion Precession in General Relativity

As we've seen, a planet orbiting the Sun traces out an ellipse. But this analysis neglects two other important facts. The first is that there are other planets in the Solar System, and these too will exert a gravitational pull. The second is that Newton's theory of gravity isn't actually correct: it is superseded by Einstein's theory of general relativity, which describes gravity in terms of the bending of space and time. 

Both of these additional effects change the orbit. But, it turns out, they don't change it much. The orbit of a planet in our Solar System remains approximately an ellipse, but the ellipse precesses. This means that the orbit doesn't close, and the point at which the planet is closest to the Sun – the perihelion – sits at a slightly different angle each time, as shown in the figure. (As we've just seen, such a precession is prohibited in the two-body Kepler problem by the conserved Runge–Lenz vector.) 

For nearly all the planets, it turns out that the observed precession can be correctly accounted for within Newtonian gravity by the gravitational pull of the other planets, with Jupiter giving the largest correction. The exception to this statement is Mercury. This is the planet closest to the Sun, and so feels the strongest gravitational field. 

The full theory of general relativity is rather complicated and will be covered in a separate volume (where we will also make an attempt at describing the corrections to perihelion precession due to other planets). For our purposes, however, we can make do with something much simpler. It turns out that much of the effect of the curvature of spacetime can be captured in a simple correction to the effective potential $(5.28)$ . In general relativity, this reads 

$$
V _ {\mathrm{eff}} (r) = - \frac {k m}{r} + \frac {m l ^ {2}}{2 r ^ {2}} - \frac {k m l ^ {2}}{c ^ {2} r ^ {3}}.\tag{5.78}
$$

Here $k = GM$ and $l = r^2\dot{\theta}$ , as throughout this chapter, and we've reverted to thinking of the planet as a test particle of mass $m$ orbiting the Sun of mass $M$ . The first two terms coincide with those of the Kepler problem. The third term is new and, indeed, introduces something novel: the speed of light $c$ . This extra term becomes unimportant when the planet orbits at distances $r \gg GM / c^2$ , which we recognise as roughly the Schwarzschild radius. This means that we might expect the effects of the additional term to become noticeable for the planet closest to the Sun. 

Repeating the steps from earlier in this chapter, the orbit equation (5.49) for the variable u = 1/r becomes 

$$
\frac {d ^ {2} u}{d \theta^ {2}} + u = \frac {k}{l ^ {2}} + \frac {3 k u ^ {2}}{c ^ {2}}.\tag{5.79}
$$

We'll treat the extra term, which is again tagged by that factor of $c^2$ , as a perturbation to the original orbit. (We're getting a little ahead of ourselves here. We'll treat perturbation theory systematically in Section 8.2.) To this end, we write $u(r) = u_0 + \epsilon u_1(r)$ where $u_0$ is a circular Newtonian orbit with 

$$
u _ {0} = \frac {k}{l ^ {2}}\tag{5.80}
$$

and $\epsilon\ll1$ . Then, expanding to leading order in $\epsilon$ , the orbit equation (5.79) becomes an equation for the perturbation $u_{1}(r)$ 

$$
\begin{array}{l l} & \frac {d ^ {2} u _ {1}}{d \theta^ {2}} + u _ {1} = \frac {3 k u _ {0} ^ {2}}{c} + \frac {6 k u _ {0} u _ {1}}{c ^ {2}} \\ \Longrightarrow & \frac {d ^ {2} u _ {1}}{d \theta^ {2}} + \left(1 - \frac {6 k ^ {2}}{c ^ {2} l ^ {2}}\right) u _ {1} = \frac {3 k ^ {3}}{c ^ {2} l ^ {4}}. \end{array}\tag{5.81}
$$

The solution to this equation is very similar to that of the Kepler problem (5.50). Including the $u_{0} = k/l^{2}$ term, the orbit is given by 

$$
u (\theta) = A \cos \left(\sqrt {1 - \frac {6 k ^ {2}}{c ^ {2} l ^ {2}}} \theta\right) + \frac {k}{l ^ {2}} + \frac {3 k ^ {2}}{c ^ {2} l ^ {4}}\tag{5.82}
$$

where we have once again chosen our polar coordinates so that the integration constant is $\theta_{0}=0$ . This equation describes an approximate ellipse. But, as advertised above, the ellipse now precesses. To see this, note that the periapsis occurs whenever the cos term is 1. This first happens at $\theta=0$ . But the next time round, it happens at 

$$
\theta = 2 \pi \left(1 - \frac {6 k ^ {2}}{c ^ {2} l ^ {2}}\right) ^ {- 1 / 2} \approx 2 \pi \left(1 + \frac {3 k ^ {2}}{c ^ {2} l ^ {2}}\right).\tag{5.83}
$$

This means that the perihelion advances by an angle of $6\pi G^{2}M^{2}/c^{2}l^{2}$ each turn. This is precisely what's needed to account for the extra precession of Mercury. 

## 5.5 A Brief History of Newton's Time

Many of the results that we described in this chapter, and indeed so far in this book, were first derived by Isaac Newton and published in 1687 in his three-volume masterpiece, Philosophiae Naturalis Principia Mathematica, known to physicists today simply as “the Principia”. 

The Principia is an astonishing book. Not only does it present the laws of motion and the inverse-square law of gravity, but it then goes into great detail deriving various consequences, from the laws of planetary motion that we've seen here, to hugely complicated topics such as how the Earth gets squashed as it rotates, the precession of the equinoxes, and a first look at the three-body problem using perturbation theory. There is a long discussion about tides, all the more wonderful because legend has it that Newton never actually saw the sea. 

Many of the great breakthroughs in the Principia were made in 1665, a year when the University of Cambridge was closed due to the plague and Newton retreated to his home in Woolsthorpe Manor, 60 miles north. But Newton was a secretive, somewhat paranoid, man and he chose not to share his great discoveries with anyone else. This would cause no end of arguments later in his life. 

However, Newton was not the only one contemplating the universe. Down in London, an impressive trio of friends were also thinking about gravity. This group consisted of Edmund Halley (of comet fame), Christopher Wren (of Christopher Wren fame) and, most importantly, Robert Hooke. You probably know Hooke for that almost-trivial spring law, but he was one of the great intellectual forces of the 1600s. At some point, his job at the Royal Society was to discover a new law of physics every week! $^{1}$ 

By the late 1670s, it seems likely that this trio knew that gravity should be described by an inverse-square law. They arrived at this conclusion from Kepler's laws, using roughly the logic that we explained in Section 5.4.2: Kepler's second law implies that the force must point towards the Sun, while Kepler's third law then tells you that the force must drop off as $1 / r^2$ on dimensional grounds. However, in some ways this wasn't much progress. It gives a mathematical formulation of two of Kepler's laws but doesn't tell you anything new. The real challenge is to show that the inverse-square law then implies Kepler's first law: that the orbits are ellipses. This was the question that the trio set themselves. 

In 1684, Hooke claimed success. He told his two friends that he could show that planets must move in ellipses but refused to give the details, not even in anagram form. Understandingly, his friends were sceptical. But this prompted Halley to come up to Cambridge to chat with Newton. Presumably somewhat nervous of being scooped, Newton told Halley that he'd figured all that out 20 years ago, but he too refused to give the details. I can only assume that Halley left just as sceptical as he arrived. 

The following month Newton sent Halley the proof in a short, nine-page, paper called De Motu Corporum in Gyrum, or The Motions of Bodies in Orbit. Halley was keen to publish but Newton asked for a delay to add a few more details. Those details took a further two years and the result is the three books that make up the Principia. 

Newton's tendency towards secrecy didn't entirely evaporate with the publication of the Principia. In particular, there was one breakthrough that he failed to mention: the discovery of calculus. Evidence suggests that Newton developed calculus back in 1665 during his miraculous plague year. It's unclear how much calculus he used in deriving his results on motion and gravity, but all the proofs in the Principia are written using more traditional (some would say archaic) geometric methods. 

Meanwhile, in Germany, Gottfried Leibniz also developed calculus, and did so in a much more systematic way than Newton. Moreover, Leibniz was excited to share his discoveries with the wider world. And, of course, everyone else quickly became excited too because, after all, calculus is brilliant. A very obvious challenge of the day was to take all of Newton's proofs in the Principia and recast them using the new language of calculus. This challenge was eagerly and successfully taken up by many mathematicians, much to Newton's displeasure as he huffed and puffed about having done it all first. 

All of this leaves Newton's original Principia as something of an enigma. It is one of the most influential scientific books ever published, and is rightly considered to be the beginning of theoretical physics. And yet, even by the time the second edition came out in 1713, the geometric techniques it uses were woefully out of date, replaced by the more powerful and intuitive tools of calculus. 

## 5.5.1 What Would Newton Do?

As some intellectual light entertainment, in this section we present a geometric proof of Kepler's laws in the style of Newton. This proof is close to, but not quite the same as, the one presented in the Principia. But the proof itself has an impressive pedigree. It was first published by Maxwell, who gave credit to Hamilton. It was later rediscovered by Feynman and published in a book called Feynman's Lost Lecture. 

## Properties of Ellipses

First, we need some geometric facts about ellipses. The way to construct an ellipse is to take a piece of string of some fixed length and tie the ends down at points that we'll call $F$ and $F'$ . Then stretch the string taut and use a pencil to sketch out all possible points. This is an ellipse. 

This situation is depicted on the left of Figure 5.5. The pencil sits at the point P, and the ellipse is the collection of points P such that the combined distance 

$$
F ^ {\prime} P + F P = \text { constant } .\tag{5.84}
$$

Next, detach one end of the string, say $F'$ . We can then use the same piece of string to draw a circle with the other point $F$ at the centre. This is shown on the right of Figure 5.5. Now here's a pretty fact. 

Fig. 5.5 On the left: an ellipse is the loci of points P that you can reach with a taut string stretched from $F'$ to F. On the right: if we unpin the string on one end, and construct the circle, there's a very cute geometrical fact. 

Claim: Consider some point G on the circle. Draw the line $F'G$ and consider its perpendicular bisector. This will intersect the line FG at 

Proof: To avoid distractions, we first draw the points $F', F, G$ , and $Q$ without the accompanying circle and ellipse. This is shown on the left in Figure 5.6. The additional dotted line is there to highlight two congruent triangles. This shows that $F'Q = QG$ . This means that the distance $F'QF$ is the same as $FG$ , which is the length of the original string. This tells us that $Q$ lies on the ellipse.

Next we show that no other point on the perpendicular bisector lies on the ellipse. This follows from the diagram on the right of Figure 5.6. Clearly $FTG > FQG$ . But $TG = F'G$ , so $FTF' > FQF'$ , so $T$ cannot lie on the ellipse. The fact that $Q$ is the only point on the perpendicular bisector that lies on the ellipse means that the perpendicular bisector must be tangent to the ellipse at that point. 

Fig. 5.6 The perpendicular bisector intersects FG at Q, which sits on the ellipse. The perpendicular bisector is tangent to the ellipse. 

There's a rather nice physics corollary to these geometric facts. If you look at the diagram on the left of Figure 5.7 then you can invoke the same congruent triangles to see that the two angles are equal: $\theta_{1} = \theta_{2}$ . But this is true for all points on the ellipse. 

Fig. 5.7 On the left: congruent triangles show that $\theta_{1} = \theta_{2}$ . On the right: all light emitted from one focus ends up at the other. 

Now suppose that you make a mirror in the shape of an ellipse. If you place a light bulb at one focus, then the result above tells you that every light ray bounces off the mirror and returns to the other focus. 

## A Geometrical View of Orbits

We now return to our original task of understanding orbits using geometrical methods alone. We'll consider a planet orbiting around the Sun. Our strategy will be the following: 

- First we show that Kepler's second law (equal areas in equal time) follows if we assume that the gravitational force on the planet acts towards the Sun. 

- Next, we show that Kepler's third law $(T \sim R^{3/2})$ implies that the force must be inverse-square, so $F \sim 1/R^2$ . 

- Finally, we show that these facts combined imply Kepler's first law: the planet travels on an ellipse. 

To proceed, we place the Sun at the point S, and we consider a planet moving, in some short time $\Delta t$ , from point A to point B. If a force acts for some short time $\Delta t$ , we talk about the impulse. This is the integral of the force over time and, from Newton's second law, results in a change of momentum 

$$
m \Delta \mathbf {v} = \int_ {t} ^ {t + \Delta t} \mathbf {F} d t.\tag{5.85}
$$

The impulse is the change of momentum. For our orbits we make the assumption that the impulse is towards the Sun and equal to some vector that we call $\overrightarrow{BV}$ . 

Now consider the next time interval $\Delta t$ . The planet travels the vector sum of $\overrightarrow{AB} + \overrightarrow{BV}$ . This means that the planet travels to point $C$ , as opposed to the point $C'$ that it would reach if the Sun wasn't exerting its pull. The situation looks like this: 

Claim: The area of the triangle $SAB$ is equal to the area of the triangle $SBC$ . This is Kepler's second law. 

Proof: We first show that the area SAB is equal to the area $SBC'$ . This follows by staring at the diagram below together with the familiar formula for the area of a triangle 

$$
\mathrm{Area} = \frac {1}{2} \mathrm{base} \times \mathrm{height} = \frac {1}{2} S B \times \mathrm{samedistance}.
$$

Alternatively, you could drop a perpendicular from S to $AC'$ and consider the bases as AB and $BC'$ respectively. 

Next we show that the area $SBC'$ is the same as the area SBC. This follows by the same formula for the area of a triangle, this time applied to the figure below 

The critical fact is that $CC'$ is parallel to $SB$ . This completes the proof: Kepler's second law follows from the assumption that the impulse is towards the Sun. 

Now the second step: we will show that Kepler's third law implies that the force of gravity must be an inverse-square law. We do this by thinking about the special case of circular orbits. From Kepler's second law, if the particle moves on a circle then it must travel at constant speed $\pmb{v}$ . If the radius of the orbit has radius $R$ then the time taken to make the orbit is 

$$
T = \frac {2 \pi R}{v}.\tag{5.87}
$$

We now prove this well-known result using geometric methods: 

Claim: If the particle moves with constant speed v around a circle of radius R, then the acceleration a is 

$$
a = \frac {v ^ {2}}{R}.\tag{5.88}
$$

Proof: The idea is to think about how the velocity vector changes as the particle moves around the circle. This is shown in Figure 5.8. On the left, is the circular path of the particle in real space, with the vector showing the velocity. As the particle traces out a circle, so too does the velocity vector, as shown on the right of Figure 5.8. This time the vector in this diagram shows the acceleration. Both circles are traversed in the same time T. By analogy, if the particle takes 

time $T = 2\pi R / v$ in real space, then it must take time $T = 2\pi v / a$ in velocity space. Equating these gives $a = v^{2} / R$ as required. 

Fig. 5.8 The geometrical proof that $a = v^{2}/R$ for circular motion. 

Before we proceed, it's worth pointing out that there is a $\pi/2$ shift between the position of the particle in real space and the position of the particle in the velocity diagram in Figure 5.8. For example, when the particle sits at $(x,y) = (R,0)$ in real space, so that it is at the far right of the orbit, then its velocity is $(v_x,v_y) = (0,v)$ and so sits at the top of the velocity diagram. This simple observation will resurface shortly when we derive Kepler's first law. 

For now, it's straightforward to prove Newton's inverse square law. We can combine (5.87) and (5.88) to write Newton's second law as 

$$
F = m a = \frac {4 \pi^ {2} m R}{T ^ {2}}.\tag{5.89}
$$

Now we invoke Kepler's third law: the time period of the orbit scales as $T \sim R^{3/2}$ . This then tells us 

$$
F \sim \frac {1}{R ^ {2}}.\tag{5.90}
$$

This, of course, is Newton's famous inverse-square law. We have shown that it follows from Kepler's second and third laws. 

Our final challenge is the important one: we need to show that Kepler's first law follows from what we have derived so far. In other words, we need to show that planets move in ellipses. To this end, we take the orbit and decompose it into segments of equal angles, as shown in Figure 5.9. 

Fig. 5.9 The orbit is decomposed into segments of equal angle $\theta$ . 

From Kepler's second law, we know that the planet must travel faster when it's nearer the Sun than when it's further away. So the speed is greater when it traverses $ABC$ compared to when it traverses $DEG$ . But how much faster does it go? Denote the ratio of the two distances $SB$ and $SE$ by 

$$
\frac {S E}{S B} = x.\tag{5.91}
$$

Then, to leading order in $\theta$ , the ratio of areas of the triangles SEG and SBC are 

$$
\frac {\text { Area } (S E G)}{\text { Area } (S B C)} = x ^ {2} .\tag{5.92}
$$

This means that the area of a triangular segment scales as $Area \sim x^{2}$ , so the time taken to traverse a segment is $\Delta t \sim x^{2}$ . But we know that the force is inverse-square, so $F \sim 1/x^{2}$ . Putting this together tells us that the impulse, or change in velocity at each corner has magnitude 

$$
\Delta v = F \Delta t = \mathrm{constant}.\tag{5.93}
$$

Now we can draw a velocity diagram, plotting how the velocity v changes as the particle undergoes its now-segmented orbit. At each corner, the velocity changes by an vector $\Delta v$ , with $|\Delta v|$ a constant, directed at uniformly increasing angles. So the end result is something like this: 

The speed is largest when the planet is closest to the Sun. This means that the top of the velocity diagram corresponds to the periheilion. The speed is smallest when the planet is furthest from the Sun, so the bottom of the velocity diagram corresponds to the aphelion. In the limit where we decompose the orbit into smaller and smaller segments, so that $\Delta t \rightarrow 0$ and $\theta \rightarrow 0$ , the velocity diagram becomes a circle. But, crucially, it is a circle where the point O is off-centre. 

Now we're almost done. If we place the picture of the orbit in real space side by side with the velocity diagram, they look like this: 

At the point P on the orbit, the velocity $v_{P}$ points up and left. We've denoted this as the point $P'$ on the corresponding velocity diagram. Note that we've also denoted the centre of the velocity diagram as point C on the right. 

The key observation is that the angle $\phi$ shown in both diagrams is the same. (This is simplest to see by returning to our jerky, segmented polygon motion.) This means that, just as in Figure 5.8, the direction of the line segment $CP'$ is rotated by $\pi/2$ in the velocity diagram, relative to the line segment SP on the real orbit. 

This motivates our final step. We take the two diagrams above, and simply rotate the velocity diagram by $90^{\circ}$ . The result looks like this: 

We've denoted the rotated velocity at point $P'$ as $\mathbf{u}_P$ . Because we rotated the diagram by $90^\circ$ , this velocity is perpendicular to the physical velocity $\mathbf{v}_P$ of the real orbit: 

$$
\mathbf {v} _ {P} \cdot \mathbf {u} _ {P} = 0.\tag{5.94}
$$

Now there's a clear path to understanding the shape of the orbit. Our goal is to reconstruct the orbit in real space so that, at every point $P$ , the tangent to the orbit $\mathbf{v}_P$ obeys (5.94). We can achieve this in the following steps: 

- On the velocity diagram, draw the perpendicular bisector to $OP'$ . 

- Place the planet at the point where this perpendicular bisector intersects $CP'$ . Call this point $Q$ . 

These steps are captured in the following diagram: 

But this diagram is familiar: it is identical to the one shown on the right of Figure 5.5. The curve constructed in this way is unique and, as we showed previously, is an ellipse, with the tangent to Q orthogonal to $OP'$ . This is what we wanted! 

Needless to say, we won't be encountering these kinds of geometric proofs elsewhere in this series of books. 

## 5.6 Scattering: Throwing Stuff at Other Stuff

Over the past 100 years or so, physicists have developed a foolproof and powerful tool that allows us to understand everything and anything in the universe. You take the object that you're interested in and you throw something at it. Ideally, you throw something at it really hard. This technique was developed around the turn of the twentieth century and has since allowed us to understand everything from the structure of atoms, to the structure of materials, to the structure of DNA. More recently, we used the same technique to discover the Higgs boson and gravitational waves. (For the latter, we had to throw one black hole at another. Admittedly, in this case someone else was doing the throwing.) 

In short, throwing stuff at other stuff is the single most important experimental method available to science. Because of this, it is given a respectable sounding name. We call it scattering. 

We'll discuss scattering a lot in this series of books. For example, there is an entire chapter devoted to scattering in Volume 3 on Quantum Mechanics. In this section, we will describe some basic aspects of particles scattering off central potentials. As we will see, this includes the problem of an alpha particle scattering off a nucleus, an experiment that Rutherford used to first understand the structure of the atom. 

## 5.6.1 The Impact Parameter

We start by setting the scene, and introduce some ideas that hold for any scattering problem. We restrict our attention to central potentials $V(r)$ , and assume that $V(r) \to 0$ as $r \to \infty$ . 

We do our experiment and throw the particle from a large distance which we will take to be $r \rightarrow \infty$ . We want to throw the particle towards the origin, but our aim is not always spot on. The particle has some energy E > 0. It comes in from infinity and will typically be deflected by some angle, and ultimately escape out to infinity again. If the interaction is repulsive, we expect that its trajectory will look something like that shown in the Figure 5.10. However, much of what we're about to say will hold whether the force is attractive or repulsive. 

Fig. 5.10 A typical trajectory of a particle moving in a repulsive central potential 

First, by energy conservation, the speed of the particle at the end of its trajectory must be the same as the initial speed. This is true because of our assumption that $V(r) \to 0$ as $r \to \infty$ , so there is no contribution from the potential energy. We call this initial and final speed v. 

In a central potential, we also have conservation of angular momentum, $L = mx \times \dot{x}$ . We can get an expression for $l = |L|/m$ as follows: draw a straight line tangent to the initial velocity. The closest this line gets to the origin is a distance b, known as the impact parameter and is shown in Figure 5.10. The modulus of the angular momentum is then 

$$
l = b v.\tag{5.95}
$$

If this equation isn't immediately obvious mathematically, the following cute way of thinking may convince you. Suppose that there was no force acting on the particle at all. In this case, the particle would indeed follow the horizontal dotted straight line shown in Figure 5.10. When the particle is closest to the origin, its velocity $\dot{\mathbf{x}}$ is perpendicular to its position $\mathbf{x}$ and its angular momentum is obviously $l = bv$ . But angular momentum is conserved for a free particle, so this must also be its initial angular momentum. 

Now we go back to the situation with the central potential $V(r)$ . The angular momentum remains constant throughout the motion and, by the same kind of argument, at the end is given by $l = b'v$ where $b'$ is the shortest distance from the origin to the exit asymptote as shown in Figure 5.10. But since the angular momentum is conserved, we must have $b = b'$ : the incoming impact parameter coincides with the outgoing impact parameter. 

## 5.6.2 Rutherford Scattering

Historically, the most important scattering experiment involved throwing a charged particle at the nucleus to uncover the structure of the atom. This process is now known as Rutherford scattering. 

Mathematically, we take a particle of charge q and mass m and throw it at a fixed particle of charge Q. The relevant force is the Coulomb potential 

$$
V = \frac {q Q}{4 \pi \epsilon_ {0} r}.\tag{5.96}
$$

This is a repulsive force if q and Q have the same sign. Happily, the Coulomb force is mathematically identical to the gravitational force, which means that we can just take all the results from Section 5.4 and simply replace 

$$
k = - \frac {q Q}{4 \pi \epsilon_ {0} m}.\tag{5.97}
$$

Another, more extreme scattering event for a repulsive Coulomb potential is shown in Figure 5.11. Here we've used the fact, derived above, that $b' = b$ . Following the notation of Section 5.4, we denote the angular position of the particle as $\theta$ , with $\theta = 0$ the closest point of the trajectory. (However, in contrast to Section 5.4, we're throwing the particle in from the left, rather than the right.) 

Fig. 5.11 Another scattering trajectory in a repulsive potential, now with various angles labelled. 

For a given scattering trajectory, the particle is deflected through a total angle $\psi$ . We want to understand how this angle $\psi$ depends on various initial conditions of the trajectory. In the short term, it turns out to be more useful to express things in terms of the angle $\alpha$ shown in Figure 5.11. Obviously this is related to $\psi$ by 

$$
\psi = \pi - 2 \alpha .\tag{5.98}
$$

All the hard work has already been done. Using our expression $(5.65)$ for a general orbit in the $V \sim 1/r$ potential, we know that the particle asymptotes to $r \to \infty$ when $\cos\theta = 1/e$ . Comparing to Figure 5.11 gives us the expression for the angle $\alpha$ 

$$
\cos \alpha = \frac {1}{e}.\tag{5.99}
$$

For a repulsive potential, we always have $e \geq 1$ . We take $\alpha$ in the range $\alpha \in [0, \pi/2)$ , as shown in Figure 5.11. 

To proceed, we look at our various expressions for the energy. We throw the particle from $r \rightarrow \infty$ at speed v. This means that when the particle started its journey, it had $E = \frac{1}{2}mv^{2}$ . We can equate this with form of the orbital energy derived in (5.63) to get 

$$
E = \frac {1}{2} m v ^ {2} = \frac {m k ^ {2}}{2 l ^ {2}} (e ^ {2} - 1) = \frac {m k ^ {2}}{2 l ^ {2}} \tan^ {2} \alpha .\tag{5.100}
$$

The angular momentum in this expression can be replaced by l = bv, and we get 

$$
\tan \left(\frac {\psi}{2}\right) = \frac {| k |}{b v ^ {2}}.\tag{5.101}
$$

This tells us the scattering angle $\psi$ for an initial impact parameter $b$ and velocity $v$ . Note that $\psi \to \pi$ as $b \to 0$ . That's to be expected: if you score a direct hit on the Coulomb target then you will bounce back the way you came. Conversely, $\psi \to 0$ as $b \to \infty$ . That's telling you that if you miss the target by a lot, you'll just sail on past as if nothing happened. 

## 5.6.3 A First Look at the Cross-Section

If you know the impact parameter of your trajectory, then (5.101) tells you the resulting scattering angle. But often in experiments, you don't know the exact impact parameter. Instead, you're throwing blind. You typically send in a whole bunch of particles and watch as each of them scatters off at some angle. At best, you have information only about the probability distribution of angles at which they emerge. To deal with this situation, we introduce the idea of a cross-section. 

In fact, if we're going to admit that we don't know the exact impact parameter, this means that we can't be sure which direction our angular momentum points in either. That means that we can't specify a single plane in which the scattering occurs, as we have so far. Instead, we will need to revert to a full three-dimensional picture. 

The resulting setup is shown in Figure 5.12. We have taken a uniform beam of particles, coming in from the left. Each of these particles has the same initial kinetic energy, $E = \frac{1}{2}mv^{2}$ . But there is a spread of the impact parameter b. We want to understand what becomes of this beam. 

Fig. 5.12 What becomes of an infinitesimal cross-sectional area after scattering. 

We consider a small cross-sectional area of the initial beam, denoted as $d\sigma$ in Figure 5.12. We write this as 

$$
d \sigma = b d \phi d b.\tag{5.102}
$$

Here $\phi$ is the additional angular variable that takes into account the fact that this is now a full three-dimensional problem. For given initial data b and v, a particle will have some fixed scattering angle $\psi(b,v)$ . (For example, for Rutherford scattering this is given by the formula (5.101).) Meanwhile, for central forces, the $\phi$ angular coordinate remains unaffected by the scattering. This means that the particles within the region $d\sigma$ will evolve to the lie in a cone of solid angle $d\Omega$ , given by 

$$
d \Omega = \sin \psi d \phi d \psi\tag{5.103}
$$

where we should think of $\psi$ as a function $\psi(b,v)$ . Alternatively, inverting this, we can think of the impact parameter as a function of the scattering angle and initial velocity: $b = b(\psi, v)$ . The differential cross-section is then defined to be 

$$
\frac {d \sigma}{d \Omega} = \frac {b}{\sin \psi} \left| \frac {d b}{d \psi} \right|.\tag{5.104}
$$

The differential cross-section is a function of v and the scattering angle $\psi$ . (A warning: in almost all texts, including later books in this series, the angle that we've called $\psi$ is denoted as $\theta$ . Here we've picked $\psi$ to avoid 

confusion with the angle $\theta$ that we used throughout this chapter to denote the angular position of the particle.) 

Physically, you should think of the differential cross-section as proportional to the flux density of particles that gets deflected by an angle $\psi$ . This is the information that's actually known experimentally. We can now apply this general framework to the problem of Rutherford scattering. From (5.101), we have 

$$
b = \frac {| k |}{v ^ {2}} \cot \left(\frac {\psi}{2}\right) = \frac {m | k |}{2 E} \cot \left(\frac {\psi}{2}\right).\tag{5.105}
$$

The resulting differential cross-section is 

$$
\frac {d \sigma}{d \Omega} = \left(\frac {m | k |}{4 E}\right) ^ {2} \frac {1}{\sin^ {4} (\psi / 2)}.\tag{5.106}
$$

This known as the Rutherford cross-section. Roughly speaking, this can be thought of as the probability distribution for a particle of energy E to be scattered in some direction $\hat{\mathbf{n}}(\phi,\psi)$ . 

## 5.6.4 A Bit More History: The Discovery of the Nucleus

The mathematics described above underlies one of the most famous experiments in the history of physics. This was performed in 1909 at the University of Manchester by Hans Geiger and his undergraduate assistant 

Ernest Marsden. They fired alpha-particles (which, we now know, are fast-moving helium nuclei) at a thin film of gold and measured how they scatter. 

One day Ernest Rutherford entered the room and, according to Marsden, suggested “see if you can get some effect of alpha-particles directly reflected”. The results were startling and entirely unexpected. About 1 alpha particle in 8000 was reflected back in the direction from which it came. Many years later, Rutherford recounted his surprise: 

It was quite the most incredible event that ever happened to me in my life. It was almost as incredible as if you fired a 15-inch shell at a piece of tissue paper and it came back and hit you. 

Why was it so surprising? At the time, there were a number of theories about the structure of atoms, all (now slightly comically) based on some everyday, intuitive concept, whether plum puddings, planetary systems, or vortices. None predicted the dramatic deflection seen in the Geiger–Marsden experiment. 

It was Rutherford himself who understood the consequences of the Geiger–Marsden experiment. Rutherford was very much an experimental physicist and not known for his love of theorists. He is reported to have said of relativity, “Oh, that stuff. We never bother with that in our work”. My favourite Rutherford quote, capturing both his attitude to theorists, and his endearingly boorish personality, is 

Nonetheless, when push came to shove, Rutherford showed himself to be no mean theorist. In 1911, he postulated that each atom contains a heavy, almost point-like object at the centre, carrying positive charge. He then did the calculation that we’ve described above to derive the cross-section (5.106). The results were in perfect agreement with the Geiger–Marsden experiment. 

There is a postscript to this story for, like many great scientists before him, Rutherford was the beneficiary of no small amount of luck. Partly this luck was on the experimental side: the alpha particles used in the experiment were fast enough to blast through the electrons of the atom without care, but slow enough to be deflected from the nucleus by the Coulomb force before they experienced the much stronger nuclear force. That meant that the experiment could be understood by known theories of electromagnetism. 

But, more importantly, Rutherford's calculation was, like ours, classical. And to really understand atomic physics, we should work with quantum mechanics. We'll study scattering in Volume 3 on Quantum Mechanics and find something interesting: quantum formulae for the differential cross-section almost never agree with their classical counterparts. So why did Rutherford's calculation give the right result?! Well, there is one exception to the rule. It turns out that the Coulomb force is special: it's the one case where the classical and quantum results agree. This is another example of the special mathematical properties of the $V \sim 1/r$ potential and, like others, can be traced to the existence of the conserved Runge–Lenz vector. 

1 Hooke could be every bit as secretive as Newton. He first published his spring law as “cediinnoopsssttuu” which is somewhat less concise than the F = -kx that we now know and love. Two years later, he revealed that this was an anagram for “Ut Pondus sic Tensio” meaning “as the extension, so the weight”. Sometimes, when reading modern scientific papers, I wonder if the authors are employing a similar method of communication. 

## Rotating Reference Frames

We stated, long ago, that inertial frames provide the setting for Newtonian mechanics. But what if you, one day, find yourself in a frame that is not inertial? For example, suppose that every 24 hours you happen to spin around an axis which is 2500 miles away. What would you feel? Or what if every year you spin around an axis 36 million miles away? Would that have any effect on your everyday life? 

In this section we will discuss what Newton's equations of motion look like in non-inertial frames. Just as there are many ways that an animal can be not a dog, so there are many ways in which a reference frame can be non-inertial. Here we will just consider one type: reference frames that rotate. We start with some basic concepts. 

## 6.1 Rotating Frames

To set the scene, we will consider two different frames. The first of these, S, is an inertial frame. It is drawn in the figure with Cartesian axes labelled, as usual, by x, y, and z. 

The second frame, $S'$ , with Cartesian axes labelled by $x'$ , $y'$ , and $z'$ , is non-inertial. We will take $S'$ to be rotating with respect to S. Our first task is to find a way to describe this rotation. The key to this is to introduce an angular velocity vector. 

Let's start with a simple situation. We will take the $z$ -axis of $S$ to be aligned with the $z'$ -axis of $S'$ , as shown in the figure. We let the angle $\theta$ between the $x$ -axis and $x'$ -axis vary as $\theta(t)$ . Then the angular velocity vector $\omega$ is defined to be 

$$
\omega = \dot {\theta} \hat {\mathbf {z}}.\tag{6.1}
$$

Previously, we referred to $\dot{\theta}$ as the angular velocity or angular speed. We see that the vector $\omega$ extends this to include information about the direction around which you rotate, in this case the z-axis. 

You should think of the direction of $\omega$ in a right-handed sense. This means that you point the thumb of your right hand in the direction of $\omega$ and curl your fingers around to see the direction of rotation. 

Consider a particle that is sitting stationary in the frame $S'$ . From the perspective of frame S, this particle will rotate around the z-axis. There is a beautifully simple formula that describes the motion of this particle as seen from frame S: it is 

$$
\dot {\mathbf {x}} = \boldsymbol {\omega} \times \mathbf {x}.\tag{6.2}
$$

This formula follows by just thinking geometrically about what's going on, as in the figure to the right. This formula ensures that the speed of the particle $|\dot{\mathbf{x}}|$ is proportional to the distance from the axis of rotation $\omega$ . In particular, if the particle lies along the axis of rotation, so that $\mathbf{x}$ is parallel to $\omega$ , then we have $\dot{\mathbf{x}} = 0$ , as the particle doesn't rotate. 

The formula $(6.2)$ continues to hold if $\omega$ points in any direction, not just along the z-axis. More importantly, it also holds if the axis of rotation changes in time. This means that we can have $\omega = \omega(t)$ , where both the magnitude and direction of $\omega$ depend on time, and $(6.2)$ tells us that instantaneous velocity of particle embedded in the rotating frame $S'$ . 

We can also extend the description (6.2) to the axes of $S'$ themselves. Let $\mathbf{e}_i'$ , for $i = 1, 2, 3$ , be the unit vectors that point along the $x'$ , $y'$ and $z'$ directions of $S'$ . Then, viewed from frame $S$ , these too rotate with velocity 

$$
\dot {\mathbf {e}} _ {i} ^ {\prime} = \boldsymbol {\omega} \times \mathbf {e} _ {i} ^ {\prime}.\tag{6.3}
$$

This will be the main formula that will allow us to understand motion in rotating frames. 

## 6.1.1 Velocity and Acceleration in a Rotating Frame

Now consider a particle which is no longer stuck in the $S'$ frame, but moves on some trajectory. We can measure the position of the particle in the inertial frame S where we write 

$$
\mathbf {x} = x _ {i} \mathbf {e} _ {i}.\tag{6.4}
$$

Here we're using the summation convention in which the repeated $i$ index is summed over its different values $i = 1,2,3$ . The unit vectors $\mathbf{e}_i$ , with $i = 1,2,3$ , point along the axes of $S$ . Alternatively, we can measure the position of the particle using axes aligned with the frame $S'$ 

$$
\mathbf {x} = x _ {i} ^ {\prime} \mathbf {e} _ {i} ^ {\prime}.\tag{6.5}
$$

The position vector x is the same in both of these expressions, but the coordinates $x_{i}$ and $x_{i}^{\prime}$ differ because they are measured with respect to different axes. Now, we can compute an expression for the velocity of the particle. Measured with respect to the axes of frame S, it is 

$$
\dot {\mathbf {x}} = \dot {x} _ {i} \mathbf {e} _ {i}\tag{6.6}
$$

because the axes $e_{i}$ do not change with time. However, when we measure the position with respect to the $e_{i}^{\prime}$ axes of frame $S^{\prime}$ , then we have 

$$
\begin{array}{r l} & {\dot {\mathbf {x}} = \dot {x} _ {i} ^ {\prime} \mathbf {e} _ {i} ^ {\prime} + x _ {i} ^ {\prime} \dot {\mathbf {e}} _ {i} ^ {\prime}} \\ & {\quad = \dot {x} _ {i} ^ {\prime} \mathbf {e} _ {i} ^ {\prime} + x _ {i} ^ {\prime} \pmb {\omega} \times \mathbf {e} _ {i} ^ {\prime}} \\ & {\quad = \dot {x} _ {i} ^ {\prime} \mathbf {e} _ {i} ^ {\prime} + \pmb {\omega} \times \mathbf {x}.} \end{array}\tag{6.7}
$$

We'll introduce a slightly novel notation to help highlight the physics hiding in (6.6) and (6.7). We write the velocity of the particle as seen by an observer in frame $S$ as 

$$
\left(\frac {d \mathbf {x}}{d t}\right) _ {S} = \dot {x} _ {i} \mathbf {e} _ {i}.\tag{6.8}
$$

Similarly, the velocity as seen by an observer in frame $S'$ is just 

$$
\left(\frac {d \mathbf {x}}{d t}\right) _ {S ^ {\prime}} = \dot {x} _ {i} ^ {\prime} \mathbf {e} _ {i} ^ {\prime}.\tag{6.9}
$$

From equations $(6.6)$ and $(6.7)$ , we see that the two observers measure different velocities 

$$
\left(\frac {d \mathbf {x}}{d t}\right) _ {S} = \left(\frac {d \mathbf {x}}{d t}\right) _ {S ^ {\prime}} + \boldsymbol {\omega} \times \mathbf {x}.\tag{6.10}
$$

This is not completely surprising: the difference $\omega \times x$ is just the relative velocity of the two frames at point x. 

What about acceleration? We can play the same game. Measuring acceleration relative to the axes $e_{i}$ , we have 

$$
\ddot {\mathbf {x}} = \ddot {x} _ {i} \mathbf {e} _ {i}.\tag{6.11}
$$

When measured with respect to the axes $e_{i}^{\prime}$ , the expression is a little more complicated. Differentiating (6.7) once more, we have 

$$
\begin{array}{r l} & {\ddot {\mathbf {x}} = \ddot {x} _ {i} ^ {\prime} \mathbf {e} _ {i} ^ {\prime} + \dot {x} _ {i} ^ {\prime} \dot {\mathbf {e}} _ {i} ^ {\prime} + \dot {x} _ {i} ^ {\prime} \pmb {\omega} \times \mathbf {e} _ {i} ^ {\prime} + x _ {i} ^ {\prime} \dot {\pmb {\omega}} \times \mathbf {e} _ {i} ^ {\prime} + x _ {i} ^ {\prime} \pmb {\omega} \times \dot {\mathbf {e}} _ {i} ^ {\prime}} \\ & {\quad = \ddot {x} _ {i} ^ {\prime} \mathbf {e} _ {i} ^ {\prime} + 2 \dot {x} _ {i} ^ {\prime} \pmb {\omega} \times \mathbf {e} _ {i} ^ {\prime} + \dot {\pmb {\omega}} \times \mathbf {x} + x _ {i} ^ {\prime} \pmb {\omega} \times (\pmb {\omega} \times \mathbf {e} _ {i} ^ {\prime}).} \end{array}
$$

As with velocities, the acceleration seen by the observer in S is $\ddot{x}_{i}e_{i}$ , while the acceleration seen by the observer in $S'$ is $\ddot{x}_{i}'e_{i}'$ . Equating the two expressions for $\ddot{x}$ above gives 

$$
\left(\frac {d ^ {2} \mathbf {x}}{d t ^ {2}}\right) _ {S} = \left(\frac {d ^ {2} \mathbf {x}}{d t ^ {2}}\right) _ {S ^ {\prime}} + 2 \pmb {\omega} \times \left(\frac {d \mathbf {x}}{d t}\right) _ {S ^ {\prime}} + \dot {\pmb {\omega}} \times \mathbf {x} + \pmb {\omega} \times (\pmb {\omega} \times \mathbf {x})
$$

This is our key equation. It contains everything we need to understand the motion of particles in a rotating frame. 

## 6.2 Newton's Equation of Motion in a Rotating Frame

With the hard work behind us, let's see how Newton's laws of motion would appear to a person sitting in the rotating frame $S'$ . We know that in the inertial frame $S$ , we have 

$$
m \left(\frac {d ^ {2} \mathbf {x}}{d t ^ {2}}\right) _ {S} = \mathbf {F}.\tag{6.14}
$$

So, using $(6.13)$ , in frame $S'$ , we have 

$$
m \left(\frac {d ^ {2} {\bf x}}{d t ^ {2}}\right) _ {S ^ {\prime}} = {\bf F} - 2 m {\pmb \omega} \times \left(\frac {d {\bf x}}{d t}\right) _ {S ^ {\prime}} - m \dot {\pmb \omega} \times {\bf x} - m {\pmb \omega} \times (\pmb \omega \times {\bf x})
$$

We've moved the additional terms in (6.13) onto the right-hand side in (6.15), so that they accompany the force $\mathbf{F}$ . We see that an observer in the rotating frame $S'$ must invoke the existence of three further terms in Newton's equation to describe the motion of a particle. These are called fictitious forces. Viewed from $S'$ , a free particle doesn't travel in a straight line and these fictitious forces are necessary to explain this departure from uniform motion. In the rest of this chapter, we will explore the consequences of these fictitious forces. 

Each of the three terms on the right-hand side of $(6.15)$ is given a name: 

- The $-m\boldsymbol{\omega} \times (\boldsymbol{\omega} \times \mathbf{x})$ term is called the centrifugal force. 

- The $-2m\omega \times \dot{\mathbf{x}}$ term is the Coriolis force. 

- The $-m\dot{\omega} \times \mathbf{x}$ term is called the Euler force. 

The most familiar non-inertial frame is the room you are sitting in. It rotates once per day around the north-south axis of the Earth. It further rotates once a year about the Sun which, in turn, rotates about the centre of the galaxy. From these time scales, we can easily compute $\omega = |\omega|$ . 

The radius of the Earth is $R_{Earth} \approx 6 \times 10^{3}$ km. The Earth rotates with angular frequency 

$$
\omega_ {\mathrm{rot}} = \frac {2 \pi}{1 \mathrm{day}} \approx 7 \times 1 0 ^ {- 5} \mathrm{s} ^ {- 1}.\tag{6.16}
$$

The distance from the Earth to the Sun is $a_{e} \approx 1.5 \times 10^{8}$ km. The angular frequency of the orbit is 

$$
\omega_ {\mathrm{orb}} = \frac {2 \pi}{1 \mathrm{year}} \approx 2 \times 1 0 ^ {- 7} \mathrm{s} ^ {- 1}.\tag{6.17}
$$

It should come as no surprise to learn that $\omega_{rot}/\omega_{orb}=T_{orb}/T_{rot}\approx365$ . 

In what follows, we will see the effect of the centrifugal and Coriolis forces on our daily lives. We will not discuss the Euler force, which arises only when the speed of the rotation changes with time. Although this plays a role in various funfair rides, it's not important in the frame of an Earth-based lab. (The angular velocity of the Earth's rotation does, in fact, have a small, but non-vanishing, $\dot{\omega}$ due to the precession and nutation of the Earth's rotational axis. However, it is tiny, with $\dot{\omega} \ll \omega^2$ and, as far as I know, the resulting Euler force has no consequence.) 

## Inertial vs Gravitational Mass Revisited

All the fictitious forces are proportional to the inertial mass m. There is no mystery here: it's because they all originate from the “ma” side of “F = ma” rather than the “F” side. But, as we mentioned in Section 2.3.3, experimentally, the gravitational force also appears to be proportional to the inertial mass. Is this evidence that gravity too is a fictitious force? In fact it is! Einstein's theory of general relativity recasts gravity as the fictitious force that we experience due to the curvature of space and time. There will, in time, be a book. 

## 6.3 The Centrifugal Force

The centrifugal force is given by 

$$
\mathbf {F} _ {\mathrm{cent}} = - m \pmb {\omega} \times (\pmb {\omega} \times \mathbf {x}) = - m (\pmb {\omega} \cdot \mathbf {x}) \pmb {\omega} + m \omega^ {2} \mathbf {x}.\tag{6.}
$$

We can get a feel for this by looking at the figure to the right. The vector $\omega \times x$ points into the page, which means that $-\omega \times (\omega \times x)$ points away from the axis of rotation as shown. If we denote the distance to the axis of rotation as d, as shown in the figure, then we can write the magnitude of the centrifugal force as 

$$
| \mathbf {F} _ {\mathrm{cent}} | = m \omega^ {2} | \mathbf {x} | \cos \theta = m \omega^ {2} d.\tag{6.19}
$$

The centrifugal force does not depend on the velocity of the particle. In fact, it is an example of a conservative force. We can see this by writing 

$$
\mathbf {F} _ {\mathrm{cent}} = - \nabla V \quad \mathrm{with} \quad V = - \frac {m}{2} | \pmb {\omega} \times \mathbf {x} | ^ {2}.\tag{6.20}
$$

In a rotating frame, V can be interpreted as a potential energy associated to a particle. The potential V is negative and its magnitude increases with distance. This means that particles can lower their energy by flying out from the axis of rotation, increasing $|\omega \times x|$ . 

## 6.3.1 An Example: Apparent Gravity

Suspend a piece of string from the ceiling. You might expect that the string points down to the centre of the Earth. But the effect of the centrifugal force due to the Earth's rotation means that there is a subtlety. If we assume that the Earth is spherical, then the string points slightly away from “down”. We will first explain the physics at play, and then return to the assumption that the Earth is spherical at the end. 

A somewhat exaggerated picture of what's going on is shown in the figure. The question that we would like to answer is: what is the angle $\alpha$ that the string makes with the line pointing to the Earth's centre? As we will now show, the angle $\alpha$ depends on the latitude, $\phi$ , at which we're sitting. 

The effective acceleration, due to the combination of gravity and the centrifugal force, is 

$$
\mathbf {g} _ {\mathrm{eff}} = \mathbf {g} - \boldsymbol {\omega} \times (\boldsymbol {\omega} \times \mathbf {x}).\tag{6.21}
$$

It is useful to resolve this acceleration in the radial and latitudinal (or northerly) directions by using the unit vectors $\hat{r}$ and $\hat{\phi}$ . The centrifugal force $F_{cent}$ is resolved as 

$$
\begin{array}{r l} & {\mathbf {F} _ {\mathrm{cent}} = | \mathbf {F} _ {\mathrm{cent}} | \cos \phi \hat {\mathbf {r}} - | \mathbf {F} _ {\mathrm{cent}} | \sin \phi \hat {\boldsymbol {\phi}}} \\ & {\quad = m \omega^ {2} r \cos^ {2} \phi \hat {\mathbf {r}} - m \omega^ {2} r \cos \phi \sin \phi \hat {\boldsymbol {\phi}}} \end{array}\tag{6.22}
$$

with $r = |x|$ and where, in the second line, we have used the magnitude of the centrifugal force computed in (6.19). Notice that the centrifugal force is largest at the equator at $\phi = 0$ , and vanishes at the poles $\phi = \pm\pi/2$ . This gives the effective acceleration 

$$
\begin{array}{r l} & {\mathbf {g} _ {\mathrm{eff}} = - g \hat {\mathbf {r}} - \boldsymbol {\omega} \times (\boldsymbol {\omega} \times \mathbf {x})} \\ & {\quad = (- g + \omega^ {2} R \cos^ {2} \phi) \hat {\mathbf {r}} - \omega^ {2} R \cos \phi \sin \phi \hat {\boldsymbol {\phi}}} \end{array}\tag{6.23}
$$

where R is the radius of the Earth. 

In our problem, the force $mg_{eff}$ must be balanced by the tension T in the string. This too can be resolved as 

$$
\mathbf {T} = T \cos \alpha \hat {\mathbf {r}} + T \sin \alpha \hat {\boldsymbol {\phi}}.\tag{6.24}
$$

At equilibrium, we need $mg_{eff} + T = 0$ , which allows us to eliminate T (by, for example, dotting with a vector perpendicular to T). We get an equation relating the angle $\alpha$ that the string makes to the latitude $\phi$ 

$$
\tan \alpha = \frac {\omega^ {2} R \cos \phi \sin \phi}{g - \omega^ {2} R \cos^ {2} \phi}.\tag{6.25}
$$

This is the answer we wanted. Let's see at what latitude the angle $\alpha$ is largest. If we compute $d(\tan \alpha) / d\phi$ , we find a fairly complicated expression. However, if we take into account the fact that $\omega^2 R \approx 3 \times 10^{-2} \mathrm{~ms}^{-2} \ll g$ then we can neglect the term in the 

denominator when differentiating. We learn that the maximum departure from the vertical occurs more or less when $d(\cos \phi \sin \phi) / d\phi = 0$ . Or, in other words, at a latitude of $\phi \approx 45^{\circ}$ . However, even at this point the deflection from the vertical is tiny, with order of magnitude $\alpha \approx 10^{-3}$ . 

When we sit at the equator, with $\phi = 0$ , then $\alpha = 0$ and the string hangs directly towards the centre of the Earth. However, gravity is somewhat weaker due to the centrifugal force. We have 

$$
\left. g _ {\mathrm{eff}} \right| _ {\mathrm{equator}} = g - \omega^ {2} R.\tag{6.26}
$$

Based on this, we expect $g - g_{eff} \approx 3 \times 10^{-2} \, m s^{-2}$ at the equator. 

Finally, we can return to our original assumption that the Earth is spherical. This isn't true, and the reason it isn't true can also be traced to the centrifugal force which acts not only on pendulums but also on the Earth itself. This means that the Earth bulges at the equator, in such a way that the force on a stationary particle is exactly normal to the Earth's surface. 

## A Rotating Bucket

Fill a bucket with water and spin it. In equilibrium, the surface of the water will form a concave shape like that shown in the figure. What is the shape? 

The water that is in contact with the bucket necessarily spins at the same speed as the bucket. (This is the so-called “no slip” boundary condition that will be described in detail in Volume 4 on Fluid Mechanics.) That ensures that the fluid inside is spinning with some velocity profile. 

A small parcel of the fluid then has a potential energy that receives two contributions: one from gravity and the other due to the centrifugal force given in $(6.20)$ 

$$
V _ {\mathrm{water}} = m g z - \frac {1}{2} m \omega^ {2} r ^ {2}.\tag{6.27}
$$

Now we use a somewhat slick physics argument. Consider a small parcel of water on the surface of the fluid. If it could lower its energy by moving along the surface, then it would. But we're looking for the equilibrium shape of the surface, which means that each point on the surface must have equal potential energy. This means that the shape of the surface is governed by the equation 

$$
z = \frac {\omega^ {2} r ^ {2}}{2 g} + \mathrm{constant}.\tag{6.28}
$$

So the surface of the water should be a parabola. 

## 6.3.2 The Roche Limit

In astrophysics, two stars that orbit each other are known as a binary system. There is a limit on how far these two stars can approach before the gravitational attraction of one starts to pull the other apart. It is straightforward to compute this using the centrifugal force. 

We take the two stars to have masses $M_{1}$ and $M_{2}$ and radii $R_{1}$ and $R_{2}$ . We’ll further assume that they sit on a circular orbit of radius r. This means that the two stars orbit their common centre of mass with angular velocity $\omega$ satisfying 

$$
\omega^ {2} r = \frac {G (M _ {1} + M _ {2})}{r ^ {2}}.\tag{6.29}
$$

Consider a particle of mass m sitting on the surface of the first star. Of course, particles sitting on stars tend to burn up, so it's best to think of this “particle” as parcel of the plasma that makes up the star. It feels a pull downwards, towards the centre of the star, but also a gravitational pull upwards towards the second star. The total downwards force is 

$$
F = \frac {G M _ {1} m}{R _ {1} ^ {2}} - \frac {G M _ {2} m}{(r - R _ {1}) ^ {2}}.\tag{6.30}
$$

In addition, there is a centrifugal force. (We will assume that this orbital centrifugal force is much larger than that arising from the rotation of the star.) The distance from the centre of the first star to the centre of mass is $x = rM_{2}/(M_{1} + M_{2})$ . This means that the distance from the particle that we're considering to the centre of mass is $x - R_{1}$ , so the downwards centrifugal force is 

$$
F _ {\mathrm{cent}} = m \omega^ {2} \left(\frac {r M _ {2}}{M _ {1} + M _ {2}} - R _ {1}\right) = \frac {G m}{r ^ {3}} \Big (M _ {2} r - (M _ {1} + M _ {2}) R _ {1} \Big)
$$

where, in the second equality, we've used (6.29). The condition that the first star exerts a positive normal force on the mass is then 

$$
\frac {G M _ {1} m}{R _ {1} ^ {2}} - \frac {G M _ {2} m}{(r - R _ {1}) ^ {2}} + \frac {G m}{r ^ {3}} \Big (M _ {2} r - (M _ {1} + M _ {2}) R _ {1} \Big) > 0.
$$

If this inequality is not satisfied, then a particle sitting on the surface of the first star will fly off. Said differently, if we want to neglect tidal forces on the near side of the star, then we better make sure that this inequality is amply satisfied, meaning 

$$
\frac {M _ {1}}{R _ {1} ^ {2}} - \frac {M _ {2}}{(r - R _ {1}) ^ {2}} \gg \frac {1}{r ^ {3}} \left((M _ {1} + M _ {2}) R _ {1} - M _ {2} r\right).\tag{6.33}
$$

Meanwhile, there's a similar story for the far side of the star. The requirement that this is not affected by tidal forces is 

$$
\frac {M _ {1}}{R _ {1} ^ {2}} + \frac {M _ {2}}{(r + R _ {1}) ^ {2}} \gg \frac {1}{r ^ {3}} \left((M _ {1} + M _ {2}) R _ {1} + M _ {2} r\right).\tag{6.34}
$$

Typically, this is of interest when the second star is bigger than the first. (It's also of interest when considering planets orbiting stars.) In this case, we take $r \gg R_1$ and add (6.33) and (6.34), Taylor expanding the $1 / (r \pm R_1)^2$ terms, to find the condition that we may neglect tidal forces 

$$
r \gg R _ {1} \left(1 + \frac {3 M _ {2}}{M _ {1}}\right) ^ {1 / 3}.\tag{6.35}
$$

This is known as the Roche limit. Two stars that orbit closer than this are in peril of being ripped apart. 

I should confess that the approximations we make in this section are pretty crude. We don't for example, take into account the deformation of one star due to the other. The advantage of these approximations is that we can focus on the key physics, but it does mean that the end result is not particularly realistic. It could be better viewed as the right result for a piece of dust on the surface of a small, spherical rock. 

Commonly, the Roche limit is written in terms of the densities $\rho_{1}$ and $\rho_{2}$ of the two stars. We have $M_{i}=4\pi\rho_{i}R_{i}^{3}$ . If we assume that $M_{1}\gg M_{2}$ , so that we may drop the +1, then we have 

$$
r \gg C R _ {2} \left(\frac {\rho_ {2}}{\rho_ {1}}\right) ^ {1 / 3}.\tag{6.36}
$$

for some numerical factor C. 

## 6.4 The Coriolis Force

The Coriolis force is given by 

$$
\mathbf {F} _ {\mathrm{cor}} = - 2 m \boldsymbol {\omega} \times \mathbf {v}.\tag{6.37}
$$

From the derivation in Section 6.2, $\mathbf{v} = (d\mathbf{x} / dt)_{S'}$ is the velocity of the particle measured in the rotating frame $S'$ . The force is velocity dependent: it is only felt by moving particles. Moreover, it is independent of the position. 

## 6.4.1 Particles, Baths, and Hurricanes

The mathematical form of the Coriolis force is identical to the Lorentz force $(2.74)$ describing a particle moving in a magnetic field. This means we already know what the effect of the Coriolis force will be when $\omega$ is constant: it makes moving particles turn in circles. 

We can easily check that this is indeed the case. Consider a particle moving on a spinning plane as shown in the figure, where $\omega$ is coming out of the page. In the diagram we have drawn various particle velocities, together with the Coriolis force (shown by the arrows with solid heads) experienced by the particle. We see that the effect of the Coriolis force is that a free particle travelling on the plane will move in a clockwise direction. 

There is a similar force, at least in principle, when you pull the plug from your bathroom sink. But here there's a subtle difference which actually reverses the direction of motion! 

Consider a fluid in which there is a region of low pressure. This region could be formed in a sink because we pulled the plug, or it could be formed in the atmosphere due to random weather fluctuations. Now the particles in the fluid will move radially towards the low pressure region, as shown in Figure 6.1. As they move, they will be deflected by the Coriolis force as shown on the left of Figure 6.1. The direction of the deflection is the same as that of a particle moving in the plane. But the net effect, as shown on the right of Figure 6.1, is that the swirling fluid moves in an anti-clockwise direction. 

Fig. 6.1 As the fluid moves towards the low pressure, it is deflected by the Coriolis force. 

The Coriolis force is responsible for the large scale motion of the ocean and atmosphere. (This is described in Volume 4 on Fluid Mechanics: see the section titled “An Introduction to Geophysical Flows”.) The Coriolis force is also responsible for the formation of hurricanes. These rotate in an anti-clockwise direction in the Northern Hemisphere and a clockwise direction in the Southern Hemisphere; two examples are shown in Figure 6.2. However, don’t spend too long staring at the rotation in your bath, hoping to see a preferred rotation direction as the water spirals down the plughole. Although the effect can be reproduced in laboratory settings, in your bathroom the Coriolis force is too small: it is no more likely to make your bath water change direction than it is to make an old record player change direction. 

Fig. 6.2 On the left, tropical cyclone Ingrid over the Coral Sea in 2005. On the right, hurricane Elena over the gulf of Mexico in 1985. Even if your geography isn't great, you can tell whether these hurricanes were in the Northern or Southern Hemisphere by their direction of rotation. 

Our discussion above supposed that objects were moving on a plane which is perpendicular to the angular velocity $\omega$ . But that's not true for hurricanes: they move along the surface of the Earth, which means that their velocity has a component parallel to $\omega$ . In this case, the effective magnitude of the Coriolis force gets a geometric factor, 

$$
| \mathbf {F} _ {\mathrm{cor}} | = 2 m | \hat {\mathbf {n}} \times (\pmb {\omega} \times \mathbf {v}) | = 2 m \omega v | \hat {\mathbf {n}} \cdot \hat {\pmb {\omega}} | = 2 m \omega v \sin \phi
$$

with $\hat{n}$ the normal to the Earth's surface and $\phi$ measuring latitude. 

It's simplest to see that the $\sin \phi$ factor makes sense in the case of a particle travelling north. Here the Coriolis force acts in an easterly direction and a little bit of trigonometry shows that the force has magnitude $2m\omega v\sin \phi$ as claimed. This is particularly clear at the equator where $\phi = 0$ . Here a particle travelling north has $\mathbf{v}$ parallel to $\omega$ and so the Coriolis force vanishes. 

It's a little more tricky to see the $\sin \phi$ factor for a particle travelling east. In this case, $\mathbf{v}$ is perpendicular to $\omega$ , so the magnitude of the force is actually $2m\omega v$ , with no trigonometric factor. However, the direction of the force no longer lies parallel to the Earth's surface: it has a component which points directly upwards. But we're not interested in this component for now as we will assume that it's negligible compared to gravity. 

Projecting onto the component that lies parallel to the Earth's surface (in a southerly direction in this case), we again get a $\sin \phi$ factor. 

The factor of $\sin\phi$ in (6.38) has an important meteorological consequence. The Coriolis force vanishes for particles moving along the Earth's surface when $\phi=0$ . This ensures that hurricanes do not form within 500 km of the equator. 

## 6.4.2 Balls and Towers

Climb up a tower and drop a ball. Where does it land? Since the Earth is rotating under the tower, you might think that the ball lands behind you. In fact, it lands in front! Let's see where this somewhat counterintuitive result comes from. 

The equation of motion in a rotating frame is 

$$
\ddot {\mathbf {x}} = \mathbf {g} - \boldsymbol {\omega} \times (\boldsymbol {\omega} \times \mathbf {x}) - 2 \boldsymbol {\omega} \times \dot {\mathbf {x}}.\tag{6.39}
$$

In what follows we will neglect the centrifugal term which, as we've seen, can be absorbed into the definition of $\mathbf{g}$ . In fact, we will ignore all terms of order $\mathcal{O}(\omega^2)$ (there will be one more coming shortly!). We will therefore solve the equation of motion 

$$
\ddot {\mathbf {x}} = \mathbf {g} - 2 \boldsymbol {\omega} \times \dot {\mathbf {x}}.\tag{6.40}
$$

The first step is easy: we can integrate this once to give 

$$
\dot {\mathbf {x}} = \mathbf {g} t - 2 \boldsymbol {\omega} \times (\mathbf {x} - \mathbf {x} _ {0})\tag{6.41}
$$

where we've introduced the initial position $\mathbf{x}_0$ as an integration constant. If we now substitute this back into the equation of motion (6.40), we get a messy, but manageable, equation. Let's, however, make our life easier by recalling that we've already agreed to drop terms of order $\mathcal{O}(\omega^2)$ . Then, upon substitution, we're left with 

$$
\ddot {\mathbf {x}} \approx \mathbf {g} - 2 \boldsymbol {\omega} \times \mathbf {g} t\tag{6.42}
$$

which we can easily integrate one last time to find 

$$
\mathbf {x} \approx \mathbf {x} _ {0} + \frac {1}{2} \mathbf {g} t ^ {2} - \frac {1}{3} \pmb {\omega} \times \mathbf {g} t ^ {3}.\tag{6.43}
$$

We pick a right-handed basis of vectors so that $\mathbf{e}_1$ points north, $\mathbf{e}_2$ points west and $\mathbf{e}_3 = \hat{\mathbf{r}}$ points radially outward as shown in the figure. However, we'll also make life easier for ourselves and assume that the tower sits at the equator. (This means that we don't have to worry about the annoying $\sin \phi$ factor that we saw in (6.38) and we will see again in the next section.) Then 

$$
\mathbf {g} = - g \mathbf {e} _ {3} \quad \text { and } \quad \boldsymbol {\omega} = \omega \mathbf {e} _ {1} \quad \text { and } \quad \mathbf {r} _ {0} = (R + h) \mathbf {e} _ {3}\tag{6.}
$$

where R is the radius of the Earth and h is the height of the tower. Our solution reads 

$$
\mathbf {x} \approx \left(R + h - \frac {1}{2} g t ^ {2}\right) \mathbf {e} _ {3} - \frac {1}{3} \omega g t ^ {3} \mathbf {e} _ {2}.\tag{6.45}
$$

The first term tells us the familiar result that the particle hits the ground in time $t^{2} = 2h/g$ . The last term gives the displacement, d, 

$$
d = - \frac {1}{3} \omega g \left(\frac {2 h}{g}\right) ^ {3 / 2} = - \frac {2 \omega}{3} \sqrt {\frac {2 h ^ {3}}{g}}.\tag{6.46}
$$

Recall that $e_{2}$ points west, so that the fact that d is negative means that the displacement is in the easterly direction. But the Earth rotates west to east. This means that the ball falls in front of the tower as promised. 

In fact, there is a simple intuitive way to understand this result. Although we have presented it as a consequence of the Coriolis force, it follows from the conservation of angular momentum. When dropped, the angular momentum (per unit mass) of the particle is 

$$
l = \omega (R + h) ^ {2}.\tag{6.47}
$$

This can't change as the ball falls. This means that the ball's final speed in the easterly direction is 

$$
R v = (R + h) ^ {2} \omega \Rightarrow v = \frac {(R + h) ^ {2} \omega}{R} > v _ {\mathrm{Earth}} = R \omega .
$$

So its tangential velocity is greater than that of the Earth's surface. This is the reason that it falls in front of the tower. 

## 6.4.3 Foucault's Pendulum

A pendulum placed at the North Pole will stay aligned with its own inertial plane while the Earth rotates beneath. An observer on the Earth would attribute this rotation of the pendulum's axis to the Coriolis force. What happens if we place the pendulum at some latitude $\phi$ ? 

We call the length of the pendulum $l$ . As in the previous example, we'll work with a right-handed orthonormal basis of vectors so that $\mathbf{e}_1$ points north, $\mathbf{e}_2$ points west and $\mathbf{e}_3 = \hat{\mathbf{r}}$ points radially outward from the Earth. We place the origin a distance $l$ below the pivot, so that when the pendulum hangs directly downwards the bob at the end sits on the origin. Finally, we ignore the centrifugal force (or think of it as already absorbed into $\mathbf{g}$ ). 

The equation of motion for the pendulum, including the Coriolis force, is 

$$
m \ddot {\mathbf {x}} = \mathbf {T} + m \mathbf {g} - 2 m \boldsymbol {\omega} \times \dot {\mathbf {x}}.\tag{6.49}
$$

Because the bob sits at the end of the pendulum, the coordinates are subject to the constraint 

$$
x ^ {2} + y ^ {2} + (l - z) ^ {2} = l ^ {2}.\tag{6.50}
$$

At latitude $\phi$ , the rotation vector is 

$$
\pmb {\omega} = \omega \cos \phi \mathbf {e} _ {1} + \omega \sin \phi \hat {\mathbf {r}}\tag{6.51}
$$

while the acceleration due to gravity is $g = -g\hat{r}$ . We also need an expression for the tension T, which points along the direction of the pendulum. Consulting the figure again, we can see that the tension is given by 

$$
\mathbf {T} = - \frac {T x}{l} \mathbf {e} _ {1} - \frac {T y}{l} \mathbf {e} _ {2} + \frac {T (l - z)}{l} \hat {\mathbf {r}}.\tag{6.52}
$$

As we'll soon see explicitly, the tension is not constant. It varies as the pendulum swings. Resolving the equation of motion along the axes gives us three equations 

$$
m \ddot {x} = - \frac {x T}{l} + 2 m \omega \dot {y} \sin \phi ,\tag{6.53}
$$

$$
m \ddot {y} = - \frac {y T}{l} + 2 m \omega (\dot {z} \cos \phi - \dot {x} \sin \phi),\tag{6.54}
$$

$$
m \ddot {z} = - m g + \frac {T (l - z)}{l} - 2 m \omega \dot {y} \cos \phi .\tag{6.55}
$$

These equations, together with the constraint $(6.50)$ , look rather formidable. To make progress, we will assume that $x/l \ll 1$ and $y/l \ll 1$ , and work to leading order in these small dimensionless numbers. 

This approximation is not as random as it may seem: Foucault's original pendulum hangs in the Pantheon in Paris and is 67 meters long, with the amplitude of the swing a few meters. The advantage of this approximation becomes apparent when we revisit the constraint (6.50) which tells us that $z / l$ is second order 

$$
l - z = l \sqrt {1 - \frac {x ^ {2}}{l ^ {2}} - \frac {y ^ {2}}{l ^ {2}}} \approx l - \frac {x ^ {2}}{2 l} - \frac {y ^ {2}}{2 l} + \dots\tag{6.56}
$$

This means that, to leading order, we can set $z$ , $\dot{z}$ and $\ddot{z}$ , all to zero. Then (6.55) provides an equation that will soon allow us to eliminate $T$ 

$$
T \approx m g + 2 m \omega \dot {y} \cos \phi .\tag{6.57}
$$

Meanwhile, we rewrite the first two equations (6.53) and (6.54) using the same trick we saw in our study of motion in a magnetic field in Section 2.4.1: we introduce the complex coordinate $\xi = x + iy$ and add (6.53) to $i$ times (6.54) to get 

$$
\ddot {\xi} \approx - \frac {g}{l} \xi - 2 \omega i \dot {\xi} \sin \phi .\tag{6.58}
$$

Here we have substituted $T \approx mg$ since the second term in (6.57) contributes only at sub-leading order. This is the equation of motion for a damped harmonic oscillator, albeit with a complex variable and, crucially, a factor of i in front of the $\dot{\xi}$ term which means that there's not actually any friction involved. We can solve it in the same way: the ansatz $\xi = e^{\beta t}$ results in the quadratic equation 

$$
\beta^ {2} + 2 i \omega \beta \sin \phi + \frac {g}{l} = 0\tag{6.59}
$$

which has solutions 

$$
\beta_ {\pm} = - i \omega \sin \phi \pm i \sqrt {\omega^ {2} \sin^ {2} \phi + \frac {g}{l}} \approx - i \left(\omega \sin \phi \mp \sqrt {\frac {g}{l}}\right) .
$$

From this we can write the general solution as 

$$
\xi = e ^ {- i \omega t \sin \phi} \left(A \cos \sqrt {\frac {g}{l}} t + B \sin \sqrt {\frac {g}{l}} t\right).\tag{6.61}
$$

Without the overall phase factor, $e^{-i\omega t \sin \phi}$ , this equation describes an ellipse. The role of the phase factor is to make the orientation of the ellipse slowly rotate in the $(x, y)$ -plane. Viewed from above, the rotation is clockwise in the Northern Hemisphere; anti-clockwise in the Southern Hemisphere. Notice that the period of rotation is not 24 hours unless the pendulum is suspended at the poles. Instead the period is $24/\sin\phi$ hours. In the Paris Pantheon, this is 32 hours. 

## 6.4.4 Orbital Precession in a Magnetic Field

The transformation to rotating frames can also be used as a cute trick to solve certain problems. Here's an example. 

Consider a particle with electric charge q in orbit around a second, fixed particle of charge Q, where $\text{sign}(q) = -\text{sign}(Q)$ . This is the two body problem that we studied in Chapter 5 where we learned that the orbits will be ellipses. Now we add to this setup an extra ingredient: a constant magnetic field B. What happens? 

The equation of motion is 

$$
m \ddot {\mathbf {x}} = - \frac {k}{r ^ {2}} \hat {\mathbf {r}} + q \dot {\mathbf {x}} \times \mathbf {B}
$$

where $k = qQ / 4\pi \epsilon_0$ . To solve this, we'll look at the same problem in a frame that rotates with angular velocity $\omega$ . Using (6.10) and (6.13), we have 

$$
m \left(\ddot {\mathbf {x}} + 2 \pmb {\omega} \times \dot {\mathbf {x}} + \pmb {\omega} \times (\pmb {\omega} \times \mathbf {x})\right) = - \frac {k}{r ^ {2}} \hat {\mathbf {r}} + q \left(\dot {\mathbf {x}} + \pmb {\omega} \times \mathbf {x}\right) \times \mathbf {B}
$$

where now x describes the coordinates of the relative position vector in the rotating frame. Now we do something clever: we use the fact that the mathematical form of the Coriolis and Lorentz forces are identical to pick the angular velocity of rotation $\omega$ so that the $\dot{x}$ terms above cancel. This works for 

$$
\pmb {\omega} = - \frac {q \mathbf {B}}{2 m}.\tag{6.62}
$$

Then the equation of motion becomes 

$$
m \ddot {\mathbf {x}} = - \frac {k}{r ^ {2}} \hat {\mathbf {r}} + \frac {q ^ {2}}{4 m} \mathbf {B} \times (\mathbf {B} \times \mathbf {x}).\tag{6.63}
$$

This is almost of the form that we studied in Chapter 5. In fact, if the magnetic field is suitably small, with $B^2 \ll 4mk/q^2r^3$ , then we can just ignore the last term. In this limit we get our old elliptic solution. But that's in the rotating frame. If we transform back to our original frame, we learn that the ellipse will rotate. 

If the magnetic field B is perpendicular to the plane of the orbit (so that B is parallel to L), then the effect will be that the ellipse precesses. This precession occurs with angular speed $\omega = qB/2m$ , half the cyclotron frequency that we met in Section 2.4.1. 

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

## Homogeneity of Space and Momentum

Consider the system of N particles with Lagrangian 

$$
L = \frac {1}{2} \sum_ {a = 1} ^ {N} m _ {a} \dot {\mathbf {x}} _ {a} ^ {2} - V (| \mathbf {x} _ {a} - \mathbf {x} _ {b} |).\tag{7.134}
$$

Crucially, the potential depends only on the distance $|x_{a}-x_{b}|$ between any two particles. This Lagrangian has the symmetry of translation. This means that the Lagrangian is unchanged if we instead consider paths $\mathbf{x}_{a}(t)\to\mathbf{x}_{a}(t)+s\hat{\mathbf{n}}$ for any constant unit vector $\hat{n}$ and for any constant $s\in R$ , so that 

$$
L (\mathbf {x} _ {a}, \dot {\mathbf {x}} _ {a}, t) = L (\mathbf {x} _ {a} + s \hat {\mathbf {n}}, \dot {\mathbf {x}} _ {a}, t).\tag{7.135}
$$

This is the statement that space is homogeneous and a translation of the system by $s\hat{n}$ does nothing to the equations of motion. These translations are elements of the Galilean group that we met in Chapter 1. From Noether's theorem, we can compute the conserved quantity associated with translations in the $\hat{n}$ direction. It is 

$$
Q = \sum_ {a} \frac {\partial L}{\partial \dot {\mathbf {x}} _ {a}} \cdot \hat {\mathbf {n}} = \sum_ {a} \mathbf {p} _ {a} \cdot \hat {\mathbf {n}}\tag{7.136}
$$

which we recognise as the total linear momentum in the direction $\hat{n}$ . Since this holds for all $\hat{n}$ , we conclude that $\sum_{a} p_{a}$ is conserved. But this is very familiar. It is simply the conservation of total linear momentum that we previously met in Chapter 4. To summarise: 

$$
\begin{array}{r c l} \text {homogeneity of space} & \Longrightarrow & \text {translation invariance of L} \\ & \Longrightarrow & \text {conservation of total linear momentum} \end{array}
$$

This statement should be intuitively clear. One point in space is much the same as any other, so a system of particles doesn't feel the need to scurry to move to some special place. This manifests itself as conservation of linear momentum. 

## Isotropy of Space and Angular Momentum

The isotropy of space is the statement that there is no special direction. This manifests itself as the invariance of the Lagrangian $(7.134)$ when all positions $x_{a}$ are rotated about some axis by the same amount. 

To work out the corresponding conserved quantities it will suffice to work with the infinitesimal form of the rotation about an axis $\hat{n}$ 

$$
\mathbf {x} _ {a} \rightarrow \mathbf {x} _ {a} + \delta \mathbf {x} _ {a} = \mathbf {x} _ {a} + \alpha \hat {\mathbf {n}} \times \mathbf {x} _ {a}\tag{7.137}
$$

where $\alpha$ is considered infinitesimal and is playing the role of the variable that we previously called $s$ . To see that this is indeed a rotation, you could calculate the length of the vector $\mathbf{x}_a + \delta \mathbf{x}_a$ and check that it's preserved to linear order in $\alpha$ . The invariance of the Lagrangian means that, also to linear order in $\alpha$ , we have 

$$
L (\mathbf {x} _ {a}, \dot {\mathbf {x}} _ {a}) = L (\mathbf {x} _ {a} + \alpha \hat {\mathbf {n}} \times \mathbf {x} _ {a}, \dot {\mathbf {x}} _ {a} + \alpha \hat {\mathbf {n}} \times \dot {\mathbf {x}} _ {a}).\tag{7.138}
$$

From this, we can use Noether's theorem to determine the conserved quantity 

$$
Q = \sum_ {a} \frac {\partial L}{\partial \dot {\mathbf {x}} _ {a}} \cdot (\hat {\mathbf {n}} \times \mathbf {x} _ {a}) = \sum_ {a} \hat {\mathbf {n}} \cdot (\mathbf {x} _ {a} \times \mathbf {p} _ {a}) = \hat {\mathbf {n}} \cdot \mathbf {L}.
$$

This is the component of the total angular momentum $L = \sum_{a} x_{a} \times p_{a}$ in the direction $\hat{n}$ . Since the vector $\hat{n}$ is arbitrary, we get the result 

$$
\begin{array}{r l} \mathrm{isotropyofspace} & \Longrightarrow \mathrm{rotationalinvarianceof} L \\ & \Longrightarrow \mathrm{conservationoftotalangularmomentum} \end{array}
$$

## Homogeneity of Time and Energy

Finally, we turn to the symmetry of time translation. The laws of physics are the same today as they were yesterday. Indeed, as far as we can tell, the laws of physics are the same today as they were during the Big Bang. In mathematical language, this means that $\partial L/\partial t = 0$ . 

But we already saw in $(7.121)$ that any system with $\partial L/\partial t = 0$ has a conserved energy 

$$
E = \dot {q} ^ {i} \frac {\partial L}{\partial \dot {q} ^ {i}} - L\tag{7.140}
$$

This is telling us that the existence of a conserved quantity that we call energy can be traced to the homogeneous passage of time. Or 

$$
\text { homogeneity   of   time } \implies \text { conservation   of   energy }.
$$

Putting this together with our previous result, we see that time is to energy as space is to momentum. 

Later, in Chapter 11, we will see that energy and 3-momentum naturally fit together in special relativity to form what's called a 4-vector, which rotates under spacetime transformations. Here we see that the link between energy-momentum and time-space exists even in the non-relativistic framework of Newtonian physics. You don't have to be Einstein to see it. You just have to be Emmy Noether. 

We've actually dodged a subtlety above. We didn't really invoke Noether's theorem to derive the energy (7.140), but just quoted a previous result. It's interesting to see how this arises from symmetry. If we shift the trajectories of all generalised coordinates to $q^i(t) \to q^i(t + s)$ then, treating $s$ as infinitesimal, to leading order we have 

$$
q ^ {i} (t) \rightarrow q ^ {i} (t) + s \dot {q} ^ {i} (t) \quad \text { and } \quad \dot {q} ^ {i} (t) \rightarrow \dot {q} ^ {i} (t) + s \ddot {q} ^ {i} (t) .
$$

Under this transformation, the Lagrangian itself is not actually invariant. Instead we have, again to leading order in s, 

$$
L (q ^ {i} (t + s), \dot {q} ^ {i} (t + s)) = L (q ^ {i} (t), \dot {q} ^ {i} (t)) + s \frac {d}{d t} L (q ^ {i} (t), \dot {q} ^ {i} (t)).
$$

This means that we're really in the realm of the slight generalisation of Noether's theorem presented in (7.132). The conserved quantity (7.133), with $G = L$ , coincides with the energy (7.140). 

## 7.5.2 Emmy Noether (1882–1935)

Emmy Noether was born in Erlangen, Germany. Her famous theorem relating symmetries to conservation laws was worked out in 1915 as a spin-off from attempts to understand certain properties of general relativity. 

Wonderful and important as her theorem is, my pure mathematician friends tell me that it is not even her best work. Her really clever stuff was in abstract algebra. 

Emmy Noether had to put up with no small amount of crap in her life. She worked at the University of Erlangen for seven years without pay. Her work gained recognition and, in 1915, she was invited by David Hilbert to take up a professorship at the University of Gottingen, then one of the leading centres of mathematics. Not everyone was happy. One member of the philosophy department wrote to Hilbert complaining “What will our soldiers think when they return to the university and find that they are required to learn at the feet of a woman?”. As a result, Noether was only allowed to give lectures under Hilbert’s name. The university finally deigned to pay her in 1923. 

More trouble came in the early 1930s when the Nazi Party's rise to power caused many of Germany's Jewish scientists to flee. Noether was among them. She found refuge in Bryn Mawr college, Pennsylvania, where she lectured until her death a few years later. 

## 7.6 Lagrangians for Fundamental Forces

The examples of Section 7.4 were all about beads and pendulums and the kind of mechanical systems that we think physics is about when we're 15. But now we're all grown up and sophisticated, we can look to more interesting things. And the real benefit of the Lagrangian formalism is that it introduces a paradigm that holds for all the fundamental laws of physics. 

Sadly, we're a little limited in what we can say at this stage. Ultimately, the fundamental laws of physics are field theories, rather than theories of particles. We will meet these in future books. But, to whet the appetite, in this section we apply the Lagrangian formalism to three examples involving particles. The first two are both familiar: the laws of gravity and electromagnetism. We will largely be recapitulating the properties of these forces, but will also use the power of the Lagrangian formalism to say some new things. The final example is a kind of warm up for ideas that will appear in the book on General Relativity. 

## 7.6.1 Gravity

We learned earlier in this book that any two particles, with masses $m_{1}$ and $m_{2}$ , separated by a distance r, experience a mutually attractive gravitational force given by the Newtonian potential 

$$
V (\mathbf {r}) = - \frac {G m _ {1} m _ {2}}{r}\tag{7.143}
$$

where $G$ is Newton's constant. We studied the dynamics of these two particles in some detail in Chapter 5 where we saw that the orbits are either ellipses or hyperbolae. Here we will first see how we can derive these same results in the Lagrangian formulation before we extend them in a slightly novel direction. 

## The Two-Body Problem Revisited

Two particles, with positions $x_{1}$ and $x_{2}$ , interacting through a potential $V(r)$ , with $r = x_{1} - x_{2}$ their separation, are described by the Lagrangian 

$$
\begin{array}{r l} & L = \frac {1}{2} m _ {1} \dot {\mathbf {x}} _ {1} ^ {2} + \frac {1}{2} m _ {2} \dot {\mathbf {x}} _ {2} ^ {2} - V (r) \\ & \quad = \frac {1}{2} (m _ {1} + m _ {2}) \dot {\mathbf {R}} ^ {2} + \frac {1}{2} \mu \dot {\mathbf {r}} ^ {2} - V (r). \end{array}\tag{7.144}
$$

Here R is the centre of mass, defined by $(m_{1} + m_{2})\mathbf{R} = m_{1}\mathbf{x}_{1} + m_{2}\mathbf{x}_{2}$ , and $\mu = m_{1}m_{2}/(m_{1} + m_{2})$ is the reduced mass. 

Importantly, the Lagrangian splits into two pieces. The centre of mass coordinate R appears in the Lagrangian with only a kinetic term. This reflects the fact that the centre of mass decouples from the dynamics and can be treated separately. Indeed, R is an example of an ignorable coordinate and the corresponding conserved quantity is just the total linear momentum $\mathbf{P} = (m_{1} + m_{2})\dot{\mathbf{R}}$ , telling us that the centre of mass drifts at some constant velocity. This is something that we already saw in Section 5.1.1. 

The Lagrangian for the separation r is more interesting, because it contains both a kinetic energy piece and a potential energy piece. This means that we have some work ahead of us in solving the equations of motion. 

We know from Noether's theorem that, because the Lagrangian has rotational symmetry, the angular momentum 

$$
\mathbf {J} = \mathbf {r} \times \mathbf {p}\tag{7.145}
$$

is conserved, where $\mathbf{p}$ is the momentum conjugate to $\mathbf{r}$ . In Chapter 5 (and in most of the subsequent books), we called the angular momentum vector $\mathbf{L}$ . But in the world of Lagrangians, the letter $L$ has already been taken. The letter $\mathbf{J}$ is our fall back option. 

At this stage, we repeat the arguments of Chapter 5. Since $J \cdot r = 0$ , the motion of the orbit must lie in a plane perpendicular to J. This allows us to turn the 3d problem described by the Lagrangian (7.144) into a 2d problem. Using polar coordinates $(r, \theta)$ , and ignoring the centre of mass piece, the Lagrangian (7.144) becomes 

$$
{\cal L} = \frac {1}{2} \mu (\dot {r} ^ {2} + r ^ {2} \dot {\theta} ^ {2}) - V (r) .\tag{7.146}
$$

To make further progress, we note that $\theta$ is ignorable so we can once again invoke Noether's theorem. This time it tells us that the magnitude of angular momentum 

$$
J = \mu r ^ {2} \dot {\theta}\tag{7.147}
$$

is conserved. To figure out the motion we calculate the Euler–Lagrange equation for r from $(7.146)$ 

$$
\frac {d}{d t} \left(\frac {\partial L}{\partial \dot {r}}\right) - \frac {\partial L}{\partial r} = \mu \ddot {r} - \mu r \dot {\theta} ^ {2} + \frac {\partial V}{\partial r} = 0.\tag{7.148}
$$

We then eliminate $\dot{\theta}$ from this equation by writing it in terms of the constant J to get a differential equation for the orbit purely in terms of r, 

$$
\mu \ddot {r} = - \frac {\partial}{\partial r} V _ {\mathrm{eff}} (r)\tag{7.149}
$$

where the effective potential $V_{eff}$ includes the additional term from the angular momentum barrier, 

$$
V _ {\mathrm{eff}} (r) = V (r) + \frac {J ^ {2}}{2 \mu r ^ {2}}.\tag{7.150}
$$

This is the same equation that we derived in Chapter 5. (See (5.27) and (5.28).) 

Let me reiterate a warning that we gave already when discussing the spherical pendulum: do not substitute $J = \mu r^{2} \dot{\phi}$ directly into the Lagrangian – you will get a minus sign wrong! You must substitute it into the equations of motion. 

If, however, we really want a Lagrangian that describes the dynamics for some fixed angular momentum J, then we can simply work with the effective potential, 

$$
{\cal L} = \frac {1}{2} \mu \dot {r} ^ {2} - V _ {\mathrm{eff}} (r) .\tag{7.151}
$$

This is a good time to point out that the Lagrangian approach isn't a magic bullet that allows us to solve problems without any work. The Lagrangian merely allows us to capture the equations of motion in a compact form, and then identify the conservation laws through symmetries. This provides some minor advantages in deriving the equation of motion (7.148). However, it doesn't actually help us solve this equation of motion. For that, we have to go back to the methods that we introduced in Chapter 5. 

Nonetheless, as our examples get more complicated, the advantages of having a Lagrangian that encapsulates the dynamics in one simple expression become greater. 

## The Restricted Three-Body Problem

We'll now use the Lagrangian machinery to describe something novel. We will stick with gravity, but we up the ante and consider three particles instead of two. Now the problem becomes more challenging. In fact, as we've mentioned previously, the general the problem of three or more particles interacting through gravity does not have a closed solution and we must resort to numerical methods. However, it turns out that, in 

particular limits, we can make progress with approximations. That is what we focus on here. 

We take our particles to have masses $m_{1}$ , $m_{2}$ , and $m_{3}$ . The limit of interest here is when $m_{3} \ll m_{1}$ , $m_{2}$ . Then it is a good approximation to first solve for the motion of $m_{1}$ and $m_{2}$ interacting alone, and then subsequently solve for the motion of $m_{3}$ in the time-dependent potential set up by $m_{1}$ and $m_{2}$ . This is known as the restricted three-body problem. It is a good description of, for example, the Sun–Earth–Moon system. We will now see how this works. 

For simplicity, let's assume $m_{1}$ and $m_{2}$ are in a circular orbit with the angular coordinate increasing as $\theta = \omega t$ . We know from Chapter 5 that the circular orbit occurs when $\partial V_{eff}/\partial r = 0$ , from which we get an expression relating the angular velocity of the orbit to the distance 

$$
\omega^ {2} = \frac {G (m _ {1} + m _ {2})}{r ^ {3}}.\tag{7.152}
$$

This is a special case of Kepler's third law. Let's further assume that $m_3$ moves in the same plane as $m_1$ and $m_2$ . (This is pretty good assumption for the Sun–Earth–Moon system.) To solve for the motion of $m_3$ in this background, we use our ability to change coordinates. We will go to a frame that rotates with $m_1$ and $m_2$ , with the centre of mass at the origin. 

We saw in Section 7.3.1 how to write down the Lagrangian in a rotating frame. We pick our frame so that the first particle, with mass $m_{1}$ , is a distance $r\mu/m_{1}$ from the origin, while the second is a distance $r\mu/m_{2}$ from the origin in the opposite direction. We can then write down the Lagrangian for the third particle (e.g. the Moon), following $(7.73)$ 

$$
{\cal L} = \frac {1}{2} m _ {3} \left[ (\dot {x} - \omega y) ^ {2} + (\dot {y} + \omega x) ^ {2} \right] - V .\tag{7.153}
$$

Here, V is the gravitational potential for the third particle interacting with the first two 

$$
V = - \frac {G m _ {1} m _ {3}}{r _ {1 3}} - \frac {G m _ {2} m _ {3}}{r _ {2 3}}.\tag{7.154}
$$

The separations are given by 

$$
r _ {1 3} ^ {2} = (x + r \mu / m _ {1}) ^ {2} + y ^ {2} \quad \mathrm{and} \quad r _ {2 3} ^ {2} = (x - r \mu / m _ {2}) ^ {2} + y ^ {2}.
$$

Be aware that x and y are the dynamical coordinates in this system, while r is the fixed separation between $m_{1}$ and $m_{2}$ . The equations of motion arising from L are 

$$
m _ {3} \ddot {x} = 2 m _ {3} \omega \dot {y} + m _ {3} \omega^ {2} x - \frac {\partial V}{\partial x}\tag{7.156}
$$

$$
m _ {3} \ddot {y} = - 2 m _ {3} \omega \dot {x} + m _ {3} \omega^ {2} y - \frac {\partial V}{\partial y}.\tag{7.157}
$$

The full solutions to these equations are interesting and complicated. In fact, in 1889, Poincaré studied the restricted three-body system and discovered the concept of chaos in dynamical systems for the first time. 

Here we'll be less ambitious and will search for solutions of the form $\dot{x} = \dot{y} = 0$ . This is where the third body sits stationary to the other two and the whole system rotates together. Physically, this arises because the centrifugal force of the third body exactly cancels its gravitational force. Needless to say, this is not what happens for the Moon! It is, however, a very useful exercise if we think of various satellites that experience the gravitational pull of both the Sun and the Earth. 

The equations we have to solve are 

$$
m _ {3} \omega^ {2} x = \frac {\partial V}{\partial x} = G m _ {1} m _ {3} \frac {x + r \mu / m _ {1}}{r _ {1 3} ^ {3}} + G m _ {2} m _ {3} \frac {x - r \mu / m _ {2}}{r _ {2 3} ^ {3}}
$$

$$
m _ {3} \omega^ {2} y = \frac {\partial V}{\partial y} = G m _ {1} m _ {3} \frac {y}{r _ {1 3} ^ {3}} + G m _ {2} m _ {3} \frac {y}{r _ {2 3} ^ {3}}.\tag{7.159}
$$

We now show that there are five solutions to these equations. First, suppose that y = 0 so that the particle with mass $m_{3}$ sits on the same line as those with masses $m_{1}$ and $m_{2}$ . Then we have to solve the algebraic equation 

$$
\omega^ {2} x = G m _ {1} \frac {x + r \mu / m _ {1}}{| x + r \mu / m _ {1} | ^ {3}} + G m _ {2} \frac {x - r \mu / m _ {2}}{| x - r \mu / m _ {2} | ^ {3}}.\tag{7.16}
$$

There are three solutions to this equation. To see this, we can plot the left-hand and right-hand sides of these equations, as shown in Figure 7.3. This shows that there is one solution in each of the regimes, 

$$
x <   - \frac {r \mu}{m _ {1}}, - \frac {r \mu}{m _ {1}} <   x <   \frac {r \mu}{m _ {2}}, x > \frac {r \mu}{m _ {2}}.\tag{7.161}
$$

Next, we look for solutions with $y \neq 0$ . From (7.159) we have 

$$
\frac {G m _ {2}}{r _ {2 3} ^ {3}} = \omega^ {2} - \frac {G m _ {1}}{r _ {1 3} ^ {3}}\tag{7.162}
$$

which we can substitute into $(7.158)$ . After a little algebra, we find the condition for solutions to be 

$$
\omega^ {2} = \frac {G (m _ {1} + m _ {2})}{r _ {1 3} ^ {3}} = \frac {G (m _ {1} + m _ {2})}{r _ {2 3} ^ {3}}\tag{7.163}
$$

which means that we must have $r_{13} = r_{23} = r$ . This tells us that the three particles form an equilateral triangle. There are two such points. 

Fig. 7.3 The three solutions sitting on the y = 0 line. 

The five stationary points are shown in Figure 7.4. They are known as Lagrange points. The three solutions (7.161) that have y = 0 are called $L_{1}$ , $L_{2}$ , and $L_{3}$ . Those with $y \neq 0$ that solve (7.163) are called $L_{4}$ and $L_{5}$ . 

Fig. 7.4 The five Lagrange points in the Earth–Sun system. 

For the Earth–Sun system, we make good use of the Lagrange points $L_{1}$ and $L_{2}$ to place satellites in orbits that sit at a constant distance from the Sun, and hence at a constant temperature. Both are about 1.5 million km away. Solar observatories sit at $L_{1}$ , between us and the Sun. Meanwhile, more cosmologically minded satellites sit at $L_{2}$ . In the past, this was home to WMAP and PLANCK, both important missions that measured the cosmic microwave background radiation in exquisite detail. (You can read more about what they found in the book on Cosmology.) The James Webb Telescope is one of the current inhabitants of $L_{2}$ . 

The Lagrange point $L_{3}$ hasn't yet found any use in science, but it has found plenty of use in science fiction. It's a popular location for authors to place an undiscovered planet, hidden at all times from the Earth by the Sun. We'll return to the Lagrange points in Section 8.1.3 where we analyse their stability. 

## 7.6.2 Electromagnetism

As we described in Chapter 2, a particle carrying electric charge q, moving in the background of an electric field $\mathbf{E}(\mathbf{x}, t)$ and a magnetic field $\mathbf{B}(\mathbf{x}, t)$ , experiences the Lorentz force given by 

$$
m \ddot {\mathbf {x}} = q (\mathbf {E} + \dot {\mathbf {x}} \times \mathbf {B}).\tag{7.164}
$$

Our task here is to write down a Lagrangian that reproduces this equation of motion. 

Here there is a surprise waiting for us. It turns out that there is no Lagrangian that depends on E and B that reproduces the Lorentz force law. There is a Lagrangian, but it's a little more subtle. 

That subtlety comes from the way we express the electric and magnetic fields E and B. It turns out that it is always possible to write the electric and magnetic fields in terms of two other functions, known as the electric potential $\phi(\mathbf{x}, t)$ and the vector potential $\mathbf{A}(\mathbf{x}, t)$ 

$$
\mathbf {E} = - \nabla \phi - \frac {\partial \mathbf {A}}{\partial t} \quad \mathrm{and} \quad \mathbf {B} = \nabla \times \mathbf {A}.\tag{7.165}
$$

We previously introduced the electric potential in Section 2.4 where we wrote a time-independent electric field as $\mathbf{E} = -\nabla \phi$ (see equation (2.77)). The first of the expressions above generalises this to the case where $\mathbf{E}$ depends on time. The second gives an analogous expression for the magnetic field. 

We'll spend a great deal of time discussing the potentials $\phi$ and $\mathbf{A}$ in Volume 2 on Electromagnetism. In the first few chapters of that book, we will see their utility: it is often a great deal easier to solve problems in electromagnetism in terms of these variables rather than $\mathbf{E}$ and $\mathbf{B}$ . But, in that context, we don't need to introduce the potentials. They are merely a useful device that makes calculations easier. 

Moreover, it is challenging to assign any physical meaning to the values of the potentials $\phi$ and $\mathbf{A}$ . This is because they're not uniquely defined. We are always at liberty to change these potentials by transformations of the form 

$$
\phi \rightarrow \phi - \frac {\partial \chi}{\partial t} \quad \mathrm{and} \quad \mathbf {A} \rightarrow \mathbf {A} + \nabla \chi\tag{7.166}
$$

for any function $\chi(\mathbf{x}, t)$ . This is known as a gauge transformation. Using the definitions (7.165), it's straightforward to show that the electric and magnetic fields $\mathbf{E}$ and $\mathbf{B}$ are unchanged under gauge transformations. But the potentials themselves certainly do change. 

The right way to think about this is that the specific values of $\phi$ and $\mathbf{A}$ are not something physical. There's no experiment that will tell you the values of $\phi$ and $\mathbf{A}$ at some particular point. More strikingly, there's no real meaning to the statement that these potentials have a definite value. For example, you might want to confidently claim that $\phi(\mathbf{x}, t)$ has value 17 (in some appropriate units) at, say, the tip of your nose, but someone else might wish to describe your nose with different potentials, related to yours by a gauge transformation. There's no point arguing about which choice is right and which is wrong. The different gauge choices are analogous to different coordinate systems, just a different set of conventions to describe the same underlying physics. 

This makes it all the more shocking that, as we move to more advanced theories of physics, the potentials $\phi$ and $\mathbf{A}$ play an increasingly prominent role. This is true, for example, in quantum mechanics which must be formulated in terms of $\phi$ and $\mathbf{A}$ , rather than $\mathbf{E}$ and $\mathbf{B}$ . And it is also true (for essentially the same reasons) of the Lagrangian approach to classical mechanics. The fact that these potentials aren't uniquely defined then brings an additional level of frisson to the story. 

We will now show that the dynamics of a particle carrying electric charge q, moving in the background of electric and magnetic fields, is described by the Lagrangian 

$$
L = \frac {1}{2} m \dot {\mathbf {x}} ^ {2} - q \phi (\mathbf {x}, t) + q \dot {\mathbf {x}} \cdot \mathbf {A} (\mathbf {x}, t)\tag{7.167}
$$

where the potentials $\phi$ and A are related to the electric and magnetic fields by (7.165). Note that the electric potential $\phi$ appears just like a potential energy term in the Lagrangian. But the vector potential term $\dot{x} \cdot A$ is something new: a velocity-dependent interaction term. 

To get going, we first compute the canonical momentum of the particle. It is 

$$
\mathbf {p} = \frac {\partial L}{\partial \dot {\mathbf {x}}} = m \dot {\mathbf {x}} + q \mathbf {A}.\tag{7.168}
$$

Here there's another minor surprise. The canonical momentum $\mathbf{p}$ is not the usual mass times velocity. It is altered in the presence of a magnetic field. We'll say a little more about this below. 

From here, it's straightforward to derive the Euler–Lagrange equation. We have 

$$
\frac {d}{d t} \left(\frac {\partial L}{\partial \dot {\mathbf {x}}}\right) - \frac {\partial L}{\partial \mathbf {x}} = \frac {d}{d t} (m \dot {\mathbf {x}} + q \mathbf {A}) + q \nabla \phi - q \nabla (\dot {\mathbf {x}} \cdot \mathbf {A}) = 0.
$$

To disentangle this, it's useful to work with indices $i, j = 1, 2, 3$ on the Cartesian coordinates, and rewrite the equation of motion as 

$$
m \ddot {x} ^ {i} = - q \left(\frac {\partial \phi}{\partial x ^ {i}} + \frac {\partial A _ {i}}{\partial t}\right) + q \left(\frac {\partial A _ {j}}{\partial x ^ {i}} - \frac {\partial A _ {i}}{\partial x ^ {j}}\right) \dot {x} ^ {j}.\tag{7.1}
$$

Happily, the potentials $\phi$ and A have arranged themselves back into the combinations E and B in this expression. This is simplest to see if we rewrite our original definition (7.165) in index form, so it reads 

$$
E _ {i} = - \frac {\partial \phi}{\partial x ^ {i}} - \frac {\partial A _ {i}}{\partial t}
$$

and 

$$
B _ {k} = \epsilon_ {k i j} \frac {\partial A _ {j}}{\partial x ^ {i}} \Rightarrow \frac {\partial A _ {j}}{\partial x ^ {i}} - \frac {\partial A _ {i}}{\partial x ^ {j}} = \epsilon_ {i j k} B _ {k}.\tag{7.171}
$$

The equation of motion then becomes 

$$
m \ddot {x} ^ {i} = q E _ {i} + q \epsilon_ {i j k} \dot {x} ^ {j} B _ {k}.\tag{7.172}
$$

This is the Lorentz force law $(7.164)$ in index notation. 

We saw from the beginning that the Lagrangian formulation is well adapted to conservative forces that can be written in terms of a potential. This means that it's no surprise to see the potential $\phi$ in the Lagrangian (7.167) giving rise to the electric part of the Lorentz force law (7.164). But we also mentioned that the Lagrangian formalism is no good at dealing with friction-type forces which are velocity dependent, like $F = -k\dot{x}$ . The ultimate reason why the Lagrangian formulation can deal with the Lorentz force law, but not friction, is that the magnetic part of the Lorentz force does no work, so energy remains conserved. 

The fact that the Lagrangian (7.167) results in equations of motion that depend only on E and B is reassuring. But we may still be a little nervous that the Lagrangian itself depends explicitly on $\phi$ and A, which suggests that the value of the action may also inherit the ambiguity inherent in the gauge transformation. To alleviate these nerves, we can look at what happens to the Lagrangian under a gauge transformation (7.166). We have 

$$
L \rightarrow L + q \frac {\partial \chi}{\partial t} + q \dot {\mathbf {x}} \cdot \nabla \chi = L + q \frac {d \chi}{d t}.\tag{7.173}
$$

The Lagrangian changes by a total derivative. We already noted in $(7.52)$ that this means that the action $S = \int dt L$ changes only by a constant, which explains why the equations of motion are independent of the function $\chi(\mathbf{x}, t)$ . 

Note, however, that the canonical momentum (7.168) does depend on the choice of gauge. This means that the momentum p can't have a physical meaning because it takes different values depending on the potential A that you choose to describe the magnetic field. Meanwhile, the usual momentum $m\dot{x}$ , sometimes called the mechanical momentum in this context, is physical but isn't the same thing as the generalised momentum $\partial L/\partial\dot{x}$ . At this point, this may sound like nothing more than a pedantic mathematical observation, but it has many interesting consequences that arise when we describe the quantum mechanics of particles in magnetic fields. We'll start to see hints of this in Chapter 10 when we turn to the Hamiltonian formalism. 

## An Example: A Particle in a Uniform Magnetic Field

We can build some intuition for some of the peculiarities of the Lagrangian by looking at the simple example of a particle moving in a uniform magnetic field $\mathbf{B} = (0, 0, B)$ . We already solved this example in Section 2.4.1. The equations of motion are 

$$
\ddot {x} = q B \dot {y}, \quad \ddot {y} = - q B \dot {x}, \quad \ddot {z} = 0.\tag{7.174}
$$

The particle travels at some constant speed in the $z$ -direction. This is boring and we'll ignore it. More interesting is the motion in the $(x, y)$ -plane. The equations are solved by 

$$
x = x _ {0} + R \sin (\omega t) \quad \text { and } \quad y = y _ {0} + R \cos (\omega t) .\tag{7.175}
$$

Here $x_{0}$ , $y_{0}$ , and R are all integration constants, while $\omega$ is the cyclotron frequency 

$$
\omega = \frac {q B}{m}.
$$

Now let's return to the Lagrangian. Obviously we will ultimately end up with the same equations of motion (7.174) and solution (7.175). But our interest here is what happens in the intermediate steps. In particular, to build the Lagrangian we must first find a vector potential $\mathbf{A}$ such that $\mathbf{B} = \nabla \times \mathbf{A}$ . There are many choices, related by gauge transformations. For example, we could pick 

$$
\mathbf {A} = (- B y, 0, 0) .\tag{7.176}
$$

The resulting Lagrangian for the motion in the plane is then 

$$
L = \frac {m}{2} (\dot {x} ^ {2} + \dot {y} ^ {2}) - q B \dot {x} y.\tag{7.177}
$$

At first glance, there's something a little disconcerting about this. Our magnetic field is uniform, so it looks as if our system has translational invariance in all directions. But the choice of the vector potential (7.176) 

is not translationally invariant in the y-direction. In fact, it turns out that there is no choice of A that respects all the symmetries of B. 

Given the relationship between translational invariance and momentum conservation, that may raise some alarm bells. It means that choosing $(7.176)$ has the consequence that $p_{y}$ is not conserved, even though the magnetic field itself is translationally invariant in the y-direction. 

This, it turns out, is a feature, not a bug. From $(7.168)$ , the momenta p are 

$$
p _ {x} = m \dot {x} - q B y \quad \mathrm{and} \quad p _ {y} = m \dot {y}.\tag{7.178}
$$

The fact that $\mathbf{A}$ in (7.176) depends on $y$ means that $p_y$ is not conserved. But that's ok! After all, we've seen that the particles go in circles (7.175), so it's certainly true that $\dot{y}$ is not a constant of motion. 

But $\mathbf{A}$ is independent of $x$ , so Noether's theorem tells us that $p_x$ is conserved. We have $p_x = m\dot{x} + qA_x$ , with the additional contribution from $A_x$ . So while it's certainly true that $\dot{x}$ is not a constant of motion, it's simple to check that the canonical momentum $p_x$ is a constant of motion when evaluated on the circle solution (7.175). 

The upshot is that the need to write the Lagrangian in terms of A, rather than B, tallies nicely with Noether's theorem. A naive application of Noether's theorem might suggest that momentum in both x- and y-directions is conserved when the magnetic field is translationally invariant. In fact, things are a little more subtle. 

There's one further comment to make about this situation. We could also look at what happens if we make a translation in the $y$ direction, $y \to y + s$ . Clearly the Lagrangian (7.177) isn't invariant but, the change is a total time derivative. So, by the generalisation of Noether's theorem (7.132), we do get a conserved quantity. You can check that this is given by $m\dot{y} + qBx$ which is indeed conserved by virtue of the second equation of motion in (7.174). We see that, despite appearances, translations in the $x$ - and $y$ -directions are not so different after all. 

## Lagrangians for Fields

In this book, we restrict ourselves to the classical dynamics of particles. But, ultimately, the laws of physics do not describe particles: they describe fields. One of the most important aspects of the principle of least action is that it generalises very easily to fields. 

For particles, the dynamical degrees of freedom are things like the position $\mathbf{x}(t)$ which, as the notation shows, depend on time. Correspondingly, the action is an integral over time so that it ascribes a number to each particle trajectory. Fields, however, are functions of space and time. The most familiar examples are the electric and magnetic fields $\mathbf{E}(\mathbf{x}, t)$ and $\mathbf{B}(\mathbf{x}, t)$ . Now we want the action to ascribe a number to every possible field configuration. This means that the action should be an integral over time and space. 

We won't describe the action principle for fields here. But, in passing, I will just mention that it is very straightforward. In particular, the Maxwell equations follow from the action 

$$
S = \int d t d ^ {3} x \left(\frac {\epsilon_ {0}}{2} \mathbf {E} ^ {2} - \frac {1}{2 \mu_ {0}} \mathbf {B} ^ {2}\right)\tag{7.179}
$$

where $\epsilon_{0}$ and $\mu_{0}$ are the constants of nature with pretentious names that describe the strength of the electric and magnetic forces respectively. Importantly, the action above should be varied with respect to the potentials $\phi$ and A, rather than the electric and magnetic fields themselves. The principle of least action then reproduces the Maxwell equations (2.106). All of this will be explained in great detail in Volume 2 on Electromagnetism. 

## 7.6.3 A Brief Look at Curved Geometry

We now turn to a slightly more abstract, but extremely useful Lagrangian. We will consider a single particle, but one that moves in d-dimensional space. We introduce generalised coordinates $q^{i}$ , with $i = 1, \ldots, d$ . Furthermore, we consider a particle with no potential energy, only kinetic energy. The novelty is that the particle is moving on a curved space. How do we describe this? 

There is a whole mathematical framework, known as differential geometry, to describe curved spaces. Here we will be very brief. The key idea is to introduce a function that describes the distance between two nearby points. We consider the point labelled by coordinates $q^{i}$ and a nearby point labelled by coordinates $q^{i} + \delta q^{i}$ . The distance $\delta s$ between them is 

$$
\delta s = \sqrt {g _ {i j} (q) \delta q ^ {i} \delta q ^ {j}}.\tag{7.180}
$$

Here, we have introduced a matrix of functions, $g_{ij}(q)$ , known as the metric. In principle, each element of this matrix can be a function of all $d$ coordinates $q^k$ , with $k = 1, \ldots, d$ . The metric is a symmetric matrix, so that $g_{ij} = g_{ji}$ . (One way of seeing this is that there's no point including an anti-symmetric piece of $g_{ij}$ because it won't contribute to the distance (7.180) anyway by virtue of the symmetry of $\delta q^i \delta q^j$ .) We will assume that $\det(g_{ij}) \neq 0$ , so that the inverse matrix $(g^{-1})^{ij}$ exists, with $(g^{-1})^{ij} g_{jk} = \delta_k^i$ . 

Suppose that the particle is moving on flat, Euclidean space $R^{2}$ , with Cartesian coordinates $q^{i} = (x, y)$ . Then the metric is simply $g_{ij} = \delta_{ij}$ and the distance above is nothing more than Pythagoras' theorem 

$$
\delta s = \sqrt {\delta x ^ {2} + \delta y ^ {2}}.\tag{7.181}
$$

The more general form of the metric $g_{ij}(q)$ allows us to describe curved space. Note, however, that just because $g_{ij}(q)$ depends on $q$ doesn't mean that we necessarily have a curved space. We may just be working in some other coordinates. For example, if we work with flat $\mathbb{R}^2$ in polar coordinates, so that $q^i = (r,\phi)$ , then 

$$
g _ {i j} = \left( \begin{array}{c c} 1 & 0 \\ 0 & r ^ {2} \end{array} \right) \quad \Longrightarrow \quad \delta s = \sqrt {\delta r ^ {2} + r ^ {2} \delta \phi^ {2}}.\tag{7.18}
$$

This is the way we measure distances in polar coordinates. 

With this preamble in place, we can now write down the Lagrangian for a non-relativistic particle moving on this (possibly) curved space. It takes the rather natural form 

$$
L = \frac {1}{2} g _ {i j} (q) \dot {q} ^ {i} \dot {q} ^ {j}.\tag{7.183}
$$

Deriving the equations of motion from this Lagrangian is an exercise in keeping index notation straight. We have 

$$
\frac {\partial L}{\partial q ^ {k}} = \frac {1}{2} \frac {\partial g _ {i j}}{\partial q ^ {k}} \dot {q} ^ {i} \dot {q} ^ {j} \quad \text { and } \quad \frac {\partial L}{\partial \dot {q} ^ {k}} = g _ {i k} \dot {q} ^ {i} .\tag{7.184}
$$

The Euler–Lagrange equations are then 

$$
\begin{array}{c} 0 = \frac {d}{d t} \left(\frac {\partial L}{\partial \dot {q} ^ {k}}\right) - \frac {\partial L}{\partial k} = g _ {i k} \ddot {q} ^ {i} + \frac {\partial g _ {i k}}{\partial q ^ {j}} \dot {q} ^ {i} \dot {q} ^ {j} - \frac {1}{2} \frac {\partial g _ {i j}}{\partial q ^ {k}} \dot {q} ^ {i} \dot {q} ^ {j} \\ = g _ {i k} \ddot {q} ^ {i} + \frac {1}{2} \left(\frac {\partial g _ {i k}}{\partial q ^ {j}} + \frac {\partial g _ {j k}}{\partial q ^ {i}} - \frac {\partial g _ {i j}}{\partial q ^ {k}}\right) \dot {q} ^ {i} \dot {q} ^ {j} \end{array}
$$

where, to go from the first to the second line, we've used the fact that the $\partial g / \partial q$ terms are contracted with $\dot{q}^i\dot{q}^j$ , which is symmetric in $i$ and $j$ indices, to construct the object in brackets that is similarly symmetric. We learn that the equation of motion can be written as 

$$
\ddot {q} ^ {i} + \Gamma_ {j k} ^ {i} \dot {q} ^ {j} \dot {q} ^ {k} = 0 \text { where } \Gamma_ {j k} ^ {i} = \frac {1}{2} (g ^ {- 1}) ^ {i l} \left(\frac {\partial g _ {j l}}{\partial q ^ {k}} + \frac {\partial g _ {k l}}{\partial q ^ {j}} - \frac {\partial g _ {j k}}{\partial q ^ {l}} \right.
$$

In the language of differential geometry, the object $\Gamma_{jk}^{i}$ is known as Christoffel symbol (or sometimes as the Levi-Civita connection), while the equation of motion (7.186) is called the geodesic equation. 

In general relativity, there is a natural generalisation of the geodesic equation $(7.186)$ to describe a particle moving in curved spacetime, rather than just curved space. This, it turns out, is the correct description of gravity. All of this will be covered in detail in the book on General Relativity. 

# Small Oscillations

Physics is that subset of human experience which can be reduced to coupled harmonic oscillators. 

Michael Peskin 

The harmonic oscillator is by far the most important system in all of physics. Partly, this is because we can solve it. And partly it's because a large number of other systems can, in certain circumstances, be made to look like a bunch of harmonic oscillators. Indeed, the art of physics often boils down to figuring out how to make things look like harmonic oscillators. 

We already got a hint of this back in Section 2.1.2 where we showed that, close to equilibrium, a system with a single degree of freedom looks like a harmonic oscillator. In this chapter, we expand this analysis. We will see that, close to equilibrium, the dynamics of a general system is described by n coupled simple harmonic oscillators, each ringing at a different frequency. 

Let's first recount the analysis of Section 2.1.2, but with slightly different notation. We have a single degree of freedom $x(t)$ , with an equation of motion of the form 

$$
\ddot {x} = f (x) .\tag{8.1}
$$

An equilibrium point $x = x_{0}$ satisfies $f(x_{0}) = 0$ . This means that if we start with the initial conditions 

$$
x = x _ {0} \quad \text { and } \quad \dot {x} = 0\tag{8.2}
$$

then the system will stay there forever. But what if we start slightly away from $x = x_{0}$ ? To analyse this, we write 

$$
x (t) = x _ {0} + \eta (t)\tag{8.3}
$$

where $\eta$ is assumed to be small so that we can Taylor expand $f(x)$ to find 

$$
\ddot {\eta} = f ^ {\prime} (x _ {0}) \eta + \mathcal {O} (\eta^ {2}).\tag{8.4}
$$

We neglect the terms quadratic in $\eta$ and higher. There are three possible behaviours of this system 

- $f'(x_0) < 0$ : In this case the restoring force sends us back to $\eta = 0$ and the solution is 

$$
\eta (t) = A \cos (\omega (t - t _ {0}))\tag{8.5}
$$

where A and $t_{0}$ are integration constants, while $\omega^{2} = -f'(x_{0})$ . The system undergoes stable oscillations about $x = x_{0}$ at frequency $\omega$ . 

- $f'(x_0) > 0$ : In this case, the force pushes us away from equilibrium and the solution is 

$$
\eta (t) = A e ^ {\lambda t} + B e ^ {- \lambda t}\tag{8.6}
$$

where A and B are integration constants, while $\lambda^{2} = f'(x_{0})$ . There is a very special initial condition, A = 0, such that $x \to x_{0}$ at late times. But for generic initial conditions, $\eta$ gets rapidly large and the approximation that $\eta$ is small breaks down. We say the system has a linear instability. 

- $f'(x_0) = 0$ : In this case, it was a bad idea to neglect the quadratic terms in (8.4) since they are where the physics lies. This means that we have to go back and do more work. 

We now generalise this discussion to N degrees of freedom with equations of motion of the form, 

$$
\ddot {q} ^ {i} = f ^ {i} (q ^ {1}, \dots , q ^ {N}) \text {with} i = 1, \dots , N.\tag{8.7}
$$

An equilibrium point $q_{0}^{i}$ must satisfy $f^{i}(q_{0}^{1},\ldots,q_{0}^{N})=0$ for all $i=1,\ldots,N$ . Consider small perturbations away from the equilibrium point 

$$
q ^ {i} (t) = q _ {0} ^ {i} + \eta^ {i} (t)\tag{8.8}
$$

where, again, we take the $\eta^{i}$ to be small so that we can Taylor expand the $f^{i}$ and neglect the quadratic terms and higher. We have 

$$
\ddot {\eta} ^ {i} \approx \left. \frac {\partial f ^ {i}}{\partial q ^ {j}} \right| _ {q = q _ {0}} \eta^ {j}\tag{8.9}
$$

where the sum over $j = 1, \ldots, N$ is implicit. It's useful to write this in matrix form. We define the vector $\eta$ and the $N \times N$ matrix F as 

$$
\boldsymbol {\eta} = \left( \begin{array}{c} \eta^ {1} \\ \vdots \\ \eta^ {N} \end{array} \right) \quad \text {and} \quad F = \left( \begin{array}{c c c} \partial f ^ {1} / \partial q ^ {1} & \ldots & \partial f ^ {1} / \partial q ^ {N} \\ \vdots & & \vdots \\ \partial f ^ {N} / \partial q ^ {1} & \ldots & \partial f ^ {N} / \partial q ^ {N} \end{array} \right)
$$

where each partial derivative in the matrix F is evaluated at $q^{i} = q_{0}^{i}$ . The equation (8.9) now becomes simply 

$$
\ddot {\eta} = F \eta .\tag{8.11}
$$

Our strategy is simple: we search for eigenvectors of F 

$$
F \pmb {\mu} _ {a} = \lambda_ {a} ^ {2} \pmb {\mu} _ {a}\tag{8.12}
$$

where there's no sum over $a$ in this equation. 

If $F$ were a symmetric matrix, then it would have a complete set of orthogonal eigenvectors with real eigenvalues. Unfortunately, there's no reason to think that $F$ is symmetric. Nonetheless, it is true that the 

eigenvalues are real for equations of the form $(8.11)$ that arise from physical Lagrangians. We will postpone a proof of this fact for a couple of paragraphs and continue assuming it to be the case 

Somewhat unusually, we've denoted the eigenvalues as square numbers, $\lambda_{a}^{2}$ . This is to make the expressions below simpler. However, the fact that the eigenvalue is $\lambda_{a}^{2}$ does not imply that it's a positive number: $\lambda_{a}^{2}$ could be positive or negative (or, indeed, zero). 

With the eigenvectors and eigenvalues to hand, it's straightforward to write down the most general solution to $(8.11)$ . If all the eigenvalues are distinct, then 

$$
\boldsymbol {\eta} (t) = \sum_ {a = 1} ^ {N} \boldsymbol {\mu} _ {a} \left[ A _ {a} e ^ {\lambda_ {a} t} + B _ {a} e ^ {- \lambda_ {a} t} \right].\tag{8.13}
$$

where $A_{a}$ and $B_{a}$ are 2N integration constants. Again, we have three possibilities for each eigenvalue: 

- $\lambda_{a}^{2} < 0$ : In this case $\lambda_{a} = \pm i\omega_{a}$ for some $\omega_{a} \in \mathbb{R}$ . The system will be stable in corresponding direction $\boldsymbol{\eta} = \boldsymbol{\mu}_{a}$ . 

- $\lambda_{a}^{2} > 0$ : Now $\pm \lambda_{a} \in \mathbb{R}$ and the system exhibits a linear instability in the direction $\boldsymbol{\eta} = \boldsymbol{\mu}_{a}$ . 

- $\lambda_{a}^{2} = 0$ : In this case, the linearised analysis that we've done here is insufficient to tell us the full story. 

The eigenvectors $\mu_{a}$ are called normal modes. The equilibrium point is only stable if $\lambda_{a}^{2}<0$ for every $a=1,\ldots,N$ . If this holds, then the system will oscillate around the equilibrium point as a linear superposition of all the normal modes, each typically vibrating at a different frequency. 

To keep things real, we can write the most general solution as 

$$
\boldsymbol {\eta} (t) = \sum_ {a: \lambda_ {a} ^ {2} > 0} \boldsymbol {\mu} _ {a} \left[ A _ {a} e ^ {\lambda_ {a} t} + B _ {a} e ^ {- \lambda_ {a} t} \right] + \sum_ {a: \lambda_ {a} ^ {2} <   0} \boldsymbol {\mu} _ {a} A _ {a} \cos (\omega_ {a} (t -
$$

where now $A_{a}$ , $B_{a}$ and $t_{a}$ are the 2N integration constants. 

If two or more eigenvalues coincide, then we need to work a little harder to show that the eigenvectors still form a complete basis and $(8.13)$ remains the most general solution. This turns out to be the case for systems described by physical Lagrangians. 

## Reality of Eigenvalues

Finally, let's show what we put off above: that the eigenvalues $\lambda_{a}^{2}$ are real for matrices $F$ derived from a physical Lagrangian. Consider a general Lagrangian of the form, 

$$
L = \frac {1}{2} T _ {i j} (q) \dot {q} ^ {i} \dot {q} ^ {j} - V (q).\tag{8.15}
$$

We will require that $T_{ij}(q)$ is invertible and positive definite for all q. Here the matrix $T_{ij}$ plays the same role as the metric in Section 7.6.3. Expanding about an equilibrium point $q_{0}$ , as in (8.8), to linear order in $\eta_{i}$ the equations read 

$$
T _ {i j} \ddot {\eta} _ {j} = - V _ {i j} \eta_ {j}\tag{8.16}
$$

where $T_{ij} = T_{ij}(q_0)$ and $V_{ij} = \partial^2 V / \partial q^i \partial q^j$ is also evaluated at $q^i = q_0^i$ . Then, in the matrix notation of (8.11), we have $F = -T^{-1} V$ . Both $T_{ij}$ and $V_{ij}$ are symmetric, but not necessarily simultaneously diagonalisable. This means that $F_{ij}$ is not necessarily symmetric. Nevertheless, F does have real eigenvalues. To see this, look at 

$$
F \boldsymbol {\mu} = \lambda^ {2} \boldsymbol {\mu} \quad \Longrightarrow \quad V \boldsymbol {\mu} = - \lambda^ {2} T \boldsymbol {\mu}.\tag{8.17}
$$

So far, both $\mu$ and $\lambda^2$ could be complex. We will now show that they're not. Take the inner product of this equation with the complex conjugate eigenvector $\mu^\dagger$ , 

$$
\boldsymbol {\mu} ^ {\dagger} V \boldsymbol {\mu} = \lambda^ {2} \boldsymbol {\mu} ^ {\dagger} T \boldsymbol {\mu}.\tag{8.18}
$$

For any symmetric matrix S, the quantity $\mu^{\dagger}S\mu$ is real, a fact that follows from expanding $\mu$ in the complete set of real, orthogonal eigenvectors of S, each of which has a real eigenvalue. Therefore $\mu^{\dagger}V\mu$ and $\mu^{\dagger}T\mu$ are both real. Since we have assumed that T is invertible and positive definite, we know that $\mu^{\dagger}T\mu \neq 0$ so, from (8.17), we conclude that the eigenvalue $\lambda^{2}$ is indeed real. 

## 8.1 Examples

In this section, we illustrate these ideas with a handful of examples. 

## 8.1.1 The Double Pendulum Revisited

We derived the Lagrangian for the double pendulum in Section 7.4.3. Restricting to the case where the two masses are the same, $m_{1} = m_{2} = m$ , and the two lengths are the same, $l_{1} = l_{2} = l$ , we derived the Lagrangian (7.103) for arbitrary oscillations 

$$
L = m l ^ {2} \dot {\theta} _ {1} ^ {2} + \frac {1}{2} m l ^ {2} \dot {\theta} _ {2} ^ {2} + m l ^ {2} \cos (\theta_ {1} - \theta_ {2}) \dot {\theta} _ {1} \dot {\theta} _ {2} + 2 m g l \cos \theta_ {1} + m g l \cos \theta_ {2}
$$

The stable equilibrium point is clearly $\theta_{1} = \theta_{2} = 0$ when both pendulums hang straight down. (You could check mathematically if you're sceptical.) Let's expand for small $\theta_{1}$ and $\theta_{2}$ . If we want to linearise the equations of motion for $\theta_{i}$ , then we must expand the Lagrangian to second order so that after we take derivatives, there's still a $\theta$ left standing. We have 

$$
L \approx m l ^ {2} \dot {\theta} _ {1} ^ {2} + \frac {1}{2} m l ^ {2} \dot {\theta} _ {2} ^ {2} + m l ^ {2} \dot {\theta} _ {1} \dot {\theta} _ {2} - m g l \theta_ {1} ^ {2} - \frac {1}{2} m g l \theta_ {2} ^ {2}\tag{}
$$

where we've thrown away an irrelevant constant. From this we can use the Euler–Lagrange equations to derive the two linearised equations of motion 

$$
\begin{array}{c} {2 m l ^ {2} \ddot {\theta} _ {1} + m l ^ {2} \ddot {\theta} _ {2} = - 2 m g l \theta_ {1},} \\ {m l ^ {2} \ddot {\theta} _ {2} + m l ^ {2} \ddot {\theta} _ {1} = - m g l \theta_ {2}.} \end{array}\tag{8.20}
$$

Writing $\pmb{\theta} = (\theta_1,\theta_2)^T$ , this becomes 

$$
\left( \begin{array}{c c} 2 & 1 \\ 1 & 1 \end{array} \right) \ddot {\boldsymbol {\theta}} = - \frac {g}{l} \left( \begin{array}{c c} 2 & 0 \\ 0 & 1 \end{array} \right) \boldsymbol {\theta} \quad \Longrightarrow \quad \ddot {\boldsymbol {\theta}} = - \frac {g}{l} \left( \begin{array}{c c} 2 & - 1 \\ - 2 & 2 \end{array} \right)
$$

We have two eigenvectors. They are: 

- $\boldsymbol{\mu}_{1} = (1, \sqrt{2})^{T}$ which has eigenvalue $\lambda_{1}^{2} = -(g/l)(2 - \sqrt{2})$ . This corresponds to the motion shown on left-hand side of Figure 8.1. 

- $\boldsymbol{\mu}_{2} = (1, -\sqrt{2})^{T}$ which has eigenvalue $\lambda_{2}^{2} = -(g / l)(2 + \sqrt{2})$ . This corresponds to the motion shown on the right-hand side of Figure 8.1. 

We see that both eigenvalues $\lambda_{a}$ are purely imaginary which tells us (unsurprisingly) that the state in which both pendulums hang down is stable. The frequency of the mode in which the two rods oscillate in opposite directions is higher than when they oscillate together. 

Fig. 8.1 The two normal modes of the double pendulum 

## 8.1.2 The Linear Triatomic Molecule

Consider a linear molecule, comprised of three atoms. The outer two have mass m, the middle one has mass M. An example is shown in the figure. 

This can be viewed as a rough approximation of $\mathrm{CO}_{2}$ . 

We'll only consider motion in the direction parallel to the molecule for each atom, in which case the Lagrangian for this molecule takes the form, 

$$
L = \frac {1}{2} m \dot {x} _ {1} ^ {2} + \frac {1}{2} M \dot {x} _ {2} ^ {2} + \frac {1}{2} m \dot {x} _ {3} ^ {2} - V (x _ {1} - x _ {2}) - V (x _ {2} - x _ {3}).
$$

The function $V$ is some rather complicated interatomic potential. But, the point of this chapter is that, if we're interested in oscillations around equilibrium, then this doesn't matter. Assume that $x_{i} = x_{i}^{0}$ in equilibrium. By symmetry, we have $|x_1^0 - x_2^0| = |x_2^0 - x_3^0| = r_0$ . We write deviations from equilibrium as 

$$
x _ {i} (t) = x _ {i} ^ {0} + \eta_ {i} (t).\tag{8.23}
$$

Taylor expanding the potential about the equilibrium point, we get 

$$
V (r) = V (r _ {0}) + \left. \frac {\partial V}{\partial r} \right| _ {r = r _ {0}} (r - r _ {0}) + \frac {1}{2} \left. \frac {\partial^ {2} V}{\partial r ^ {2}} \right| _ {r = r _ {0}} (r - r _ {0}) ^ {2} + \dots
$$

Here the first term $V(r_{0})$ is a constant and can be ignored, while the second term $\partial V/\partial r$ vanishes because we are in equilibrium. Substituting into the Lagrangian, we have 

$$
L \approx \frac {1}{2} m \dot {\eta} _ {1} ^ {2} + \frac {1}{2} M \dot {\eta} _ {2} ^ {2} + \frac {1}{2} m \dot {\eta} _ {3} ^ {2} - \frac {k}{2} \left[ (\eta_ {1} - \eta_ {2}) ^ {2} + (\eta_ {2} - \eta_ {3}) ^ {2} \right]
$$

where $k = \partial^{2}V/\partial r^{2}$ evaluated at $r = r_{0}$ . The equations of motion are then 

$$
\left( \begin{array}{c} m \ddot {\eta} _ {1} \\ M \ddot {\eta} _ {2} \\ m \ddot {\eta} _ {3} \end{array} \right) = - k \left( \begin{array}{c} \eta_ {1} - \eta_ {2} \\ (\eta_ {2} - \eta_ {1}) + (\eta_ {2} - \eta_ {3}) \\ \eta_ {3} - \eta_ {2} \end{array} \right)\tag{8.26}
$$

or, putting it in the form $\ddot{\eta}=F\eta$ , we have 

$$
F = \left( \begin{array}{c c c} - k / m & k / m & 0 \\ k / M & - 2 k / M & k / M \\ 0 & k / m & - k / m \end{array} \right) .\tag{8.27}
$$

Again, we must look for eigenvectors of F. There are three: 

- $\boldsymbol{\mu} = (1, 1, 1)^T$ which has eigenvalue $\lambda_1^2 = 0$ . This is just an overall translation of the molecule. It's not an oscillation. It looks like this: 

Modes with $\lambda = 0$ are called, quite reasonably, zero modes. Often such zero modes arise because there is some symmetry in the problem that allows us to move the system in some way without affecting the physics. That's the case here, where the zero mode arises because of translational symmetry. 

- $\boldsymbol{\mu}_{2} = (1,0,-1)^{T}$ which has eigenvalue $\lambda_{2}^{2} = -k/m$ . In this motion, the outer two atoms oscillate out of phase, while the middle atom remains stationary. The oscillation has frequency $\omega_{2} = \sqrt{k/m}$ . It looks like this: 

- $\boldsymbol{\mu}_{3} = (1, -2m / M, 1)^{T}$ which has eigenvalue $\lambda_{3}^{2} = -(k / m)(1 + 2m / M)$ . This oscillation is a little less obvious. The two outer atoms move in the same direction, while the middle atom moves in the opposite direction. The frequency of this vibration $\omega_{3} = \sqrt{-\lambda_{3}^{2}}$ is greater than that of the second normal mode. It looks like this: 

For small deviations from equilibrium, the most general motion is a superposition of all of these modes 

$$
\boldsymbol {\eta} (t) = \boldsymbol {\mu} _ {1} (A + B t) + \boldsymbol {\mu} _ {2} C \cos (\omega_ {2} (t - t _ {2})) + \boldsymbol {\mu} _ {3} D \cos (\omega_ {3} (t - t _ {3})
$$

with A, B, C, and D all arbitrary integration constants, albeit ones that should be taken to be suitably small so that we can trust our linearised analysis. 

## 8.1.3 The Stability of Lagrange Points

In Section 7.6.1, we studied the three-body problem, at least in a restricted sense. Recall that we considered a light particle, with mass $m_{3}$ , moving in the gravitational potential of two much heavier particles, with masses $m_{1}, m_{2} \gg m_{3}$ . 

For simplicity, we took the two heavy particles to orbit in a circle of radius $r$ . The frequency of their orbit is, by Kepler's third law 

$$
\omega^ {2} = \frac {G (m _ {1} + m _ {2})}{r ^ {3}}.\tag{8.29}
$$

In the reference frame that rotates at the same frequency $\omega$ , we derived the equations of motion for the third particle (7.157) 

$$
\begin{array}{l} {m _ {3} \ddot {x} = 2 m _ {3} \omega \dot {y} + m _ {3} \omega^ {2} x - \frac {\partial V}{\partial x}} \\ {m _ {3} \ddot {y} = - 2 m _ {3} \omega \dot {x} + m _ {3} \omega^ {2} y - \frac {\partial V}{\partial y}.} \end{array}\tag{8.30}
$$

Here the potential experienced by the third particle is given by 

$$
V = - \frac {G m _ {1} m _ {3}}{r _ {1 3}} - \frac {G m _ {2} m _ {3}}{r _ {2 3}}\tag{8.31}
$$

where the separations are 

$$
\begin{array}{r l} & r _ {1 3} ^ {2} = (x + r \mu / m _ {1}) ^ {2} + y ^ {2} + z ^ {2} \\ \text { and } & r _ {2 3} ^ {2} = (x - r \mu / m _ {2}) ^ {2} + y ^ {2} + z ^ {2} \end{array}\tag{8.32}
$$

which contains the reduced mass $\mu = m_{1}m_{2}/(m_{1} + m_{2})$ . 

In Section 7.6.1, we found the stationary solutions to (8.30), satisfying $\dot{x} = \ddot{x} = 0$ . There are five such solutions, known as Lagrange points, shown in Figure 8.2. Three of these points, $L_{1}, L_{2}$ , and $L_{3}$ , lie on the y = 0 axis, co-linear with the original orbiting particles. The other two, $L_{4}$ and $L_{5}$ , lie in the orbital plane, but with $y \neq 0$ . 

Fig. 8.2 The five Lagrange points in the Earth–Sun system. 

Our goal in this section is to understand the stability of these Lagrange points. Suppose that you sit just away from them. Do you get pushed further away, or slowly drift back? 

To answer this, first recall that, as part of our derivation in Section 7.6.1, we assumed that the third particle was moving in the same orbital plane as the first two which, in our notation, is the $z = 0$ plane. It's simple to check that the particle is stable to perturbations out of this plane. The additional equation of motion is just 

$$
\ddot {z} = - \frac {\partial^ {2} V}{\partial z ^ {2}}.\tag{8.33}
$$

A quick calculation shows that $\partial^{2}V/\partial z^{2}\big|_{z=0}>0$ , which means that each of the Lagrange points is at least stable to perturbations out of the z=0 plane. But what about within the plane? 

This calculation is a little more involved. We expand 

$$
x = x _ {0} + \delta x \quad \text { and } \quad y = y _ {0} + \delta y .\tag{8.34}
$$

Here $(x_{0}, y_{0})$ is one of the Lagrange points: we know that these obey $m_{3}\omega^{2}x_{0} = \nabla V|_{x_{0}}$ . Substituting (8.34) into the equation of motion (8.30), and expanding to leading order in $\delta x$ , we have 

$$
\begin{array}{l} \delta \ddot {x} - 2 \omega \delta \dot {y} = \omega^ {2} \delta x - \frac {\partial^ {2} V}{\partial x ^ {2}} \delta x - \frac {\partial^ {2} V}{\partial x \partial y} \delta y \\ \delta \ddot {y} + 2 \omega \delta \dot {x} = \omega^ {2} \delta y - \frac {\partial^ {2} V}{\partial y ^ {2}} \delta y - \frac {\partial^ {2} V}{\partial x \partial y} \delta x. \end{array}\tag{8.35}
$$

At this stage we make an ansatz for the time dependence 

$$
\delta x = \delta x _ {0} e ^ {\lambda t} \quad \mathrm{and} \quad \delta y = \delta y _ {0} e ^ {\lambda t}.\tag{8.36}
$$

Here $\delta x_{0}$ is the amplitude of the perturbation which is left arbitrary (but necessarily small). We know from the general analysis of this section that the system will be unstable if $\lambda$ is real, but will oscillate about the equilibrium point if $\lambda$ is imaginary. Substituting the ansatz (8.36) into the perturbed equation of motion (8.35) gives us the matrix equation 

$$
\mathcal {M} \binom{\delta x}{\delta y} = 0 \quad \text {with} \mathcal {M} = \left( \begin{array}{c c} \lambda^ {2} - \omega^ {2} + A & - 2 \omega \lambda + B \\ 2 \omega \lambda + B & \lambda^ {2} - \omega^ {2} + C \end{array} \right)
$$

Here we've defined the partial derivatives 

$$
A = \frac {\partial^ {2} V}{\partial x ^ {2}}, \quad B = \frac {\partial^ {2} V}{\partial x \partial y}, \quad C = \frac {\partial^ {2} V}{\partial y ^ {2}}\tag{8.38}
$$

each of which should be evaluated at the particular Lagrange point. The expressions for these partial derivatives are easily found, but are a little messy 

$$
\begin{array}{r l} & A = \frac {G m _ {1} (y ^ {2} - 2 (x + r \mu / m _ {1}) ^ {2})}{r _ {1 3} ^ {5}} + \frac {G m _ {2} (y ^ {2} - 2 (x - r \mu / m _ {2}) ^ {2})}{r _ {2 3} ^ {5}} \\ & B = - \frac {3 G m _ {1} y (x + r \mu / m _ {1})}{r _ {1 3} ^ {5}} - \frac {3 G m _ {2} y (x - r \mu / m _ {2})}{r _ {2 3} ^ {5}} \\ & C = \frac {G m _ {1} ((x + r \mu / m _ {1}) ^ {2} - 2 y ^ {2})}{r _ {1 3} ^ {5}} + \frac {G m _ {2} ((x - r \mu / m _ {2}) ^ {2} - 2 y ^ {2})}{r _ {2 3} ^ {5}} \end{array}
$$

where we've taken the liberty of setting $z = 0$ since each Lagrange point sits in the plane. We'll see below how to extract what we need from these expressions. 

The matrix equation $(8.37)$ is like an eigenvalue equation in the sense that we should solve it at each Lagrange point to determine $\lambda$ . We can do this by taking the determinant, 

$$
\det \mathcal {M} = (\lambda^ {2} - \omega^ {2} + A) (\lambda^ {2} - \omega^ {2} + C) + 4 \omega^ {2} \lambda^ {2} - B ^ {2} = 0.
$$

This is a quadratic equation in $\lambda^{2}$ , so that solutions come in $\pm\lambda$ pairs. An equilibrium point will be stable only if $\lambda$ is purely imaginary, which 

means that all the roots $\lambda^{2}$ must be real and negative for stability. 

The story is slightly different for the three co-linear Lagrange points $L_{1}$ , $L_{2}$ , and $L_{3}$ , and the other two. We'll start with the co-linear points. These sit at $y = 0$ which means that the partial derivatives are $B = 0$ and $A = -2C$ with 

$$
C = \frac {G m _ {1}}{(| x + r \mu / m _ {1} | ^ {3}} + \frac {G m _ {2}}{| x - r \mu / m _ {2} | ^ {3}} > 0.\tag{8.41}
$$

Solving the quadratic $(8.40)$ in this case gives 

$$
\lambda^ {2} = \frac {1}{2} \left(C - 2 \omega^ {2} \pm \sqrt {C (9 C - 8 \omega^ {2})}\right).\tag{8.42}
$$

The roots are clearly real only if $9C \geq 8\omega^{2}$ . But, for stability, we also require that both roots are negative and this gives the extra condition 

$$
\frac {8}{9} \omega^ {2} \leq C <   \omega^ {2}.\tag{8.43}
$$

So does this condition hold? The answer is no. To see this, we need to use the fact, derived in $(7.160)$ , that at these co-linear Lagrange points obey 

$$
\omega^ {2} x = G m _ {1} \frac {x + r \mu / m _ {1}}{| x + r \mu / m _ {1} | ^ {3}} + G m _ {2} \frac {x - r \mu / m _ {2}}{| x - r \mu / m _ {2} | ^ {3}}.\tag{8.44}
$$

Dividing through by x, we can use this to write 

$$
C = \omega^ {2} + \frac {G r \mu}{x} \left(\frac {1}{| x - r \mu / m _ {2} | ^ {3}} - \frac {1}{| x + r \mu / m _ {1} | ^ {3}}\right).\tag{8}
$$

But it's not hard to show that the extra term is always positive, so $C > \omega^2$ . For example, at the Lagrange point $L_2$ , we have $x > r\mu / m_2 > 0$ and the term in brackets above is positive. Similar arguments hold for $L_1$ and $L_3$ . This means that the co-linear Lagrange points are all unstable. 

We learned in Section 7.6.1 that $L_{1}$ and $L_{2}$ are particularly useful points for placing satellites. Now we see that they are unstable. Without doing any further work, we can see that the time scale of the instability is set by $\omega = (\text{year})^{-1}$ . In fact, a more accurate analysis shows that it's unstable on a time scale of less than a month. This means that the satellites must be equipped with the ability to correct their position. 

This leaves us with the Lagrange points $L_{4}$ and $L_{5}$ , in which the three particles make an equilateral triangle, so that $r_{13} = r_{23} = r$ . Some simple geometry shows that $(x + r\mu/m_{1}) = -(x - r\mu/m_{2}) = r/2$ and $y = \pm\sqrt{3}r/2$ , where the $\pm$ sign are for $L_{4}$ and $L_{5}$ respectively. From this, we can explicitly calculate the values of the partial derivatives. We have 

$$
A = \frac {1}{4} \frac {G (m _ {1} + m _ {2})}{r ^ {3}} = \frac {1}{4} \omega^ {2} \quad \mathrm{and} \quad C = - \frac {5}{4} \frac {G (m _ {1} + m _ {2})}{r ^ {3}} = - \frac {5}{4}
$$

while the mixed partial derivative depends on the ratio of masses, 

$$
B = - \frac {3 \sqrt {3}}{4} \frac {G (m _ {1} - m _ {2})}{r ^ {3}} = - \frac {3 \sqrt {3}}{4} \omega^ {2} \left(\frac {m _ {1} - m _ {2}}{m _ {1} + m _ {2}}\right).
$$

With these results, it's straightforward to find the roots of the quadratic (8.40). We have 

$$
\frac {\lambda^ {2}}{\omega^ {2}} = - \frac {1}{2} \pm \frac {1}{2} \sqrt {1 - \frac {2 7}{4} \left(1 - \left(\frac {m _ {1} - m _ {2}}{m _ {1} + m _ {2}}\right) ^ {2}\right)}.\tag{8.48}
$$

Recall that both roots should be real and negative for stability. This holds provided that one of the original masses is sufficiently smaller than that other, so that 

$$
\left(\frac {m _ {1} - m _ {2}}{m _ {1} + m _ {2}}\right) ^ {2} > \frac {2 3}{2 7}.\tag{8.49}
$$

If we take $m_2 < m_1$ , then the condition for stability becomes 

$$
\frac {m _ {2}}{m _ {1} + m _ {2}} \lesssim 0. 0 3 8 5.\tag{8.50}
$$

The Earth–Sun system comfortably obeys this, with $m_{Earth}/m_{Sun} \approx 10^{-5}$ and a collection of dust has gathered at $L_{4}$ and $L_{5}$ . It is also obeyed by 

Jupiter, with $m_{Jupiter}/m_{Sun} \approx 0.01$ . In this case, a number of large asteroids have gathered at $L_{4}$ and $L_{5}$ , known as trojans. 

## 8.1.4 A Lattice of Atoms

As our final example, consider a chain of N particles, each connected to their neighbour by a spring. This is a fairly decent model for a solid, although admittedly a 1d solid rather than a 3d solid. The particles are the atoms in the solid, while the springs model the inter-atomic forces that stop the solid from falling apart. 

To fully specify the problem, we need to fix some boundary conditions on the first and last atom. One option is to take them to be fixed in place. Another, which is less realistic but slightly simpler mathematically, is to take the atoms to lie on a circle and implement periodic boundary conditions. We'll choose the latter. Although less realistic, it doesn't change the key physics: if you've got, say, $N = 10^{23}$ atoms, then those in the middle couldn't care less about what those on the ends are doing. 

For simplicity, we'll take all the atoms to have the same mass $m$ (i.e. identical atoms) and all the springs to have the same spring constant $k$ . In addition, we'll take the equilibrium distance between particles to be $a$ . The Lagrangian of this system is 

$$
L = \frac {1}{2} m \sum_ {n} \dot {x} _ {n} ^ {2} - \frac {1}{2} k \sum_ {i} (x _ {n + 1} - x _ {n} - a) ^ {2}.\tag{8.51}
$$

It's useful to work with a slightly different coordinate 

$$
u _ {n} = x _ {n} - a n.\tag{8.52}
$$

That means that $u_{n}$ is the distance of the $n^{th}$ atom from equilibrium. (Note that $u_{n}$ is a position variable, not a velocity variable here!) These variables are useful because they eliminate the linear terms in $(8.51)$ that arise when you expand out the potential term. We now have 

$$
L = \frac {1}{2} m \sum_ {n} \dot {u} _ {n} ^ {2} - \frac {1}{2} k \sum_ {n} (u _ {n + 1} - u _ {n}) ^ {2}.\tag{8.53}
$$

The Euler-Lagrange equations are 

$$
m \ddot {u} _ {n} = \frac {\partial L}{\partial u _ {n}} = - k (2 u _ {n} - u _ {n + 1} - u _ {n - 1}).\tag{8.54}
$$

This is an equation of the form $(8.11)$ , with F a very large but very sparse matrix. In this case, we diagonalise the equation by a Fourier transform. This means that, as in Section 2.5.1, we pretend that $u_{n}(t)$ is a complex variable, safe in the knowledge that it obeys a linear equation $(8.54)$ so if we find a solution then the real part will also be a solution. We then define the linear sum 

$$
\xi_ {q} (t) = \frac {1}{\sqrt {N}} \sum_ {n = 1} ^ {N} e ^ {i q a n} u _ {n} (t)\tag{8.55}
$$

with $\xi_{q}$ our new variable, now carrying a different label q. First, we should figure out what range of numbers q runs over. To see this, first note that q only appears in the complex exponent in the form $e^{-2\pi i q a n}$ and $n \in Z$ . This means that if we shift $q \to q + 2\pi/a$ , then nothing changes in (8.55). So we can always restrict q to lie in the region 

$$
q \in \left[ - \frac {\pi}{a}, + \frac {\pi}{a}\right).\tag{8.56}
$$

In the context of solid-state physics (the study of materials), this region is known as the Brillouin zone. Next, we use the fact that we have imposed periodic boundary conditions. This requires that $u_{n}(t) = u_{n+N}(t)$ . Making this shift in $(8.55)$ leaves $\xi_{q}$ unaffected provided that 

$$
q = \frac {2 \pi}{N a} l \quad \mathrm{with} \quad l = - \frac {N}{2}, \ldots , \frac {N}{2}.\tag{8.57}
$$

So we see that q is, like n, a discrete variable. The label q is called the wavenumber. We can always invert $(8.55)$ by writing 

$$
u _ {n} (t) = \frac {1}{\sqrt {N}} \sum_ {q} e ^ {- i q a n} \xi_ {q} (t)\tag{8.58}
$$

where the sum goes over the discrete range of q specified in $(8.57)$ . This is telling us that, for some particular $\xi_{q} \in R \neq 0$ , the displacements $u_{n}$ get periodically bigger and smaller as $\cos(qan)$ as we move through the 

lattice. In other words, we are setting up a wave in the lattice with wavelength $\sim 1/q$ . 

To see that the Fourier sum (8.55) is indeed what's needed to solve the equation of motion (8.54), we look at 

$$
\begin{array}{r l} & {\ddot {\xi_ {q}} = \frac {1}{\sqrt {N}} \sum_ {n} e ^ {i q a n} \ddot {u} _ {n}} \\ & {\quad = - \frac {1}{\sqrt {N}} \frac {k}{m} \sum_ {n} e ^ {i q a n} (2 u _ {n} - u _ {n + 1} - u _ {n - 1})} \\ & {\quad = - \frac {1}{N} \frac {k}{m} \sum_ {n} e ^ {i q a n} \sum_ {q ^ {\prime}} e ^ {- i q ^ {\prime} a n} \left(2 - e ^ {- i q ^ {\prime} a} - e ^ {i q ^ {\prime} a}\right) \xi_ {q ^ {\prime}}.} \end{array}
$$

Now we do the sum over the integer n and use the fact that $\sum_{n} e^{i(q-q')an} = N\delta_{q,q'}$ . We then have 

$$
\ddot {\xi} _ {q} = - \frac {k}{m} (2 - 2 \cos (q a)) \xi_ {q} = - \frac {4 k}{m} \sin^ {2} \left(\frac {q a}{2}\right) \xi_ {q}.\tag{8.60}
$$

That's exactly what we wanted. A given mode $\xi_q$ doesn't couple to other modes. It oscillates with a frequency that depends on $q$ , given by 

$$
\omega (q) = 2 \sqrt {\frac {k}{m}} \left| \sin \left(\frac {q a}{2}\right) \right|.\tag{8.61}
$$

This is plotted in Figure 8.3. The very short wavelength modes have $q \approx \pi / a$ and a frequency $\omega^{2} \approx 2k / m$ . This is twice the frequency of a single spring. 

Fig. 8.3 The frequency $\omega(q)$ as s function of the wavenumber $q$ . In reality, only discrete values of $q$ are allowed, but with $N \approx 10^{23}$ discrete values between $q = -\pi/2$ and $q = +\pi/2$ , in practice that's the same as a continuous function. 

There is one mode with $q = 0$ and $\omega = 0$ . This is just an overall translation of the whole lattice. The next lowest frequency arises for $q = 2\pi / Na$ and has $\omega \sim 1 / N$ . For a macroscopically large number of atoms, say $N \approx 10^{23}$ , that's a very small frequency! What's happening here is that the large number of atoms are oscillating coherently and, in doing so, reduce the natural frequency of the system $\omega \sim \sqrt{k / m}$ , by the number of atoms. In this way, while each individual atom might naturally oscillate at some high frequency, the collection of atoms can oscillate at a frequency that is, for all intents and purposes, arbitrarily small. For suitably small $q$ , the frequency is approximately linear in the wavenumber 

$$
\omega \approx \sqrt {\frac {k}{m}} q a.\tag{8.62}
$$

These kind of long wavelength modes have a name: they are called sound waves in a solid. This will be described more in the forthcoming book on Condensed Matter. 

## 8.2 A Brief Look at Perturbation Theory

So far in this chapter, we have looked at small perturbations about an equilibrium point. In this section, we develop perturbation theory in a slightly different direction. Here's the basic idea. Suppose that you have a problem that you can't solve. (This, it turns out, is the normal way of things.) If you're lucky, it might be close to a problem that you can solve. The hope, then, is that you can build a solution to the problem you care about by starting with a problem that you can make progress on. This is known as perturbation theory. 

As we progress on our journey through physics, we will use various different types of perturbation methods and, as our physical theories get more advanced, we rely on them more and more. Here we just sketch a basic example, and offer a salutary warning about the kind of things that can happen. 

## 8.2.1 The Anharmonic Oscillator

Our example of choice is the anharmonic, or non-linear oscillator. This has the equation of motion 

$$
\ddot {x} = - \omega^ {2} x - \lambda x ^ {3}\tag{8.63}
$$

where, for simplicity, we've set the mass of the particle to unity. When $\lambda = 0$ , this is just the usual harmonic oscillator. It's clear that the additional term shouldn't qualitatively change the dynamics of the 

system: for $\lambda > 0$ the extra force pushes us back towards the origin, just like the linear term. Moreover, the energy 

$$
E = \frac {1}{2} \dot {x} ^ {2} + V \quad \mathrm{with} \quad V = \frac {1}{2} \omega^ {2} x ^ {2} + \frac {1}{4} \lambda x ^ {4}\tag{8.64}
$$

is conserved and so we see that the particle will oscillate back and forth in the potential $V(x)$ , just like a harmonic oscillator. However, we'd like to do better than this qualitative analysis and actually find a solution to (8.63). Sadly the general solution cannot be written down in closed form. 

Our goal here is to make progress when $\lambda$ is, in some sense, small. This looks promising because we certainly know the solution when $\lambda = 0$ : it is 

$$
x _ {0} (t) = A \cos (\omega (t - t _ {0})) .\tag{8.65}
$$

The hope is that we can build off this solution to find an approximation to the true solution when $\lambda$ is small. 

Our first task is to clarify what it means for $\lambda$ to be small. This is because $\lambda$ has dimensions $[\lambda] = L^{-2}T^{-2}$ and so, as explained in Chapter 3, can only be small relative to something else. In fact there's a unique combination of parameters that have the same dimension and so we're looking for solutions in the situation that 

$$
\lambda \ll \frac {\omega^ {2}}{A ^ {2}}.\tag{8.66}
$$

Note that $\omega$ is a parameter of our equation of motion (8.63), but $A$ is an integration constant for our starting solution (8.65). This reflects the fact that we're not going to find approximations to the general solution to (8.63) using this method: only to some restricted class of solutions. In fact, it's perhaps better to say that this method works for any $\lambda$ , but is restricted to solutions with $A^2 \ll \omega^2 / \lambda$ . Either way, we introduce the dimensionless small quantity 

$$
\epsilon = \frac {\lambda A ^ {2}}{\omega^ {2}} \ll 1.\tag{8.67}
$$

Our task is to set up a perturbative expansion in $\epsilon$ . 

The obvious way to proceed is to postulate a solution that has the expansion 

$$
x (t) = x _ {0} (t) + \epsilon x _ {1} (t) + \epsilon^ {2} x _ {2} (t) + \ldots .\tag{8.68}
$$

We substitute this into the equation of motion (8.63) and equate terms order by order in $\epsilon$ . The first equation is simply $\ddot{x}_{0} = -\omega^{2}x_{0}$ and is solved by (8.65). To find the subsequent equations, it's best to think of $\lambda \sim \epsilon$ and let the dimensions come out in the wash. We have 

$$
\mathcal {O} (\epsilon): \quad \ddot {x} _ {1} + \omega^ {2} x _ {1} = - \frac {\omega^ {2}}{A ^ {2}} x _ {0} ^ {3},\tag{8.69}
$$

$$
\mathcal {O} (\epsilon^ {2}): \quad \ddot {x} _ {2} + \omega^ {2} x _ {2} = - \frac {3 \omega^ {2}}{A ^ {2}} x _ {0} ^ {2} x _ {1}.\tag{8.70}
$$

Each of these is rather like the driven harmonic oscillator that we saw in Section 2.5.2, albeit without the friction term. Moreover, we can solve these equations successively. The solution $x_0$ acts as a driving force for $x_1$ . Both $x_0$ and $x_1$ are then needed to determine the driving force $\sim x_0^2 x_1$ for $x_2$ . And so on. 

Let's start by solving the first equation (8.69). For simplicity, I'll set the integration constant $t_0 = 0$ in (8.65). (As we'll see, this will turn out to be not as innocent as it looks!) Plugging in the solution (8.65), we have 

$$
\ddot {x} _ {1} + \omega^ {2} x _ {1} = - \omega^ {2} A \cos^ {3} (\omega t) = - \frac {\omega^ {2} A}{4} \Big (\cos (3 \omega t) + 3 \cos (\omega t) \Big).
$$

This is a linear equation in $x_{1}$ , with two sources on the right-hand side: one proportional to $\cos(3\omega t)$ and one proportional to $\cos(\omega t)$ . We can solve each of these in turn. First, we have 

$$
\ddot {x} _ {1} + \omega^ {2} x _ {1} = - \frac {\omega^ {2} A}{4} \cos (3 \omega t) \quad \Longrightarrow \quad x _ {1} = A _ {1} \cos (3 \omega t)
$$

where a quick calculation shows that the overall amplitude is $A_{1} = A/32$ . This is typical of the kind of behaviour that arises in perturbation theory: 

we started with a system oscillating at one frequency $\omega$ , and the perturbation induces an oscillation at a different frequency, here $3\omega$ . 

Next we turn to the second source term in (8.71). And here we hit a snag. This is because the frequency of the driving force is $\omega$ , which coincides with the natural frequency of $x_{1}$ . The solution isn't $x_{1} \sim \cos(\omega t)$ because that's the homogeneous solution. Instead the solution is 

$$
\ddot {x} _ {1} + \omega^ {2} x _ {1} = - \frac {3 \omega^ {2} A}{4} \cos (\omega t) \quad \Longrightarrow \quad x _ {1} = A _ {1} ^ {\prime} \omega t \sin (\omega t)
$$

where, again, a short calculation shows that $A_{1}^{\prime} = -3A/8$ . Rather worryingly, this solution isn't oscillatory, but grows with t, a result of the fact that the driving force is at resonance. This means that, beyond some time $t \sim 1/\omega\epsilon$ , the term $x_{1}(t)$ will not be a small correction to our original solution $x_{0}(t)$ . Instead it will dominate. And that's bad because our whole strategy was based on finding increasingly small corrections. Terms like (8.73) that grow with time are called secular. 

What to do about this? The answer depends on the problem at hand. For some problems, the secular growth may well be telling us that the original solution was unstable. However, that can't be the case for the anharmonic oscillator because, as we've already seen on energy grounds, the solution can't run away. Instead, the culprit is our original expansion (8.68). 

The problem is that, to leading order, the non-linear term has two effects: it induces a second frequency, $3\omega$ , in the oscillation. And it also changes the original frequency $\omega$ . This means that a better perturbative expansion, at leading order, is to take 

$$
x (t) = A \cos ((\omega + \epsilon \omega_ {1}) t) + \epsilon x _ {1} (t) + \mathcal {O} (\epsilon^ {2})\tag{8.74}
$$

which allows for a change in the frequency of the original solution. If we expand out this first term to leading order in $\epsilon$ , we have 

$$
\cos ((\omega + \epsilon \omega_ {1}) t) \approx \cos (\omega t) - \epsilon \omega_ {1} t \sin (\omega t) + \dots .\tag{8.75}
$$

There we see the same $\omega t \sin(\omega t)$ behaviour that appeared in (8.73). 

Except now we understand the meaning of this: it is just a small change to the original frequency. Comparing to our solution $(8.73)$ , this shift in the frequency must be 

$$
\Delta \omega = \epsilon \omega_ {1} = \frac {3}{8} \epsilon \omega .\tag{8.76}
$$

The frequency should be expected to pick up further shifts at $\mathcal{O}(\epsilon^{2})$ and higher. 

There is another way to think about this. Our original solution (8.65) included an integration constant $t_{0}$ that we set to zero in our subsequent analysis. The shift of frequency (8.76) can be viewed as endowing this integration constant with some time dependence, so that $t_{0} \rightarrow -\frac{3}{8}\epsilon t$ . This kind of behaviour is common in many problems. As a general rule of 

thumb, when secular terms arise one should see if they can be accounted for by endowing integration constants with some small time dependence. 

# Rigid Bodies

To those who study the progress of exact science, the common spinning-top is a symbol of the labours and the perplexities of men. 

James Clerk Maxwell, no less 

We started this book by explaining that classical mechanics describes the motion of “particles”, defined to be objects of insignificant size. But there are things in the world whose size is not insignificant and it would be nice to be able to say something about them. We do this by modelling these objects as made of many constituent particles. 

For much of this section, we'll be interested in so-called rigid bodies. This is a collection of $N$ particles, constrained so that the relative distance between any two points, $i$ and $j$ , is fixed: 

$$
\left| \mathbf {x} _ {a} - \mathbf {x} _ {b} \right| = \text { fixed }.
$$

for $a, b = 1, \ldots, N$ . You could have in your mind a bunch of point masses, fixed together by rigid rods as shown in the figure. Alternatively, in many situations we will be interested in continuous solids, rather than discrete point masses. 

The question that we want to ask is: how does such a rigid body move? We already know from Chapter 4 that the centre of mass motion will act like a particle. But, in addition, the object can tumble and turn. The purpose of this chapter is to describe this tumbling. One of the lessons we will learn is that things that spin can be somewhat counterintuitive. 

## 9.1 Kinematics

Our first task is to understand the ways in which a rigid body can move, and then to develop the mathematical machinery to describe it. It turns out that a rigid body can undergo two types of motion: its centre of mass can move; and it can rotate. This means that a rigid body has six degrees of freedom: three translations, and three rotations. 

To kick things off, we will ignore translational motion. We achieve this by considering a rigid body that is fixed at some point P so that the only allowed motion is rotation about P. We want to describe this rotation. 

To do this, we introduce two different sets of axes. The first is a set of axes that is fixed in space. We denote these as $\{\tilde{\mathbf{e}}_{i}: i = 1, 2, 3\}$ . The second is a set of axes that is embedding in the rigid body. We denote these as $\{e_{i}: i = 1, 2, 3\}$ . Examples of these axes are shown in Figure 9.1. The idea is that the rotation of the rigid body can be described by saying how the body frame axes $\mathbf{e}_{i}(t)$ move with respect to the space frame axes $\tilde{\mathbf{e}}_{i}$ . 

Fig. 9.1 The space frame $\{\tilde{e}_{i}\}$ stays fixed, while the body frame $\{e_{i}\}$ changes with time, rotating with the rigid body. 

We take both sets of axes to be orthonormal, meaning that 

$$
\tilde {\mathbf {e}} _ {i} \cdot \tilde {\mathbf {e}} _ {j} = \delta_ {i j} \quad \text { and } \quad \mathbf {e} _ {i} (t) \cdot \mathbf {e} _ {j} (t) = \delta_ {i j} .\tag{9.1}
$$

These two orthonormal bases are related by a time-dependent rotation matrix $R(t)$ , so that 

$$
\mathbf {e} _ {i} (t) = R _ {i j} (t) \tilde {\mathbf {e}} _ {j}.\tag{9.2}
$$

The fact that $R(t)$ is a rotation matrix follows from (9.1): substituting (9.2), we have $\mathbf{e}_{i} \cdot \mathbf{e}_{j} = (R_{ik} \tilde{\mathbf{e}}_{k}) \cdot (R_{jl} \tilde{\mathbf{e}}_{l}) = R_{ik} R_{jk} = \delta_{ij}$ . Losing the indices, this tells us that R is an orthogonal matrix, satisfying $RR^{T} = 1$ . Any such matrix describes a rotation, possibly together with a reflection. 

We will assume that the bases $\{e_{i}\}$ and $\{\tilde{e}_{i}\}$ share the same handedness. (For example, it may be useful to take $\mathbf{e}_{i}(t=0)=\tilde{\mathbf{e}}_{i}$ .) This means that det R=1 and R is a rotation matrix with no reflection. For concreteness, we take both bases to be right-handed so that, for example $e_{1}\times e_{2}=e_{3}$ . 

The set of all $3 \times 3$ orthogonal matrices with unit determinant form a group that is denoted $SO(3)$ . (Here the “O” stands for “orthogonal” and the “S” for special which, in this context, means unit determinant.) As the rigid body rotates it is described by a time-dependent matrix $R(t) \in SO(3)$ . Conversely, every one-parameter family $R(t) \in SO(3)$ describes a possible motion of the rigid body. Translating this into the language of classical dynamics, it means that the configuration space C of a rotating rigid body, fixed at some point, is 

$$
\mathcal {C} = S O (3) .\tag{9.3}
$$

A $3 \times 3$ matrix has nine components but the condition of orthogonality $R^T R = 1$ imposes six relations, so the configuration space $\mathcal{C}$ is three-dimensional and we need three generalised coordinates to parameterise $\mathcal{C}$ . We will actually be able to make a great deal of progress without finding explicit coordinates on $\mathcal{C}$ but, at some point, we'll need to do this. The coordinates are called Euler angles and are introduced in Section 9.5. 

## 9.1.1 Angular Velocity

Any point x in the body can be expanded in either the space frame or the body frame bases 

$$
\begin{array}{r l} \mathbf {x} (t) = \tilde {x} _ {i} (t)   \tilde {\mathbf {e}} _ {i} & \text { in   the   space   frame, } \\ = x _ {i}   \mathbf {e} _ {i} (t) & \text { in   the   body   frame. } \end{array}\tag{9.4}
$$

Note the different places where time dependence occurs. From the perspective of the space frame, any point in the body is moving: hence $\tilde{x}_{i}(t)$ . In contrast, from the perspective of the body frame all the points are at some fixed distance $x_{i}$ , independent of time, because we're dealing with a rigid body. Instead, it is the axes $\mathbf{e}_{i}(t)$ that move. 

Substituting the relation $(9.2)$ into $(9.4)$ , we get the relationship between coordinates 

$$
\tilde {x} _ {j} (t) = x _ {i} R _ {i j} (t).\tag{9.5}
$$

Next, we can take time derivatives to see how things change with time. In fact, there are two different questions that we can ask: How does the body basis $\mathbf{e}_i(t)$ change with time, and how do the coordinates $\tilde{x}_i(t)$ change with time? We'll answer both here, although it turns out that the former is the more useful so we start with that. From (9.2), we have 

$$
\frac {d \mathbf {e} _ {i}}{d t} = \frac {d R _ {i j}}{d t} \tilde {\mathbf {e}} _ {j} = \frac {R _ {i j}}{d t} R _ {j k} ^ {- 1} \mathbf {e} _ {k}.\tag{9.6}
$$

The matrix $\dot{R}R^{-1}$ is important enough to deserve its own name. We write 

$$
\Omega = \frac {d R}{d t} R ^ {- 1} = \frac {d R}{d t} R ^ {T}.\tag{9.7}
$$

It's simple to show that $\Omega$ is an anti-symmetric matrix. This follows from the fact that $RR^{T} = 1$ which, upon differentiation, gives 

$$
\Omega = \frac {d R}{d t} R ^ {T} = - R \frac {d R ^ {T}}{d t} = - \Omega^ {T}.\tag{9.8}
$$

We write the entries of this anti-symmetric matrix as 

$$
\Omega = \left( \begin{array}{c c c} 0 & \omega_ {3} & - \omega_ {2} \\ - \omega_ {3} & 0 & \omega_ {1} \\ \omega_ {2} & - \omega_ {1} & 0 \end{array} \right) \text {or} \Omega_ {i j} = \epsilon_ {i j k} \omega_ {k} \Longrightarrow \omega_ {i} = \frac {1}{2} \epsilon_ {i j k} \Omega_ {i j k}
$$

We think of the $\omega_{i}$ as the components of a vector in the body frame, and define 

$$
\boldsymbol {\omega} = \omega_ {i} \mathbf {e} _ {i}.\tag{9.10}
$$

The vector $\omega$ is called the instantaneous angular velocity. As we see above, its components $\omega_{i}$ are measured with respect to the body frame. Our expression (9.6) for the change of the body basis then becomes 

$$
\frac {d \mathbf {e} _ {i}}{d t} = \Omega_ {i k} \mathbf {e} _ {k} = \epsilon_ {i k j} \omega_ {j} \mathbf {e} _ {k} = \pmb {\omega} \times \mathbf {e} _ {i}\tag{9.11}
$$

where, in the final step, we've used the fact that our body frame basis is right-handed and so obeys $\mathbf{e}_i \times \mathbf{e}_j = \epsilon_{ijk}\mathbf{e}_k$ . Equivalently, expanding $\mathbf{x}(t) = x_i\mathbf{e}_i(t)$ in the body frame, we have 

$$
\frac {d \mathbf {x}}{d t} = x _ {i} \frac {d \mathbf {e} _ {i}}{d t} = x _ {i} \pmb {\omega} \times \mathbf {e} _ {i} = \pmb {\omega} \times \mathbf {x}.\tag{9.12}
$$

We already met (9.11) in Chapter 6 in the context of rotating frames. There we gave just a little justification and then wrote it down. (See equation (6.2).) The derivation given above was much more formal. 

We can build some intuition for $\omega$ by looking at a rigid body rotating around the z-axis, as shown in the figure below. Consider some point in the rigid body. In spherical polar coordinates $(r, \theta, \phi)$ , this point sits at the position 

$$
\mathbf {x} = (r \cos \theta \sin \phi , r \cos \theta \cos \phi , r \sin \theta).
$$

The angular coordinate $\phi$ is rotating, meaning that $\dot{\phi} \neq 0$ , so the velocity is 

$$
\dot {\mathbf {x}} = (r \cos \theta \cos \phi , - r \cos \theta \sin \phi , 0) \dot {\phi}.
$$

If we introduce the angular velocity vector $\omega = \dot{\phi}\hat{z}$ , then we can write this as 

$$
\dot {\mathbf {x}} = \boldsymbol {\omega} \times \mathbf {x}\tag{9.13}
$$

as claimed. Note that the angular velocity vector is defined in a right-handed sense. This means that if you curl the fingers of your right hand in the direction of rotation, then your thumb points in the direction of $\omega$ . 

Finally, we mentioned above that, in addition to asking how $\mathbf{e}_{i}(t)$ changes with time, we could also ask how the space frame coordinates $\tilde{x}_{i}(t)$ change with time. Differentiating (9.5), we have 

$$
\frac {d \tilde {x} _ {j}}{d t} = x _ {i} \frac {d R _ {i j}}{d t} = \tilde {x} _ {k} R _ {i k} \frac {d R _ {i j}}{d t}.\tag{9.14}
$$

Stare closely at the indices and you'll see that it's not the angular velocity matrix $\Omega = \dot{R} R^{T}$ that appears in this expression. Instead, we have 

$\dot{\tilde{x}}_{j} = \tilde{x}_{k}\tilde{\Omega}_{kj}$ , with 

$$
\tilde {\Omega} = R ^ {T} \frac {d R}{d t}.\tag{9.15}
$$

The matrices $R^{T}$ and $\dot{R}$ appear in the opposite order in this new matrix $\tilde{\Omega}$ compared to the angular velocity matrix $\Omega$ . The matrix $\tilde{\Omega}$ is sometimes called the convective angular velocity. You can think of the two as like the difference between passive and active transformations. As these things are confusing, it's best to pick one and stick with it. So for the rest of this book we will work only with our original $\Omega = \dot{R}R^{T}$ defined in (9.7). 

## 9.1.2 An Aside: Path-Ordered Exponentials

Our goal throughout this chapter will be to figure out the angular velocity vector $\omega(t)$ of various objects as they spin. Once we've got an expression for $\omega(t)$ , we'll typically just declare success and move on. However, as we've seen, the configuration space $\mathcal{C}$ is actually parameterised by the $SO(3)$ matrix $R(t)$ . So one might wonder how, given $\omega(t)$ , we can reconstruct the evolution of $R(t)$ . The purpose of this short section is to briefly explain how to do this, at least in principle. 

As we've seen above, the angular momentum vector $\omega$ is equivalent to the anti-symmetric matrix $\Omega_{ij} = \epsilon_{ijk}\omega_k$ and we can determine the rotation matrix $R(t)$ by solving the differential equation 

$$
\Omega = \frac {d R}{d t}   R ^ {- 1} \quad \Longrightarrow \quad \frac {d R}{d t} = \Omega R .\tag{9.16}
$$

So what do solutions to this equation look like? If $\Omega$ and R were scalar functions of time, then life would be straightforward: we could simply integrate this equation to get the solution 

$$
R (t) = \exp \left(\int_ {0} ^ {t} \Omega (t ^ {\prime}) d t ^ {\prime}\right)\tag{9.17}
$$

which satisfies the initial condition $R(0) = 1$ . But things are slightly more complicated because both $\Omega$ and R are matrices. As we now show, the would-be solution (9.17) no longer works for matrices. 

To see what goes wrong with $(9.17)$ , first recall that the exponential of any matrix M is defined by the Taylor expansion, 

$$
\exp (M) \equiv 1 + M + \frac {1}{2} M ^ {2} + \dots .\tag{9.18}
$$

This means that we should think of the would-be solution (9.17) as a Taylor expansion in $M = \int_{0}^{t} \Omega(t') dt'$ . The trouble comes when we get to the quadratic term in the expansion. If we differentiate this with respect to time, we have 

$$
\frac {1}{2} \frac {d}{d t} \left(\int_ {0} ^ {t} \Omega (t ^ {\prime}) d t ^ {\prime}\right) ^ {2} = \frac {1}{2} \Omega (t) \left(\int_ {0} ^ {t} \Omega (t ^ {\prime}) d t ^ {\prime}\right) + \frac {1}{2} \left(\int_ {0} ^ {t} \Omega (t ^ {\prime}) d t ^ {\prime}\right) \Omega
$$

The ordering here is important. In particular, we can't commute the $\Omega(t)$ past the terms in the integral with $\Omega(t')$ with $t' \neq t$ because there is no reason to think that the angular velocity matrices $\Omega(t)$ commute at different times. This is the reason that (9.17) does not solve our original equation (9.16). The first term on the right-hand side of (9.19) looks good, since this also appears in the Taylor expansion of $\Omega R$ . But the second term isn't right just because the $\Omega(t)$ sits in the wrong place. The upshot is that equation (9.17) is not the solution to (9.16) when $\Omega$ and $R$ are matrices. 

However, seeing how $(9.17)$ fails does give us an idea for how to proceed. Since the problem is in the ordering of the matrices, the correct solution to $(9.16)$ takes a similar form to $(9.17)$ , but with a different ordering. This is known as the time-ordered exponential, and is denoted as 

$$
R (t) = T \exp \left(\int_ {0} ^ {t} \Omega (t ^ {\prime}) d t ^ {\prime}\right).\tag{9.20}
$$

All the subtleties are hiding in that capital T that sits in front. This means that when we Taylor expand the exponential, all matrices are ordered so that later times appear on the left. In other words 

$$
R (t) = 1 + \int_ {0} ^ {t} \Omega (t ^ {\prime}) d t ^ {\prime} + \int_ {0} ^ {t} \left(\Omega (t ^ {\prime \prime}) \int_ {0} ^ {t ^ {\prime \prime}} \Omega (t ^ {\prime}) d t ^ {\prime}\right) d t ^ {\prime \prime} + \dots .
$$

The double integral is taken over the range $0 < t' < t'' < t$ . If we now differentiate this double integral with respect to t, we get just the one term, 

$$
\frac {d}{d t} \int_ {0} ^ {t} \left(\Omega (t ^ {\prime \prime}) \int_ {0} ^ {t ^ {\prime \prime}} \Omega (t ^ {\prime}) d t ^ {\prime}\right) d t ^ {\prime \prime} = \Omega (t) \left(\int_ {0} ^ {t} \Omega (t ^ {\prime}) d t ^ {\prime}\right)
$$

instead of the two that appear in $(9.19)$ . It can be checked that the higher terms in the Taylor expansion also have the correct property if they are ordered so that matrices evaluated at later times appear to the left in the integrals. 

In some ways, the solution (9.21) feels a bit like cheating. To some extent, we solved the problem by introducing a new notation – the time-ordering symbol T – to do the job for us. And it’s certainly true that for a given $\Omega(t)$ it can be difficult to explicitly construct the corresponding $R(t)$ . Nonetheless, this kind of ordered integral shows up frequently in theories involving non-commuting matrices. (A particularly important example is Dyson’s formula which we’ll meet in Volume 3 on Quantum Mechanics.) 

As an aside, there's some interesting group theory lurking in (9.21). We've already seen that the rotation matrix $R(t)$ lies in the group $SO(3)$ . Continuous groups of this kind are known as Lie groups. It's a fact that any element of a Lie group can be written as the exponential of a different kind of matrix which, in this case, is the anti-symmetric angular velocity matrix $\Omega$ . The matrices that sit in the exponents are said to belong to the 

Lie algebra, usually denoted in lower case as $so(3)$ . And the Lie algebra $so(3)$ is defined to be the space of $3 \times 3$ anti-symmetric matrices. 

## 9.2 The Inertia Tensor

The previous section gave us the tools to describe the rotation of a rigid body. Now we want to understand how it actually moves. The way to do this is to look at the kinetic energy. For a pinned, rotating rigid body this is given by 

$$
\begin{array}{l} T = \frac {1}{2} \sum_ {a} m _ {a} \dot {\mathbf {x}} _ {a} ^ {2} \\ = \frac {1}{2} \sum_ {a} m _ {a} (\boldsymbol {\omega} \times \mathbf {x} _ {a}) \cdot (\boldsymbol {\omega} \times \mathbf {x} _ {a}) \\ = \frac {1}{2} \sum_ {a} m _ {a} ((\boldsymbol {\omega} \cdot \boldsymbol {\omega}) (\mathbf {x} _ {a} \cdot \mathbf {x} _ {a}) - (\mathbf {x} _ {a} \cdot \boldsymbol {\omega}) ^ {2}). \end{array}\tag{9.23}
$$

We can succinctly write this as 

$$
T = \frac {1}{2} \omega_ {i} \mathcal {I} _ {i j} \omega_ {j}\tag{9.24}
$$

where $I_{ij}$ , with i, j = 1, 2, 3, are the components of the inertia tensor measured in the body frame 

$$
\mathcal {I} _ {i j} = \sum_ {a} m _ {a} \left((\mathbf {x} _ {a} \cdot \mathbf {x} _ {a}) \delta_ {i j} - (\mathbf {x} _ {a}) _ {i} (\mathbf {x} _ {a}) _ {j}\right) .\tag{9.25}
$$

Note that the inertia tensor is symmetric: $\mathcal{I}_{ij} = \mathcal{I}_{ji}$ . Furthermore, the components are independent of time since they are measured with respect to the body frame. As we mentioned in the introduction to this section, we will often be interested in continuous bodies with density $\rho(\mathbf{x})$ , rather than discrete point masses. In this case, there's an obvious, analogous expression for the inertia tensor 

$$
\mathcal {I} = \int d ^ {3} \mathbf {x}   \rho (\mathbf {x})   \left( \begin{array}{c c c} y ^ {2} + z ^ {2} & - x y & - x z \\ - x y & x ^ {2} + z ^ {2} & - y z \\ - x z & - y z & x ^ {2} + y ^ {2} \end{array} \right)  .\tag{}
$$

Now comes the key point. Because $I_{ij}$ is a symmetric real matrix, we can diagonalise it. Moreover, it can be diagonalised by an orthogonal matrix O, such that 

$$
O I O ^ {T} = \mathcal {I} ^ {\prime} = \operatorname{diag} (I _ {1}, I _ {2}, I _ {3})\tag{9.27}
$$

where $O^{T}O = 1$ , the unit matrix. This means that O can be viewed as a rotation of the original body frame basis $\{e_{i}\}$ to a new basis $\{Oe_{i}\}$ . This new basis is precisely the eigenvectors of the inertia tensor I. 

Physically, there's something rather surprising about this result. It means that every object, no matter how complicated, has a preferred set of orthogonal axes sitting within it. For an object that has a lot of symmetry, this is obvious as the axes simply align with the symmetry. For example, for a cube rotating around its middle point, the axes will be perpendicular to the faces of the cube. But complicated objects that have no symmetry at all also have a preferred set of axes. These are the eigenvectors of the inertia tensor. 

The preferred body frame axes are known as principal axes. As we have seen, in this frame the inertia tensor takes the diagonal form 

$$
\mathcal {I} = \operatorname{diag} (I _ {1}, I _ {2}, I _ {3}).\tag{9.28}
$$

The eigenvalues $I_{i}$ are called the principal moments of inertia. The kinematical properties of a rigid body are fully determined by its mass, principal axes, and moments of inertia. The moments of inertia $I_{1}, I_{2}$ , and $I_{3}$ are to rotations what the mass is to translations. The bigger the $I_{i}$ , the more energy you need to supply to the body to make it spin in about the axis $e_{i}$ . 

The principal moments of inertia are real and positive. To see this, consider some arbitrary vector n and look at 

$$
\mathcal {I} _ {j k} n ^ {j} n ^ {k} = \sum_ {a = 1} ^ {N} m _ {a} (\mathbf {x} _ {a} ^ {2} \mathbf {n} ^ {2} - (\mathbf {x} _ {a} \cdot \mathbf {n}) ^ {2}) \geq 0.\tag{9.29}
$$

The inequality is a strict equality only if all the $x_{a}$ lie on a line. If n is the $i^{th}$ eigenvector of I then this result becomes $I_{jk}n^{j}n^{k}=I_{i}|\mathbf{n}|^{2}$ , which tells us $I_{i}\geq0$ . 

As we've seen, any object has three preferred axes buried within it. But the object need not necessarily be spinning around one of these axes. If the object spins around a general axis $\hat{\mathbf{n}}$ , with $\hat{\mathbf{n}} \cdot \hat{\mathbf{n}} = -1$ , then we define 

$$
I = \mathbf {n} ^ {T} \cdot \mathcal {I} \mathbf {n}.\tag{9.30}
$$

This is the moment of inertia of the rigid body about the axis $\hat{n}$ . 

## 9.2.1 Angular Momentum

The result $(9.24)$ shows that the kinetic energy of a rotating body is written in terms of the inertia tensor. That alone is reason to be interested in the inertia tensor. However, as we now show, the angular momentum or a rigid body also has a nice description in terms of the inertia tensor. 

Again, we consider the case where the body is pinned at some point P, about which it rotates. We have 

$$
\begin{array}{r l} & {\mathbf {L} = \sum_ {a} m _ {a} \mathbf {x} _ {a} \times \dot {\mathbf {x}} _ {a}} \\ & {\quad = \sum_ {a} m _ {a} \mathbf {x} _ {a} \times (\pmb {\omega} \times \mathbf {x} _ {a})} \\ & {\quad = \sum_ {a} m _ {a} ((\mathbf {x} _ {a} \cdot \mathbf {x} _ {a}) \pmb {\omega} - (\pmb {\omega} \cdot \mathbf {x} _ {a}) \mathbf {x} _ {a}).} \end{array}\tag{9.31}
$$

We recognise the two terms in the sum as the inertia tensor $(9.25)$ , now multiplying the angular velocity $\omega$ 

$$
\mathbf {L} = \mathcal {I} \boldsymbol {\omega}.\tag{9.32}
$$

Perhaps counterintuitively, the angular momentum L is not necessarily aligned with the spin $\omega$ . If the spin happens to point along a principal axis of the rigid body then $\omega$ and L do align. Otherwise $\omega$ and L point in different directions. Many of the more peculiar properties of spinning objects follow from this simple fact. 

The components of the inertia tensor $I_{ij}$ are written in the body frame. We then have 

$$
L _ {i} = I _ {i j} \omega_ {j}\tag{9.33}
$$

where $L = L_{i}e_{i}$ and $\omega = \omega_{i}e_{i}$ . 

## 9.2.2 Computing the Inertia Tensor for Simple Examples

Computing the inertia tensor is a straightforward exercise. Here we present three of the simplest examples. 

## The Rod

As a first example, consider a uniform, one-dimensional rod of length $L$ and mass $M$ and, hence, density $\rho = M / L$ . We will compute the inertia tensor about the centre of the rod. We take the rod to be aligned along the $z$ -axis. Because we're treating this as a strictly one-dimensional object, sitting at $x = y = 0$ , we have $I_3 = 0$ . By symmetry, the inertia tensor then takes the form $\mathcal{I}=\mathrm{diag}(I,I,0)$ where a quick calculation is needed to figure out the moment of inertia I 

$$
I = \int_ {- L / 2} ^ {L / 2} \rho z ^ {2} d z = \frac {1}{1 2} M L ^ {2}.\tag{9.34}
$$

This is the moment of inertia for rotating around any axis perpendicular to the rod. 

## The Disc

Now consider a uniform disc of radius $a$ and mass $M$ , lying in the $(x, y)$ -plane. Two-dimensional objects, such as the disc, are sometimes referred to as laminas. The density of the disc is $\rho = M / \pi a^2$ . We'll again compute $\mathcal{I}$ about the centre of the disc. This time we have $\mathcal{I} = \mathrm{diag}(I_1, I_2, I_3)$ , with 

$$
I _ {1} = \int \rho y ^ {2} d ^ {2} x \quad \text { and } \quad I _ {2} = \int \rho x ^ {2} d ^ {2} x .\tag{9.35}
$$

So $I_{1} = I_{2}$ by symmetry, while 

$$
I _ {3} = \int \rho (x ^ {2} + y ^ {2}) d ^ {2} x.\tag{9.36}
$$

Therefore 

$$
I _ {3} = I _ {1} + I _ {2} = 2 \pi \rho \int_ {0} ^ {a} r ^ {3} d r = \frac {1}{2} M a ^ {2}\tag{9.37}
$$

and the moments of inertia are $I_{1} = I_{2} = \frac{1}{4} Ma^{2}$ and $I_{3} = \frac{1}{2} Ma^{2}$ . 

These two calculations illustrate a general fact about laminas, even those without any symmetry. If we take the z-axis to lie perpendicular to the plane of the lamina, then the moments of inertia about the x- and y-axes are $I_{x} = \int \rho y^{2} dA$ and $I_{y} = \int \rho x^{2} dA$ . Meanwhile, the distance of any point to the z-axis is $r = \sqrt{x^{2} + y^{2}}$ , so the moment of inertia about the z-axis is 

$$
I _ {z} = \int \rho (x ^ {2} + y ^ {2}) d A = I _ {x} + I _ {y}.\tag{9.38}
$$

This is known as the perpendicular axis theorem. 

## A Sphere

A uniform sphere has radius a and mass $M = \frac{4}{3}\pi\rho a^{3}$ . By symmetry, the inertia tensor is proportional to the unit matrix, I = I1, with all moments of inertia the same. 

To compute the moment of inertia I, we pick spherical polar coordinates with the axis $\theta = 0$ pointing along the axis of rotation which passes through the centre of the sphere. A point with coordinates $(r, \theta, \phi)$ sits at a distance $r \sin \theta$ from the axis of rotation. We also have the Jacobian 

factor $r^{2}\sin\theta$ , so that the volume element is $dV = r^{2}\sin\theta drd\theta d\phi$ with $\theta \in [0,\pi]$ and $\phi \in [0,2\pi)$ . The moment of inertia is 

$$
I = \int_ {0} ^ {a} \int_ {0} ^ {\pi} \int_ {0} ^ {2 \pi} \rho (r \sin \theta) ^ {2} r ^ {2} \sin \theta d r d \theta d \phi = \frac {8}{1 5} \pi \rho a ^ {5} = \frac {2}{5} M a ^ {2}
$$

The moments of inertia for all these examples are a number of order 1, multiplied by mass $\times$ distance $_{2}$ , as they must be on dimensional grounds. 

## 9.2.3 Parallel Axis Theorem

The inertia tensor depends on what point P in the body is held fixed. In general, if we know I about a point P then it is messy to compute $I'$ about some other point $P'$ . But this computation becomes very simple if P happens to coincide with the centre of mass of the object. This follows from the parallel axis theorem: 

Claim: If an object of mass M has inertia tensor I about the centre of mass, and $P'$ is displaced by a vector d from the centre of mass, then the inertia tensor about $P'$ is 

$$
\mathcal {I} _ {i j} ^ {\prime} = \mathcal {I} _ {i j} + M (\mathbf {d} ^ {2} \delta_ {i j} - \mathbf {d} _ {i} \mathbf {d} _ {j}).\tag{9.40}
$$

Note that the additional term $M(\mathbf{d}^{2}\delta_{ij}-\mathbf{d}_{i}\mathbf{d}_{j})$ is the inertia tensor we would find for a point mass M sitting at point d. 

Proof: The proof is of the plug-it-in-and-check variety 

$$
\begin{array}{l} \mathcal {I} _ {i j} ^ {\prime} = \sum_ {a} m _ {a} \left\{(\mathbf {x} _ {a} - \mathbf {d}) ^ {2} \delta_ {i j} - (\mathbf {x} _ {a} - \mathbf {d}) _ {i} (\mathbf {x} _ {a} - \mathbf {d}) _ {j} \right\} \\ = \sum_ {a} m _ {a} \Big ((\mathbf {x} _ {a} \cdot \mathbf {x} _ {a}) \delta_ {i j} - (\mathbf {x} _ {a}) _ {i} (\mathbf {x} _ {a}) _ {j} + \mathbf {d} ^ {2} \delta_ {i j} - \mathbf {d} _ {i} \mathbf {d} _ {j} \\ \qquad \qquad \qquad - \left[ 2 \mathbf {x} _ {a} \cdot \mathbf {d}   \delta_ {i j} - (\mathbf {x} _ {a}) _ {i} \mathbf {d} _ {j} - (\mathbf {x} _ {a}) _ {j} \mathbf {d} _ {i} \right] \Big)  . \end{array}
$$

But each term on the second line is linear in $x_{a}$ , and so proportional to $\sum m_{a}x_{a}$ which vanishes if $x_{a}$ is measured from the centre of mass. The remaining terms give the promised result 

Here are two examples of the parallel axis theorem in action. 

## The Rod Again

The inertia tensor of the rod about one of its ends is 

$$
I _ {1} = \frac {1}{1 2} M L ^ {2} + M (L / 2) ^ {2} = \frac {1}{3} M L ^ {2}.\tag{9.42}
$$

## The Disc Again

We can consider our previous example of the disc, now displaced by $\mathbf{d} = (d, 0, 0)$ from the centre. We have 

$$
\begin{array}{l} \mathcal {I} _ {\mathbf {c}} ^ {\prime} = \frac {M}{4} \left( \begin{array}{c c c} a ^ {2} & & \\ & a ^ {2} & \\ & & 2 a ^ {2} \end{array} \right) + M \left( \begin{array}{c c c} 0 & & \\ & d ^ {2} & \\ & & d ^ {2} \end{array} \right) \\ = \frac {M}{4} \left( \begin{array}{c c c} a ^ {2} & & \\ & a ^ {2} + 4 d ^ {2} & \\ & & 2 a ^ {2} + 4 d ^ {2} \end{array} \right). \end{array}
$$

Note that $I'$ remains diagonal because we have shifted the point P along a principal axis. 

## 9.3 Motion of a Rigid Body: Preliminaries

Until now, we've only considered rigid bodies pinned at some point $P$ . Now we free things up and think about rigid bodies whose centre of mass is free to move. 

The most general motion of a rigid body is an overall translation, superposed with a rotation. We could choose to describe the rotation as being about any point, either inside or outside the body. But, as we now show, nice things happen if we choose the point of rotation to be about the centre of mass. We will write the position of a general point $x_{a}$ in the rigid body as 

$$
\mathbf {x} _ {a} (t) = \mathbf {R} (t) + \mathbf {y} _ {a} (t),\tag{9.44}
$$

where R is the centre of mass and, by definition, $y_{a}$ is the position measured from the centre of mass. If the body rotates with angular velocity $\omega$ about the centre of mass, then we have 

$$
\dot {\mathbf {y}} _ {a} = \boldsymbol {\omega} \times \mathbf {y} _ {a}.\tag{9.45}
$$

The kinetic energy for the rigid body is then 

$$
\begin{array}{r l} & T = \frac {1}{2} \sum_ {a} m _ {a} \dot {\mathbf {x}} _ {a} ^ {2} \\ & \quad = \sum_ {a} m _ {a} \left[ \frac {1}{2} \dot {\mathbf {R}} ^ {2} + \dot {\mathbf {R}} \cdot (\pmb {\omega} \times \mathbf {y} _ {a}) + \frac {1}{2} (\pmb {\omega} \times \mathbf {y} _ {a}) ^ {2} \right] \\ & \quad = \frac {1}{2} M \dot {\mathbf {R}} ^ {2} + \frac {1}{2} \pmb {\omega} _ {i} \mathcal {I} _ {i j} \pmb {\omega} _ {j} \end{array}\tag{9.4¢}
$$

where, to go to the final line, we've used the fact that $\sum_{a} m_{a} \mathbf{y}_{a} = 0$ , which ensures that the term linear in $\omega$ vanishes. We've also used our original definition of the inertia tensor (9.24) as it appears in the kinetic energy of a rotating body. This is a rather nice result: it tells us that the dynamics separates into the translational motion of the centre of mass $\mathbf{R}$ , together with rotation about the centre of mass. Happily, this means that the work we did in the previous sections describing an object that rotates about a fixed point, is also valid for a free object. 

## Motion with Rotation about A Different Point

It is certainly most natural to split the motion into the centre of mass trajectory $\mathbf{R}(t)$ together with rotation about the centre of mass. With this choice, Newton's second law (4.10) ensures that $\mathbf{R}(t)$ is dictated only by external forces. Moreover, the kinetic energy splits nicely into translational and rotational energies, as seen in (9.46). But nothing tells us that we have to describe an object in this way. We could, instead, decide that it's better to think of the motion in terms of some other point $\mathbf{Q}$ (say the tip of the nose of a dead, rigid cat), together with rotation about $\mathbf{Q}$ . 

We can derive an expression for such motion using our results above. From $(9.44)$ and $(9.45)$ , the velocity of a general point $x_{a}$ in the rigid body is 

$$
\dot {\mathbf {x}} _ {a} = \dot {\mathbf {R}} + \boldsymbol {\omega} \times (\mathbf {x} _ {a} - \mathbf {R}).\tag{9.47}
$$

We can apply this formula to $x_{a} = Q$ itself, to get 

$$
\dot {\mathbf {Q}} = \dot {\mathbf {R}} + \boldsymbol {\omega} \times (\mathbf {Q} - \mathbf {R}).\tag{9.48}
$$

If we then substitute this back into $(9.47)$ to eliminate $\dot{R}$ , we get an expression for the motion of any point $x_{a}$ about Q, 

$$
\dot {\mathbf {x}} _ {a} = \dot {\mathbf {Q}} + \boldsymbol {\omega} \times (\mathbf {x} _ {a} - \mathbf {Q}).\tag{9.49}
$$

There's something a little counterintuitive about this result. It tells us that if the angular velocity is $\omega$ about the centre of mass, then the angular velocity about any other point $\mathbf{Q}$ will also be $\omega$ . 

## 9.3.1 Roll, Don't Slip

As a simple example of these ideas, we look at a hoop of radius $a$ as shown in the figure. In this case, the translational speed and the angular speed are related. This comes about if we insist that there is no slipping between the hoop and the ground, a requirement that is usually, quite reasonably, called the no-slip condition. 

Consider point A of the hoop which, at a given instance, is in contact with the ground. The no-slip condition is the statement that point A is instantaneously at rest. In other words, it has no speed relative to the ground. If we denote the angular speed of the hoop as $\dot{\theta}$ , then the no-slip condition means that the horizontal speed v of the origin is 

$$
v = a \dot {\theta}.\tag{9.50}
$$

What, however, is the speed of a different point, P, on the circumference? When $\theta = 0$ , so P sits at the top of the hoop, the horizontal speed is $a\dot{\theta}$ with respect to centre, resulting in a total horizontal speed of $2a\dot{\theta}$ . 

To compute the speed of a general point P, it's best to think about the hoop as rotating about A. From the argument above, we know that the angular speed about A is also $\dot{\theta}$ . But the distance $AP = 2a \cos(\theta/2)$ , which means that the speed v of the point P relative to A (which is the same as relative to the ground) is 

$$
v = 2 a \dot {\theta} \cos (\theta / 2).\tag{9.51}
$$

We can check that this gives the right answer when P is at the top and bottom of the hoop: $\theta = 0$ and $\theta = \pi$ gives $v = 2a\dot{\theta}$ and v = 0 respectively, as it should. 

The velocity of the point P does not lie tangent to the circle. That would only be the case if the hoop was rotating while staying fixed. Instead the velocity of point P is at right-angles to the line AP. This reflects the fact that the point P is rotating about the origin, but also moving forwards as the hoop moves. 

Finally, a quick comment: despite the presence of friction, this is one example where we can still use energy conservation. This is because the point of the wheel that is in contact with the ground is at rest, which means that friction acting on this point does no work. Instead, the only role of friction is to impose the no-slip condition. 

## 9.3.2 A Swinging Rod

We've discussed the pendulum several times already in this book. But, each time we've always consisted of a mass sitting at the end of a light rod, where light means effectively massless. Let's now look at an example where the rod itself has mass $m$ . 

This is a case where it's most natural to think about rotation around the pivot at the end of the rod, rather than around the centre of mass. We already calculated the moment of inertia $I$ for a rod of length $L$ which pivots about its end point in (9.42): it is $I = \frac{1}{3} mL^2$ . 

If the rod has angular speed $\omega = \dot{\theta}$ , then the kinetic energy can be written as 

$$
T = \frac {1}{2} I \dot {\theta} ^ {2}.\tag{9.52}
$$

Alternatively, we could view this as motion of the centre of mass, together with rotation around the centre of mass. As we saw above, the angular 

speed about the centre of mass remains $\dot{\theta}$ : it is the same as the angular speed about the pivot. The speed of the centre of mass is $v = (L/2)\dot{\theta}$ and the kinetic energy splits in the form (9.46) 

$$
\begin{array}{l} T = \text { translational   K.E. } + \text { rotational   K.E. } \\ = \frac {1}{2} m \left(\frac {L}{2} \dot {\theta}\right) ^ {2} + \frac {1}{2} I _ {\text { CoM }} \dot {\theta} ^ {2} . \end{array}\tag{9.53}
$$

But, by the parallel axis theorem, we know that $I = I_{\mathrm{CoM}} + m(L/2)^{2}$ which happily means that the kinetic energies computed in these two different ways coincide. 

To derive the equation of motion of the pendulum, it's perhaps easiest to first get the energy. The centre of mass of the pendulum sits at a distance $-(L/2)\cos\theta$ below the pivot. So combining the kinetic and gravitational energies, we have 

$$
E = \frac {1}{2} I \dot {\theta} ^ {2} - m g \frac {L}{2} \cos \theta .\tag{9.54}
$$

Differentiating with respect to time, we get the equation of motion 

$$
I \ddot {\theta} = - m g \frac {L}{2} \sin \theta .\tag{9.55}
$$

We can compare this with our earlier treatment of a pendulum where all the mass sits at the end of the length l. In that case, the equation of 

motion is $(2.29)$ . We see that the equations of motion agree if set $l = 2I/Lm = 2L/3$ . 

## 9.3.3 A Rolling Disc

A disc of mass $M$ and radius $a$ rolls down a slope without slipping. The plane of the disc is vertical. The moment of inertia of the disc about an axis which passes through the centre, perpendicular to the plane of the disc, is $I$ . (We already know from our earlier calculation that $I = \frac{1}{2} Ma^2$ , but we'll leave it general for now). 

We denote the speed of the disc down the slope as v and the angular speed of the disc as $\omega$ . (From the picture and the right-hand rule, we see that the angular velocity $\omega$ is a vector pointing out of the page). As in (9.50), the no-slip condition gives us the relation 

$$
v = a \omega .\tag{9.56}
$$

To understand the motion of the disc, it is simplest to work with the energy. This is allowed since, as we mentioned before, when friction imposes the no-slip condition it does no work. We've seen a number of times that the kinetic energy splits into the translational kinetic energy of the centre of mass, together with the rotational kinetic energy about the centre of mass. (See equation (9.46).) In the present case, this means 

$$
T = \frac {1}{2} M v ^ {2} + \frac {1}{2} I \omega^ {2} = \frac {1}{2} \left(\frac {I}{a ^ {2}} + M\right) v ^ {2}.\tag{9.57}
$$

Including the gravitational potential energy, we have 

$$
E = \frac {1}{2} \left(\frac {I}{a ^ {2}} + M\right) \dot {x} ^ {2} - M g x \sin \alpha\tag{9.58}
$$

where x measures the progress of the disc down the slope, so $\dot{x} = v$ . From this we can derive the equation of motion simply by taking the time derivative. We have 

$$
\left(\frac {I}{a ^ {2}} + M\right) \ddot {x} = M g \sin \alpha .\tag{9.59}
$$

We learn that, while the overall mass M drops out of the calculation (recall that I is proportional to M), the moment of inertia I does not. The larger the moment of inertia I of an object, the slower its progress down the slope. This is because the gravitational potential energy is converted into both translational and rotational kinetic energy. But only the former affects how fast the object makes it down. 

Take two identical barrels, one empty and the other filled with cheese, and roll them down a hill. The cheesy one will make it to the bottom first. But this isn't because it's heavier. It's because it has a smaller ratio $I / M$ . 

## 9.4 Euler's Equations

With the simple examples above behind us, we now turn to some more sophisticated examples of the motion of rigid bodies. In this section, we discuss so-called free tops. You should think of this as a rigid body that is suspended in space so that it can freely move or rotate in any direction. In particular, the body won't experience any reaction forces, like the rolling disc of the last section. Nor will it experience the effect of gravity (an omission that we'll remedy in Section 9.6). That means that the analysis of this section will describe planets or satellites, or simply objects in free fall if we're uninterested in the acceleration downwards. 

The basic idea underlying the rotation of a free, rigid body is very simple: angular momentum is conserved. This gives us the vector equation 

$$
\frac {d \mathbf {L}}{d t} = 0.\tag{9.60}
$$

We expand this in the body frame, with $L = L_{i}e_{i}$ . Both the components $L_{i}$ and the basis vectors $e_{i}$ can change with time, so we have 

$$
0 = \frac {d \mathbf {L}}{d t} = \frac {d L _ {i}}{d t} \mathbf {e} _ {i} + L _ {i} \frac {d \mathbf {e} _ {i}}{d t} = \frac {d L _ {i}}{d t} \mathbf {e} _ {i} + L _ {i} \pmb {\omega} \times \mathbf {e} _ {i}\tag{9.61}
$$

where we've used the expression $\dot{\mathbf{e}}_i = \boldsymbol {\omega}\times \mathbf{e}_i$ , derived in (9.11), to express the change of the body frame basis in terms of the angular velocity $\omega = \omega_{i}\mathbf{e}_{i}$ . 

The next step is to combine (9.61) with the relation $\mathbf{L} = \mathcal{I}\omega$ from (9.32). Things are significantly simpler if we pick the body frame axes $\{\mathbf{e}_i\}$ to coincide with the principal axes. Then the inertia tensor is diagonal and the expression $L_{i} = \mathcal{I}_{ij}\omega_{j}$ is just $L_{1} = I_{1}\omega_{1}$ and so on. The conservation of angular momentum (9.60) now becomes three non-linear coupled first order differential equations, 

$$
\begin{array}{l} I _ {1} \dot {\omega} _ {1} + \omega_ {2} \omega_ {3} (I _ {3} - I _ {2}) = 0 \\ I _ {2} \dot {\omega} _ {2} + \omega_ {3} \omega_ {1} (I _ {1} - I _ {3}) = 0 \\ I _ {3} \dot {\omega} _ {3} + \omega_ {1} \omega_ {2} (I _ {2} - I _ {1}) = 0. \end{array}\tag{9.62}
$$

These are Euler's Equations. (Euler has way too many things named after him! Euler's equations are not to be confused with the more general Euler–Lagrange equations, nor with the equation for a fluid which is called the Euler equation.) 

It is straightforward to extend the analysis above to include a torque $\tau$ acting on the body. The equation of motion becomes $dL/dt = \tau$ and repeating the steps above results in Euler's equations (9.62), now with the components of the torque $\tau = \tau_{i}e_{i}$ , expanded in the body frame, arising on the right-hand side. 

## 9.4.1 The Symmetric Top

The simplest example of a rigid body is the sphere. It is, sadly, too simple. The moments of inertia all coincide, $I_{1} = I_{2} = I_{3}$ , which means that the inertia tensor I is diagonal and the angular momentum $\omega$ is always parallel to the angular momentum L. Euler's equations (9.62) then tell us that $\omega$ is constant. If you spin a sphere about some axis, then it continues to spin about the same axis. 

To find something more interesting, we need to go to the next simplest case. This an object with $I_{1} = I_{2} \neq I_{3}$ , known as the symmetric top. An example is shown in the figure to the right. Euler's equations (9.62) for the symmetric top are, 

$$
\begin{array}{l} I _ {1} \dot {\omega} _ {1} = \omega_ {2} \omega_ {3} (I _ {1} - I _ {3}), \\ I _ {2} \dot {\omega} _ {2} = - \omega_ {1} \omega_ {3} (I _ {1} - I _ {3}), \\ I _ {3} \dot {\omega} _ {3} = 0. \end{array}\tag{9.63}
$$

We see that $\omega_{3}$ , which is the spin about the axis of symmetry, is a constant of motion. In contrast, the spins about the other two axes vary in time, and obey the equations 

$$
\dot {\omega} _ {1} = \Omega \omega_ {2} \quad \text { and } \quad \dot {\omega} _ {2} = - \Omega \omega_ {1} \quad \text { with } \quad \Omega = \frac {I _ {1} - I _ {3}}{I _ {1}} \omega_ {3} .
$$

These are familiar equations, with $(\omega_{1}, \omega_{2})$ tracing out a circle 

$$
\omega_ {1} = \omega_ {0} \sin \Omega t \quad \mathrm{and} \quad \omega_ {2} = \omega_ {0} \cos \Omega t\tag{9.65}
$$

for some integration constant $\omega_{0}$ . Recall that the components $\omega_{i}$ in Euler's equations describe the angular velocity in the body frame. The solution (9.65) is then telling us that, in the body frame, the direction of the spin precesses about the axis of symmetry $e_{3}$ , with frequency $\Omega$ . Note from (9.64) that the sign of $\Omega$ depends on whether $I_{1} > I_{3}$ or $I_{1} < I_{3}$ . For a tall, skinny object, $I_{3} < I_{1}$ and $\Omega > 0$ . Meanwhile, a squat, fat object has $I_{1} < I_{3}$ and $\Omega < 0$ . Examples of the spin precession are shown in Figure 9.2. 

Fig. 9.2 The precession of the spin: the direction of precession depends on whether the object is tall and skinny with $I_{3} < I_{1}$ (known as a prolate spheroid) or is short and fat with $I_{3} > I_{1}$ (known as an oblate spheroid). 

The story above holds in the body frame, meaning it's relevant for someone unlucky enough to be clinging to the spinning object (presumably trying to keep their food down). But what does the situation look like for someone in the inertial, space frame? The angular momentum $\mathbf{L}$ is a fixed vector. But $\omega_{3}$ , and hence $L_{3}$ , are also fixed which ensures that the angle between $\mathbf{e}_{3}$ and $\mathbf{L}$ doesn't change in time. Instead, $\mathbf{e}_{3}$ precesses around $\mathbf{L}$ , while the body simultaneously spins such that $\omega$ remains between $\mathbf{e}_{3}$ and $\mathbf{L}$ . A picture of this motion, albeit one that is necessarily rather static, is shown to the right. The fact that $\omega$ precesses around the body frame axis $\mathbf{e}_{3}$ is sometimes referred to as a wobble. We'll return to the motion of the symmetric top in the space frame in Section 9.5.2 where we'll parameterise the motion in terms of Euler angles. 

## An Example: The Earth's Wobble

When we were children, our teachers told us that the Earth is round. They presumably meant this as a topological statement rather than a statement about the metric. The spin of the Earth causes it to bulge at the equator so that it is no longer a sphere but is closer to an oblate ellipsoid. In other words, the Earth is a symmetric top. The moments of inertia turn out to be 

$$
\frac {I _ {1} - I _ {3}}{I _ {1}} \approx - \frac {1}{3 0 0}.\tag{9.66}
$$

Our childhood teachers also told us that $\omega_{3}=2\pi\times(1\ day)^{-1}$ . This information is enough to calculate the frequency of the earth's wobble; from (9.64), it should be 

$$
\Omega_ {\mathrm{Earth}} = \frac {2 \pi}{3 0 0} \mathrm{day} ^ {- 1}.\tag{9.67}
$$

This calculation was first performed by Euler in 1749 who predicted that the Earth completes a wobble every 300 days. Note, however, that the size of the wobble isn't predicted by the analysis above: it is given by the integration constant $\omega_0$ . 

Despite many searches, this effect wasn't detected until 1891 when Chandler re-analysed the data and saw a wobble with a period of 427 days. It is now known as the Chandler wobble. It is very small! The angular velocity $\omega$ intercepts the surface of the earth approximately 10 metres from the 

North pole and precesses around it. A greatly exaggerated picture of the wobble is shown in the figure. 

More recent measurements place the frequency at 435 days. The discrepancy with the predicted 300 days can be traced to the fact that the Earth is not, in fact, a rigid body. Instead it is flexible because of tidal effects. Less well understood is why these same tidal effects haven't caused the wobble to dampen and disappear completely. There are various theories about what keeps the wobble alive, from earthquakes to fluctuating pressure at the bottom of the ocean. 

## 9.4.2 The Asymmetric Top: Stability

The most general rigid body has no symmetries and distinct moments of inertia, $I_i \neq I_j$ for $i \neq j$ . Euler's equations are now non-linear differential equations and the general solution is complicated. (We will give some insight into it in Section 9.4.3.) Here, we look at a special case of the motion and present a simple but striking result. 

The special situation that we're interested in is when the spin is aligned with one of the principal axes, say $\mathbf{e}_1$ , so that 

$$
\omega_ {1} = \Omega \quad \text { and } \quad \omega_ {2} = \omega_ {3} = 0 .\tag{9.68}
$$

This is a steady-state solution to Euler's equations (9.62), with $\dot{\omega}_i = 0$ . The question we want to ask is: what happens if we perturb the system, so that the spin lies close to the $\mathbf{e}_1$ axis, but isn't quite aligned. To answer this, we write the spin as 

$$
\omega_ {1} = \Omega + \eta_ {1}, \quad \omega_ {2} = \eta_ {2}, \quad \omega_ {3} = \eta_ {3}\tag{9.69}
$$

where $\eta_{i}$ , with $i = 1,2,3$ , are all taken to be small which, in this case, means $\eta_{i} \ll \Omega$ . Substituting this into Euler's equations, and ignoring terms of order $\eta^{2}$ and higher, we get the system of linear differential equations 

$$
\begin{array}{l} I _ {1} \dot {\eta} _ {1} = 0 \\ I _ {2} \dot {\eta} _ {2} = \Omega \eta_ {3} (I _ {3} - I _ {1}) \\ I _ {3} \dot {\eta} _ {3} = \Omega \eta_ {2} (I _ {1} - I _ {2}). \end{array}\tag{9.70}
$$

We substitute the third equation into the second to find an equation for just one of the perturbations, say $\eta_{2}$ , 

$$
I _ {2} \ddot {\eta} _ {2} = \Omega^ {2} \frac {(I _ {3} - I _ {1}) (I _ {1} - I _ {2})}{I _ {3}} \eta_ {2} \equiv A \eta_ {2}.\tag{9.71}
$$

The fate of the small perturbation depends on the sign of the quantity A. We have two possibilities: 

- $A < 0$ : In this case, the disturbance will oscillate around the original solution. 

- $A > 0$ : In this case, the disturbance will grow exponentially. 

Examining the definition of A, we find that if the body was originally spinning around the axis with the middle moment of inertia, meaning 

$$
I _ {2} <   I _ {1} <   I _ {3} \quad \text { or } \quad I _ {3} <   I _ {1} <   I _ {2} ,\tag{9.72}
$$

then the motion is unstable. In contrast, if the body was originally spinning about an axis with either the smallest moment of inertia $I_{1} < I_{2}, I_{3}$ or the largest moment of inertia $I_{1} > I_{2}, I_{3}$ , then the motion will be stable. 

You can get a vivid (and, if you're not careful, painful) demonstration of this result by picking up some suitable object – say a book or, if you're brave, a tennis racket – and trying it for yourself. Throw the object upwards, spinning around either the axis with the largest or smallest moment of inertia and it will gracefully return to you. Throw it spinning around the intermediate axis then good luck catching it as it tumbles and turns in unexpected directions due to the instability. 

## 9.4.3 The Poinsot Construction

As we mentioned above, for unequal moments of inertia, Euler's equations are non-linear. But they're not terribly non-linear and there's no chaotic motion. Indeed, it turns out that there is an analytic solution for the general solution of an asymmetric top, given in terms of elliptic functions. We won't describe this here, but instead present a nice, geometrical perspective on the motion, due to Poinsot. 

We start by working in the body frame. As always, we make progress by focussing on conserved quantities. There are two: the kinetic energy T and the magnitude of the angular momentum $L^{2}$ . In terms of the angular velocity, they are 

$$
2 T = I _ {1} \omega_ {1} ^ {2} + I _ {2} \omega_ {2} ^ {2} + I _ {3} \omega_ {3} ^ {2},\tag{9.73}
$$

$$
\mathbf {L} ^ {2} = I _ {1} ^ {2} \omega_ {1} ^ {2} + I _ {2} ^ {2} \omega_ {2} ^ {2} + I _ {3} ^ {2} \omega_ {3} ^ {2}.\tag{9.74}
$$

Each of these equations defines an ellipsoid in $\omega$ space. The motion of the vector $\omega$ is constrained to lie on the intersection of these two ellipsoids. The first of these ellipsoids, defined by 

$$
\frac {I _ {1}}{2 T} \omega_ {1} ^ {2} + \frac {I _ {2}}{2 T} \omega_ {2} ^ {2} + \frac {I _ {3}}{2 T} \omega_ {3} ^ {2} = 1\tag{9.75}
$$

is known as the inertia ellipsoid (or, sometimes, the inertia quadric). If we fix the kinetic energy, then we can think of this abstract ellipsoid as embedded within the object, rotating with it. 

We will take $I_{1} > I_{2} > I_{3}$ . This means that $\omega_{3}$ is the major axis of the inertial ellipsoid, while $\omega_{1}$ is the minor axis. The second ellipsoid, defined by (9.74), has the same major and minor axes because $I_{1}^{2} > I_{2}^{2} > I_{3}^{2}$ . To understand the motion in the body frame, we can consider the intersection of the two ellipsoids for different values of $L^{2}$ . These lines of intersection are drawn on the inertia ellipsoid in the figure below. 

On the major and minor axes, the two ellipsoids intersect in small closed orbits, as shown. Meanwhile, the behaviour is different along the intermediate axis $\omega_{2}$ , where the intersection appears as two crossed lines. This gives a graphical rendering of the result that we saw in the previous section. If the body is spinning along either the $\omega_{1}$ or $\omega_{3}$ axis, then a 

perturbation is stable, and the spin will precess around the original axis, tracing out the circles shown in the figure. Meanwhile, if it was originally spinning around $\omega_{2}$ , then a general perturbation will be unstable and the orientation of the spin will rapidly change when moved away from $e_{2}$ . 

The path that $\omega$ traces on the inertia ellipsoid is known as the polhode curve. One of the things we learn from this pictorial representation is that the polhode curves are always closed and therefore motion in the body frame is periodic. 

There is a slightly different way to view this. Equations $(9.73)$ and $(9.74)$ can be rearranged to give the condition 

$$
\left(2 I _ {1} T - \mathbf {L} ^ {2}\right) I _ {1} \omega_ {1} ^ {2} + \left(2 I _ {2} T - \mathbf {L} ^ {2}\right) I _ {2} \omega_ {2} ^ {2} + \left(2 I _ {3} T - \mathbf {L} ^ {2}\right) I _ {3} \omega_ {3} ^ {2} = 0
$$

This is the equation for a cone. To see this, note that if $\omega$ satisfies (9.76), then so does any rescaled vector $\lambda\omega$ for all real numbers $\lambda$ . It is known as the polhode cone. For fixed T and $L^{2}$ , the motion of $\omega$ in the body frame runs along the intersection of the inertia ellipsoid and the polhode cone. Two examples are shown in Figure 9.3, the first with $L^{2} < 2I_{2}T$ , the second with $2I_{2}T < L^{2} < 2I_{3}T$ , so that the orientation of the cone is different in the two cases. 

Fig. 9.3 The intersection of the inertia ellipsoid with the polhode cone. On the left, $L^{2} > 2I_{2}T$ and the cone is oriented along the $\omega_{3}$ axis. On the right, $2I_{2}T < L^{2} < 2I_{3}T$ , and the cone is oriented along the $\omega_{1}$ axis. 

The discussion above holds in the body frame. What does all this look like in the space frame? The vector L is a constant of motion. Since the kinetic energy $2T = L \cdot \omega$ is also constant, we learn that $\omega$ must lie in a fixed plane perpendicular to L. This is known as the invariable plane. The inertia ellipsoid touches the invariable plane at the point defined by the angular velocity vector $\omega$ . Moreover, the invariable plane is always tangent to the inertial ellipsoid at the point $\omega$ . To see this, note that the angular momentum can be written as 

$$
\mathbf {L} = \nabla_ {\omega} T\tag{9.77}
$$

where the gradient operator is in $\omega$ space, i.e. 

$\nabla_{\omega} = (\partial/\partial\omega_{1}, \partial/\partial\omega_{2}, \partial/\partial\omega_{3})$ . But recall that the inertia ellipsoid is defined as a level surface of T, so equation (9.77) tells us that the angular momentum L is always perpendicular to the ellipsoid. This, in turn, ensures that the invariable plane is always tangent to the ellipsoid. 

In summary, the angular velocity traces out two curves: one on the inertia ellipsoid, known as the polhode curve, and another on the invariable plane, known as the herpolhode curve. The body moves as if it is embedded within the inertia ellipsoid, which rolls around the invariable plane without slipping, with the centre of the ellipsoid a constant distance from the plane. The motion is shown in Figure 9.4. Unlike the polhode curve, the herpolhode curve does not necessarily close. 

Fig. 9.4 The inertia ellipsoid rolling around on the invariable plane, with the polhode and herpolhode curves drawn for a fixed time period. 

## 9.5 Euler Angles

So far, we've made a fair bit of progress simply by using the relation $\mathbf{L} = I\omega$ between angular momentum and angular velocity, and interpreting what this means for the tumbling motion of rigid bodies. We haven't yet needed to say anything about what this motion looks like in the configuration space $\mathcal{C}$ of the rigid body. 

However, to make further progress we will need to get a better handle on the way to describe the orientation of the rigid body. Recall that the configuration space is given by all possible rotations of a set of axes. An example of such a rotation is shown in Figure 9.5. Our first task is to find a way to explicitly parameterise such a rotation. There is a way do do this, due to Euler, that often leads to simple solutions for problems of interest. 

Fig. 9.5 The rotation from the space frame $\{\tilde{\mathbf{e}}_i\}$ to the body frame $\{\mathbf{e}_i\}$ . 

As an aside, we mentioned previously that the configuration space for a fixed, rigid body is actually the group $\mathcal{C} = SO(3)$ . This means that we will be looking for a way to parameterise the group manifold $SO(3)$ . 

The key idea is that arbitrary rotation may be expressed as the product of three successive rotations about three (in general) different axes. Let $\{\tilde{e}_{i}\}$ be space frame axes. Let $\{e_{i}\}$ be body frame axes. We want to find the rotation R so that $e_{i}=R_{ij}\tilde{e}_{j}$ . We can accomplish this in three steps: 

$$
\{\tilde {\mathbf {e}} _ {i} \} \stackrel {{R _ {3} (\phi)}} {{\longrightarrow}} \{\mathbf {e} _ {i} ^ {\prime} \} \stackrel {{R _ {1} (\theta)}} {{\longrightarrow}} \{\mathbf {e} _ {i} ^ {\prime \prime} \} \stackrel {{R _ {3} (\psi)}} {{\longrightarrow}} \{\mathbf {e} _ {i} \}\tag{9.78}
$$

Let's look at these steps in turn. 

Step 1: Rotate by $\phi$ about the $\tilde{\mathbf{e}}_3$ axis. So $\mathbf{e}_i' = R_3(\phi)_{ij}\tilde{\mathbf{e}}_j$ with 

$$
R _ {3} (\phi) = \left( \begin{array}{c c c} \cos \phi & \sin \phi & 0 \\ - \sin \phi & \cos \phi & 0 \\ 0 & 0 & 1 \end{array} \right) .\tag{9.79}
$$

This rotates the axes like this: 

Step 2: Next, we rotate by $\theta$ about the new axis $\mathbf{e}_1'$ . This axis $\mathbf{e}_1'$ is sometimes called the line of nodes. We write $\mathbf{e}_i'' = R_1(\theta)_{ij}\mathbf{e}_j'$ with 

$$
R _ {1} (\theta) = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & \cos \theta & \sin \theta \\ 0 & - \sin \theta & \cos \theta \end{array} \right) .\tag{9.80}
$$

This time, it acts on the axes like this: 

Step 3: Finally, we rotate by $\psi$ about the new new axis $\mathbf{e}_3^{\prime \prime}$ so $\mathbf{e}_i = R_3(\psi)_{ij}\mathbf{e}_j^{\prime \prime}$ with 

$$
R _ {3} (\psi) = \left( \begin{array}{c c c} \cos \psi & \sin \psi & 0 \\ - \sin \psi & \cos \psi & 0 \\ 0 & 0 & 1 \end{array} \right) .\tag{9.81}
$$

This final rotation looks like this: 

This brings us to the promised rotation shown in Figure 9.5. Putting it all together, we have 

$$
R _ {i j} (\phi , \theta , \psi) = [ R _ {3} (\psi) R _ {1} (\theta) R _ {3} (\phi) ] _ {i j}.\tag{9.82}
$$

Any general rotation of the space frame to the body frame can be written in this way. The angles $\phi$ , $\theta$ , and $\psi$ are known as Euler angles. 

In longhand, the matrix $R(\phi, \theta, \psi)$ needs a smaller font. It reads 

$$
R = \left( \begin{array}{c c c} \cos \psi \cos \phi - \cos \theta \sin \phi \sin \psi & \sin \phi \cos \psi + \cos \theta \sin \psi \cos \phi & \sin \theta \sin \phi \\ - \cos \phi \sin \psi - \cos \theta \cos \psi \sin \phi & - \sin \psi \sin \phi + \cos \theta \cos \psi \cos \phi & \sin \theta \cos \phi \\ \sin \theta \sin \phi & - \sin \theta \cos \phi & \cos \theta \end{array} \right)
$$

Before we proceed, a warning. Here we've thought about the rotations as acting on the basis vectors $\{\mathbf{e}_i\}$ . Some textbooks instead choose to think of the rotations as acting on the components of a vector $\mathbf{x} = x_i\mathbf{e}_i = \tilde{x}_i\tilde{\mathbf{e}}_i$ , writing $\tilde{x}_j = x_iR_{ij}$ . When expanded in terms of Euler angles, this can result in an apparent reversal of the ordering of the three rotation matrices in $(9.82)$ . 

## 9.5.1 Angular Velocity

There is a simple expression for the instantaneous angular velocity $\omega$ in terms of Euler angles. One way straightforward, but slightly tedious, way to derive this is to plug in the expression (9.82) into the definition (9.7) of the angular momentum matrix $\Omega = \dot{R}R^{-1}$ . However, a little thought about what this means physically will get us there quicker. Consider the motion of a rigid body in an infinitesimal time dt, during which each of the Euler angles will change a little 

$$
(\psi , \theta , \phi) \rightarrow (\psi + d \psi , \theta + d \theta , \phi + d \phi).\tag{9.83}
$$

From the definition of the Euler angles, the angular velocity must be of the form 

$$
\pmb {\omega} = \dot {\phi} \tilde {\mathbf {e}} _ {3} + \dot {\theta} \mathbf {e} _ {1} ^ {\prime} + \dot {\psi} \mathbf {e} _ {3}.\tag{9.84}
$$

We just need to write each of these vectors in the same basis. We'll choose to write everything in the body frame basis $\{\mathbf{e}_i\}$ . We can write the first two vectors above as 

$$
\begin{array}{l} \tilde {\mathbf {e}} _ {3} = \sin \theta \sin \psi \mathbf {e} _ {1} + \sin \theta \cos \psi \mathbf {e} _ {2} + \cos \theta \mathbf {e} _ {3} \\ \mathbf {e} _ {1} ^ {\prime} = \cos \psi \mathbf {e} _ {1} - \sin \psi \mathbf {e} _ {2} \end{array}\tag{9.85}
$$

from which we find the expression for the angular velocity $\omega$ in terms of Euler angles in the body frame axis 

$$
\begin{array}{r} \pmb {\omega} = [ \dot {\phi} \sin \theta \sin \psi + \dot {\theta} \cos \psi ] \mathbf {e} _ {1} + [ \dot {\phi} \sin \theta \cos \psi - \dot {\theta} \sin \psi ] \mathbf {e} _ {2} \\ + [ \dot {\psi} + \dot {\phi} \cos \theta ] \mathbf {e} _ {3}. \end{array}
$$

By playing a similar game, we can also express $\omega$ in the space frame axis. 

## 9.5.2 The Free Symmetric Top Revisited

To get some intuition for Euler angles, we can return to the free symmetric top that we looked at in Section 9.4.1. There we studied the angular velocity components in the body frame and found that $\omega_{3}$ is constant, while, as shown in (9.65), $\omega_{1}$ and $\omega_{2}$ precess as 

$$
(\omega_ {1}, \omega_ {2}) = \omega_ {0} (\sin \Omega t, \cos \Omega t) \quad \mathrm{with} \quad \Omega = \omega_ {3} \frac {(I _ {1} - I _ {3})}{I _ {1}}.
$$

But what does this look like in the space frame? Now that we have parametrised motion in the space frame in terms of Euler angles, we can answer this question. This is simplest if we choose the angular momentum L to lie along the $\tilde{e}_{3}$ space-axis. The resulting rigid body, garlanded with its many angles, is shown in Figure 9.6. 

Fig. 9.6 Euler angles for the free symmetric top when L coincides with $\tilde{e}_{3}$ . 

Because both L and its body-frame component $L_{3} = I_{3}\omega_{3}$ are conserved, so too is the angle between them. But this angle is identified with the Euler angle $\theta$ . This means that $\dot{\theta} = 0$ . 

Next, we want to compute $\dot{\psi}$ . The simplest way to do this is to stare at Figure 9.6 and convince yourself that 

$$
\dot {\psi} = \Omega .\tag{9.88}
$$

Alternatively, you can reach the same result by comparing the expression for the angular velocity (9.86) with our result (9.87) for the precession. This holds only if $\ddot{\phi}=0$ and $\dot{\psi}=\Omega$ . Next, we can get an expression for $\dot{\phi}$ by using the component of the body frame angular velocity 

$$
\omega_ {3} = \dot {\psi} + \dot {\phi} \cos \theta .\tag{9.89}
$$

Substituting our expression $\Omega = \dot{\psi}$ , we find the precession frequency 

$$
\dot {\phi} = \frac {I _ {3} \omega_ {3}}{I _ {1} \cos \theta}\tag{9.90}
$$

This is the rate of the wobble as seen from the space frame. 

## An Example: The Wobbling Plate

The physicist Richard Feynman tells the following story: 

I was in the cafeteria and some guy, fooling around, throws a plate in the air. As the plate went up in the air I saw it wobble, and I noticed the red medallion of Cornell on the plate going around. It was pretty obvious to me that the medallion went around faster than the wobbling.

I had nothing to do, so I start figuring out the motion of the rotating plate. I discover that when the angle is very slight, the medallion rotates twice as fast as the wobble rate – two to one. It came out of a complicated equation!

I went on to work out equations for wobbles. Then I thought about how the electron orbits start to move in relativity. Then there's the Dirac equation in electrodynamics. And then quantum electrodynamics. And before I knew it....the whole business that I got the Nobel prize for came from that piddling around with the wobbling plate. 

## Feynman was right about quantum electrodynamics. But what about the plate?

We can easily look at this using what we've learnt. The spin of the plate is $\omega_{3}$ , while the precession, or wobble, rate $\dot{\phi}$ is given in (9.90). The relevant moments of inertia for a plate were calculated in Section 9.2 where we found that $I_{3} = 2I_{1}$ . From (9.87), we then have $\Omega = -\omega_{3}$ . We can use this to see that $\dot{\psi} = -\omega_{3}$ for this example and so, for slight angles $\theta$ , with $\cos \theta \approx 1$ , we have 

$$
\dot {\phi} \approx - 2 \dot {\psi}.\tag{9.91}
$$

This means that the wobble rate of the plate is twice as fast as the spin. It's the opposite to how Feynman remembers! 

There is another elegant and simple method you can use to see that Feynman was wrong: you can pick up a plate and throw it. It's hard to see that the wobble to spin ratio is exactly two. But, after a few goes, it becomes obvious that the plate wobbles faster than it spins. 

## 9.6 The Heavy Symmetric Top

Until now, all our rigid bodies have been free. They tumble and turn, only because of conservation of angular momentum. Now we start adding forces to the story. And the most obvious force to add is gravity. 

We'll work with a symmetric top, pinned at a point $P$ which is a distance $l$ from the centre of mass, as shown in Figure 9.7. The principal axes are $\mathbf{e}_1$ , $\mathbf{e}_2$ , and $\mathbf{e}_3$ and we have $I_1 = I_2$ . It's straightforward to write down the Lagrangian in terms of Euler angles 

$$
\begin{array}{r l} & L = \frac {1}{2} I _ {1} (\omega_ {1} ^ {2} + \omega_ {2} ^ {2}) + \frac {1}{2} I _ {3} \omega_ {3} ^ {2} - M g l \cos \theta \\ & \quad = \frac {1}{2} I _ {1} (\dot {\theta} ^ {2} + \sin^ {2} \theta \dot {\phi} ^ {2}) + \frac {1}{2} I _ {3} (\dot {\psi} + \cos \theta \dot {\phi}) ^ {2} - M g l \cos \theta . \end{array}
$$

Clearly both $\psi$ and $\phi$ are ignorable coordinates, giving us two constants of motion. The first of these is 

$$
p _ {\psi} = I _ {3} (\dot {\psi} + \cos \theta \dot {\phi}) = I _ {3} \omega_ {3}.\tag{9.93}
$$

This is the angular momentum about the symmetry axis $e_{3}$ of the top. The angular velocity $\omega_{3}$ about this axis is called the spin of the top and, as for the free symmetric top, it is a constant. The other constant of motion is 

$$
p _ {\phi} = I _ {1} \sin^ {2} \theta \dot {\phi} + I _ {3} \cos \theta (\dot {\psi} + \dot {\phi} \cos \theta).\tag{9.94}
$$

In addition to these two conjugate momenta, the total energy E is also conserved 

$$
E = T + V = \frac {1}{2} I _ {1} (\dot {\theta} ^ {2} + \dot {\phi} ^ {2} \sin^ {2} \theta) + \frac {1}{2} I _ {3} \omega_ {3} ^ {2} + M g l \cos \theta .
$$

To simplify these equations, we define the two constants 

$$
a = \frac {I _ {3} \omega_ {3}}{I _ {1}} \quad \text { and } \quad b = \frac {p _ {\phi}}{I _ {1}} .\tag{9.96}
$$

Then we can write 

$$
\dot {\phi} = \frac {b - a \cos \theta}{\sin^ {2} \theta}\tag{9.97}
$$

and 

$$
\dot {\psi} = \frac {I _ {1} a}{I _ {3}} - \frac {(b - a \cos \theta) \cos \theta}{\sin^ {2} \theta}.\tag{9.98}
$$

So if we can solve $\theta = \theta(t)$ somehow, then we can always integrate these two equations to get $\phi(t)$ and $\psi(t)$ . But first we have to figure out what $\theta$ is doing. To do this, we define the “reduced energy” $E' = E - \frac{1}{2} I_{3} \omega_{3}^{2}$ . Because both E and $\omega_{3}$ are constant, so too is $E'$ . We have 

$$
E ^ {\prime} = \frac {1}{2} I _ {1} \dot {\theta} ^ {2} + V _ {\mathrm{eff}} (\theta)\tag{9.99}
$$

where the effective potential is 

$$
V _ {\mathrm{eff}} (\theta) = \frac {I _ {1} (b - a \cos \theta) ^ {2}}{2 \sin^ {2} \theta} + M g l \cos \theta .\tag{9.100}
$$

This now looks like the kind of thing that we can understand by plotting the effective potential $V_{\mathrm{eff}}(\theta)$ . It turns out to be simpler if we define the new coordinate 

$$
u = \cos \theta .\tag{9.101}
$$

Clearly $-1 \leq u \leq 1$ . We'll also define two further constants to help put the equations in the most concise form 

$$
\alpha = \frac {2 E ^ {\prime}}{I _ {1}} \quad \text { and } \quad \beta = \frac {2 M g l}{I _ {1}} .\tag{9.102}
$$

With all these redefinitions, the equations of motion $(9.97)$ , $(9.98)$ , and $(9.99)$ can be written as 

$$
\dot {u} ^ {2} = (1 - u ^ {2}) (\alpha - \beta u) - (b - a u) ^ {2} \equiv f (u),\tag{9.103}
$$

$$
\dot {\phi} = \frac {b - a u}{1 - u ^ {2}},\tag{9.104}
$$

$$
\dot {\psi} = \frac {I _ {1} a}{I _ {3}} - \frac {u (b - a u)}{1 - u ^ {2}}.\tag{9.105}
$$

We could take the square root of equation (9.103) and integrate to reduce the problem to quadrature. The result is an elliptic integral. But, rather than doing this, there's a better way to understand the physics qualitatively. 

Fig. 9.7 The heavy top with its Euler angles 

Note that the function $f(u)$ defined in $(9.103)$ is a cubic polynomial that behaves as 

$$
f (u) \to \left\{ \begin{array}{l l} + \infty & \text { as } u \to + \infty \\ - \infty & \text { as } u \to - \infty \end{array} \right.
$$

and $f(\pm1) = -(b \mp a)^{2} \leq 0$ . This means that if we plot the function $f(u)$ then it looks like Figure 9.8. 

Fig. 9.8 The cubic $f(u)$ , defined in (9.103) 

The physical range is $\dot{u}^{2}=f(u)>0$ and $-1\leq u\leq1$ so we find that, like in the spherical pendulum and central force problem, the system is confined to lie between the two roots of $f(u)$ . 

There are three possibilities for the motion, depending on the sign of $\dot{\phi}$ at the two roots $u = u_{1}$ and $u = u_{2}$ , as determined by (9.104). These are: 

- $\dot{\phi} > 0$ at both $u = u_{1}$ and $u = u_{2}$ ; 

- $\dot{\phi} > 0$ at $u = u_{1}$ , but $\dot{\phi} < 0$ at $u = u_{2}$ ; 

- $\dot{\phi} > 0$ at $u = u_{1}$ and $\dot{\phi} = 0$ at $u = u_{2}$ . 

The different paths of the heavy top, corresponding to these three possibilities, are shown in Figure 9.9. Motion in $\phi$ is called precession while motion in $\theta$ is known as nutation. 

Fig. 9.9 The three different types of motion depend on the direction of precession $\dot{\phi}$ when $\theta$ reaches its maximum and minimum values. 

## Letting the Top Go

The last of these three motions, with the cuspy trajectory, is not as unlikely as it may first appear. Suppose we spin the top and let it go at some angle $\theta$ . What happens? We have the initial conditions 

$$
\dot {\theta} (t) = 0 \quad \Longrightarrow \quad f (u (0)) = 0 \quad \Longrightarrow \quad u (0) = u _ {2}
$$

$$
\text { and } \dot {\phi} (0) = 0 \Rightarrow b - a u (0) = 0 \Rightarrow u (0) = \frac {b}{a}.
$$

Remember also that the quantity 

$$
p _ {\phi} = I _ {1} \dot {\phi} \sin^ {2} \theta + I _ {3} \omega_ {3} \cos \theta = I _ {3} \omega_ {3} \cos \theta_ {t = 0}\tag{9.107}
$$

is a constant of motion. We now have enough information to figure out the qualitative motion of the top. First it starts to fall under the influence of gravity, so $\theta$ increases. But as the top falls, $\dot{\phi}$ must turn and increase in order to keep $p_{\phi}$ constant. Moreover, we also see that the direction of the precession $\dot{\phi}$ must be in the same direction as the spin $\omega_{3}$ itself. What we get is motion of the third kind. 

## 9.6.1 Uniform Precession

Can we make the top precess without bobbing up and down? This would require $\dot{\theta}=0$ and $\dot{\phi}$ constant. For this to happen, we would need $\dot{u}=0$ and $\ddot{u}=0$ . This happens if the function $f(u)$ has a single root $u_{0}$ lying in the physical range $-1\leq u_{0}\leq+1$ , as shown in Figure 9.10. This root must satisfy 

$$
f (u _ {0}) = (1 - u _ {0} ^ {2}) (\alpha - \beta u _ {0}) - (b - a u _ {0}) ^ {2} = 0
$$

and 

$$
f ^ {\prime} (u _ {0}) = - 2 u _ {0} (\alpha - \beta u _ {0}) - \beta (1 - u _ {0} ^ {2}) + 2 a (b - a u _ {0}) = 0.
$$

Combining these, we find $\frac{1}{2}\beta = a\dot{\phi} - \dot{\phi}^{2}u_{0}$ . Substituting the definitions $I_{1}a = I_{3}\omega_{3}$ and $\beta = 2Mgl/I_{1}$ into this expression, we find 

$$
M g l = \dot {\phi} (I _ {3} \omega_ {3} - I _ {1} \dot {\phi} \cos \theta_ {0}).\tag{9.109}
$$

The interpretation of this equation is as follows: for a fixed value of $\omega_{3}$ (the spin of the top) and $\theta_{0}$ (the angle at which you let it go), we need to give exactly the right push $\dot{\phi}$ to make the top spin without bobbing. In fact, since equation (9.109) is quadratic in $\dot{\phi}$ , there are two frequencies with which the top can precess without bobbing. 

Fig. 9.10 For uniform precession, the function $f(u)$ has just a single root $u_{0}$ . 

These “slow” and “fast” precessions only exist if equation $(9.109)$ has any solutions at all. Since it is quadratic, this is not guaranteed, but requires 

$$
\omega_ {3} > \frac {2}{I _ {3}} \sqrt {M g l I _ {1} \cos \theta_ {0}}.\tag{9.110}
$$

So we see that, for a given $\theta_{0}$ , the top has to be spinning fast enough in order to have uniform solutions. What happens if it's not spinning fast enough? Well, the top falls over! 

## 9.6.2 The Sleeping Top

Suppose we start the top spinning in an upright position, with 

$$
\theta = \dot {\theta} = 0.\tag{9.111}
$$

When it spins upright, it is called a sleeping top. The question we want to answer is: Will it stay there? Or will it fall over? From (9.103), we see that the function $f(u)$ must have a root at $\theta = 0$ , or u = +1, so that $f(1) = 0$ . From the definitions (9.96) and (9.102), we can check that a = b and $\alpha = \beta$ in this situation and $f(u)$ actually has a double zero at u = +1, 

$$
f (u) = (1 - u) ^ {2} (\alpha (1 + u) - a ^ {2}).\tag{9.112}
$$

The other root of $f(u)$ is at $u_{2} = a^{2}/\alpha - 1$ . There are two possibilities: 

- The first possibility is when $u_2 > 1$ or, equivalently, $\omega_3^2 > 4I_1Mgl / I_3^2$ . In this case, the graph of $f(u)$ is plotted on the left of Figure 9.11. This motion is stable: if we perturb the initial conditions slightly, we will perturb the function $f(u)$ slightly, but the physical condition that we must restrict to the regime $f(u) > 0$ means that the motion will continue to be trapped near $u = 1$ . 

- The second possibility is when $u_{2} < 1$ , or $\omega_{3}^{2} < 4I_{1}Mgl / I_{3}^{2}$ . In this case, the function $f(u)$ looks like the plot on the right of Figure 9.11. Now the top is unstable: slight changes in the initial condition allow a large excursion. 

Fig. 9.11 The function $f(u)$ for the stable sleeping top (on the left) and the unstable sleeping top (on the right). 

In practice, the top spins upright until it is slowed by friction to $I_{3}\omega_{3}=2\sqrt{I_{1}Mgl}$ , at which point it starts to fall and precess. 

## 9.6.3 The Precession of the Equinox

The Earth spins at an angle of $\theta = 23.5^{\circ}$ to the plane of its orbit around the Sun, known as the plane of the ecliptic. The spin of the Earth is familiar: it is $\dot{\psi} = 2\pi \times (\text{day})^{-1}$ . This spin causes the Earth to bulge at the equator so it is no longer a sphere, but rather a symmetric top. This, in turn, allows both the Sun and Moon to exert a torque on the Earth which produces a precession $\dot{\phi}$ . Physically this means that the direction in which the North Pole points traces a circle in the sky and what we currently call the “pole star” will no longer be in several thousand years time. It turns out that this precession is “retrograde” i.e. opposite to the direction of the spin. The relevant angles are shown in Figure 9.12. 

Fig. 9.12 The precession of the Earth. (Not to scale.) 

One can calculate the precession $\dot{\phi}$ of the Earth due to the Moon and Sun using the techniques described in this chapter. We won't. Instead, we will use a more novel technique to calculate the precession of the Earth: astrology. After all, it's got to be good for something. 

To compute the precession of the Earth, the first fact we need to know is that Jesus was born in the age of Pisces. This doesn't mean that Jesus looked up Pisces in his daily horoscope (while scholars are divided over the exact date of his birth, he seems to exhibit many traits of a typical Capricorn) but rather refers to the patch of the sky in which the Sun appears during the first day of spring. Known in astronomical terms as the “vernal equinox”, this day of the year is defined by the property that the Sun sits directly above the Equator at midday. As the Earth precesses, this event takes place at a slightly different point in its orbit each year, with a slightly different backdrop of stars as a result. The astrological age is defined to be the background constellation in which the Sun rises during vernal equinox. 

It is easy to remember that Jesus was born in the age of Pisces because the fish was used as an early symbol for Christianity. The next fact that we need to know is that we're currently entering the age of Aquarius (which will be familiar to anyone who has sang along to the musical Hair). So we managed to travel backwards one house of the zodiac in 2000 years. We've got to make it around 12 in total, giving us a precession time of $2000 \times 12 = 24,000$ years. The actual value of the precession is 25,700 years. Our calculation is pretty close considering the method! 

The Earth also undergoes other motion. The value of $\theta$ varies from $22.1^{\circ}$ to $24.5^{\circ}$ over a period of 41,000 years, mostly due to the effects of the other planets. These also affect the eccentricity of the orbit over a period of 105,000 years. 

## 9.7 The Motion of Deformable Bodies

Take a lively cat. (Not one that's half dead like Schrödinger's). Hold it upside down and drop it. The cat will twist its body and land sprightly on its feet. Yet it doesn't do this by pushing against anything and its angular momentum is zero throughout. If the cat were rigid, such motion would be impossible since a change in orientation for a rigid body necessarily requires non-vanishing angular momentum. But the cat isn't rigid and, indeed, it can be checked that dead cats are unable to perform this feat. Bodies that can deform are able to reorient themselves without violating the conservation of angular momentum. 

In this section we'll describe some of the beautiful mathematics that lies behind this. I should warn you that this material is somewhat more advanced than the motion of rigid bodies. The theory described below was first developed in the late 1980s in order to understand how micro-organisms swim. 

## 9.7.1 Kinematics

We first need to describe the configuration space C of a deformable body. We factor out translations by insisting that all bodies have the same centre of mass. Then the configuration space C is the space of all shapes with some orientation. 

Rotations act naturally on the space C: they simply rotate each shape. This allows us to define the smaller shape space $\tilde{C}$ so that any two configurations in C which are related by a rotation are identified in $\tilde{C}$ . In other words, any two objects that have the same shape, but different orientation, are described by different points in C, but the same point in $\tilde{C}$ . Mathematically, we say $\tilde{\mathcal{C}} \cong \mathcal{C}/SO(3)$ . 

We can describe this in more detail for a body consisting of $N$ point masses, each with position $\mathbf{x}_a$ . Unlike in Section 9.1, we do not require that the distances between particles are fixed, i.e. $|\mathbf{x}_a - \mathbf{x}_b| \neq$ constant. However, there may still be some restrictions on the $\mathbf{x}_a$ . The configuration space $\mathcal{C}$ is the space of all possible configurations described by $\mathbf{x}_a$ with $a = 1, \ldots, N$ . For each different shape in $\mathcal{C}$ , we pick a representative $\tilde{\mathbf{x}}_a$ with some, fixed orientation. It doesn't matter what representative we choose, just as long as we pick one. These variables $\tilde{\mathbf{x}}_a$ are coordinates on the space shape $\tilde{\mathcal{C}}$ . For each $\mathbf{x}_a \in \mathcal{C}$ , we can always find a rotation matrix $R \in SO(3)$ such that 

$$
\mathbf {x} _ {a} = R \tilde {\mathbf {x}} _ {a}.\tag{9.113}
$$

We can play the same game if we have a continuous body, instead of one made up of discrete masses. In this case, the configuration space C and the shape space $\tilde{C}$ may be infinite-dimensional. Examples of different shapes for a continuously deformable body are shown in Figure 9.13. 

Fig. 9.13 Three possible shapes of a deformable object. 

We want to understand how an object rotates as it changes shape, keeping its angular momentum fixed (for example, keeping $\mathbf{L} = 0$ throughout). The first thing to note is that we can't really talk about the rotation between objects of different shapes. How would you say that the third object in Figure 9.13 is rotated with respect to the first or the second? Instead, we should think of an object moving through a sequence of shapes before returning to its initial shape. We can then ask if there's been a net rotation. As the object moves through its sequence of shapes, the motion is described by a time dependent $\tilde{\mathbf{x}}_a(t)$ , while the corresponding change through the configuration space is 

$$
\mathbf {x} _ {a} (t) = R (t) \tilde {\mathbf {x}} _ {a} (t)\tag{9.114}
$$

where the $3 \times 3$ rotation matrix $R(t)$ describes the necessary rotation to go from our fixed orientation of the shape $\tilde{x}_{a}$ to the true orientation. As in Section 9.1, we can define the $3 \times 3$ anti-symmetric matrix that describes the instantaneous angular velocity of the object. In fact, it will for once prove more useful to work with the “convective angular velocity” matrix defined in (9.15) 

$$
\tilde {\Omega} = R ^ {- 1} \frac {d R}{d t}.\tag{9.115}
$$

This angular velocity is non-zero due to the changing shape of the object, rather than the rigid rotation that we saw before. Let's do a quick change of notation and write coordinates on the shape space $\tilde{C}$ as $x^{A}$ , with $A = 1, \ldots, 3N$ , instead of in vector notation $\tilde{x}_{a}$ , with $a = 1, \ldots, N$ . Then, since $\Omega$ is linear in time derivatives, we can write 

$$
\tilde {\Omega} = \Omega_ {A} (x) \dot {x} ^ {A}.\tag{9.116}
$$

The component $\Omega_{A}(x)$ is the $3 \times 3$ angular velocity matrix induced if the shape changes from $x^{A}$ to $x^{A} + \delta x^{A}$ . It is independent of time: all the time dependence sits in the $\dot{x}^{A}$ factor which tells us how the shape is changing. The upshot is that for each shape $x \in \tilde{C}$ , we have a $3 \times 3$ antisymmetric matrix $\Omega_{A}$ associated to each of the $A = 1, \ldots, 3N$ directions in which the shape can change. 

However, there is an ambiguity in defining the angular velocity $\Omega$ . This comes about because of our arbitrary choice of reference orientation when we picked a representative $\tilde{x}_{a} \in \tilde{C}$ for each shape. We could quite easily have picked a different orientation, 

$$
\tilde {\mathbf {x}} _ {a} \rightarrow S (x ^ {A}) \tilde {\mathbf {x}} _ {a}\tag{9.117}
$$

where $S(x^{A})$ is a rotation that, as the notation suggests, can vary for each shape $x^{A}$ . If we pick this new set of representative orientations, then the rotation matrix R defined in (9.114) changes: $R(t) \to R(t) S^{-1}(x^{A})$ . Equation (9.115) then tells us that the angular velocity also change as 

$$
\Omega_ {A} \rightarrow S \Omega_ {A} S ^ {- 1} + S \frac {\partial S ^ {- 1}}{\partial x ^ {A}}.\tag{9.118}
$$

This ambiguity is related to the fact that we can't define the meaning of rotation between two different shapes. Nonetheless, we will see shortly that when we come to compute the net rotation of the same shape, this ambiguity will disappear, as it must. 

Objects such as $\Omega_A$ which suffer an ambiguity of form (9.118) are extremely important in modern physics and geometry. They are known as non-abelian gauge potentials to physicists, or as connections to mathematicians. In fact, we've already met something like this before: the ambiguity (9.118) is closely related to the gauge transformation (7.166) in electromagnetism. We will learn more about this in the books on Electromagnetism and on Quantum Field Theory. 

## 9.7.2 Dynamics

So far we've learnt how to describe the angular velocity $\tilde{\Omega}$ of a deformable object. The next step is to see how to calculate $\tilde{\Omega}$ . We'll now show that, up to the ambiguity described in (7.166), the angular velocity $\tilde{\Omega}$ is specified by the requirement that the angular momentum $\mathbf{L}$ of the object is zero. 

$$
\begin{array}{l} \mathbf {L} = \sum_ {a} m _ {a} \mathbf {x} _ {a} \times \dot {\mathbf {x}} _ {a} \\ = \sum_ {a} m _ {a} \left[ (R \tilde {\mathbf {x}} _ {a}) \times (R \dot {\tilde {\mathbf {x}}} _ {a}) + (R \tilde {\mathbf {x}} _ {a}) \times (\dot {R} \tilde {\mathbf {x}} _ {a}) \right] = 0. \end{array}
$$

In components this reads 

$$
L _ {i} = \epsilon_ {i j k} \sum_ {a} m _ {a} \left[ R _ {j l} R _ {k m} (\tilde {\mathbf {x}} _ {a}) _ {l} (\dot {\tilde {\mathbf {x}}} _ {a}) _ {m} + R _ {j l} \dot {R} _ {k m} (\tilde {\mathbf {x}} _ {a}) _ {l} (\tilde {\mathbf {x}} _ {a}) _ {m} \right] = 0
$$

The vanishing L = 0 is enough information to determine the following result: 

Claim: The $3 \times 3$ angular velocity matrix $\tilde{\Omega}_{ij} = R_{ik}^{-1} \dot{R}_{kj}$ is given by 

$$
\tilde {\Omega} _ {i j} = \epsilon_ {i j k} \tilde {I} _ {k l} ^ {- 1} \tilde {L} _ {l}\tag{9.121}
$$

where $\tilde{I}$ is the instantaneous inertia tensor of the shape described by $\tilde{x}_{a}$ , 

$$
\tilde {I} _ {i j} = \sum_ {a} m _ {a} ((\tilde {\mathbf {x}} _ {a} \cdot \tilde {\mathbf {x}} _ {a}) \delta_ {i j} - (\tilde {\mathbf {x}} _ {a}) _ {i} (\tilde {\mathbf {x}} _ {a}) _ {j})\tag{9.122}
$$

and $\tilde{L}_{i}$ is the apparent angular momentum 

$$
\tilde {L} _ {i} = \epsilon_ {i j k} \sum_ {a} m _ {a} (\tilde {\mathbf {x}} _ {a}) _ {j} (\dot {\tilde {\mathbf {x}}} _ {a}) _ {k}.\tag{9.123}
$$

Proof: We start by multiplying $L_{i}$ by $\epsilon_{inq}$ . We need to use the fact that if we multiply two $\epsilon$ -symbols, we have 

$\epsilon_{ijk}\epsilon_{inq} = (\delta_{jn}\delta_{kq} - \delta_{jq}\delta_{kn})$ . Then 

$$
\begin{array}{r} \epsilon_ {i n q} L _ {i} = \sum_ {a} m _ {a} \left[ R _ {n l} R _ {q m} (\tilde {\mathbf {x}} _ {a}) _ {l} (\dot {\tilde {\mathbf {x}}} _ {a}) _ {m} - R _ {q l} R _ {n m} (\tilde {\mathbf {x}} _ {a}) _ {l} (\dot {\tilde {\mathbf {x}}} _ {a}) _ {m} \right. \\ \left. - R _ {q l} \dot {R} _ {n m} (\tilde {\mathbf {x}} _ {a}) _ {l} (\tilde {\mathbf {x}} _ {a}) _ {m} + R _ {n l} \dot {R} _ {q m} (\tilde {\mathbf {x}} _ {a}) _ {l} (\tilde {\mathbf {x}} _ {a}) \right. \end{array}
$$

Now multiply by $R_{nj}R_{qk}$ . Since R is orthogonal, we know that $R_{nj}R_{nl} = \delta_{jl}$ which, after contracting a bunch of indices, gives us 

$$
\begin{array}{r l r} & & {R _ {n j} R _ {q k} \epsilon_ {i n q} L _ {i} = \sum_ {a} m _ {a} \left[ (\tilde {\mathbf {x}} _ {a}) _ {j} (\dot {\tilde {\mathbf {x}}} _ {a}) _ {k} - (\tilde {\mathbf {x}} _ {a}) _ {k} (\dot {\tilde {\mathbf {x}}} _ {a}) _ {j} \right.} \\ & & {- \left. \tilde {\Omega} _ {j l} (\tilde {\mathbf {x}} _ {a}) _ {k} (\tilde {\mathbf {x}} _ {a}) _ {l} + \tilde {\Omega} _ {k l} (\tilde {\mathbf {x}} _ {a}) _ {j} (\tilde {\mathbf {x}} _ {a}) \right.} \\ & & {= 0 .} \end{array}
$$

This is almost in the form that we want, but the indices aren't quite contracted in the right manner to reproduce (9.121). One can try to play around to get the indices working right, but at this stage it's just as easy to expand out the components explicitly. For example, we can look at 

$$
\begin{array}{r l} & {\tilde {L} _ {1} = \sum_ {a} m _ {a} \left[ (\tilde {\mathbf {x}} _ {a}) _ {2} (\dot {\tilde {\mathbf {x}}} _ {a}) _ {3} - ((\tilde {\mathbf {x}} _ {a}) _ {3} (\dot {\tilde {\mathbf {x}}} _ {a}) _ {2} \right]} \\ & {\quad = \sum_ {a} m _ {a} \left[ \tilde {\Omega} _ {2 1} (\tilde {\mathbf {x}} _ {a}) _ {3} (\tilde {\mathbf {x}} _ {a}) _ {1} + \tilde {\Omega} _ {2 3} (\tilde {\mathbf {x}} _ {a}) _ {3} (\tilde {\mathbf {x}} _ {a}) _ {3} \right.} \\ & {\qquad \left. - \tilde {\Omega} _ {3 1} (\tilde {\mathbf {x}} _ {a}) _ {2} (\tilde {\mathbf {x}} _ {a}) _ {1} - \tilde {\Omega} _ {3 2} (\tilde {\mathbf {x}} _ {a}) _ {2} (\tilde {\mathbf {x}} _ {a}) _ {2} \right]} \\ & {\quad = \tilde {I} _ {1 1} \tilde {\Omega} _ {2 3} + \tilde {I} _ {1 2} \tilde {\Omega} _ {3 1} + \tilde {I} _ {1 3} \tilde {\Omega} _ {1 2} = \frac {1}{2} \epsilon_ {i j k} \tilde {I} _ {1 i} \tilde {\Omega} _ {j k}} \end{array}
$$

where the first equality is the definition of $\tilde{L}_{1}$ , while the second equality uses our result above, and the third equality uses the definition of $\tilde{I}$ given in (9.122). There are two similar equations, which are summarised in the formula 

$$
\tilde {L} _ {i} = \frac {1}{2} \epsilon_ {j k l} \tilde {I} _ {i j} \tilde {\Omega} _ {k l}.\tag{9.127}
$$

Multiplying both sides by $\tilde{I}^{-1}$ gives us precisely the claimed result (9.121). This concludes the proof. 

To summarise: a system with no angular momentum that can twist and turn and change its shape has an angular velocity (9.121) where $\tilde{\mathbf{x}}_{a}(t)$ is the path it chooses to take through the space of shapes. This is a nice formula. But what do we do with it? We want to compute the net rotation R as the body moves through a sequence of shapes and returns to its starting point at a time $T_{final}$ later. This is given by solving (9.115) for R. The way to do this was described in Section 9.1. We use time-ordered exponentials 

$$
R = \tilde {T} \exp \left(\int_ {0} ^ {T _ {\text { final }}} \tilde {\Omega} (t) d t\right) = \tilde {T} \exp \left(\oint \Omega_ {A} d x ^ {A}\right).
$$

The path-ordering symbol $\tilde{T}$ puts all matrices evaluated at later times to the right. (This differs from the ordering in Section 9.1 where we put later matrices to the left. The difference arises because we're working with the convective angular velocity $\tilde{\Omega} = R^{-1}\dot{R}$ instead of the angular velocity $\Omega = \dot{R}R^{-1}$ .) In the second equality above, we've written the exponent as an integral around a closed path in shape space. Here time has dropped out. This tells us an important fact: it doesn't matter how quickly we perform the change of shapes, the net rotation of the object will be the same. 

In particle physics language, the integral in $(9.128)$ is called a Wilson loop. We can see how the rotation fares under the ambiguity $(9.116)$ . After some algebra, you can find that the net rotation R of an object with shape $x^{A}$ is changed by 

$$
R \to S (x ^ {A}) R S (x ^ {A}) ^ {- 1}.\tag{9.129}
$$

This is as it should be: the $S^{-1}$ takes the shape back to our initial choice of standard orientation; the matrix R is the rotation due to the change in shape; finally S puts us back to the new, standard orientation. So we see that even though the definition of the angular velocity is plagued with ambiguity, when we come to ask physically meaningful questions, such as how much has a shape rotated, the ambiguity disappears. However, if we ask non-sensical questions, such as the rotation between two different shapes, then the ambiguity looms large. In this manner, the theory contains a rather astonishing new ingredient: it lets us know what are the sensible questions to ask! Quantities for which the ambiguity (9.116) vanishes are called gauge invariant. 

In general, it's quite hard to explicitly compute the integral (9.128). One case where it is possible is for infinitesimal changes of shape. Suppose we start with a particular shape $x_A^0$ , and move infinitesimally in a loop in shape space: 

$$
x _ {A} (t) = x _ {A} ^ {0} + \alpha_ {A} (t).\tag{9.130}
$$

Then we can Taylor expand our angular velocity components, 

$$
\Omega_ {A} (x (t)) = \Omega_ {A} (x ^ {0}) + \left. \frac {\partial \Omega_ {A}}{\partial x ^ {B}} \right| _ {x ^ {0}} \alpha_ {B}.\tag{9.131}
$$

Expanding out the rotation matrix $(9.128)$ and taking care with the ordering, one can show that 

$$
\begin{array}{l} R = 1 + \frac {1}{2} F _ {A B} \oint \alpha_ {A} \dot {\alpha} _ {B} d t + \mathcal {O} (\alpha^ {3}) \\ = 1 + \frac {1}{2} \int F _ {A B} d A _ {A B} + \mathcal {O} (\alpha^ {3}) \end{array}\tag{9.132}
$$

where $F_{AB}$ is anti-symmetric in the shape space indices A and B, and is a $3 \times 3$ matrix (the i, j = 1, 2, 3 indices have been suppressed) given by 

$$
F _ {A B} = \frac {\partial \Omega_ {A}}{\partial x ^ {B}} - \frac {\partial \Omega_ {B}}{\partial x ^ {A}} + [ \Omega_ {A}, \Omega_ {B} ].\tag{9.133}
$$

It is known as the field strength to physicists (or the curvature to mathematicians). It is evaluated on the initial shape $x_{A}^{0}$ . The second equality in $(9.132)$ gives the infinitesimal rotation as the integral of the field strength over the area traversed in shape space. This field strength contains all the information one needs to know about the infinitesimal rotations of objects induced by changing their shape. 

One of the nicest things about the formalism described above is that it mirrors very closely the mathematics needed to describe the fundamental laws of nature, such as the strong and weak nuclear forces. They are all 

described by “non-abelian gauge theories”, with an object known as the gauge potential (analogous to $\Omega_{A}$ ) and an associated field strength. 

## 10 The Hamiltonian Formalism

Throughout this book, we have promised two reformulations of classical mechanics. The first was the Lagrangian formalism described in Chapter 7. The purpose of this chapter is to present the second of these, due to Hamilton and dating to around 1830. 

We're not going to use the Hamiltonian formulation to solve increasingly complicated problems in classical mechanics. That's not really its purpose. Instead our goal is to better understand the mathematical structure that underlies classical mechanics. This will certainly help us gain a better intuition for the kinds of behaviour that can occur in classical mechanics. We'll be able to prove some general theorems, and also look at novel classical systems that we might not have considered if we were stuck in a Newtonian mindset. But, in some sense, the real pay-off of this chapter will come only when we turn to quantum mechanics in a subsequent book. We will see that all the main equations of quantum mechanics have a classical counterpart. And the counterpart lies in the Hamiltonian framework. 

## 10.1 Hamilton's Equations

The Lagrangian formulation of classical mechanics starts with a function, the eponymous the Lagrangian $L(q^i, \dot{q}^i, t)$ . As the notation shows, this function depends on $n$ generalised coordinates, $q^i$ , with $i = 1, \ldots, n$ , their time derivatives $\dot{q}^i$ and, possibly, time. The Euler-Lagrange equations are 

$$
\frac {d}{d t} \left(\frac {\partial L}{\partial \dot {q} ^ {i}}\right) - \frac {\partial L}{\partial q ^ {i}} = 0.\tag{10.1}
$$

These are n second order differential equations. Crucially, if we wish to find a solution, then we have to give 2n initial conditions, say $q^{i}$ and $\dot{q}^{i}$ at time t = 0. 

Roughly speaking, the basic idea of Hamilton's approach is to try and place positions and velocities on a more symmetric footing. The “rough speaking” here is because it turns out that it’s not quite the velocities that we should consider: instead it is the generalised, or canonical, momenta that we introduced in Section 7.3 

$$
p _ {i} = \frac {\partial L}{\partial \dot {q} ^ {i}}.\tag{10.2}
$$

In terms of the generalised momenta, the Euler–Lagrange equations (10.1) take the particularly simple form 

$$
\dot {p} _ {i} = \frac {\partial L}{\partial q ^ {i}}.\tag{10.3}
$$

We should think of these generalised momenta as functions $p_{i}(q^{j},\dot{q}^{j},t)$ . In many familiar situations the Lagrangian is quadratic in velocities (because the kinetic energy is $\frac{1}{2}mv^{2}$ ) in which case the momenta will be linearly related to the velocities. But this need not be the case, and we'll see examples in this section where p and $\dot{q}$ have a different relationship. 

Now we can state more precisely the key idea of the Hamiltonian formalism: it is to put coordinates $q^{i}$ and momenta $p^{i}$ on a more symmetric footing. 

## Phase Space

First, a definition. Recall that the generalised coordinates $q^{i}$ parameterise the configuration space C of the system. Time evolution can be viewed as a path in in C. However, if we know the that the system sits at a point in C at some particular time $t_{0}$ , that's not enough information to determine where the system is at some later time. This is because we also need the initial velocity: we need $\dot{q}^{i}$ at time $t_{0}$ as well. Only then is the full evolution of the system uniquely determined. 

As we mentioned above, throughout this section we will replace the velocities $\dot{q}^{i}$ with the momenta $p_{i}$ . So, alternatively, we could say that the future evolution of the system is uniquely determined by specifying the pair $(q^{i}, p_{i})$ at some moment in time. This pair $(q^{i}, p_{i})$ defines the state of the system. The space of all states comprise the 2n-dimensional phase 

space, M, parameterised by $(q^{i}, p_{i})$ . A cartoon of this is shown in Figure 10.1. 

Fig. 10.1 Motion in the n-dimensional configuration space on the left, and in the 2n-dimensional phase space on the right. 

If you sit at a point in phase space at some time then your future (and, indeed past) evolution is uniquely determined. This means, among other things, that paths in phase space can never cross. We say that evolution is governed by a flow in phase space. Another way of saying this is that the phase space is the “solution space” of the system. Each point in phase space corresponds to a different solution. 

## An Example: The Pendulum

Here's a simple example. The pendulum has a configuration space $\mathcal{C} = \mathbf{S}^1$ , parameterised by an angle $\theta \in [-\pi, \pi)$ . The phase space is then the cylinder $\mathcal{M} = \mathbb{R} \times \mathbf{S}^1$ , with the $\mathbb{R}$ factor corresponding to the momentum $p_\theta$ . We've drawn this in Figure 10.2 by flattening out the cylinder, so that the left-hand edge at $\theta = -\pi$ and the right-hand edge at $\theta = \pi$ are identified. The phase space flows are also shown. 

Fig. 10.2 Flows in the phase space of a pendulum. 

Two different types of motion are clearly visible in the flows. For small momentum, the pendulum oscillates back and forth, motion which appears as a squashed circle in phase space. But for large momentum, the pendulum swings all the way around and so the lines in phase space wrap around the $S^{1}$ . Separating these two different motions is the special case where the pendulum starts upright, falls, and just makes it back to the upright position. This curve in phase space is called the separatrix. 

## 10.1.1 The Hamiltonian

We've seen that dynamical evolution is given by a flow on phase space. Our next goal is to write down equations that describe this flow. We do this by constructing the Hamiltonian. This is a function $H(q, p)$ , on phase space. (When we write $H(q, p)$ , with no indices on $q$ and $p$ , we mean that it depends on all coordinates $q^i$ and $p_i$ with $i = 1, \ldots, n$ .) The Hamiltonian is defined in terms of the Lagrangian by 

$$
H (q, p, t) = p _ {i} \dot {q} ^ {i} - L (q, \dot {q}, t).\tag{10.4}
$$

We've met something very similar to the Hamiltonian function before: we saw in (7.121) that, if $\partial L / \partial t = 0$ , then the function $H(q,p)$ is identified as the conserved energy. This connection also manifests itself in quantum mechanics where the Hamiltonian is identified as the energy operator. 

However, there's more to the Hamiltonian than just the energy. In what follows, it's crucial that we think of the Hamiltonian as a function on phase space. This means that $H$ is a function of $q^i$ and $p_i$ . This is in contrast to the 

Lagrangian which is a function of $q^i$ and $\dot{q}^i$ . 

In practice, this means that, given a Lagrangian, you first compute the momentum 

$$
p _ {i} = \frac {\partial L}{\partial \dot {q} ^ {i}}\tag{10.5}
$$

and then compute the right-hand side of $(10.4)$ . Often the resulting expression will be given as a function of $q^{i}$ and $\dot{q}^{i}$ . The last step is to then invert $\dot{q}^{i} = \dot{q}^{i}(q, p, t)$ , so that the Hamiltonian takes the desired form $H(q, p, t)$ as a function over phase space. 

The difference between thinking of $H(q, p, t)$ as a function of momentum vs velocities may seem like a pedantic one. But it's a difference on which the whole Hamiltonian formalism hangs. We'll see this in some examples as we move forwards. But, mathematically, the reason is that the Hamiltonian is a Legendre transform of the Lagrangian. We now take a small detour to explain what this means. 

## An Aside: The Legendre Transform

The Legendre transform arises in a number of places in physics. In classical mechanics it relates the Lagrangian and Hamiltonian. But we will also see the same transformation in the book on Statistical Physics where it relates different thermodynamic functions of state, like energy and free energy. Here we give a brief account of the mathematics behind the Legendre transform. 

First, consider an arbitrary function $f(x,y)$ . Here the variable y will just go along for the ride. (It will be like the coordinates q in the Lagrangian.) Meanwhile, we're going to do the transform with respect to the variable x (which is like the $\dot{q}$ in the Lagrangian). 

The total derivative of $f$ is 

$$
d f = \frac {\partial f}{\partial x} d x + \frac {\partial f}{\partial y} d y.\tag{10.6}
$$

Next, define the related function 

$$
g (x, y, u) = u x - f (x, y).\tag{10.7}
$$

The function $g(u, x, y)$ depends on the original two variables x and y, as well as a third variable u that, for now, just appears linearly in the definition. The total derivative of g is 

$$
d g = d (u x) - d f = u d x + x d u - \frac {\partial f}{\partial x} d x - \frac {\partial f}{\partial y} d y.\tag{10.}
$$

So far, we've viewed $u$ as a new independent variable. At this point, we choose it to be a specific function of $x$ and $y$ , defined by 

$$
u (x, y) = \frac {\partial f}{\partial x}.\tag{10.9}
$$

With this choice, the term proportional to dx in $(10.8)$ vanishes. We have 

$$
d g = x d u - \frac {\partial f}{\partial y} d y.\tag{10.10}
$$

This is telling us that g can be thought of as a function of just u and y. If we want an explicit expression for $g(u,y)$ , we must first invert (10.9) to get $x = x(u,y)$ and then insert this into the definition (10.7), so that 

$$
g (u, y) = u   x (u, y) - f (x (u, y), y)  .\tag{10.11}
$$

This is the Legendre transform. It takes us from one function $f(x,y)$ to a different function $g(u,y)$ where $u = \partial f / \partial x$ . 

A crucial fact about the Legendre transformation is that (with one caveat to be explained below) it doesn't lose any information about the original function. To see this, we just need to note that we can recover the original $f(x,y)$ from $g(u,y)$ by doing a second Legendre transformation. We have 

$$
\left. \frac {\partial g}{\partial u} \right| _ {y} = x (u, y) \quad \text { and } \quad \left. \frac {\partial g}{\partial y} \right| _ {u} = - \frac {\partial f}{\partial y} .\tag{10.12}
$$

This assures us that the inverse Legendre transform $f = (\partial g / \partial u)u - g$ does indeed take us back to the original function. 

We can get more insight into the Legendre transform by thinking geometrically. The figure shows the two curves $f(x,y)$ and ux for fixed y and for fixed u. The function $g(u;x)$ , as defined in (10.7), is just the difference between these two curves. But the all-important condition 

(10.9) tells us that, if we fix u, and so fix the slope of the straight line, then function $g(u)$ is the maximum distance between these curves. You can see this geometrically because the maximum distance occurs when the tangents of the two curves are equal. Or you can see this algebraically by extremising the distance 

$$
\frac {d}{d x} \left(u x - f (x)\right) = 0 \quad \Longrightarrow \quad u = \frac {\partial f}{\partial x}.\tag{10.13}
$$

This, then, is the geometrical interpretation of the Legendre transform. As you change u, you change the slope of the line ux. The function $g(u)$ is the maximum distance between that line and the original curve $f(x)$ . 

The graphical approach also hints at the caveat that we mentioned above. This arises because there is only a unique local maximum distance between the curves when the original function $f(x)$ is convex. This is an additional requirement that we need for the Legendre transform to be single-valued and hence well-defined. In the world of classical mechanics, the basic Lagrangian $L = T - V$ is quadratic in $\dot{q}$ which is a convex function so we're safe. But we don't have to go far in the subject to find situations where $L$ is not convex. This happens, for example, for the relativistic particle that we will meet in Chapter 11. These Lagrangians typically have some other interesting feature (such as redundancies or constraints) that we have to get to grips with before we can understand the physics. 

## Hamilton's Equations

With a better understanding of the Legendre transform, we can now return to physics. We have the Hamiltonian $H(q,p,t)$ , defined in (10.4) and we know from the discussion above that this contains the same information as our original Lagrangian $L(q,\dot{q},t)$ . Let's follow the discussion of the Legendre transform and consider the total derivative of the Hamiltonian 

$$
\begin{array}{l} d H = (\dot {q} ^ {i} d p _ {i} + p _ {i} d \dot {q} ^ {i}) - \left(\frac {\partial L}{\partial q ^ {i}} d q ^ {i} + \frac {\partial L}{\partial \dot {q} ^ {i}} d \dot {q} ^ {i} + \frac {\partial L}{\partial t} d t\right) \\ = \dot {q} ^ {i} d p _ {i} - \frac {\partial L}{\partial q ^ {i}} d q ^ {i} - \frac {\partial L}{\partial t} d t. \end{array}
$$

We see that the $d\dot{q}^{i}$ terms have cancelled upon using the definition of generalised momenta $p_{i} = \partial L / \partial \dot{q}^{i}$ . This mimics the fact that the dx term vanished in (10.10) and is telling us that we can think of $H = H(q, p, t)$ . In other words, we must have 

$$
d H = \frac {\partial H}{\partial q ^ {i}} d q ^ {i} + \frac {\partial H}{\partial p _ {i}} d p _ {i} + \frac {\partial H}{\partial t} d t.\tag{10.15}
$$

Now we simply equate terms in (10.14) and (10.15). So far this is repeating the steps of the Legendre transformation. But we add a physics ingredient into the mix in the guise of the Euler–Lagrange equation (10.3) which reads $\dot{p}_{i} = \partial L / \partial q^{i}$ . The result is a collection of first order differential equations, 

$$
\dot {p} _ {i} = - \frac {\partial H}{\partial q ^ {i}} \quad \text { and } \quad \dot {q} ^ {i} = \frac {\partial H}{\partial p _ {i}} .\tag{10.16}
$$

These are Hamilton's equations. In addition, if the Lagrangian $L$ has explicit time dependence, then so too does the Hamiltonian with 

$$
- \frac {\partial L}{\partial t} = \frac {\partial H}{\partial t}.\tag{10.17}
$$

In Hamilton's equations (10.16), we have replaced $n$ second order equations of motion with $2n$ first order equations of motion. This may not seem like a great leap forward. In particular, when we come to solve these equations we will often revert back to the second order form. Nevertheless, as we promised above, Hamilton's equations are the starting point for peeling apart the structure of classical mechanics. We'll see more of this as we progress. For now, we just note that we can already see a glimpse of the symmetry between $q$ and $p$ in Hamilton's equations: both sit on a similar footing, with just a minus sign in the first equation of (10.16) to distinguish them. 

## Briefly, Conservation Laws

We saw in Section 7.5 how conservation laws arise in the Lagrangian formalism. Some of the simpler implications of Noether's theorem carry over straightforwardly to the Hamiltonian formulation. 

For example, if $\partial H/\partial t = 0$ then H itself is a constant of motion. This follows by looking at the total time derivative 

$$
\frac {d H}{d t} = \frac {\partial H}{\partial q ^ {i}} \dot {q} ^ {i} + \frac {\partial H}{\partial p _ {i}} \dot {p} _ {i} + \frac {\partial H}{\partial t} = - \dot {p} _ {i} \dot {q} ^ {i} + \dot {q} ^ {i} \dot {p} _ {i} + \frac {\partial H}{\partial t} = \frac {\partial H}{\partial t}
$$

where we've imposed the equations of motion in the second equality. In most examples, $H$ will be identified with the energy. 

Similarly, if a coordinate $q^{j}$ is ignorable, meaning that it appears only as $\dot{q}^{j}$ in the Lagrangian, then only the conjugate momentum $p_{j}$ appears in the Hamiltonian. This momentum is then conserved since 

$$
\dot {p} _ {j} = \frac {\partial H}{\partial q ^ {j}} = 0.\tag{10.19}
$$

We'll have more to say about conservation laws in the Hamiltonian formalism in Section 10.4.2. 

## 10.1.2 The Principle of Least Action

The principle of least action is a central piece of the Lagrangian formalism of classical mechanics. We define the action as a functional of all possible paths $q^{i}(t)$ in configuration space, 

$$
S [ q (t) ] = \int_ {t _ {1}} ^ {t _ {2}} L (q, \dot {q}, t) d t.\tag{10.20}
$$

The equations of motion then follow by insisting that $\delta S = 0$ for all paths with fixed end points so that $\delta q^{i}(t_{1}) = \delta q^{i}(t_{2}) = 0$ . 

There is a version of this story in the Hamiltonian formalism that goes through with only minor tweaks. This time, we define the action 

$$
S [ q (t), p (t) ] = \int_ {t _ {1}} ^ {t _ {2}} \left(p _ {i} \dot {q} ^ {i} - H\right) d t.\tag{10.21}
$$

where $\dot{q}^{i} = \partial H / \partial p_{i}$ . This looks the same as our original action (10.20) but the devil is in the details: the action now is a function of all possible paths $q^{i}(t)$ and $p_{i}(t)$ in phase space. This means that we vary $q^{i}(t)$ and $p_{i}(t)$ independently. This differs from the Lagrangian formalism where a variation of $q^{i}(t)$ automatically leads to a variation of $\dot{q}^{i}$ . But remember that the whole point of the Hamiltonian formalism is that we treat $q^{i}$ and $p_{i}$ on an equal footing. So we vary both. We have 

$$
\begin{array}{r l} & {\delta S = \int_ {t _ {1}} ^ {t _ {2}} \left\{\dot {q} ^ {i} \delta p _ {i} + p _ {i} \delta \dot {q} ^ {i} - \frac {\partial H}{\partial p _ {i}} \delta p _ {i} - \frac {\partial H}{\partial q ^ {i}} \delta q ^ {i} \right\} d t} \\ & {\quad = \int_ {t _ {1}} ^ {t _ {2}} \left\{\left[ \dot {q} ^ {i} - \frac {\partial H}{\partial p _ {i}} \right] \delta p _ {i} + \left[ - \dot {p} _ {i} - \frac {\partial H}{\partial q ^ {i}} \right] \delta q ^ {i} \right\} d t + \left[ p _ {i} \delta q ^ {i} \right] _ {t _ {1}} ^ {t _ {2}}} \end{array}
$$

where we've integrated the $p_i \delta \dot{q}_i$ term by parts. There are Hamilton's equations waiting for us in the square brackets. If we look for extrema $\delta S = 0$ for all $\delta p_i$ and $\delta q^i$ , then we get Hamilton's equations 

$$
\dot {q} ^ {i} = \frac {\partial H}{\partial p _ {i}} \quad \text { and } \quad \dot {p} _ {i} = - \frac {\partial H}{\partial q ^ {i}} .\tag{10.23}
$$

Except there's a very slight subtlety with the boundary conditions. We need the last term in (10.22) to vanish, and so require only that 

$$
\delta q ^ {i} (t _ {1}) = \delta q ^ {i} (t _ {2}) = 0\tag{10.24}
$$

while $\delta p_{i}$ can be free at the end points $t = t_{1}$ and $t = t_{2}$ . So, despite our best efforts, $q^{i}$ and $p_{i}$ are not quite symmetric in this formalism. 

## 10.1.3 A Particle in a Potential

We can illustrate the Hamiltonian formalism by looking at a particle moving in $R^{3}$ in the presence of a potential $V(\mathbf{x})$ . In this simple example, there are no surprises. (This will not continue to be the case as we look at more complicated examples.) 

The Lagrangian is 

$$
L = \frac {1}{2} m \dot {\mathbf {x}} ^ {2} - V (\mathbf {x}).\tag{10.25}
$$

The corresponding momentum takes the familiar form 

$$
\mathbf {p} = \frac {\partial L}{\partial \dot {\mathbf {x}}} = m \dot {\mathbf {x}}.\tag{10.26}
$$

The Hamiltonian is then given by 

$$
H = \mathbf {p} \cdot \dot {\mathbf {x}} - L = \frac {1}{2 m} \mathbf {p} ^ {2} + V (\mathbf {x}).\tag{10.27}
$$

In the final step, we've eliminated $\dot{x}$ in favour of p. Of course, this is trivial to do in the present example but it is important nonetheless. It means that the kinetic energy is written as $p^{2}/2m$ rather than the $m\dot{x}^{2}/2$ . 

In Volume 3 of this series, we will see that the Hamiltonian plays a starring role in quantum mechanics. There too, it should be thought of as a function of momentum, rather than velocity, albeit with the momentum variable replaced by the differential operator $p \rightarrow -i\hbar\nabla$ . 

Back in the classical world, Hamilton's equations (10.16) are 

$$
\dot {\mathbf {x}} = \frac {\partial H}{\partial \mathbf {p}} = \frac {1}{m} \mathbf {p} \quad \mathrm{and} \quad \dot {\mathbf {p}} = - \frac {\partial H}{\partial \mathbf {x}} = - \nabla V.\tag{10.28}
$$

Both of these are familiar. The first is just the definition of velocity in terms of momentum, while the second is Newton's equation of motion for this system. 

## 10.1.4 A Particle in an Electromagnetic Field

We described the Lagrangian for a particle with charge q moving in electric and magnetic fields in Section 7.6.2. One of the surprises was that we're obliged to work with the electric potential $\phi(\mathbf{x}, t)$ and the vector potential $\mathbf{A}(\mathbf{x}, t)$ , with the electric and magnetic fields given by 

$$
\mathbf {E} = - \nabla \phi - \frac {\partial \mathbf {A}}{\partial t} \quad \mathrm{and} \quad \mathbf {B} = \nabla \times \mathbf {A}.\tag{10.29}
$$

The Lagrangian is 

$$
{\cal L} = \frac {1}{2} m \dot {\bf x} ^ {2} - q \left(\phi - \dot {\bf x} \cdot {\bf A}\right) .\tag{10.30}
$$

The conjugate momentum is now given by 

$$
\mathbf {p} = \frac {\partial L}{\partial \dot {\mathbf {x}}} = m \dot {\mathbf {x}} + q \mathbf {A}.\tag{10.31}
$$

Crucially, the momentum p is not just “mass times velocity”. It now gets an extra contribution from the vector potential. Moreover, as we stressed in Section 7.6.2, the momentum p is not gauge invariant, so it’s not possible to ascribe physical meaning to the value of p! These issues notwithstanding, it’s trivial to invert the relationship above and write the velocity as 

$$
\dot {\mathbf {x}} = \frac {1}{m} (\mathbf {p} - q \mathbf {A}).\tag{10.32}
$$

We now calculate the Hamiltonian 

$$
\begin{array}{r l} & H (\mathbf {p}, \mathbf {x}) = \mathbf {p} \cdot \dot {\mathbf {x}} - L \\ & \qquad = \frac {1}{m} \mathbf {p} \cdot (\mathbf {p} - q \mathbf {A}) - \left[ \frac {1}{2 m} (\mathbf {p} - q \mathbf {A}) ^ {2} - q \phi + \frac {q}{m} (\mathbf {p} - q \mathbf {A}) \right. \\ & \qquad = \frac {1}{2 m} (\mathbf {p} - q \mathbf {A}) ^ {2} + q \phi . \end{array}
$$

There's something curious about this expression. If we were to write the Hamiltonian in terms of the velocity $\dot{\mathbf{x}}$ , then the first term is just the usual kinetic energy $m\dot{\mathbf{x}}^2 / 2$ and the Hamiltonian coincides with the energy $E = m\dot{\mathbf{x}}^2 / 2 + q\phi$ . This energy has no dependence on the vector potential $\mathbf{A}$ which is just the statement that magnetic fields do no work and so don't affect the energy. But, as we've stressed above, the Hamiltonian must be thought of as a function of $\mathbf{p}$ . And, when viewed as a function of $\mathbf{p}$ , the gauge potential $\mathbf{A}$ sneaks back in. This means that the Hamiltonian depends on $\mathbf{A}$ , and so magnetic fields can affect the equations of motion, even though the energy is independent of $\mathbf{A}$ . 

The first of Hamilton's equations reads 

$$
\dot {\mathbf {x}} = \frac {\partial H}{\partial \mathbf {p}} = \frac {1}{m} (\mathbf {p} - q \mathbf {A}).\tag{10.34}
$$

which, as usual, is a recapitulation of our earlier expression (10.32). The second of Hamilton's equations, $\dot{p} = -\partial H/\partial x$ , is best expressed in terms of components 

$$
\dot {p} _ {i} = - \frac {\partial H}{\partial x ^ {i}} = - q \frac {\partial \phi}{\partial x ^ {i}} + \frac {q}{m} (p _ {j} - e A _ {j}) \frac {\partial A _ {j}}{\partial x ^ {i}}.\tag{10.35}
$$

A little rearranging of indices shows that this coincides with the Lorentz force law (7.164). 

## 10.1.5 William Rowan Hamilton (1805–1865)

The formalism described above arose out of Hamilton's interest in the theory of optics. The ideas were published in a series of books entitled Theory of Systems of Rays, the first of which appeared while Hamilton was still an undergraduate at Trinity College, Dublin. They also contain the first application of the Hamilton-Jacobi formulation (which we will see in Section 10.7) and the first general statement of the principal of least action, which sometimes goes by the name “Hamilton’s Principle”. 

Hamilton's genius was recognised early. His capacity to soak up classical languages and to find errors in famous works of mathematics impressed many. In an unprecedented move, he was offered a full professorship in Dublin while still an undergraduate. He also held the position of Royal Astronomer of Ireland, allowing him to live at Dunsink Observatory although he rarely did any observing. Unfortunately, the later years of Hamilton's life were not happy ones. The woman he loved married another and he spent much time depressed, mired in drink, bad poetry, and quaternions. 

## 10.2 Liouville's Theorem

Now it's time to use the Hamiltonian formalism to uncover some of the features of classical dynamics. In this section we'll describe two such features, each of which follows from the description of the dynamics in terms of a flow in phase space, captured by Hamilton's equations (10.16). First, however, some motivation. 

If you were to look to classical mechanics for a philosophical lesson to take home, then there is one that stands out: the universe is deterministic. If you know the starting points and velocities of every particle in the universe, then the future is yours. All you need is a big enough computer and you can run Newton's laws of motion forward in time to correctly predict everything that will happen. Admittedly, there may be some difficulties in doing this in practice, both in gaining the knowledge about the initial conditions in the first place and in solving the resulting equations. Nonetheless, it hints at a vision of the universe in which everything is pre-destined from the time of the Big Bang. 

With the advent of quantum mechanics, it became clear that this particular philosophical lesson is not really one that you want to take home. We now know that classical mechanics is not the final answer. Instead, it is an emergent framework that arises only when you look on suitably large distance scales and ignore more subtle microscopic physics. And prominent among these microscopic quantum laws is the idea of an innate uncertainty in the universe, one that pulls the rug from the deterministic dream. 

With this in mind, it's worth returning to the framework of classical mechanics and asking: is there some way to formulate the theory in which things look a little less certain. Of course, we can't overthrow the deterministic nature of the world without introducing $\hbar$ . But we can at least inject a little humility into the situation and admit ignorance of certain things. 

The most obvious place to admit ignorance is in those initial conditions. If we know them precisely, then everything in classical mechanics is predetermined. In the Hamiltonian picture, this means that if we start our system in some particular point in phase space then it will follow a particular path as it evolves in time. But what if we admit that we don't know the state of the system exactly? In this case, it would make sense to talk about a probability distribution $\rho(q, p, t)$ on phase space, parameterising our ignorance. Because this is a probability distribution, it should be normalised, so that 

$$
\int \prod_ {i} d q ^ {i} d p _ {i} \rho (q, p, t) = 1.\tag{10.36}
$$

We could then ask how this probability distribution $\rho(q,p,t)$ evolves in time. 

There is a second, closely related, scenario that we can talk about simultaneously. We may have a system with a large number N of identical, non-interacting particles, for example $N = 10^{23}$ gas molecules in a jar. In this case, we may not care about the individual positions of every particle, only about the averaged behaviour. We can again introduce a density function $\rho(q,p,t)$ , describing how the N particles are averaged over phase space at some given time, now normalised to 

$$
\int \prod_ {i} d q ^ {i} d p _ {i} \rho (q, p, t) = N.\tag{10.37}
$$

This prompts the same question: how does $\rho(q,p,t)$ evolve in time? 

This is the question that we will answer in this section. And we find something surprising. Now that we've injected some uncertainty into the system, in the guise of the probability distribution $\rho(q, p, t)$ , the equations of classical mechanics start to look very similar to those of quantum mechanics. They're not exactly the same of course. After all, as we will see in a later book, quantum mechanics is really a radical departure from the classical framework. But there are certainly hints in the classical world of the quantum world that lies underneath. 

We start this story with the following, important result: 

Liouville's Theorem: As a region of phase space evolves in time, its shape will typically change but its volume will not. 

Proof: We prove this result by considering the evolution of an infinitesimal volume, moving for an infinitesimal time. We'll take this region of phase space to be centred around the point $(q^i, p_i)$ with volume 

$$
V = d q ^ {1} \dots d q ^ {n} d p _ {1} \dots d p _ {n}.\tag{10.38}
$$

Then in time dt, we know that 

$$
q ^ {i} \rightarrow q ^ {i} + \dot {q} ^ {i} d t = q ^ {i} + \frac {\partial H}{\partial p _ {i}} d t \equiv \tilde {q} ^ {i}\tag{10.39}
$$

and 

$$
p _ {i} \rightarrow p _ {i} + \dot {p} _ {i} d t = p _ {i} - \frac {\partial H}{\partial q ^ {i}} d t \equiv \tilde {p} _ {i}.\tag{10.40}
$$

So the new volume in phase space is 

$$
\tilde {V} = d \tilde {q} ^ {1} \dots d \tilde {q} ^ {n} d \tilde {p} _ {1} \dots d \tilde {p} _ {n} = (\det \mathcal {J}) V\tag{10.41}
$$

where $\det J$ is the Jacobian of the transformation defined by the determinant of the $2n \times 2n$ matrix 

$$
\mathcal {J} = \left( \begin{array}{c c} \partial \tilde {q} ^ {i} / \partial q ^ {j} & \partial \tilde {q} ^ {i} / \partial p _ {j} \\ \partial \tilde {p} _ {i} / \partial q ^ {j} & \partial \tilde {p} _ {i} / \partial p _ {j} \end{array} \right)  .\tag{10.42}
$$

To prove the theorem, we need to show that $\det J = 1$ . First consider a single degree of freedom (i.e. n = 1). Then we have 

$$
\begin{array}{r l} & {\det \mathcal {J} = \det \left( \begin{array}{c c} 1 + (\partial^ {2} H / \partial p \partial q) d t & (\partial^ {2} H / \partial p ^ {2}) d t \\ - (\partial^ {2} H / \partial q ^ {2}) d t & 1 - (\partial^ {2} H / \partial q \partial p) d t \end{array} \right)} \\ & {\qquad = 1 + \mathcal {O} (d t ^ {2}).} \end{array}
$$

which means that 

$$
\frac {d (\det \mathcal {J})}{d t} = 0.\tag{10.44}
$$

This tells us that the volume remains constant for all time. Now to generalise this to arbitrary n, we have 

$$
\det \mathcal {J} = \det \left( \begin{array}{c c} \delta_ {i j} + (\partial^ {2} H / \partial p _ {i} \partial q ^ {j}) d t & (\partial^ {2} H / \partial p _ {i} \partial p _ {j}) d t \\ - (\partial^ {2} H / \partial q ^ {i} \partial q ^ {j}) d t & \delta_ {i j} - (\partial^ {2} H / \partial q ^ {i} \partial p _ {j}) d t \end{array} \right)
$$

To compute the determinant, we need the result that 

$$
(1 + \epsilon M) = 1 + \epsilon \operatorname{Tr} M + \mathcal {O} (\epsilon^ {2})
$$

$$
\det \mathcal {J} = 1 + \sum_ {i} \left(\frac {\partial^ {2} H}{\partial p _ {i} \partial q ^ {i}} - \frac {\partial^ {2} H}{\partial q ^ {i} \partial p _ {i}}\right) d t + \mathcal {O} (d t ^ {2}) = 1 + \mathcal {O} (
$$

and we're done. 

Liouville's theorem is telling us that classical systems act, in many ways, like an incompressible fluid. But the fluid is incompressible in phase space rather than in configuration space. In fact, we can extend this analogy further. Suppose that we think of a “velocity field” in phase space, with $\mathbf{u} = (\dot{q}^{i}, \dot{p}_{i})$ . We also introduce the 2n-dimensional gradient operator, $\nabla = (\partial/\partial q^{i}, \partial/\partial p_{i})$ . Then, another way of capturing the spirit of Liouville's theorem is to note that 

$$
\nabla \cdot \mathbf {u} = \frac {\partial \dot {q} ^ {i}}{\partial q ^ {i}} + \frac {\partial \dot {p} _ {i}}{\partial p _ {i}} = \frac {\partial^ {2} H}{\partial p _ {i} \partial q ^ {i}} - \frac {\partial^ {2} H}{\partial q ^ {i} \partial p _ {i}} = 0.\tag{10.47}
$$

The equation $\nabla \cdot \mathbf{u} = 0$ is telling us that the "velocity field" $\mathbf{u}$ can't pile up at any point. What goes in, must come out. This is what's meant by an incompressible fluid. 

Liouville's theorem holds whether or not the system conserves energy. (i.e. whether or not $\partial H / \partial t = 0$ ). But the system must be described by a Hamiltonian. For example, systems with friction that exhibit dissipation do not obey Liouville's theorem. Instead, they tend to grind to a halt, heading to ever smaller regions of phase space with $\dot{q}_i = 0$ . That's one way of seeing why there is no Hamiltonian formulation for theories with friction. 

Liouville's theorem states that the volume of a region of phase space stays constant under Hamiltonian evolution. But the theorem says nothing about the shape of that region. In some simple examples, the region might retain its rough shape. But there's nothing that says that this must be the case. Indeed, in systems that exhibit chaos, a given starting region will stretch and twist, keeping its original volume but ultimately spreading tendril-like over a large region of phase space, rather like a droplet of ink spreading in water. This means that although Liouville's theorem tells us that the volume in phase space is strictly unchanged, in any practical terms our ignorance nonetheless increases. 

As we mentioned in the introduction to this section, there are hints of quantum mechanics in Liouville's theorem. Suppose we have a system of particles distributed randomly within a square $\Delta q\Delta p$ in phase space. Liouville's theorem implies that if we evolve the system in any Hamiltonian manner, we can cut down the spread of positions of the particles only at the cost of increasing the spread of momentum. There is a similar story in quantum mechanics, where Heisenberg's uncertainty relation is also written $\Delta q\Delta p = \text{constant}$ . However, it's worth stressing that, while Liouville and Heisenberg carry a similar smell, there are very profound differences between them. The distribution in the classical picture reflects our ignorance of the system rather than any intrinsic uncertainty. 

## An Example: Falling Particles

Here's a particularly simple demonstration of Liouville's theorem in a system that most definitely is not chaotic: a particle undergoing uniform acceleration due to gravity. 

Consider a bunch of particles which are initially spread uniformly in height, far above the ground, over a region $-h \leq z \leq +h$ . In addition, we'll assume that the particles have random vertical momenta, distributed uniformly over the interval $-P \leq p \leq P$ . The initial area of phase space covered by these particles is A = 4hP. 

As the particles are accelerated downwards, their positions in phase space evolve as 

$$
(z _ {0}, p _ {0}) \mapsto (z (t), p (t))\tag{10.48}
$$

with $z(t) = z_0 + p_0 t / m - \frac{1}{2} g t^2$ and $p(t) = p_0 - m g t$ . What was previously a square in phase space evolves to a parallelogram. It's simple to check that the area of this parallelogram remains $A = 4hP$ for all time. 

## 10.2.1 Liouville's Equation

We can now apply Liouville's theorem to understand the evolution of a probability distribution $\rho(q, p, t)$ on phase space. Any probability distribution must obey a normalisation condition - either (10.36) or (10.37) - and, moreover, this must hold for all time. We know from Liouville's theorem that co-moving volume elements $dp dq$ are preserved, so the normalisations can only hold for all time if 

$$
\frac {d \rho}{d t} = \frac {\partial \rho}{\partial t} + \frac {\partial \rho}{\partial q ^ {i}} \dot {q} ^ {i} + \frac {\partial \rho}{\partial p _ {i}} \dot {p} _ {i} = 0.\tag{10.49}
$$

If we replace the expressions for $\dot{p}_i$ and $\dot{q}^i$ by Hamilton's equations (10.16) then, rearranging terms, we get 

$$
\frac {\partial \rho}{\partial t} = \frac {\partial \rho}{\partial p _ {i}} \frac {\partial H}{\partial q ^ {i}} - \frac {\partial \rho}{\partial q ^ {i}} \frac {\partial H}{\partial p _ {i}}.\tag{10.50}
$$

This is Liouville's equation. 

## Time-Independent Distributions

An individual particle will evolve in time (unless it's sitting at an equilibrium point). But what about a distribution of particles or a collection of particles? Now there's the possibility that it doesn't evolve in time at all, because when one particle moves in phase space, another comes in to take its place. These are called, quite reasonably, time-independent distributions. 

We should be careful because there are different meanings to time dependence here. We already know that the total time derivative $d\rho /dt = 0$ for all distributions. This is just the statement of Liouville's theorem that the volume of phase space doesn't change. For a time-independent distribution, it's the partial time derivative that vanishes 

$$
\frac {\partial \rho}{\partial t} = 0 \quad \Longrightarrow \quad \frac {\partial \rho}{\partial p _ {i}} \frac {\partial H}{\partial q ^ {i}} - \frac {\partial \rho}{\partial q ^ {i}} \frac {\partial H}{\partial p _ {i}} = 0.\tag{10.51}
$$

where the second expression follows from Liouville's equation (10.50). 

The most important class of time-independent probability distributions are those constructed from the Hamiltonian on phase space. Any distribution of the form 

$$
\rho = \rho (H (q, p))\tag{10.52}
$$

is time independent. To see this, we just compute 

$$
\frac {\partial \rho}{\partial p _ {i}} \frac {\partial H}{\partial q ^ {i}} - \frac {\partial \rho}{\partial q ^ {i}} \frac {\partial H}{\partial p _ {i}} = \frac {\partial \rho}{\partial H} \frac {\partial H}{\partial p _ {i}} \frac {\partial H}{\partial q ^ {i}} - \frac {\partial \rho}{\partial H} \frac {\partial H}{\partial q ^ {i}} \frac {\partial H}{\partial p _ {i}} = 0.
$$

Within this class, there is one distribution that stands out. This is the Boltzmann distribution 

$$
\rho = \exp \left(- \frac {H (q , p)}{k _ {B} T}\right)\tag{10.54}
$$

where T is temperature and $k_{B}$ is a constant of nature called the Boltzmann constant that can be thought of as a conversion factor between temperature and energy. The Boltzmann distribution describes the probability for any system in thermal equilibrium at some temperature T. Roughly, the hotter the system the more likely that the high energy states will be populated. For example, for a free particle with $H = p^{2}/2m$ , the Boltzmann distribution is $\rho = \exp\left(-m\dot{x}^{2}/2k_{B}T\right)$ , which is a Gaussian distribution in velocities. 

It's not yet obvious why, out of all the probability distributions of the form $\rho(H)$ , the Boltzmann distribution $\rho = e^{-H/k_B T}$ is preferred. There is a fairly long, but important, calculation that explains this for $10^{23}$ particles in a gas that we will present in Volume 4 on Fluid Mechanics (see the chapter on kinetic theory). We will also devote much of the book on Statistical Physics to understanding the origin and consequences of the Boltzmann distribution. 

There's an interesting historical anecdote here. We can look back to the Hamiltonian of a free particle in a magnetic field (10.33), 

$H = (\mathbf{p} - e\mathbf{A})^{2}/2m$ . But, as we noted back then, written in terms of the velocity, the Hamiltonian is just $H = \dot{x}^{2}/2m$ , so the corresponding Boltzmann distribution is 

$$
\rho = \exp \left(- \frac {H (q , p)}{k _ {B} T}\right) = \exp \left(- \frac {m \dot {\mathbf {x}} ^ {2}}{2 k _ {B} T}\right).\tag{10.55}
$$

This is again a Gaussian distribution of velocities and is independent of the magnetic field. This is a concern: the magnetism of solids is all about how the motion of electrons is affected by magnetic fields. Yet, while the magnetic field clearly affects the velocity of a single particle, it doesn't change the average velocity of many particles. This is known as the Bohr-Van Leeuwen paradox: there can be no magnetism in classical physics. This was one of the motivations for the development of quantum theory. 

## 10.2.2 Poincaré Recurrence Theorem

Next, we turn to another aspect of motion in phase space. The following theorem applies to systems with a bounded accessible phase space, meaning that it has finite volume. At first glance, the requirement of a finite volume phase space seems overly restrictive because all phase spaces that we've met so far have infinite volume. But the meat is in the word “accessible”. If we have a conserved energy, $E = T + V$ with T > 0 and V > 0, then the accessible phase space lies in the spatial region $V(\mathbf{x}) \leq E$ . This is what we require to be bounded. It just means that the particles can't escape to infinity. 

With this in mind, we have the following theorem, due to Poincaré, from around 1890. Roughly speaking, it says that, wherever you start in phase space, if you wait long enough you will ultimately return to somewhere arbitrarily close to this initial point. More precisely... 

Poincaré Recurrence Theorem: Consider an initial point P in phase space. Then for any neighbourhood $D_{0}$ of P, there exists a point $P' \in D_{0}$ that will return to $D_{0}$ in a finite time. 

Proof: Consider the evolution of the region $D_{0}$ over a finite time interval T. Hamilton's equations provide a map $D_{0} \mapsto D_{1}$ shown in Figure 10.3. By Liouville's theorem, we know that $\operatorname{Vol}(D_{0}) = \operatorname{Vol}(D_{1})$ , although the shapes of these two regions will in general be different. Let $D_{k}$ be the region after time kT, with k a positive integer. Then we first note that there there must exist integers k and $k'$ such that the intersection of $D_{k}$ and $D_{k'}$ is not empty 

$$
D _ {k} \cap D _ {k ^ {\prime}} \neq \phi .\tag{10.56}
$$

To see this, suppose that it's not true. Then the total volume $\bigcup_{k=0}^{\infty} D_k \to \infty$ but, by assumption, the accessible phase space volume is finite. 

Take $k' > k$ such that the intersection region $\Omega_{k,k'} = D_k \cap D_{k'}$ is not empty. But since the Hamiltonian mapping $D_k \to D_{k+1}$ is invertible, we can track backwards to find 

$\Omega_{0,k^{\prime} - k} = D_0\cap D_{k^{\prime} - k}\neq \phi$ , as shown in Figure 10.4. This tells us that some point $P' \in D_{0}$ has returned to $D_{0}$ in $k' - k$ time steps T. ☐ 

Fig. 10.3 The Hamiltonian map in a time step T. 

Fig. 10.4 The inverse Hamiltonian map for $k' - k$ time steps proves the Poincaré recurrence theorem. 

What does the Poincaré recurrence theorem mean? Consider gas molecules all in one corner of the room. If we let them go, they fill the room. But the Poincaré recurrence theorem tells us that if we wait long enough, then they will all return once more to the corner of the room. 

That's a little disconcerting. One of the most powerful results in physics is the second law of thermodynamics which says that a quantity called entropy always increases. (This is described in detail in the book on Statistical Physics.) Yet this appears to be in stark contradiction to the Poincaré recurrence theorem which says that, if you wait long enough, then you'll get arbitrarily close to your starting point. If entropy did indeed increase, then it must later decrease. 

We reconcile these contradictory statements only by considering the relevant timescales. The Poincaré recurrence theorem says that there exists a time $(k' - k)T$ after which we return to our starting point, but it says nothing about how long we would expect to wait. The precise recurrence time depends on how “close” we want the system to return. (As an advanced comment: the question of how close we are in phase space isn’t fully well defined in classical mechanics, because phase space doesn't come with a natural metric that would allow us to measure distances.) But we can get some idea through a simple, crude argument. 

To illustrate this, let's go back to a gas with, say, $10^{23}$ molecules initially confined to one half of a room. We let the gas go and it rapidly fills the room. At some fixed time later, there is a probability $1/2$ that a given gas molecule will be in the original half of the room. If we assume that the motion of the gas molecules are independent, this means that the probability that all $10^{23}$ gas molecules return to the original half of the room is 

$$
P = \left(\frac {1}{2}\right) ^ {1 0 ^ {2 3}}.\tag{10.57}
$$

That's a very small number! Suppose that a gas molecule takes some characteristic time $T$ to cross the room. (Say, $T = L / v$ with $L$ the size of the room, and $v$ the velocity of the molecule.) Then, one might expect that all molecules return to the original half in some recurrence time of order 

$$
T _ {\mathrm{recurrence}} \sim 2 ^ {1 0 ^ {2 3}} T.\tag{10.58}
$$

That's now a very very long time! Rather amusingly, it doesn't matter what the characteristic time scale $T$ actually is. A reasonable estimate might be $T = 1$ second, but if you replace this with a Planck time $T \approx 10^{-44}$ seconds or a Hubble time $T \approx 10$ billion years you still get the same ball park answer for the recurrence time because everything is swamped by 

that double exponential. (This boils down to the fact that $10^{23} - 44 \approx 10^{23}$ .) 

More generally, the recurrence time of a complicated system is of order 

$$
T _ {\mathrm{recurrence}} \sim e ^ {S} \times \mathrm{someunitoftime}\tag{10.59}
$$

with S the entropy of the system. Again, the unit of time is completely irrelevant when S is exponentially large. 

There is something of an irony to this. The second law of thermodynamics is one law of physics that we can be confident will never be overthrown. But this is precisely because we know that it's not an exact statement! The second law of thermodynamics is probabilistic in nature. We know that, if we wait long enough, then the second law will certainly be violated. But the time that you need to wait is so unfathomably vast that it's a good operational definition of the word “never”. 

## 10.3 Poisson Brackets

We now continue with our study of the structure underlying classical mechanics. We start with a definition that looks slightly weird when you first see it. 

Let $f(q,p)$ and $g(q,p)$ be two functions on phase space. Then the Poisson bracket is defined to be 

$$
\{f, g \} = \frac {\partial f}{\partial q ^ {i}} \frac {\partial g}{\partial p _ {i}} - \frac {\partial f}{\partial p _ {i}} \frac {\partial g}{\partial q ^ {i}}.\tag{10.60}
$$

As we will soon see, it's a structure that appears in many places. 

The Poisson bracket obeys the following properties, all of which are straightforward to prove: 

• $\{f,g\}=-\{g,f\}$ . 

- linearity: $\{\alpha f + \beta g, h\} = \alpha \{f, h\} + \beta \{g, h\}$ for all $\alpha, \beta \in \mathbb{R}$ . 

- Leibniz rule: $\{fg, h\} = f\{g, h\} + \{f, h\}g$ . This follows from the chain rule in differentiation. 

- Jacobi identity: $\{f, \{g, h\}\} + \{g, \{h, f\}\} + \{h, \{f, g\}\} = 0$ . To prove this you need a large piece of paper and a hot cup of coffee. Expand out all 24 terms and watch them cancel one by one. 

There are a number of other mathematical objects that obey these same four algebraic properties. The most familiar is the commutator 

$[A, B] = AB - BA$ between two matrices A and B. Another, more advanced example, is something called a “Lie derivative” in differential geometry. 

For the standard coordinates on phase space, the Poisson bracket reads 

$$
\{q ^ {i}, q ^ {j} \} = \{p _ {i}, p _ {j} \} = 0 \quad \text { and } \quad \{q ^ {i}, p _ {j} \} = \delta_ {j} ^ {i} .\tag{10.61}
$$

This is another place where something in classical mechanics looks rather quantumy. Essentially the same equations (10.61) appear in quantum mechanics, but with the Poisson bracket { , } replaced by commutators [ , ] and an extra factor of $i\hbar$ thrown in. This is something that we'll explore further in Section 10.8. 

The Poisson bracket is an example of what mathematicians call a symplectic structure on phase space. Roughly speaking, given an even-dimensional manifold, a symplectic structure is an anti-symmetric pairing of coordinates on the space. In physics language, this means that directions on the space are paired into position variables q and their conjugate momenta p, as captured by the relations $(10.61)$ . 

Among the many uses of the Poisson bracket is that it provides a natural way to describe time evolution. 

Claim: For any function $f(q, p, t)$ on phase space, evolution under Hamilton's equations is given by the following lovely result 

$$
\frac {d f}{d t} = \{f, H \} + \frac {\partial g}{\partial t}.\tag{10.62}
$$

We sometimes say that the Hamiltonian H generates time evolution on phase space. This is language that will embrace further as this section proceeds. 

Proof: We simply need to look at 

$$
\begin{array}{r l} & {\frac {d f}{d t} = \frac {\partial f}{\partial p _ {i}} \dot {p _ {i}} + \frac {\partial f}{\partial q ^ {i}} \dot {q} ^ {i} + \frac {\partial g}{\partial t}} \\ & {\quad = - \frac {\partial f}{\partial p _ {i}} \frac {\partial H}{\partial q ^ {i}} + \frac {\partial f}{\partial q ^ {i}} \frac {\partial H}{\partial p _ {i}} + \frac {\partial g}{\partial t} = \{f, H \} + \frac {\partial g}{\partial t}} \end{array}
$$

where we've invoked Hamilton's equations in the second equality. $\square$ 

The result (10.62) reduces to Liouville's equation (10.50) when we consider a probability distribution with $d\rho /dt = 0$ . If we restrict to the function $f = q^i$ or $f = p_i$ , then the expression (10.62) simply gives us back Hamilton's equations 

$$
\dot {q} ^ {i} = \frac {\partial H}{\partial p _ {i}} \quad \text { and } \quad \dot {p} _ {i} = - \frac {\partial H}{\partial q _ {i}} .\tag{10.64}
$$

But (10.62) generalises this to any function $f(q,p)$ . This general expression also has a counterpart in quantum mechanics, where an analogous equation describes the time evolution of operators in the so-called Heisenberg picture. 

A simple consequence of $(10.62)$ is that any function $Q(q,p)$ on phase space that obeys 

$$
\{Q, H \} = 0\tag{10.65}
$$

is a constant of motion. We say that $Q$ and $H$ Poisson commute. As an example of this, suppose that some coordinate $q^i$ is ignorable, meaning that it doesn't appear in the Hamiltonian. Then, from the definition of the Poisson bracket, we have 

$$
\dot {p} _ {i} = \{p _ {i}, H \} = 0\tag{10.66}
$$

which tells us that the conjugate momentum $p_{i}$ is a conserved quantity. This simply confirms the result that we saw earlier in both the Lagrangian formalism (7.116) and the Hamiltonian formalism (10.19), now in the language of Poisson brackets. 

If $Q_{1}$ and $Q_{2}$ are constants of motion, so that $\{Q_{1}, H\} = \{Q_{2}, H\} = 0$ , then the Jacobi identity tells us that 

$\{\{Q_{1}, Q_{2}\}, H\} = \{Q_{1}, \{Q_{2}, H\}\} + \{\{Q_{1}H\}, Q_{2}\} = 0$ which means that $\{Q_{1}, Q_{2}\}$ is also a constant of motion. We say that the constants of motion form a closed algebra under the Poisson bracket. 

We now illustrate the Poisson bracket structure with a number of examples. Our first examples will be things that are familiar. But, we'll then move to things that look nothing like the kind of $L = \frac{1}{2} m \dot{\mathbf{x}}^{2} - V(\mathbf{x})$ classical mechanics systems that we first encountered in this book. 

## 10.3.1 Angular Momentum

The angular momentum of a particle is given by $L = x \times p$ . In components, this reads 

$$
L _ {1} = x ^ {2} p _ {3} - x ^ {3} p _ {2}, L _ {2} = x ^ {3} p _ {1} - x ^ {1} p _ {3}, L _ {3} = x ^ {1} p _ {2} - x ^ {2} p _ {1}.
$$

The Poisson bracket structure is 

$$
\begin{array}{r l} & {\left\{L _ {1}, L _ {2} \right\} = \left\{x ^ {2} p _ {3} - x ^ {3} p _ {2}, x ^ {3} p _ {1} - x ^ {1} p _ {3} \right\}} \\ & {\qquad = \left\{x ^ {2} p _ {3}, x ^ {3} p _ {1} \right\} + \left\{x ^ {3} p _ {2}, x ^ {1} p _ {3} \right\}} \\ & {\qquad = - x ^ {2} p _ {1} + p _ {2} x ^ {1} = L _ {3}.} \end{array}\tag{10.68}
$$

So if $L_{1}$ and $L_{2}$ are conserved, then we see that $L_{3}$ must also be conserved. By symmetry, this means that the whole vector L is conserved if any two components are. A similar calculation for other components gives 

$$
\left\{L _ {i}, L _ {j} \right\} = \epsilon_ {i j k} L _ {k}.\tag{10.69}
$$

Similarly, one can show that 

$$
\{\mathbf {L} ^ {2}, L _ {i} \} = 0 \quad \text {with} i = 1, 2, 3\tag{10.70}
$$

where $L^{2} = \sum_{i} L_{i}^{2}$ . As with many other equations in this section, you will see very similar expressions when we learn quantum mechanics, with the Poisson brackets { , } replaced by commutators [ , ] (and the occasional appearance of an $\hbar$ ). 

In fact, there is some group theory that sits behind this structure. The Poisson bracket structure (10.69) is the structure that underlies the Lie group $SO(3)$ of rotations. Or, more precisely, it is the structure of the related Lie algebra $so(3)$ . This is ultimately the reason why this same kind of structure arises in both classical mechanics and quantum mechanics. 

## 10.3.2 A Particle in a Magnetic Field, Revisited

We saw the Hamiltonian for a particle of charge q moving in a magnetic field B in Section 10.1.4. It is 

$$
H = \frac {1}{2 m} \left(\mathbf {p} - q \mathbf {A}\right) ^ {2} = \frac {1}{2} m \dot {\mathbf {x}} ^ {2}\tag{10.71}
$$

with the vector potential A related to the magnetic field by $B = \nabla \times A$ . As emphasised in the expression above, when written in terms of the velocity $\dot{x}$ , the Hamiltonian takes the same form with and without a magnetic field. All the physics in this example is buried in the relation between the momentum P and the velocity $\dot{x}$ 

$$
\mathbf {p} = m \dot {\mathbf {x}} + q \mathbf {A}.\tag{10.72}
$$

Alternatively, we can think of the magnetic field as hiding in the Poisson bracket structure. The canonical momentum has the usual Poisson bracket 

$$
\{x ^ {i}, p _ {j} \} = \delta_ {j} ^ {i} \quad \text { and } \quad \{p _ {i}, p _ {j} \} = 0 .\tag{10.73}
$$

However, as we've mentioned before, the canonical momentum $\mathbf{p}$ is not gauge invariant: it changes under a gauge transformation $\mathbf{A} \rightarrow \mathbf{A} + \nabla \chi$ . This means that there's no sense in which you can assign an unambiguous number to the momentum because someone else, working with a different but physically equivalent choice of $\mathbf{A}$ , will assign a different number. In contrast, the velocity $m\dot{\mathbf{x}}$ is gauge invariant and physical: everyone agrees on the value of the velocity. But its Poisson bracket structure is more complicated. A short calculation shows 

$$
\{x ^ {i}, \dot {x} ^ {j} \} = \frac {1}{m} \delta^ {i j} \quad \mathrm{and} \quad \{\dot {x} ^ {i}, \dot {x} ^ {j} \} = \frac {q}{m ^ {2}} \epsilon^ {i j k} B _ {k}.\tag{10.74}
$$

It's this Poisson bracket structure that is responsible for the interesting physics of a particle moving in a magnetic field. 

## A Curious Example: The Magnetic Monopole

It is an experimental fact that magnets have both a north and south pole. Cut a magnet in two, and each piece also has a north and a south pole. 

Nonetheless, we can postulate the existence of a magnetic monopole which would be, say, just a north pole on its own. Such a magnetic monopole would emit a radial magnetic field 

$$
\mathbf {B} = \frac {g}{4 \pi} \frac {\mathbf {r}}{r ^ {3}}\tag{10.75}
$$

with g the magnetic charge. 

Magnetic monopoles have never been observed. Moreover, at first glance there is a law of physics that says that they can't exist. This law of physics follows immediately from the formulation of electromagnetism in terms of the vector potential $\mathbf{A}$ . Since we define $\mathbf{B} = \nabla \times \mathbf{A}$ , we immediately have one of Maxwell's equations 

$$
\nabla \cdot \mathbf {B} = 0.\tag{10.76}
$$

This states that any flux that enters a region must also leave. In particular, it prohibits field configurations of the form (10.75) which give rise to a delta-function source on the right-hand side of $\nabla \cdot B$ . 

So if magnetic monopoles have never been observed and, moreover, are forbidden by the laws of physics, then why are we interested in them?! The reason is that every theory that goes beyond Maxwell's equations and tries to unify electromagnetism with the other forces of nature predicts magnetic monopoles. In fact, the existence of magnetic monopoles are one of the few robust predictions of every attempt to go beyond the current laws of physics. Which means that there's reason to suspect that, somewhere in the universe, there may be particles with a radial magnetic field given by (10.75). 

Here we ask a very simple question: what motion does an electron make when it moves in the presence of a magnetic monopole? It's tricky to set up the Lagrangian as we don't have a gauge potential A. (Actually, there are certain singular gauge potentials that we could work with. These will be described in Volume 2 on Electromagnetism, but we'll steer clear of them for now.) However, there is a more straightforward way to determine the motion using the Poisson brackets (10.74), which only depend on the magnetic field B and don't make any reference to the underlying vector potential A. 

The trick is to look at the angular momentum. Or, more precisely, to look at the modified angular momentum 

$$
\mathbf {J} = m \mathbf {x} \times \dot {\mathbf {x}} - \frac {q g}{4 \pi} \hat {\mathbf {r}}\tag{10.77}
$$

where $\hat{\mathbf{r}} = \mathbf{x} / |\mathbf{x}|$ is the unit radial vector. When $g = 0$ , the vector $\mathbf{J}$ reduces to the usual angular momentum. But the usual angular momentum isn't conserved in the presence of a magnetic monopole, even though the system has rotational symmetry. Instead, $\mathbf{J}$ defined in (10.77) is the conserved quantity. Indeed, it's simple to show, using the Poisson brackets (10.74), together with the Hamiltonian $H = \frac{1}{2} m\dot{\mathbf{x}}^2$ , that 

$$
\{H, \mathbf {J} \} = 0.\tag{10.78}
$$

This ensures that J is a constant of motion. Note that we managed to do this calculation without ever introducing a gauge potential A. 

The extra term in (10.77) is somewhat odd. It means that even if the electrically charged particle isn't moving, it still carries angular momentum in the presence of a monopole! This fact has a number of interesting consequences, especially when we come to think of magnetic monopoles in quantum mechanics. For now, however, we can look at what (10.77) teaches us. Since J is conserved, we can look at 

$$
\hat {\mathbf {r}} \cdot \mathbf {J} = - \frac {q g}{4 \pi}.\tag{10.79}
$$

This tells us that the radial direction $\hat{r}$ of the electron always sits at a constant angle relative to J. In other words, the electron lies on a cone of angle $\cos\theta=qg/4\pi J$ pointing away from the vector J. This tells us that if we throw an electron at a magnetic monopole, then it will move on a cone with opening angle $\theta$ . In fact it can be shown that the electron travels on a geodesic on this cone, typically moving towards the monopole until it reaches some minimal distance before it spirals back out again. 

## 10.3.3 First-Order Vortex Dynamics in the Plane

Sometimes, we might find ourselves given a set of equations of motion and wish to cast them in the framework of Hamiltonian dynamics. Here's 

an example. 

Consider N vortices moving in the $(x, y)$ -plane. The vortices have position $\mathbf{x}_{i} = (x_{i}, y_{i})$ and each is assigned a vorticity $\gamma_{i}$ , which you can think of as something akin to electric charge. In certain situations, the dynamics of these vortices is described by the equations of motion 

$$
\begin{array}{l} \dot {x} _ {i} = - \sum_ {j \neq i} \gamma_ {j} \frac {y _ {i} - y _ {j}}{| \mathbf {x} _ {i} - \mathbf {x} _ {j} | ^ {2}} \\ \dot {y} _ {i} = + \sum_ {j \neq i} \gamma_ {j} \frac {x _ {i} - x _ {j}}{| \mathbf {x} _ {i} - \mathbf {x} _ {j} | ^ {2}}. \end{array}\tag{10.80}
$$

The interaction terms between vortices drops off as 1/r, which is like the electrostatic force confined to a plane. 

The novelty with these equations is that they are first order, rather than second order. It's like the particles live in the world envisaged by Aristotle, in which forces directly change velocities, rather than the world Galileo appreciated in which forces cause only acceleration. It means, in particular, that you only need to specify the initial positions $\mathbf{x}_i$ of each vortex to uniquely solve the equations of motion. In other words, the positions $\mathbf{x}_i$ specify the state of the system. This is in contrast to more familiar second-order equations of motion where you need the positions and momenta to specify the state of the system. 

Earlier in this chapter, we explained that the state of the system parameterises what we called phase space M. This means that the phase space of a first-order system is parameterised only by the positions of the N particles, so that $M = R^{2N}$ . 

This has consequence for the Hamiltonian formulation of these equations. In particular, the Poisson bracket is a structure on phase space, so the bracket $\{f,g\}$ acts on functions $f(\mathbf{x}_{i})$ and $g(\mathbf{x}_{i})$ . For our vortex dynamics, it turns out that the relevant Poisson bracket structure is 

$$
\{f, g \} = \sum_ {i = 1} ^ {n} \frac {1}{\gamma_ {i}} \left(\frac {\partial f}{\partial x _ {i}} \frac {\partial g}{\partial y _ {i}} - \frac {\partial f}{\partial y _ {i}} \frac {\partial g}{\partial x _ {i}}\right).\tag{10.81}
$$

In particular, we have 

$$
\{x _ {i}, y _ {j} \} = \frac {\delta_ {i j}}{\gamma_ {i}}.\tag{10.82}
$$

This is a slightly strange structure: it means that one of the position coordinates, say y, is the canonical momentum for the other position, x. It arises whenever we are dealing with first-order, rather than second-order, equations of motion. 

To specify the dynamics, we also need to write down the Hamiltonian on phase space. We take 

$$
H = - \sum_ {i <   j} \gamma_ {i} \gamma_ {j} \log | \mathbf {r} _ {i} - \mathbf {r} _ {j} |.\tag{10.83}
$$

Note that there is no kinetic energy term. However, the Hamiltonian is not unfamiliar: it takes the same form as a potential between electric charges confined to a plane. We can now check that the Poisson bracket (10.81), together with the Hamiltonian (10.83), does indeed reproduce our equations of motion. We have 

$$
\dot {x} _ {i} = \{x _ {i}, H \} = \frac {1}{\gamma_ {i}} \frac {\partial H}{\partial y _ {i}} = - \sum_ {j \neq i} \gamma_ {j} \frac {y _ {i} - y _ {j}}{| \mathbf {x} _ {i} - \mathbf {x} _ {j} | ^ {2}}\tag{10.84}
$$

$$
\dot {y} _ {i} = \left\{y _ {i}, H \right\} = - \frac {1}{\gamma_ {i}} \frac {\partial H}{\partial x _ {i}} = \sum_ {j \neq i} \gamma_ {j} \frac {x _ {i} - x _ {j}}{\left| \mathbf {x} _ {i} - \mathbf {x} _ {j} \right| ^ {2}}.\tag{10.85}
$$

We can also briefly say a few words about the solutions to these equations. First, there are a few conserved quantities. There is one that follows from overall translational symmetry that we would usually call the total momentum although, in this context, it is more like a kind of centre of mass 

$$
P _ {x} = \sum_ {i} \gamma_ {i} y _ {i} \quad \text { and } \quad P _ {y} = - \sum_ {i} \gamma_ {i} x _ {i}.\tag{10.86}
$$

These satisfy $\{P_{x}, H\} = \{P_{y}, H\} = 0$ , ensuring that they are conserved quantities. We also have $\{P_{x}, P_{y}\} = \sum_{i} \gamma_{i}$ and the right-hand side, being constant, is trivially conserved. 

Another conserved quantity follows from rotational invariance on the plane, so we would usually identify it as the total angular momentum. In this case, it takes the form 

$$
J = - \frac {1}{2} \sum_ {i = 1} ^ {n} \gamma_ {i} (x _ {i} ^ {2} + y _ {i} ^ {2})\tag{10.87}
$$

which again satisfies $\{J,H\}=0$ , ensuring it is conserved. The full algebra of the conserved quantities includes $\{P_{x},J\}=-P_{y}$ and $\{P_{y},J\}=P_{x}$ , so the system closes, meaning we get back something that is among our conserved quantities on the right-hand side. In fact, one can show that H, J, and $(P_{x}^{2}+P_{y}^{2})$ provide three mutually Poisson-commuting conserved quantities. 

So what is the resulting motion of a bunch of vortices? A single vortex doesn't move: it's stuck in position. However, two vortices are induced to move by their mutual interaction. It's simple to solve their equations of motion to find that they move in a circle 

$$
\begin{array}{c} x _ {1} - x _ {2} = R \sin \left(\omega (t - t _ {0})\right) \\ y _ {1} - y _ {2} = R \cos \left(\omega (t - t _ {0})\right) \end{array}\tag{10.88}
$$

where R is the separation between the vortices and $\omega = (\gamma_{1} + \gamma_{2})/R^{2}$ . So we learn that two vortices orbit each other with frequency inversely proportional to the square of their separation. 

For three vortices, it turns out that there is a known solution which is possible because of the three mutually Poisson-commuting conserved quantities we saw above. For four or more vortices, the motion turns out to be chaotic. 

The Poisson bracket structure (10.82) is rather odd. However, it also arises naturally in another familiar system: a particle moving in a uniform magnetic field $\mathbf{B} = (0, 0, B)$ . We discussed this example previously in Section 7.6.2 and Section 10.1.4 where we saw that the canonical momentum gets modified to 

$$
\mathbf {p} = m \dot {\mathbf {x}} + q \mathbf {A}.\tag{10.89}
$$

If we work in the gauge $\mathbf{A} = (-By, 0, 0)$ then $p_{x} = m\dot{x} - qBy/m$ . We might consider situations in which the magnetic field is strong, so the second term dominates. In this case 

$$
p _ {x} \approx - \frac {q B y}{m} \quad \text { and } \quad \{x, p _ {x} \} = 1 \implies \{x, y \} \approx - \frac {m}{q B} .
$$

This is the same Poisson bracket structure (10.82) that we saw for vortices. I should confess that the $\approx$ sign is doing quite a lot of heavy lifting in (10.90). It's not really obvious that we can ignore the $\dot{x}$ term in the momentum in the classical world. However, the same approximation is valid in quantum mechanics where this can be thought of as something called the “projection to the lowest Landau level” and underlies, among other things, the quantum Hall effect. 

## 10.3.4 Spin and a Compact Phase Space

Our next example is again a story about angular momentum. However, this won't become apparent for a while. Instead, we're going to motivate this example with a rather different question. 

So far, in most of our examples of phase space it's been obvious what directions are “position” and what directions are “momentum”. Indeed, we usually start with some configuration space C, describing the positions of the system, and then double the dimension to get the phase space. For what it's worth, in fancy mathematical language the phase space in these familiar cases is called the cotangent bundle of the configuration space and denoted $M = T^{*}C$ . 

However, now that we've got a more abstract formulation of classical mechanics, we can spread our wings a little. We could take any even-dimensional space $\mathcal{M}$ (strictly a manifold) and think of it as the phase space of some system. To do this, we just need to equip it with a Poisson bracket structure. Then, adding a function over $\mathcal{M}$ that we identify as the Hamiltonian $H$ will tell us how anything evolves in time, using (10.62). 

Here we give the simplest example of this kind of approach. We will consider a phase space that is a two-dimensional sphere 

$$
\mathcal {M} = \mathbf {S} ^ {2}.\tag{10.91}
$$

This certainly doesn't look like our previous phase spaces, not least because it's a compact space meaning that it doesn't extend to infinity in any direction. In contrast, for all our other phase spaces, the momentum direction was always non-compact. For example, for the pendulum example the phase space was a cylinder $\mathcal{M} = \mathbb{R} \times \mathbf{S}^1$ , with the momentum parameterising the $\mathbb{R}$ direction. 

We'll parameterise the phase space $\mathbf{S}^2$ with the usual spherical polar coordinates, 

$$
\theta \in [ 0, \pi ] \quad \text { and } \quad \phi \in [ 0, 2 \pi)\tag{10.92}
$$

and consider the somewhat unusual action 

$$
S = \int d t J \dot {\phi} \cos \theta\tag{10.93}
$$

with J a constant that, for reasons that we will see below, should be thought of as the radius of the sphere. This is different from our previous actions because it is only linear in velocities, rather than quadratic. This means that the momentum conjugate to $\phi$ is 

$$
p _ {\phi} = \frac {\partial L}{\partial \dot {\phi}} = J \cos \theta\tag{10.94}
$$

which involves the other coordinate on the $S^{2}$ . This is why $S^{2}$ is the phase space, rather than the configuration space. Meanwhile, there is no momentum conjugate to $\theta$ , since $p_{\theta} = \partial L / \partial \dot{\theta} = 0$ . The Poisson bracket structure is defined on functions $f(\theta, \phi)$ and $g(\theta, \phi)$ by 

$$
\{f, g \} = - \frac {1}{J \sin \theta} \left(\frac {\partial f}{\partial \phi} \frac {\partial g}{\partial \theta} - \frac {\partial f}{\partial \theta} \frac {\partial g}{\partial \phi}\right) .\tag{10.95}
$$

The peculiar $1/\sin\theta$ factor out front ensures that this gives 

$$
\{\phi , p _ {\phi} \} = \{\phi , J \cos \theta \} = 1\tag{10.96}
$$

which is the expected Poisson bracket between a coordinate and its conjugate momentum. 

It's interesting to construct the 3-vector from the origin to some point on the sphere. We will call this 3-vector $\mathbf{J}$ (pre-empting the fact advertised above that $J$ is the radius of the sphere). The components of this three vector are 

$$
\begin{array}{l} J _ {1} = J \sin \theta \cos \phi , \\ J _ {2} = J \sin \theta \sin \phi , \\ J _ {3} = J \cos \theta . \end{array}\tag{10.97}
$$

We can compute the Poisson brackets between these. We have 

$$
\begin{array}{r l} & {\left\{J _ {1}, J _ {2} \right\} = J ^ {2} \left\{\sin \theta \cos \phi , \sin \theta \sin \phi \right\}} \\ & {\qquad = - \frac {J}{\sin \theta} \left(- \sin \theta \cos \theta \sin^ {2} \phi - \sin \theta \cos \theta \cos^ {2} \phi\right)} \\ & {\qquad = J \cos \theta = J _ {3}.} \end{array}
$$

Similar calculations show that we have the cyclic Poisson bracket 

$$
\left\{J _ {i}, J _ {j} \right\} = \epsilon_ {i j k} J _ {k}.\tag{10.99}
$$

This is the same Poisson bracket structure that we saw for the angular momentum in $(10.69)$ . This is not a coincidence. As we mentioned previously, this commutation relation captures the essence of the $SO(3)$ rotation group. In the present context, the structure $(10.99)$ reflects the $SO(3)$ rotational symmetry of the phase space $S^{2}$ , even though this rotational symmetry isn’t immediately apparent in our original action $(10.93)$ . 

In fact, the vector J has a physical connection to angular momentum: it describes the spin of a particle. We already used the word “spin” in Chapter 9 when describing rigid body motion. (It was the $\omega_{3}$ component of the angular velocity.) But that’s not the same thing as our spin J, although both are related to angular momentum. Instead the spin J is something that is usually first introduced in quantum mechanics and is unfamiliar in classical mechanics. For this reason, it’s worth pausing to take a brief diversion into the quantum world. 

Elementary particles such as electrons or quarks carry an internal angular momentum known as spin. In quantum mechanics, this manifests as two internal states of the particles, often denoted “spin up” $|\uparrow\rangle$ and “spin down” $|\downarrow\rangle$ . In contrast to other systems, we tend not to introduce spin in quantum mechanics by starting with some classical set-up and then quantising it. Indeed, some authors will tell you that spin is an intrinsically quantum mechanical property with no classical analogue. But that’s not true. The classical analogue is precisely the action (10.93). It turns out that we get a finite dimensional Hilbert space after quantisation precisely because we have a compact phase space $\mathcal{M} = \mathbf{S}^2$ . (For what it's worth, the classical magnitude of the spin $J$ determines the number of states in the Hilbert space. This will be explained in the book on Quantum Mechanics.) 

Back to classical mechanics, we can now ask: What is the dynamics of the spin J? If we compute the Hamiltonian that follows from the action (10.93), we find $H = \dot{\phi} p_{\phi} - L = 0$ . There's nothing deep going on here: the action (10.93) has H = 0 for the obvious reason that the spin J doesn't move. In fact, this is always the case whenever we have an action that is first order in time derivatives, rather than second order. In this case, the Hamiltonian is associated only to the potential terms in the action. 

To initiate some motion, we need to add such a potential term. Physically, we do this by coupling the spin to a magnetic field B. Mathematically, we do this by adding a term to the action $(10.93)$ 

$$
S = \int d t J \dot {\phi} \cos \theta + \mu \mathbf {B} \cdot \hat {\mathbf {J}}.\tag{10.100}
$$

Here $\hat{J} = J/J$ should be thought of as a function of $\theta$ and $\phi$ , i.e. a function on phase space. Meanwhile $\mu$ is a parameter that governs the strength of the coupling to to the spin, known as the magnetic moment. This now gives the Hamiltonian 

$$
H = - \mu \mathbf {B} \cdot \hat {\mathbf {J}} = - \mu (B _ {1} \sin \theta \cos \phi + B _ {2} \sin \theta \sin \phi + B _ {3} \cos \theta)
$$

The motion of the spin J can be seen from $(10.62)$ , 

$$
\begin{array}{r l} & {\frac {d J _ {i}}{d t} = \{J _ {i}, H \} = - \frac {\mu}{J} \{J _ {i}, J _ {j} \} B _ {j} = - \frac {\mu}{J} \epsilon_ {i j k} B _ {j} J _ {k}} \\ {\implies} & {\frac {d \mathbf {J}}{d t} = - \mu \mathbf {B} \times \hat {\mathbf {J}}.} \end{array}
$$

This tells us that the spin J only moves if it is not parallel to B. Suppose that $\mathbf{B} = (0, 0, B)$ . Then the equation of motion reads $J_{3} = constant$ , so $\dot{\theta} = constant$ , while 

$$
\begin{array}{l} \dot {J} _ {1} = \mu B \hat {J} _ {2} \\ \dot {J} _ {2} = - \mu B \hat {J} _ {1}. \end{array}\tag{10.103}
$$

This means that $\phi = \mu B t / J$ and the spin precesses around the direction of B, as shown in the figure above. 

## 10.4 Canonical Transformations

We first motivated the Hamiltonian framework by suggesting that it might be fruitful to place positions $q^{i}$ and momenta $p_{i}$ on a more equal footing. In fact, there's a notational trick that allows us to write Hamilton's equations so that they look even more symmetric with respect to interchanging q and p. We define the 2n vector 

$$
\mathbf {x} = (q ^ {1}, \dots , q ^ {n}, p _ {1}, \dots , p _ {n}) ^ {T}\tag{10.104}
$$

and the $2n \times 2n$ matrix $\Omega$ , 

$$
\Omega = \left( \begin{array}{c c} 0 & 1 \\ - 1 & 0 \end{array} \right)\tag{10.105}
$$

where each entry 0 and 1 is itself an $n \times n$ matrix. With this notation, Hamilton's equations read 

$$
\dot {\mathbf {x}} = \Omega \frac {\partial H}{\partial \mathbf {x}}.\tag{10.106}
$$

What does this buy us? Recall that, in the Lagrangian formalism, we made a big deal about the fact that we could change coordinates $q^i \to q^i(q)$ without changing the form of the equations. (These are the generalised coordinates that we described in Section 7.3.) Now that we've managed to put q and p on a more equal footing, we might wonder if its possible to make an even larger class of transformations that mix up positions and momenta, of the form, 

$$
q ^ {i} \to Q ^ {i} (q, p) \quad \mathrm{and} \quad p _ {i} \to P _ {i} (q, p).\tag{10.107}
$$

The answer is yes! But not all such transformations are allowed. To see what class of transformations leaves Hamilton's equations invariant, we use our new symmetric form in terms of x and write the transformation as 

$$
x _ {i} \rightarrow y _ {i} (x).\tag{10.108}
$$

Note that we'll continue to use the index $i$ which now runs over the range $i = 1, \ldots, 2n$ . We have 

$$
\dot {y} _ {i} = \frac {\partial y _ {i}}{\partial x _ {j}} \dot {x} _ {j} = \frac {\partial y _ {i}}{\partial x _ {j}} \Omega_ {j k} \frac {\partial H}{\partial y _ {l}} \frac {\partial y _ {l}}{\partial x _ {k}}\tag{10.109}
$$

or, collating all the indices, we have 

$$
\dot {\mathbf {y}} = \left(\mathcal {J} \Omega \mathcal {J} ^ {T}\right) \frac {\partial H}{\partial \mathbf {y}}.\tag{10.110}
$$

where $\mathcal{J}_{ij} = \partial y_i / \partial x_j$ is the Jacobian that we defined in (10.42) when proving Liouville's theorem. We see that Hamilton's equations are left invariant under any transformation whose Jacobian J satisfies 

$$
\mathcal {J} \Omega \mathcal {J} ^ {T} = \Omega \quad \Longleftrightarrow \quad \frac {\partial y _ {i}}{\partial x _ {j}} \Omega_ {j k} \frac {\partial y _ {l}}{\partial x _ {k}} = \Omega_ {i l}.\tag{10.111}
$$

The Jacobian J is said to be symplectic if this holds. A change of variables with a symplectic Jacobian is said to be a canonical transformation. As an aside, real, symplectic matrices J, defined by $(10.111)$ , form a group, $Sp(2n, \mathbb{R})$ , known as the symplectic group. 

The purpose of this section is to convince you that much of the essence of the Hamiltonian framework can be boiled down to understanding what kinds of canonical transformations are allowed. To set us on the way, we first note that there is an interplay between canonical transformation and the Poisson bracket structure, given by the following theorem: 

Theorem: The Poisson bracket is invariant under canonical transformations. Conversely, any transformation $(10.107)$ which preserves the Poisson bracket structure so that 

$$
\{q ^ {i}, Q ^ {j} \} = \{P _ {i}, P _ {j} \} = 0 \quad \text { and } \quad \{q ^ {i}, P _ {j} \} = \delta_ {i j}\tag{10}
$$

is canonical. 

Proof: Let's start by showing that the Poisson bracket is invariant under canonical transformations. Consider two functions $f(x_{i})$ and $g(x_{i})$ . Then 

$$
\{f, g \} = \frac {\partial f}{\partial q ^ {i}} \frac {\partial g}{\partial p _ {i}} - \frac {\partial f}{\partial p _ {i}} \frac {\partial g}{\partial q ^ {i}} = \frac {\partial f}{\partial x _ {i}} \Omega_ {i j} \frac {\partial g}{\partial x _ {j}}.\tag{10.}
$$

If $x\to y(x)$ , we have 

$$
\frac {\partial f}{\partial x _ {i}} = \frac {\partial f}{\partial y _ {k}} \mathcal {J} _ {k i}\tag{10.114}
$$

and, assuming the transformation is canonical, the Poisson bracket becomes 

$$
\{f, g \} = \frac {\partial f}{\partial y _ {k}} \mathcal {J} _ {k i} \Omega_ {i j} \mathcal {J} _ {l j} \frac {\partial g}{\partial y _ {l}} = \frac {\partial f}{\partial y _ {k}} \Omega_ {k l} \frac {\partial g}{\partial y _ {l}}.\tag{10.}
$$

This means that we can compute our Poisson brackets in any coordinates related by a canonical transformation. Now let's show the converse. Go back to the notation $(q^i, p_i)$ and the new coordinates $(Q^i(q, p), P_i(q, p))$ . The Jacobian is given by 

$$
\mathcal {J} _ {i j} = \left( \begin{array}{c c} \partial Q ^ {i} / \partial q ^ {j} & \partial Q ^ {i} / \partial p _ {j} \\ \partial P _ {i} / \partial q ^ {j} & \partial P _ {i} / \partial p _ {j} \end{array} \right)  .\tag{10.116}
$$

If we now compute $\mathcal{J}\Omega \mathcal{J}^T$ in components, we get 

$$
(\mathcal {J} \Omega \mathcal {J} ^ {T}) _ {i j} = \left( \begin{array}{c c} \{Q ^ {i}, Q ^ {j} \} & \{Q ^ {i}, P _ {j} \} \\ \{P _ {i}, Q ^ {j} \} & \{P _ {i}, P _ {j} \} \end{array} \right)  .\tag{10.117}
$$

So whenever the Poisson bracket structure is preserved, meaning that $(10.112)$ holds, the transformation is canonical. ☐ 

## A Trivial Example

In the next section we'll see several non-trivial examples of canonical transformations which mix up $q$ and $p$ variables. But for now let's content ourselves with reproducing the change to generalised coordinates that we already saw in Section 7.3. This means that we'll consider a change of coordinates of the form 

$$
q ^ {i} \to Q ^ {i} (q) .\tag{10.118}
$$

We know that Lagrange's equations are invariant under this. But what transformation do we have to make on the momenta 

$$
p _ {i} \rightarrow P _ {i} (q, p)\tag{10.119}
$$

so that Hamilton's equations are also invariant? We write $\Theta_{ij} = \partial Q^{i}/\partial q^{j}$ and look at the Jacobian (10.116) 

$$
\mathcal {J} _ {i j} = \left( \begin{array}{c c} \Theta_ {i j} & 0 \\ \partial P _ {i} / \partial q ^ {j} & \partial P _ {i} / \partial p _ {j} \end{array} \right)  .\tag{10.120}
$$

In order for the transformation to be canonical, we require $J\Omega J^{T} = \Omega$ . By expanding these matrices out in components, we see that this is true if 

$$
P _ {i} = (\Theta^ {- 1}) _ {j i} p _ {j}.\tag{10.121}
$$

This is what we would expect, because it's equivalent to $P_{i} = \partial L / \partial \dot{Q}^{i}$ . Although $Q^{i} = Q^{i}(q)$ only, we don't have “ $P_{i} = P_{i}(p)$ ”. Instead, the new momentum $P_{i}$ depends on both $q$ and $p$ . 

## 10.4.1 Infinitesimal Canonical Transformations

An infinitesimal canonical transformation takes the form 

$$
\begin{array}{l} q ^ {i} \to Q ^ {i} = q ^ {i} + \alpha F ^ {i} (q, p)  , \\ p _ {i} \to P _ {i} = p _ {i} + \alpha E _ {i} (q, p) \end{array}\tag{10.122}
$$

where $\alpha$ is considered to be infinitesimally small. What functions $F^{i}(q,p)$ and $E_{i}(q,p)$ are allowed for this to be a canonical transformation? The Jacobian (10.116) is 

$$
\mathcal {J} _ {i j} = \left( \begin{array}{c c} \delta_ {i j} + \alpha   \partial F ^ {i} / \partial q ^ {j} & \alpha   \partial F ^ {i} / \partial p _ {j} \\ \alpha   \partial E _ {i} / \partial q ^ {j} & \delta_ {i j} + \alpha   \partial E _ {i} / \partial p _ {j} \end{array} \right)  .\tag{10.1}
$$

The requirement that $\mathcal{J}\Omega\mathcal{J}^{T}=\Omega$ then gives 

$$
\frac {\partial F ^ {i}}{\partial g _ {j}} = - \frac {\partial E _ {i}}{\partial p _ {j}}.\tag{10.124}
$$

This holds if the transformations $F^{i}$ and $G_{i}$ can be written in the form 

$$
F ^ {i} = \frac {\partial G}{\partial p _ {i}} \quad \text { and } \quad E _ {i} = - \frac {\partial G}{\partial q ^ {i}}\tag{10.125}
$$

for some function $G(q, p)$ . We say that G generates the transformation. 

This discussion motivates a slightly different way of thinking about canonical transformations. Suppose that we have a one-parameter family of transformations, 

$$
q ^ {i} \rightarrow Q ^ {i} (q, p; \alpha) \quad \text { and } \quad p _ {i} \rightarrow P _ {i} (q, p; \alpha)\tag{10.126}
$$

which are canonical for all $\alpha\in R$ and have the property that $Q^{i}(q,p;\alpha=0)=q^{i}$ and $P_{i}(q,p;\alpha=0)=p_{i}$ . Up until now, we've been thinking of canonical transformations in the “passive” sense, with $(Q^{i},P_{i})$ labelling the same point in phase space as $(q^{i},p_{i})$ , just in different 

coordinates. But a one-parameter family of canonical transformations can be endowed with a different interpretation, namely that the transformations take us from one point in the phase space $(q^{i}, p_{i})$ to another point in the same phase space $(Q^{i}(q, p; \alpha), P_{i}(q, p; \alpha))$ . In this “active” interpretation, as we vary the parameter $\alpha$ we trace out lines in phase space. Using the results (10.122) and (10.125), the tangent vectors to these lines are given by, 

$$
\frac {d q ^ {i}}{d \alpha} = \frac {\partial G}{\partial p _ {i}} \quad \mathrm{and} \quad \frac {d p _ {i}}{d \alpha} = - \frac {\partial G}{\partial q ^ {i}}.\tag{10.127}
$$

But these look just like Hamilton's equations, with the Hamiltonian replaced by the function $G$ and time replaced by the parameter $\alpha$ . 

What we've found is that every one-parameter family of canonical transformations can be thought of as “Hamiltonian flow” on phase space for an appropriately chosen “Hamiltonian” $G$ . Equivalently, time evolution itself can be thought of as a canonical transformation for the coordinates 

$$
(q ^ {i} (t _ {0}), p _ {i} (t _ {0})) \rightarrow (q ^ {i} (t), p _ {i} (t))\tag{10.128}
$$

generated by the Hamiltonian. 

## 10.4.2 The Inverse Noether Theorem

In Section 7.5, we learned that there is a deep connection between symmetries and conservation laws. This connection is enshrined in 

Noether's theorem which tells us that, given a symmetry of the Lagrangian, we can construct a conserved quantity. We will now see that the idea of canonical transformations allows us to go the other way: given a conserved quantity, we can construct the underlying symmetry. 

First, let's see what a symmetry looks like in this set-up. We consider a canonical transformation generated by some function $G(q, p)$ on phase space. From (10.122) and (10.125), this means that the positions and momenta transform as 

$$
\delta q ^ {i} = \frac {\partial G}{\partial p _ {i}} \quad \text { and } \quad \delta p _ {i} = - \frac {\partial G}{\partial q ^ {i}}\tag{10.129}
$$

where we've chosen to drop the infinitesimal parameter on the grounds that it just goes along for the ride in all formulae below. Under such an infinitesimal transformation, the Hamiltonian changes as 

$$
\delta H = \frac {\partial H}{\partial q ^ {i}} \delta q ^ {i} + \frac {\partial H}{\partial p _ {i}} \delta p _ {i} = \frac {\partial H}{\partial q ^ {i}} \frac {\partial G}{\partial p _ {i}} - \frac {\partial H}{\partial p _ {i}} \frac {\partial G}{\partial q ^ {i}} = \{H, G \}.
$$

The generator G is called a symmetry of the Hamiltonian if $\delta H = 0$ . We see that a symmetry is generated by a function G that obeys 

$$
\{G, H \} = 0.\tag{10.131}
$$

But, from $(10.62)$ , we know that any function $G(q, p)$ that Poisson-commutes with the Hamiltonian is a constant of motion 

$$
\{G, H \} = 0 \quad \Longleftrightarrow \quad \frac {d G}{d t} = 0.\tag{10.132}
$$

This is the Hamiltonian version of Noether's theorem. And it tells us something new: the conserved quantity $G$ generates the symmetry through the canonical transformations (10.129). 

## Examples: Momentum, Angular Momentum, and Energy

We'll work with the familiar example of a particle moving in $\mathbb{R}^3$ , so that the coordinates on phase space are $q^i = (x,y,z)$ and $p_i = (p_x,p_y,p_z)$ . We can then run through the usual gamut of examples, in each case inverting the logic that we saw in Section 7.5. 

First, suppose that the momentum in the direction $\mathbf{n}$ is conserved, so $G = \mathbf{n} \cdot \mathbf{p}$ . Using (10.129), we see that this generates the symmetry 

$$
\delta \mathbf {x} = \mathbf {n} \quad \text { and } \quad \delta \mathbf {p} = 0 .\tag{10.133}
$$

This, of course, is a translation in the direction n. We see that translations are generated by momentum. 

Next, angular momentum. For concreteness, we'll focus on the component of angular momentum $L_{3} = xp_{y} - yp_{x}$ . Take $G = L_{3}$ in (10.129) to see that this generates the transformation 

$$
\begin{array}{c} \delta x = - y, \quad \delta y = x, \quad \delta z = 0 \\ \delta p _ {x} = - p _ {y}, \quad \delta p _ {y} = p _ {x}, \quad \delta p _ {z} = 0. \end{array}\tag{10.134}
$$

This is an infinitesimal rotation about the z-axis. We see that rotations are generated by angular momentum. 

Finally, time translations are something of a special case. This is because, as we've already seen, Hamilton's equation, when written in the language of Poisson brackets (10.62), already tells us that the Hamiltonian generates time translations. 

## The Runge–Lenz Vector Revisited

In Section 5.4.3, we saw that the Kepler problem is special. A particle moving in $\mathbb{R}^3$ , with Hamiltonian 

$$
H (\mathbf {x}, \mathbf {p}) = \frac {1}{2 m} \mathbf {p} ^ {2} - \frac {k}{r}\tag{10.135}
$$

has the usual conserved quantities of energy and angular momentum L. But, in addition, there is an extra conserved quantity called the Runge–Lenz vector 

$$
\mathbf {A} = \frac {\mathbf {p} \times \mathbf {L}}{m k} - \hat {\mathbf {r}}.\tag{10.136}
$$

Previously, we showed that this is conserved, and that it can be used to quickly show that particles move on conic sections. But we didn't see the symmetry that underlies this conservation law. Now, in the Hamiltonian framework, we can rectify this. 

The symmetry transformation on x and p is generated by the Runge–Lenz vector itself. This means that there are three symmetries generated by $A_{i}$ with i = 1, 2, 3. Using $(10.129)$ , we have 

$$
\delta_ {i} x _ {j} = \frac {\partial A _ {i}}{\partial p ^ {j}} = \frac {1}{m k} \Big (2 x _ {i} p _ {j} - p _ {i} x _ {j} - (\mathbf {x} \cdot \mathbf {p}) \delta_ {i j} \Big)\tag{10.137}
$$

and 

$$
\delta_ {i} p _ {j} = - \frac {\partial A _ {i}}{\partial x _ {j}} = \frac {1}{m k} \left(p _ {i} p _ {j} - \mathbf {p} ^ {2} \delta_ {i j}\right) + \frac {\delta_ {i j}}{r} - \frac {x _ {i} x _ {j}}{r ^ {3}}.\tag{10}
$$

This symmetry certainly isn't obvious. In particular, it mixes up position and momenta coordinates. 

We mentioned that conserved charges form a closed algebra under the Poisson bracket. This means that if $Q_{1}$ and $Q_{2}$ are conserved, then so too is $\{Q_{1}, Q_{2}\}$ . For the Kepler potential, we have angular momentum L, the Runge–Lenz vector A, and the Hamiltonian H all conserved. Some time playing with indices reveals that their algebra is 

$$
\begin{array}{r l} & {\{L _ {i}, L _ {j} \} = \epsilon_ {i j k} L _ {k}} \\ & {\{L _ {i}, A _ {j} \} = \epsilon_ {i j k} A _ {k}} \\ & {\{A _ {i}, A _ {j} \} = - \frac {2 H}{m k} \epsilon_ {i j k} L _ {k}.} \end{array}\tag{10.139}
$$

Meanwhile, the Hamiltonian Poisson commutes with the other two, $\{H,L\}=\{H,A\}=0$ which is just the statement that L and A are themselves conserved. 

The remainder of this Runge–Lenz section is a mathematical aside for those who know something about Lie groups. Little will be lost (at least at this stage) if you're not one of those people! 

There is often some group theory underlying the algebra of conserved quantities. For example, we mentioned previously that the algebra of angular momentum operators $\{L_{i}, L_{j}\} = \epsilon_{ijk} L_{k}$ is synonymous with the group of rotations $SO(3)$ . (More specifically, this coincides with the Lie algebra $so(3)$ where, by convention, algebras are written in lower case while groups are written in upper case.) We can ask: what is the group associated to the algebra (10.139)? 

The presence of the Hamiltonian H on the right-hand side of $(10.139)$ is interesting. By definition, H commutes with all other conserved quantities. For our purposes, it means that we may as well just replace the conserved Hamiltonian $H(\mathbf{x}, \mathbf{p})$ with its value E on a particular orbit. We then define the following linear combinations of L and A, 

$$
G _ {i} ^ {\pm} = \frac {1}{2} \left(L _ {i} \pm \sqrt {- \frac {m k}{2 E}} A _ {i}\right).\tag{10.140}
$$

It's straightforward to show that these disentangle the Poisson relations in (10.139), which now become 

$$
\{G _ {i} ^ {+}, G _ {j} ^ {+} \} = \epsilon_ {i j k} G _ {k} ^ {+}, \quad \{G _ {i} ^ {-}, G _ {j} ^ {-} \} = \epsilon_ {i j k} G _ {k} ^ {-}, \quad \{G _ {i} ^ {+}, G _ {j} ^ {-} \} = 0
$$

We see that we get two, decoupled $so(3)$ algebras. There's a quirky group-theoretic fact that $SO(3) \times SO(3) = SO(4)$ , so it's often said that the Kepler problem has a hidden $SO(4)$ symmetry. 

In fact there's one last subtlety hiding in this problem. That's the minus sign under the square-root in (10.140). Recall that there are two kinds of orbits in the Kepler problem. The closed, elliptic orbits have $E < 0$ . In this case, the generators $G_{i}^{\pm}$ are real, and the algebra does indeed describe a hidden $SO(4)$ symmetry. But for the hyperbolic orbits with $E > 0$ , the generators $G_{i}^{\pm}$ are complex. In this case, it's more accurate to say that the symmetry group is $SO(1,3)$ . These kind of subtle issues to do with the reality of various algebras won't raise their heads again until the book on Quantum Field Theory where we will discuss them in some more detail. 

## 10.4.3 Generating Functions

So far, we've learned that canonical transformations are interesting. In particular, any conserved quantity necessarily generates a canonical transformation. But we haven't yet given a way to construct canonical transformations other than to scrabble around and find a symplectic matrix obeying (10.111). 

The purpose of this brief section is to describe a more systematic way of constructing canonical transformations. This is largely for the sake of completeness; we won't actually use this method in anger in the rest of this book (nor, indeed, in any of the subsequent books). 

We want to construct canonical transformations between coordinates $(q^{i}, p_{i})$ and $(Q^{i}, P_{i})$ . The key idea is to consider a function that depends on one set of the new coordinates and one set of the old. For example, we could take the function $F(q, Q)$ , depending on the original $q^{i}$ and the final $Q^{i}$ . Let 

$$
p _ {i} = \frac {\partial F}{\partial q ^ {i}}.\tag{10.142}
$$

This gives us $p_i = p_i(q, Q)$ . After inverting, this equation can be thought of as defining the new coordinate $Q^i = Q^i(q, p)$ . But what is the new canonical momentum $P$ ? We'll show that it's given by 

$$
P _ {i} = - \frac {\partial F}{\partial Q ^ {i}}.\tag{10.143}
$$

The proof of this is a simple matter of playing with partial derivatives. Let's see how it works in an example with just a single degree of freedom. 

(It generalises trivially to the case of several degrees of freedom.) We can look at the Poisson bracket 

$$
\{Q, P \} = \left. \frac {\partial Q}{\partial q} \right| _ {p} \left. \frac {\partial P}{\partial p} \right| _ {q} - \left. \frac {\partial Q}{\partial p} \right| _ {q} \left. \frac {\partial P}{\partial q} \right| _ {p}\tag{10.144}
$$

where, for once, we're using the notation that stresses what variable we keep fixed when we differentiate. At this point we need to do the playing. Equation (10.143) defines $P = P(q, Q)$ , so we have 

$$
\left. \frac {\partial P}{\partial p} \right| _ {q} = \left. \frac {\partial P}{\partial Q} \right| _ {q} \left. \frac {\partial Q}{\partial p} \right| _ {q} \quad \text {and} \quad \left. \frac {\partial P}{\partial q} \right| _ {p} = \left. \frac {\partial P}{\partial q} \right| _ {Q} + \left. \frac {\partial P}{\partial Q} \right| _ {q} \left. \frac {\partial Q}{\partial q} \right| _ {p}.
$$

Inserting this into the Poisson bracket gives 

$$
\{Q, P \} = - \frac {\partial Q}{\partial p} \bigg | _ {q} \frac {\partial P}{\partial q} \bigg | _ {Q} = \left. \frac {\partial Q}{\partial p} \right| _ {q} \frac {\partial^ {2} F}{\partial q \partial Q} = \left. \frac {\partial Q}{\partial p} \right| _ {q} \frac {\partial p}{\partial Q} \bigg | _ {q} = 1
$$

as required. The function $F(q, Q)$ is known as a generating function of the first kind. 

There are three further types of generating function, related to the first by Legendre transforms. Each is a function of one of the original coordinates and one of the new coordinates. We then have 

$$
F _ {2} (q, P): \quad p _ {i} = \frac {\partial F _ {2}}{\partial q ^ {i}} \quad \text { and } \quad q ^ {i} = \frac {\partial F _ {2}}{\partial P _ {i}} .
$$

$$
F _ {3} (p, Q): \qquad q ^ {i} = - \frac {\partial F _ {3}}{\partial p _ {i}} \quad \mathrm{and} \quad P _ {i} = - \frac {\partial F _ {3}}{\partial q ^ {i}}.\tag{10.147}
$$

$$
F _ {4} (p, P): \qquad q ^ {i} = - \frac {\partial F _ {4}}{\partial p _ {i}} \quad \text { and } \quad q ^ {i} = \frac {\partial F _ {4}}{\partial P _ {i}} .
$$

You can check that each of these defines a canonical transformation. 

## 10.5 Action-Angle Variables

We've all tried to solve problems using the wrong coordinates and seen what a mess it can be. If you work in Cartesian coordinates when the problem really requires, say, spherical polar coordinates, then it's always possible to get to the right answer with enough perseverance, but you're really making life hard for yourself. The ability to change coordinate systems can drastically simplify a problem. 

Now we have a much larger set of transformations at hand; we can mix up $q$ s and $p$ s. An obvious question is: Is this useful for anything?! In other words, is there a natural choice of variables which makes solving a given problem much easier. In some cases, there is. They're called action-angle variables. 

## 10.5.1 The Harmonic Oscillator

We'll start this section by doing a simple example to illustrate the main point. We'll then move on to the more general theory. The example we choose is the harmonic oscillator. Notice that, as our theory gets more abstract, our examples get easier! 

We have the Hamiltonian 

$$
H = \frac {p ^ {2}}{2 m} + \frac {1}{2} m \omega^ {2} q ^ {2}\tag{10.148}
$$

so that Hamilton's equations are the familiar 

$$
\dot {p} = - m \omega^ {2} q \quad \mathrm{and} \quad \dot {q} = \frac {p}{m}.\tag{10.149}
$$

This has the solution 

$$
q = A \cos (\omega (t - t _ {0})) \quad \text { and } \quad p = - m \omega A \sin (\omega (t - t _ {0}))
$$

where A and $t_{0}$ are integration constants. The flows in phase space are ellipses, as shown in the figure. 

Now let's do a rather strange change of variables in which we use our freedom to mix up the position and momentum variables. We write 

$$
(q, p) \rightarrow (\theta , I)\tag{10.151}
$$

where you can think of $\theta$ is our new position coordinate and I our new momentum coordinate. The transformation we choose is: 

$$
q = \sqrt {\frac {2 I}{m \omega}} \sin \theta \quad \mathrm{and} \quad p = \sqrt {2 I m \omega} \cos \theta\tag{10.152}
$$

It's an odd choice, but it has advantages. Before we turn to these, let's spend a minute checking that this is indeed a canonical transformation. There's two ways to do this and we'll do both. 

The first way to check that (10.152) is canonical is to show that the Poisson brackets are preserved. In fact, it's easier to work backwards and check that $\{q,p\} = 1$ in $(\theta ,I)$ coordinates. In other words, we need to show that 

$$
\{q, p \} _ {(\theta , I)} \equiv \frac {\partial q}{\partial \theta} \frac {\partial p}{\partial I} - \frac {\partial q}{\partial I} \frac {\partial p}{\partial \theta} = 1.\tag{10.153}
$$

This is simple enough to check. From $(10.152)$ , we have 

$$
\{q, p \} _ {(\theta , I)} = 2 \left\{\sqrt {I} \sin \theta , \sqrt {I} \cos \theta \right\} _ {(\theta , I)} = 1\tag{10.154}
$$

where a couple of factors of $1/\sqrt{m\omega}$ and $\sqrt{m\omega}$ have cancelled and a quick differentiation is needed to get the final equality. So we see that the transformation (10.152) is indeed canonical. 

The second way to see that the transformation is canonical is to prove that the Jacobian is symplectic. We have 

$$
\mathcal {J} = \left( \begin{array}{c c} \partial \theta / \partial q & \partial \theta / \partial p \\ \partial I / \partial q & \partial I / \partial p \end{array} \right) = \left( \begin{array}{c c} (m \omega / p) \cos^ {2} \theta & - (m \omega q / p ^ {2}) \cos^ {2} \theta \\ m \omega q & p / m \omega \end{array} \right)
$$

From this it's a short calculation to check that $\mathcal{J}\Omega\mathcal{J}^T = \Omega$ , as required in (10.111). 

So we have a canonical transformation in (10.152). But what's the point of doing this? Let's look at the Hamiltonian in our new variables 

$$
H = \frac {1}{2 m} (2 m \omega I) \sin^ {2} \theta + \frac {1}{2} m \omega^ {2} \frac {2 I}{m \omega} \cos^ {2} \theta = \omega I.\tag{10}
$$

So the Hamiltonian doesn't depend on the variable $\theta!$ 

This means that Hamilton's equations read 

$$
\dot {\theta} = \frac {\partial H}{\partial I} = \omega
$$

$$
\mathrm{and} \dot {I} = - \frac {\partial H}{\partial \theta} = 0.
$$

The coordinate $I$ is conserved: it doesn't change with time. From the perspective of phase space, now parameterised by $\theta$ and $I$ , the flows have become straight lines, as shown in the figure. The coordinates $(\theta, I)$ are examples of action-angle variables, with $I$ the action variable, and $\theta$ the angle variable. 

Note that we've got two things called the action: the integral of the Lagrangian that we met back in Chapter 7, and now this new variable $I$ . They are not the same thing, although both have the dimensions of angular momentum. 

## 10.5.2 Briefly, Integrable Systems

For the harmonic oscillator, we can find a change of variables so that we can straighten out the flow lines in phase space and motion becomes trivial. Of course, we can also solve the harmonic oscillator in other ways! This whole story would be much more impressive if we could do it for more complicated problems. 

Here's the dream. Suppose that we have $n$ degrees of freedom. We would like to find canonical transformations to a collection of action-angle variables 

$$
(q ^ {i}, p _ {i}) \rightarrow (\theta_ {i}, I _ {i})\tag{10.156}
$$

such that the Hamiltonian becomes $H = H(I_1, \ldots, I_n)$ and doesn't depend on $\theta_i$ . If we can do this, then Hamilton's equations tell us that we have $n$ conserved quantities $I_i$ , while 

$$
\dot {\theta} _ {i} = \frac {\partial H}{\partial I _ {i}} = \omega_ {i}\tag{10.157}
$$

where the frequencies $\omega_{i}$ are independent of $\theta$ but in general depend on I. The solutions are then simply $\theta_{i} = \omega_{i}t$ . 

It turns out that such a transformation isn't possible in general. That would make things too easy! But there are rather special systems for which it is possible. These systems are known as integrable. They are the most solvable of classical mechanics systems, sitting at the opposite end of the spectrum from chaotic systems for which a solution is too far out of reach. 

Note that the question of whether action-angle variables exist is a global one. Locally you can always straighten out the flow lines; it's a question of whether you can tie these straight lines together globally without them getting tangled. 

Integrable systems are rare and precious objects. Most systems, it turns out, are very much not integrable. Clearly an integrable system with n degrees of freedom has n conserved quantities: these are the $I_{i}$ above. But the converse statement is also true: 

Liouville's Theorem on Integrable Systems: A system with $n$ degrees of freedom and $n$ , mutually Poisson-commuting, constants of motion $I_1, \ldots, I_n$ can be parameterised by action-angle variables. The requirement of Poisson-commuting, meaning $\{I_i, I_j\} = 0$ , is the statement that we can view the $I_i$ as canonical momentum variables. 

This result is known as Liouville's theorem. (Same Liouville, different theorem). We will not prove it here. 

Clearly the motion of a completely integrable system is restricted to lie on $I_{i} = \text{constant slices of the phase space}$ . A theorem in topology says that these surfaces must be tori, meaning that they take the form $T^{n} = S^{1} \times \ldots \times S^{1}$ . Each of these circles $S^{1}$ is labelled by one of the angle coordinates $\theta_{i}$ . The submanifold $T^{n}$ is known known as the invariant torus. 

## 10.5.3 Action-Angle Variables for One-Dimensional Systems

It's always possible to construct action-angle variables for a one-dimensional system. We start with the Hamiltonian 

$$
H = \frac {p ^ {2}}{2 m} + V (q).\tag{10.158}
$$

Obviously, H itself is a constant of motion, with H = E for some energy E which remains unchanged as the system evolves. This is enough to ensure that the system is integrable. 

We assume that the motion is bounded so that $q_{1} \leq q \leq q_{2}$ as shown in the figure. Then the motion is periodic, oscillating back and forth between the two end points, as shown in the figure to the right. The motion in phase space then looks something like the picture on the left in Figure 10.5. Our goal is to find a canonical transformation to variables $\theta$ and I that straightens out this flow to look like the picture on the right in Figure 10.5. 

Fig. 10.5 Can we straighten out the flow lines in phase space? 

So what are I and $\theta$ ? Since I is a constant of motion, it should be some function of the energy or, alternatively 

$$
H = H (I) = E.\tag{10.159}
$$

The challenge is to find a choice of I such that its canonical partner $\theta \in [0, 2\pi)$ satisfies 

$$
\dot {\theta} = \frac {\partial H}{\partial I} = \frac {\partial E}{\partial I} = \omega\tag{10.160}
$$

for a constant $\omega$ , the frequency of the orbit. 

Claim: The correct choice for I is 

$$
I = \frac {1}{2 \pi} \oint p d q.\tag{10.161}
$$

This is the area of phase space enclosed by an orbit (divided by $2\pi$ ) and is a function of the energy only. 

Proof: Since the Hamiltonian is conserved, we can write the momentum as a function of q and E: 

$$
p = \sqrt {2 m} \sqrt {E - V (q)}.\tag{10.162}
$$

For this simple system, the momentum takes the form that we learned in high school, $p = m\dot{q}$ . We then have 

$$
d t = \sqrt {\frac {m}{2}} \frac {d q}{\sqrt {E - V (q)}}.\tag{10.163}
$$

Integrating over a single orbit with period $T = 2\pi/\omega$ gives 

$$
\begin{array}{r l} & {\frac {2 \pi}{\omega} = \sqrt {\frac {m}{2}} \oint \frac {d q}{\sqrt {E - V (q)}}} \\ & {\quad = \sqrt {2 m} \oint \left(\frac {d}{d E} \sqrt {E - V (q)}\right) d q.} \end{array}\tag{10.164}
$$

At this point we do something slippery: we take the differentiation $d / dE$ outside the integral. It isn't immediately obvious that this is a valid step because the path around which the integral is evaluated itself changes with energy $E$ . We'll soon show that this doesn't matter. But, for now, we assume that it's valid and continue. This then gives what we need: 

$$
\frac {2 \pi}{\omega} = \frac {d}{d E} \oint \sqrt {2 m} \sqrt {E - V (q)} d q = \frac {d}{d E} \oint p d q = 2 \pi \frac {d I}{d E}
$$

where, in the final equality, we've substituted for our putative action variable $I$ . The upshot is that our action variable $I$ , defined in (10.161) obeys 

$$
\frac {d E}{d I} = \omega\tag{10.166}
$$

where $\omega$ is the frequency of the orbit. This is our desired result. 

It still remains to show that we didn't miss anything by taking $d / dE$ outside the integral. Let's think about this. We want to see how the area enclosed by the curve changes under a small shift in energy $\delta E$ . Both the curve itself and the end points $q_{1} \leq q \leq q_{2}$ vary as the energy shifts. The latter changes by $\delta q^{i} = (dV(q^{i}) / dq)^{-1} \delta E$ . 

Allowing the differential $d / dE$ to wander inside and outside the integral is tantamount to neglecting the change in the end points. The piece that we've missed is the small white region in the figure. But these pieces are of order $\delta E^2$ . To see this, note that order $\delta E$ pieces are given by 

$$
\begin{array}{l} \int_ {q ^ {i} + \delta q ^ {i}} ^ {q ^ {i}} \sqrt {2 m} \sqrt {E - V (q)} d q \\ \approx \sqrt {2 m} \sqrt {E - V (q)} \left(\frac {\partial V}{\partial q}\right) ^ {- 1} \delta E \end{array}
$$

evaluated at the end point $q = q^{i}$ . They vanish because $E = V(q^{i})$ at the end points. This completes the proof. 

□ 

This tells us that we can calculate the period of the orbit $T = 2\pi/\omega$ by figuring out the area enclosed by the orbit in phase space as a function of the energy. We can do this without ever having to work out the angle variable $\theta$ , which satisfies $\theta = \omega t$ . In general, $\theta$ will be a complicated function of q and p. 

In fact, it's not too hard to get an expression for $\theta$ by going over the above analysis for a small part of the period. It follows from the above proof that 

$$
t = \frac {d}{d E} \int p d q.\tag{10.167}
$$

We want an angle $\theta$ that evolves as $\theta = \omega t$ . We can achieve this by taking the choice 

$$
\theta = \omega \frac {d}{d E} \int p d q = \frac {d E}{d I} \frac {d}{d E} \int p d q = \frac {d}{d I} \int p d q.\tag{10.]}
$$

This is our angle variable. 

## 10.5.4 Action-Angle Variables for Higher-Dimensional Systems

All one-dimensional systems of the form (10.158) are integrable by dint of the conserved energy. As we mentioned above, we are usually not so lucky for higher dimensional systems. However, when they are integrable the action variables take the same form as in one dimension: they are the integrals over cycles in phase space 

$$
I _ {i} = \frac {1}{2 \pi} \oint_ {\gamma_ {i}} \sum_ {j} p _ {j} d q ^ {j}\tag{10.169}
$$

where each integral is to be taken over a complete orbit $\gamma_{i}$ in phase space. These $\gamma_{i}$ are the circles $S^{1} \subset T^{n}$ that live inside the invariant torus. The corresponding angle variable is then 

$$
\theta_ {i} = \frac {\partial}{\partial I _ {i}} \int_ {\gamma_ {i}} \sum_ {j} p _ {j} d q ^ {j}.\tag{10.170}
$$

## Action-Angle Variables for the Kepler Problem

An example of a higher-dimensional integrable system is the Kepler problem. This should come as no surprise since integrable systems are typically ones that we can solve and we solved this back in Chapter 5. 

The Kepler problem describes a particle of mass m moving in three dimensions, subject to the potential 

$$
V (\mathbf {r}) = - \frac {k}{r}.\tag{10.171}
$$

Recall that the first step to solving any central force problem is to use the conservation of the (direction of) angular momentum to restrict 

dynamics to a two-dimensional plane. Working in polar coordinates $(r, \phi)$ in this spatial plane, the associated momenta are 

$$
p _ {r} = m \dot {r} \quad \mathrm{and} \quad p _ {\phi} = m r ^ {2} \dot {\phi} .\tag{10.172}
$$

The Hamiltonian for the Kepler problem is 

$$
H = \frac {1}{2 m} p _ {r} ^ {2} + \frac {1}{2 m r ^ {2}} p _ {\phi} ^ {2} - \frac {k}{r}.\tag{10.173}
$$

There are two action variables, one associated to the radial motion and one associated to the angular motion. The latter is straightforward: it is the angular momentum itself 

$$
I _ {\phi} = \frac {1}{2 \pi} \int_ {0} ^ {2 \pi} p _ {\phi} d \phi = p _ {\phi}.\tag{10.174}
$$

The action variable for the radial motion is more interesting. We can calculate it by using the fact that the total energy E and the angular momentum $I_{\phi}$ are both conserved. Then, rearranging (10.173), we have 

$$
p _ {r} ^ {2} = 2 m \left(E + \frac {k}{r}\right) - \frac {I _ {\phi} ^ {2}}{r ^ {2}}\tag{10.175}
$$

and the action variable is 

$$
\begin{array}{l} I _ {r} = \frac {1}{2 \pi} \oint p _ {r} d r = \frac {1}{2 \pi} 2 \int_ {r _ {\min}} ^ {r _ {\max}} p _ {r} d r \\ = \frac {1}{2 \pi} 2 \int_ {r _ {\min}} ^ {r _ {\max}} \sqrt {2 m \left(E + \frac {k}{r}\right) - \frac {I _ {\phi} ^ {2}}{r ^ {2}}} d r. \end{array}\tag{10.176}
$$

Here $r_{min}$ and $r_{max}$ are, respectively, the closest and furthest distance to the origin, also known as the periapsis and apoapsis. These sit at opposite points on the orbit. The factor of 2 in the second equality then comes because a complete cycle goes from $r_{min}$ to $r_{max}$ and back again. To do this integral, we need the result 

$$
\int_ {r _ {\mathrm{min}}} ^ {r _ {\mathrm{max}}} d r \sqrt {\left(1 - \frac {r _ {\mathrm{min}}}{r}\right) \left(\frac {r _ {\mathrm{max}}}{r} - 1\right)} = \frac {\pi}{2} \left(r _ {\mathrm{min}} + r _ {\mathrm{max}}\right) - \pi \sqrt {r _ {\mathrm{min}} r _ {\mathrm{n}}}
$$

Using this, we find 

$$
I _ {r} = \sqrt {\frac {m}{2 | E |}} k - I _ {\phi}.\tag{10.177}
$$

Or, rearranging 

$$
E = - \frac {m k ^ {2}}{2 (I _ {r} + I _ {\phi}) ^ {2}}.\tag{10.178}
$$

There's something rather nice lurking in this result, which can be traced to the fact that the energy is symmetric in $I_r$ and $I_\phi$ . (This, it turns out, is not usually the case for integrable systems.) The Hamiltonian is the same as the energy and we can use it to compute the speed at which the angular variables change. This follows from Hamilton's equations 

$$
\dot {\theta} _ {r} = \frac {\partial H}{\partial I _ {r}} \quad \text { and } \quad \dot {\theta} _ {\phi} = \frac {\partial H}{\partial I _ {\phi}} .\tag{10.179}
$$

Here $\theta_{\phi} = \phi$ while $\theta_r$ is some complicated function of $r$ . But we see from (10.178) that the Hamiltonian is symmetric in $I_r$ and $I_{\phi}$ . This means that the frequency at which the particle completes a $\phi$ cycle is the same as the frequency at which it completes a $\theta_r$ cycle. But that's the statement that the orbit is closed: when you go around $2\pi$ in space, you come back to the same $r$ value. The existence of closed orbits is a unique feature of the $1/r$ potential. We saw in Chapter 5 that the existence of closed orbits could be understood using the Runge–Lenz vector. Here we see another explanation in terms of action-angle variables. 

## 10.6 Adiabatic Invariants

Consider a one-dimensional system with a potential $V(q; \lambda)$ that depends on some external parameter $\lambda$ . If the motion is bounded by the potential then it is necessarily periodic. We want to ask what happens if we slowly change $\lambda$ over time. For example, we may slowly change the length of a pendulum, or the frequency of the harmonic oscillator. 

This is a situation where the Hamiltonian depends explicitly on time. This means that energy will not be conserved. Instead, we have 

$$
\dot {E} = \frac {\partial H}{\partial \lambda} \dot {\lambda}.\tag{10.180}
$$

That looks bad for us. Much of the progress that we've made in classical mechanics has been through finding conserved quantities, and energy is paramount among them. 

Happily, all is not lost. If the parameter $\lambda$ changes only slowly in time, then it turns out that there is a combination of $E$ and $\lambda$ that remains (at least approximately) constant. Combinations like this are called adiabatic invariants and the purpose of this section is to find them. In fact, as we'll see, the adiabatic invariants are precisely the action variables that we met in the previous section. 

For the 1d system, the Hamiltonian is 

$$
H = \frac {p ^ {2}}{2 m} + V (q; \lambda (t)).\tag{10.181}
$$

I (and many before me) claim that the adiabatic invariant is 

$$
I = \frac {1}{2 \pi} \oint p d q.\tag{10.182}
$$

One slight novelty is that we must integrate over a path in phase space given by $(10.162)$ , 

$$
p = \sqrt {2 m} \sqrt {E (t) - V (q ; \lambda (t))}.\tag{10.183}
$$

But, because of that $\lambda(t)$ dependence, the path itself depends on time. We'll see the implications of this in the process of showing that $I$ is an adiabatic invariant. Along the way, we'll also see what it means for $\lambda$ to vary "slowly". 

We start by thinking of the action variable I as a function of the energy E and the parameter $\lambda$ , so $I = I(E, \lambda)$ . As we vary either of these, I will change. We have, 

$$
\dot {I} = \left. \frac {\partial I}{\partial E} \right| _ {\lambda} \dot {E} + \left. \frac {\partial I}{\partial \lambda} \right| _ {E} \dot {\lambda}.\tag{10.184}
$$

For an arbitrary variation of E and $\lambda$ , this equation tells us that I also changes. But, of course, E and $\lambda$ do not change arbitrarily: they are related by (10.180). The point of the adiabatic invariant is that when $\dot{E}$ and $\dot{\lambda}$ are related in this way, the two terms in (10.184) approximately cancel out. Our task is to show this. 

We deal with each of these terms in $(10.184)$ in turn. For the first term we need $\partial E/\partial I = \omega$ (a result that we previously derived in $(10.166)$ ). Or, equivalently, 

$$
\left. \frac {\partial I}{\partial E} \right| _ {\lambda} = \frac {1}{\omega (\lambda)} = \frac {T (\lambda)}{2 \pi}\tag{10.185}
$$

where $T(\lambda)$ is the period of the system evaluated at fixed $\lambda$ . 

The second term in $(10.184)$ tells us how the path changes as $\lambda$ is varied. Two possible paths, for two different values of $\lambda$ , are shown in Figure 10.6. The change in I is the change in the area under the two curves. We have 

$$
\begin{array}{c} \frac {\partial I}{\partial \lambda} \Big | _ {E} = \frac {1}{2 \pi} \left. \frac {\partial I}{\partial \lambda} \right| _ {E} \oint p d q = \frac {1}{2 \pi} \oint \left. \frac {\partial p}{\partial \lambda} \right| _ {E} d q \\ = \frac {1}{2 \pi} \int_ {0} ^ {T (\lambda)} \left. \frac {\partial p}{\partial \lambda} \right| _ {E} \left. \frac {\partial H}{\partial p} \right| _ {\lambda} d t ^ {\prime} \end{array}\tag{10.186}
$$

where, in the second equality, we have neglected a contribution arising from the fact that the path around which we integrate changes as $\lambda$ changes. But this contribution can be safely ignored by the same 

argument given in Section 10.5.3 when discussing action-angle variables for a one-dimensional system. 

Fig. 10.6 Two paths in phase space, one with fixed parameter $\lambda_{1}$ and the other with fixed $\lambda_{2}$ . 

Next, we need an expression for the product of partial derivatives in $(10.186)$ . We get this by differentiating the Hamiltonian and remembering what depends on what. We have the expression $H(q,p,\lambda)=E$ and we can think of p as depending on $\lambda$ . Then, keeping E and q fixed, we have 

$$
\left. \frac {\partial H}{\partial \lambda} \right| _ {p} + \left. \frac {\partial H}{\partial p} \right| _ {\lambda} \left. \frac {\partial p}{\partial \lambda} \right| _ {E} = 0.\tag{10.187}
$$

So substituting this into $(10.186)$ we have 

$$
\left. \frac {\partial I}{\partial \lambda} \right| _ {E} = - \frac {1}{2 \pi} \int_ {0} ^ {T (\lambda)} \left. \frac {\partial H}{\partial \lambda} \right| _ {E} d t ^ {\prime}.\tag{10.188}
$$

Now we can put it all together. Substituting $(10.180)$ , $(10.185)$ , and $(10.188)$ into the expression $(10.184)$ , we find that the time variation of I is given by 

$$
\dot {I} = \left[ T (\lambda) \left. \frac {\partial H}{\partial \lambda} \right| _ {E} - \left(\int_ {0} ^ {T (\lambda)} \left. \frac {\partial H}{\partial \lambda} \right| _ {E} d t ^ {\prime}\right) \right] \frac {\dot {\lambda}}{2 \pi}.\tag{10.1}
$$

So far, each term on the right-hand side is evaluated at a given time $t$ or, correspondingly, for a given $\lambda(t)$ . The two terms look similar, but they don't cancel! But we have yet to make use of the fact that the change in $\lambda$ is slow. At this point we can clarify what we mean by this. The basic idea is that the speed at which the particle bounces backwards and forwards in the potential is much faster than the speed at which $\lambda$ changes. This means that the particle has performed many periods before it notices any appreciable change in the potential. Mathematically, if we compute averaged quantities over a single period, defined by 

$$
\langle A (\lambda) \rangle = \frac {1}{T} \int_ {0} ^ {T} A (t, \lambda) d t\tag{10.190}
$$

then we may treat $\lambda$ as if it is effectively constant inside the integral. 

Now we can return to the variation of I and look at the time-averaged motion $\langle\dot{I}\rangle$ . If we assume that $\lambda$ can be taken to be constant over a single period, then the two terms in (10.189) do now cancel. We have 

$$
\langle \dot {I} \rangle = 0.\tag{10.191}
$$

This is the statement that I is an adiabatic invariant: for slow changes in $\lambda$ , the averaged value of I remains constant. 

We'll look at some examples and applications of adiabatic invariants shortly. But, first, some historical comments. The adiabatic invariants played an important role in the early history of quantum mechanics. Before Heisenberg and Schrödinger made their mark, there were ideas floating around that various things should be quantised. 

One suggestion, due to Bohr and Sommerfeld, is that the quantity 

$$
\frac {1}{2 \pi} \oint p d q = n \hbar\tag{10.192}
$$

should be quantised in units of $\hbar$ , with $n \in Z$ . This is known as Bohr–Sommerfeld quantisation. 

It is a heuristic approach to quantum mechanics that sometimes gives something close to the right answer. (It turns out that it does annoyingly well for the hydrogen atom, less well for other systems.) 

The problem with insisting that something takes integer values is that integers can't change continuously. So the thing that you're postulating to be an integer better not change either. That tallies nicely with the fact that $\oint p dq$ is an adiabatic invariant so doesn't vary if some underlying parameter changes in time, provided at least that the change is slow. 

This idea first reared its head in the 1911 Solvay conference. Lorentz complained that the proposed quantisation law $E = \hbar n\omega$ between energy 

$E$ and frequency $\omega$ was difficult to maintain when the frequency varies in time. Einstein offered the rebuttal: $E / \omega$ doesn't change. 

## An Example: The Pendulum

We can illustrate the adiabatic invariant for a pendulum. For small oscillations, the Hamiltonian is 

$$
H = \frac {p _ {\theta} ^ {2}}{2 m L ^ {2}} + \frac {1}{2} m g L \theta^ {2}\tag{10.193}
$$

where L is the length of the pendulum, and m the mass of the weight on the end. The adiabatic invariant is given by 

$$
I = \frac {1}{2 \pi} \oint p _ {\theta} d \theta = \frac {\sqrt {2 m L ^ {2}}}{2 \pi} \oint \sqrt {E - \frac {1}{2} m g L \theta^ {2}} d \theta .\tag{10}
$$

Here the energy is given by $E = \frac{1}{2}mgL\theta_{0}^{2}$ where $\theta_{0}$ is the maximum angle that the pendulum reaches. Ignoring overall constants, the adiabatic invariant is 

$$
I \sim \sqrt {\frac {L}{g}} E \sim m g ^ {1 / 2} L ^ {3 / 2} \theta_ {0} ^ {2}.\tag{10.195}
$$

From this, we can read off some straightforward physics. Suppose that we slowly decrease the length L of the pendulum. What happens? We know that I must remain constant, which means that the maximum angle $\theta_{0}$ necessarily increases as $\theta_{0} \sim 1/L^{3/4}$ . Although the angle increases, the linear amplitude of the swing is given by $L\theta_{0} \sim L^{1/4}$ and that decreases. Finally, the period of the swing is 

$$
T = \frac {\partial I}{\partial E} \sim \sqrt {\frac {L}{g}}\tag{10.196}
$$

and we see that T decreases. 

## Another Example: The Kepler Problem

We already computed the action variables for the Kepler problem in Section 10.5.4. For a potential $V(r) = -k / r$ , we have (10.178) 

$$
E = - \frac {m k ^ {2}}{2 (I _ {r} + I _ {\phi}) ^ {2}}.\tag{10.197}
$$

Let's be more concrete. We could consider a planet orbiting some star of mass $M$ . The parameter $k$ in the potential is proportional to this mass $k \sim M$ . Now suppose that the star slowly loses mass due to a stellar wind. Because $I_r$ and $I_\phi$ are adiabatic invariants, we learn that the planet loses energy as $E \sim -M^2$ . 

## Adiabatic Invariants and Liouville's Theorem

There is a heuristic way to think of adiabatic invariants using Liouville's theorem. Consider first a series of systems, all described by a 

Hamiltonian with fixed parameter $\lambda$ . We set off each system with the same energy $E$ or, equivalently, the same action $I$ , but we start them with slightly different phases $\theta$ . This means that their dynamics is described by a series of dots, all chasing each other around a fixed curve as shown in the figure. As we've seen, $I$ is the area contained within this curve. 

Now let's think about how this train of dots evolves under the Hamiltonian with time-dependent $\lambda(t)$ . Recall that Liouville's theorem states that the area of phase space is invariant under any Hamiltonian evolution. This holds whether or not $\partial H / \partial t = 0$ , so it is still valid for the time-dependent Hamiltonian with $\lambda(t)$ . One might be tempted to say that we're done since all the words sound right: Liouville's theorem implies that the area is conserved which is also the statement that our adiabatic invariant $I$ doesn't change with time. 

But this is a little too fast! Liouville's theorem says the area of a distribution of particles in phase space is conserved, not the area enclosed by a perimeter ring of particles. Indeed, Liouville's theorem holds for any variation $\lambda(t)$ , not just for adiabatic variations. For a fast change of $\lambda(t)$ , there is nothing to ensure that the particles that had the same initial energy, but different phases, would have the same final energy and we lose the interpretation of a ring of dots in phase space enclosing some area. 

The missing ingredient is the adiabatic principle. In this context it states that, for a suitably slow change of the parameter $\lambda$ , all the systems in the same orbit, with the same energy, are affected in the same manner. If this holds then, after some time, the dots in phase space will still be chasing each other around another curve of constant energy $E'$ . We can now think of a distribution of particles filling the area $I$ inside the curve. As $\lambda$ varies slowly, the area doesn't change and the outer particles remain the outer particles, all with the same energy. Under these circumstances, Liouville's theorem implies that the adiabatic invariant $I$ is constant in time. 

## 10.6.1 A Particle in a Magnetic Field

We've met the problem of a particle moving in a constant magnetic field several times in this book. If the particle has mass $m$ and electric charge $q$ , and the magnetic field is $\mathbf{B} = (0, 0, B)$ , then the particle traces circles in the $(x, y)$ -plane with cyclotron frequency 

$$
\omega = \frac {q B}{m}.\tag{10.198}
$$

The radius of the circle R is an integration constant. 

Now we ask: what happens if B varies slowly over space? Here, “slow” means that as an particle completes an orbit, the magnetic field remains almost, but not quite, constant. Mathematically, this means that 

$$
| \nabla B | \ll \frac {B}{R}.\tag{10.199}
$$

We will see that the particle continues to perform its small cyclotron orbits, now accompanied by a drift along lines of constant B. 

First, we'll suppose that the particle has $\dot{z} = 0$ , so that it moves only in the $(x, y)$ -plane. The solution in a constant magnetic field is 

$$
x = x _ {0} + R \cos (\omega t) \quad \text { and } \quad y = y _ {0} + R \sin (\omega t) .\tag{10.20}
$$

For a slowly varying magnetic field, we may expect that the solution can be approximated by simply endowing the parameters $x_{0}$ , $y_{0}$ , R, and $\omega$ with some time dependence. We will see that this is indeed the case, but that only $x_{0}$ and $y_{0}$ become functions of time: both R and $\omega$ remain constant. 

To see this, we can first compute the energy. In this example, there's no explicit time dependence so we know that the energy is an exact constant of motion. Evaluated on the constant solution (10.200) 

$$
E = \frac {1}{2} m \omega^ {2} R ^ {2} = \frac {q ^ {2} R ^ {2} B ^ {2}}{2 m}.\tag{10.201}
$$

Now suppose that we had the situation with spatially varying B. We could evaluate this again on the approximate solution in which the parameters in $(10.200)$ are time dependent. This would result in additional terms, proportional to $\dot{x}_{0}$ and $\dot{R}$ and so on. But these will be much smaller than the term $(10.201)$ . 

We learn that, to leading order, the combination $R^{2}B^{2}$ should be constant. So, for example, the particle could drift to a region with higher magnetic field, but to compensate it should reduce the radius of its orbit. 

To see what actually happens, we next compute the adiabatic invariant. This is 

$$
I = \frac {1}{2 \pi} \oint p d q = \frac {1}{2 \pi} \int_ {0} ^ {T} (p _ {x} \dot {x} + p _ {y} \dot {y}) d t\tag{10.202}
$$

which is to be thought of as a line integral along the orbit of the electron. If we work in the gauge $\mathbf{A} = (-By, 0, 0)$ , then the momenta are given by (see (7.178)) $p_{x} = m\dot{x} - qBy$ and $p_{y} = m\dot{y}$ . Evaluated on the constant solution (10.200), the adiabatic invariant is 

$$
\begin{array}{l} {I = \frac {1}{2 \pi} \int_ {0} ^ {T} \left(m \omega^ {2} R ^ {2} + q B y _ {0} \omega R \sin (\omega t) + q B R ^ {2} \omega \sin^ {2} (\omega t)\right) d t} \\ {= \frac {m \omega R ^ {2}}{2 \pi} \int_ {0} ^ {2 \pi} (1 + \sin^ {2} \theta) d \theta .} \end{array}
$$

The remaining integral just gives a constant. The all-important fact is that the adiabatic invariant scales as $I \sim BR^2$ . Taken together with the conserved energy, which scales as $E \sim B^2 R^2$ , we see that both $B$ and $R$ must remain constant. This is the statement that the particle can't move into regions of higher or lower magnetic field: it is consigned to drift along lines of constant magnetic field. 

There's a simple physical way to understand the drift of the particle. Suppose that $B$ is constant in the $x$ -direction, but increases in the $y$ -direction. This means that the particle feels a slightly stronger Lorentz force at the top of its orbit that at the bottom. Because the particle has a velocity in the x-direction at these moments, one might naively think that the imbalance in the Lorentz force law $F = qv \times B$ acts to accelerate the particle in the y-direction. But the adiabatic invariant means that isn't possible. Instead, the slow drift of the particle in the x-direction creates a compensating small force, keeping the particle on constant field lines. 

There's a slight variant of this set-up which allows charged particles to be trapped by magnetic fields. Consider the particle making its little circles in the $(x, y)$ -plane, but now also moving in the $z$ -direction. This time we'll take a magnetic field that varies in the $z$ -direction. The energy of the particle is 

$$
E = \frac {1}{2} m \dot {\mathbf {x}} ^ {2} = \frac {q ^ {2} R ^ {2} B ^ {2}}{2 m} + \frac {1}{2} m \dot {z} ^ {2}.\tag{10.204}
$$

The first term in $(10.204)$ is proportional to IB. Both E > 0 and I > 0 are constant in time. So if B is increasing in the z-direction, then there is necessarily a value of B > 0 at which we must have $\dot{z} = 0$ . This means that a particle moving in the z-direction must stop and turn around at this point. By creating a magnetic field that increases at two ends, charged particles can be made to bounce back and forth in the z-direction, while executing circular motion in the $(x, y)$ -plane. This is known as a magnetic bottle. It is this mechanism that traps charged particles in magnetic loops emitted from the Sun. 

## 10.7 The Hamilton-Jacobi Equation

In this section we will describe yet another viewpoint on classical dynamics, known as Hamilton–Jacobi theory. It will tie together several concepts that we’ve met so far. 

We start, as in Chapter 7, with the principle of least action. The action is defined by 

$$
S = \int_ {0} ^ {T} L (q ^ {i}, \dot {q} ^ {i}, t) d t\tag{10.205}
$$

and is evaluated on all paths $q(t)$ with fixed end points 

$$
q ^ {i} (0) = q _ {\mathrm{initial}} ^ {i} \quad \mathrm{and} \quad q ^ {i} (T) = q _ {\mathrm{final}} ^ {i}.\tag{10.206}
$$

Famously, the true path taken is an extremum of the action, meaning $\delta S = 0$ . 

Now let's change perspective a little. We consider the value of the action evaluated on the true path $q_{\mathrm{classical}}^{i}(t)$ that obeys the Euler-Lagrange equation of motion. We write 

$$
W (q _ {\mathrm{initial}} ^ {i}, q _ {\mathrm{final}} ^ {i}, T) = S [ q _ {\mathrm{classical}} ^ {i} (t) ].\tag{10.207}
$$

(Those lengthy subscripts are ugly, but they won't be with us for long!) While $S$ is a functional of any path, $W$ is to be considered to be a function of the initial and final configurations $q_{\text{initial}}^i$ and $q_{\text{final}}^i$ as well as the time $T$ it takes to get between them. The object $W$ is sometimes called the on-shell action, where “on-shell” is a slightly silly name meaning “evaluated on the solution to the equation of motion”. We'll see that this on-shell action has some nice properties. 

First, we ask what happens if we keep $q_{initial}^{i}$ fixed but vary the end point $q_{final}^{i}$ . We can go back to the analysis of Chapter 7 to see what happens when the action is varied. We get 

$$
\delta S = \int_ {0} ^ {T} d t \left[ \frac {\partial L}{\partial q ^ {i}} - \frac {d}{d t} \left(\frac {\partial L}{\partial \dot {q} ^ {i}}\right) \right] \delta q ^ {i} (t) + \left[ \frac {\partial L}{\partial \dot {q} ^ {i}} \delta q ^ {i} (t) \right] _ {0} ^ {T}.
$$

If we evaluate this on the true classical path, then the first term vanishes. We're left with 

$$
\frac {\partial W}{\partial q _ {\mathrm{final}} ^ {i}} = \left. \frac {\partial L}{\partial \dot {q} ^ {i}} \right| _ {t = T} = p _ {i} ^ {\mathrm{final}}.\tag{10.209}
$$

We see that if we differentiate the on-shell action with respect to the final position, then we get the final momentum. Note that there's been a change of perspective above. In Chapter 7, we discarded the second term in (10.208) but kept the first term to derive the Euler–Lagrange equations. Now, we reverse the strategy and we discard the first term, on the 

grounds that the path obeys the classical equation of motion, and focus on the second. 

Next, we compute $\partial W / \partial T$ . We start by considering a classical path with fixed initial configuration $q_{\mathrm{initial}}^i$ . We'll let the path run on a little longer than before, so $T \to T + \delta T$ . Then we have 

$$
\frac {d W}{d T} = \frac {\partial W}{\partial T} + \frac {\partial W}{\partial q _ {\mathrm{final}} ^ {i}} \dot {q} _ {\mathrm{final}} ^ {i} = \frac {\partial W}{\partial T} + p _ {i} ^ {\mathrm{final}} \dot {q} _ {\mathrm{final}} ^ {i}.\tag{10.21}
$$

But this total derivative is easily calculated since $dS/dT = L$ , or 

$$
\frac {d W}{d T} = L (q _ {\mathrm{classical}} ^ {i} (T), \dot {q} _ {\mathrm{classical}} ^ {i} (T), T) = L (q _ {\mathrm{final}} ^ {i}, \dot {q} _ {\mathrm{final}} ^ {i}, T).
$$

We arrive at the equation, 

$$
\frac {\partial W}{\partial T} = - \left(p _ {i} ^ {\mathrm{final}} \dot {q} _ {\mathrm{final}} ^ {i} - L (q _ {\mathrm{final}} ^ {i}, \dot {q} _ {\mathrm{final}} ^ {i}, T)\right) = - H (q _ {\mathrm{final}} ^ {i}, p _ {i} ^ {\mathrm{final}}, T)
$$

At this stage, the only time in the game is T and the only position in the game is $q_{final}^{i}$ . So we can simply drop the word “final”, and relabel $T \rightarrow t$ . We have found ourselves a time-dependent function on configuration space $W = W(q^{i}, t)$ that satisfies 

$$
\frac {\partial W}{\partial q ^ {i}} = p _ {i} \quad \text { and } \quad \frac {\partial W}{\partial t} = - H (q ^ {i}, p _ {i}, t)\tag{10.213}
$$

or, substituting the first into the second, we have 

$$
\frac {\partial W}{\partial t} = - H (q ^ {i}, \partial W / \partial q ^ {i}, t).\tag{10.214}
$$

This is the Hamilton–Jacobi equation. 

We've shown how a solution to the Hamilton-Jacobi equation can be constructed by looking at the classical action of paths which reach a point $q^i$ at time $T$ , starting from some initial reference point $q_{\text{initial}}^i$ . The coordinates of the starting point $q_{\text{initial}}^i$ can be considered integration constants. In fact, there are more general solutions to the Hamilton-Jacobi equation, although all are related to the classical action in a similar way. 

Suppose that we find a solution to (10.214). What do we do with it? We're now armed with some time-dependent function $W(q^i, t)$ on configuration space. We combine this with the first of Hamilton's equations which reads 

$$
\dot {q} ^ {i} = \left. \frac {\partial H}{\partial p _ {i}} \right| _ {p _ {i} = \partial W / \partial q ^ {i}}\tag{10.215}
$$

where, on the right-hand side, we've replaced every appearance of the momenta $p_i$ by a function of the coordinates using $p_i = \partial W / \partial q^i$ . What we're left with is $n$ first order differential equations for the evolution of $q^i$ . In this manner, the function $W$ determines the path of the classical system: start the system off at a point in configuration space and $W$ can be considered as a real-valued classical wavefunction which tells it how to evolve. 

What we need to show is that the evolution dictated by $(10.215)$ does indeed satisfy the equations of motion. In other words, we should prove that the second of Hamilton's equations, $\dot{p}_{i} = -\partial H/\partial q^{i}$ , is satisfied. We have 

$$
\dot {p} _ {i} = \frac {d}{d t} \left(\frac {\partial W}{\partial q ^ {i}}\right) = \frac {\partial^ {2} W}{\partial q ^ {i} \partial q ^ {j}} \dot {q} ^ {j} + \frac {\partial^ {2} W}{\partial t \partial q ^ {i}}.\tag{10.216}
$$

But differentiating the Hamilton–Jacobi equation (10.214) with respect to $q^{i}$ , we see that we can rewrite the right-hand side of this equation using 

$$
\frac {\partial^ {2} W}{\partial t \partial q ^ {i}} = - \frac {\partial H}{\partial q ^ {i}} - \frac {\partial H}{\partial p _ {j}} \frac {\partial^ {2} W}{\partial q ^ {i} \partial q ^ {j}} = - \frac {\partial H}{\partial q ^ {i}} - \dot {q} ^ {j} \frac {\partial^ {2} W}{\partial q ^ {i} \partial q ^ {j}}\tag{10}
$$

so that (10.216) becomes $\dot{p}_i = -\partial H / \partial q^i$ as required. 

Let's see what we've done. We're used to dealing with second order differential equations for the time evolution on configuration space (the Euler-Lagrange equations) and first order differential equations for time evolution on phase space (Hamilton's equations). But the Hamilton–Jacobi approach allows us to incorporate n of the integration constants in the function $W(q^{i}, t)$ so that we're left solely with first order differential equations on configuration space given by $(10.215)$ . 

When we have conservation of energy, so $\partial H/\partial t = 0$ , there is solution of the Hamilton–Jacobi equation of a particularly simple form. We write 

$$
W (q ^ {i}, t) = W ^ {0} (q ^ {i}) - E t\tag{10.218}
$$

for some constant E. Then the time dependence drops out and we get the equation 

$$
H (q ^ {i}, \partial W ^ {0} / \partial q ^ {i}) = E.\tag{10.219}
$$

The function $W^0$ is known as Hamilton's principal function. 

The special property of this solution to the 

Hamilton–Jacobi equation is that every path in configuration space determined by the function $W_{0}$ has the same energy E. 

With a little thought, we can envisage how to construct solutions to $(10.219)$ . Start with a co-dimension one surface in configuration space which we will specify to be a surface of constant $W_{0}$ . (Co-dimension one means that the surface has dimension $(n - 1)$ . Such a surface splits the configuration space in two.) At any point on this surface, the potential energy $V(q)$ is determined. Since $p_{i} = \partial W_{0}/\partial q^{i}$ , the momentum is perpendicular to the surface and in the direction of increasing $W_{0}$ . Its magnitude is fixed by requiring that the total energy is E. But this magnitude then tells us the position of the next surface of constant $W_{0}$ (with incremental increase). 

In multi-dimensional configuration spaces, there are many solutions to $(10.219)$ . Moreover, something singular happens to $W_{0}$ in regions where $V(q^{i}) = 0$ . 

## 10.7.1 Action and Angles from Hamilton–Jacobi

For the majority of examples the Hamilton–Jacobi approach doesn’t give a particularly useful way for solving a problem. It’s utility really lies in the structure it reveals about classical dynamics. So rather than go through the gymnastics of solving a complicated problem using this method, let us focus on a rather simple example which illustrates connections between the different ideas we’ve seen. 

A system with a single degree of freedom has Hamiltonian 

$$
H = \frac {p ^ {2}}{2 m} + V (q) .\tag{10.220}
$$

Energy is conserved and the solution to the Hamilton–Jacobi equation has a single integration constant, let's call it $\beta$ , which is necessarily some function of the energy. 

In the above discussion we were a little lax about showing these integration constants explicitly, but let's do it now: we'll write $W = W(q,t;\beta)$ with $\beta = \beta(E)$ . Now we ask a somewhat strange question: suppose we try to perform a canonical transformation from $(q,p)$ to new coordinates $(\alpha,\beta)$ such that $\beta$ is the new momentum. What is the new coordinate $\alpha$ ? 

The change of coordinates should be canonical, so we must be able to write $q = q(\alpha, \beta)$ and $p = p(\alpha, \beta)$ such that 

$$
\{q, p \} _ {(\alpha , \beta)} \equiv \frac {\partial q}{\partial \alpha} \frac {\partial p}{\partial \beta} - \frac {\partial q}{\partial \beta} \frac {\partial p}{\partial \alpha} = 1.\tag{10.221}
$$

Using $p = \partial W / \partial q$ , and remembering what depends on what ( $W = W(q, \beta)$ and $q = q(\alpha, \beta)$ and $p = p(\alpha, \beta)$ ), we can write this as 

$$
\begin{array}{c} \{q, p \} _ {(\alpha , \beta)} = \frac {\partial q}{\partial \alpha} \left(\frac {\partial^ {2} W}{\partial \beta \partial q} + \frac {\partial^ {2} W}{\partial q ^ {2}} \frac {\partial q}{\partial \beta}\right) - \frac {\partial q}{\partial \beta} \frac {\partial^ {2} W}{\partial q ^ {2}} \frac {\partial q}{\partial \alpha} \\ = \frac {\partial q}{\partial \alpha} \frac {\partial}{\partial q} \left(\frac {\partial W}{\partial \beta}\right) \end{array}
$$

and we find that the transformation is canonical if we take $\alpha = \partial W / \partial \beta$ . Note the nice symmetry here: we have a solution $W(q, t; \beta)$ to the Hamilton Jacobi equation and we can think in terms of canonical coordinates $(q, p)$ or alternatively $(\alpha, \beta)$ where 

$$
p = \frac {\partial W}{\partial q} \quad \text { and } \quad \alpha = \frac {\partial W}{\partial \beta} .\tag{10.223}
$$

The function W is an example of a generating function of the second kind $(10.147)$ . 

So what to do with this? Let's look at some examples. Take $\beta = E$ , so that our new momentum variable is the energy itself. What is the canonical coordinate? If we write $W(q,t;E) = W_0(q,E) - Et$ then the coordinate canonically dual to $E$ is 

$$
\alpha = \frac {\partial W _ {0}}{\partial E} (q, E) - t.\tag{10.224}
$$

Taking the time dependence over the left-hand side, we see that $\alpha$ has the interpretation of $-t_{0}$ , the initial starting time. This tells us that we may parameterise every trajectory in a one-dimensional system in terms of the energy and starting time of the path, and that these are canonical variables. Again we see the dual relationship between energy and time. 

Note that both $E$ and $t_0$ are independent of time; we've found canonical variables for which neither the coordinate nor the momentum vary along the path. 

As another example consider the case of $\beta = I$ , our action variable of Section 10.5. What is the canonical coordinate $\alpha$ in this case? We expect that it will be related to the angle variable $\theta$ . To see this, we use the fact that W is the classical action to write 

$$
W _ {0} = \int L d t + E t = \int (L + H) d t = \int \dot {q} p d t = \int p d q.
$$

We then have 

$$
\alpha = \frac {\partial W}{\partial \beta} = \frac {d}{d I} \int p d q - \frac {d E}{d I} t = \theta - \omega t\tag{10.226}
$$

where we've used our expression (10.168) for the angle variable, as well as the equation (10.166) for the frequency of motion $\omega$ . So we see that $\alpha$ is not quite equal to $\theta$ , but is shifted by a term linear in time. In fact this means that $\alpha$ itself does not change in time. Once again, we've arrived at a way to parameterise the orbits of motion by canonical variables which do not themselves change with time. 

## 10.8 Quantum Mechanics

One of the primary reasons for studying the rather formal aspects of classical mechanics that we've seen in this chapter is to make contact with quantum mechanics. In this section, we flesh out some these connections. 

I should warn you that this section will make a lot more sense if you've already studied some quantum mechanics. The hope is that by seeing where the classical and quantum worlds are at their most similar, quantum mechanics may seem a little less weird. 

In classical mechanics the state of a system is described by a point $(q^{i}, p_{i})$ in phase space. In quantum mechanics the state is described by a very different object: a complex valued wavefunction $\psi(q)$ over the configuration space. The observables are operators on the space of wavefunctions. The standard representations of the position operator $\hat{q}^{i}$ and momentum operator $\hat{p}_{i}$ are 

$$
\begin{array}{l} \hat {q} ^ {i} \psi (q) = q ^ {i} \psi (q) \\ \hat {p} _ {i} \psi (q) = - i \hbar \frac {\partial \psi}{\partial q ^ {i}}. \end{array}\tag{10.227}
$$

This leads to the well known Heisenberg commutation relations 

$$
[ \hat {q} ^ {i}, \hat {p} _ {j} ] = i \hbar \delta_ {i j} \quad \mathrm{and} \quad [ \hat {q} ^ {i}, \hat {q} ^ {j} ] = [ \hat {p} _ {i}, \hat {p} _ {j} ] = 0.\tag{10.228}
$$

We've already seen something very familiar in Section 10.3, where we introduced Poisson brackets. In the classical world, the coordinates and momenta obey 

$$
\{q ^ {i}, p _ {j} \} = \delta_ {i j} \quad \mathrm{and} \quad \{q ^ {i}, q ^ {j} ] = \{p _ {i}, p _ {j} \} = 0.\tag{10.229}
$$

The quantum mechanical commutator [ , ] and the classical Poisson bracket { , } are different beasts, acting on very different objects. Yet both are bi-linear, anti-symmetric operations that share the same algebraic structure. Roughly speaking, the similarity between (10.228) and (10.229) reflects the fact that, in both the classical and quantum world, the momentum $p_{i}$ generates translations of the coordinate $q^{i}$ . We saw this in the classical context in Section 10.4. 

The similarity between the Poisson bracket and commutator structure seen above extends to other systems. In general, given a classical system with some Poisson bracket structure, the operators in the corresponding quantum system should obey 

$$
\{, \} _ {\mathrm{classical}} \longleftrightarrow - \frac {i}{\hbar} [, ] _ {\mathrm{quantum}}.\tag{10.230}
$$

This prescription for going between the classical and quantum theories is known as canonical quantisation. It also gives rise to the quantum equations of motion. In the Poisson bracket language, we have seen that the classical equation of motion for an arbitrary function $f(q,p)$ is 

$$
\frac {d f}{d t} = \{f, H \} \longrightarrow i \hbar \frac {d \hat {f}}{d t} = [ \hat {f}, \hat {H} ]\tag{10.231}
$$

which is the equation of motion in the Heisenberg picture, in which the time dependence is assigned to the operator rather than the state. 

While a great physicist, Dirac was never much of a storyteller. It shows in the following anecdote recounting his graduate student days: 

I went back to Cambridge at the beginning of October 1925, and resumed my previous style of life, intense thinking about these problems during the week and relaxing on Sunday, going for a long walk in the country alone. The main purpose of these long walks was to have a rest so that I would start refreshed on the following Monday. 

It was during one of the Sunday walks in October 1925, when I was thinking about this $(uv - vu)$ , in spite of my intention to relax, that I thought about Poisson brackets. I remembered something which I had read up previously, and from what I could remember, there seemed to be a close similarity between a Poisson bracket of two quantities and the commutator. The idea came in a flash, I suppose, and provided of course some excitement, and then came the reaction “No, this is probably wrong”. 

I did not remember very well the precise formula for a Poisson bracket, and only had some vague recollections. But there were exciting possibilities there, and 

I thought that I might be getting to some big idea. It was really a very disturbing situation, and it became imperative for me to brush up on my knowledge of Poisson brackets. Of course, I could not do that when I was right out in the countryside. I just had to hurry home and see what I could find about Poisson brackets. 

I looked through my lecture notes, the notes that I had taken at various lectures, and there was no reference there anywhere to Poisson brackets. The textbooks which I had at home were all too elementary to mention them. There was nothing I could do, because it was Sunday evening then and the libraries were all closed. I just had to wait impatiently through that night without knowing whether this idea was really any good or not, but I still think that my confidence gradually grew during the course of the night. 

The next morning I hurried along to one of the libraries as soon as it was open, and then I looked up Poisson brackets in Whitacker's Analytical Dynamics, and I found that they were just what I needed. 

## 10.8.1 Hamilton, Jacobi, Schrödinger, and Feynman

While the Poisson bracket structure of quantum mechanics dovetails nicely with Heisenberg's approach, the Hamilton–Jacobi equation is closely tied to Schrödinger's wave equation. 

Recall that the time-dependent Schrödinger equation is 

$$
i \hbar \frac {\partial \psi}{\partial t} = \hat {H} \psi\tag{10.232}
$$

where $\hat{H}$ is the Hamiltonian operator. For a 1d system, with $\hat{H} = \hat{p}^{2}/2m + V(\hat{q})$ , using the representation (10.227), the Schrödinger 

equation becomes 

$$
i \hbar \frac {\partial \psi}{\partial t} = \hat {H} \psi = - \frac {\hbar^ {2}}{2 m} \frac {\partial^ {2} \psi}{\partial q ^ {2}} + V (q) \psi\tag{10.233}
$$

where $\psi = \psi(q)$ . To see the relationship of this equation to classical dynamics, we decompose the wavefunction into the modulus and phase 

$$
\psi (q, t) = R (q, t) e ^ {i W (q, t) / \hbar}\tag{10.234}
$$

where R and W are both real functions. One of the postulates of quantum mechanics states that the probability density $P(q, t)$ for a particle to be found at position q at time t is 

$P(q,t)=|\psi(q,t)|^{2}=R(q,t)^{2}$ . But what is the physical interpretation of the phase W? If we substitute the decomposition of $\psi$ into the Schrödinger equation, we get 

$$
\begin{array}{c} i \hbar \left[ \frac {\partial R}{\partial t} + \frac {i R}{\hbar} \frac {\partial W}{\partial t} \right] = - \frac {\hbar^ {2}}{2 m} \left[ \frac {\partial^ {2} R}{\partial q ^ {2}} + \frac {2 i}{\hbar} \frac {\partial R}{\partial q} \frac {\partial W}{\partial q} \right. \\ \left. - \frac {R}{\hbar^ {2}} \left(\frac {\partial W}{\partial q}\right) ^ {2} + \frac {i R}{\hbar} \frac {\partial^ {2} W}{\partial q ^ {2}} \right] + V \end{array}
$$

At this stage, we take the classical limit which, roughly, means $\hbar \rightarrow 0$ . More precisely, it means that we should consider a wavefunction such that 

$$
\hbar \left| \frac {\partial^ {2} W}{\partial q ^ {2}} \right| \ll \left| \frac {\partial W}{\partial q} \right|.\tag{10.235}
$$

Physically, this can be understood as the requirement that the de Broglie wavelength of the particle is much smaller than any other length scale around. Collecting together the terms above to leading order in $\hbar$ we find 

$$
\frac {\partial W}{\partial t} + \frac {1}{2 m} \left(\frac {\partial W}{\partial q}\right) ^ {2} + V (q) = \mathcal {O} (\hbar).\tag{10.236}
$$

But this is precisely Hamilton–Jacobi equation (10.214)! We learn that, in the classical limit, the phase of the wavefunction is understood as the classical action of the path taken by the particle. 

As a final flourish, we return to the principle of least action. Recall from Chapter 7 that we can determine the true path of a system by assigning a number, called the action S, to every possible path. The equations of motion are then equivalent to insisting that the true path is an extremum of S. But what about all the other paths? Do they play any role in nature? 

The answer is that, in the quantum world, they do. Suppose that a particle is observed to be at position $q_{i}$ at time t = 0. Then the probability P that it will later be observed to be at position $q_{f}$ at time t = T is encapsulated in the wavefunction $\psi(q_{f}, T)$ . There is a wonderful formula, due to Feynman, that gives the wavefunction at the later time in terms of a sum over all possible paths 

$$
\psi (q _ {f}, T) = \mathcal {N} \int_ {q _ {i}} ^ {q _ {f}} \mathcal {D} q (t) e ^ {i S [ q (t) ] / \hbar}.\tag{10.237}
$$

Here N is just a normalisation constant to ensure that probabilities add up to one, i.e. $\int |\psi(q)|^{2} dq = 1$ . The tricky part of this formula is the integral: it is a sum over all possible paths from $q = q_{i}$ at time t = 0 to $q = q_{f}$ at time t = T, known as a path integral. These paths are weighted with their action. The formula (10.237) suggests that the particle really does take every possible path, but this comes accompanied by a particular phase $e^{iS/\hbar}$ . 

In the limit $\hbar \rightarrow 0$ , the phases oscillate wildly for any path away from the classical equation of motion $\delta S = 0$ and they cancel out in the integral. In that case, the only contribution to the integral comes from the extrema of the action such that $\delta S = 0$ . These, of course, are the classical paths. Meanwhile, in other situations $\hbar$ is important and, correspondingly, so are paths that are not close to the classical one. 

Here we will prove that the wavefunction defined by $(10.237)$ satisfies the Schrödinger equation. Firstly we need to understand the integral over paths a little better. We do this by splitting the path into n small segments, each ranging over a small time $\delta t = T/n$ . This is shown in Figure 10.7. Then we define 

$$
\int \mathcal {D} q (t) = \lim _ {n \to \infty} \prod_ {k = 1} ^ {n} \int_ {- \infty} ^ {+ \infty} \frac {d q _ {k}}{C}\tag{10.238}
$$

where $q_{k}$ is the position of the particle at time $t = k\delta t$ . In this expression C is a constant that we're going to figure out shortly that will be required to make sense of this infinite number of integrals. In any given segment, we treat the path as a straight line and replace the action with the appropriate quantity, 

$$
\begin{array}{l} S = \int_ {0} ^ {T} d t \left(\frac {1}{2} m \dot {q} ^ {2} - V (q)\right) \\ \longrightarrow \sum_ {k = 1} ^ {n} \left(\frac {m}{2} \frac {(q _ {k + 1} - q _ {k}) ^ {2}}{\delta t} - \delta t V \left(\frac {q _ {k + 1} + q _ {k}}{2}\right)\right). \end{array}
$$

Then, to prove that $\psi$ defined in (10.237) satisfies Schrödinger's equation, we consider adding a single extra time step to look at the wavefunction at time $T + \delta t$ . We can Taylor expand the left-hand side of (10.237) to get 

$$
\psi (q _ {f}, T + \delta t) = \psi (q _ {f}, T) + \frac {\partial \psi}{\partial T} \delta t + \mathcal {O} (\delta t ^ {2})\tag{10.240}
$$

while the right-hand side requires us to do one extra integral over the penultimate position of the path $q'$ . But the first n integrals simply give back the original wavefunction, now evaluated at $q'$ . We get 

$$
\int_ {- \infty} ^ {+ \infty} \frac {d q ^ {\prime}}{C} \exp \left[ \frac {i m}{2 \hbar} \frac {(q _ {f} - q ^ {\prime}) ^ {2}}{\delta t} - \frac {i}{\hbar} \delta t V \left(\frac {q _ {f} + q ^ {\prime}}{2}\right) \right] \psi (q ^ {\prime}, t).
$$

The term in the exponent means that the integral oscillates wildly whenever $q'$ is far from $q_{f}$ and these regions of the integral will all cancel out. We can therefore Taylor expand around $(q_{f} - q')$ to rewrite this as 

$$
\begin{array}{l} \int_ {- \infty} ^ {+ \infty} \frac {d q ^ {\prime}}{C} \exp \left[ \frac {i m}{2 \hbar} \frac {(q _ {f} - q ^ {\prime}) ^ {2}}{\delta t} \right] \left(1 - \frac {i \delta t}{\hbar} V (q _ {f}) + \dots\right) \\ \times \left(1 + (q ^ {\prime} - q _ {f}) \frac {\partial}{\partial q _ {f}} + \frac {1}{2} (q ^ {\prime} - q _ {f}) ^ {2} \frac {\partial^ {2}}{\partial q _ {f} ^ {2}} + \dots\right) \psi (q _ {f}, \end{array}
$$

At this stage we do the integral over $q'$ . We'll need the formulae for Gaussian integration 

$$
\begin{array}{c} {\int d y e ^ {- a y ^ {2}} = \sqrt {\frac {\pi}{a}}} \\ {\int d y y e ^ {- a y ^ {2}} = 0} \\ {\int d y y ^ {2} e ^ {- a y ^ {2}} = \frac {1}{2 a} \sqrt {\frac {\pi}{a}}.} \end{array}\tag{10.243}
$$

We then equate the left-hand side of $(10.240)$ with the right-hand side of $(10.242)$ to find 

$$
\begin{array}{r} \psi (q _ {f}, T) + \frac {\partial \psi}{\partial T} \delta t = \frac {1}{C} \sqrt {\frac {2 \pi \hbar \delta t}{- i m}} \left[ 1 - \frac {i \delta t}{\hbar} V (q _ {f}) \right. \\ \left. + \frac {i \hbar \delta t}{2 m} \frac {\partial^ {2}}{\partial q _ {f} ^ {2}} + \mathcal {O} (\delta t ^ {2}) \right] \psi (q _ {f}, T) \end{array}
$$

At this stage we see what the constant C has to be to make sense of this whole calculation: we should take 

$$
C = \sqrt {\frac {2 \pi \hbar \delta t}{- i m}}\tag{10.244}
$$

so that $C \rightarrow 0$ as $\delta t \rightarrow 0$ . Then the terms of order $\mathcal{O}(\delta t^{0})$ agree. Collecting the terms of order $\mathcal{O}(\delta t)$ , and replacing the time T at the end point with the general time t, we see that we have 

$$
i \hbar \frac {\partial \psi}{\partial t} = - \frac {\hbar^ {2}}{2 m} \frac {\partial^ {2} \psi}{\partial q _ {f} ^ {2}} + V (q _ {f}) \psi = \hat {H} \psi\tag{10.245}
$$

and we recover Schrödinger's equation as promised. We will devote a chapter in Volume 3 on Quantum Mechanics to better understand the path integral and its applications. 

Fig. 10.7 Discretising the paths. 

## 11 Special Relativity

Although Newtonian mechanics gives an excellent description of the world, it is not universally valid. When we reach extreme conditions — the very small, the very heavy, or the very fast — the familiar Newtonian universe needs replacing. You could say that Newtonian mechanics encapsulates our common-sense view of the world. One of the major themes of twentieth-century physics is that when you look away from our everyday world, common sense is not much of a guide. 

One such extreme is when particles travel very fast. The theory that replaces Newtonian mechanics in this limit is due to Einstein. It is called special relativity. The effects of special relativity are apparent only when the speeds of particles become comparable to the speed of light in the vacuum. The speed of light is 

$$
c = 2 9 9, 7 9 2, 4 5 8 \mathrm{ms} ^ {- 1}.
$$

This value of c is exact. It may seem strange that the speed of light is an integer when measured in meters per second. The reason is simply that this is taken to be the definition of what we mean by a meter: it is the distance travelled by light in 1/299,792,458 seconds. For our purposes, we'll be quite happy with the approximation $c \approx 3 \times 10^{8}$ ms $^{-1}$ . 

The first thing to say is that the speed of light is fast. Really fast. The speed of sound is around $300 \, m s^{-1}$ ; escape velocity from the Earth is around $10^{4} \, m s^{-1}$ ; the orbital speed of our solar system in the Milky Way galaxy is around $10^{5} \, m s^{-1}$ . As we shall soon see, nothing travels faster than c. 

The theory of special relativity rests on two experimental facts. (We will look at the evidence for these shortly.) In fact, we have already met the first of these: it is simply the Galilean principle of relativity described in Chapter 1. The second postulate is more surprising: 

- Postulate 1: The principle of relativity: the laws of physics are the same in all inertial frames. 

- Postulate 2: The speed of light in vacuum is the same in all inertial frames. 

On the face of it, the second postulate looks nonsensical. How can the speed of light look the same in all inertial frames? If light travels towards me at speed c and I run away from the light at speed v, surely I measure the speed of light as c - v. Right? Well, no. 

This common sense view is encapsulated in the Galilean transformations that we met in Section 1.1.2. Mathematically, we derive this “obvious” result as follows: two inertial frames, S and $S'$ , which move relative to each with velocity $\mathbf{v} = (v, 0, 0)$ , have Cartesian coordinates related by 

$$
x ^ {\prime} = x - v t, \quad y ^ {\prime} = y, \quad z ^ {\prime} = z, \quad t ^ {\prime} = t.\tag{11.1}
$$

If a ray of light travels in the x-direction in frame S with speed c, then it traces out the trajectory x/t = c. The transformations above then tell us that, in frame $S'$ , the trajectory of the light ray is $x'/t' = c - v$ . This is the result we claimed above: the speed of light should clearly be c - v. If this is wrong (and it is) something must be wrong with the Galilean transformations (11.1). But what? 

Our immediate goal is to find a transformation law that obeys both postulates above. As we will see, the only way to achieve this goal is to allow for a radical departure in our understanding of time. In particular, we will be forced to abandon the assumption of absolute time, enshrined in the equation $t' = t$ above. We will see that time ticks at different rates for observers sitting in different inertial frames. 

## 11.1 Lorentz Transformations

We stick with the set-up of two inertial frames, $S$ and $S'$ , moving with relative speed $v$ . For simplicity, we'll start by ignoring the directions $y$ and $z$ which are perpendicular to the direction of motion. Both inertial frames come with Cartesian coordinates: $(x, t)$ for $S$ and $(x', t')$ for $S'$ . We want to know how these are related. The most general possible relationship takes the form 

$$
x ^ {\prime} = f (x, t) \quad \text { and } \quad t ^ {\prime} = g (x, t)\tag{11.2}
$$

for some functions $f$ and $g$ . However, there are a couple of facts that we can use to restrict the form of these functions. The first is that the law of inertia holds: left alone in an inertial frame, a particle will travel at constant velocity. Drawn in the $(x, t)$ -plane, the trajectory of such a particle is a straight line. Since both $S$ and $S'$ are inertial frames, the map $(x, t) \mapsto (x', t')$ must map straight lines to straight lines. Such maps are, by definition, linear. The functions $f$ and $g$ must therefore be of the form 

$$
x ^ {\prime} = \alpha_ {1} x + \alpha_ {2} t \quad \mathrm{and} \quad t ^ {\prime} = \alpha_ {3} x + \alpha_ {4} t\tag{11.3}
$$

where $\alpha_{i}$ , with i = 1, 2, 3, 4, can each be a function of v. 

Second, we use the fact that $S'$ is travelling at speed v relative to S. This means that an observer sitting at the origin, $x' = 0$ , of $S'$ moves along the trajectory x = vt in S, as shown in the figure to the right. Or, in other 

words, the points x = vt must map to $x' = 0$ . (There is actually one further assumption implicit in this statement: that the origin $x' = 0$ coincides with x = 0 when t = 0.) 

Together with the requirement that the transformation is linear, this restricts the coefficients $\alpha_{1}$ and $\alpha_{2}$ in (11.3) to be of the form, 

$$
x ^ {\prime} = \gamma (x - v t)\tag{11.4}
$$

for some parameter $\gamma$ which can be a function of the velocity. We'll sometimes denote this by writing $\gamma = \gamma_v$ . (We use subscript notation $\gamma_v$ rather than the more standard $\gamma(v)$ to denote that $\gamma$ depends on $v$ . This avoids confusion with the factors of $(x - vt)$ which aren't arguments of $\gamma$ but will frequently appear after $\gamma$ like in the equation (11.4).) 

There is actually a small, but important, restriction on the form of $\gamma_{v}$ : it must be an even function, so that $\gamma_{v} = \gamma_{-v}$ . There are a couple of ways to see this. The first is by using rotational invariance, which states that $\gamma$ cannot depend on the direction of the relative velocity v, but only on the magnitude $v^{2} = v \cdot v$ . Alternatively, if this is a little slick, we can reach the same conclusion by considering inertial frames $\tilde{S}$ and $\tilde{S}'$ which are identical to S and $S'$ except that we measure the x-coordinate in the opposite direction, meaning $\tilde{x} = -x$ and $\tilde{x}' = -x'$ . While S is moving with velocity +v relative to $S'$ , $\tilde{S}$ is moving with velocity -v with respect to $\tilde{S}'$ simply because we measure things in the opposite direction. That means that 

$$
\tilde {x} ^ {\prime} = \gamma_ {- v} (\tilde {x} + v t).\tag{11.5}
$$

Comparing this to $(\underline{11.4})$ , we see that we must have $\gamma_{v} = \gamma_{-v}$ as claimed. 

Next, we look at things from the perspective of $S'$ , relative to which the frame S moves backwards with velocity -v. The same argument that led us to (11.4) now tells us that 

$$
x = \gamma_ {- v} (x ^ {\prime} + v t ^ {\prime}).\tag{11.6}
$$

Here the coefficient that sits in front is $\gamma = \gamma_{-v}$ . But by the argument above, we know that $\gamma_{v} = \gamma_{-v}$ . In other words, the coefficient $\gamma$ appearing in (11.6) is the same as that appearing in (11.4). 

At this point, things don't look too different from what we've seen before. Indeed, if we were to now insist on absolute time, so $t = t'$ , then we're forced to have $\gamma = 1$ and we get back to the Galilean transformations (11.1). However, as we've seen, this is not compatible with the second postulate of special relativity. So let's push forward and insist instead that the speed of light is equal to $c$ in both $S$ and $S'$ . In $S$ , a light ray has trajectory 

$$
x = c t.\tag{11.7}
$$

While, in $S'$ , we demand that the same light ray has trajectory 

$$
x ^ {\prime} = c t ^ {\prime}.\tag{11.8}
$$

Substituting these trajectories into $(\underline{11.4})$ and $(\underline{11.6})$ , we have two equations relating t and $t'$ , 

$$
c t ^ {\prime} = \gamma (c - v) t \quad \text { and } \quad c t = \gamma (c + v) t ^ {\prime} .\tag{11.9}
$$

A little algebra shows that these two equations are compatible only if $\gamma$ is given by 

$$
\gamma = \sqrt {\frac {1}{1 - v ^ {2} / c ^ {2}}} .\tag{11.10}
$$

We'll be seeing a lot of this coefficient $\gamma$ in what follows. For $v \ll c$ , we have $\gamma \approx 1$ and the transformation law (11.4) is approximately the same as the Galilean transformation (11.1). However, as $v \to c$ we have $\gamma \to \infty$ . Furthermore, $\gamma$ becomes imaginary for $v > c$ which means that we're unable to make sense of inertial frames with relative speed $v > c$ . 

Equations (11.4) and (11.10) give us the transformation law for the spatial coordinate. But what about for time? In fact, the temporal transformation law is already lurking in our analysis above. Substituting the expression for $x'$ in (11.4) into (11.6), and rearranging, we get 

$$
t ^ {\prime} = \gamma \left(t - \frac {v}{c ^ {2}} x\right).\tag{11.11}
$$

We shall soon see that this equation has dramatic consequences. For now, however, we merely note that when $v \ll c$ , we recover the trivial Galilean transformation law $t' \approx t$ . Equations (11.4) and (11.11) are the Lorentz transformations. 

## 11.1.1 Lorentz Transformations in Three Spatial Dimensions

In the above derivation, we ignored the transformation of the coordinates y and z perpendicular to the relative motion. These transformations turn out to be trivial. Using the above arguments for linearity, and the fact that the origins coincide at t = 0, the most general form of the transformation is 

$$
y ^ {\prime} = \kappa y.\tag{11.12}
$$

But, by symmetry, we must also have $y = \kappa y'$ . Clearly, we require $\kappa = 1$ . (The other possibility $\kappa = -1$ does not give the identity transformation when v = 0. Instead, it is a reflection.) 

With this we can write down the final form of the Lorentz transformations. They look more symmetric between x and t if we write them using the combination ct, 

$$
\begin{array}{l} {x ^ {\prime} = \gamma \left(x - \frac {v}{c} c t\right)} \\ {y ^ {\prime} = y} \\ {z ^ {\prime} = z} \\ {c t ^ {\prime} = \gamma \left(c t - \frac {v}{c} x\right)} \end{array}\tag{11.13}
$$

where $\gamma$ is given by (11.10). These are also known as Lorentz boosts. Notice that, for $v/c \ll 1$ , the Lorentz boosts reduce to the more intuitive Galilean boosts that we saw in Chapter 1. (We sometimes say, rather sloppily, that the Lorentz transformations reduce to the Galilean transformations in the limit $c \to \infty$ .) 

It's also worth stressing again the special properties of these transformations. To be compatible with the first postulate, the transformations must take the same form if we invert them to express $x$ and $t$ in terms of $x'$ and $t'$ , except with $v$ replaced by $-v$ . And, after a little bit of algebraic magic, they do. 

We want the speed of light to be the same in all inertial frames. We already imposed this in our derivation of the Lorentz transformations for light travelling in the x-direction, but it's simple to check again: in frame S, the trajectory of an object travelling at the speed of light obeys x = ct. In $S'$ , the same object will follow the trajectory 

$$
x ^ {\prime} = \gamma (x - v t) = \gamma (c t - v x / c) = c t ^ {\prime}.
$$

What about an object travelling in the y direction at the speed of light? Its trajectory in S is y = ct. From $(11.13)$ , its trajectory in $S'$ is $y' = ct'/\gamma$ and $x' = -vt'$ . Its speed in $S'$ is therefore $v'^{2} = v_{x}^{2} + v_{y}^{2}$ , or 

$$
v ^ {2} = \left(\frac {x ^ {\prime}}{t ^ {\prime}}\right) ^ {2} + \left(\frac {y ^ {\prime}}{t ^ {\prime}}\right) ^ {2} = v ^ {2} + \frac {c ^ {2}}{\gamma^ {2}} = c ^ {2}.\tag{11.14}
$$

Again, we see that the speed of light is constant. 

## 11.1.2 Spacetime Diagrams

We will find it very useful to introduce a simple spacetime diagram to illustrate the physics of relativity. In a fixed inertial frame S, we draw one direction of space, say x, along the horizontal axis and time on the vertical axis. But things look much nicer if we rescale time and plot ct on the vertical instead. This is a spacetime diagram. In the context of special relativity, space and time are combined into something called Minkowski space. The proper definition of Minkowski space requires some extra structure which we will meet in Section 11.3. 

Each point $P$ in spacetime represents an event. In the following, we will label points on the spacetime diagram by coordinates $(ct, x)$ , i.e. giving the coordinate along the vertical axis first. (This is backwards from the usual convention for specifying coordinates, but it's chosen so that it's consistent with a later convention that we will meet in Section 11.3.) 

A particle moving in spacetime traces out a curve called a worldline, as shown in Figure 11.1. Because we've rescaled the time axis, a light ray moving in the $x$ -direction moves at $45^{\circ}$ . We'll later see that no object can move faster than the speed of light, which means that the worldlines of particles must always move upwards at an angle steeper than $45^{\circ}$ . 

Fig. 11.1 On the left, the worldline of a massive particle. On the right, light rays always travel at $45^{\circ}$ . 

The horizontal and vertical axes in the spacetime diagram are the coordinates of the inertial frame S. But we could also draw the axes corresponding to an inertial frame $S'$ moving with relative velocity $\mathbf{v} = (v, 0, 0)$ . The $t'$ -axis sits at $x' = 0$ and is given by 

$$
x = v t.\tag{11.15}
$$

Meanwhile, the $x'$ -axis is determined by the simple relation $t' = 0$ which, from the Lorentz transformation (11.13), is given by the equation 

$$
c t = \frac {v}{c} x.\tag{11.16}
$$

These two axes are drawn on the figure to the right. They can be the thought of as the x- and ct-axes, rotated by an equal amount towards the diagonal light ray. The fact the axes are symmetric about the light ray reflects the fact that the speed of light is equal to c in both frames. 

## 11.1.3 A History of Light Speed

The first evidence that light does not travel instantaneously was presented by the Danish Astronomer Ole Rømer in 1676. He noticed that the periods of the orbits of Io, the innermost moon of Jupiter, are not constant. When the Earth is moving towards Jupiter, the orbits are a few minutes shorter; when the Earth moves away, the orbits are longer by the same amount. Rømer correctly deduced that this was due to the finite speed of light and gave a rough estimate for the value of c. 

By the mid 1800s, the speed of light had been determined fairly accurately using experiments involving rotating mirrors. Then came a theoretical bombshell. James Clerk Maxwell successfully combined various ideas in electromagnetism to write down the unified equations that now bear his name. Among the many delights hiding in these equations, one stands out: they predict that light travels with a fixed speed 

$$
c = \sqrt {\frac {1}{\epsilon_ {0} \mu_ {0}}}\tag{11.17}
$$

where $\epsilon_0$ and $\mu_0$ are constants of nature, known as the permittivity and permeability of free space, that describe the strengths of electric and magnetic forces. We'll see the derivation of (11.17) in Volume 2 on Electromagnetism. 

If we try to reconcile the result (11.17) with our common-sense ideas of Newtonian (or Galilean) ideas of relativity, in which the speed of light depends on our reference frame, then we're led to conclude that the Maxwell equations themselves should be valid only in a preferred reference frame. That was the prevailing consensus of the 1800s. And it doesn't seem so unreasonable. Just as water waves need water, and sound waves need air, so it was thought that light waves must be waving in something. That hypothetical material was dubbed the luminiferous ether, and it was thought that Maxwell's equations must only be valid in the frame at rest with respect to this ether. 

That leads to an interesting question: What speed are we travelling at with respect to the ether? In 1881, Michelson and Morley performed an experiment to measure this. They used the fact that the Earth is orbiting the Sun at a speed of $3 \times 10^{4}$ m s $^{-1}$ . This means that, even if we just happen to be stationary with respect to the ether at some point of the orbit, six months later this can no longer be the case. If the experiment is accurate enough, then it should be possible to measure the way the speed of light changes over the year. 

Here's the underlying mathematics. Suppose that at some moment the Earth is moving in the $x$ -direction relative to the ether with speed $v$ . The Newtonian addition of velocities tells us that light propagating in the $x$ -direction should have speed $c + v$ going one way and $c - v$ going the other. The total time to travel backwards and forwards along a length $L$ , oriented in the $x$ -direction, should therefore be 

$$
T _ {x} = \frac {L}{c + v} + \frac {L}{c - v} = \frac {2 c L}{c ^ {2} - v ^ {2}}.\tag{11.18}
$$

Now think about light making the same journey, but along a length L oriented in the y-direction, which is perpendicular to the motion with respect to the ether. In the y-direction, light travels at the proper speed c. But the motion with respect to the ether means that it has further to go. If light takes a time $T_{y}/2$ to travel the length L in the y-direction then, by Pythagoras, the light will have travelled a total distance of 

$\sqrt{L^{2}+v^{2}(T_{y}/2)^{2}}$ . It makes this journey at speed c, meaning that we can equate 

$$
\frac {c T _ {y}}{2} = \sqrt {L ^ {2} + v ^ {2} (T _ {y} / 2) ^ {2}} \quad \Longrightarrow \quad T _ {y} = \frac {2 L}{\sqrt {c ^ {2} - v ^ {2}}} .
$$

We see that when we're sitting at rest with respect to the ether, so $v = 0$ , the times $T_x$ and $T_y$ are the same. But when $v \neq 0$ , we have $T_x \neq T_y$ . The goal of the Michelson–Morley experiment was to measure this time difference using interference patterns of light rays making the two journeys. Needless to say, the experiment didn't work. There seemed to be no difference in the time taken to travel in the $x$ -direction and $y$ -direction. 

Towards the end of the 1800s, the null result of the Michelson–Morley experiment had become a major headache for theoretical physicists. Several increasingly convoluted explanations were proposed, including the idea that the ether was somehow dragged along with the Earth. The Dutch physicist, Hendrik Lorentz, went some way to finding the correct solution. He noticed that Maxwell's equations had the peculiar symmetry that we now call the Lorentz transformations. He argued that, if a reason could be found that would allow distances between matter to change as 

$$
x ^ {\prime} = \gamma (x - v t)\tag{11.20}
$$

then lengths would be squeezed in the direction parallel to the ether, explaining why no difference is seen between $T_{x}$ and $T_{y}$ . (We will shortly derive this contraction of lengths using special relativity.) Lorentz set to work trying to cook up a mechanical explanation for this transformation law. 

Although Lorentz had put in place much of the mathematics, the real insight came from Einstein in 1905. He understood that there is no mechanical mechanism underlying the Lorentz transformations. Nor is there an ether. Instead, the Lorentz transformations are a property of space and time themselves. 

With Einstein's new take on the principle of relativity, all problems with Maxwell's equation evaporate. There is no preferred inertial frame. Instead, Maxwell's equations work equally well in all inertial frames. However, they are not invariant under the older transformations of Galilean relativity. Instead they are the first law of physics to be invariant under the correct transformations (11.13) of Einstein/Lorentz relativity. 

It's worth pointing out that, from this perspective, we could dispense with the second postulate of relativity all together. We need only insist that the laws of physics, which include the Maxwell equations, hold in all inertial frames. Since Maxwell's equations predict the speed of light, this is sufficient to imply that the speed of light is the same in all inertial frames. But since we haven't yet seen the relationship between Maxwell's equations, light and relativity, it's perhaps best to retain the second postulate for now. 

## 11.2 Relativistic Physics

In this section we will explore some of the more interesting and surprising consequences of the Lorentz transformations. 

## 11.2.1 Simultaneity

We start with a simple question: How can we be sure that things happen at the same time? In Newtonian physics, this is a simple question to answer. In that case, we have an absolute time t and two events, $P_{1}$ and $P_{2}$ , happen at the same time if $t_{1} = t_{2}$ . However, in the relativistic world, things are not so easy. 

We start with an observer in inertial frame S, with time coordinate t. This observer sensibly decides that two events, $P_{1}$ and $P_{2}$ , occur simultaneously if $t_{1} = t_{2}$ . In the spacetime diagram on the left of Figure 11.2 we have drawn lines of simultaneity for this observer. 

## Fig. 11.2 Simultaneity is relative.

But, for an observer in the inertial frame $S'$ , simultaneity of events occurs for equal $t'$ . Using the Lorentz transformation, lines of constant $t'$ become lines described by the equation $t - vx/c^{2} = constant$ . These lines are drawn on the spacetime diagram on the right of Figure 11.2. 

The upshot of this is that two events which are simultaneous in one inertial frame are not simultaneous in another. An observer in S thinks that events $P_{1}$ and $P_{2}$ happen at the same time. Other observers disagree. 

## A Train Story

The fact that all observers cannot agree on what events are simultaneous is a direct consequence of the fact that all observers do agree on the speed of light. We can illustrate this connection with a simple gedankenexperiment (an ugly German word for “thought experiment”, a favourite trick of theoretical physicists who can’t be bothered to do real experiments). Consider a train moving at constant speed, with a lightbulb hanging from the middle of one of the carriages. A passenger on the train turns the bulb on and off and, because the bulb is equidistant from both the front and back wall of the carriage, observes that the light hits both walls at the same time. 

However, a person standing on the platform as the train passes through disagrees. The light from the bulb travels at equal speed $\pm c$ to the left and right, but the back of the train is rushing towards the point in space where the light first emerged from. The person on the platform will see the light hit the back of the train first. This is shown in Figure 11.3. 

Fig. 11.3 Lights on trains: simultaneity is relative. On the left, the view seen by someone on the moving train. On the right, the view seen by someone on the platform. 

It is worth emphasising that, although the two people disagree on whether the light hits the walls at the same time, this does not mean that they can't be friends. 

## A Potential Confusion: What the Observer Observes

We'll pause briefly to press home a point that may lead to confusion. You might think that the question of simultaneity has something to do with the finite speed of propagation. You don't see something until the light has travelled to you, just as you don't hear something until the sound has travelled to you. This is not what's going on here! A look at the spacetime diagram in Figure 11.2 shows that we've already taken this into account when deciding whether two events occur simultaneously. The lack of simultaneity between moving observers is a much deeper issue, not due to the finiteness of the speed of light but rather due to the constancy of the speed of light. 

The confusion about the time of flight of the signal is sometimes compounded by the common use of the word observer to mean “inertial frame”. This brings to mind some guy sitting at the origin, surveying all around him. Instead, you should think of the observer more as a Big Brother figure: a sea of clocks and rulers throughout the inertial frame which can faithfully record and store the position and time of any event, to be studied at some time in the future. 

Of course, this means that there is a second question we can ask which is: What does the guy sitting at the origin actually see? Now we have to take into account both the relative nature of simultaneity and the issues related with the finite speed of propagation. This adds an extra layer of complexity which we will discuss in Section 11.7. 

## 11.2.2 Causality

We've seen that different observers disagree on the temporal ordering of two events. But where does that leave the idea of causality? Surely it's important that we can say that one event definitely occurred before another. Thankfully, all is not lost: there are only some events which observers can disagree about. 

To see this, note that because Lorentz boosts are only possible for v < c, the lines of simultaneity cannot be steeper than $45^{\circ}$ . Take a point P and draw the $45^{\circ}$ light rays that emerge from P. This is called the light cone. (For once, this is shown in the figure below with an extra spatial dimension present to illustrate how this works in spatial dimensions bigger than one). The light cone is really two cones, touching at the point P. They are known as the future light cone and the past light cone. 

For events inside the light cone of P, there is no difficulty deciding on the temporal ordering of events. All observers will agree that Q, show in the figure, occurred after P. However, for events outside the light cone, the matter is up for grabs: some observers will see R as happening after P, some before. 

This tells us that the events which can be causally influenced by $P$ lie within the future light cone of $P$ , and all observers agree on this. Similarly, the events which can plausibly influence $P$ are those inside the past light cone. This is why we can sleep comfortably at night, happy in the knowledge that causality is preserved only if nothing can propagate outside the light cone. But that's the same thing as travelling faster than the speed of light. 

The converse to this is that if we do ever see particles that travel faster than the speed of light, then we're in trouble. We could use them to transmit information faster than light. But another observer would view this as transmitting information backwards in time. All our ideas of cause and effect will be turned on their head. You will therefore be relieved to learn that we will show in Section 11.3 why it is impossible to accelerate particles past the light speed barrier. 

The fact that events outside the lightcone cannot influence each other means, among other things, that there can be no perfectly rigid objects. Suppose that you push on one end of a rod. The other end cannot move immediately since that would allow us to communicate faster than the speed of light. Of course, for real rods, the other end does not move instantaneously. Instead, pushing on one end of the rod initiates a sound wave which propagates through the rod, telling the other parts to move. The statement that there is no rigid object really means that this sound wave must travel slower than the speed of light. 

Finally, let me mention that, when we're talking about waves, as opposed to point particles, there is a slight subtlety in exactly what must travel slower than light. There are at least two velocities associated to a wave: the group velocity is (usually) the speed at which information can be communicated. This is less than $c$ . In contrast, the phase velocity is the speed at which the peaks of the wave travel. This can be greater than $c$ , but transmits no information. 

## 11.2.3 Time Dilation

We'll now turn to one of the more dramatic results of special relativity. Consider a clock sitting stationary in the frame $S'$ which ticks at intervals of $T'$ . This means that the tick events in frame $S'$ occur at $(ct_1', 0)$ then $(ct_1' + cT', 0)$ and so on. What are the intervals between ticks in frame $S$ ? 

We can answer immediately from the Lorentz transformations (11.13). Inverting this gives 

$$
t = \gamma \left(t ^ {\prime} + \frac {v x ^ {\prime}}{c ^ {2}}\right).\tag{11.21}
$$

The clock sits at $x' = 0$ so we immediately learn that, in frame S, the interval between ticks is 

$$
T = \gamma T ^ {\prime}.\tag{11.22}
$$

This means that the gap between ticks is longer in the stationary frame. Said differently, a moving clock runs more slowly. But the same argument holds for any process, be it clocks, elementary particles, or human hearts. The correct interpretation is that time itself runs more slowly in moving frames. 

## Another Train Story

Let's go back to our lightbulb and gedankenbahn. If the train has height $h$ , a passenger on the train will measure time $t' = h / c$ for the light to travel from the light bulb to the middle of the floor (i.e. the point directly below the light bulb). What about for the guy on the platform? The situation is shown in Figure 11.4. After the light turns on, the train has moved forward at speed v. To hit the same point on the floor, the light has to travel a distance $\sqrt{h^{2} + (vt)^{2}}$ . The time taken is therefore 

$$
t = \frac {\sqrt {h ^ {2} + (v t) ^ {2}}}{c} \quad \Longrightarrow \quad t = \frac {h}{c} \sqrt {\frac {1}{1 - v ^ {2} / c ^ {2}}} = \gamma t ^ {\prime}.
$$

This gives another, more pictorial, derivation of the time dilation formula. 

Fig. 11.4 More lights on trains: time dilation. 

## On Muons and Planes

Away from the world of gedankenexperiments, there are a couple of real experimental consequences of time dilation. The place that this phenomenon is tested most accurately is in particle accelerators where elementary particles routinely reach speeds close to c. The protons spinning around the LHC have $\gamma \approx 3500$ . The previous collider in CERN, called LEP, accelerated electrons and positrons to $\gamma \approx 2 \times 10^{5}$ . (Although the electrons in LEP were travelling faster than the protons in LHC, the greater mass of the protons means that there is substantially more energy in the LHC collisions.) 

The effect of time dilation is particularly vivid for unstable particles, which live much longer in the lab frame than in their own rest frame. An early demonstration was seen in muons in 1941. These are heavier, unstable, versions of the electron. They decay into an electron, together with a couple of neutrinos, with a half-life of $\tau \approx 2 \times 10^{-6}$ s. Muons are created when cosmic rays hit the atmosphere, and subsequently rain down on Earth. Yet to make it down to sea level, it takes about $t = 7 \times 10^{-6}$ s, somewhat longer than their lifetime. Given this, why are there any muons detected on Earth at all? Surely they should have decayed. The reason that they are able to make the journey is because the muons are travelling at a speed $v \approx 0.99c$ , giving $\gamma \approx 10$ . From the muon's perspective, the journey only takes $t' = t / \gamma \approx 7 \times 10^{-7}$ s, somewhat less than their lifetime. 

Elementary particles are, by definition, structureless. They're certainly not some clock with an internal machinery. The reason that they live longer can't be explained because of some mechanical device which slows down: it is time itself which is running slower. 

A more direct test of time dilation was performed in 1971 by Hafele and Keating. They flew two atomic clocks around the world on commercial airliners. Two more were left at home. When they were subsequently brought together, their times differed by about $10^{-7}$ s. There are actually two contributions to this effect: the time dilation of special relativity that we've seen above, together with a related effect in general relativity due to the gravity of the Earth. 

## The Twin Paradox

Two twins, Luke and Leia, decide to spend some time apart. Leia stays at home while Luke jumps in a spaceship and heads at some speed v to the planet Tatooine. With sadness, Leia watches Luke leave but is relieved to see him safely reach the planet only a time T later from her perspective. 

However, upon arrival, Luke finds that he doesn't like Tatooine so much. It is a dusty, violent place with little to do. So he turns around and heads back to Leia at the same speed $v$ as before. When he returns, he finds that Leia has aged by $T_{\text{Leia}} = 2T$ . And yet, fresh faced Luke has only aged by $T_{\text{Luke}} = 2T / \gamma$ . After the journey, Luke is younger than Leia. In fact, for large enough values of $\gamma$ , Luke could return to find Leia long dead. 

This is known as the twin paradox. So far, it is nothing more than the usual time dilation story. So why is it a paradox? Well, things seem puzzling from Luke's perspective. He's sitting happily in his inertial spaceship, watching Leia and the whole planet flying off into space at speed v. From his perspective, it should be Leia who is younger. Surely things should be symmetric between the two? 

The resolution to this “paradox” is that there is no symmetry between Luke’s journey and Leia’s. Leia remained in an inertial frame for all time. Luke, however, does not. When he reaches Tatooine, he has to turn around and this event means that he has to accelerate. This is what breaks the symmetry. 

We can look at this in some detail. We draw the spacetime diagram in Leia's frame, as shown in the figure on the right. Luke sits at $x = vt$ , or $x' = 0$ . Leia sits at $x = 0$ . Luke reaches Tatooine at point $P$ . We've also drawn two lines of simultaneity. 

The point Y is when Leia thinks that Luke has arrived on Tatooine. The point X is where Luke thinks Leia was when he arrived at Tatooine. As we’ve already seen, it’s quite ok for Luke and Leia to disagree on the simultaneity of these points. Let’s figure out the coordinates for X and Y. 

Event Y sits at coordinate $(cT, 0)$ in Leia's frame, while P is at $(cT, vT)$ . The time elapsed in Luke's frame is just the usual time dilation calculation, 

$$
T ^ {\prime} = \gamma \left(T - \frac {v ^ {2} T}{c ^ {2}}\right) = \frac {T}{\gamma}.\tag{11.24}
$$

We can also work out the coordinates of the event X. Clearly this takes place at x = 0 in Leia's frame. In Luke's frame, this is simultaneous with his arrival at Tatooine, and so occurs at $t' = T' = T/\gamma$ . We can again use the Lorentz transformation 

$$
t ^ {\prime} = \gamma \left(t - \frac {v ^ {2} x}{c ^ {2}}\right)\tag{11.25}
$$

now viewed as an equation for t, given x and $t'$ . This gives us 

$$
t = \frac {T ^ {\prime}}{\gamma} = \frac {T}{\gamma^ {2}}.\tag{11.26}
$$

So at this point, we see that everything is indeed symmetric. When Luke reaches Tatooine, he thinks that Leia is younger than him by a factor of $\gamma$ . 

Meanwhile, Leia thinks that Luke is younger than her by the same factor. 

Things change when Luke turns around. 

To illustrate this, let's first consider a different scenario where he doesn't return from Tatooine. Instead, as soon as he arrives, he synchronises his clock with a friend – let's call him Han – who is on his way to meet Leia. Now things are still symmetric. Luke thinks that Leia has aged by $T / \gamma^2$ on the outward journey; Han also thinks that Leia has aged by $T / \gamma^2$ on the inward journey. So where did the missing time go? 

We can see this by looking at the spacetime diagram of Han's journey, as shown in the figure above. We've again drawn lines of simultaneity. From Han's perspective, he thinks that Leia is sitting at point $Z$ when he leaves Tatooine, while Luke is still convinced that she's sitting at point $X$ . It's not hard to check that at point $Z$ , Leia's clock reads $t = 2T - T / \gamma^2$ . 

From this perspective, we can also see what happens if Luke does return home. 

When he arrives at Tatooine, he thinks Leia is at point X. Yet, in the time he takes to turn around and head home, the acceleration makes her appear to rapidly age, from point X to point Z. 

## 11.2.4 Length Contraction

We've seen that moving clocks run slow. We will now show that moving rods are shortened. Consider a rod of length $L'$ sitting stationary in the frame $S'$ . What is its length in frame $S$ ? 

To begin, we should state more carefully something which seems obvious: when we say that a rod has length $L'$ , it means that the distance between the two end points at equal times is $L'$ . So, drawing the axes for the frame $S'$ , in which the rod is stationary, the situation looks like the diagram on the left of Figure 11.5. The two simultaneous end points in $S'$ are $P_{1}$ and $P_{2}$ . Their coordinates in $S'$ are $(ct', x') = (0, 0)$ and $(0, L')$ respectively. 

Fig. 11.5 Length Contraction. On the left, the view from the frame of the rod $S'$ . On the right, the view from the moving frame S. 

Now let's look at this in frame S. This is drawn on the right of Figure 11.5. Clearly $P_{1}$ sits at $(ct, x) = (0, 0)$ . Meanwhile, the Lorentz transformation gives us the coordinate for $P_{2}$ 

$$
x = \gamma L ^ {\prime} \quad \text { and } \quad t = \frac {\gamma v L ^ {\prime}}{c ^ {2}} .\tag{11.27}
$$

But to measure the rod in frame S, we want both ends to be at the same time. And the points $P_{1}$ and $P_{2}$ are not simultaneous in S. We can follow the point $P_{2}$ backwards along the trajectory of the end point to $Q_{2}$ , which sits at 

$$
x = \gamma L ^ {\prime} - v t.\tag{11.28}
$$

We want $Q_{2}$ to be simultaneous with $P_{1}$ in frame S. This means we must move back a time $t = \gamma v L' / c^{2}$ , giving 

$$
x = \gamma L ^ {\prime} - \frac {\gamma v ^ {2} L ^ {\prime}}{c ^ {2}} = \frac {L ^ {\prime}}{\gamma}.\tag{11.29}
$$

This is telling us that the length L measured in frame S is 

$$
L = \frac {L ^ {\prime}}{\gamma}.\tag{11.30}
$$

It is shorter than the length of the rod in its rest frame by a factor of $\gamma$ . This phenomenon is known as Lorentz contraction. 

## Trying to Pop a Balloon

A balloon sits a distance L behind a wall. Your job is to pop the balloon. You have a nail of length l, and there's a small hole in the wall that's big enough for the nail to pass, except for the ridge at the back of the nail which gets stopped by the wall. The question is: can you use the nail to pop the balloon? 

When the nail is longer than the distance to the ballon, so l > L, the answer is obviously yes. But what if l < L? Without the wonders of special relativity, the answer would be obviously no. But maybe we can use length contraction to help us. At first glance, this looks confusing because there are two arguments, each giving the opposite conclusion 

- From the perspective of the balloon, the nail contracts to a length $l / \gamma$ . Now there's no way that the nail is going to stretch the distance $L$ and the balloon can feel safe and smug. 

- From the perspective of the nail, the distance to the balloon has contracted to length $L / \gamma$ . Provided that the nail travels sufficiently fast, so that $\gamma > L / l$ , it will hit the balloon and we will hear a satisfying pop. 

What's going on? We seem to have reached two, physically contradictory, conclusions. Which is right? 

The answer is that the second conclusion is right: the nail does pop the balloon. To see what's wrong with the first argument, we need to think a little more carefully about what's going on. The nail is travelling with speed v and has length l/γ. That means that, from the balloon's reference frame, the back of the nail gets stopped by the wall when the front of the nail is a distance l/γ inside. While the back of the nail gets stopped, it's not possible for the front of the nail to stop immediately, because that would mean an instantaneous communication between the back and the front. So the front of the nail must carry on travelling at speed v until it receives a message from the back to stop. Provided that this message takes long enough, it's possible for the tip of the nail to hit the balloon. This highlights something that we mentioned before: there's no such thing as a "rigid body" in special relativity. Everything can ultimately stretch, or squish, because denying this would be tantamount to instantaneous communication. 

How long is “long enough”? The fastest that the back of the nail can communicate with the front is at speed c. (In reality, the communication travels at speed $c_{s} < c$ , the speed of sound in the nail.) This means that there’s time for the nail to reach the balloon provided that 

$$
\begin{array}{r c l} \frac {L}{c} > \frac {L - l / \gamma}{v} & \Longrightarrow & l > L \sqrt {\frac {1 - v / c}{1 + v / c}} \\ & \Longrightarrow & v > c \sqrt {\frac {1 - l ^ {2} / L ^ {2}}{1 + l ^ {2} / L ^ {2}}}  . \end{array}\tag{11.31}
$$

Our result (11.31) can be written as the requirement $l > L / \gamma (1 + v)$ which is weaker than the result $l > L / \gamma$ that we derived using the second argument. That's because we also assumed that the front and back of the nail stop at the same time in the nail's reference frame. They don't. Again, it takes time for your front end to realise that your back end has stopped. 

## 11.2.5 Addition of Velocities

A particle moves with constant velocity $u'$ in frame $S'$ which, in turn, moves with constant velocity v with respect to frame S. What is the velocity u of the particle as seen in S? 

The Newtonian answer is just $u = u' + v$ . But we know that this can't be correct because it doesn't give the right answer when $u' = c$ . So what is the right answer? 

The worldline of the particle in $S'$ is 

$$
x ^ {\prime} = u ^ {\prime} t ^ {\prime}.\tag{11.32}
$$

So the velocity of the particle in frame S is given by 

$$
u = \frac {x}{t} = \frac {\gamma (x ^ {\prime} + v t ^ {\prime})}{\gamma (t ^ {\prime} + v x ^ {\prime} / c ^ {2})}\tag{11.33}
$$

which follows from the Lorentz transformations (11.13). (Actually, we've used the inverse Lorentz transformations since we want S coordinates in terms of $S'$ coordinates, but these differ only changing -v to v). Substituting (11.32) into the expression above, and performing a little algebra, gives us the result we want 

$$
u = \frac {u ^ {\prime} + v}{1 + u ^ {\prime} v / c ^ {2}}.\tag{11.34}
$$

Note that when $u' = c$ , this gives us u = c as expected. 

We can also show that if $|u'| < c$ and $|v| < c$ then we necessarily have -c < u < c. The proof is simple algebra, if a little fiddly 

$$
c - u = c - \frac {u ^ {\prime} + v}{1 + u ^ {\prime} v / c ^ {2}} = \frac {c (c - u ^ {\prime}) (c - v)}{c ^ {2} + u ^ {\prime} v} > 0\tag{11.35}
$$

where the last equality follows because, by our initial assumptions, each factor in the final expression is positive. An identical calculation will show you that -c < u as well. We learn that, if a particle is travelling slower than the speed of light in one inertial frame, then it will also be travelling slower than light in all others. 

## 11.3 The Geometry of Spacetime

We have seen that time is relative, length is relative, simultaneity is relative. Is nothing sacred anymore? Well, happily, something is. There is one measurement that all observers will agree on. 

## 11.3.1 The Invariant Interval

The views of space and time which I wish to lay before 

you have sprung from the soil of experimental physics, 

and therein lies their strength. They are radical. 

Henceforth space by itself, and time by itself, are doomed 

to fade away into mere shadows, and only a kind of union 

of the two will preserve an independent reality. 

Hermann Minkowski, 1908 

We start by considering a spacetime with just a single spatial coordinate, x. In frame S, two events $P_{1}$ and $P_{2}$ have coordinates $(ct_{1}, x_{1})$ and $(ct_{2}, x_{2})$ . The events are separated by $\Delta t = t_{1} - t_{2}$ in time and $\Delta x = x_{1} - x_{2}$ in space. 

We define the invariant interval $\Delta s^{2}$ as a measure of the distance between these two points 

$$
\Delta s ^ {2} = c ^ {2} \Delta t ^ {2} - \Delta x ^ {2}.\tag{11.36}
$$

The advantage of the invariant interval is that it is something all observers agree upon. In frame $S'$ , we have 

$$
\begin{array}{r l} & {\Delta s ^ {2} = \gamma^ {2} \left(c \Delta t ^ {\prime} + \frac {v \Delta x ^ {\prime}}{c}\right) ^ {2} - \gamma^ {2} \left(\Delta x ^ {\prime} + v \Delta t ^ {\prime}\right) ^ {2}} \\ & {\qquad = \gamma^ {2} (c ^ {2} - v ^ {2}) \Delta t ^ {\prime 2} - \gamma^ {2} \left(1 - \frac {v ^ {2}}{c ^ {2}}\right) \Delta x ^ {\prime 2}} \\ & {\qquad = c ^ {2} \Delta t ^ {\prime 2} - \Delta x ^ {\prime 2}} \end{array}\tag{11.37}
$$

where, in going from the first line to the second, we see that the cross-terms $\Delta t' \Delta x'$ cancel out. 

Including all three spatial dimensions, the definition of the invariant interval is 

$$
\Delta s ^ {2} = c ^ {2} \Delta t ^ {2} - \Delta x ^ {2} - \Delta y ^ {2} - \Delta z ^ {2}\tag{11.38}
$$

which, again, is the same in all frames. The only non-trivial part of the calculation is $(11.37)$ above since y and z are invariant under a boost in the x-direction. 

The spacetime of special relativity is topologically $\mathbb{R}^4$ . When endowed with the measure of distance (11.38), this spacetime is referred to as Minkowski space. Although topologically equivalent to Euclidean space, distances are measured differently. To stress the difference between the temporal and spatial directions, Minkowski space is sometimes said to have dimension $d = 1 + 3$ . (For once, it's important that you don't do this sum!) In later books (in particular, the one on General Relativity), we will write the invariant interval as the distance between two infinitesimally 

close points. In practice that just means we replace all the $\Delta(\text{something})$ s with $d(\text{something})$ s 

$$
d s ^ {2} = c ^ {2} d t ^ {2} - d x ^ {2} - d y ^ {2} - d z ^ {2}.\tag{11.39}
$$

In this infinitesimal form, $ds^{2}$ is called the line element. 

The invariant interval provides an observer-independent characterisation of the distance between any two events. However, it has a strange property: it is not positive definite. Two events whose separation is $\Delta s^{2} > 0$ are said to be timelike separated. They are closer together in space than they are in time. Pictorially, such events sit within each others light cone. 

In contrast, events with $\Delta s^{2} < 0$ are said to be spacelike separated. They sit outside each others light cone. From our discussion in Section 11.2.2, we know that two observers can disagree about the temporal ordering of spacelike separated events. However, they agree on the ordering of timelike separated events. Note that since $\Delta s^{2} < 0$ for spacelike separated events, if you insist on talking about $\Delta s$ itself then it must be purely imaginary. However, usually it will be perfectly fine if we just talk about $\Delta s^{2}$ . 

Finally, two events with $\Delta s^2 = 0$ are said to be lightlike separated. Notice that this is an important difference between the invariant interval and most measures of distance that you're used to. Usually, if two points are separated by zero distance, then they are the same point. This is not true in Minkowski spacetime: if two points are separated by zero distance, it means that they can be connected by a light ray. 

## A Rotational Analogy

There's a simple analogy to understand the meaning of the invariant interval. Let's go back to consider three-dimensional Euclidean space with coordinates $\mathbf{x} = (x, y, z)$ . An observer measures the position of a stationary object – let's say a helicopter – and proudly announces the $x$ , $y$ , and $z$ coordinates of the helicopter. 

Meanwhile, a second observer shares the same origin as the first, but has rotated her axes to use coordinates $\mathbf{x}' = (x', y', z')$ where $x' = Rx$ for some rotation matrix R. She too sees the helicopter and declares that it sits at coordinates $x'$ , $y'$ , and $z'$ . 

Of course, there's no reason why the coordinates of the two observers should agree with each other. However, there is one quantity that should be invariant: the distance from the origin (which is shared by both observers) to the helicopter. In other words, we should find that 

$$
s _ {\mathrm{Euclidean}} ^ {2} = x ^ {2} + y ^ {2} + z ^ {2} = x ^ {\prime 2} + y ^ {\prime 2} + z ^ {\prime 2}\tag{11.40}
$$

And, of course, this is indeed true if the rotation matrix obeys $R^T R = 1$ . 

The essence of special relativity is nothing more than an extrapolation of the discussion above. The Lorentz boosts should be thought of as a rotation between space and time. The individual spatial and temporal coordinates are different for the two observers, but there remains an 

invariant distance. The only thing that's different is that the time and space directions in this invariant distance (11.38) come with different minus signs. We'll shortly explore this analogy between boosts and rotations in some detail. 

## A Headache: The Signature of Spacetime

The key feature of Minkowski space is that distances in time and space are measured with a relative minus sign. But which one should you choose to be positive and which negative? This is a matter of convention and, sadly, it is a convention on which the physics community is split firmly in two! In this book, we choose to put the minus sign in front of the spatial directions, so 

$$
d s ^ {2} = c ^ {2} d t ^ {2} - d x ^ {2} - d y ^ {2} - d z ^ {2}.\tag{11.41}
$$

In this case, spacetime is said to have signature (+---). But you could equally well choose to measure distances as 

$$
d s _ {\mathrm{alternative}} ^ {2} = - c ^ {2} d t ^ {2} + d x ^ {2} + d y ^ {2} + d z ^ {2}.\tag{11.42}
$$

This is signature $(- + + + )$ . Obviously, this is just the negative of (11.41) and some of the definitions that we've used (e.g. for spacelike vs timelike) will have to be amended accordingly. There's no right or wrong choice between (11.41) and (11.42) but you do have to make a choice. 

When we take a deeper dive into the laws of physics, one choice of signature may be more useful than the other. For example, in general relativity we focus on the geometry of spacetime and its useful to pick the mostly plus signature (11.42) so that spatial distances are positive. But in quantum field theory, there are advantages in choosing the mostly minus signature (11.41) as it makes energy and frequencies positive. Ultimately, you just need to get used to both conventions. When reading any textbook or research paper, you should first check to see what their preferred signature is. (I know of one textbook that flips signature halfway through!) 

## 11.3.2 The Lorentz Group

We have defined the interval (11.38) as the measure of distance that is invariant under Lorentz transformations. However, it is actually better to look at things the other way: the invariant interval is the primary object. This is a property of spacetime which defines the Lorentz transformations. Let's see how the argument runs this way around. 

If we sit at the origin in a fixed frame $S$ , the coordinates of an event can be written as a 4-vector $X$ . We won't denote that this vector by bold font or a squiggly line underneath. (We're saving the former for three-dimensional spatial vectors.) We're getting sophisticated now and just the capital letter will have to suffice. The components of the 4-vector are 

$$
X = \left( \begin{array}{c} c t \\ x \\ y \\ z \end{array} \right)  .\tag{11.43}
$$

We will also use index notation and write the components of X as $X^{\mu}$ . Here there is a notational flourish: we take $\mu$ to run over the values 

$$
\mu = 0, 1, 2, 3\tag{11.44}
$$

rather than the more traditional option of 1 to 4. The zeroth component of the vector is highlighting that this corresponds to time (multiplied by c). The invariant distance between the origin and the point P can be written as an inner product, defined as 

$$
X \cdot X = X ^ {T} \eta X = X ^ {\mu} \eta_ {\mu \nu} X ^ {\nu}.\tag{11.45}
$$

In the first expression above we are using matrix-vector notation and in the second we have resorted to index notation, with the summation convention for both indices $\mu$ and $\nu$ . The matrix $\eta$ is given by 

$$
\eta = \left( \begin{array}{c c c c} 1 & 0 & 0 & 0 \\ 0 & - 1 & 0 & 0 \\ 0 & 0 & - 1 & 0 \\ 0 & 0 & 0 & - 1 \end{array} \right)  .\tag{11.46}
$$

This matrix is called the Minkowski metric. With this expression for the Minkowski metric, the inner product becomes 

$$
X \cdot X = c ^ {2} t ^ {2} - x ^ {2} - y ^ {2} - z ^ {2}\tag{11.47}
$$

which is indeed the invariant distance (11.38) between the origin and the point described by X, as promised. 

Following our characterisation of distances using the invariant interval, a 4-vector obeying $X \cdot X > 0$ is said to be timelike, one with $X \cdot X < 0$ is said to be spacelike, and one with $X \cdot X = 0$ is said to be lightlike or, alternatively, null. 

The Lorentz transformation can be thought of as a $4 \times 4$ matrix $\Lambda$ , rotating the coordinates in frame S to coordinates in frame $S'$ , such that the 4-vector becomes 

$$
X ^ {\prime} = \Lambda X.\tag{11.48}
$$

This can also be written in index notation as 

$$
X ^ {\prime \mu} = \Lambda_ {\nu} ^ {\mu} X ^ {\nu}.\tag{11.49}
$$

The Lorentz transformations are defined to be those matrices which leave the inner product invariant. This means that 

$$
X ^ {\prime} \cdot X ^ {\prime} = X \cdot X.\tag{11.50}
$$

From our definition (11.45), we see that this is true only if $\Lambda$ obeys the matrix equation 

$$
\Lambda^ {T} \eta \Lambda = \eta .\tag{11.51}
$$

Let's try to understand the solutions to this. We can start by counting how many we expect. The matrix $\Lambda$ has $4 \times 4 = 16$ components. Both sides of equation (11.51) are symmetric matrices, which means that the equation only provides 10 constraints on the coefficients of $\Lambda$ . We therefore expect to find $16 - 10 = 6$ independent solutions. 

The solutions to $(11.51)$ fall into two classes. The first class is very familiar. They are solutions of the form 

$$
\Lambda = \left( \begin{array}{c c c c} 1 & 0 & 0 & 0 \\ \hline 0 & & \\ 0 & & \mathrm{R} \\ 0 & & \end{array} \right)\tag{11.52}
$$

where R is a $3 \times 3$ matrix. These transformations change space, but leave time intact. The condition (11.51) reduces to a condition for the matrix R, 

$$
R ^ {T} R = \mathbb {1}\tag{11.53}
$$

where the 1 on the right-hand side is the $3 \times 3$ unit matrix. But this is something that we've seen before: it is the requirement for $R$ to be a rotation matrix. There are three such independent matrices, corresponding to rotations about the three different spatial axes. 

The remaining three solutions to $(11.51)$ are the Lorentz boosts that have preoccupied us for much of this chapter. The boost along the x-axis is given by 

$$
\Lambda = \left( \begin{array}{c c c c} \gamma & - \gamma v / c & 0 & 0 \\ - \gamma v / c & \gamma & 0 & 0 \\ \hline 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{array} \right) .\tag{11.54}
$$

These are precisely the Lorentz transformations (11.13). Two further solutions to (11.51) come from boosting along the y- and z-directions. 

The set of all matrices $\Lambda$ obeying (11.51) form the Lorentz group, denoted $O(1,3)$ . You can easily check that they indeed obey all axioms of a group. Taking the determinant of both sides of (11.51), we see that $\det \Lambda^{2} = 1$ , so the Lorentz group splits into two pieces with $\det \Lambda = \pm 1$ . The subgroup with $\det \Lambda = 1$ is called the proper Lorentz group and is denoted $SO(1,3)$ . 

There is one further decomposition of the Lorentz group. Any element can either flip the direction of time or leave it unchanged. Those transformations which preserve the direction of time are called orthochronous. The group of proper orthochronous Lorentz 

transformations is denoted $SO^{+}(1,3)$ although people like me are usually lazy and just refer to it as $SO(1,3)$ . 

## Rapidity

We previously derived the velocity addition law (11.34). Let's see how we get this from the matrix approach above. We can focus on the $2 \times 2$ upper left-hand part of the matrix in (11.54). We'll write this as 

$$
\Lambda [ v ] = \left( \begin{array}{c c} \gamma & - \gamma v / c \\ - \gamma v / c & \gamma \end{array} \right)  .\tag{11.55}
$$

If we combine two boosts, both in the x direction, the resulting Lorentz transformation is 

$$
\Lambda [ v _ {1} ] \Lambda [ v _ {2} ] = \left( \begin{array}{c c} \gamma_ {1} & - \gamma_ {1} v _ {1} / c \\ - \gamma_ {1} v _ {1} / c & \gamma_ {1} \end{array} \right) \left( \begin{array}{c c} \gamma_ {2} & - \gamma_ {2} v _ {2} / c \\ - \gamma_ {2} v _ {2} / c & \gamma_ {2} \end{array} \right)
$$

It takes a little bit of algebra, but multiplying out these matrices you can show that 

$$
\Lambda [ v _ {1} ] \Lambda [ v _ {2} ] = \Lambda \left[ \frac {v _ {1} + v _ {2}}{1 + v _ {1} v _ {2} / c ^ {2}} \right].\tag{11.57}
$$

This is again the velocity addition rule $(11.34)$ , now for the composition of boosts. 

The algebra involved in the above calculation is somewhat tedious, and the result somewhat ugly. But there's a better way to see how this works. We can get a clue from the rotation matrices $R$ . Recall that the $2 \times 2$ matrix which rotates a plane by angle $\theta$ is 

$$
R [ \theta ] = \left( \begin{array}{c c} \cos \theta & \sin \theta \\ - \sin \theta & \cos \theta \end{array} \right)  .\tag{11.58}
$$

If we perform two rotations in succession, we have 

$$
R [ \theta_ {1} ] R [ \theta_ {2} ] = R [ \theta_ {1} + \theta_ {2} ].\tag{11.59}
$$

But the nice addition rule only worked because we were clever in parameterising our rotation by an angle and writing the rotation matrix using cos and sin. In the case of Lorentz boosts, there is a similarly clever parameterisation. Instead of using the velocity v, we define the rapidity $\varphi$ by 

$$
\gamma = \cosh \varphi .\tag{11.60}
$$

The rapidity is a new, dimensionless measure of velocity which ranges over $\varphi\in(-\infty,+\infty)$ , rather than the usual velocity which takes values in $v\in(-c,+c)$ . We can see one of the nice algebraic properties of the rapidity if we look at 

$$
\sinh \varphi = \sqrt {\cosh^ {2} \varphi - 1} = \sqrt {\gamma^ {2} - 1} = \frac {v \gamma}{c}.\tag{11.61}
$$

This is the other component of the Lorentz boost matrix. We can therefore write 

$$
\Lambda [ \varphi ] = \left( \begin{array}{c c} \cosh \varphi & - \sinh \varphi \\ - \sinh \varphi & \cosh \varphi \end{array} \right)  .\tag{11.62}
$$

Looking again at the composition of two Lorentz boosts, we see that the rapidities add, just like the angles of rotation 

$$
\Lambda [ \varphi_ {1} ] \Lambda [ \varphi_ {2} ] = \Lambda [ \varphi_ {1} + \varphi_ {2} ].\tag{11.63}
$$

The matrix description of the Lorentz boost (11.62) shows most clearly the close relationship between rotations and boosts. 

## 11.3.3 A Rant: Why c = 1

We started this chapter by mentioning that the speed of light is exactly $c = 299,792,458 \, m s^{-1}$ . The only reason that this fundamental constant is exactly an integer is because the meter is defined to be the distance travelled by light in 1/299,792,458 seconds. 

In our everyday world, the meter is a very useful unit. It is roughly the size of most things in my house. But viewed from the perspective of fundamental physics, it is rather parochial. If we're going to pick the speed of light to be an integer, we should probably pick one that is easier to remember. Like c = 1. We can do this by picking a different unit of length, namely 

$$
c = 1 \quad (\text { light   second }) \mathrm{s} ^ {- 1}\tag{11.64}
$$

where a light second is the distance travelled by light in one second. 

There's a better way of thinking about this: the existence of a universal speed of light is nature's way of telling us that space and time are more similar than our ancestors realised. We only labelled space and time with different units because we were unaware of the relationship between them. 

We can illustrate this by going back to the rotational analogy. Suppose that you decide that all distances in the x-direction should be measured in centimeters, while all distances in the y-direction should be measured in inches. You then declare that there is a new, fundamental constant of nature – let's call it $\lambda$ – given by 

$$
\lambda \approx 2. 5 4 \mathrm{cm} (\mathrm{inch}) ^ {- 1}\tag{11.65}
$$

Why is this a dumb thing to do? The reason it's dumb is because of the rotational symmetry of the laws of physics: different observers have different $x$ and $y$ coordinates and can quite happily pick the same unit of measurement for both. But we've learned in this chapter that there is also a symmetry between space and time. Insisting that we retain the 

conversion factor c in the fundamental laws of physics is no more sensible than retaining $\lambda$ . 

Despite my rant, in this book, we will retain c in all equations. (Although we will use units which allow us to set $\lambda = 1$ .) But it is a common practice to work with the convention c = 1, and we will do so in some future books. The equations look simpler and the only price you pay is that the units of time and space are equivalent. If, at the end of the day, you want to get your answer in terms of meters or seconds or whatever then you can always put the factors of c back in by dimensional analysis. 

## 11.4 Relativistic Kinematics

So far, our discussion has been focussed on what the world looks like to different observers. Let's now return to the main theme of this book: the motion of particles. Remember that our ultimate goal is to construct laws of physics which look the same to all inertial observers. For this reason, we will start by defining some of the basic elements that go into the laws of physics: velocity, momentum, and acceleration. We want to define these in such a way that they have nice transformation properties when viewed from different inertial frames. 

## 11.4.1 Proper Time

We kicked off this book in Chapter 1 by describing the trajectory of a particle in an inertial frame in terms of a curve $\mathbf{x}(t)$ and velocity $\mathbf{u} = d\mathbf{x}/dt$ . There's nothing incorrect with this description in special relativity but, as we will see, there's a much better way to parameterise the trajectory of a particle. 

Let's start by considering a particle at rest at the origin of frame $S'$ with $\mathbf{x}' = 0$ . The invariant interval between two different points on the worldline of the particle is 

$$
\Delta s ^ {2} = c ^ {2} \Delta t ^ {\prime 2}.\tag{11.66}
$$

We see that the invariant interval between two points on the worldline is proportional to the time experienced by the particle. But, because 

everyone agrees on $\Delta s^2$ , this must be true in all frames. The time experienced by the particle is called the proper time and is denoted $\tau$ . For a particle travelling at constant velocity, the proper time in any inertial frame between two points on the particle's trajectory is 

$$
\Delta \tau = \frac {\Delta s}{c}\tag{11.67}
$$

where $\Delta s$ is real as long as the particle doesn't travel faster than the speed of light, so that it sits on a timelike trajectory. (We keep promising to prove that a particle is unable to travel faster than light...we are almost there!) 

We can us this idea to determine the time experienced by a particle moving along a general trajectory, even one which accelerates and decelerates in some complicated fashion. Viewed from an inertial frame S, along a small segment of its trajectory the particle experiences proper time 

$$
d \tau = \sqrt {d t ^ {2} - \frac {d \mathbf {x} ^ {2}}{c ^ {2}}} = d t \sqrt {1 - \frac {1}{c ^ {2}} \left(\frac {d \mathbf {x}}{d t}\right) ^ {2}} = d t \sqrt {1 - \frac {u ^ {2}}{c ^ {2}}}
$$

from which we have 

$$
\frac {d t}{d \tau} = \gamma_ {u}.\tag{11.69}
$$

Here $\gamma_{u}$ is a function of the speed u of the particle seen by the observer in S. For a general trajectory, the speed u is not constant and so $\gamma_{u} = \gamma_{u}(t)$ . From this, the total time T experienced by a particle as it travels along its worldline is simply the sum of the proper times associated to each small segment, 

$$
T = \int d \tau = \int \frac {d t}{\gamma_ {u}}.\tag{11.70}
$$

Although we calculated this in frame S, we have a similar formula in any other inertial frame, and all inertial observers agree on the time T that the particle itself experienced. 

In this way, proper time provides a way to parameterise the trajectory of a particle in a manner that all inertial observers will agree on. Consider the trajectory of a general particle, not necessarily travelling in a straight line. Viewed from an inertial frame S, the worldline can be parameterised by $\mathbf{x}(\tau)$ and $t(\tau)$ . 

## 11.4.2 4-Velocity

We'll now explain why it's useful to parameterise the trajectory of a particle in terms of proper time $\tau$ . We can write a general trajectory in spacetime using the 4-vector 

$$
X (\tau) = \binom{c t (\tau)}{\mathbf {x} (\tau)}.\tag{11.71}
$$

From this, we can define the 4-velocity 

$$
U = \frac {d X}{d \tau} = \binom{c d t / d \tau}{d \mathbf {x} / d \tau}.\tag{11.72}
$$

Using the relationship (11.69) between the proper time of the particle $\tau$ and the observer's time $t$ we can write this as 

$$
U = \frac {d t}{d \tau} \binom{c}{\mathbf {u}} = \gamma \binom{c}{\mathbf {u}}\tag{11.73}
$$

where $u = d x / dt$ . This definition of the 4-velocity has a nice property: if an observer in frame S measures a particle's 4-velocity as U, then an observer in frame $S'$ with $X' = \Lambda X$ will measure the 4-velocity 

$$
U ^ {\prime} = \Lambda U.\tag{11.74}
$$

This transformation holds only because $d\tau$ is invariant, meaning that it is the same for all observers. In contrast, if we had tried to define a 4-velocity by, say, V = dX/dt then both X and t would change under a Lorentz transformation and we would be left with a messy, complicated expression for V in frame $S'$ . Our definition of U differs from V by the extra factor of $\gamma$ in (11.73). This is all important! 

We now have two objects which transform nicely under Lorentz transformations: the coordinates $X \rightarrow \Lambda X$ and the 4-velocity $U \rightarrow \Lambda U$ . 

Quantities like this are called 4-vectors. It's a name that we've already used to label points in spacetime. More generally, the definition of a 4-vector is any 4-component object $A$ which transforms as $A \to \Lambda A$ under a Lorentz transformation. 

Because of the simple transformation law (11.74), we can immediately import some of the things that we learned from our previous discussion of the Lorentz group. In particular, from the definition of $\Lambda$ given in (11.51), we know that the inner product 

$$
U \cdot U = U ^ {T} \eta U\tag{11.75}
$$

is invariant. It is the same for all observers: $U \cdot U = U' \cdot U'$ . 

Let's look at a simple example. A particle which is stationary in frame $S$ has 4-velocity 

$$
U = \binom{c}{\mathbf {0}}\tag{11.76}
$$

and so $U \cdot U = c^2$ . But this must be true in all frames. We can check this explicitly from (11.73) (we'll take the middle equation to illustrate the point) which gives us 

$$
U \cdot U = \left(\frac {d t}{d \tau}\right) ^ {2} (c ^ {2} - u ^ {2}) = \left(\frac {d t}{d \tau}\right) ^ {2} \frac {c ^ {2}}{\gamma^ {2}} = c ^ {2}.\tag{11.77}
$$

This result also helps answer a puzzle. In Newtonian mechanics, if we want to specify the velocity, then we only have to give three numbers, the components of u. But in special relativity, the velocity is a 4-vector U. Nonetheless, we still only need specify three variables because U is not any 4-vector: it is constrained to obey $U \cdot U = c^{2}$ . 

## Addition of Velocities Revisited

In Section 11.2.5, we derived the rule for the addition of velocities in one dimension. But what if the velocity of a particle is not aligned with the relative velocity between S and $S'$ ? The addition of velocities in this case is simple to compute using 4-vectors. We start with a particle in frame S travelling with 4-velocity 

$$
U = \left( \begin{array}{c} \gamma_ {u} c \\ u \gamma_ {u} \cos \alpha \\ u \gamma_ {u} \sin \alpha \\ 0 \end{array} \right)  .\tag{11.78}
$$

Here we've added the subscript to $\gamma_{u} = (1 - u^{2} / c^{2})^{-1 / 2}$ to distinguish it from the $\gamma$ -factor arising between the two frames. Frame $S'$ moves in the $x$ -direction with speed $v$ relative to $S$ . The Lorentz boost is given in (11.54). In frame $S'$ , the 4-velocity is then 

$$
U ^ {\prime} = \Lambda U = \gamma_ {u} \left( \begin{array}{c} \Big (1 - (u v / c ^ {2}) \cos \alpha \Big) \gamma_ {v} c \\ (u \cos \alpha - v) \gamma_ {v} \\ u \sin \alpha \\ 0 \end{array} \right) = \left( \begin{array}{c} \gamma_ {u ^ {\prime}} c \\ u ^ {\prime} \gamma_ {u ^ {\prime}} \cos \alpha^ {\prime} \\ u ^ {\prime} \gamma_ {u ^ {\prime}} \sin \alpha^ {\prime} \\ 0 \end{array} \right)
$$

Dividing the t - and x-components of this 4-vector, we recover the velocity transformation law (11.34) for the speed in the x-direction, namely 

$$
u ^ {\prime} \cos \alpha^ {\prime} = \frac {u \cos \alpha - v}{1 - u v \cos \alpha / c ^ {2}}.\tag{11.80}
$$

Meanwhile, dividing the y-component by the x-component gives 

$$
\tan \alpha^ {\prime} = \frac {u \sin \alpha}{\gamma_ {v} (u \cos \alpha - v)}.\tag{11.81}
$$

where $\alpha'$ is the angle that the particle's trajectory makes with the $x'$ -axis. 

## 11.4.3 4-Momentum

The 4-momentum is defined by 

$$
P = m U = \binom{m c \gamma}{m \gamma \mathbf {u}}\tag{11.82}
$$

where m is the mass of the particle, usually referred to as the rest mass. Importantly, it will turn out that P is the quantity that is conserved in the relativistic context. The spatial components give us the relativistic generalisation of the 3-momentum 

$$
\mathbf {p} = m \gamma \mathbf {u}.\tag{11.83}
$$

As the particle approaches the speed of light, so $u \rightarrow c$ , the momentum diverges, $p \rightarrow \infty$ . Since momentum is conserved in all processes, this is really telling us that massive particles cannot break the speed of light barrier. (Here the word “massive” doesn’t mean “really really big”: it just means “not massless”, or $m \neq 0$ .) This is sometimes interpreted by viewing the quantity $m\gamma$ as a velocity-dependent relativistic mass. From this perspective, the relativistic mass of the particle diverges $m\gamma \rightarrow \infty$ as the particle approaches the speed of light. The words may be different, but the maths (and underlying physics) is the same: particles are bound by nature’s speed limit. Nothing can travel faster than the speed of light. 

What is the interpretation of the time-component $P^{0}$ of the momentum 4-vector? We can get a hint of this by Taylor expanding the $\gamma$ factor 

$$
P ^ {0} = \frac {m c}{\sqrt {1 - u ^ {2} / c ^ {2}}} = \frac {1}{c} \left(m c ^ {2} + \frac {1}{2} m u ^ {2} + \dots\right).\tag{11.84}
$$

The first term is just a constant. But the second term is something familiar: it is the non-relativistic kinetic energy of the particle. This, coupled with the fact that all four components of P are conserved, strongly suggests that the right interpretation of $P^{0}$ is the energy of the particle (divided by c), so 

$$
P = \binom{E / c}{\mathbf {p}}.\tag{11.85}
$$

The expansion of $(11.84)$ shows that both the mass and the kinetic energy contribute to the energy of a particle. These combine to give 

$$
E = m \gamma c ^ {2}.\tag{11.86}
$$

As the particle approaches the speed of light, its energy diverges. Yet again, we see a barrier to breaking the speed limit: as we approach the speed of light, the energy required to make a particle go just a little faster gets bigger and bigger. 

For a stationary particle, all its energy is contained in its rest mass, giving what is, perhaps, the most famous equation in physics 

$$
E = m c ^ {2}.\tag{11.87}
$$

Famous as it is, this equation tells us only the energy of a stationary particle. This energy is not kinetic energy nor potential energy, but rather something else entirely: it is energy stored in mass. 

There's a nice way to rearrange (11.86), to replace the u in the $\gamma$ factor with p defined in (11.83). If you plough blindly ahead, substituting u for p, then you'll quickly find yourself in an algebraic morass. There is, however, a cute trick that gives the desired result much more quickly. We look at the inner product $P \cdot P$ . In the rest frame of the particle, we have $P = (mc, 0, 0, 0)$ and so 

$$
P \cdot P = m ^ {2} c ^ {2}.\tag{11.88}
$$

But the inner product is an invariant, holding in any frame. From $(11.85)$ , we have 

$$
P \cdot P = \frac {E ^ {2}}{c ^ {2}} - \mathbf {p} ^ {2}.
$$

Equating these two expressions gives 

$$
E ^ {2} = \mathbf {p} ^ {2} c ^ {2} + m ^ {2} c ^ {4}.\tag{11.89}
$$

This is the generalisation of $E = mc^{2}$ to include the kinetic energy. This equation can also be derived the hard way by playing around with $(11.86)$ and $(11.83)$ . 

The identification $P^{0} = E/c$ has dramatic consequences. In Newtonian mechanics, we boasted about the conservation of energy but implicit in everything we did was the more elementary fact that mass is conserved. Even in the variable mass problems of Section 4.3, the mass never disappeared: it just left our rocket ship. However, relativity teaches us that the conservation of mass is subsumed into the conservation of energy. There is nothing that guarantees that mass and energy are individually conserved. Just as potential energy can be converted into kinetic energy, so too can mass be converted into kinetic energy. In Japan, in 1945, this fact was vividly demonstrated. 

It's sometimes easy to forget the power of theoretical physics. We shouldn't. The equations that we've derived throughout this book have changed the direction of human history. 

## Masses of Fundamental Particles

From a fundamental perspective, the equation $E = mc^{2}$ gives a conversion between mass and energy. This is used in the world of particle physics, where masses of particles are usually stated in terms of electronvolts, where 

$$
1 \mathrm{eV} \approx 1. 6 \times 1 0 ^ {- 1 9} \mathrm{J}.\tag{11.90}
$$

The actual mass of the particle is then given by the energy divided by $c^{2}$ . If you want to translate into, say, kilograms then we have 

$$
1 \mathrm{eV} \approx 1. 7 8 \times 1 0 ^ {- 3 6} \mathrm{kg} c ^ {2}.\tag{11.91}
$$

However, there's really no reason to do this translation because kilograms are a stupid unit in which to measure the masses of elementary particles. In fact, electronvolts aren't a whole lot better. An electronvolt is a good measure of the atomic energy scales, while for fundamental particles we typically need $\mathrm{MeV} = 10^{6}$ eV or $\mathrm{GeV} = 10^{9}$ eV. So, for example, the mass of the electron $m_{e}$ and proton $m_{p}$ are given by 

$$
m _ {e} c ^ {2} \approx 0. 5 1 1 \mathrm{MeV} \quad \text { and } \quad m _ {p} c ^ {2} \approx 9 3 8 \mathrm{MeV}.\tag{11.92}
$$

The full nitty gritty details of all elementary particles and their masses will be given in the book on the Standard Model. 

## 11.4.4 Massless Particles

Until now, we built our discussion of particle trajectories on proper time. But looking back at Section 11.4.1, proper time is only defined for timelike trajectories. This is fine for massive particles. But what about for massless particles? We can sidestep the need for proper time by looking at the invariant of the 4-momentum (11.88) which, for particles with m = 0, tells us that the 4-momentum must be null, 

$$
P \cdot P = 0.\tag{11.93}
$$

This means that the 4-momentum of a massless particle necessarily lies along a light ray. 

This fact also allows us to clarify one of our original postulates of special relativity: that the speed of light is the same for all inertial frames. You may wonder why the propagation of light, an electromagnetic phenomenon, is singled out for special treatment. The answer is: because the particle of light, known as the photon, is massless. In fact, a better way of stating the postulate is to say that there is an upper speed limit in the universe, which is the same for all inertial observers. Any massless particle must travel at this speed limit. All massive particles must go slower. 

We know of only two types of massless particles in the universe: the photon and the graviton. Both of these owe their particle-like nature to quantum mechanics (actually, this is true of all particles) and have a classical analogue as light waves and gravitational waves respectively. You’ve all seen light waves (literally!) and individual photons have been routinely measured in experiments for more than a century. Gravitational waves were observed for the first time in 2015, although compelling indirect evidence had existed for decades. There appears to be no hope at all of detecting an individual graviton, at least within our lifetimes. 

Until the late 1990s, it was thought that neutrinos were also massless. It is now known that they have a small, but non-vanishing mass. (Actually, there's a caveat here: there are three different types of neutrino: an 

electron neutrino, a muon neutrino, and a tau neutrino. The differences between their masses are known to be of order of 0.01–0.1 eV and there are constraints which limit the sum of their masses to be no greater than 0.3 eV or so. But the absolute scale of their masses has not yet been determined. It may be that one of the three neutrinos is actually massless.) 

From (11.89), the energy and momentum of a massless particle are related by $E^{2} = p^{2}c^{2}$ . The 4-momentum takes the form 

$$
P = \frac {E}{c} \binom{1}{\hat {\mathbf {p}}}\tag{11.94}
$$

where $\hat{p}$ is a unit vector in the direction of the particle's motion. 

To get an expression for the energy, we need a result from quantum mechanics which relates the energy to the wavelength $\lambda$ of the photon or, equivalently, to the angular frequency $\omega = 2\pi c/\lambda$ . This expression is 

$$
E = \hbar \omega = \frac {2 \pi \hbar c}{\lambda}.\tag{11.95}
$$

There's something rather nice about how this equation ties in with special relativity. Suppose that, in your frame, the photon has energy $E$ . But a different observer moves towards the light with velocity $v$ . By the Lorentz transformation, they will measure the 4-momentum of the photon to be $P' = \Lambda P$ and, correspondingly, will see a bigger energy $E' > E$ . From the above equation, this implies that they will see a smaller wavelength. But this is nothing other than Lorentz contraction. The phenomenon of different observers observing different wavelengths of light is called the Doppler effect. 

## Tachyons and Why They're Nonsense

It is sometimes stated that a particle that has imaginary mass, so that $m^{2} < 0$ , will have $P \cdot P < 0$ and so travel consistently at speeds u > c. Such particles are called tachyons. They too would be unable to cross nature's barrier at u = c and are consigned to always travel on spacelike trajectories. 

Although, consistent within the framework of classical relativistic particle mechanics, the possibility of tachyons does not survive the leap to more sophisticated theories of physics. All our current best theories of physics are written in the framework of quantum field theory. Here particles emerge as ripples of fields, tied into small lumps of energy by quantum mechanics. But in quantum field theory, it is not unusual to have fields with imaginary mass so that $m^2 < 0$ . The resulting particles do not travel faster than the speed of light. Instead, imaginary mass signals an instability of the vacuum. (For what it's worth, there's a sense in which the Higgs boson has $m^2 < 0$ and it certainly doesn't travel faster than the speed of light!) This will be discussed in more detail in the book on the Standard Model. 

## 11.4.5 Newton's Laws of Motion

Finally, we are in a position to write down Newton's equation of motion in a manner that is consistent with special relativity: it is 

$$
\frac {d P ^ {\mu}}{d \tau} = F ^ {\mu}\tag{11.96}
$$

where $F^{\mu}$ are the components of a 4-vector force. It is not difficult to anticipate that the spatial components of F should be related to the 3-vector force f. (This is the same thing that we've been calling F up until now, but we'll lower its standing to a small f to save confusion with the 4-vector). In fact, we need an extra factor of $\gamma$ , so 

$$
F = \binom{F ^ {0}}{\gamma \mathbf {f}}.\tag{11.97}
$$

With this factor of $\gamma$ in place, the spatial components of Newton's equation (11.96) agree with the form that we're used to in the reference frame $S$ , 

$$
\frac {d \mathbf {p}}{d t} = \frac {d \tau}{d t} \frac {d \mathbf {p}}{d \tau} = \frac {1}{\gamma} \frac {d \mathbf {p}}{d \tau} = \mathbf {f}.\tag{11.98}
$$

A quick calculation shows that the temporal component $F^{0}$ is related to the power, which is the rate of change of energy with time 

$$
F ^ {0} = \frac {d P ^ {0}}{d \tau} = \frac {\gamma}{c} \frac {d E}{d t}.\tag{11.99}
$$

With these definitions, we can derive a familiar equation. Consider a particle with constant rest mass m, so that $P \cdot P = m^{2}c^{2}$ is unchanging. Using $P^{0} = m\gamma c$ and $p = m\gamma u$ , we have 

$$
\begin{array}{c} \frac {d}{d \tau} (P \cdot P) = 2 P ^ {0} \frac {d P ^ {0}}{d \tau} - 2 \mathbf {p} \cdot \frac {d \mathbf {p}}{d \tau} \\ = 2 \gamma^ {2} m \left(\frac {d E}{d t} - \mathbf {u} \cdot \mathbf {f}\right) = 0. \end{array}\tag{11.100}
$$

We see that the rate of change of energy is given by 

$$
\frac {d E}{d t} = \mathbf {u} \cdot \mathbf {f}\tag{11.101}
$$

where we recognise the right-hand side as the work done (per unit time). All of this is just to show how the familiar laws of Newtonian physics sit within special relativity. 

## Electromagnetism Revisited

Ironically, equation (11.96) is rarely used in relativistic physics. The reason is that, by the time we are in the relativistic realm, most of the forces that we've come across so far are no longer valid. The one exception is the electromagnetic force law for a particle of charge $q$ that we met in Section 2.4. This does have a relativistic formulation, with the equation of motion given by 

$$
\frac {d P ^ {\mu}}{d \tau} = \frac {q}{c} F _ {\nu} ^ {\mu} U ^ {\nu}\tag{11.102}
$$

where $U^{\nu}$ is the 4-velocity of the particle and $F_{\nu}^{\mu}$ is the electromagnetic tensor, a $4 \times 4$ matrix which contains the electric and magnetic fields arranged as 

$$
F _ {\nu} ^ {\mu} = \left( \begin{array}{c c c c} 0 & E _ {1} & E _ {2} & E _ {3} \\ E _ {1} & 0 & c B _ {3} & - c B _ {2} \\ E _ {2} & - c B _ {3} & 0 & c B _ {1} \\ E _ {3} & c B _ {2} & - c B _ {1} & 0 \end{array} \right)  .\tag{11.103}
$$

The tensor $F_{\nu}^{\mu}$ is not to be confused with the 4-force $F^{\mu}$ : they are related, but are different objects. In an ideal world they would have different names, but as we proceed through this series of books we'll see that the notion of a 4-force $F^{\mu}$ falls by the wayside, while the electromagnetic tensor $F_{\nu}^{\mu}$ will become a familiar friend. Furthermore, we're using a slight abuse of notation in which the $\mu$ and $\nu$ indices are not shown on the right-hand side of (11.103). This too is something you should get used to! The spatial components of the 4-vector equation gives rise to the familiar Lorentz force law (2.74). The temporal component gives the rate of work done, $dE/dt = q\mathbf{E} \cdot \mathbf{u}$ . 

## 11.4.6 Acceleration

We can construct a 4-vector for acceleration by differentiating again with respect to proper time 

$$
A = \frac {d U}{d \tau}.\tag{11.104}
$$

Because $U \cdot U = c^{2}$ , we must have that A is always orthogonal to U in the Minkowski sense: $A \cdot U = 0$ . 

Suppose that the velocity of a particle in frame S is u. Then, in this frame, the Newtonian notion of 3-acceleration is $a = d\mathbf{u}/dt$ . Recalling our expression relating time and proper time, $dt/d\tau = \gamma$ , we see that the 4-acceleration actually depends on both u and a. It is 

$$
A = \gamma \binom{\dot {\gamma} c}{\dot {\gamma} \mathbf {u} + \gamma \mathbf {a}}\tag{11.105}
$$

with $\dot{\gamma}=d\gamma/dt$ . 

Let's now suppose that we sit in an inertial frame $S'$ in which, at a fixed moment of time $t$ , the particle is instantaneously at rest. If the particle is accelerating, then this frame $S'$ will not coincide with the particle's rest frame an instant later, but momentarily this will do fine. Since $\mathbf{u}' = 0$ in this frame, the 4-acceleration is 

$$
A ^ {\prime} = \binom{0}{\mathbf {a} ^ {\prime}}\tag{11.106}
$$

with $a' = du' / dt'$ . (You need to do a small calculation here to check that $\dot{\gamma}(u = 0) = 0$ .) But, since we have constructed our acceleration as a 4-vector, A and $A'$ must be related by a Lorentz transformation. To make matters easy for ourselves, let's take both u and a to lie in the x-direction so that we can consistently ignore the y and z-directions. 

Then the Lorentz transformation tells us 

$$
\begin{array}{c} A = \gamma \binom{\dot {\gamma} c}{\dot {\gamma} u + \gamma a} = \left( \begin{array}{c c} \gamma & u \gamma / c \\ u \gamma / c & \gamma \end{array} \right) \binom{0}{a ^ {\prime}} \\ = \binom{u \gamma a ^ {\prime} / c}{\gamma a ^ {\prime}}. \end{array}\tag{11.}
$$

From the top component, we can determine the relationship between the accelerations $a$ and $a'$ seen in the two frames 

$$
a = \dot {u} = \left(1 - u ^ {2} / c ^ {2}\right) ^ {3 / 2} a ^ {\prime}.\tag{11.108}
$$

Suppose now that the particle undergoes constant acceleration. As with everything in special relativity, we need to be more careful about what we mean by this. The natural interpretation is that the acceleration in the frame of the particle is constant. Mathematically, this means that $a'$ is constant. In contrast, viewed from frame S, the acceleration is not constant. Indeed, for constant $a'$ , we can integrate our equation above to get u, the velocity seen in frame S, as a function of time. If we assume that u = 0 when t = 0, we have 

$$
u = \frac {a ^ {\prime} c t}{\sqrt {c ^ {2} + a ^ {\prime 2} t ^ {2}}} \quad \Longrightarrow \quad \gamma (t) = \sqrt {1 + \frac {a ^ {\prime 2} t ^ {2}}{c ^ {2}}}.\tag{11.]}
$$

Since $u = \dot{x}$ , integrating the first of these equations once more gives us the position in the frame S as a function of time 

$$
x = \frac {c}{a ^ {\prime}} \left(\sqrt {c ^ {2} + a ^ {2} t ^ {2}} - c\right)\tag{11.110}
$$

where we've picked an integration constant so that $x = 0$ at time $t = 0$ . We see that the particle moves on the hyperbola shown in the figure below. Viewed from $S$ , the particle approaches, but never reaches, the speed of light. 

There's some interesting physics here. 

A particle at point P in the diagram can only receive information from within its own past lightcone. This means that, if the particle continues along its accelerated trajectory, then there's a whole part of spacetime – everything that sits to the left of the dotted null line x = ct – that is inaccessible to the particle. This part of the universe will forever remain a mystery to an accelerated observer. The null cone, defined by x = ct, which forms the boundary of the mysterious region is called the Rindler event horizon. It has many things in common with the event horizon of a black hole, in the sense that the region inside a black hole horizon is inaccessible to an observer who sits outside. Indeed, the Rindler horizon is often used as a toy model to understand some of the stranger aspects of black hole physics. Of course, if an accelerated observer really wants to see what's behind the horizon, it's easy: he just stops accelerating. If an observer in the background of a black hole wants to see what's behind the horizon, he must be somewhat braver. 

We can look at what the accelerated observer feels. His time is simply the proper time of the particle. To compute this, the form of $\gamma(t)$ given in (11.109) is particularly useful. From (11.70), if time t elapses in the stationary frame S, then the particle feels 

$$
\tau = \int_ {0} ^ {t} \frac {c d \tilde {t}}{\sqrt {c ^ {2} + a ^ {\prime 2} \tilde {t} ^ {2}}} = \frac {c}{a ^ {\prime}} \sinh^ {- 1} \left(\frac {a ^ {\prime} t}{c}\right).\tag{11.111}
$$

This analysis gives us a more quantitative way to view the twin paradox. Suppose that Luke undertakes his trip to Tatooine on a trajectory of constant acceleration. He leaves Leia at the time t < 0 where their worldlines intersect, arrives at Tatooine at t = 0 and $x = c^{2}/a'$ , and returns back to Leia as shown in the figure to the right. (The direction of the journey has been flipped relative to our previous twin discussion.) Leia experiences time t, Luke time $\tau < t$ . 

Finally, we can look at how far the accelerated observer thinks he has travelled. Of course, this observer is not in an inertial frame, but at any time t we can consider the inertial frame that is momentarily at rest with respect to the accelerated particle. This allows us to simply use the Lorentz contraction formula. Using our results $(11.109)$ and $(11.110)$ , we have 

$$
x ^ {\prime} = \frac {x}{\gamma} = \frac {c ^ {2}}{a ^ {\prime}} \left(1 - \frac {c}{\sqrt {c ^ {2} + a ^ {\prime 2} t ^ {2}}}\right) .\tag{11.112}
$$

Curiously, $x' \rightarrow c^{2}/a'$ is finite as $t \rightarrow \infty$ or, equivalently, as $\tau \rightarrow \infty$ . Despite all that effort, an accelerated observer doesn't think he has got very far! This again, is related to the presence of the horizon. 

## 11.4.7 Indices Up, Indices Down

The minus signs in the Minkowski metric $\eta = \mathrm{diag}(+1, -1, -1, -1)$ means that it's useful to introduce a slight twist to the usual summation convention of repeated indices. For all the 4-vectors that we introduced above, we were careful to always place the spacetime index $\mu = 0, 1, 2, 3$ as a superscript (i.e up) rather than a subscript. We have 

$$
X ^ {\mu} = (c t, \mathbf {x}).\tag{11.113}
$$

This is because the same object with an index down, $X_{\mu}$ , will mean something subtly different! 

$$
X _ {\mu} = (c t, - \mathbf {x}).\tag{11.114}
$$

With this convention, the Minkowski inner product can be written using the usual convention of summing over repeated indices as 

$$
X ^ {\mu} X _ {\mu} = c ^ {2} t ^ {2} - \mathbf {x} \cdot \mathbf {x}.\tag{11.115}
$$

In contrast, $X^{\mu}X^{\mu} = c^{2}t^{2} + x^{2}$ is a dumb thing to write in the context of special relativity because it looks very different to observers in different inertial frames. In fact, we will shortly declare it illegal to write things like $X^{\mu}X^{\mu}$ . 

There is a natural way to think of $X_{\mu}$ in terms of $X^{\mu}$ . If we write the Minkowski metric as the diagonal matrix $\eta_{\mu\nu} = \text{diag}(+1, -1, -1, -1)$ , then we can raise and lower indices using $\eta_{\mu\nu}$ and the summation convention, so 

$$
X _ {\mu} = \eta_ {\mu \nu} X ^ {\nu}.\tag{11.116}
$$

To raise indices back up, we need the inverse of $\eta_{\mu\nu}$ which, fortunately, is the same matrix: $\eta^{\mu\nu} = \text{diag}(+1, -1, -1, -1)$ . We have 

$$
\eta^ {\mu \rho} \eta_ {\rho \nu} = \delta_ {\nu} ^ {\mu}.\tag{11.117}
$$

This means that we can easily get back to $X^{\mu}$ by writing $X^{\mu} = \eta^{\mu\nu} X_{\nu}$ . 

The indices of any other relativistic object can be similarly raised or lowered by contracting with $\eta$ . For example, we could rewrite the electromagnetic tensor defined in $(11.103)$ as 

$$
F ^ {\mu \nu} = F _ {\rho} ^ {\mu} \eta^ {\rho \nu} = \left( \begin{array}{c c c c} 0 & - E _ {1} & - E _ {2} & - E _ {3} \\ E _ {1} & 0 & - c B _ {3} & c B _ {2} \\ E _ {2} & c B _ {3} & 0 & - c B _ {1} \\ E _ {3} & - c B _ {2} & c B _ {1} & 0 \end{array} \right)  .\tag{:}
$$

The object $F^{\mu\nu}$ is actually somewhat more natural than $F_{\nu}^{\rho}$ because the former is anti-symmetric. 

This trick of distinguishing between indices up and indices down provides a simple formalism to ensure that all objects have nice transformation properties under the Lorentz group. We insist that, just as in the usual summation convention, repeated indices only ever appear in pairs. But now we further insist that pairs always appear with one index up and the other down. The result will be an object that is either invariant or covariant under Lorentz transformations. 

This convention, where the up/down placement of indices holds meaning, will be developed further in subsequent books, starting with Volume 2 on Electromagnetism. Later still, in the book on General Relativity, we will learn that there is somewhat deeper mathematics lying behind distinguishing $X^{\mu}$ and $X_{\mu}$ . Formally, these objects live in different spaces (sometimes called dual spaces). Objects such as $X^{\mu}$ are said to be contravariant vectors, while $X_{\mu}$ is said to be a covariant vector. 

## 11.5 Particle Physics

Oh, that stuff. We never bother with that in our work. 

Ernest Rutherford's attitude to relativity. 

Our goal in this section is to describe various relativistic phenomena that arise in particle physics. All these processes occur in the absence of external forces, so F = 0 and we will rely only on conservation of 4-momentum, meaning 

$$
\frac {d P}{d \tau} = 0.\tag{11.119}
$$

Here, conservation of 4-momentum includes both conservation of 3-momentum and conservation of energy. 

The calculations that follow are similar in spirit to the collision calculations of Section 4.2. Before we proceed, there are a couple of hints that may help when solving these problems. First, we need to choose a frame of reference in which to calculate and the smart frame to choose is nearly always the centre of mass of the system (which should more correctly be called the centre of momentum frame, for it is the one with vanishing spatial 3-momentum). Second, you will often be presented with a situation where there is one particle with momentum P about which you know nothing. A good way to eliminate this is often to rearrange your equation so it takes the form $P = \ldots$ and then square it to get the left-hand side to be $P \cdot P = m^{2}c^{2}$ , thereby eliminating the velocity and 

energy of the particle you know nothing about in one swoop. Let's now see how this works in a few examples. 

## 11.5.1 Particle Decay

Consider a single particle with rest mass $m_{1}$ that decays into two particles with rest masses $m_{2}$ and $m_{3}$ . Conservation of 4-momentum tells us 

$$
P _ {1} = P _ {2} + P _ {3}\tag{11.120}
$$

or, equivalently, 

$$
E _ {1} = E _ {2} + E _ {3} \quad \text { and } \quad \mathbf {p} _ {1} = \mathbf {p} _ {2} + \mathbf {p} _ {3} .\tag{11.121}
$$

In the rest frame of the decaying particle, we can write (using $(\underline{11.89})$ ), 

$$
E _ {1} = m _ {1} c ^ {2} = \sqrt {p _ {2} ^ {2} c ^ {2} + m _ {2} ^ {2} c ^ {4}} + \sqrt {p _ {3} ^ {2} c ^ {2} + m _ {3} ^ {2} c ^ {4}} \geq m _ {2} c ^ {2} + m _ {3} c ^ {2}
$$

which tells us the unsurprising result that a particle can only decay if its mass is greater than that of its decay products. With a little algebra, it's straightforward to show that the velocities $v_{2}$ and $v_{3}$ of the decay products in the centre-of-mass frame are given by 

$$
\gamma_ {2} = \frac {m _ {1} ^ {2} + m _ {2} ^ {2} - m _ {3} ^ {2}}{2 m _ {1} m _ {2}} \quad \mathrm{and} \quad \gamma_ {3} = \frac {m _ {1} ^ {2} + m _ {3} ^ {2} - m _ {2} ^ {2}}{2 m _ {1} m _ {3}}.\tag{1}
$$

We can look at some twists on this story. 

## An Example: Higgs Decay

The LHC has taught us that the Higgs boson has mass $m_{h}c^{2} \approx 125$ GeV. It mostly decays into two photons. In particle physics, photons are always denoted by $\gamma$ . (Do not confuse them with the Lorentz contraction factor!) The “equations” in which the photon $\gamma$ ’s appear are more like chemical reactions than true equations. The decay of the Higgs into two photons is written as 

$$
h \to \gamma \gamma .\tag{11.123}
$$

Similar decays occur for other particles, most notably the neutral pion, a meson (meaning that it is made of a quark and an anti-quark) with mass $m_{\pi}c^{2} \approx 140$ MeV. This too decays as $\pi^{0} \rightarrow \gamma\gamma$ . 

To be concrete, we'll focus on the Higgs. Conservation of 4-momentum tells us that 

$$
P _ {h} = P _ {\gamma} + P _ {\gamma} ^ {\prime}\tag{11.124}
$$

where $P_{h}$ is the 4-momentum of the Higgs, and $P_{\gamma}$ and $P_{\gamma}^{\prime}$ are the 4-momenta of the two photons. If we sit in the rest frame of the Higgs, so $P_{h}^{\mu} = (m_{h}c, 0)$ , then the photons must have equal and opposite 3-momentum and, therefore, equal energy $E_{\gamma} = \frac{1}{2}m_{h}c^{2}$ . The photons must be emitted back-to-back but, because the problem is rotationally symmetric, can be emitted at any angle. 

What if we're not sitting in the rest frame of the Higgs? Suppose that the Higgs has energy $E_h$ and the energy of one of the photons is measured to be $E_\gamma$ . What is the angle $\theta$ that this photon makes with the path of the Higgs? 

We'll use the strategy that we described above. We have no information about the second photon with 4-momentum $P_{\gamma}'$ . So we rearrange the conservation of momentum to read $P_{\gamma}' = P_h - P_{\gamma}$ . Upon squaring this, we have $P_{\gamma}' \cdot P_{\gamma}' = 0$ , so 

$$
\begin{array}{r l} & 0 = (P _ {h} - P _ {\gamma}) \cdot (P _ {h} - P _ {\gamma}) \\ & \quad = P _ {h} \cdot P _ {h} + P _ {\gamma} \cdot P _ {\gamma} - 2 P _ {h} \cdot P _ {\gamma} \\ & \quad = m _ {h} ^ {2} c ^ {2} - \frac {2 E _ {h} E _ {\gamma}}{c ^ {2}} + 2 \mathbf {p} _ {h} \cdot \mathbf {p} _ {\gamma} \\ & \quad = m _ {h} ^ {2} c ^ {2} - \frac {2 E _ {h} E _ {\gamma}}{c ^ {2}} + \frac {2 E _ {\gamma}}{c} \cos \theta \sqrt {E _ {h} ^ {2} / c ^ {2} - m _ {h} ^ {2} c ^ {2}} \end{array}\tag{11.}
$$

where, in the last equality, we have used $E^{2} = p^{2}c^{2} + m^{2}c^{4}$ , which is just E = pc for the photon. This can now be rearranged to give the answer for the angle $\theta$ . 

## 11.5.2 Particle Collisions

We now turn to the physics of relativistic collisions. We'll collide two particles together, both of mass $m$ . They interact in some manner, preserving both energy and 3-momentum, and scatter at an angle $\theta$ . The incoming momenta are $P_{1}$ and $P_{2}$ , the outgoing momenta $P_{3}$ and $P_{4}$ . Conservation implies 

$$
P _ {1} + P _ {2} = P _ {3} + P _ {4}.\tag{11.126}
$$

As we mentioned previously, it's easiest to see what happens in the centre-of-mass frame. Without loss of generality, we take the initial momenta to be in the $x$ -direction. After the collision, the particles must have equal and opposite momenta which means they must also have equal energy. This, in turn, ensures that, in the centre-of-mass frame, the speed $v$ after the collision is the same as before. We can choose our axes so that the initial and final momenta are given by 

$$
\begin{array}{r l} & P _ {1} ^ {\mu} = (m c \gamma_ {v}, m v \gamma_ {v}, 0, 0) \\ & P _ {2} ^ {\mu} = (m c \gamma_ {v}, - m v \gamma_ {v}, 0, 0) \\ & P _ {3} ^ {\mu} = (m c \gamma_ {v}, m v \gamma_ {v} \cos \theta , m v \gamma_ {v} \sin \theta , 0) \\ & P _ {4} ^ {\mu} = (m c \gamma_ {v}, - m v \gamma_ {v} \cos \theta , - m v \gamma_ {v} \sin \theta , 0) \end{array}\tag{11.127}
$$

where we've put the subscript on $\gamma_v$ to denote its argument. These momenta are shown on the left of Figure 11.6. 

Fig. 11.6 Collisions in the centre-of-mass frame on the left, and the lab frame on the right 

We can also look at the same collision in the lab frame. This refers to the situation where one of the particles is initially at rest (presumably in your lab). By the velocity addition formula, the other particle must start with speed 

$$
u = \frac {2 v}{1 + v ^ {2} / c ^ {2}}.\tag{11.128}
$$

You can also derive this result by writing down the momenta $P_{1}^{\prime}$ and $P_{2}^{\prime}$ in the lab frame and equating $(P_{1} + P_{2})^{2} = (P_{1}^{\prime} + P_{2}^{\prime})^{2}$ . 

In the lab frame, the angles $\phi$ and $\alpha$ at which the particles scatter are not equal, as shown on the right of Figure 11.6. They can be easily determined using the addition of 4-velocities that we saw in Section 11.4.2. Set u = -v in equation (11.81) and use the identity $\tan(x/2) = \sin x/(1 + \cos x)$ to get 

$$
\tan \phi = \frac {1}{\gamma_ {v}} \tan \theta / 2 \quad \mathrm{and} \quad \tan \alpha = \frac {1}{\gamma_ {v}} \tan (\theta / 2 + \pi / 2).
$$

This relates the two scattering angles $\phi$ and $\alpha$ in the lab frame to the scattering angle $\theta$ in the centre-of-mass frame. 

## Compton Scattering

A particularly interesting example of a collision arises when a photon bounces off an electron. This is known as Compton scattering. Suppose that the photon enters the collision with some 3-momentum p, aligned along the x-axis, and leaves with some 3-momentum q, deflected by an angle $\phi$ . The initial and final 4-momenta are 

$$
P _ {\gamma} = p (1, 1, 0, 0) \quad \mathrm{and} \quad P _ {\gamma} ^ {\prime} = q (1, \cos \phi , \sin \phi , 0).\tag{11}
$$

Meanwhile the electron starts out at rest. Its initial and final 4-momentum are then 

$$
P _ {e} = (m c, 0, 0, 0) \quad \text { and } \quad P _ {e} ^ {\prime} = \gamma (m c, m v \cos \alpha , m v \sin \alpha) .
$$

Conservation of 4-momentum gives $P_{e} + P_{\gamma} = P_{e}' + P_{\gamma}'$ . Rearranging and squaring, we have 

$$
(P _ {\gamma} - P _ {\gamma} ^ {\prime}) ^ {2} = (P _ {e} - P _ {e} ^ {\prime}) ^ {2} \Rightarrow - 2 P _ {\gamma} \cdot P _ {\gamma} ^ {\prime} = 2 m ^ {2} c ^ {2} - 2 P _ {e} \cdot P _ {e} ^ {\prime}
$$

A little bit of algebra then shows that this gives the relation 

$$
2 \sin^ {2} (\phi / 2) = m c \left(\frac {1}{p} - \frac {1}{q}\right).\tag{11.133}
$$

This is a nice result. On the right-hand side, we have the change of the momentum of the photon. But, because this is light, that's equivalent to the change in the wavelength, or the colour, of the photon. The expression above relates this change of wavelength to the scattering angle $\phi$ in the lab frame. 

## Particle Creation

Just as mass can be converted into kinetic energy, so kinetic energy can be converted into mass through the creation of new particles. Roughly speaking, this is the way we discover new fundamental particles of nature. 

Suppose that we collide two particles, each of mass m. After the collision, we hope to be left with these two particles, together with a third of mass M. How fast must the original two particles collide? 

Conservation of momentum gives us 

$$
P _ {1} + P _ {2} = P _ {3} + P _ {4} + P _ {5}\tag{11.134}
$$

where $P_{1}^{2}=P_{2}^{2}=P_{3}^{2}=P_{4}^{2}=m^{2}c^{2}$ , while $P_{5}^{2}=M^{2}c^{2}$ . Let's work in the centre-of-mass frame of the colliding particles, each of which has speed v. In this case, we have 

$$
(P _ {1} + P _ {2}) ^ {2} = 4 m ^ {2} \gamma_ {v} ^ {2} c ^ {2} = (P _ {3} + P _ {4} + P _ {5}) ^ {2}.\tag{11.135}
$$

Since we're in the centre-of-mass frame, the final momenta must take the form $P_{3} + P_{4} + P_{5} = ((E_{1} + E_{2} + E_{3}) / c, \mathbf{0})$ so that 

$$
(P _ {3} + P _ {4} + P _ {5}) ^ {2} = \frac {1}{c ^ {2}} (E _ {1} + E _ {2} + E _ {3}) ^ {2} \geq \frac {1}{c ^ {2}} (2 m c ^ {2} + M c ^ {2}) ^ {2}
$$

where, for each particle, we've used the fact that 

$E = \sqrt{m^2c^4 + p^2c^2}\geq mc^2$ . Substituting this into (11.135) gives 

$$
4 m ^ {2} \gamma_ {v} ^ {2} c ^ {2} \geq 4 m ^ {2} c ^ {2} + M ^ {2} c ^ {2} + 4 M m c ^ {2} \Rightarrow \gamma_ {v} \geq 1 + \frac {M}{2 m}.
$$

This makes sense. The minimum amount of kinetic energy per particle is $T = \gamma_{v} mc^{2} - mc^{2} = \frac{1}{2} Mc^{2}$ . With this minimum amount, the two colliding particles can combine their kinetic energies to form the new particle. After the collision, all three particles are then at rest. 

It's worth mentioning another way to do the above computation. Suppose that you hadn't noticed that the 3-momentum of $P_3 + P_4 + P_5$ vanished and instead expanded out the right-hand side of (11.135) to end up with nine terms. Things are a bit harder this way, but all is not lost. We can apply a Cauchy-Schwarz-like inequality to each of these terms. For any massive particles with 4-momenta $P$ and $Q$ , such that $P^2 = m_1^2 c^2$ and $Q^2 = m_2^2 c^2$ , we necessarily have $P \cdot Q \geq m_1m_2c^2$ . The simplest way to 

prove this statement is by working in a frame in which one particle is stationary. Then we have 

$$
\begin{array}{c} P \cdot Q = \left( \begin{array}{c} m _ {1} c \\ 0 \end{array} \right) \cdot \left( \begin{array}{c} E _ {2} / c \\ p _ {2} \end{array} \right) \\ = m _ {1} E _ {2} = m _ {1} \sqrt {m _ {2} ^ {2} c ^ {4} + p _ {2} ^ {2} c ^ {2}} \geq m _ {1} m _ {2} c ^ {2}. \end{array}\tag{11.13}
$$

Applied to $(11.135)$ this once again gives $(11.137)$ . 

What if we re-do this experiment in the lab frame, in which one of the original particles is at rest and the other has speed u? Now we have $P_{1} = (m\gamma_{u}c, m\gamma_{u}u)$ and $P_{2} = (mc, 0)$ , so 

$$
(P _ {1} + P _ {2}) ^ {2} = P _ {1} ^ {2} + P _ {2} ^ {2} + 2 P _ {1} \cdot P _ {2} = 2 m ^ {2} c ^ {2} + 2 m ^ {2} \gamma_ {u} c ^ {2}.
$$

But we don't have to compute $(P_{3} + P_{4} + P_{5})^{2}$ again because the beauty of taking the square of the 4-momenta is that the result is frame independent. We have 

$$
\begin{array}{r l} & 2 m ^ {2} c ^ {2} + 2 m ^ {2} \gamma_ {u} c ^ {2} \geq 4 m ^ {2} c ^ {2} + M ^ {2} c ^ {2} + 4 M m c ^ {2} \\ \Longrightarrow & \gamma_ {u} \geq 1 + \frac {2 M}{m} + \frac {M ^ {2}}{2 m ^ {2}}. \end{array}
$$

Now we see that it's not so easy to create a particle. It's certainly not enough to give the incoming particle kinetic energy $T = \frac{1}{2} Mc^2$ , or even $T = Mc^2$ , as you might intuitively expect. Instead, if you want to create very heavy particles, $M \gg m$ , you need to give your initial particle a kinetic energy of order $T \approx M^2 c^2 / 2m$ . This scales quadratically with $M$ , rather than the linear scaling that we saw in the centre-of-mass frame. The reason for this is simple: there's no way that the end products can be at rest. The need to conserve momentum means that much of the kinetic energy of the incoming particle goes into producing kinetic energy of the outgoing particles. 

This simple calculation brings with it a whole lot of technological pain. When particle physics was in its infancy, new particles were discovered in what we’ve called the lab frame. This means that you use an accelerator to create a beam of particles and then smash it into a stationary target, say a lump of lead sitting at the far end of your lab. The advantage of this is that it’s very hard to miss a lump of lead. The disadvantage, as we’ve seen, is that much of the energy of the beam is wasted as it goes into the kinetic energy of whatever new particle you created. 

By the early 1970s, it became clear that more energy was needed, prompting the move to particle colliders, in which two different beams, each with the same energy, are coaxed to hit each other. That's not an easy thing to do. Now you're not aiming your elementary particle at a lump of lead, but instead at another elementary particle. Imagine how accurate you need to be! And yet it's worth the effort just so that all the kinetic energy can be harnessed to create something new and exciting. The first particle to be discovered this way was the charm quark. 

Our best current collider is the LHC in CERN. Its day job is to collide two beams of protons and look through the wreckage to gain insight into the properties of the new particles, such as the Higgs boson, that are created. However, for one month a year, the LHC switches its beams to lead nuclei in an attempt to understand a new form of matter known as the quark-gluon plasma. Each lead nuclei contains around 200 protons and neutrons. The collision results in a dramatic demonstration of particle creation, with the production of many thousands of particles – protons, neutrons, mesons, and baryons. One of the first collisions of lead nuclei at the LHC is shown in Figure 11.7, captured in all its glory by the ALICE detector. 

Fig. 11.7 Particle creation at the LHC. 

## 11.6 Lagrangians and Hamiltonians

So far, we've set up the kinematics of a relativistic particle. Our next question is: How do we write down a Lagrangian or Hamiltonian that describes these particles? In this section, we give the answer. 

I should warn you that we won't solve anything new with this technology. We will, however, see that the Lagrangian has a number of rather novel features. Its importance lies, in part, in the fact that these features are repeated in more advanced laws of physics, specifically various field theories. The relativistic particle provides a simple setting in which to explore these ideas and understand how to interpret them. 

We can start by writing down a naive action principle for a free, relativistic particle. This is 

$$
S [ \mathbf {x} (t) ] = - m c ^ {2} \int d t \sqrt {1 - \frac {\dot {\mathbf {x}} ^ {2}}{c ^ {2}}} .\tag{11.141}
$$

This looks promising for a few reasons. First, if we Taylor expand the action we get 

$$
S [ \mathbf {x} (t) ] = \int d t \left[ - m c ^ {2} + \frac {1}{2} m \dot {\mathbf {x}} ^ {2} + \dots \right].\tag{11.142}
$$

The first term has an obvious interpretation as the -V term in the action, but now with $V = mc^{2}$ a constant that doesn't affect the equation of 

motion. Meanwhile, the second term is the familiar action for a free, non-relativistic particle. The ... are then corrections that kick in as the particle gets close to the speed of light. Next, we can look at the canonical momentum. It is 

$$
\mathbf {p} (t) = \frac {\partial L}{\partial \dot {\mathbf {x}} (t)} = m \gamma \dot {\mathbf {x}} (t) \quad \mathrm{with} \quad \gamma = \sqrt {\frac {1}{1 - \dot {\mathbf {x}} ^ {2} / c ^ {2}}} .\tag{1}
$$

This is indeed the right momentum (11.83) for a relativistic particle, replete with the correct gamma factor. This means that we get the right equation of motion for a free particle, namely $d_{p}/dt = 0$ . 

All of this means that there's a lot to like about the simple action (11.141). It gives the right answers. However, there's also something more than a little unsatisfactory about it because it doesn't seem to embrace the spirit of special relativity. This is because the action (11.141) is written for an observer in a very particular reference frame, with a very particular choice of time coordinates $t$ . It's not at all obvious why the action is invariant under Lorentz transformations that relate different observers. That's particularly embarrassing because we spent a large part of Chapter 7 bragging about how well adapted the Lagrangian formalism is to exhibiting symmetries. 

We can do better. Our goal is to write down an action principle that holds for observers in any reference frame. 

## 11.6.1 The Covariant Action

First, we can see why it might be tricky to write down an action that holds in any reference frame. From our discussion earlier in this chapter, if we want Lorentz transformations to be manifest, then we should think about the whole 4-vector $X^{\mu} = (ct, \mathbf{x})$ , rather than just the position $\mathbf{x}(t)$ . We will then write down an action that depends on the trajectory $X^{\mu}$ that the particle makes in spacetime. To do this, we first need to parameterise the worldline of the particle. We'll call this parameter $\sigma$ and think of the trajectory of the particle as tracing out a worldline $X^{\mu}(\sigma)$ in spacetime. 

But this means that the degrees of freedom for our relativistic particle are very different from those of a non-relativistic particle. For a non-relativistic particle, the action is a function of $\mathbf{x}(t)$ . But for a relativistic particle, the action is a function of $\mathbf{x}(\sigma)$ and $t(\sigma)$ for some parameter $\sigma$ . This means that we have one more degree of freedom, $t(\sigma)$ , for the relativistic particle. In addition, we've got to introduce this new parameter $\sigma$ that describes where we are on the worldline. Yet, despite these differences, the relativistic action should reduce to the non-relativistic action when the speed of a particle is small. How can we achieve all these things? 

The answer to this is rather nice. It's simplest if we just write down the action and then explore its properties. The better action for a relativistic particle is a functional of the trajectory $X^{\mu}(\sigma)$ , given by 

$$
S [ X ^ {\mu} (\sigma) ] = - m c \int_ {\sigma_ {1}} ^ {\sigma_ {2}} d \sigma \sqrt {\eta_ {\mu \nu} \frac {d X ^ {\mu}}{d \sigma} \frac {d X ^ {\nu}}{d \sigma}}\tag{11.144}
$$

where, as before, $\eta_{\mu\nu} = \text{diag}(+1, -1, -1, -1)$ is the Minkowski metric. There are a number of interesting properties of (11.144). First, it is manifestly invariant under Lorentz transformations. These are symmetries of the form 

$$
X ^ {\mu} \to \Lambda_ {\nu} ^ {\mu} X ^ {\nu} \quad \mathrm{with} \quad \Lambda_ {\mu} ^ {\rho} \eta_ {\rho \sigma} \Lambda_ {\nu} ^ {\sigma} = \eta_ {\mu \nu}.\tag{11.145}
$$

You can see by inspection that this leaves the action (11.144) unchanged. For this reason, (11.144) is known as the covariant action. 

In fact, we've already met the action (11.144) before: it is the proper time (11.70) experienced by a particle that moves along the worldline $X^{\mu}(\sigma)$ , 

$$
\tau (\sigma) = \frac {1}{c} \int_ {0} ^ {\sigma} d \sigma^ {\prime} \sqrt {\eta_ {\mu \nu} \frac {d X ^ {\mu}}{d \sigma^ {\prime}} \frac {d X ^ {\nu}}{d \sigma^ {\prime}}} .\tag{11.146}
$$

The lesson of the twin paradox of Section 11.2.3 is that the dull stay-at-home twin ages fastest. In other words, the proper time is maximised by a particle that does not accelerate. This sits nicely with the fact that the proper time is identified with the action and hence is extremised on solutions to the equations of motion which, for a free particle, are precisely those that travel at a constant velocity. 

In addition to Lorentz invariance, the action (11.144) has a second symmetry of a very different kind, and this is the key to understanding its properties. This second symmetry is reparameterisation invariance. So far, we didn't say how we picked the parameterisation $\sigma$ of the worldline. Suppose that we made a different choice and parameterised the worldline by a different coordinate $\tilde{\sigma}$ , related to the first parameterisation by a monotonic function $\tilde{\sigma}(\sigma)$ . Then we could equally as well construct an action $\tilde{S}$ using this new parameter, given by 

$$
\tilde {S} = - m c \int_ {\tilde {\sigma} _ {1}} ^ {\tilde {\sigma} _ {2}} d \tilde {\sigma} \sqrt {\eta_ {\mu \nu} \frac {d X ^ {\mu}}{d \tilde {\sigma}} \frac {d X ^ {\nu}}{d \tilde {\sigma}}} .\tag{11.147}
$$

We might worry that this different parameterisation will give different equations of motion. Happily this is not the case because the two actions are, in fact, identical. This follows from the fact that the action is equal to an intrinsic property of the particle, namely its proper time. Or alternatively, it follows from a quick calculation: 

$$
\tilde {S} = - m c \int_ {\sigma_ {1}} ^ {\sigma_ {2}} d \sigma \frac {d \tilde {\sigma}}{d \sigma} \sqrt {\eta_ {\mu \nu} \frac {d X ^ {\mu}}{d \sigma} \frac {d X ^ {\nu}}{d \sigma} \left(\frac {d \sigma}{d \tilde {\sigma}}\right) ^ {2}} = S.\tag{1}
$$

We see that the action takes the same form regardless of our choice of parameterisation. Although we’ve called this a “symmetry”, it’s not a symmetry in the same sense as Lorentz transformations. In particular, reparameterisation does not generate new solutions from old ones. Instead, it is a redundancy in the way we describe the system. It is similar in spirit to the gauge “symmetry” (7.166) of electromagnetism which, despite the name, is also a redundancy rather than a symmetry. 

Reparameterisation invariance has a number of consequences. The first is that it explains why the action $(11.144)$ has only three degrees of freedom, even though it is a function of four variables $X^{\mu}(\sigma)$ with $\mu = 0, 1, 2, 3$ . 

This is because one of the degrees of freedom $X^{\mu}$ is not physical. Suppose that you solve the equation of motion to find a trajectory $X^{\mu}(\sigma)$ . In most dynamical systems, each of these four functions would tell you something about the physical trajectory. But, for us, reparameterisation invariance means that there is no actual information in the value of $\sigma$ . To find the physical path, we should eliminate $\sigma$ to find the relationship between the $X^{\mu}$ . And this removes one degree of freedom. 

We can see this most clearly by making a cunning choice for the parameter $\sigma$ that parameterises the worldline. Suppose that we choose $\sigma$ to coincide with the time t for some intertial observer: $\sigma = t$ . Then $dX^{0}/d\sigma = c$ and the action (11.144) then becomes 

$$
S = - m c ^ {2} \int_ {t _ {1}} ^ {t _ {2}} d t \sqrt {1 - \frac {\dot {\mathbf {x}} ^ {2}}{c ^ {2}}}\tag{11.149}
$$

where, here, $\dot{x} = d\mathbf{x}/dt$ . But this is the action (11.141) that we started this section with. So our two actions (11.144) and (11.141) are indeed equivalent, but each has different advantages. The action (11.141) makes it clear that we are dealing with a system with three degrees of freedom x, but Lorentz invariance is hidden. Meanwhile the action (11.144) has manifest Lorentz invariance, but at the cost of introducing more degrees of freedom than are physical. But, as we've seen above, the reparameterisation invariance of the action then allows us to remove the time degree of freedom and return to (11.141). 

There's yet another manifestation of reparameterisation invariance. To see this, we compute the canonical momentum associated to $X^{\mu}$ , 

$$
P _ {\mu} = \frac {\partial L}{\partial \dot {X} ^ {\mu}} = - m c \frac {1}{\sqrt {\dot {X} ^ {\nu} \dot {X} _ {\nu}}} \dot {X} _ {\mu}\tag{11.150}
$$

where, here, $\dot{X}^{\mu} = \partial X^{\mu}/\partial\sigma$ . You can check that this coincides with the usual definition of 4-momentum $P^{\mu} = mdX^{\mu}/d\tau$ . (This follows from the fact that the proper time $\tau$ defined by (11.146) obeys $d\tau/d\sigma = L/mc^{2}$ with L the Lagrangian.) We've already seen in (11.88) that these momenta are not all independent, but obey 

$$
\eta^ {\mu \nu} P _ {\mu} P _ {\nu} = m ^ {2} c ^ {2}.\tag{11.151}
$$

While this result is familiar in special relativity, it's rather surprising from the perspective of Lagrangian mechanics. In all the other examples that we've met, the canonical momenta are independent of each other. But not here. This novel feature can be traced to the existence of reparameterisation invariance, meaning that there was a redundancy in our original description. Indeed, whenever theories have such a redundancy there will be some constraint analogous to (11.151). As one final comment, note that if we expand out (11.151), we have 

$$
(P ^ {0}) ^ {2} = \mathbf {p} ^ {2} + m ^ {2} c ^ {2}.\tag{11.152}
$$

In particular, we see that we must have $P^{0} \neq 0$ . This is important. There's nothing that tells us that we must have $p \neq 0$ and that's to be expected: the particle is quite able to just sit still in space if it wants. But $P^{0} \neq 0$ tells us that $\dot{X}^{0} = dX^{0}/d\sigma \neq 0$ so the particle is obliged to move in the time direction. Physically, this again reflects the fact that the action (11.144) has only three degrees of freedom, not four. Physiologically, this is why you get old. 

So far, our covariant action (11.144) only describes a free, relativistic particle. But it's straightforward to couple it to relativistic forces. The most obvious such force is electromagnetism and here there is a nice interplay with relativity. It turns out that the potentials $\phi$ and $\mathbf{A}$ that we introduced in (7.165) sit nicely in a 4-vector $A_{\mu} = (\phi / c, -\mathbf{A})$ , known as a gauge field. If the particle carries electric charge $q$ , then it couples to the electromagnetic field through the action 

$$
S [ X ^ {\mu} (\sigma) ] = \int_ {\sigma_ {1}} ^ {\sigma_ {2}} d \sigma \left[ - m c \sqrt {\eta_ {\mu \nu} \frac {d X ^ {\mu}}{d \sigma} \frac {d X ^ {\nu}}{d \sigma}} - q A _ {\mu} (X) \frac {d X ^ {\mu}}{d \sigma} \right].
$$

If we again pick the worldline parameter $\sigma$ to coincide with the time of some inertial observer, $\sigma = t$ , then the calculation that previously led us to the action (11.149) will now include the additional terms of the electromagnetic action (7.167). We will explore this action further in Volume 2 on Electromagnetism. 

## Ein Einbein

Our covariant action (11.144) has a lot of nice properties. Unless, that is, you're a massless particle, in which case the action vanishes courtesy of the $m$ that sits in front. If we want an action for a massless particle, we need to try something else. 

To achieve this, we will think of the trajectory of the particle in spacetime $X^{\mu}(\sigma)$ but, in addition, introduce one further variable on the worldline $e(\sigma)$ , which is known as an einbein. We then consider the action 

$$
S = \frac {1}{2} \int d \sigma \left(e ^ {- 1} \eta_ {\mu \nu} \dot {X} ^ {\mu} \dot {X} ^ {\nu} - e m ^ {2}\right).\tag{11.154}
$$

Here $\dot{X}^{\mu}=dX^{\mu}/d\sigma$ . This form of the action will look more familiar if you’ve done a little differential geometry. (This will be covered in the book on General Relativity.) It looks very much like we’ve coupled the worldline of the particle to a kind of 1d gravity, with the field $e(\sigma)$ acting as an einbein (in the sense of vierbeins that are introduced in general relativity). To see this, note that we could change notation and write this action in the more suggestive form 

$$
S = - \frac {1}{2} \int d \sigma \sqrt {- g _ {\sigma \sigma}} \left(g ^ {\sigma \sigma} \dot {X} ^ {2} + m ^ {2}\right)\tag{11.155}
$$

where $g_{\sigma \sigma} = (g^{\sigma \sigma})^{-1}$ is the metric on the worldline and $e = \sqrt{-g_{\sigma\sigma}}$ . 

Our action (11.154) appears to have yet another degree of freedom $e(\sigma)$ . But this doesn't have any dynamics associated with it because there's no $\dot{e}$ term in the action. Instead, the equation of motion for $e(\sigma)$ fixes it in terms of what $X^{\mu}(\sigma)$ is doing, with 

$$
\dot {X} \cdot \dot {X} + e ^ {2} m ^ {2} = 0.\tag{11.156}
$$

Substituting this into the action (11.154) recovers the covariant action (11.144). 

The action (11.154) has a couple of advantages over (11.144). First, it works for massless particles with $m = 0$ . Second (and somewhat tangentially for our current purposes), the absence of the annoying square root means that it's easier to quantise in a path integral framework. 

The action (11.154) retains invariance under reparameterisations which are now written in a form that looks more like general relativity. For transformations parameterised by an infinitesimal $\epsilon$ , we have 

$$
\sigma \rightarrow \tilde {\sigma} = \sigma - \epsilon (\sigma), \quad \delta e = \frac {d}{d \sigma} (\epsilon (\sigma) e), \quad \delta X ^ {\mu} = \frac {d X ^ {\mu}}{d \sigma} \epsilon (\sigma).
$$

Again, if you've got some differential geometry behind you, you can see that the einbein $e$ transforms as a density on the worldline. 

## 11.6.2 The Hamiltonian for a Relativistic Particle

We now turn to the Hamiltonian for a relativistic particle. Here, too, we will see something interesting. 

First, we could look at the Lagrangian (11.141) that holds in a particular reference frame. Inverting the momentum (11.143), we have 

$$
\dot {\mathbf {x}} = \frac {\mathbf {p}}{\sqrt {m ^ {2} + \mathbf {p} ^ {2} / c ^ {2}}} .\tag{11.158}
$$

The Hamiltonian is then 

$$
H (\mathbf {x}, \mathbf {p}) = \mathbf {p} \cdot \dot {\mathbf {x}} - L = m c ^ {2} \gamma .\tag{11.159}
$$

This we recognise as the energy of a relativistic particle. So far, so good. 

The second, covariant action (11.144) is more subtle. We computed the conjugate momentum in (11.150). This gives us the Hamiltonian 

$$
H = P _ {\mu} \dot {X} ^ {\mu} - L = 0.\tag{11.160}
$$

Wait. What? That's certainly unexpected: the Hamiltonian for the covariant action vanishes! 

What's going on here is that the Hamiltonian governs evolution with respect to the appropriate “time” coordinate which, in the present case, is the label $\sigma$ on the worldline. But the label $\sigma$ is a coordinate that has no independent meaning. And the way the formalism deals with this is by handing us a Hamiltonian H = 0 which is telling us that there is no evolution with respect to $\sigma$ . This is also related to the fact that the covariant Lagrangian is not, in fact, convex in $\dot{X}^{\mu}$ . 

Instead, you have to look elsewhere for the dynamics when working in the Hamiltonian formulation of the covariant action. And the right place is in the constraint (11.151) that tell us $P_{\mu}P^{\mu}=mc^{2}$ . As we saw above, this is the equation that drives the particle forward in the timelike direction. This is the dynamics. 

It turns out that these kind of issues raise their heads whenever we have a theory with reparameterisation invariance and, to a lesser extent, when we have a theory with gauge symmetry. In particular, the Hamiltonian for general relativity turns out to be H = 0. Again, the physics is hiding in the constraints. For Maxwell theory, the Hamiltonian is non-vanishing but there are also constraints that arise from gauge symmetry that complicate the issue. These issues will be discussed in later books. 

## 11.7 The Lorentz Group and $SL(2, \mathbb{C})$

In this final section, we return to understand more of the mathematical structure underlying spacetime and the Lorentz group. Ultimately, the new structure that we will uncover here has very important implications for the way the universe works. But we will also see a nice application of our new tools. 

Let's start by recalling our definition of the Lorentz group. We introduced elements of the group as $4 \times 4$ real matrices satisfying 

$$
\Lambda^ {T} \eta \Lambda = \eta\tag{11.161}
$$

where $\eta = \text{diag}(1, -1, -1, -1)$ is the diagonal Minkowski metric. Elements with $\det \Lambda = +1$ define the group $SO(1, 3)$ . If we further restrict to elements with the upper-left component $\Lambda_{0}^{0} > 0$ , which ensures that the transformation does not flip the direction of time, then we have the sub-group $SO^{+}(1, 3)$ . As we will now see, there's some rather beautiful subtleties associated with this group. 

## 11.7.1 A New Way of Looking at Spacetime

The Lorentz group $SO^{+}(1,3)$ is (almost) the same as the rather different looking group $SL(2,\mathbb{C})$ , the group of $2 \times 2$ complex matrices with determinant 1. We will start by providing the map between these two groups and explaining what the word “almost” means. 

Before we talk about Lorentz transformations, let's first go back to think about the points in Minkowski space themselves. So far, we've been labelling these by the 4-vector $X^{\mu} = (ct, x, y, z)$ . But there is alternative way of labelling these points, not by a 4-vector but instead by a $2 \times 2$ Hermitian matrix. Given a 4-vector $X$ , we can write down such a matrix $\hat{X}$ by 

$$
\hat {X} = \left( \begin{array}{c c} c t + z & x - i y \\ x + i y & c t - z \end{array} \right)\tag{11.162}
$$

which clearly satisfies $\hat{X} = \hat{X}^{\dagger}$ . Moreover, this is the most general form of a $2 \times 2$ 

Hermitian matrix. This means that there is a one-to-one map between 4-vectors X and $2 \times 2$ Hermitian matrices. We can equally well take the latter to define a point in Minkowski space. 

We learned earlier that Minkowski space comes equipped with an inner product structure on 4-vectors. The inner product $X \cdot X$ measures the distance in spacetime between the origin and the point X. But this is very natural in terms of the matrix language: it is simply the determinant 

$$
X \cdot X = \det \hat {X} = c ^ {2} t ^ {2} - x ^ {2} - y ^ {2} - z ^ {2}.\tag{11.163}
$$

With this new way of labelling points in Minkowski space, using the matrices $\hat{X}$ , we can return to think about Lorentz transformations. Recall that, by definition, a Lorentz transformation is a linear map that preserves the inner-product structure on Minkowski space. Let's consider a general matrix $A \in SL(2, \mathbb{C})$ , which means that $\det A = 1$ . We can use this to define a linear map 

$$
\hat {X} \rightarrow \hat {X} ^ {\prime} = A \hat {X} A ^ {\dagger}.\tag{11.164}
$$

By construction, if $\hat{X} = \hat{X}^{\dagger}$ then we also have $\hat{X}' = (\hat{X}')^{\dagger}$ , so $\hat{X}'$ also defines a point in Minkowski space. Moreover, 

$$
\det \hat {X} ^ {\prime} = \det \left(A \hat {X} A ^ {\dagger}\right) = \det A \det X \det A ^ {\dagger} = \det X
$$

where the last equality follows because $\det A = 1$ . This means that the map (11.164) preserves the inner product on Minkowski space and therefore defines a Lorentz transformation. 

We may wonder if all Lorentz transformations can be implemented by suitable choices of $A$ . The answer is yes. We'll exhibit the map explicitly below, but first let's just count the dimension of the two groups to make sure we stand a chance of it working. A general $2 \times 2$ complex matrix has four complex entries. The requirement that its determinant is 1 reduces this to three complex parameters, or six real parameters. This agrees with the dimension of the Lorentz group: $6 = 3$ rotations + 3 boosts. 

Although the dimensions of $SO^{+}(1,3)$ and $SL(2,\mathbb{C})$ are equal, they are not quite the same groups. In some sense, $SL(2,\mathbb{C})$ is twice as big. The reason is that the matrices A and -A both implement the same Lorentz transformation in (11.164). We say that $SL(2, \mathbb{C})$ is the double cover of $SO^{+}(1,3)$ or, alternatively 

$$
S O ^ {+} (1, 3) \cong S L (2, \mathbb {C}) / \mathbb {Z} _ {2}.\tag{11.166}
$$

Mathematically, there is a 2:1 group homomorphism between $SL(2,\mathbb{C})$ and $SO^{+}(1,3)$ . The word “homomorphism” means that the group structure is preserved under this map. The existence of this double cover leads to some quite extraordinary consequences. But, before we get to these, let’s first just look at how the map works in more detail. 

## Rotations

We've seen that points in Minkowski space can be written as a 4-vector $X$ or Hermitian matrix $\hat{X}$ . Meanwhile, Lorentz transformations act as $X \to \Lambda X$ or $\hat{X} \to A\hat{X}A^{\dagger}$ . Here we would like to be more explicit about which matrices $A$ correspond to the different Lorentz transformations. 

We start with rotations. By definition, these are the transformations that leave time untouched. From $(11.164)$ , this means that we want matrices A which map the spatial origin $\hat{X} = ct \mathbb{1}$ to itself, where 1 here is the unit $2 \times 2$ matrix. In other words, rotations should obey 

$$
A A ^ {\dagger} = \mathbb {1}.\tag{11.167}
$$

But such matrices are familiar unitary matrices. We learn that rotations sit in the subgroup $A \in SU(2) \subset SL(2, \mathbb{C})$ . You may be used to thinking of the rotation group as $SO(3)$ rather than $SU(2)$ . But these are almost the same thing: $SU(2)$ is the double cover of $SO(3)$ 

$$
S O (3) \cong S U (2) / \mathbb {Z} _ {2}.\tag{11.168}
$$

Let's see how this equivalence between matrices $R \in SO(3)$ and $A \in SU(2)$ works. For rotations around the $x$ -axis, we have 

$$
R = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & \cos \theta & \sin \theta \\ 0 & - \sin \theta & \cos \theta \end{array} \right) \quad \longleftrightarrow \quad A = \pm \left( \begin{array}{c c} \cos (\theta / 2) & i \sin (\theta / 2) \\ i \sin (\theta / 2) & \cos (\theta / 2) \end{array} \right)
$$

To see this, you just need to substitute the matrix A into the map $(11.164)$ and check that it reproduces the same rotation as the matrix R. Note the all-important $\pm$ possibility on A, which reflects the fact that $SL(2, \mathbb{C})$ is the double cover of the Lorentz group so that there are two different $A \in SU(2)$ matrices that correspond to the same $R \in SO(3)$ matrix. This is also related to the fact that the angle in A is $\theta/2$ rather than $\theta$ : we will return to this shortly. For rotations about the y-axis, we have 

$$
R = \left( \begin{array}{c c c} \cos \theta & 0 & - \sin \theta \\ 0 & 1 & 0 \\ \sin \theta & 0 & \cos \theta \end{array} \right) \quad \longleftrightarrow \quad A = \pm \left( \begin{array}{c c} \cos (\theta / 2) & \sin (\theta / 2) \\ - \sin (\theta / 2) & \cos (\theta / 2) \end{array} \right)
$$

Finally, for rotations about the $z$ -axis, we have 

$$
R = \left( \begin{array}{c c c} \cos \theta & \sin \theta & 0 \\ - \sin \theta & \cos \theta & 0 \\ 0 & 0 & 1 \end{array} \right) \quad \longleftrightarrow \quad A = \pm \left( \begin{array}{c c c} e ^ {i \theta / 2} & 0 \\ 0 & e ^ {- i \theta / 2} \end{array} \right)
$$

There's a somewhat nicer way of writing these matrices which makes their structure clearer. To see this, we first need to introduce the Pauli matrices, 

$$
\sigma^ {1} = \left( \begin{array}{c c} 0 & 1 \\ 1 & 0 \end{array} \right)    ,    \sigma^ {2} = \left( \begin{array}{c c} 0 & - i \\ i & 0 \end{array} \right)    ,    \sigma^ {3} = \left( \begin{array}{c c} 1 & 0 \\ 0 & - 1 \end{array} \right)    .
$$

Together with the unit matrix, these form a basis of $2 \times 2$ Hermitian matrices. They have the nice property that $\sigma^{i}\sigma^{j} = \delta^{ij} + i\epsilon^{ijk}\sigma^{k}$ . In general, a rotation by angle $\theta$ around an axis with unit vector $\vec{n}$ is associated to the unitary matrix 

$$
A = \pm \exp \left(\frac {i \theta}{2} n ^ {i} \sigma^ {i}\right).\tag{11.171}
$$

The above was for rotations $R \in SO(3)$ , but it's straightforward to embed this in the larger Lorentz group. The matrix A remains unchanged, while the Lorentz transformation $\Lambda$ is constructed by embedding the orthogonal matrix R in the lower-right block, as shown in (11.52). 

## Boosts

The Pauli matrices also provide a simple way to describe the matrices $A \in SL(2, \mathbb{C})$ corresponding to Lorentz boosts. A boost with rapidity $\varphi$ in the direction $\vec{n}$ is implemented by 

$$
A = \pm \exp \left(- \frac {\varphi}{2} n ^ {i} \sigma^ {i}\right).\tag{11.172}
$$

Unlike rotations, these matrices are not unitary. This ensures that they affect the time component. 

Again, you can check that $(11.172)$ reproduces the Lorentz boosts of the form $(11.62)$ simply by substituting this expression for A into the map $(11.164)$ . For example, a boost in the z-direction is given by the matrix 

$$
A = \left( \begin{array}{c c} e ^ {- \varphi / 2} & 0 \\ 0 & e ^ {+ \varphi / 2} \end{array} \right) \implies A \hat {X} A ^ {\dagger} = \hat {X} ^ {\prime} = \left( \begin{array}{c c} e ^ {- \varphi} (t + z) & x - i y \\ x + i y & e ^ {+ \varphi} (t - z) \end{array} \right)
$$

This tells us that $x$ and $y$ are left unchanged, while $t' + z' = e^{-\varphi}(t + z)$ and $t' - z' = e^{+\varphi}(t - z)$ . Doing the algebra gives 

$$
t ^ {\prime} = \cosh \varphi t - \sinh \varphi z, \qquad z ^ {\prime} = \cosh \varphi z - \sinh \varphi t\tag{1}
$$

which indeed agrees with the usual form of the Lorentz transformation (11.62) written in terms of the rapidity. 

## 11.7.2 What the Observer Actually Observes

There's a rather nice application of the above formalism. In Section 11.2, when we first encountered relativistic phenomena such as length contraction, we stressed that different observers ascribe different coordinates to spacetime events. But this is not the same thing as what the observer actually sees because this also involves the time that the light took to travel from the event to the observer. So this leaves open the question: What does an observer observe? What do Lorentz contracted objects really look like? As we will now show, writing the Lorentz group as $SL(2,\mathbb{C})$ gives a wonderfully elegant way to answer this question. Moreover, what we will find is somewhat surprising. 

What an observer actually sees are, of course, light rays. As objects move through Minkowski space, they emit light which then propagates to the position of the observer. This is sketched in the two diagrams in Figure 11.8, both of which have the observer placed at the origin of Minkowski space. We've also drawn the future and past lightcones emitted from the origin. 

Fig. 11.8 The celestial sphere, on the past light cone, as seen by two different observers. 

In the left-hand diagram, the observer is assumed to be stationary with time coordinate t. At each fixed moment in time t, the light rays form a sphere $S^{2}$ . This is drawn as the circle in the past lightcone of the diagram. If we assume that no other object comes between this sphere and the observer, then the light rays intersecting the sphere are a good representation of what the observer actually sees. If they take a snapshot of everything around them with some really super-dooper fancy camera, then they would record the image on this sphere. This is sometimes given the name of the celestial sphere, reflecting the fact that this is how we should think of viewing the night sky (at least if the Earth wasn't obscuring half of it). 

Let's now look at what an observer in a different inertial frame sees. This is shown in the right-hand diagram of Figure 11.8. This second observer will also take a snapshot using their fancy camera as they pass through the origin. But this new observer's celestial sphere is given by null rays that sit at $t' = \text{constant}$ . Although it's no longer obvious from the picture, we know that the space defined by the intersection of light rays with the constant $t'$ hyperplane must still be a sphere simply because all inertial observers are equivalent. However, this new celestial sphere is tilted with respect to the previous one. 

The four light rays drawn in the figure intersect both celestial spheres. These light rays therefore provide a map between what the two observers see. This is a map between the two celestial spheres, $S^{2} \rightarrow S^{2}$ . Our goal is to construct this map. 

This is where our new mathematical formalism comes in. Any point on a light ray is, by definition, at vanishing distance from the origin when measured in the Minkowski metric. Equivalently, the $2 \times 2$ Hermitian matrix $\hat{X}$ describing this point must have vanishing determinant. But there's a nice way to write down such matrices with zero determinant. We introduce a two-component complex vector, $\xi_{\alpha}$ with $\alpha = 1, 2$ . Then we write 

$$
\hat {X} = \xi \xi^ {\dagger} = \left( \begin{array}{c c} | \xi_ {1} | ^ {2} & \xi_ {1} \xi_ {2} ^ {\dagger} \\ \xi_ {2} \xi_ {1} ^ {\dagger} & | \xi_ {2} | ^ {2} \end{array} \right)\tag{11.174}
$$

which, by construction, obeys $\det \hat{X} = 0$ . It's simple to check that the most general Hermitian matrix $\hat{X}$ with $\det \hat{X} = 0$ and non-negative trace can be written in this way. (The non-negative trace condition means that $\hat{X}$ lives in the future lightcone. We can always parameterise the past lightcone by $\hat{X} = -\xi\xi^{\dagger}$ .) Note, however, that there's a redundancy in this description, since if we rotate both components of $\xi$ by a phase, so that $\xi \to e^{i\beta}\xi$ , then $\hat{X}$ remains unchanged. 

## An Aside: The Hopf Map

In our new notation, the celestial sphere at constant time t is simply given by 

$$
\xi^ {\dagger} \xi = | \xi_ {1} | ^ {2} + | \xi_ {2} | ^ {2} = \mathrm{constant}.\tag{11.175}
$$

There's actually some interesting maths in this statement. It's obvious that given two complex variables $\xi_1$ and $\xi_2$ , the equation (11.175) defines a three-dimensional sphere $\mathbf{S}^3$ . What's perhaps less obvious, but nonetheless true, is that if we identify all points on $\mathbf{S}^3$ related by $\xi \to e^{i\beta}\xi$ , then we get a two-dimensional sphere $\mathbf{S}^2$ . In mathematical language, we say that $\mathbf{S}^3 / U(1) \cong \mathbf{S}^2$ . 

It's simple to write directly the map $\mathbf{S}^3\to \mathbf{S}^2$ . Given a complex 2-vector $\xi$ , obeying $\xi^{\dagger}\xi = 1$ , you can define three real numbers $k^{i}$ by 

$$
k ^ {i} = \xi^ {\dagger} \sigma^ {i} \xi\tag{11.176}
$$

where $\sigma^{i}$ are the three Pauli matrices (11.170). Then a little algebra shows that $k^{i}k^{i}=1$ . In other words, $k^{i}$ gives a point on $S^{2}$ . This map from $S^{3}$ to $S^{2}$ is called the Hopf map. 

## Back to the Real World

Let's now use these new objects $\xi$ to construct the map between the two celestial spheres. A nice fact is that Lorentz transformations act in a natural way on the two-component $\xi$ . To see this, recall that 

$$
\hat {X} ^ {\prime} = \xi^ {\prime} \xi^ {\prime \dagger} = A \xi \xi^ {\dagger} A ^ {\dagger}.\tag{11.177}
$$

But we can view this as a transformation of $\xi$ itself. We have simply the $SL(2, \mathbb{C})$ transformation 

$$
\xi^ {\prime} = A \xi .\tag{11.178}
$$

However, this is not quite our mapping. We can start with a celestial sphere defined by $(11.175)$ and act with a Lorentz transformation. The trouble is that the resulting space we get remains the first celestial sphere, just written in the second observer's coordinates. We still need to propagate the light rays forward and backwards so that they intersect the second celestial sphere. 

To avoid this complication, it's best to think about these celestial spheres in a slightly different way. Rather than saying that they are defined at constant time, let's instead define them as equivalence classes of light rays. This means that we lose the information about where we are along the light ray: we only keep the information about which light ray we're talking about. Mathematically, this is very simple: to each $\xi = (\xi_1, \xi_2)$ we associate a single complex number $\omega \in \mathbb{C}$ by 

$$
\omega = \frac {\xi_ {1}}{\xi_ {2}}.\tag{11.179}
$$

The map from the celestial sphere $S^{2} \rightarrow C$ is known as stereographic projection and is shown in Figure 11.9. Strictly speaking, $\omega$ parameterises $C \cup \{\infty\}$ , with the point at infinity included to accommodate the point $\xi_{2} = 0$ , which is the North pole of the celestial sphere. This extended complex plane is called the Riemann sphere. 

Fig. 11.9 The stereographic projection. The southern hemisphere is mapped to inside the dotted circle; the northern hemisphere is mapped to outside this circle. 

Now the light rays seen by the first observer are labelled by $\omega \in C$ and form a celestial sphere. The light rays seen by the second observer are labelled by $\omega' = \xi_{1}' / \xi_{2}'$ and form a different celestial sphere. A Lorentz transformation $A \in SL(2, \mathbb{C})$ acts on $\xi$ as (11.178) which, in terms of $\omega$ , reads 

$$
\omega^ {\prime} = \frac {a \omega + b}{c \omega + d} \quad \text {where} A = \left( \begin{array}{c c} a & b \\ c & d \end{array} \right) \text {and} a d - b c = 1.
$$

This transformation on the complex plane is known as a Möbius transformation. It's simple to see that Möbius transformations form a group. In fact, from what we've seen above, you shouldn't be surprised to learn that the group of Möbius transformations is $SL(2,\mathbb{C})$ , up to a discrete $\mathbb{Z}_2$ identification. 

Suppose now that the first observer sees an object on their celestial sphere that traces out some shape. After stereographic projection, that will result in a shape on the complex plane (perhaps passing through the point at infinity). This appears to the second observer to be transformed by $(11.180)$ . Upon taking the inverse stereographic projection, we will learn what shape the second observer really sees. 

To make progress, we should look at a simple example. And the simplest example is an object which is itself a sphere. This means that, when stationary with respect to the first observer, the outline of the object looks like a circle. What does the second observer see? To answer this, I'll need to invoke some simple facts about stereographic projection and Möbius transformations. 

- The stereographic projection maps circles on the sphere to circles or lines on the plane. 

- Möbius transformations map circles and lines on the plane to circles or lines on the plane. 

Hiding behind these facts is the statement that both maps are conformal, meaning that they preserve angles. But, for us, the upshot is that a circle on the first celestial sphere is mapped under a Lorentz transformation to a circle on the second. 

Let's pause to take this in. The first observer saw an object that had the shape of a circle. Based on the arguments of Lorentz contraction, you might expect that the second observer sees a squashed circle, maybe an ellipse. Yet this is not what happens. Instead, the second observer also sees a circle! The effects of the time of flight of light completely eliminates the Lorentz contraction. This fact was only realised more than 50 years after Einstein's formulation of special relativity when it was discovered independently by Terrell and Penrose. It is sometimes said to be the “invisibility of the Lorentz contraction”. Note that it doesn't mean that the effects of Lorentz contraction that we discussed before are not real. It just means that you don't get to see them if you take a picture of a sphere. If you look more closely, you will certainly find that there are things that change. For example, if you paint a picture on the surface of the sphere, this will appear distorted to the moving observer. 

## 11.7.3 Spinors

We end with a short advertisement for things to come. A spinor is simply a two-dimensional complex vector $\xi$ which, under a Lorentz transformation $A \in SL(2, \mathbb{C})$ , changes as $\xi \to A\xi$ . 

We've already seen how spinors can be used to describe light rays. But this is not their only use; they have much more a life of their own. Before I describe this, let me firstly explain a property that makes it very 

surprising that spinors have any real relevance in the world. This harks back to the observation that $SL(2, \mathbb{C})$ is the double cover of the Lorentz group. Suppose that there is some object in the universe that is actually described by a spinor. This means, in particular, that the state of the object with $\xi$ is different from the state of the object with $-\xi$ . What happens when we rotate this object? Well, we've already seen how to enact a rotation using $SL(2, \mathbb{C})$ matrices: they are given by (11.171). Except if we're acting on spinors we need to make a decision: do we pick $+A$ or do we pick $-A$ ? Because, unlike the action on Minkowski space, these two different matrices will result in different states $\xi$ after a rotation. It doesn't actually matter which choice we pick, as long as we make one. So let's decide that a rotation about an axis $n^i$ acts on a spinor by 

$$
\xi \rightarrow \exp \left(\frac {i \theta}{2} n ^ {i} \sigma^ {i}\right) \xi .\tag{11.181}
$$

This all seems fine. The surprise comes when we look at what happens if we rotate the spinor by $2\pi$ . It doesn't come back to itself. Instead, after a rotation by $2\pi$ we find $\xi \rightarrow -\xi$ . We have to rotate by $4\pi$ to get the spinor to return to itself! 

Wouldn't it be astonishing if there were objects in the universe with this property. If that were the case, you could rotate them and find that they didn't come back to themselves. This is even more astonishing when you realise that rotating an object is the same thing as walking around it. If such objects existed, you would be able to circle them once and see that the object sits in a different state just because you walked around it. How weird would that be? 

Well, such objects exist. What's more, they're the same objects that you and I are made of: electrons and protons and neutrons. All of these particles carry a little angular momentum whose direction is described by a spinor rather than a vector. This means that nature makes use of all the pretty mathematics that we've introduced in this section. The symmetry group of the universe we live in is not the Lorentz group $SO^{+}(1,3)$ . Instead, it is the double cover $SL(2,\mathbb{C})$ . And the basic building blocks of matter have subtle and wonderful properties. Turn an electron $360^{\circ}$ and it isn't the same; turn it $720^{\circ}$ and you're back to where you started. If you want to learn more about this, you can find deeper explanations in the books on Quantum Mechanics and Quantum Field Theory. 

## Further Reading

There is no shortage of books on classical mechanics. Here are a collection of all-purpose textbooks that I like, followed by some resources that I've used for individual chapters. 

At the lighter end, the book by Tom Kibble and Frank Berkshire [22] is easy reading, as is the book by Gregory [18]. Meanwhile, the books by Taylor [40] and by Hand and Finch [20] are slightly more advanced, and closer to the level of the book you're holding. All of these books are well written and do an excellent job of explaining the fundamentals of classical mechanics. 

There are also a number of classical mechanics classics that you should be aware of. The first volume of Landau and Lifshitz [24] is a gorgeous, concise and elegant summary of the subject in 150 content-packed pages. Landau is one of the most important physicists of the twentieth century and this is the first volume in a series of ten, considered by him to be the “theoretical minimum” amount of knowledge required to embark on research in physics. In 30 years, only 43 people passed Landau’s exam! Landau originally co-authored the Mechanics book with one of his students, Leonid Pyatigorsky. They subsequently had a falling out and the co-author was changed to Lifshitz. There are rumours that Pyatigorsky got his own back by denouncing Landau to the Soviet authorities, resulting in his arrest. 

The most canonical classical mechanics textbook was known to many generations of students simply as “Goldstein”. It is authoritative and not a little verbose. Goldstein died and the current, third edition found two extra authors to carry the flag $[15]$ . 

If you're more mathematically inclined, you might enjoy Arnold's beautiful treatise on classical mechanics, making connections with differential geometry [3]. It kicks off with “The universe is an affine space” and proceeds from there. Another mathematical rendering of the subject can be found in the book by Abraham and Marsden [1]. 

You can also find some excellent lecture notes on this subject online. At the risk of link rot, here are two that are particularly good: Daniel Arovas at UC San Diego [4] and Sunil Golwala at Caltech [16]. 

What follows is a mixed bag of further reading. I’ve usually flagged things up that I’ve taken from the more recent literature (where, in the world of classical mechanics, “recent” means within the last half century or so). 

## Chapter 1: Newtonian Mechanics

The quote that I rather cheekily ascribed to a teaching evaluation of Newton was written by one of his assistants, Humphrey Newton (no relation) in a letter to John Conduit [28]. The two sentences are from two different letters, dated 1727 and 1728. 

If you like to get your physics straight from the horse's mouth, then Galileo's originals are rather enjoyable as Salviati, Sagredo, and Simplicio slowly unravel the mysteries of the universe [11]. Newton's masterpiece [30] is a somewhat harder read, relying on a great deal of geometry that is no longer common knowledge. The great astrophysicist Chandrasekhar wrote a commentary on the Principia, in which he walks you through these geometrical proofs [6]. I should warn you that I sometimes found Newton easier to understand than Chandra. 

If you're looking for an easier read then there are, of course, many good biographies of these two famous scientists. On the more scholarly end, you could look at [21] and [47]. On the gentler, and generally more fun, end of the spectrum, you might try [14, 36], and [25]. 

## Chapter 2: Forces

This chapter contains the standard fare of classical mechanics. The quote about animals and terminal velocity is taken from a wonderful essay called “On Being the Right Size” by J.B.S. Haldane [19]. 

## Chapter 3: Dimensional Analysis

G.I Taylor's analysis of the atomic bomb blast was presented in two papers [38] and [39] and the photograph shown was reprinted in the second of these. A detailed discussion of the background to Taylor's analysis, together with a debunking of the myths that surround this story, can be found in [7]. The application of dimensional analysis to rowing was derived in [26]. Stoney's original paper, suggesting three fundamental units of nature, is from 1881 and uses $G$ , $c$ , and the electron charge in place of Planck's constant [37]. Planck's paper, introducing the units that now bear his name, is from 1899 [33]. For an entertaining discussion on fundamental units in physics, see [8]. 

A wide ranging, scholarly, sometimes rambling, and occasionally fun discussion of dimensional analysis can be found in the classic book by Barrow and Tipler [5]. 

## Chapter 4: Systems of Particles

The lovely bouncing ball problem that enumerates the digits of $\pi$ was first presented in Galperin in 2003 [12]. I'm grateful to Ben Green for pointing this paper out to me. (He suggested that we use the problem as a question for undergraduate admissions to Cambridge. I politely declined.) Galperin gives a geometric proof. The variation of the problem given in this book has a somewhat easier proof that Joe Minahan helped construct. 

## Chapter 5: The Two-Body Problem

This chapter contains more standard fare. 

For a nice discussion of how to view general relativity as a correction to Newton's law of gravity, see the paper by James Wells [46]. 

I learned about the geometrical proof of Kepler's laws, with a flavour of centuries gone by, from the wonderful book by David and Judith Goodstein [17]. 

The lovely Rutherford quote – “How can a fellow sit down at a table and calculate something that would take me – me – six months to measure in a laboratory” – is from a speech that Neville Mott gave at the Royal Society [27]. The quote appears more reasonable when you appreciate that Rutherford was talking about Eddington’s nonsensical attempts to compute the fine structure constant. 

## Chapter 6: Rotating Reference Frames

I took the discussion of the Roche limit from Steven Weinberg's lectures on astrophysics, published in 2020 [44]. He claims that the additional $-R_{1}$ term in (6.31) was missed for 170 years until it was pointed out in his book! That seems too good to be true, but Weinberg is one of the most scholarly physicists I know. 

## Chapter 7: The Lagrangian Formalism

Perhaps surprisingly, there are some really beautiful, classic textbooks on the calculus of variations. The book by Gelfand and Fomin [13] is a real gem, although not particularly easy going. There are also lots of lovely results in the books by Lanczos [23] and, for the more physically minded, by Yourgrau and Mandelstam [48]. (This latter book has a preface which says that Schrödinger, Heisenberg, and Oppenheimer all encouraged them to include a chapter on fluid mechanics! I guess that's a crowd that's difficult to refuse.) 

The material that sits at the heart of this chapter is the essence of classical mechanics and can be found in any of the more advanced book listed at the beginning. The discussion of electromagnetism in this chapter is somewhat brief and much can be found in the companion book on Electromagnetism [42]. 

There are two good biographies of Emmy Noether [29, 34]. Chapter 8: Small Oscillations 

The book by Landau and Lifshitz [24] has a particularly nice chapter on this material. 

## Chapter 9: Rigid Bodies

The Feynman plate story is from “Surely You’re Joking” [9]. I learned about the astrology thing from John Baez’ “this week’s finds” website: https://math.ucr.edu/home/baez/wobble/wob10.html. The theory of a falling cat was developed by Al Shapere and Frank Wilczek [35]. This is the same Frank Wilczek who won the 2004 Nobel prize for his work on quark interactions You can also find a famous film of a falling cat, made in 1894 by Étienne-Jules Marey, on YouTube: www.youtube.com/watch?v=fKYmECOKd58. 

## Chapter 10: The Hamiltonian Formalism

Much of the material contained in this chapter is, again, very standard and can be found in any of the more advanced textbooks listed at the beginning. 

The subject of magnetic monopoles will be a recurring theme throughout these books and you can read more in the companion books on Electromagnetism [42] and Quantum Mechanics [43], and in books that will appear later on Quantum Field Theory and the Standard Model. Several of the ideas in this chapter will reappear in the companion book on Quantum Mechanics [43]. This includes the system with phase space $\mathbf{S}^2$ which is the classical version of a qubit. More details on first-order vortex dynamics can be found in [2]. 

## Chapter 11: Special Relativity

There are a few specialised and rather short textbooks covering special relativity. The book by French is clear on the details [10]. If you're looking for something more challenging, you could turn to Pauli's book, written when he was just 21 [31]. A hundred years after its first publication, it remains perhaps the most scholarly account of the subject. It's not for the faint of heart. But it is cheap. 

The fact that the Lorentz contraction is not visible for a sphere was discovered independently by Penrose $[32]$ and by Terrell $[41]$ . It was popularised in a characteristically clear article by Viki Weisskopf $[45]$ . 

## References



[1] R. Abraham and J. E. Marsden, Foundations of Mechanics, Am. Math. Soc. 2nd edition, (2008) 





[2] H. Aref, Integrable, Chaotic, and Turbulent Vortex Motion in Two-Dimensional Flows, Ann. Rev. Fluid Mech. 15 345)1983) 





[3] V. I. Arnold, Mathematical Methods of Classical Mechanics, Springer-Verlag (1989) 





[4] D. Arovas, Classical Mechanics, lecture notes available at: https://courses.physics.ucsd.edu/2019/Winter/physics110b/lectures.html 





[5] J. Barrow and F. Tipler, The Anthropic Cosmological Principle, Oxford University Press (1986) 





[6] S. Chandrasekhar, Newton's Principia for the Common Reader, Clarendon Press (2003) 





[7] M. Deakin, G.I. Taylor and the Trinity Test, IJMEST 42 8 (2011) 





[8] M. Duff, L. B. Okun, and G. Veneziano, Trialogue on the Number of Fundamental Constants, arXiv:physics/0110060 





[9] R. P. Feynman and R. Leighton, Surely You're Joking Mr Feynman, Vintage (1985) 





[10] A. P. French, Special Relativity, Routledge (1968) 





[11] G. Galileo, Dialogue Concerning the Two Chief World Systems (1632) 





[12] G. Galperin, Playing Pool with $\pi$ , Regular and Chaotic Dynamics, 84, (2003) 





[13] I. M. Gelfand and S. V. Fomin, Calculus of Variations [original 1963] Dover (2000) 





[14] J. Gleick, Isaac Newton, Harper Perennial (2004) 





[15] H. Goldstein, C. Poole, and J. Safko, Classical Mechanics, Pearson, 3rd edition (2001) 





[16] S. Golwala, Classical Mechanics lecture notes available at: https://sites.astro.caltech.edu/golwala/ph106ab/ 





[17] D. Goodstein and J. Goodstein, Feynman's Lost Lecture: The Motions of Planets Around the Sun, Vintage (1997) 





[18] D. Gregory, Classical Mechanics, Cambridge University Press (2006) 





[19] J. B. S. Haldane, “On Being the Right Size” in Possible Worlds and Other Essays, Chatto & Windus (1926) 





[20] L. Hand and J. Finch, Analytical Mechanics, Cambridge University Press (1999) 





[21] J. L. Heilbron, Galileo, Oxford University Press (2012) 





[22] T. Kibble and F. Berkshire, Classical Mechanics, Imperial College Press (2004) 





[23] C. Lanczos, The Variational Principles of Mechanics, Dover Publications (1970) 





[24] L. D. Landau and E. M. Lifshitz, Mechanics, Vol 1, Butterworth-Heinemann (1976) 





[25] T. Levenson, Newton and the Counterfeiter, Faber and Faber (2010) 





[26] T. McMahon, Rowing: A Similarity Analysis, Science, 173,349 (1971) 





[27] N. F. Mott Rutherford and Theory, Rutherford Centenary Celebrations, Royal Society (1972) 





[28] H. Newton, Letter to J. Conduit, The Newton Project https://www.newtonproject.ox.ac.uk/view/texts/normalized/THEM00033 





[29] D. Neunschwander, Emmy Noether's Wonderful Theorem, Johns Hopkins University Press (2017) 





[30] I. Newton, Philosophiae Naturalis Principia Mathematica (1687) 





[31] W. Pauli, Theory of Relativity, Dover (2013) 





[32] R. Penrose, The Apparent Shape of a Relativistically Moving Sphere, Proc. Cambridge Phil. Soc., 55(1), 137 (1959) 





[33] M. Planck, U“ber irreversible Strahlungsvorg“ange, Sitzungsberichte der Königlich Preussischen Akademie der Wissenschaften zu Berlin, (in German as if you hadn’t guessed). 5, 440 (1899) 





[34] D. E. Rowe and M. Koreuber, Proving it Her Way: Emmy Noether, a Life in Mathematics, Springer (2020) 





[35] A. Shapere and F. Wilczek, Geometry of Self-Propulsion at Low Reynolds Number, J. Fluid Mech. 198, 557 (1989) 





[36] D. Sobel, Galileo's Daughter, Fourth Estate (2009) 





[37] G. Stoney, On The Physical Units of Nature, Phil. Mag. 11, 381 (1881) 





[38] G. I. Taylor, The Formation of a Blast Wave by a Very Intense Explosion: I. Theoretical Discussion, Proc. Roy. Soc. A201 (1950) 





[39] G. I. Taylor, The Formation of a Blast Wave by a Very Intense Explosion: II. The Atomic Explosion of 1945, Proc. Roy. Soc. A201 (1950) 





[40] J. R. Taylor, Classical Mechanics, University Science Books (2004) 





[41] J. Terrell, Invisibility of the Lorentz Contraction, Phys. Rev. 116, 1041 (1959) 





[42] D. Tong, Electromagnetism, Cambridge University Press (2025) 





[43] D. Tong, Quantum Mechanics, Cambridge University Press (2025) 





[44] S. Weinberg, Lectures on Astrophysics, Cambridge University Press (2025) 





[45] V. Weisskopf, The Visual Appearance of Rapidly Moving Objects, Phys. Today, 13(9), 24 (1960) 





[46] J. Wells, When Effective Theories Predict: The Inevitability of Mercury's Anomalous Perihelion Precession, arXiv:1106.1568 [physics.hist-ph] 





[47] R. S. Westfall, Never at Rest: A Biography of Isaac Newton, Cambridge University Press (1983) 





[48] W. Yourgrau and S. Mandelstam, Variational Principles in Dynamics and Quantum Theory, Dover (1968) 



## Index

4-momentum, 375
4-velocity, 373 

absolute time, 11
acceleration, 7
action, 166
action-angle variables, 315
adiabatic invariant, 324
angular frequency, 18
angular momentum, 28, 79, 97, 193, 237
angular momentum barrier, 101
angular velocity, 99, 137, 231
anharmonic oscillator, 225
apoapsis (or aphelion), 104
apparent gravity, 141
Aristotle, 8
arugula, 89
astrology, 265
asymmetric top, 250
atomic bomb, 70
avalanche, 93 

bead on rotating hoop, 182
binary stars, 144
black hole, 35
body frame, 229
Bohr–Van Leeuwen paradox, 291
Boltzmann distribution, 290
boost, Galiliean, 9
boost, Lorentz, 347
bouncing balls, 85
Bridgman's theorem, 66
Brillouin zone, 223
Buckingham Π theorem, 69 

calculus of variations, 155
canonical momentum, 174, 275
canonical quantisation, 338
canonical transformation, 306
causality, 354
celestial sphere, 405
central force, 28, 95
centre of mass, 78
centrifugal force, 141
centripetal force, 99
collisions, 84
Compton scattering, 390
conductivity, 55
configuration space, 169
conic section, 108
connection, 270
conservation laws, 83, 188, 281
conservation of energy, 189
conservative forces, 25
constant of motion, 188
constraints, 177
Coriolis force, 145
cosmology, 12
Coulomb force, 43
covariant relativistic action, 394
cross-section, 132
curved geometry, 208
cyclic coordinate, 188
cyclotron frequency, 40 

damped harmonic oscillator, 48
deformable objects, 267
degrees of freedom, 169
determinism, 285
digits of pi, 86
dimensional analysis, 65
dissipation, 47
Doppler effect, 379
double pendulum, 184, 214
drag, 45
driven harmonic oscillator, 50 

Drude model, 55
dry friction, 45 

eccentricity, 108
eccentricity vector, 114
effective potential, 101
einbein, 398
elastic collisions, 84
electric charge, 36
electric field, 36, 283
electric potential, 38, 202
electromagnetism, 36, 202
ellipse, 109, 121
elliptic integral, 25
energy, 17, 25, 194
entropy, 292
equation of motion, 12
equilibrium, 22, 210
escape velocity, 34
ether, 350
Euler angles, 254
Euler force, 140
Euler's equations, 246
Euler–Lagrange equation, 158, 167 

falling cat, 267
Feynman, Richard, 259
fictitious forces, 139
field strength, 273
first-order Hamiltonian dynamics, 299
fluid drag, 45
force, 16
central, 28
conservative, 25
Foucault's pendulum, 150
free symmetric top, 258
free tops, 246
frequency, 18
friction, 44
functional, 155 

Galilean group, 10
Galilean relativity, 9, 171
gamma factor, 346
gauge transformation, 203, 269
Gauss' law
for electrostatics, 64
for gravity, 62
Geiger–Marsden experiment, 134
general relativity, 116
generalised coordinates, 173
generalised momentum, 174
generating functions, 313
geodesic, 158
geodesic equation, 209
gravitational field, 31
gravity, 29, 196
uniform field, 17
Halley, Edmund, 119
Hamilton's equations, 280
Hamilton's principle, 167, 281
Hamilton, William Rowan, 284
Hamilton–Jacobi equation, 331
Hamiltonian, 277
harmonic oscillator, 18, 22, 315
damped, 48
driven, 50
harmonic oscillators (coupled), 210
heavy symmetric top, 260
herpolhode, 254
Hilbert, David, 195
holonomic constraints, 178
homogeneity of space, 193
homogeneity of time, 194
Hooke's law, 18
Hooke, Robert, 119
Hopf map, 406
hurricanes, 147
hyperbola, 110 

ignorable coordinate, 188 impact parameter, 129
impulse, 123
inertia ellipsoid, 252
inertia tensor, 236
inertial frame, 8
inertial mass, 13
integrable system, 317
inverse square law, 31, 43
isotropy of space, 193 

Kepler problem, 107
Kepler's laws of motion, 112 

Lagrange multiplier, 179
Lagrange points, 201, 217
Lagrange, Joseph-Louis, 176
Lagrangian, 165
Laplace–Runge–Lenz vector, 114, 311
lattice, 221
law of inertia, 8
Legendre condition, 164
Legendre transform, 278
Leibniz, Gottfried, 120
lightcone, 354
line integrals, 58
Liouville's equation, 289
Liouville's theorem, 286, 328
Lorentz contraction, 360
Lorentz force, 37
Lorentz group, 367, 400
Lorentz transformation, 344 

Möbius transformation, 408  
magnetic field, 36, 38, 205, 283, 297  
magnetic monopole, 298  
mass  
inertial, 13  
inertial vs gravitational, 36  
massless particles, 378  
Maxwell equations, 44  
Maxwell Lagrangian, 207 

metric, 208
Michelson–Morley experiment, 351
Minkowski metric, 367
Minkowski space, 363
moment of inertia, 237
momentum, 13, 193 

Newton's constant, 30
Newton's first law, 8
Newton's law of gravity, 31
Newton's laws of motion, 7
Newton's second law, 12
Newton's third law, 77, 80
Newton, Isaac, 118
no-slip condition, 243
Noether's theorem, 190, 310
Noether, Emmy, 195
non-linear oscillator, 225
nutation, 263 

Ohm's law, 55
orbit equation, 107 

parabola, 111
parallel axis theorem, 240
particle, 6
particle collisions, 388
particle decay, 387
path integral, 340
path-ordered exponentials, 233
Pauli matrices, 403
pendulum, 23, 67, 177, 244, 276
periapsis (or perihelion), 104
perihelion precession, 116
period, 19
permittivity of free space, 43
perpendicular axis theorem, 239
perturbation theory, 224
phase space, 275
Planck units, 74
Poincar'e recurrence theorem, 291 

Poinso construction, 251
Poisson brackets, 294
Poisson equation, 61
polar coordinates on the plane, 98
polhode, 253
potential
central, 28
effective, 101
electric, 38
potential energy
in 1d, 16
in 3d, 25
power, 26
precession in a magnetic field, 152
precession of a top, 263
precession of spin, 306
precession of the equinox, 265
principal moment of inertia, 237
Principia, 118
principle of least action, 165, 281
principle of relativity, 10
principle of superposition, 32
probability distribution, 285
proper Lorentz group, 369 

rapidity, 369
reduced mass, 96
reduction to quadrature, 19
reference frame, 6
refractive index, 161
relativity, Einsteinian, 344
relativity, Galilean, 9, 171
resistance, 56
resonance, 52
rest mass, 376
Reynolds number, 46
rigid bodies, 229
Roche limit, 145
rocket equation, 89 

rotating reference frames, 136
rowing, 72
Runge–Lenz vector, 114, 311
Rutherford scattering, 131
Rutherford, Ernest, 134 

satellites, 202
scattering, 129
Schwarzschild radius, 35
second law of thermodynamics, 292
secular terms, 227
signature (of spacetime), 366
simultaneity, 352
sleeping top, 264
small oscillations, 210
Snell's law, 161
SO(1,3), 369
SO(3), 231
sound waves, 224
space frame, 229
special relativity, 343
speed of light, 343
spherical pendulum, 185
spin, 302
spinning top, 247
spinor, 409
spring constant, 18
stability, 22, 210
stability of circular orbits, 104
stability of spinning things, 250
stereographic projection, 407
Stokes' theorem, 28
Stoney, George, 74
symmetric top, 247, 260
symmetry, 188
symplectic matrix, 307
symplectic structure, 295 

tachyon, 380
Taylor, G. I., 70
terminal velocity, 52 

Terrell–Penrose effect, 409
test particle, 30
three-body problem, 199, 217
throwing stuff at other stuff, 129
time dilation, 356
torque, 29, 80
trajectory of particle, 7
transient solution, 51
triatomic molecule, 215
twin paradox, 358
two-body problem, 96, 197 

unstable equilibrium, 23 

varying mass, 88
vector potential, 202
velocity, 7
velocity addition, 362, 375
vis-viva equation, 112
viscosity, 46
vortex dynamics, 299 

water going down a plughole, 146
why you get old, 397
wobbles, 259
work done, 26
worldline, 349
Wren, Christopher, 119 

Yukawa potential, 30 