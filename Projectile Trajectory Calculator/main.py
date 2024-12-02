import math

# Constants for gravitational acceleration and graphical symbols
GRAVITATIONAL_ACCELERATION = 9.81
PROJECTILE = "∙"
x_axis_tick = "T"
y_axis_tick = "⊣"

class Projectile:
    # Using slots to limit attributes and optimize memory
    __slots__ = ('__speed', '__height', '__angle')

    def __init__(self, speed, height, angle):
        self.__speed = speed
        self.__height = height
        self.__angle = math.radians(angle)  # Convert angle to radians for calculations

    def __str__(self):
        # Return formatted string with projectile details
        return f'''
Projectile details:
speed: {self.speed} m/s
height: {self.height} m
angle: {self.angle}°
displacement: {round(self.__calculate_displacement(), 1)} m
'''

    def __calculate_displacement(self):
        # Calculate horizontal and vertical components of motion
        horizontal_component = self.__speed * math.cos(self.__angle)
        vertical_component = self.__speed * math.sin(self.__angle)
        
        # Calculate displacement using kinematic equations
        squared_component = vertical_component ** 2
        gh_component = 2 * GRAVITATIONAL_ACCELERATION * self.__height
        sqrt_component = math.sqrt(squared_component + gh_component)
        
        return horizontal_component * (vertical_component + sqrt_component) / GRAVITATIONAL_ACCELERATION

    def __calculate_y_coordinate(self, x):
        # Calculate the y-coordinate at a given x using projectile motion equations
        height_component = self.__height
        angle_component = math.tan(self.__angle) * x
        acceleration_component = (GRAVITATIONAL_ACCELERATION * x ** 2) / (
            2 * self.__speed ** 2 * math.cos(self.__angle) ** 2)
        
        return height_component + angle_component - acceleration_component

    def calculate_all_coordinates(self):
        # Generate coordinates for the trajectory
        return [
            (x, self.__calculate_y_coordinate(x))
            for x in range(math.ceil(self.__calculate_displacement()))
        ]

    # Getters and setters for attributes
    @property
    def height(self):
        return self.__height

    @property
    def angle(self):
        return round(math.degrees(self.__angle))

    @property
    def speed(self):
        return self.__speed

    @height.setter
    def height(self, n):
        self.__height = n

    @angle.setter
    def angle(self, n):
        self.__angle = math.radians(n)

    @speed.setter
    def speed(self, s):
        self.__speed = s

class Graph:
    def __init__(self, coordinates):
        self.__coordinates = coordinates

    def create_coordinates_table(self):
        # Create a formatted table of trajectory coordinates
        table = '\n  x      y\n'
        for x, y in self.__coordinates:
            table += f'{x:>3}{y:>7.2f}\n'
        return table

    def create_trajectory(self):
        # Generate a simple text-based graph of the projectile trajectory
        rounded_coords = [(round(x), round(y)) for x, y in self.__coordinates]

        x_max = max(rounded_coords, key=lambda i: i[0])[0]
        y_max = max(rounded_coords, key=lambda j: j[1])[1]

        matrix_list = [[" " for _ in range(x_max + 1)] for _ in range(y_max + 1)]

        for x, y in rounded_coords:
            if 0 <= y < len(matrix_list):
                matrix_list[-1 - y][x] = PROJECTILE

        matrix = ["".join(line) for line in matrix_list]

        matrix_axes = [y_axis_tick + row for row in matrix]
        matrix_axes.append(" " + x_axis_tick * (len(matrix[0])))
        return "\n" + "\n".join(matrix_axes) + "\n"

def projectile_helper(speed, height, angle):
    ball = Projectile(speed, height, angle)
    
    # Display projectile details
    print(ball)
    
    # Calculate and print trajectory coordinates
    coordinates = ball.calculate_all_coordinates()
    graph = Graph(coordinates)
    print(graph.create_coordinates_table())
    
    # Display the trajectory graph
    print(graph.create_trajectory())

# Example call to visualize trajectory
if __name__ == '__main__':
    projectile_helper(10, 3, 45)
