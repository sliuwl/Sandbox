# Lagrange Multiplier

An extremely powerful method which allows us to find the maxima or minima of functions which are subject to **constraints**.

Suppose we have a marble that always remains attached to an inclined plane and moves on this plane only along a circle. What is the highest point?

Plane:

\[
z(x,y)=-2x+y
\tag{1}
\]

Circle:

\[
x^2+y^2-1=0
\tag{2}
\]

**Q:** Find which point on the circle defined in \((2)\) is the highest.

---

## Method 1: Substitution (Traditional Approach)

The traditional way to solve a constrained optimization problem is to use the constraint to eliminate one of the variables, reducing the problem to an unconstrained optimization in the remaining variable.

From the constraint \((2)\), we solve for \(x\):

\[
x = \pm \sqrt{1-y^2}.
\]

Substituting this into the function \((1)\) gives

\[
z(y) = -2\bigl(\pm \sqrt{1-y^2}\bigr) + y.
\]

Because the coefficient of \(x\) in \(z\) is negative, the highest value of \(z\) will occur when \(x\) itself is negative.  We therefore select the **negative branch**

\[
x = -\sqrt{1-y^2},
\]

so that

\[
z(y) = 2\sqrt{1-y^2} + y.
\]

To find the extremum we set the derivative to zero:

\[
\frac{dz}{dy}
= \frac{-2y}{\sqrt{1-y^2}} + 1 = 0.
\]

Hence

\[
\sqrt{1-y^2} = 2y.
\]

Since the left-hand side is non-negative, we must have \(y \ge 0\).  Squaring both sides:

\[
1-y^2 = 4y^2
\quad\Longrightarrow\quad
y^2 = \frac{1}{5}.
\]

Therefore

\[
y = \frac{1}{\sqrt{5}}
\qquad (\text{taking the positive root because } y\ge 0).
\]

The corresponding \(x\) value is

\[
x = -\sqrt{1-\frac{1}{5}} = -\sqrt{\frac{4}{5}} = -\frac{2}{\sqrt{5}}.
\]

Finally,

\[
z_{\max} = -2\Bigl(-\frac{2}{\sqrt{5}}\Bigr) + \frac{1}{\sqrt{5}}
= \frac{4}{\sqrt{5}} + \frac{1}{\sqrt{5}}
= \sqrt{5}.
\]

> **Remark.** If we had chosen the positive branch \(x = +\sqrt{1-y^2}\), the same calculation would lead to \(y = -1/\sqrt{5}\) and \(z = -\sqrt{5}\), which is the lowest point on the circle.  The substitution method therefore works, but it requires us to keep track of which branch gives the desired extremum.

---

## Method 2: Lagrange Multipliers

We now introduce a new variable \(\lambda\) and define the **auxiliary function (辅助函数)**

\[
\Lambda(x,y,\lambda)
=
z(x,y)+\lambda(x^2+y^2-1).
\]

Here,

\[
z(x,y)
\]

is the original function, and

\[
x^2+y^2-1
\]

is the constraint.

\[
\lambda
\]

is a **Lagrangian multiplier**.

Now,

\[
\frac{d\Lambda}{dx}
=
\frac{d}{dx}
\left(
-2x+y+\lambda(x^2+y^2-1)
\right).
\]

So

\[
-2+2\lambda x=0.
\]

Hence,

\[
x=\frac{1}{\lambda}.
\]

Analogously,

\[
\frac{d\Lambda}{dy}
=
\frac{d}{dy}
\left(
-2x+y+\lambda(x^2+y^2-1)
\right).
\]

Thus,

\[
1+2\lambda y=0,
\]

so

\[
y=-\frac{1}{2\lambda}.
\]

And for \(\lambda\),

\[
\frac{d\Lambda}{d\lambda}
=
x^2+y^2-1=0.
\]

This is exactly our constraint.

Therefore,

\[
x=\frac{1}{\lambda},
\qquad
y=-\frac{1}{2\lambda}.
\]

Substitute into the constraint:

\[
\frac{1}{\lambda^2}
+
\frac{1}{4\lambda^2}
=
1.
\]

So

\[
5=4\lambda^2,
\]

and

\[
\lambda^2=\frac{5}{4}.
\]

Hence,

\[
\lambda=\pm \frac{\sqrt{5}}{2}.
\]

Then

\[
y
=
-\frac{1}{2}
\cdot
\frac{1}{\pm \frac{\sqrt{5}}{2}}
=
\pm \frac{1}{\sqrt{5}}.
\]

Choose positive \(y\),

\[
y=\frac{1}{\sqrt{5}},
\]

and negative \(x\),

\[
x=-\frac{2}{\sqrt{5}}.
\]

Thus,

\[
z=-2x+y.
\]

Therefore,

\[
z
=
-2\left(-\frac{2}{\sqrt{5}}\right)
+
\frac{1}{\sqrt{5}}
=
\sqrt{5}.
\]

---

## Summary

Define

\[
\Lambda(x,y,\cdots,\lambda_1,\lambda_2,\cdots)
=
f(x,y,\cdots)
+
\lambda_1 g_1(x,y,\cdots)
+
\lambda_2 g_2(x,y,\cdots).
\]

Here,

\[
g_1(x,y,\cdots),
\qquad
g_2(x,y,\cdots),
\qquad
\ldots
\]

are constraints.

The stationary conditions are

\[
\boxed{
\frac{\partial \Lambda}{\partial x}
=
\frac{\partial \Lambda}{\partial y}
=
\cdots
=
\frac{\partial \Lambda}{\partial \lambda_1}
=
\frac{\partial \Lambda}{\partial \lambda_2}
=
\cdots
=
0
}
\]

---

# A Formal Explanation

Let a system be described by \(n\) generalized coordinates

\[
q_1,q_2,\cdots,q_n.
\]

Assume further that the system is subjected to \(k\) holonomic constraints. So there are \(k\) equations to relate the coordinates.

There are only

\[
n-k
\]

independent generalized coordinates.

However, we prefer for the moment to use all \(n\) of the coordinates.

The behavior of the system is described by Hamilton's principle:

\[
\delta S
=
\int_{t_1}^{t_2} L\,dt
=
0.
\]

And the \(k\) equations of constraint are

\[
f_j(q_1,q_2,\cdots,q_n)=0,
\qquad
j=1,2,\cdots,k.
\tag{1}
\]

If all the coordinates were independent,

\[
\frac{d}{dt}
\left(
\frac{\partial L}{\partial \dot q_i}
\right)
-
\frac{\partial L}{\partial q_i}
=
0,
\qquad
i=1,2,\cdots,n.
\tag{2}
\]

This result depends on \(\delta q_i\) being independent.

Equations \((1)\) represent holonomic constraints, so

\[
\delta f_j
=
\frac{\partial f_j}{\partial q_1}\delta q_1
+
\frac{\partial f_j}{\partial q_2}\delta q_2
+
\cdots
+
\frac{\partial f_j}{\partial q_n}\delta q_n
=
0.
\]

Equivalently,

\[
\sum_i^n
\frac{\partial f_j}{\partial q_i}
\delta q_i
=
0,
\qquad
j=1,2,\cdots,k.
\tag{3}
\]

If equation \((3)\) holds, multiplying it by some quantity \(\lambda_j\) will have no effect:

\[
\lambda_j
\sum_i^n
\frac{\partial f_j}{\partial q_i}
\delta q_i
=
0.
\]

Adding \(k\) equations,

\[
\sum_j^k
\lambda_j
\sum_i^n
\frac{\partial f_j}{\partial q_i}
\delta q_i
=
0.
\]

Therefore,

\[
\int_{t_1}^{t_2}
dt
\left(
\sum_j^k
\lambda_j
\sum_i^n
\frac{\partial f_j}{\partial q_i}
\delta q_i
\right)
=
0.
\tag{4}
\]

Also,

\[
\delta S=0
=
\sum_i
\int_{t_1}^{t_2}
dt
\left[
\frac{\partial L}{\partial q_i}
-
\frac{d}{dt}
\left(
\frac{\partial L}{\partial \dot q_i}
\right)
\right]
\delta q_i
=
0.
\tag{5}
\]

Combining \((4)\) and \((5)\),

\[
\int_{t_1}^{t_2}
dt
\sum_i
\left(
\frac{\partial L}{\partial q_i}
-
\frac{d}{dt}
\frac{\partial L}{\partial \dot q_i}
+
\sum_j^k
\lambda_j
\frac{\partial f_j}{\partial q_i}
\right)
\delta q_i
=
0.
\]

The \(\delta q_i\)'s are not all independent.

But \(n-k\) of them are independent. Then for these coordinates,

\[
\frac{\partial L}{\partial q_i}
-
\frac{d}{dt}
\frac{\partial L}{\partial \dot q_i}
+
\sum_j^k
\lambda_j
\frac{\partial f_j}{\partial q_i}
=
0,
\qquad
i=1,\cdots,n-k.
\]

For the remaining \(k\) equations, we can select the undetermined \(\lambda_j\) such that

\[
\frac{\partial L}{\partial q_i}
-
\frac{d}{dt}
\frac{\partial L}{\partial \dot q_i}
+
\sum_j^k
\lambda_j
\frac{\partial f_j}{\partial q_i}
=
0,
\qquad
i=n-k+1,\cdots,n.
\]

Consequently, we have for all \(q_i\)'s the following relations:

\[
\frac{d}{dt}
\frac{\partial L}{\partial \dot q_i}
-
\frac{\partial L}{\partial q_i}
=
\sum_j^k
\lambda_j
\frac{\partial f_j}{\partial q_i},
\qquad
i=1,\cdots,n.
\]

The \(n+k\) equations solve for \(n\) coordinates \(q_i\) and \(k\) multipliers \(\lambda_j\).

Here \(L\) is \(L_{\text{free}}\):

\[
\frac{d}{dt}
\frac{\partial L}{\partial \dot q_i}
-
\frac{\partial L}{\partial q_i}
=
\sum_j^k
\lambda_j
\frac{\partial f_j}{\partial q_i}
=
F_i.
\]

Here,

\[
F_i
\]

are generalized constraint forces.

---

# Example: Pendulum Constraint

For a pendulum,

\[
x^2+y^2=\ell^2.
\]

The constraint is

\[
f=x^2+y^2-\ell^2.
\]

The free Lagrangian is

\[
L_{\text{free}}
=
T-V
=
\frac{1}{2}m(\dot x^2+\dot y^2)-(-mgy).
\]

Thus,

\[
L_{\text{free}}
=
\frac{1}{2}m(\dot x^2+\dot y^2)+mgy.
\]

The full Lagrangian with constraint is

\[
L
=
T-V+\lambda f.
\]

Using the note's convention,

\[
L
=
\frac{1}{2}m(\dot x^2+\dot y^2)
+
mgy
+
\frac{1}{2}\lambda(x^2+y^2-\ell^2).
\]

Then the Euler-Lagrange equations give

\[
\frac{\partial L}{\partial x}
-
\frac{d}{dt}
\left(
\frac{\partial L}{\partial \dot x}
\right)
=
0.
\]

Therefore,

\[
\lambda x-m\ddot x=0.
\]

Similarly,

\[
\frac{\partial L}{\partial y}
-
\frac{d}{dt}
\left(
\frac{\partial L}{\partial \dot y}
\right)
=
0,
\]

so

\[
\lambda y+mg-m\ddot y=0.
\]

Thus,

\[
\lambda x-m\ddot x=0,
\]

\[
\lambda y+mg-m\ddot y=0.
\]

And

\[
\frac{\partial L}{\partial \lambda}
-
\frac{d}{dt}
\left(
\frac{\partial L}{\partial \dot\lambda}
\right)
=
0.
\]

Hence,

\[
\frac{1}{2}(x^2+y^2-\ell^2)=0.
\]

So,

\[
x^2+y^2-\ell^2=0.
\]

---

## What if we use \(\theta\) as the generalized coordinate?

The constraint term is

\[
L_{\text{cons}}
=
\frac{1}{2}\lambda(x^2+y^2-\ell^2).
\]

Using

\[
x=\ell\sin\theta,
\qquad
y=\ell\cos\theta,
\]

we get

\[
L_{\text{cons}}
=
\frac{1}{2}\lambda
\left(
(\ell\sin\theta)^2
+
(\ell\cos\theta)^2
-
\ell^2
\right).
\]

Therefore,

\[
L_{\text{cons}}=0.
\]

In the Lagrangian formalism, as soon as we have found suitable coordinates which make the constraints trivially true, we don't have to care about the constraints at all!

The Lagrangian multiplier terms vanish.

**Note:** We can relate the generalized constraint force to the actual force. If we have time, we can get back to this.