from abc import ABC, abstractmethod
import re
import math

class Equation(ABC):
    degree: int
    
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

    def solve(self):
        a, b = self.coefficients.values()
        x = -b / a
        return [x]  # Return the root in a list for consistency

    def analyze(self):
        slope, intercept = self.coefficients.values()
        return f"Slope: {slope}, Intercept: {intercept}"

class QuadraticEquation(Equation):
    degree = 2
    
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
        
        return {"x": x, "y": y}

lin_eq = LinearEquation(1, 3)
# LinearEquation(4, 5) ---> 4x + 5 = 0
print(lin_eq)
print(lin_eq.solve())
print(lin_eq.analyze())

quadr_eq = QuadraticEquation(1, 2, 1)
print(quadr_eq)
print(quadr_eq.solve())

# Adding main function
# making the code take input from the user