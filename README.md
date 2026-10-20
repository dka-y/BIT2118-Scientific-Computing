# BIT 2118 — Scientific Computing: Financial Calculator

**Author:** Keith Kyule
**Reg No:** BSCCS/2025/49920
**Unit:** BIT 2118 — Scientific Computing
**Group Work:** Tasks 2–20 + Integrated Project (Weeks 11–13)

---

## Overview

Individual submission for the BIT 2118 Scientific Computing group work.
Each task (2–20) lives in its own file under `code/` and applies one
numerical method to a financial problem. The integrated project — a
menu-driven **Financial Calculator** — combines 16 of the tasks into one
application.

Section B/C/D documentation for each task (inputs, parameter changes,
output interpretation) is in [`docs/task_notes.md`](docs/task_notes.md).

---

## Repository Structure
BIT2118-Scientific-Computing/
├── README.md
├── code/
│ ├── Task_02_numpy_arrays.py
│ ├── Task_03_vectorization.py
│ ├── Task_04_numerical_errors.py
│ ├── Task_05_matrix_algebra.py
│ ├── Task_06_linear_systems.py
│ ├── Task_07_gaussian_lu.py
│ ├── Task_08_iterative_linear.py
│ ├── Task_09_eigenvalues.py
│ ├── Task_10_bisection_fixed_point.py
│ ├── Task_11_newton_secant.py
│ ├── Task_12_nonlinear_equations.py
│ ├── Task_13_interpolation.py
│ ├── Task_14_curve_fitting.py
│ ├── Task_15_numerical_differentiation.py
│ ├── Task_16_numerical_integration.py
│ ├── Task_17_euler_ode.py
│ ├── Task_18_scipy_ode.py
│ ├── Task_19_optimization.py
│ ├── Task_20_monte_carlo.py
│ └── Project_Financial_Calculator.py
└── docs/
└── task_notes.md

text

---

## Requirements

```bash
pip install numpy scipy matplotlib
Python 3.9+ recommended. NumPy 2.0+ assumed (np.trapezoid); a
np.trapz fallback is included.

How to Run the Project
bash
python code/Project_Financial_Calculator.py
A menu appears. Pick an analysis (1–16). Plots open in a Matplotlib
window — close them to return to the menu. Type 0 to exit.

How to Run an Individual Task
bash
python code/Task_02_numpy_arrays.py
Task → Project Mapping
#	Concept	Financial Application
2	NumPy arrays	Monthly balance summary
3	Vectorization	1M price-change returns
4	Floating-point errors	360-payment precision
5	Matrix algebra	Portfolio rebalancing
6	Linear systems	Revenue stream allocation
7	LU decomposition	Loan balance per month
8	Iterative (Jacobi)	Linked investment returns
9	Eigenvalues	Bank systemic risk
10	Bisection	Break-even volume
11	Newton / Secant	Loan IRR
12	Nonlinear systems	Market equilibrium
13	Interpolation	Intraday stock prices
14	Curve fitting	Revenue forecast
15	Differentiation	Price momentum
16	Integration	Total interest earned
17	Euler ODE	Loan amortization
18	solve_ivp ODE	Compound growth
19	Optimization	Portfolio allocation
20	Monte Carlo	Investment loss risk
