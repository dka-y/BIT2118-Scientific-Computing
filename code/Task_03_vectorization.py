"""Task 03: Vectorization - 1M price changes -> percentage returns"""
import numpy as np
import timeit

rng = np.random.default_rng(42)
price_changes_cents = rng.uniform(-500, 500, 1_000_000)
base_price = 1000.0

def loop_version():
    pct = []
    for c in price_changes_cents:
        pct.append(((c / 100.0) / base_price) * 100)
    return pct

def vectorized_version():
    return ((price_changes_cents / 100.0) / base_price) * 100

lt = timeit.timeit(loop_version, number=1)
vt = timeit.timeit(vectorized_version, number=3) / 3
r = vectorized_version()

print(f"First 5 percentage changes: {r[:5]}")
print(f"Loop time      : {lt:.4f} s")
print(f"Vectorized time: {vt:.4f} s")
print(f"Speed-up       : {lt/vt:.1f}x")
