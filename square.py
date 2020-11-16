from shape import Shape


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def name(self):
        return 'Square'

    def area(self):
        return self.length ** 2

    def perimeter(self):
        return 4 * self.length
