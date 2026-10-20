"""Task 15: Numerical Differentiation - price momentum"""
import numpy as np
import matplotlib.pyplot as plt

days = np.array([1, 2, 3, 4, 5, 6, 7], dtype=float)
prices = np.array([100.0, 102.5, 101.8, 105.2, 108.7, 107.3, 111.0])

momentum = np.zeros_like(prices)
momentum[0] = (prices[1] - prices[0]) / (days[1] - days[0])
for i in range(1, len(days) - 1):
    momentum[i] = (prices[i+1] - prices[i-1]) / (days[i+1] - days[i-1])
momentum[-1] = (prices[-1] - prices[-2]) / (days[-1] - days[-2])

for d, p, m in zip(days, prices, momentum):
    arrow = "UP" if m > 0 else "DOWN"
    print(f"Day {d:.0f}: KES {p:.1f}, momentum {m:+.2f} KES/day {arrow}")

plt.plot(days, momentum, marker="o")
plt.axhline(0, linewidth=0.8, linestyle="--")
plt.xlabel("Day")
plt.ylabel("Momentum (KES/day)")
plt.title("Price momentum")
plt.grid(True)
plt.show()