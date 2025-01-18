from abc import ABC, abstractmethod
import re

# Base class for all equations
class Equation(ABC):
    degree: int  # Degree of the equation (e.g., 1 for linear, 2 for quadratic)
    type: str    # Type of the equation (e.g., "Linear Equation")

    def __init__(self, *args):
        # Ensure the correct number of coefficients are passed
        if (self.degree + 1) != len(args):
            raise TypeError(
                f"'Equation' object takes {self.degree + 1} positional arguments but {len(args)} were given"
            )
        # Ensure all coefficients are numbers (int or float)
        if any(not isinstance(arg, (int, float)) for arg in args):
            raise TypeError("Coefficients must be of type 'int' or 'float'")
        # The highest degree coefficient must not be zero
        if args[0] == 0:
            raise ValueError("Highest degree coefficient must be different from zero")
        # Create a dictionary with coefficients (ex: {degree: coefficient})
        self.coefficients = {(len(args) - n - 1): arg for n, arg in enumerate(args)}

    # Ensure that subclasses specify degree and type attributes
    def __init_subclass__(cls):
        if not hasattr(cls, "degree"):
            raise AttributeError(
                f"Cannot create '{cls.__name__}' class: missing required attribute 'degree'"
            )
        if not hasattr(cls, "type"):
            raise AttributeError(
                f"Cannot create '{cls.__name__}' class: missing required attribute 'type'"
            )

    # String representation of the equation
    def __str__(self):
        terms = []
        for n, coefficient in self.coefficients.items():
            if not coefficient:
                continue
            if n == 0:
                terms.append(f'{coefficient:+}')
            elif n == 1:
                terms.append(f'{coefficient:+}x')
            else:
                terms.append(f"{coefficient:+}x**{n}")
        equation_string = ' '.join(terms) + ' = 0'
        return re.sub(r"(?<!\d)1(?=x)", "", equation_string.strip("+"))

    # Abstract methods to solve and analyze the equation
    @abstractmethod
    def solve(self):
        pass
        
    @abstractmethod
    def analyze(self):
        pass


# Subclass for linear equations
class LinearEquation(Equation):
    degree = 1
    type = 'Linear Equation'
    
    def solve(self):
        # Solve ax + b = 0, so x = -b / a
        a, b = self.coefficients.values()
        x = -b / a
        return [x]

    def analyze(self):
        # Linear equation analysis (slope, y-intercept)
        slope, intercept = self.coefficients.values()
        return {'slope': slope, 'intercept': intercept}


# Subclass for quadratic equations
class QuadraticEquation(Equation):
    degree = 2
    type = 'Quadratic Equation'

    def __init__(self, *args):
        super().__init__(*args)
        # Compute the discriminant (delta) for the quadratic equation
        a, b, c = self.coefficients.values()
        self.delta = b**2 - 4 * a * c

    def solve(self):
        # Solve ax^2 + bx + c = 0 using the quadratic formula
        if self.delta < 0:
            return []  # No real solutions
        a, b, _ = self.coefficients.values()
        x1 = (-b + (self.delta) ** 0.5) / (2 * a)
        x2 = (-b - (self.delta) ** 0.5) / (2 * a)
        if self.delta == 0:
            return [x1]  # One real solution
        return [x1, x2]  # Two real solutions

    def analyze(self):
        # Analyze the vertex (x, y) and concavity of the parabola
        a, b, c = self.coefficients.values()
        x = -b / (2 * a)
        y = a * x**2 + b * x + c
        if a > 0:
            concavity = 'upwards'
            min_max = 'min'
        else:
            concavity = 'downwards'
            min_max = 'max'
        return {'x': x, 'y': y, 'min_max': min_max, 'concavity': concavity}


# Function to solve and analyze any given equation
def solver(equation):
    if not isinstance(equation, Equation):
        raise TypeError("Argument must be an Equation object")

    output_string = f'\n{equation.type:-^24}'
    output_string += f'\n\n{equation!s:^24}\n\n'
    output_string += f'{"Solutions":-^24}\n\n'
    results = equation.solve()
    match results:
        case []:
            result_list = ['No real roots']
        case [x]:
            result_list = [f'x = {x:+.3f}']
        case [x1, x2]:
            result_list = [f'x1 = {x1:+.3f}', f'x2 = {x2:+.3f}']
    for result in result_list:
        output_string += f'{result:^24}\n'
    output_string += f'\n{"Details":-^24}\n\n'
    details = equation.analyze()
    match details:
        case {'slope': slope, 'intercept': intercept}:
            details_list = [f'slope = {slope:>16.3f}', f'y-intercept = {intercept:>10.3f}']
        case {'x': x, 'y': y, 'min_max': min_max, 'concavity': concavity}:
            coord = f'({x:.3f}, {y:.3f})'
            details_list = [
                f'concavity = {concavity:>12}', 
                f'{min_max} = {coord:>18}'
            ]
    for detail in details_list:
        output_string += f'{detail}\n'
    return output_string


# Example usage with Linear and Quadratic Equations
lin_eq = LinearEquation(2, 3)  # Linear equation: 2x + 3 = 0
quadr_eq = QuadraticEquation(1, 2, 1)  # Quadratic equation: x^2 + 2x + 1 = 0

# Solve and display the results
print(solver(quadr_eq))
