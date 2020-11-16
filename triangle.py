from shape import Shape


class Triangle(Shape):
    def __init__(self, base_length, height, side_length1, side_length2):
        self.base_length = base_length
        self.height = height
        self.side_length1 = side_length1
        self.side_length2 = side_length2

    def name(self):
        return 'Triangle'

    def area(self):
        return (self.base_length * self.height) / 2

    def perimeter(self):
        return self.base_length + self.side_length1 + self.side_length2
