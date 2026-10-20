"""Task 09: Eigenvalues - bank systemic risk"""
import numpy as np

banks = np.array([
    [0., 1., 1., 0.],
    [1., 0., 1., 1.],
    [1., 1., 0., 1.],
    [0., 1., 1., 0.]
])

eigenvalues, eigenvectors = np.linalg.eig(banks)

idx = np.argmax(np.real(eigenvalues))
dom_value = np.real(eigenvalues[idx])
dom_vec = np.abs(np.real(eigenvectors[:, idx]))
scores = dom_vec / dom_vec.sum()

names = ["Bank A", "Bank B", "Bank C", "Bank D"]

print(f"Dominant eigenvalue: {dom_value:.4f}")
print("\nSystemic importance scores:")
for n, s in zip(names, scores):
    print(f"  {n}: {s:.4f}")
print("\nMost systemic:", names[np.argmax(scores)])