"""Task 13: Interpolation - stock prices"""
import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt

hours = np.array([9, 10, 11, 12, 13, 14, 15], dtype=float)
prices = np.array([102.0, 105.5, 103.0, 107.5, 110.0, 108.5, 112.0])

linear = interp1d(hours, prices, kind="linear")
cubic = CubicSpline(hours, prices)

fine = np.arange(9, 15 + 1/6, 1/6)

print(f"Linear @ 11:30: KES {float(linear(11.5)):.2f}")
print(f"Cubic  @ 11:30: KES {float(cubic(11.5)):.2f}")

plt.scatter(hours, prices, label="Hourly", zorder=5)
plt.plot(fine, linear(fine), label="Linear")
plt.plot(fine, cubic(fine), label="Cubic")
plt.xlabel("Hour")
plt.ylabel("Price (KES)")
plt.title("Intraday price interpolation")
plt.legend()
plt.grid(True)
plt.show()