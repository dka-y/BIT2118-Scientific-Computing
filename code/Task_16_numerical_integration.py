"""Task 16: Numerical Integration - total interest earned"""
import numpy as np
from scipy.integrate import simpson

try:
    _trap = np.trapezoid
except AttributeError:
    _trap = np.trapz

months = np.arange(0, 13, dtype=float)
rate_pct = np.array([
    0.5, 0.52, 0.55, 0.53, 0.58, 0.60,
    0.62, 0.59, 0.57, 0.61, 0.63, 0.60, 0.58
])
principal = 100000.0

tr = _trap(rate_pct, months)
sr = simpson(rate_pct, x=months)

print(f"Total rate (Trapezoidal): {tr:.4f}%")
print(f"Total rate (Simpson)    : {sr:.4f}%")
print(f"Interest (Trap)  : KES {principal * tr / 100:.2f}")
print(f"Interest (Simp)  : KES {principal * sr / 100:.2f}")
print(f"Difference       : KES {abs(principal * tr / 100 - principal * sr / 100):.2f}")