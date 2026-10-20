"""Task 18: solve_ivp - compound growth"""
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

r, A0 = 0.08, 10000.0

def growth(t, A):
    return [r * A[0]]

t_eval = np.linspace(0, 10, 200)
sol = solve_ivp(growth, (0, 10), [A0], t_eval=t_eval, rtol=1e-9, atol=1e-11)
exact = A0 * np.exp(r * sol.t)

print(f"Balance after 10 years (solve_ivp): KES {sol.y[0, -1]:.2f}")
print(f"Balance after 10 years (exact)    : KES {exact[-1]:.2f}")
print(f"Maximum error                     : KES {np.max(np.abs(sol.y[0] - exact)):.4e}")

plt.plot(sol.t, sol.y[0], label="solve_ivp")
plt.plot(sol.t, exact, linestyle="--", label="Exact")
plt.xlabel("Years")
plt.ylabel("Balance (KES)")
plt.title("Compound interest growth (ODE)")
plt.legend()
plt.grid(True)
plt.show()