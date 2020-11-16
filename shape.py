import abc


class Shape(metaclass=abc.ABCMeta):
    """creates shape instances with name, area, and perimeter"""
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        """returns the name of the shape from the appropriate child class"""
        return self.name

    @name.setter
    def name(self, value):
        """ensures the name of the object is a string and is not empty; and
        is an allowable shape (circle, square, rectangle, or triangle"""
        if not type(value) == str:
            raise TypeError('Name is not a string.')
        if value == "":
            raise ValueError("Assigned shape can not be empty.")
        self.name = value

    @abc.abstractmethod
    def area(self):
        """returns the area of the shape from the child classes"""
        pass

    @abc.abstractmethod
    def perimeter(self):
        """returns the perimeter of the shape from the child classes"""
        pass

    def __str__(self):
        """get the shape object in String format -- this will return a string
        with (shape_name, area, perimeter)"""
        return '({:s}, {:f}, {:f})'.format(self.name(), self.area(), self.perimeter())

    def draw(self):
        """prints the name of the shape followed by the area and perimeter of the
        shape, formatted as follows: "name_of_shape, area: value_of_area,
        perimeter: value_of_perimeter" """
        return '{:s}, area: {:f}, perimeter: {:f}'.format(self.name(), self.area(), self.perimeter())

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Shape:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True
        return NotImplemented

    def __eq__(self, other):
        """compare against another Shape object for equality"""
        if isinstance(other, Shape):
            if self.name == other.name and self.area == other.area:
                return True
            return False
        raise TypeError("object passed to equals function is not a Shape")

    def __lt__(self, other):
        """compare against another Shape to see if current shape's area and
        perimeter are less than the other"""
        if isinstance(other, Shape):
            if self.name < other.name:
                return True
            if self.name == other.name and self.area < other.area:
                return True
            return False
        raise TypeError("object passed to less than is not a Shape")

    def __gt__(self, other):
        """compare against another Shape to see if current shape's area and
        perimeter are greater than the other"""
        if isinstance(other, Shape):
            if self.name > other.name:
                return True
            if self.name == other.name and self.area > other.area:
                return True
            return False
        raise TypeError("object passed to greater than is not a Shape")

