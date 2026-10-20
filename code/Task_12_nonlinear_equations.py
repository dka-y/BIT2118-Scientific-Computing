"""Task 12: Nonlinear Systems - market equilibrium"""
import numpy as np
from scipy.optimize import root

def market_equations(z):
    Q, P = z
    return [
        P - (100 - 2*Q),
        P - (10 + Q**1.5)
    ]

solution = root(market_equations, [20.0, 60.0])
Q_eq, P_eq = solution.x

print(f"Equilibrium quantity: {Q_eq:.4f} units")
print(f"Equilibrium price   : KES {P_eq:.4f}")
print(f"Residuals           : {market_equations(solution.x)}")
print(f"Converged           : {solution.success}")