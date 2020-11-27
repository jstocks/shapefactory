"""
This is the triangle class, it inherits from Shape.
"""
from shape import Shape


class Triangle(Shape):
    """
    This class is given 3 lengths to form a triangle shape
    """
    def __init__(self, base_length, height, side_length1, side_length2):
        """
        Initializes a triangle object.
        Parameters: 3 heights, and the name
        """
        if type(base_length) == str or \
                type(height) == str or \
                type(side_length1) == str or \
                type(side_length2) == str:
            raise TypeError("Lengths and heights cannot be strings")
        if base_length < 0 or \
                height < 0 or \
                side_length1 < 0 or \
                side_length2 < 0:
            raise ValueError("Lengths and heights cannot be less than 0")
        self.base_length = base_length
        self.height = height
        self.side_length1 = side_length1
        self.side_length2 = side_length2

    def name(self):
        # returns the name of the object as a string
        return 'Triangle'

    def area(self):
        # returns the area by multiplying the base_length and the height, then dividing by 2
        return (self.base_length * self.height) / 2

    def perimeter(self):
        # returns the perimeter by adding all three side lengths of the triangle
        return self.base_length + self.side_length1 + self.side_length2
