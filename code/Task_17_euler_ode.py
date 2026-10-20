"""Task 17: Euler ODE - loan amortization"""
import numpy as np
import matplotlib.pyplot as plt

B0, r, P = 500000.0, 0.01, 11122.22
h, end_month = 1.0, 60

def balance_rate(B):
    return r * B - P

months = np.arange(0, end_month + h, h)
balance = np.zeros_like(months)
balance[0] = B0

for i in range(len(months) - 1):
    balance[i+1] = balance[i] + h * balance_rate(balance[i])
    if balance[i+1] < 0:
        balance[i+1] = 0

print(f"Balance after 60 months (Euler): KES {balance[-1]:.2f}")

plt.plot(months, balance, marker="o", markersize=3)
plt.xlabel("Month")
plt.ylabel("Loan balance (KES)")
plt.title("Loan amortization via Euler method")
plt.grid(True)
plt.show()