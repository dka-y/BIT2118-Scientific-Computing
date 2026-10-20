"""Task 06: Linear Systems - Revenue streams"""
import numpy as np

A = np.array([[2.5, 4.0], [3.0, 1.0]])
b = np.array([23.0, 14.0])

solution = np.linalg.solve(A, b)
residual = b - A @ solution

print(f"Online sales volume  : KES {solution[0]:.2f}K")
print(f"In-store sales volume: KES {solution[1]:.2f}K")
print(f"Verification A@x     : {A @ solution}")
print(f"Residual norm        : {np.linalg.norm(residual):.2e}")