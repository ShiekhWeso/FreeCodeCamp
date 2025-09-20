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
 
class Graph:
    __slots__ = ('__coordinates')
        
    def __init__(self, coordinates):
        self.__coordinates = coordinates
            
    def __repr__(self):
        return f'Graph({self.__coordinates})'
    
    def create_coordinates_table(self):
        table = "\n  x      y\n"
        for x, y in self.__coordinates:
            table += f"{x:>3}{y:>7.2f}\n"
            
        return table
        
    def create_trajectory(self):
        rounded_coords = [(round(x), round(y)) for x, y in self.__coordinates]
        x_max = max(x for x, y in rounded_coords)
        y_max = max(y for x, y in rounded_coords)
        
        matrix_list = [[" " for _ in range(x_max + 1)] for _ in range(y_max + 1)]
        
        for (x, y) in rounded_coords:
            matrix_list[-y-1][x] = PROJECTILE
            
        matrix = ["".join(line) for line in matrix_list]
        
        matrix_axes = [y_axis_tick + row for row in matrix]
        matrix_axes.append(" " + x_axis_tick * (len(matrix[0])))
        
        graph = "\n" + "\n".join(matrix_axes) + "\n"
                    
        return graph
    
def main():
    print("This is a module for calculating projectile trajectories.")
    while True:
        try:
            while True:
                choice = str(input("1. Calculate trajectory\n2. Exit\nChoose an option (1-2): "))
                if choice == '2':
                    print("Exiting the program.")
                    return
                
                elif choice == '1':
                    speed = float(input("Enter the initial speed (m/s): "))
                    if speed <= 0:
                        print("Speed must be a positive number.")
                        continue
                    height = float(input("Enter the initial height (m): "))
                    if height < 0:
                        print("Height cannot be negative.")
                        continue
                    angle = float(input("Enter the launch angle (degrees): "))
                    if angle < 0 or angle > 90:
                        print("Angle must be between 0 and 90 degrees.")
                        continue
                    
                    projectile = Projectile(speed, height, angle)
                    print(projectile)
                    coordinates = projectile.calculate_all_coordinates()
                    graph = Graph(coordinates)
                    print(graph.create_coordinates_table())
                    print(graph.create_trajectory())
                    
                else:
                    print("Invalid choice. Please select 1 or 2.")
                    continue
            
        except ValueError:
            print("Invalid input. Please enter numeric values.")    
            
if __name__ == "__main__":
    main()