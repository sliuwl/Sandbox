# Glossary: 03LagrangianMechanics

| English | 中文 | Brief explanation |
|---------|------|-------------------|
| **Physical space** | 物理空间 | The ordinary three-dimensional Euclidean space $\mathbb{R}^3$ in which particles move. |
| **Configuration** | 构型 | The complete specification of the position of every particle in a system. |
| **Configuration space** | 构型空间/位形空间 | The $3N$-dimensional space of all possible configurations for a system of $N$ particles; a point $q\in\mathbb{R}^{3N}$ encodes all positions. |
| **Generalized coordinates** | 广义坐标 | Any set of independent parameters $q_1,\dots,q_n$ that completely specifies the configuration of a system; they need not be Cartesian. |
| **Generalized velocity** | 广义速度 | The time derivative $\dot q_i$ of a generalized coordinate, giving the rate of change along the $q_i$ direction in configuration space. |
| **Phase space** | 相空间 | The $6N$-dimensional space combining positions and momenta, $(q,p)\in\mathbb{R}^{6N}$; a point specifies the complete mechanical state in Hamiltonian mechanics. |
| **Hamilton's principle** | 哈密顿原理 / 作用量取驻值原理 | The actual path a system follows between two fixed configurations makes the action functional stationary: $\delta S=0$. |
| **Principle of least action** | 最小作用量原理 | An informal name for Hamilton's principle; the stationary action is often a local minimum over short times. |
| **Action** | 作用量 | The functional $S[q]=\int_{t_i}^{t_f}L(q,\dot q,t)\,dt$ that assigns a number to each path in configuration space. |
| **Lagrangian** | 拉格朗日量 | The function $L(q,\dot q,t)$ whose integral gives the action; for many mechanical systems $L=T-V$. |
| **Functional** | 泛函 | A rule that maps an entire function (a path $q(t)$) to a single real number, e.g. the action $S[q]$. |
| **Discrete approximation** | 离散近似 | Approximating the action integral by a Riemann sum $\sum_k L_k\Delta t$ to clarify how $S$ is evaluated. |
| **Variation** | 变分 | A small change in the input path, $q_\alpha(t)=q(t)+\alpha\eta(t)$, with fixed endpoints $\eta(t_i)=\eta(t_f)=0$. |
| **Euler–Lagrange equation** | 欧拉–拉格朗日方程 | The necessary condition for stationary action: $\frac{d}{dt}\bigl(\partial L/\partial\dot q_k\bigr)-\partial L/\partial q_k=0$, one per coordinate. |
| **Fixed but arbitrary endpoints** | 固定但任意的端点 | Boundary conditions $q(t_i)$ and $q(t_f)$ are held fixed during variation, but their values are not pre-determined; this yields a local equation valid for any pair. |
| **Local differential equation** | 局部微分方程 | The Euler–Lagrange equation holds at each instant along the path; once derived, the final endpoint need not be known in advance. |
| **Initial-value problem** | 初值问题 | Specifying $q(t_i)$ and $\dot q(t_i)$; standard ODE existence and uniqueness theorems guarantee a unique local solution. |
| **Boundary-value problem** | 边值问题 | Specifying $q(t_i)$ and $q(t_f)$; stationary paths may be unique, multiple, or nonexistent over long intervals. |
| **Kinetic energy** | 动能 | $T=\frac12m\dot{\mathbf r}^2$ in Cartesian coordinates; in generalized coordinates it may become a quadratic form $T=\frac12\sum_{i,j}A_{ij}(q)\dot q_i\dot q_j$. |
| **Potential energy** | 势能 | The function $V(q)$ from which conservative forces are derived; appears with a minus sign in the Lagrangian, $L=T-V$. |
| **Proper time** | 固有时间 | The Lorentz-invariant time measured along a particle's worldline in relativity; the relativistic free-particle action is proportional to it. |
| **Worldline** | 世界线 | The trajectory of a particle through spacetime. |
| **Form invariance** | 形式不变性 / 协变性 | The Euler–Lagrange equations retain exactly the same form in any choice of generalized coordinates. |
| **Polar coordinates** | 极坐标 | Coordinates $(r,\phi)$ in a plane; illustrate how the same Euler–Lagrange template yields equations that look more complicated but have identical structure. |
| **Angular momentum** | 角动量 | In polar coordinates $p_\phi=mr^2\dot\phi$; conserved when $\phi$ is cyclic. |
| **Torque** | 力矩 | The generalized force conjugate to an angular coordinate, $\tau=-\partial V/\partial\phi=rF_\phi$. |
| **Constrained system** | 约束系统 | A system whose motion is restricted by geometric or kinematic conditions, reducing the number of independent coordinates. |
| **Degrees of freedom** | 自由度 | The number of coordinates that can be independently varied in a small displacement. |
| **Holonomic constraint** | 完整约束 | A constraint expressible as an equation $f(\mathbf r_1,\dots,\mathbf r_N,t)=0$ relating coordinates (and possibly time). |
| **Scleronomous constraint** | 定常约束 | A holonomic constraint with no explicit time dependence. |
| **Rheonomous constraint** | 非定常约束 | A holonomic constraint that depends explicitly on time. |
| **Nonholonomic constraint** | 非完整约束 | A constraint that cannot be written as a coordinate equation, e.g. an inequality or a nonintegrable velocity relation such as rolling without slipping. |
| **Rolling without slipping** | 无滑动滚动 | A velocity constraint relating translation to rotation; it is nonholonomic because it cannot be integrated into a pure coordinate relation. |
| **Natural coordinates** | 自然坐标 | Generalized coordinates in which the Cartesian-to-generalized transformation does not involve time explicitly; the kinetic energy is then a homogeneous quadratic function of the velocities. |
| **Homogeneous quadratic function** | 齐次二次函数 | A function $f$ satisfying $f(\lambda x)=\lambda^k f(x)$ with $k=2$; the kinetic energy in natural coordinates has this form. |
| **Jacobian matrix** | 雅可比矩阵 | The matrix $J^A{}_i=\partial x^A/\partial q_i$ of a coordinate transformation; must be invertible ($\det J\neq0$) for a valid change of coordinates. |
| **Einstein summation convention** | 爱因斯坦求和约定 | An implied sum over any repeated index in a term, e.g. $\dot x^A=(\partial x^A/\partial q_i)\dot q_i$. |
| **Lagrange multipliers** | 拉格朗日乘子 | Auxiliary dynamical functions $\lambda^\alpha(t)$ introduced to enforce constraints without eliminating coordinates. |
| **Extended Lagrangian** | 扩展拉格朗日量 | $\mathcal L'=\mathcal L+\lambda^\alpha f_\alpha$; treating $\lambda^\alpha$ as coordinates makes the constraint $f_\alpha=0$ an equation of motion. |
| **Constraint force** | 约束力 | The term $\lambda^\alpha\,\partial f_\alpha/\partial x^A$ appearing on the right-hand side of the extended Euler–Lagrange equation. |
| **Reduced Lagrangian** | 约化拉格朗日量 | The Lagrangian expressed only in the independent generalized coordinates after substituting the constraints; gives the same equations of motion as the extended formalism. |
| **Kronecker delta** | 克罗内克δ | $\delta_{ij}=1$ if $i=j$ and $0$ otherwise; used to simplify expressions involving coordinate derivatives. |
| **Generalized momentum** | 广义动量 | $p_i=\partial L/\partial\dot q_i$; the Lagrangian analogue of momentum conjugate to the coordinate $q_i$. |
| **Generalized force** | 广义力 | $\partial L/\partial q_i$; plays the role of force in the Euler–Lagrange equation $\dot p_i=\partial L/\partial q_i$. |
| **Cyclic coordinate** | 循环坐标 | A coordinate $q_i$ that does not appear explicitly in $L$ ($\partial L/\partial q_i=0$); also called an ignorable coordinate. |
| **Ignorable coordinate** | 可忽略坐标 | Same as cyclic coordinate; its conjugate momentum is conserved, so it can be partly ignored when solving the equations. |
| **Conservation law** | 守恒定律 | A statement that a dynamical quantity remains constant along the physical motion, e.g. $p_i=\text{constant}$ when $q_i$ is cyclic. |
| **Noether's theorem** | 诺特定理 | Every continuous symmetry of the Lagrangian gives rise to a conserved quantity; spatial invariance yields momentum conservation, time invariance yields energy conservation. |
| **Hamiltonian** | 哈密顿量 | Defined by $H=\sum_i p_i\dot q_i-L$; a function of coordinates and momenta obtained from the Lagrangian by a Legendre transform. |
| **Legendre transform** | 勒让德变换 | The mathematical operation that changes the independent variables from $(q,\dot q)$ to $(q,p)$, exchanging velocities for momenta. |
| **Conservation of the Hamiltonian** | 哈密顿量的守恒 | If $\partial L/\partial t=0$, then $dH/dt=0$ and $H$ is a constant of the motion. |
| **Euler's theorem for homogeneous functions** | 欧拉齐次函数定理 | If $f$ is homogeneous of degree $k$, then $\sum_i x_i\,(\partial f/\partial x_i)=kf$; gives $\sum_i\dot q_i\,(\partial T/\partial\dot q_i)=2T$ for natural coordinates. |
| **Effective potential energy** | 有效势能 | $U_{\text{eff}}(\rho)$; combines the real potential with centrifugal-like terms to reduce the problem to one-dimensional energy balance. |
| **Stable equilibrium** | 稳定平衡 | A configuration where the effective potential has a local minimum; small displacements produce restoring motion. |
| **Unstable equilibrium** | 不稳定平衡 | A configuration where the effective potential has a local maximum; small displacements cause the system to move away. |
| **Neutral equilibrium** | 随遇平衡 | A configuration where the effective potential is flat; the system can stay at rest at any nearby point. |
| **Critical angular velocity** | 临界角速度 | The value $\omega_{\text{crit}}=\sqrt{2g\alpha}$ at which the stability of the bead on a rotating parabolic wire changes character. |
