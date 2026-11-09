# Glossary: 04VirtualWork

| English | 中文 | Brief explanation |
|-----------------------------------------|----------------------|-------------------------------------------------------------------|
| **Virtual displacement** | 虚位移 | A hypothetical infinitesimal displacement $\delta\vec r$ consistent with the constraints of the system at a fixed instant of time, obtained by setting $\delta t=0$. |
| **Physical displacement** | 实位移 | The actual infinitesimal displacement $d\vec r$ occurring over a time interval $dt$, including the explicit time dependence through $\partial\vec r/\partial t$. |
| **Virtual work** | 虚功 | The work $\delta W=\vec F\cdot\delta\vec r$ done by a force along a virtual displacement; in generalized coordinates $\delta W=\sum_i Q_i\,\delta q_i$. |
| **Generalized force** | 广义力 | Defined as $Q_i=\vec F\cdot(\partial\vec r/\partial q_i)$; the component of force conjugate to the generalized coordinate $q_i$. |
| **Constraint force** | 约束力 | The force arising from constraints, written in generalized coordinates as $Q_i^c=\lambda\,\partial g/\partial q_i$ for a holonomic constraint $g(q_i,t)=0$. |
| **Applied force** | 主动力 | The external or active force directly imposed on the system, as distinguished from constraint forces. |
| **Ideal constraint** | 理想约束 | A constraint for which the total virtual work done by constraint forces vanishes for all allowed virtual displacements. |
| **Principle of virtual work** | 虚功原理 | In static equilibrium with ideal constraints, the total virtual work done by the applied forces is zero: $\sum_i Q_i\,\delta q_i=0$. |
| **Holonomic constraint** | 完整约束 | A constraint expressible as an equation $g(q_i,t)=0$ relating the generalized coordinates and possibly time. |
| **Lagrange multiplier** | 拉格朗日乘子 | An auxiliary parameter $\lambda(t)$ (or $\lambda_j(t)$ for multiple constraints $g_j=0$) that enforces the constraint and determines the magnitude of the constraint force. |
| **Degrees of freedom** | 自由度 | The number of independent coordinates that can be varied in a small displacement of the system. |
| **Independent coordinates** | 独立坐标 | Generalized coordinates whose virtual variations $\delta q_i$ can be chosen arbitrarily; the vanishing of their coefficients gives the equilibrium conditions. |
| **Static equilibrium** | 静力平衡 | A state in which the system experiences no acceleration; all generalized forces vanish ($Q_i=0$) or, for conservative systems, $\partial V/\partial q_i=0$. |
| **Equilibrium condition** | 平衡条件 | The requirement that each generalized force be independently zero, $Q_i=0$, derived from the independence of the virtual displacements. |
| **Conservative system** | 保守系统 | A system in which all applied forces derive from a scalar potential energy $V$, so that $Q_i=-\partial V/\partial q_i$. |
| **Potential energy** | 势能 | The scalar function $V(q)$ whose partial derivatives give the generalized forces of a conservative system. |
| **Stationary point** | 驻点 | A configuration where the first derivatives of the potential energy vanish, $\partial V/\partial q_i=0$, yielding a possible static equilibrium. |
| **d'Alembert's principle** | 达朗贝尔原理 | The extension of the principle of virtual work to dynamics: an accelerating system is treated as being in equilibrium in a non-inertial frame co-moving with the system, provided fictitious forces $-m\ddot{\vec r}$ are included. |
| **Fictitious force** | 虚构力 / 惯性力 | The force $-m\vec a$ (or $-m\ddot{\vec r}$) introduced in a non-inertial frame to enable the use of static equilibrium methods for dynamical problems. |
| **Non-inertial frame** | 非惯性参考系 | A reference frame that accelerates relative to an inertial frame; fictitious forces must be added to apply equilibrium conditions. |
| **Lagrange's equation** | 拉格朗日方程 | Derived from d'Alembert's principle: $\frac{d}{dt}\bigl(\partial T/\partial\dot q_i\bigr)-\partial T/\partial q_i=Q_i$, valid for arbitrary generalized forces. |
| **Euler–Lagrange equation** | 欧拉–拉格朗日方程 | For conservative systems, $\frac{d}{dt}\bigl(\partial L/\partial\dot q_i\bigr)-\partial L/\partial q_i=0$, where $L=T-V$ is the Lagrangian. |
| **Non-conservative force** | 非保守力 | Forces not derivable from a potential; they appear as $Q_i^{\rm nc}$ on the right-hand side of the Euler–Lagrange equation. |
| **Kinetic energy** | 动能 | $T=\frac12m\dot{\mathbf r}^2$ in Cartesian coordinates; in generalized coordinates its derivatives with respect to $\dot q_i$ and $q_i$ produce the inertial terms in Lagrange's equation. |
