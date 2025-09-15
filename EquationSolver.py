from abc import ABC, abstractmethod

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
        equation_string = " ".join(terms) + " = 0"
        
        return equation_string.strip("+")
    
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
        return x
    
    def analyze(self):
        slope, intercept = self.coefficients.values()
        return f"Slope: {slope}, Intercept: {intercept}"
    
lin_eq = LinearEquation(2, 3)
# LinearEquation(4, 5) ---> 4x + 5 = 0
print(lin_eq)
print(lin_eq.solve())
print(lin_eq.analyze())

# Adding main function
# making the code take input from the user