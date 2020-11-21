"""
This is the square class it inherits from Shape.
"""
from shape import Shape


class Square(Shape):
    """
    This class uses the length of one side to form a square.
    """
    def __init__(self, length, name):
        super().__init__(name)
        self.length = length

    def name(self):
        # returns the name of the object as a string
        return 'Square'

    def area(self):
        # returns the area by squaring the length
        return self.length ** 2

    def perimeter(self):
        # returns the perimeter by multuplying the length by 4
        return 4 * self.length
