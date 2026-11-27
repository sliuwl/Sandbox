# Glossary: 07CoupledOscillators

| English | 中文 | Brief explanation |
|-----------------------------------------|----------------------|-------------------------------------------------------------------|
| **Coupled oscillators** | 耦合振子 | Oscillators whose equations of motion depend on one another's coordinates; here the middle spring couples the two blocks. |
| **Equilibrium configuration** | 平衡构型 | A configuration in which the net force on every block vanishes; displacements are measured from it. |
| **Spring constant / stiffness** | 弹簧劲度系数 | The coefficient relating spring force to extension; $k$ denotes the outer-spring stiffness and $k'$ the middle-spring stiffness in the two-block system. |
| **Restoring force** | 回复力 | A force tending to restore equilibrium; for a linear spring system, $\mathbf F=-\mathbf K\mathbf x$. |
| **Coupling spring** | 耦合弹簧 | A spring connecting two moving blocks; its extension is their relative displacement, $x_2-x_1$, and its energy is $\tfrac12k'(x_2-x_1)^2$. |
| **Lagrangian** | 拉格朗日量 | The difference $L=T-U$; for the linear system, $L=\tfrac12\dot{\mathbf x}^{\mathsf T}\mathbf M\dot{\mathbf x}-\tfrac12\mathbf x^{\mathsf T}\mathbf K\mathbf x$. |
| **Decoupling** | 解耦 | A change of coordinates that separates coupled equations into independent equations, each involving only one coordinate. |
| **Collective coordinate** | 集体坐标 | The sum $\eta_1=x_1+x_2$ for two equal masses; $\eta_1/2$ is their center-of-mass displacement. |
| **Relative coordinate** | 相对坐标 | The difference $\eta_2=x_2-x_1$, which measures the change in separation and the extension of the middle spring. |
| **Simple harmonic motion** | 简谐运动 | Motion satisfying $\ddot q+\omega^2q=0$ with $\omega>0$, whose solution is $q=A\cos\omega t+B\sin\omega t$. |
| **Complex amplitude** | 复振幅 | A constant encoding amplitude and phase: $q=\operatorname{Re}(Ce^{i\omega t})$, with $C=q(0)-i\dot q(0)/\omega$. |
| **Normal mode** | 简正模式 | A motion with a fixed displacement pattern and a single frequency; its shape is an eigenvector, and its time dependence is described by one normal coordinate. |
| **Mode shape** | 振型 | The relative signed displacements of the blocks in a mode, given by the components of an eigenvector in the original coordinates. |
| **In phase** | 同相位 | Oscillations with the same phase; in the two-block collective mode, $x_1=x_2$ and $\omega_1=\sqrt{k/m}$. |
| **Out of phase / opposite phase** | 反相位 | Here, oscillations differing in phase by $\pi$; in the two-block relative mode, $x_2=-x_1$ and $\omega_2=\sqrt{(k+2k')/m}$. |
| **Pure mode / mode excitation** | 纯模式 / 模式激发 | Only one mode participates when all other normal coordinates have both zero initial displacement and zero initial velocity. |
| **Superposition** | 叠加 | Adding solutions of the linear equations to obtain another solution; general motion is $\mathbf x(t)=\sum_jq_j(t)\mathbf e_{(j)}$. |
| **Degeneracy** | 简并 | Two or more independent modes share an eigenvalue; for the two-block system at $k'=0$, both frequencies equal $\sqrt{k/m}$ and the mode basis is not unique. |
| **Displacement vector** | 位移矢量 | The column vector $\mathbf x=(x_1,x_2,\ldots)^{\mathsf T}$ collecting the blocks' displacements from equilibrium. |
| **Configuration space** | 配置空间 | The space whose coordinates specify the whole system; $(x_1,x_2)$ describes two blocks on a line, not one block moving in a plane. |
| **Mass matrix** | 质量矩阵 | The matrix in $T=\tfrac12\dot{\mathbf x}^{\mathsf T}\mathbf M\dot{\mathbf x}$; for Cartesian block displacements it is diagonal, and for equal masses $\mathbf M=m\mathbf I$. |
| **Stiffness matrix** | 刚度矩阵 | The matrix in $U=\tfrac12\mathbf x^{\mathsf T}\mathbf K\mathbf x$; for a one-dimensional spring chain, diagonal entries sum attached stiffnesses and off-diagonal entries are minus the directly connecting stiffnesses. |
| **Potential-energy curvature** | 势能曲率 | The second derivatives $K_{ij}=(\partial^2U/\partial x_i\partial x_j)_{\rm eq}$, which determine the quadratic potential and linear restoring forces near equilibrium. |
| **Eigenvalue problem** | 本征值问题 | Finding nonzero vectors whose directions are preserved by a matrix; here $\mathbf K\mathbf e_{(j)}=m\omega_j^2\mathbf e_{(j)}$ for equal masses. |
| **Characteristic equation / secular equation** | 特征方程 / 久期方程 | The condition $\det(\mathbf K-\omega^2\mathbf M)=0$ that permits a nonzero mode amplitude and determines the allowed frequencies. |
| **Eigenvalue** | 本征值 | The scalar multiplying an eigenvector; the eigenvalues of $\mathbf K/m$ are $\omega_j^2$, while those of $\mathbf K$ are $m\omega_j^2$ in the equal-mass system. |
| **Eigenfrequency** | 本征频率 | The angular frequency $\omega_j$ of a mode; for stable oscillatory modes it is the positive square root of the corresponding squared-frequency eigenvalue. |
| **Eigenvector** | 本征矢 / 本征向量 | A nonzero vector giving a mode's relative signed amplitudes; multiplying it by any nonzero scalar leaves the mode shape unchanged. |
| **Orthonormality** | 正交归一 | Unit-length eigenvectors satisfy $\mathbf e_{(i)}^{\mathsf T}\mathbf e_{(j)}=\delta_{ij}$; distinct basis vectors are perpendicular. |
| **Kronecker delta** | 克罗内克符号 | The symbol $\delta_{ij}$, equal to 1 when $i=j$ and 0 otherwise. |
| **Normal coordinates** | 简正坐标 | The time-dependent coefficients in a mode expansion; for equal masses and orthonormal modes, $q_j=\mathbf e_{(j)}^{\mathsf T}\mathbf x$ and $\ddot q_j+\omega_j^2q_j=0$. |
| **Projection / expansion coefficient** | 投影 / 展开系数 | The signed weight $q_j(t)$ of a normalized mode shape in $\mathbf x(t)$; it varies with time and is not a probability or an energy fraction. |
| **Mode basis** | 模式基组 | A complete set of independent mode shapes used to express any displacement vector as a linear combination. |
| **Orthogonal matrix** | 正交矩阵 | A matrix $\mathbf S$ whose columns form an orthonormal basis, so $\mathbf S^{\mathsf T}\mathbf S=\mathbf I$ and $\mathbf S^{-1}=\mathbf S^{\mathsf T}$. |
| **Change of basis** | 换基 | Expressing the same displacement in new coordinates: $\mathbf x=\mathbf S\mathbf q$ and $\mathbf q=\mathbf S^{\mathsf T}\mathbf x$, with the mode shapes as columns of $\mathbf S$. |
| **Diagonalization** | 对角化 | Converting a matrix to diagonal form using its eigenvectors; here $\mathbf S^{\mathsf T}\mathbf K\mathbf S=m\operatorname{diag}(\omega_1^2,\omega_2^2)$, which decouples the motion since $\mathbf M=m\mathbf I$. |
| **Orthogonal similarity transformation** | 正交相似变换 | The transformation $\mathbf D=\mathbf S^{-1}\mathbf K\mathbf S=\mathbf S^{\mathsf T}\mathbf K\mathbf S$, representing the same linear operator in an orthonormal eigenvector basis. |
| **Initial-value problem** | 初值问题 | Determining the motion from initial displacements and velocities; their projections give $q_j(0)$ and $\dot q_j(0)$ for each mode. |
| **Reconstruction of motion** | 运动重构 | After solving $q_j(t)=q_j(0)\cos\omega_jt+\dot q_j(0)\sin\omega_jt/\omega_j$ for $\omega_j>0$, recover the original motion by $\mathbf x(t)=\sum_jq_j(t)\mathbf e_{(j)}$. |
| **Normal-mode energy** | 简正模式能量 | For the equal-mass normalization, $\mathcal E_j=\tfrac m2(\dot q_j^2+\omega_j^2q_j^2)$; each mode's energy is separately conserved in the undamped linear system. |
| **Weak coupling** | 弱耦合 | The regime $k'/k\ll1$, in which the two frequencies are close and their superposition can produce slow beating and energy exchange between blocks. |
| **Mean frequency / frequency splitting** | 平均频率 / 频率劈裂 | $\bar\omega=(\omega_1+\omega_2)/2$ is the mean; the splitting is $\omega_2-\omega_1=2\Delta\omega$, so $\Delta\omega$ is half the splitting. |
| **Beating** | 拍 | Slow amplitude modulation produced by the superposition of nearby frequencies; fast oscillation occurs near $\bar\omega$ while the modulation involves $\Delta\omega$. |
| **Amplitude envelope** | 振幅包络 | The slowly varying magnitude bounding the fast oscillation; in the weak-coupling single-kick approximation, the envelopes vary as $\lvert\cos\Delta\omega t\rvert$ and $\lvert\sin\Delta\omega t\rvert$. |
| **Beat period** | 拍周期 | The period of the amplitude magnitude, $T_{\rm beat}=2\pi/(\omega_2-\omega_1)=\pi/\Delta\omega$; the full displacement need not repeat after this time. |
| **Energy-transfer time** | 能量转移时间 | For weak coupling with only block 1 initially kicked, the first approximate transfer occurs at $t_{\rm transfer}=\pi/(\omega_2-\omega_1)=T_{\rm beat}/2$. |
| **Energy exchange** | 能量交换 | The block energies $E_i=\tfrac12m\dot x_i^2+\tfrac12kx_i^2$ vary through the coupling spring, while their sum plus its energy and the individual mode energies remain conserved. |
| **Strong coupling** | 强耦合 | The regime $k'\gg k$, where $\omega_2\gg\omega_1$; for the single-kick initial condition, slow collective motion is accompanied by small, rapid relative vibration. |
| **Separation of time scales** | 时间尺度分离 | Widely different frequencies produce distinct slow and fast motions; in strong coupling the single-kick fast-to-slow displacement-amplitude ratio is $\omega_1/\omega_2\ll1$. |
| **Fixed-end chain** | 固定端链 | A chain whose end blocks are attached to fixed walls by springs; the walls prevent a free collective translation. |
| **Free-end chain** | 自由端链 | A chain with internal springs but no wall springs; it supports a common translation as well as internal vibrations. |
| **Zero-frequency mode** | 零频模 | A mode with no restoring force, satisfying $\ddot q=0$ and $q(t)=q(0)+\dot q(0)t$; in the free chain it is collective translation. |
| **Translation symmetry** | 平移对称性 | Invariance under an equal shift of all blocks; for an unanchored spring chain it gives zero row sums of $\mathbf K$, a translation mode, and conserved total momentum. |
| **Center of mass** | 质心 | The mass-weighted mean position; its displacement for two masses is $R=(mx_1+Mx_2)/(m+M)$, and it moves uniformly when no external force acts. |
| **Internal vibration** | 内部振动 | Motion changing the relative positions of the masses; in the free chain, the nonzero-frequency modes leave the center of mass fixed. |
| **Degree of freedom** | 自由度 | An independent coordinate needed to specify a configuration; three blocks moving on a line have three degrees of freedom. |
| **Reduced mass** | 约化质量 | $\mu=mM/(m+M)$, the effective inertia of the relative coordinate of two free masses; one connecting spring gives $\omega=\sqrt{k/\mu}$. |
| **Generalized eigenvalue problem** | 广义本征值问题 | The mode equation $\mathbf K\mathbf b_j=\omega_j^2\mathbf M\mathbf b_j$; necessary when the mass matrix is not a scalar multiple of the identity. |
| **Mass-weighted orthogonality** | 质量加权正交性 | Distinct-frequency modes satisfy $\mathbf b_i^{\mathsf T}\mathbf M\mathbf b_j=0$; they need not be perpendicular under the ordinary dot product. |
| **Mass-weighted projection** | 质量加权投影 | For a complete mass-orthogonal mode basis, the coefficient of $\mathbf b_j$ is $Q_j=\mathbf b_j^{\mathsf T}\mathbf M\mathbf x/(\mathbf b_j^{\mathsf T}\mathbf M\mathbf b_j)$. |
| **Small-oscillation approximation** | 小振动近似 | Keeping the energies through quadratic order in small displacements and velocities near equilibrium, yielding linear equations with constant mass and stiffness matrices. |
| **Double pendulum** | 双摆 | Two masses joined by two massless links; small motions in the absolute angles $\theta_1,\theta_2$ form a coupled system with an off-diagonal kinetic-energy term. |
| **Angular amplitude ratio** | 角振幅比 | The ratio $a_2/a_1$ in a pendulum mode; for equal link lengths, the lower-to-upper horizontal displacement ratio is $(a_1+a_2)/a_1$ when $a_1\ne0$. |
