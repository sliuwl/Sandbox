# Degrees of Freedom of a Rigid Body

**Reading material:** Chapter 10 of *Classical Mechanics* by John R. Taylor; Chapter 4 of *Classical Mechanics* by Goldstein, Poole, Safko

## Table of Contents

1. [Counting Constraints](#1-counting-constraints)
   - [1.1 Fix Particle 1](#11-fix-particle-1)
   - [1.2 Constrain Particle 2 Relative to Particle 1](#12-constrain-particle-2-relative-to-particle-1)
   - [1.3 Constrain Particle 3 Relative to Particles 1 and 2](#13-constrain-particle-3-relative-to-particles-1-and-2)
   - [1.4 Constrain Each Remaining Particle](#14-constrain-each-remaining-particle)
   - [1.5 Total Number of Independent Constraints](#15-total-number-of-independent-constraints)
2. [Degrees of Freedom](#2-degrees-of-freedom)

---

## 1. Counting Constraints

For $N$ particles in 3D, we start with $3N$ coordinates:
\[
\mathbf r_i=(x_i,y_i,z_i),\qquad i=1,\dots,N.
\]
A **rigid body (刚体)** has only 6 degrees of freedom, so the number of independent constraints is $3N-6$.

One constructive way to see this is to count how many independent distance constraints are needed to fix all internal geometry. Assume the body is generic, meaning at least three particles are not collinear.

------

### 1.1 Fix Particle 1

Particle 1 can be anywhere; $\mathbf r_1$ has 3 degrees of freedom. No constraint is needed yet.

------

### 1.2 Constrain Particle 2 Relative to Particle 1

Particle 2 originally has 3 degrees of freedom. To make its distance from particle 1 fixed, impose
\[
|\mathbf r_2-\mathbf r_1|=d_{12}.
\]
This is one constraint. Therefore particle 2 has $3-1=2$ remaining degrees of freedom. The number of constraints so far is $1$.

------

### 1.3 Constrain Particle 3 Relative to Particles 1 and 2

Particle 3 originally has 3 degrees of freedom. Fixing its distances to particles 1 and 2 gives two constraints:
\[
|\mathbf r_3-\mathbf r_1|=d_{13},\qquad |\mathbf r_3-\mathbf r_2|=d_{23}.
\]
So particle 3 has $3-2=1$ remaining degree of freedom. The number of constraints so far is $1+2=3$.

At this stage, particles 1, 2, and 3 define the position and orientation of a rigid triangular frame, up to overall translation and rotation.

------

### 1.4 Constrain Each Remaining Particle

For each particle $i\ge 4$, its position relative to the already fixed frame is determined by its distances to three non-collinear particles, say particles 1, 2, and 3:
\[
|\mathbf r_i-\mathbf r_1|=d_{i1},\qquad |\mathbf r_i-\mathbf r_2|=d_{i2},\qquad |\mathbf r_i-\mathbf r_3|=d_{i3}.
\]
These are three independent constraints. Since particle $i$ has 3 coordinates, these constraints remove all its internal degrees of freedom.

There are $N-3$ such particles, so the number of constraints from them is $3(N-3)$.

------

### 1.5 Total Number of Independent Constraints

Therefore,
\[
\text{number of constraints} = 1+2+3(N-3).
\]
Simplifying,
\[
1+2+3(N-3) = 3+3N-9 = 3N-6.
\]
So the rigid body has
\[
\boxed{3N-6}
\]
independent constraints.

------

## 2. Degrees of Freedom

Since the unconstrained system has $3N$ degrees of freedom, the remaining number is
\[
3N-(3N-6)=6.
\]
Thus a rigid body in three dimensions has
\[
\boxed{6}
\]
degrees of freedom: 3 translations and 3 rotations.
