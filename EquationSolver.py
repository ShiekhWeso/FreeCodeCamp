from abc import ABC
from abc import abstractmethod

class Equation(ABC):
    @abstractmethod
    def solve(self):
        pass
    
    @abstractmethod
    def analyze(self):
        pass
    
class LinearEquation(Equation):
    def solve(self):
        pass
    
    def analyze(self):
        pass

eq = Equation()
lin_eq = LinearEquation()