from circle import Circle
from square import Square
from rectangle import Rectangle
from triangle import Triangle


class ShapeFactory:
    """creates shapes using constructs of class Shape"""

    @staticmethod
    def create_circle(radius):
        """creates a circle based on the class Shape and child class circle"""
        return Circle(radius)

    @staticmethod
    def create_square(length):
        """creates a square based on the class Shape and child class square"""
        return Square(float(length))

    @staticmethod
    def create_rectangle(length, width):
        """creates a rectangle based on the class Shape and child class rectangle"""
        return Rectangle(float(length), float(width))

    @staticmethod
    def create_triangle(base_length, height, side_length1, side_length2):
        """creates a triangle based on the class Shape and child class triangle"""
        return Triangle(float(base_length), float(height), float(side_length1),
                        float(side_length2))



