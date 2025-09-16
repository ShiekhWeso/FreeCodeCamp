from abc import ABC, abstractmethod
import re
import math

class Equation(ABC):
    degree: int
    type: str  
    
    def __init__(self, *args):
        if len(args) != self.degree + 1:
            raise TypeError(f"'{self.__class__.__name__}' object takes {self.degree + 1} positional arguments but {len(args)} were given")
        if any(not isinstance(i , (int, float)) for i in args):
            raise TypeError("Coefficients must be of type 'int' or 'float'")
        if args[0] == 0:
            raise ValueError("Highest degree coefficient must be different from zero")
        
        # Store coefficients in a dictionary: {degree: coefficient}
        self.coefficients = {self.degree - i: coef for i, coef in enumerate(args)}
    
    def __init_subclass__(cls):
        if not hasattr(cls, "degree"):
            raise AttributeError(f"Cannot create '{cls.__name__}' class: missing required attribute 'degree'")
        if not hasattr(cls, "type"):
            raise AttributeError(f"Cannot create '{cls.__name__}' class: missing required attribute 'type'")
    
    def __str__(self):
        terms = []
        for n, coefficient in self.coefficients.items():
            if not coefficient:
                continue
            if n == 0:
                terms.append(f"{coefficient:+}")
            elif n == 1:
                terms.append(f"{coefficient:+}x")
            elif n > 1:
                terms.append(f"{coefficient:+}x^{n}")        
        equation_string = " ".join(terms) + " = 0"
        
        return re.sub(r'(?<!\d)1(?=x)', '', equation_string.strip("+"))
    
    @abstractmethod
    def solve(self):
        pass
    
    @abstractmethod
    def analyze(self):
        pass
    
class LinearEquation(Equation):
    degree = 1
    type = "Linear Equation"

    def solve(self):
        a, b = self.coefficients.values()
        x = -b / a
        return [x]  # Return the root in a list for consistency

    def analyze(self):
        slope, intercept = self.coefficients.values()
        return {"slope": slope, "intercept": intercept}

class QuadraticEquation(Equation):
    degree = 2
    type = "Quadratic Equation"
    
    def __init__(self, *args):
        super().__init__(*args)
        a, b, c = self.coefficients.values()
        self.delta = b**2 - 4*a*c
    
    def solve(self):
        if self.delta < 0:
            return []
        a, b, _ = self.coefficients.values()
        x1 = (-b + (math.sqrt(self.delta))) / (2 * a)
        x2 = (-b - (math.sqrt(self.delta))) / (2 * a)
        
        if self.delta == 0:
            return [x1]
        
        return [x1, x2] 
    
    def analyze(self):
        a, b, c = self.coefficients.values()
        x = -b / (2 * a)
        y = a * x**2 + b * x + c
        
        if a > 0:
            concavity = "upward"
            min_max = "min"
        else:
            concavity = "downward"
            min_max = "max"
        
        return {"x": x, "y": y, "concavity": concavity, "min_max": min_max}
    
def solver(equation):
    if not isinstance(equation, Equation):
        raise TypeError("Argument must be an instance of 'Equation' or its subclasses")
    
    output_string = f'\n{equation.type:-^24}'
    output_string += f'\n\n{equation!s:^24}\n\n'
    output_string += f'{"Solutions":-^24}\n\n'

    results = equation.solve()
    match results:
        case []:
            result_list = ["No real roots"]
        case [x]:
            result_list = [f"x = {x:+.3f}"]  # <-- .3f for 3 decimal digits
        case [x1, x2]:
            result_list = [f"x1 = {x1:+.3f}", f"x2 = {x2:+.3f}"]  # <-- .3f for 3 decimal digits        
    for result in result_list:
        output_string += f"{result:^24}\n"
        
    output_string += f'\n{"Details":-^24}\n\n'
    
    details = equation.analyze()
    match details:
        case {'slope': slope, 'intercept': intercept}:
            details_list = [f'slope = {slope:>16.3f}', f'y-intercept = {intercept:>10.3f}']
        case {'x': x, 'y': y, 'min_max': min_max, 'concavity': concavity}:
            coord = f'({x:.3f}, {y:.3f})'
            details_list = [f'concavity = {concavity:>12}', f'{min_max} = {coord:>18}']
    for detail in details_list:
        output_string += f'{detail}\n'    

    return output_string

lin_eq = LinearEquation(2, 3)
# LinearEquation(4, 5) ---> 4x + 5 = 0
print(lin_eq)
print(lin_eq.solve())
print(lin_eq.analyze())

quadr_eq = QuadraticEquation(1, 2, 1)
print(quadr_eq)
print(quadr_eq.solve())

print(solver(quadr_eq))

# Adding main function
# making the code take input from the user