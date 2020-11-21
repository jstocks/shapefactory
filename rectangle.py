"""
This is the rectangle class. It inherits from Shape.
"""
from shape import Shape


class Rectangle(Shape):
    # This class uses attributes of length and width to calculate the area and perimeter
    def __init__(self, length, width):
        """
        Initializes a rectangle object.
        parameter: length, width
        """
        self.length = length
        self.width = width

    def name(self):
        # Returns the name of the object as a string
        return 'Rectangle'

    def area(self):
        # Returns the area by multiplying the length and width
        return self.length * self.width

    def perimeter(self):
        # Returns the perimeter by multiplying the sum of the length and width by 2
        return 2 * (self.length + self.width)
