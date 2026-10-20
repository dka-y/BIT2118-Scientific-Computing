"""
BIT 2118 - Integrated Project: Financial Calculator
Author: Keith Kyule | Reg: BSCCS/2025/49920

Menu-driven application combining Tasks 2-20.
Run: python code/Project_Financial_Calculator.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar, root, minimize, curve_fit
from scipy.integrate import simpson, solve_ivp
from scipy.interpolate import interp1d, CubicSpline
from scipy.linalg import lu_factor, lu_solve

try:
    _trapezoid = np.trapezoid
except AttributeError:
    _trapezoid = np.trapz


def task02_portfolio_summary():
    print("\n=== TASK 2: Portfolio Summary ===")
    balances = np.array([45.2, 38.7, 52.1, 61.0, 47.3,
                         55.8, 43.9, 66.2, 71.5, 58.4, 49.7, 63.1])
    rate = 0.0077
    print(f"Mean: KES {np.mean(balances):.2f}K")
    print(f"Min : KES {np.min(balances):.2f}K")
    print(f"Max : KES {np.max(balances):.2f}K")
    print(f"USD (first 6): {balances[:6] * rate}")


def task03_vectorized_returns():
    print("\n=== TASK 3: Vectorized Returns ===")
    import timeit
    rng = np.random.default_rng(42)
    pc = rng.uniform(-500, 500, 1_000_000)
    base = 1000.0
    def loop_v():
        out = []
        for c in pc:
            out.append(((c/100.0)/base)*100)
        return out
    def vec_v():
        return ((pc/100.0)/base)*100
    lt = timeit.timeit(loop_v, number=1)
    vt = timeit.timeit(vec_v, number=3)/3
    r = vec_v()
    print(f"First 5: {r[:5]}")
    print(f"Loop: {lt:.4f}s  Vec: {vt:.4f}s  Speed-up: {lt/vt:.1f}x")


def task04_precision_check():
    print("\n=== TASK 4: Floating-Point Precision ===")
    mp, months = 4999.99, 360
    naive = 0.0
    for _ in range(months):
        naive += mp
    arr = np.full(months, mp)
    nsum = np.sum(arr)
    true = mp * months
    print(f"True: {true:.4f}  Naive: {naive:.4f}  NumPy: {nsum:.4f}")
    print(f"Naive err: {abs(naive-true):.6f}  NumPy err: {abs(nsum-true):.6f}")


def task05_portfolio_rebalance():
    print("\n=== TASK 5: Portfolio Rebalancing ===")
    p = np.array([[5.0,3.0,2.0],[4.5,3.5,2.0],[6.0,2.5,1.5]])
    r = np.array([[0.90,0.10,0.00],[0.05,0.95,0.00],[0.00,0.00,1.00]])
    print("Rebalanced:\n", p @ r)
    print(f"det = {np.linalg.det(r):.4f}")
    print(f"Value preserved: {np.isclose(p.sum(), (p@r).sum())}")


def task06_budget_allocation():
    print("\n=== TASK 6: Budget Allocation ===")
    A = np.array([[2.5,4.0],[3.0,1.0]])
    b = np.array([23.0,14.0])
    x = np.linalg.solve(A, b)
    print(f"Online: KES {x[0]:.2f}K  In-store: KES {x[1]:.2f}K")
    print(f"Residual: {np.linalg.norm(b - A@x):.2e}")


    def task09_bank_contagion():
        print("\n=== TASK 9: Bank Contagion ===")
    B = np.array([[0.,1.,1.,0.],[1.,0.,1.,1.],[1.,1.,0.,1.],[0.,1.,1.,0.]])
    w, v = np.linalg.eig(B)
    i = np.argmax(np.real(w))
    s = np.abs(np.real(v[:, i]))
    s = s / s.sum()
    names = ["Bank A","Bank B","Bank C","Bank D"]
    print(f"Dominant eigenvalue: {np.real(w[i]):.4f}")
    for n, sc in zip(names, s):
        print(f"  {n}: {sc:.4f}")
    print(f"Most systemic: {names[np.argmax(s)]}")


def task10_break_even():
    print("\n=== TASK 10: Break-Even ===")
    def profit(q):
        return 50*q - (2000 + 30*q + 0.01*q**2)
    sol = root_scalar(profit, bracket=[0,500], method="bisect", xtol=1e-10)
    print(f"Break-even: {sol.root:.2f} units")
    q = np.linspace(0, 500, 300)
    plt.figure()
    plt.plot(q, profit(q))
    plt.axhline(0, linewidth=0.8)
    plt.axvline(sol.root, linestyle="--")
    plt.xlabel("Units"); plt.ylabel("Profit (KES)")
    plt.title("Break-even analysis"); plt.grid(True); plt.show()


def task11_irr():
    print("\n=== TASK 11: Loan IRR ===")
    cf = [-50000, 12000, 12000, 12000, 12000, 12000]
    def npv(r):
        return sum(c/(1+r)**t for t,c in enumerate(cf))
    def d(r):
        return sum(-t*c/(1+r)**(t+1) for t,c in enumerate(cf) if t>0)
    n = root_scalar(npv, fprime=d, x0=0.10, method="newton", xtol=1e-12)
    s = root_scalar(npv, x0=0.05, x1=0.20, method="secant", xtol=1e-12)
    print(f"Newton: {n.root:.4%}  Secant: {s.root:.4%}")


def task13_price_interpolation():
    print("\n=== TASK 13: Price Interpolation ===")
    h = np.array([9,10,11,12,13,14,15], dtype=float)
    p = np.array([102.0,105.5,103.0,107.5,110.0,108.5,112.0])
    lin = interp1d(h, p, kind="linear")
    cub = CubicSpline(h, p)
    print(f"Linear @11:30: {float(lin(11.5)):.2f}")
    print(f"Cubic  @11:30: {float(cub(11.5)):.2f}")


def task14_revenue_forecast():
    print("\n=== TASK 14: Revenue Forecast ===")
    m = np.array([1,2,3,4,5,6,7,8], dtype=float)
    r = np.array([120,138,161,190,225,268,315,372], dtype=float)
    def mod(t, a, b):
        return a * np.exp(b*t)
    p, _ = curve_fit(mod, m, r, p0=[100, 0.1])
    a, b = p
    print(f"R = {a:.2f}*e^({b:.4f}t)")
    print(f"Month 12: KES {mod(12,a,b):.2f}K")


def task15_price_momentum():
    print("\n=== TASK 15: Price Momentum ===")
    d = np.array([1,2,3,4,5,6,7], dtype=float)
    p = np.array([100.0,102.5,101.8,105.2,108.7,107.3,111.0])
    mom = np.zeros_like(p)
    mom[0] = (p[1]-p[0])/(d[1]-d[0])
    for i in range(1, len(d)-1):
        mom[i] = (p[i+1]-p[i-1])/(d[i+1]-d[i-1])
    mom[-1] = (p[-1]-p[-2])/(d[-1]-d[-2])
    for di, pi, mi in zip(d, p, mom):
        print(f"Day {di:.0f}: {mi:+.2f} KES/day")

        def task16_total_interest():
            print("\n=== TASK 16: Total Interest ===")
    m = np.arange(0,13, dtype=float)
    r = np.array([0.5,0.52,0.55,0.53,0.58,0.60,0.62,0.59,0.57,0.61,0.63,0.60,0.58])
    p = 100000.0
    tr = _trapezoid(r, m)
    sr = simpson(r, x=m)
    print(f"Trapezoidal: {tr:.4f}%  ->  KES {p*tr/100:.2f}")
    print(f"Simpson    : {sr:.4f}%  ->  KES {p*sr/100:.2f}")


def task17_loan_euler():
    print("\n=== TASK 17: Loan Euler ===")
    B0, r, P, h, end = 500000.0, 0.01, 11122.22, 1.0, 60
    def dB(B):
        return r*B - P
    m = np.arange(0, end+h, h)
    bal = np.zeros_like(m)
    bal[0] = B0
    for i in range(len(m)-1):
        bal[i+1] = max(bal[i] + h*dB(bal[i]), 0.0)
    print(f"Balance after 60 months: KES {bal[-1]:.2f}")


def task18_compound_growth():
    print("\n=== TASK 18: Compound Growth ===")
    r, A0 = 0.08, 10000.0
    def g(t, A):
        return [r*A[0]]
    t = np.linspace(0, 10, 200)
    s = solve_ivp(g, (0,10), [A0], t_eval=t, rtol=1e-9, atol=1e-11)
    ex = A0*np.exp(r*s.t)
    print(f"After 10 yrs: KES {s.y[0,-1]:.2f}  (exact: {ex[-1]:.2f})")


def task19_portfolio_optimization():
    print("\n=== TASK 19: Portfolio Optimization ===")
    bud = 100000.0
    minr = 0.10*bud
    def risk(z):
        return 0.04*z[0] + 0.12*z[1]
    def rcon(z):
        return 0.08*z[0] + 0.14*z[1] - minr
    def bcon(z):
        return z[0] + z[1] - bud
    cons = [{"type":"ineq","fun":rcon},{"type":"eq","fun":bcon}]
    sol = minimize(risk, x0=[50000,50000], method="SLSQP",
                   bounds=[(0,bud),(0,bud)], constraints=cons)
    x, y = sol.x
    print(f"Asset A: KES {x:,.2f}  Asset B: KES {y:,.2f}")
    print(f"Success: {sol.success}")


def task20_monte_carlo_risk():
    print("\n=== TASK 20: Monte Carlo Risk ===")
    rng = np.random.default_rng(42)
    init, thr, N = 100000.0, 0.20, 100_000
    ret = rng.normal(0.08, 0.15, N)
    fv = init*(1+ret)
    losses = fv < init*(1-thr)
    print(f"P(loss > 20%): {losses.mean():.4%}")
    print(f"5th percentile: KES {np.percentile(fv, 5):,.2f}")


def task09_bank_contagion():
    print("\n=== TASK 9: Bank Contagion ===")
    B = np.array([[0.,1.,1.,0.],[1.,0.,1.,1.],[1.,1.,0.,1.],[0.,1.,1.,0.]])
    w, v = np.linalg.eig(B)
    i = np.argmax(np.real(w))
    s = np.abs(np.real(v[:, i]))
    s = s / s.sum()
    names = ["Bank A","Bank B","Bank C","Bank D"]
    print(f"Dominant eigenvalue: {np.real(w[i]):.4f}")
    for n, sc in zip(names, s):
        print(f"  {n}: {sc:.4f}")
    print(f"Most systemic: {names[np.argmax(s)]}")


def task16_total_interest():
    print("\n=== TASK 16: Total Interest ===")
    m = np.arange(0,13, dtype=float)
    r = np.array([0.5,0.52,0.55,0.53,0.58,0.60,0.62,0.59,0.57,0.61,0.63,0.60,0.58])
    p = 100000.0
    tr = _trapezoid(r, m)
    sr = simpson(r, x=m)
    print(f"Trapezoidal: {tr:.4f}%  ->  KES {p*tr/100:.2f}")
    print(f"Simpson    : {sr:.4f}%  ->  KES {p*sr/100:.2f}")


MENU = {
    "1":  ("Portfolio Summary",      task02_portfolio_summary),
    "2":  ("Vectorized Returns",     task03_vectorized_returns),
    "3":  ("Precision Check",        task04_precision_check),
    "4":  ("Portfolio Rebalancing",  task05_portfolio_rebalance),
    "5":  ("Budget Allocation",      task06_budget_allocation),
    "6":  ("Bank Contagion",         task09_bank_contagion),
    "7":  ("Break-Even",             task10_break_even),
    "8":  ("Loan IRR",               task11_irr),
    "9":  ("Price Interpolation",    task13_price_interpolation),
    "10": ("Revenue Forecasting",    task14_revenue_forecast),
    "11": ("Price Momentum",         task15_price_momentum),
    "12": ("Total Interest",         task16_total_interest),
    "13": ("Loan Amortization",      task17_loan_euler),
    "14": ("Compound Growth",        task18_compound_growth),
    "15": ("Portfolio Optimization", task19_portfolio_optimization),
    "16": ("Investment Risk",        task20_monte_carlo_risk),
}


def main():
    print("\n" + "="*60)
    print("  BIT 2118 - FINANCIAL CALCULATOR")
    print("="*60)
    while True:
        print("\nAvailable analyses:")
        for k, (t, _) in MENU.items():
            print(f"  {k:>3}. {t}")
        print("    0. Exit")
        c = input("\nSelect: ").strip()
        if c == "0":
            print("Goodbye.")
            break
        if c in MENU:
            try:
                MENU[c][1]()
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()