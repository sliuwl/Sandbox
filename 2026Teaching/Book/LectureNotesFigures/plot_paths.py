#!/usr/bin/env python3
"""
Simple plot of three different paths connecting two fixed endpoints.
Based on Section 3 of 03LagrangianMechanics-A.md (Action).
"""

import numpy as np
import matplotlib.pyplot as plt

# Fixed endpoints
x = np.linspace(0, 1, 200)
t_i, t_f = 0.0, 1.0

# Three different paths q1(x), q2(x), q3(x)
q1 = 0.5 * x                      # straight line
q2 = 0.5 * x + 0.15 * np.sin(2 * np.pi * x)  # wavy path
q3 = 0.5 * x**2                # parabola ending at 0.5

plt.figure(figsize=(6, 4))
plt.plot(x, q1, label=r'$q_1(t)$,  $S = 8.73$', color='steelblue', lw=2)
plt.plot(x, q2, label=r'$q_2(t)$,  $S = 9.21$', color='crimson', lw=2)
plt.plot(x, q3, label=r'$q_3(t)$,  $S = 10.5$', color='forestgreen', lw=2)

# Mark endpoints
plt.scatter([t_i, t_f], [q1[0], q1[-1]], color='black', zorder=5)
plt.text(t_i, q1[0] - 0.06, r'$1$', ha='center', fontsize=12)
plt.text(t_f, q1[-1] + 0.04, r'$2$', ha='center', fontsize=12)

plt.title('Different paths between two fixed points')
plt.xlabel(r'$t$')
plt.ylabel(r'$q(t)$')
plt.legend(loc='upper left')
plt.ylim(-0.15, 0.75)
plt.tight_layout()
plt.savefig('paths_action.png', dpi=200)
plt.show()
