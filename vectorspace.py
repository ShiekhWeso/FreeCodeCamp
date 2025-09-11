class R2Vector:
    def __init__(self, *, x, y):
        self.x = x
        self.y = y 
    
    def norm(self):
        # self.__dict__.values() is the same as vars(self).values()
        return sum(val**2 for val in vars(self).values())**0.5
    
    def __str__(self):
        # return f"({self.x}, {self.y})"
        return str(tuple(getattr(self, i) for i in vars(self)))
    
    def __repr__(self):
        arg_list = [f"{key} = {val}" for key, val in vars(self).items()]
        args = ", ".join(arg_list)
        return f"{self.__class__.__name__}({args})"
    
    def __add__(self, other):
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i : getattr(self, i) + getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs) 
    
    def __sub__(self, other):
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i : getattr(self, i) - getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)
        
class R3Vector(R2Vector):
    def __init__(self, *, x, y, z):
        super().__init__(x=x , y=y)
        self.z = z
    
v1 = R2Vector(x=2, y=3)
v2 = R3Vector(x=2, y=2, z=3)
v3 = R2Vector(x=0.5, y=1.25)
print(f"v1 = {v1}\nv2 = {v2}\nv3 = {v3}")
v4 = v1 + v3
print(f"v4 = v1 + v3 = {v4}")
v5 = v1 - v3
print(f"v5 = v1 - v3 = {v5}")