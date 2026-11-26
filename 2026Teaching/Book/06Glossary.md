# Glossary: 06CentralForce

| English | 中文 | Brief explanation |
|-----------------------------------------|----------------------|-------------------------------------------------------------------|
| **Central force** | 中心力 | A force always directed toward or away from a fixed point, $\mathbf F(\mathbf r)=F(r)\,\hat{\mathbf r}$; $F<0$ is attractive and $F>0$ is repulsive. |
| **Force center** | 力心 | The fixed point from which a central force is directed; it is taken as the origin and is fixed in an inertial frame. |
| **Spherically symmetric force** | 球对称力 | A central force whose magnitude depends only on the distance $r$, not on direction. |
| **Conservative force** | 保守力 | A force derivable from a scalar potential, $\mathbf F=-\nabla V$; for a central force this is equivalent to spherical symmetry. |
| **Central potential** | 中心势 | The potential energy $V(r)$ of a conservative central force, with $F(r)=-dV/dr$. |
| **Two-body problem** | 两体问题 | The motion of two point masses under their mutual interaction, which depends only on their separation. |
| **Center of mass** | 质心 | The mass-weighted mean position $\mathbf R=(m_1\mathbf r_1+m_2\mathbf r_2)/M$ with $M=m_1+m_2$. |
| **Relative coordinate** | 相对坐标 | The separation $\mathbf r=\mathbf r_1-\mathbf r_2$, which describes the internal motion of a two-body system. |
| **Reduced mass** | 约化质量 | $\mu=m_1m_2/(m_1+m_2)$, equivalently $1/\mu=1/m_1+1/m_2$; the effective inertia of the relative coordinate. |
| **Equivalent one-body problem** | 等效单体问题 | The exact reduction of the relative motion to a single particle of mass $\mu$ moving in the fixed central field $U(r)$. |
| **Angular momentum** | 角动量 | $\mathbf L=\mathbf r\times\mathbf p$; it is conserved for any central force, since $\dot{\mathbf L}=\mathbf r\times\mathbf F=0$. |
| **Planar motion** | 平面运动 | Motion confined to a plane perpendicular to the fixed vector $\mathbf L$; when $\mathbf L=0$ the motion is along a straight line. |
| **Cyclic coordinate** | 循环坐标 | A generalized coordinate absent from the Lagrangian, whose conjugate momentum is therefore conserved. |
| **Areal velocity** | 面积速度 | The rate at which the radius vector sweeps area, $dA/dt=\tfrac12r^2\dot\theta=\ell/(2m)$. |
| **Kepler's second law** | 开普勒第二定律 | The radius vector sweeps out equal areas in equal times; equivalent to angular-momentum conservation for central-force motion. |
| **Radial equation** | 径向方程 | The equation for $r(t)$ after eliminating $\dot\theta$: $m\ddot r-\ell^2/(mr^3)=F(r)$. |
| **Effective potential** | 有效势能 | $V_{\text{eff}}(r)=V(r)+\ell^2/(2mr^2)$, which turns the radial motion into an equivalent one-dimensional problem. |
| **Equivalent one-dimensional problem** | 等效一维问题 | The radial motion regarded as that of a particle of mass $m$ moving in $V_{\text{eff}}(r)$ with $r>0$. |
| **Centrifugal barrier** | 离心势垒 | The term $\ell^2/(2mr^2)$, which diverges as $r\to0$ and prevents a particle with $\ell\neq0$ from reaching the force center. |
| **Turning point** | 转折点 | A radius where $E=V_{\text{eff}}(r)$ and $\dot r=0$, so the radial motion reverses. |
| **Periapsis / pericenter** | 近拱点 / 近心点 | The closest point of an orbit to the force center, where $r=r_{\min}$. |
| **Apoapsis / apocenter** | 远拱点 / 远心点 | The farthest point of a bound orbit from the force center, where $r=r_{\max}$. |
| **Apse (plural apsides)** | 拱点 | A turning point of the radial motion, i.e. a periapsis or an apoapsis. |
| **Circular orbit** | 圆轨道 | An orbit with $\dot r=0$ and $\ddot r=0$; it satisfies $F(r_0)=-\ell^2/(mr_0^3)$ and has energy $E_0=V_{\text{eff}}(r_0)$. |
| **Stability of a circular orbit** | 圆轨道稳定性 | A circular orbit is stable when $r_0$ is a minimum of $V_{\text{eff}}$, i.e. $V_{\text{eff}}''(r_0)>0$. |
| **Radial oscillation frequency** | 径向振荡频率 | The frequency $\omega_r=\sqrt{V_{\text{eff}}''(r_0)/m}$ of small radial oscillations about a stable circular orbit. |
| **Power-law force** | 幂律力 | An attractive force $F(r)=-kr^n$ with $k>0$; it admits stable circular orbits when $n>-3$. |
| **Binet's equation** | 比内方程 | The orbit equation in $u=1/r$: $\dfrac{d^2u}{d\theta^2}+u=-\dfrac{m}{\ell^2u^2}F\!\left(\dfrac1u\right)$. |
| **Reciprocal radius** | 倒半径 | The variable $u=1/r$, in terms of which the orbit is written as $u(\theta)$. |
| **Orbit first integral** | 轨道第一积分 | $\left(\dfrac{du}{d\theta}\right)^2=\dfrac{2mE}{\ell^2}-\dfrac{2m}{\ell^2}V\!\left(\dfrac1u\right)-u^2$, obtained from energy conservation. |
| **Kepler problem** | 开普勒问题 | Motion under an attractive inverse-square force $F=-k/r^2$, with $V=-k/r$; its orbits are conic sections. |
| **Inverse-square force** | 平方反比力 | A force whose magnitude falls as $1/r^2$; the principal exactly solvable central-force law. |
| **Conic section** | 圆锥曲线 | The orbit shape for the inverse-square force, with one focus at the force center. |
| **Eccentricity** | 偏心率 | The dimensionless constant $e$ in $r=p/(1+e\cos\phi)$, with $e=\sqrt{1+2E\ell^2/(mk^2)}$; it classifies the conic. |
| **Semi-latus rectum** | 半通径 | The constant $p=\ell^2/(mk)$, equal to $r$ at $\phi=\pi/2$ measured from the focus. |
| **Semi-major axis** | 半长轴 | The quantity $a=-k/(2E)$; positive for an ellipse, infinite for a parabola, and negative (signed) for a hyperbola. |
| **Focal distance** | 焦距 | The distance $c=ae$ from the geometric center of an ellipse to either focus. |
| **Ellipse** | 椭圆 | A bound Kepler orbit with $0\le e<1$ and $E<0$, satisfying $r_{\min}=a(1-e)$ and $r_{\max}=a(1+e)$. |
| **Parabola** | 抛物线 | The marginal Kepler orbit with $e=1$ and $E=0$. |
| **Hyperbola** | 双曲线 | An unbound Kepler orbit with $e>1$ and $E>0$. |
| **Vis-viva equation** | 活力公式 | $v^2=\dfrac{k}{m}\left(\dfrac2r-\dfrac1a\right)$, giving the orbital speed from $r$ and $a$ alone. |
| **Kepler's third law** | 开普勒第三定律 | For the gravitational two-body problem, $\tau^2=\dfrac{4\pi^2a^3}{G(m_1+m_2)}$; the period squared is proportional to the semimajor axis cubed. |
| **Laplace–Runge–Lenz vector** | 拉普拉斯–龙格–楞次矢量 | $\mathbf A=\mathbf p\times\mathbf L-mk\,\hat{\mathbf r}$, a conserved vector for the inverse-square force with magnitude $mk e$ pointing toward periapsis. |
| **Tangential impulse** | 切向冲量 | An instantaneous change of speed in the tangential direction at a fixed position, leaving $r$ and the velocity direction unchanged. |
| **Speed ratio** | 速度比 | The dimensionless ratio $\alpha=v/v_c$ of the post-impulse speed to the circular speed at the same radius. |
| **Virial theorem** | 维里定理 | For a bounded system, $2\langle T\rangle=-\langle\mathbf F\cdot\mathbf r\rangle$; for $F=-kr^n$ it becomes $2\langle T\rangle=(n+1)\langle V\rangle$. |
| **Time average** | 时间平均 | The average $\langle f\rangle_{t_{\mathrm{av}}}=\dfrac{1}{t_{\mathrm{av}}}\displaystyle\int_0^{t_{\mathrm{av}}}f(t)\,dt$ over a period or a long time interval. |
| **Virial** | 维里 | The auxiliary scalar $\mathcal G=\mathbf p\cdot\mathbf r=\tfrac12\,d(mr^2)/dt$, whose boundedness justifies the vanishing endpoint term in the virial theorem. |
| **Bound orbit** | 束缚轨道 | An orbit whose allowed radial interval is finite, so the particle oscillates between periapsis and apoapsis. |
| **Unbound orbit** | 非束缚轨道 | An orbit for which $E$ exceeds the asymptotic value of $V_{\text{eff}}$, so the particle escapes to $r\to\infty$. |
| **Radial fall** | 径向下落 | Motion with $\ell=0$, for which the centrifugal barrier is absent and an attractive force can pull the particle through the origin. |
| **Root-mean-square speed** | 均方根速度 | The mass-weighted mean-square speed $v_{\mathrm{rms}}^2=\dfrac1M\sum_i m_i\langle v_i^2\rangle$, used to express a cluster's kinetic energy. |
| **Cluster mass estimate** | 星系团质量估计 | The virial estimate $M\simeq R_{\mathrm c}v_{\mathrm{rms}}^2/(CG)$ for a gravitationally bound cluster of characteristic radius $R_{\mathrm c}$. |
| **Dark matter** | 暗物质 | Unseen gravitating matter inferred when the observed speeds in a cluster exceed those that the visible mass could bind. |
