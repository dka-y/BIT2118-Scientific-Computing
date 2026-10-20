"""Task 10: Bisection - break-even analysis"""
import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

def profit(q):
    return 50 * q - (2000 + 30*q + 0.01*q**2)

solution = root_scalar(profit, bracket=[0, 500], method="bisect", xtol=1e-10)

q_vals = np.linspace(0, 500, 300)
plt.plot(q_vals, profit(q_vals))
plt.axhline(0, linewidth=0.8)
plt.axvline(solution.root, linestyle="--", label=f"Break-even = {solution.root:.1f}")
plt.xlabel("Units sold (q)")
plt.ylabel("Profit (KES)")
plt.title("Break-even analysis")
plt.legend()
plt.grid(True)
plt.show()

print(f"Break-even volume: {solution.root:.2f} units")
print(f"Profit at break-even: KES {profit(solution.root):.6f}")