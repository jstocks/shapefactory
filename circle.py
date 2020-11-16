import math
from shape import Shape


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def name(self):
        return 'Circle'

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius
