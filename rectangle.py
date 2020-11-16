from shape import Shape


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def name(self):
        return 'Rectangle'

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)
