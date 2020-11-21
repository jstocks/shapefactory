"""
This is the circle class. It inherits from Shape.
"""
import math
from shape import Shape


class Circle(Shape):
    """
    This class used the radius attribute and pi to calculate the circumference and area of a circle
    """
    def __init__(self, radius, name):
        """
        Initializes a Circle object.
        Parameters: radius, name
        """
        super().__init__(name)
        self.radius = radius

    def name(self):
        # Returns the name of the object as a string
        return 'Circle'

    def area(self):
        # Returns the area by multiplying pi with the radius squared.
        return math.pi * self.radius ** 2

    def perimeter(self):
        # Returns the perimeter by multiplying 2 * pi * radius
        return 2 * math.pi * self.radius
