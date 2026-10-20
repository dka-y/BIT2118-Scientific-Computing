"""Task 05: Matrix Algebra - Portfolio rebalancing"""
import numpy as np

portfolio = np.array([
    [5.0, 3.0, 2.0],
    [4.5, 3.5, 2.0],
    [6.0, 2.5, 1.5]
])

rebalance = np.array([
    [0.90, 0.10, 0.00],
    [0.05, 0.95, 0.00],
    [0.00, 0.00, 1.00]
])

rebalanced = portfolio @ rebalance

print("Original portfolio (KES millions):\n", portfolio)
print("\nRebalanced portfolio (KES millions):\n", rebalanced)
print("\nDeterminant of rebalance matrix:", np.linalg.det(rebalance))
print("Total value preserved:", np.isclose(portfolio.sum(), rebalanced.sum()))