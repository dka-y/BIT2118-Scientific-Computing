"""Task 08: Iterative Methods - linked investment accounts"""
import numpy as np
import matplotlib.pyplot as plt

A = np.array([
    [ 3., -1.,  0.,  0.,  0.],
    [-1.,  3., -1.,  0.,  0.],
    [ 0., -1.,  3., -1.,  0.],
    [ 0.,  0., -1.,  3., -1.],
    [ 0.,  0.,  0., -1.,  3.]
])
b = np.array([12., 8., 9., 7., 10.])

def jacobi(A, b, tol=1e-8, max_iter=500):
    D = np.diag(A)
    R = A - np.diagflat(D)
    x = np.zeros_like(b)
    errors = []
    for _ in range(max_iter):
        x_new = (b - R @ x) / D
        error = np.linalg.norm(x_new - x, ord=np.inf)
        errors.append(error)
        if error < tol:
            return x_new, errors
        x = x_new
    return x, errors

returns, errors = jacobi(A, b)
exact = np.linalg.solve(A, b)

print("Equilibrium returns (%):", returns)
print("Direct solution        :", exact)

plt.semilogy(errors)
plt.xlabel("Iteration")
plt.ylabel("Maximum change")
plt.title("Jacobi convergence for linked investment returns")
plt.grid(True)
plt.show()