# The Legendre Transform

The **Legendre transform** is a method to express the information encoded in a given function in a different way. Instead of describing a function by its original variable, we describe it using its **slope**.

---

## 1. Original Function

Let

\[
L=L(V).
\]

Define

\[
P(V)=\frac{\partial L(V)}{\partial V}.
\]

Here, \(P\) is the slope function of \(L(V)\).

Equivalently,

\[
L(V)=\int_0^V P(V')\,dV'.
\]

So \(L(V)\) can be interpreted as the area under the curve \(P(V)\).

---

## 2. Rotating and Flipping the Picture

The Legendre transform changes variables from \(V\) to \(P\).

If

\[
P=\frac{\partial L}{\partial V},
\]

then, assuming this relation can be inverted, we can write

\[
V=V(P).
\]

The new function is

\[
H(P)=\int_0^P V(P')\,dP'.
\]

This function depends on the slope variable \(P\), rather than the original variable \(V\).

---

## 3. Relation Between \(L(V)\) and \(H(P)\)

The areas satisfy

\[
L(V)+H(P)=PV.
\]

Therefore,

\[
H(P)=PV-L(V).
\]

This is the Legendre transform of \(L(V)\).

In words:

> We switch from a function \(L(V)\), which depends on \(V\), to a new function \(H(P)\), which depends on the value of the slope \(P\) at each point.

---

## 4. Mechanical Application

In mechanics, the generalized momentum is defined by

\[
p=\frac{\partial L}{\partial \dot q}.
\]

The Hamiltonian is the Legendre transform of the Lagrangian with respect to \(\dot q\):

\[
H(q,p,t)
=
p\dot q
-
L\bigl(q,\dot q(q,p),t\bigr).
\]

Here \(\dot q\) is eliminated in favor of \(p\).

From the Hamiltonian, one obtains

\[
\dot q=\frac{\partial H}{\partial p}.
\]

Thus the Legendre transform changes the description from the variables

\[
(q,\dot q)
\]

to the variables

\[
(q,p).
\]