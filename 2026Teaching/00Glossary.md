# Glossary: 00Overview

A bilingual glossary of key concepts introduced in the Classical Mechanics overview.

| English | 中文 | Brief explanation |
|---------|------|-------------------|
| **Classical mechanics** | 经典力学 | The branch of physics that describes the motion of macroscopic objects using concepts such as force, energy, momentum, and action. |
| **Macroscopic object** | 宏观物体 | An object large and massive enough that its motion can usually be described accurately by classical mechanics without explicit quantum effects. |
| **Quantum mechanics** | 量子力学 | The fundamental theory describing microscopic systems (electrons, atoms, molecules), where classical mechanics breaks down. |
| **Quantum field theory** | 量子场论 | The theoretical framework combining quantum mechanics with special relativity, used to describe elementary particles and fields. |
| **Effective theory** | 有效理论 | A theory that is not fundamental but works well within a limited range of conditions or accuracy requirements. |
| **Potential energy function** | 势能函数 | A function $V(q)$ whose negative gradient gives the conservative force acting on a system. |
| **Force field** | 力场 | A mathematical description of the force exerted on a particle in classical molecular dynamics simulations |
| **Newtonian mechanics** | 牛顿力学 | The formulation of classical mechanics in ordinary physical space, based on Newton's laws of motion. |
| **Newton's Second Law** | 牛顿第二定律 | $\frac{d\vec{p}}{dt} = \vec{F}$: the rate of change of momentum equals the net force. |
| **Equation of motion** | 运动方程 | A differential equation that determines how the coordinates of a system evolve in time. |
| **Lagrangian mechanics** | 拉格朗日力学 | A formulation of classical mechanics in configuration space, based on the Lagrangian and the principle of least action. |
| **Configuration space** | 位形空间 | An $N$-dimensional space whose points specify all generalized coordinates $\{q_1, \dots, q_N\}$ of a system. |
| **Generalized coordinate** | 广义坐标 | Any set of independent coordinates $q_i$ used to describe the configuration of a mechanical system. |
| **Generalized velocity** | 广义速度 | The time derivative $\dot{q}_i$ of a generalized coordinate. |
| **Lagrangian** | 拉格朗日量 | Usually $L = T - V$, the difference between kinetic and potential energy; central to the action principle. |
| **Euler–Lagrange equation** | 欧拉–拉格朗日方程 | $\frac{\partial L}{\partial q} - \frac{d}{dt}\frac{\partial L}{\partial \dot{q}} = 0$; the equation of motion derived from the Lagrangian. |
| **Hamiltonian mechanics** | 哈密顿力学 | A formulation of classical mechanics in phase space, using positions and conjugate momenta. |
| **Phase space** | 相空间 | A $2N$-dimensional space spanned by generalized coordinates $q_i$ and conjugate momenta $p_i$; each point represents a complete state of the system. |
| **Hamiltonian** | 哈密顿量 | The Legendre transform of the Lagrangian, $H = p_i\dot{q}_i - L$; usually equal to the total energy $T + V$. |
| **Hamilton's equations** | 哈密顿方程 | $\dot{q} = \frac{\partial H}{\partial p}$, $\dot{p} = -\frac{\partial H}{\partial q}$; first-order equations of motion in phase space. |
| **Generalized momentum** | 广义动量 | Also called **conjugate momentum**; defined by $p_i = \frac{\partial L}{\partial \dot{q}_i}$. |
| **Conjugate momentum** | 共轭动量 | The momentum canonically paired with a generalized coordinate $q_i$. |
| **Legendre transform** | 勒让德变换 | The mathematical operation that transforms the Lagrangian $L(q, \dot{q}, t)$ into the Hamiltonian $H(q, p, t)$. |
| **Action** | 作用量 | $S = \int_{t_1}^{t_2} L(q, \dot{q}, t)\,dt$; the time integral of the Lagrangian along a path. |
| **Principle of least action** | 最小作用量原理 | The principle that the actual path taken by a system makes the action stationary: $\delta S = 0$. |
| **Cyclic coordinate** | 循环坐标 | A coordinate that does not appear explicitly in the Lagrangian; also called an **ignorable coordinate**. |
| **Ignorable coordinate** | 可忽略坐标 | Same as cyclic coordinate; its conjugate momentum is conserved. |
| **Symmetry** | 对称性 | A transformation (e.g., translation or rotation) that leaves the Lagrangian or Hamiltonian unchanged. |
| **Noether's theorem** | 诺特定理 | Every continuous symmetry of the action corresponds to a conserved quantity. |
| **Conserved quantity** | 守恒量 | A physical quantity that remains constant during the time evolution of an isolated system. |
| **Canonical transformation** | 正则变换 | A change of phase-space variables $(q, p) \to (Q, P)$ that preserves the form of Hamilton's equations. |
| **Poisson bracket** | 泊松括号 | $\{A, B\} = \frac{\partial A}{\partial q_i}\frac{\partial B}{\partial p_i} - \frac{\partial A}{\partial p_i}\frac{\partial B}{\partial q_i}$; encodes the symplectic structure of classical mechanics and foreshadows quantum commutators. |
| **Commutator** | 对易子 | In quantum mechanics, $[\hat{A}, \hat{B}] = \hat{A}\hat{B} - \hat{B}\hat{A}$; the quantum analogue of the Poisson bracket. |
| **Physical space** | 物理空间 | Ordinary three-dimensional Euclidean space, described by Cartesian coordinates $(x, y, z)$ or position vectors $\vec{r}$. |
| **Degrees of freedom** | 自由度 | The number of independent coordinates needed to specify the configuration of a system. |
| **Differential equation** | 微分方程 | An equation relating a function to its derivatives; most mechanical systems are described by differential equations. |
| **Analytical solution** | 解析解 | A closed-form, exact mathematical expression for the solution of an equation. |
| **Chaos / chaotic behavior** | 混沌 / 混沌行为 | Extreme sensitivity to initial conditions, making long-term prediction impossible even for deterministic systems. |
| **Special relativity** | 狭义相对论 | The theory of spacetime and motion at speeds comparable to the speed of light. |
| **General relativity** | 广义相对论 | Einstein's theory of gravitation, also formulated using an action principle. |
| **Path integral formulation** | 路径积分表述 | A formulation of quantum mechanics in which the amplitude for a process is a sum over all possible paths weighted by $e^{iS/\hbar}$. |
| **Planck's constant** | 普朗克常数 | The fundamental constant $\hbar$ that sets the scale of quantum effects. |
| **Statistical mechanics** | 统计力学 | The study of large assemblies of particles using probability theory and concepts from Hamiltonian mechanics. |
| **Field theory** | 场论 | The extension of Lagrangian methods from particles to continuous systems such as waves, fluids, and fields. |

---

## Quick reference: Three formulations of classical mechanics

| Formulation | Space | Main equation |
|-------------|-------|---------------|
| Newtonian mechanics | Physical space (物理空间) | $\frac{d\vec{p}}{dt} = \vec{F}$ |
| Lagrangian mechanics | Configuration space (位形空间) | $\frac{\partial L}{\partial q} - \frac{d}{dt}\frac{\partial L}{\partial \dot{q}} = 0$ |
| Hamiltonian mechanics | Phase space (相空间) | $\dot{q} = \frac{\partial H}{\partial p}$, $\dot{p} = -\frac{\partial H}{\partial q}$ |
