"""Task 11: Newton & Secant - loan interest rate (IRR)"""
from scipy.optimize import root_scalar

loan_amount = 50000
repayments = [-loan_amount, 12000, 12000, 12000, 12000, 12000]

def npv(rate):
    return sum(cf / (1 + rate)**t for t, cf in enumerate(repayments))

def d_npv(rate):
    return sum(-t * cf / (1 + rate)**(t+1) for t, cf in enumerate(repayments) if t > 0)

newton = root_scalar(npv, fprime=d_npv, x0=0.10, method="newton", xtol=1e-12)
secant = root_scalar(npv, x0=0.05, x1=0.20, method="secant", xtol=1e-12)

print(f"Loan interest rate (Newton): {newton.root:.4%}")
print(f"Loan interest rate (Secant): {secant.root:.4%}")
print(f"NPV at solution            : {npv(newton.root):.6f}")