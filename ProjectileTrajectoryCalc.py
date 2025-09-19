import math

GRAVITATIONAL_ACCELERATION = 9.81
PROJECTILE = "∙"
x_axis_tick = "T"
y_axis_tick = "⊣"

class Projectile:
    __slots__ = ('__speed', '__height', '__angle')

    def __init__(self, speed, height, angle):
        self.__speed = speed
        self.__height = height
        self.__angle = math.radians(angle)
        
    def __str__(self):
        return f"\nProjectile details:\nspeed: {self.speed} m/s\nheight: {self.height} m\nangle: {round(self.angle)}°\ndisplacement: {self.__calculate_displacement():.1f} m\n"

    def __calculate_displacement(self):
        g = GRAVITATIONAL_ACCELERATION
        v = self.__speed
        θ = self.__angle
        h = self.__height        

        d = ((v * math.cos(θ)) * ((v * math.sin(θ)) + (math.sqrt((((v)**2) * (math.sin(θ))**2) + (2 * g * h))))) / g
        return d
    
    def __calculate_y_coordinate(self, x):
        g = GRAVITATIONAL_ACCELERATION
        v = self.__speed
        θ = self.__angle
        y0 = self.__height
        
        y = y0 + (x * math.tan(θ)) - ((g * (x**2)) / (2 * (v**2) * (math.cos(θ))**2))
        
        return y
    
    def calculate_all_coordinates(self):
        max_x = math.ceil(self.__calculate_displacement())
        coordinates = []
        
        for x in range(max_x):
            y = self.__calculate_y_coordinate(x)
            coordinates.append((x, y))
    
        return coordinates
    
    @property
    def speed(self):
        return self.__speed
    
    @property
    def height(self):
        return self.__height
    
    @property
    def angle(self):
        return round(math.degrees(self.__angle))
    
    @speed.setter
    def speed(self, value):
        self.__speed = value
        
    @height.setter
    def height(self, value):
        self.__height = value
        
    @angle.setter
    def angle(self, value):
        self.__angle = math.radians(value)
        
    def __repr__(self):
        return f'Projectile({self.speed}, {self.height}, {self.angle})'
 
ball = Projectile(10, 3, 45)
print(ball)
coordinates = ball.calculate_all_coordinates()
print(coordinates)