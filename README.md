# linear-equations-methods
Solving systems of linear equations using the Gaussian elimination and Gauss-Seidel methods in Python.

The project was developed as part of university work during my second year of study.

## Key Variables

* Ag - coefficient matrix for the Gaussian elimination method;
* Bg - right-hand side vector for the Gaussian elimination method;
* Az - coefficient matrix for the Gauss-Seidel method;
* Bz - right-hand side vector for the Gauss-Seidel method;
* matrix - input coefficient matrix in the Gaussian elimination function;
* vector - right-hand side vector in the Gaussian elimination function;
* n - size of the system of linear equations;
* max_el - maximum absolute element in the current column;
* max_row - index of the row containing the maximum element;
* c - elimination coefficient;
* x - solution vector obtained by the Gaussian elimination method;
* x0 - initial approximation for the Gauss-Seidel method;
* x_new - updated approximation during an iteration;
* EPS - convergence accuracy;
* max_iter - maximum number of iterations;
* iter_count - current iteration number;
* sum_ - sum of the calculated terms for the current equation;
* result - solution obtained by the Gaussian elimination method;
* solution - solution obtained by the Gauss-Seidel method.

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/dolzhkris/linear-equations-methods.git
```

2. Run the program:

```bash
python main.py
```
