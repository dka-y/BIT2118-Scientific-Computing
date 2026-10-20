"""Task 07: LU Decomposition - repeated payment vectors"""
import numpy as np
from scipy.linalg import lu_factor, lu_solve

A = np.array([
    [1.008, -0.3,   0.0  ],
    [-0.2,   1.008, -0.3  ],
    [0.0,   -0.2,   1.008]
])

payment_sets = [
    np.array([5000.0, 4800.0, 4600.0]),
    np.array([5100.0, 4900.0, 4700.0]),
    np.array([4950.0, 4750.0, 4550.0])
]

lu, piv = lu_factor(A)

for i, b in enumerate(payment_sets, start=1):
    x = lu_solve((lu, piv), b)
    residual = b - A @ x
    print(f"Month {i} balances: {x}")
    print(f"Residual norm: {np.linalg.norm(residual):.2e}\n")