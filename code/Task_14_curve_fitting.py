"""Task 14: Curve Fitting - revenue forecast"""
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

months = np.array([1, 2, 3, 4, 5, 6, 7, 8], dtype=float)
revenue = np.array([120, 138, 161, 190, 225, 268, 315, 372], dtype=float)

def model(t, a, b):
    return a * np.exp(b * t)

params, _ = curve_fit(model, months, revenue, p0=[100, 0.1])
a, b = params
pred = model(months, a, b)
rmse = np.sqrt(np.mean((revenue - pred)**2))

print(f"Fitted: R(t) = {a:.2f} * exp({b:.4f} * t)")
print(f"RMSE  : KES {rmse:.2f}K")
print(f"Month 12 forecast: KES {model(12, a, b):.2f}K")

x = np.linspace(1, 12, 200)
plt.scatter(months, revenue, label="Actual")
plt.plot(x, model(x, a, b), label="Fitted")
plt.xlabel("Month")
plt.ylabel("Revenue (KES K)")
plt.title("Revenue growth & forecast")
plt.legend()
plt.grid(True)
plt.show()