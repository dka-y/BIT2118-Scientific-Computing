"""Task 02: NumPy Arrays - Portfolio Summary (Financial Adaptation)"""
import numpy as np

balances_kes = np.array([
    45.2, 38.7, 52.1, 61.0, 47.3,
    55.8, 43.9, 66.2, 71.5, 58.4,
    49.7, 63.1
])
exchange_rate = 0.0077

print(f"Mean monthly balance : KES {np.mean(balances_kes):.2f}K")
print(f"Minimum balance      : KES {np.min(balances_kes):.2f}K")
print(f"Maximum balance      : KES {np.max(balances_kes):.2f}K")
print(f"Balances in USD (first 6): {balances_kes[:6] * exchange_rate}")
