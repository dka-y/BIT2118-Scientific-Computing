"""Task 20: Monte Carlo - investment loss risk"""
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

initial, threshold, N = 100000.0, 0.20, 100_000
returns = rng.normal(0.08, 0.15, N)
final_values = initial * (1 + returns)
losses = final_values < initial * (1 - threshold)

p_loss = losses.mean()

print(f"P(loss > 20%): {p_loss:.4%}")
print(f"Loss scenarios: {losses.sum()} / {N}")
print(f"Expected value: KES {final_values.mean():,.2f}")
print(f"5th percentile: KES {np.percentile(final_values, 5):,.2f}")

running = np.cumsum(losses) / np.arange(1, N+1)
idx = np.unique(np.logspace(1, np.log10(N), 200).astype(int)) - 1

plt.semilogx(idx + 1, running[idx])
plt.xlabel("Simulations")
plt.ylabel("P(loss > 20%)")
plt.title("Monte Carlo: investment risk")
plt.grid(True)
plt.show()