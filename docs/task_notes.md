# Task Notes — B, C, D for Tasks 2–20

Each entry records the inputs and operation (B), the parameter change
and its effect (C), and the output interpretation (D). Section E
(financial-calculator adaptation) lives in `code/Task_XX_*.py`.

---

## Task 2 — NumPy Arrays
**B.** 12 monthly balances; `np.mean`, `np.min`, `np.max`, vectorized
conversion to USD.  
**C.** Higher balances raise the mean; min shows liquidity risk.  
**D.** Mean = average account level. Min flags possible cash-flow risk.

## Task 3 — Vectorization
**B.** 1,000,000 price changes; loop vs vectorized `(change/100/base)*100`.  
**C.** Wider range → larger percentage returns; speed-up ratio unchanged.  
**D.** Vectorized typically 50–200× faster — critical for tick data.

## Task 4 — Floating-Point Errors
**B.** 360 payments of KES 4,999.99; naive loop vs NumPy sum.  
**C.** Non-round payment exposes accumulation error.  
**D.** Small error (fractions of a cent) — `np.isclose` for comparisons.

## Task 5 — Matrix Algebra
**B.** 3×3 portfolio × rebalance matrix. `@`, `det`, value preservation.  
**C.** Different rebalance fractions → new allocation, det near 1.  
**D.** Total value preserved; det ≈ 1 confirms rebalance is
volume-preserving.

## Task 6 — Linear Systems
**B.** 2×2 system: revenue + transactions → online vs in-store split.  
**C.** Different total b → new split; residual stays ~0.  
**D.** Solution gives exact contribution per stream. Residual ~0
confirms correctness.

## Task 7 — LU Decomposition
**B.** Same 3×3 matrix, 3 payment vectors. Factor once, solve thrice.  
**C.** Fourth vector costs negligible extra time.  
**D.** Factor-once/solve-many is exactly how monthly loan books are
recomputed.

## Task 8 — Iterative Methods
**B.** 5×5 linked-returns matrix; Jacobi vs direct solve.  
**C.** Higher target returns → higher equilibrium; convergence path
same.  
**D.** Equilibrium returns match direct solve — convergence graph shows
error decay.

## Task 9 — Eigenvalues
**B.** 4-bank lending adjacency matrix; dominant eigenvector.  
**C.** Extra edges → centrality shifts; dominant eigenvalue grows.  
**D.** Banks B and C tied as most systemic (structural symmetry).
Mirrors central-bank contagion models.

## Task 10 — Bisection
**B.** Profit(q) = 50q − (2000 + 30q + 0.01q²); bisection on [0, 500].  
**C.** Higher fixed cost → break-even moves right.  
**D.** Break-even ≈ 64 units. Root of the profit function.

## Task 11 — Newton / Secant
**B.** NPV of 5-year loan; find rate where NPV = 0.  
**C.** Different cash flows → different IRR; both methods agree.  
**D.** IRR ≈ 6.40% is the effective annual borrowing cost.

## Task 12 — Nonlinear Systems
**B.** Supply / demand equilibrium via `scipy.optimize.root`.  
**C.** Different initial guess → different root if multiple exist.  
**D.** Q ≈ 15.24, P ≈ 69.51. Residuals ≈ 0 confirm solution.

## Task 13 — Interpolation
**B.** 7 hourly prices; linear vs cubic spline at 11:30.  
**C.** Denser sample → smaller difference between methods.  
**D.** Linear fast; cubic smoother. Used for intraday pricing.

## Task 14 — Curve Fitting
**B.** 8 monthly revenues; fit `a·exp(b·t)`; forecast month 12.  
**C.** Linear model → worse RMSE (curvature missed).  
**D.** Fitted parameters capture growth; month-12 forecast ≈ KES
520K.

## Task 15 — Numerical Differentiation
**B.** 7 daily closes; forward/central/backward differences.  
**C.** Smaller step → more accurate momentum.  
**D.** Momentum = rate of price change; positive = up-trend signal.

## Task 16 — Numerical Integration
**B.** 12 monthly rates; trapezoid vs Simpson; × principal.  
**C.** Higher rate curve → larger interest; methods diverge slightly.  
**D.** Simpson more accurate (parabolic fit). Total interest ≈ KES
6,900 on KES 100K.

## Task 17 — Euler ODE
**B.** `dB/dt = r·B − P`; Euler step h=1 month; 60 months.  
**C.** Smaller h → smaller truncation error, more computation.  
**D.** Balance decays to 0 at month 60 — matches amortization formula.

## Task 18 — solve_ivp ODE
**B.** `dA/dt = r·A`; solve_ivp with adaptive stepping.  
**C.** Higher r → larger final balance; error vs exact ~1e-9.  
**D.** Balance ≈ KES 22,255 after 10 years at 8% — matches closed-form.

## Task 19 — Optimization
**B.** Minimize risk `0.04x + 0.12y` s.t. return ≥ KES 10K, x + y = KES
100K.  
**C.** Higher required return → more into Asset B.  
**D.** Optimum is a corner solution: all into Asset A if possible,
otherwise minimum Asset B — linear risk.

## Task 20 — Monte Carlo
**B.** 100,000 normal return draws (μ=8%, σ=15%); count losses > 20%.  
**C.** Larger σ → higher loss probability; slower convergence.  
**D.** P(loss > 20%) ≈ 3.1%; 5th percentile (VaR₉₅) ≈ KES 83,125.
Used in bank regulatory stress tests.