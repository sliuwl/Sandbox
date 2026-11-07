"""Verify the main HW3 formulas symbolically and with independent ODE solutions.
Requires Python packages: sympy, numpy, scipy.
Run: python hw3_verification.py
The checks write verification_results.json beside this script.
"""
from pathlib import Path
import json
import re
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

checks = {}
t = sp.symbols("t", real=True)
m, M, k, g, ell = sp.symbols("m M k g ell", positive=True)
gamma = sp.symbols("gamma", real=True)
q = sp.Function("q")(t)
v, acc = sp.diff(q,t), sp.diff(q,t,2)
ordinary_EL = lambda lag: sp.diff(sp.diff(lag,v),t)-sp.diff(lag,q)

# Problem 1: adding d f/dt is a null Lagrangian, for both coordinates.
q2 = sp.Function("q2")(t)
f = t*q*q*q2 + sp.sin(q)
df = sp.diff(f,t)
for name, coord in [("q1",q),("q2",q2)]:
    expr = sp.diff(sp.diff(df,sp.diff(coord,t)),t)-sp.diff(df,coord)
    checks["P1_null_total_derivative_"+name] = sp.simplify(expr)==0

# Problem 2: higher-order Euler-Lagrange equation and boundary derivative identity.
L2 = -m*q*acc/2-k*q*q/2
EL2 = sp.diff(sp.diff(L2,acc),t,2)-sp.diff(sp.diff(L2,v),t)+sp.diff(L2,q)
checks["P2_higher_order_EL"] = sp.simplify(EL2+m*acc+k*q)==0
checks["P2_boundary_identity"] = sp.simplify(
    L2-(m*v*v/2-k*q*q/2-sp.diff(m*q*v/2,t)))==0

# Problem 3: original and transformed equations; conserved quantity.
L3 = sp.exp(gamma*t)*(m*v*v-k*q*q)/2
checks["P3_damped_equation"] = sp.simplify(
    ordinary_EL(L3)/sp.exp(gamma*t)-(m*acc+m*gamma*v+k*q))==0
s = sp.Function("s")(t)
sd = sp.diff(s,t)
L3s = sp.simplify(L3.subs(q,sp.exp(-gamma*t/2)*s).doit())
Leff = m*sd*sd/2-(k-m*gamma**2/4)*s*s/2
checks["P3_transformed_boundary_term"] = sp.simplify(
    L3s-Leff+sp.diff(m*gamma*s*s/4,t))==0
I = sp.exp(gamma*t)*(m*v*v+m*gamma*q*v+k*q*q)/2
checks["P3_exact_invariant"] = sp.simplify(
    sp.diff(I,t)-sp.exp(gamma*t)*(v+gamma*q/2)*(m*acc+m*gamma*v+k*q))==0
E = (m*v*v+k*q*q)/2
checks["P3_mechanical_energy_loss"] = sp.simplify(
    sp.diff(E,t).subs(acc,-gamma*v-k*q/m)+m*gamma*v*v)==0

# Problem 4: independent Newton equations, differentiated constraint and work.
a = sp.symbols("alpha", positive=True)
sn, cs = sp.sin(a), sp.cos(a)
N = m*M*g*cs/(M+m*sn*sn)
A = N*sn/M
ax = -N*sn/m
ay = N*cs/m-g
checks["P4_wedge_acceleration_constraint"] = sp.trigsimp(
    ay*cs-(ax-A)*sn)==0
checks["P4_vertical_acceleration"] = sp.trigsimp(
    ay+(M+m)*g*sn*sn/(M+m*sn*sn))==0
checks["P4_horizontal_momentum"] = sp.simplify(m*ax+M*A)==0
vx, U = sp.symbols("vx U",real=True)
vy = (vx-U)*sp.tan(a)
checks["P4_energy_conservation"] = sp.trigsimp(
    m*(vx*ax+vy*ay)+M*U*A+m*g*vy)==0
checks["P4_particle_constraint_power"] = sp.trigsimp(
    N*(-sn*vx+cs*vy)+N*sn*U)==0

# Problem 5: slack angle and accessible speed; threshold endpoints.
beta = sp.symbols("beta", real=True)
cos_slack = (2-beta)/3
checks["P5_zero_tension"] = sp.simplify(beta-2+3*cos_slack)==0
checks["P5_slack_speed"] = sp.simplify(
    beta-2+2*cos_slack-(beta-2)/3)==0
checks["P5_horizontal_critical_point"] = cos_slack.subs(beta,2)==0
checks["P5_top_critical_point"] = cos_slack.subs(beta,5)==-1

# Problem 6: arbitrary single-coordinate functions; no missing factor of 2.
fq = sp.Function("f")(q)
Vq = sp.Function("V")(q)
L6 = fq*v*v-Vq
EL6 = ordinary_EL(L6)
expected6 = 2*fq*acc+sp.diff(fq,q)*v*v+sp.diff(Vq,q)
checks["P6_separable_equation"] = sp.simplify(EL6-expected6)==0
checks["P6_separate_energy"] = sp.simplify(
    sp.diff(fq*v*v+Vq,t)-v*expected6)==0

# Numerical check of the damped invariant from an independently integrated ODE.
mm, kk, gg = 2.0, 8.0, .6
sol = solve_ivp(lambda time,z:[z[1],-gg*z[1]-kk*z[0]/mm],
                (0,8),(.7,-.3),rtol=2e-11,atol=1e-13,
                dense_output=True,max_step=.02)
tt = np.linspace(0,8,501)
qq, qd = sol.sol(tt)
invariant = np.exp(gg*tt)*(mm*qd*qd+mm*gg*qq*qd+kk*qq*qq)/2
mech = (mm*qd*qd+kk*qq*qq)/2
checks["P3_numerical_invariant"] = np.max(np.abs(invariant-invariant[0]))<1e-8
checks["P3_numerical_energy_decreases"] = np.max(np.diff(mech))<1e-9

# Numerical wedge motion with a nonzero initial wedge speed.
mm, MM, grav, angle = 2.,3.,9.81,.45
normal = mm*MM*grav*np.cos(angle)/(MM+mm*np.sin(angle)**2)
Aw = normal*np.sin(angle)/MM
amx = -normal*np.sin(angle)/mm
amy = normal*np.cos(angle)/mm-grav
duration, U0, vx0, y0 = .4,-.3,.2,2.
vy0=(vx0-U0)*np.tan(angle)
U1=U0+Aw*duration
vx1,vy1=vx0+amx*duration,vy0+amy*duration
y1=y0+vy0*duration+amy*duration**2/2
displacement=U0*duration+Aw*duration**2/2
W=normal*np.sin(angle)*displacement
checks["P4_numeric_wedge_work"] = abs(MM*(U1*U1-U0*U0)/2-W)<1e-11
checks["P4_numeric_particle_work"] = abs(
    mm*(vx1*vx1+vy1*vy1-vx0*vx0-vy0*vy0)/2+mm*grav*(y1-y0)+W)<1e-11

# Independently integrate the taut pendulum up to the first loss of tension.
# Units are g/L = 1, and tension/(mg) = theta_dot**2 + cos(theta).
def first_slack(time,state):
    return state[1]**2+np.cos(state[0])
first_slack.direction=-1
first_slack.terminal=True
for bb in (2.5,3.,4.5):
    solution=solve_ivp(lambda time,z:[z[1],-np.sin(z[0])],
                      (0,10),(0,np.sqrt(bb)),events=first_slack,
                      rtol=1e-11,atol=1e-13,max_step=.01)
    angle_s,speed_s=solution.y_events[0][0]
    checks["P5_ODE_slack_beta_"+str(bb)] = (
        abs(np.cos(angle_s)-(2-bb)/3)<1e-9 and
        abs(speed_s**2-(bb-2)/3)<1e-9)

folder=Path(__file__).resolve().parent
answer=folder/"HW3_answers_EN.md"
if answer.exists():
    doc=answer.read_text(encoding="utf-8-sig")
    checks["all_six_problems_present"] = (
        re.findall(r"^## (\d+)\. ",doc,re.M)==list(map(str,range(1,7))))
    checks["all_six_restatements_present"] = (
        len(re.findall(r"^### Problem statement$",doc,re.M))==6)
    checks["balanced_display_math"] = doc.count("$$")%2==0
checks={name:bool(value) for name,value in checks.items()}
assert all(checks.values()),checks
result={"checks":checks,
        "damped_invariant_max_abs_error":float(np.max(np.abs(invariant-invariant[0])))}
(folder/"verification_results.json").write_text(
    json.dumps(result,indent=2),encoding="utf-8")
print(json.dumps(result,indent=2))

