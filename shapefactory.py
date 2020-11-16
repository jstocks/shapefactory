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


a_circle = Circle(1)
print(a_circle.name())
print(a_circle.area())
print(a_circle.perimeter())
print(a_circle)
print(a_circle.draw())

a_rect = Rectangle(2, 3)
print(a_rect.name())
print(a_rect.area())
print(a_rect.perimeter())
print(a_rect)
print(a_rect.draw())

a_sq = Square(2)
print(a_sq.name())
print(a_sq.area())
print(a_sq.perimeter())
print(a_sq)
print(a_sq.draw())
a_tri = Triangle(3, 4.5, 4, 5)
print(a_tri.name())
print(a_tri.area())
print(a_tri.perimeter())
print(a_tri)
print(a_tri.draw())
