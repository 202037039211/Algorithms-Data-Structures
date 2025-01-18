# Equation Solver

This project provides a system to solve and analyze linear and quadratic equations.

## Classes:

### `Equation`
The base class for creating any equation object. Subclasses must implement `solve()` and `analyze()` methods.

### `LinearEquation`
Represents linear equations in the form `ax + b = 0`.

### `QuadraticEquation`
Represents quadratic equations in the form `ax^2 + bx + c = 0`.

## Methods:

### `solve()`
Solves the equation and returns the solutions.

### `analyze()`
Analyzes the equation and returns details such as slope, y-intercept, or the vertex for quadratic equations.

## Example Usage:

```python
# Linear Equation: 2x + 3 = 0
lin_eq = LinearEquation(2, 3)

# Quadratic Equation: x^2 + 2x + 1 = 0
quadr_eq = QuadraticEquation(1, 2, 1)

# Solve and display results
print(solver(quadr_eq))
```
