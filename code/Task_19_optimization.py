"""Task 19: Optimization - portfolio allocation"""
import numpy as np
from scipy.optimize import minimize

budget = 100000.0
min_ret = 0.10 * budget

def risk(z):
    return 0.04 * z[0] + 0.12 * z[1]

def r_con(z):
    return 0.08 * z[0] + 0.14 * z[1] - min_ret

def b_con(z):
    return z[0] + z[1] - budget

cons = [
    {"type": "ineq", "fun": r_con},
    {"type": "eq",   "fun": b_con}
]

sol = minimize(risk, x0=[50000, 50000], method="SLSQP",
               bounds=[(0, budget), (0, budget)], constraints=cons)

x, y = sol.x
print(f"Asset A: KES {x:,.2f}")
print(f"Asset B: KES {y:,.2f}")
print(f"Expected return: KES {0.08*x + 0.14*y:,.2f}")
print(f"Risk score     : {0.04*x + 0.12*y:,.2f}")
print(f"Success        : {sol.success}")