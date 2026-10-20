"""Task 04: Floating-Point Errors - 360 monthly payments"""
import numpy as np

monthly_payment = 4999.99
months = 360

naive_total = 0.0
for _ in range(months):
    naive_total += monthly_payment

payments = np.full(months, monthly_payment)
numpy_total = np.sum(payments)
true_total = monthly_payment * months

print(f"True total       : KES {true_total:.4f}")
print(f"Naive loop total : KES {naive_total:.4f}")
print(f"NumPy sum total  : KES {numpy_total:.4f}")
print(f"Naive error      : KES {abs(naive_total - true_total):.6f}")
print(f"NumPy error      : KES {abs(numpy_total - true_total):.6f}")
print(f"Tolerance check  : {np.isclose(naive_total, true_total)}")