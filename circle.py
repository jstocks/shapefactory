import math


class Circle(Shape):
    def __init__(self, name, radius):  # no reference to name, I think unecessary
        self.name = name
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius
