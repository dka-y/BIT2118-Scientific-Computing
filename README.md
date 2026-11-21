# BIT 2118 Scientific Computing — Financial Calculator

This project applies scientific computing methods to sample financial problems. It includes 19 standalone Python scripts for Tasks 2–20 and a menu-driven calculator that runs the same analyses.

## Objectives

- Apply numerical methods to financial examples such as loan repayment, portfolio allocation, and investment risk.
- Compare methods using residuals, error estimates, timings, or plots where appropriate.
- Change inputs and explain how the results respond.

## What the calculator covers

The menu includes balance summaries, precision checks, linear systems, break-even and loan interest calculations, price interpolation, revenue forecasting, loan amortization, and investment loss simulation. Some analyses also show plots.

The [task notes](docs/task_notes.md) explain the inputs, methods, sample results, and a parameter change to try for every task.

## Setup and run

The project uses Python 3, NumPy, SciPy, and Matplotlib. From the repository root, create a virtual environment, install the libraries, and launch the calculator.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install numpy scipy matplotlib
python code/Project_Financial_Calculator.py
```

On Windows, create the environment with `py -m venv .venv` and activate it in PowerShell with `.\.venv\Scripts\Activate.ps1`. Select a menu option from 1 to 19. Close any plot window to return to the menu, or enter 0 to exit.

To run a single task, use its script in the `code/` folder. For example, this command runs the monthly balance summary.

```bash
python code/Task_02_numpy_arrays.py
```

## Group members and contributions

- Wallcot Isack — BSCCS/2025/48040
- Keith Kyule — BSCCS/2025/49920
- John Omayo - BSCCS252616702 
- Maxwell Munene — BSCCS/2025/51289
- Elton Mutugi — BSCCS/2025/47559
- Jorbat Collins — BSCCS/2025/53345
- Enock Orenge — BSCCS/2025/55142
- Christopher Mutunga — BSCCS/2025/56161
- Eugene Mukaria — BSCCS/2025/51904
- Frankline Kimutai — BSCCS/2025/48032


## Submission notes

The assignment lists *Data Science Essentials with Python* as a prerequisite. 
