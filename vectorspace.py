class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
        
    def norm(self):
        return (self.x**2 + self.y**2)**0.5
    
v1 = Vector(2, 3)
print(v1.norm())