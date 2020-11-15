import abc
import math


class Shape(metaclass=abc.Meta):
    def __init__(self, name):
        self.__name = name

    @abc.abstractmethod
    def area(self):
        pass

    @abc.abstractmethod
    def perimeter(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not type(value) == str:
            raise TypeError('Name is not a string.')
        if value == "":
            raise ValueError("Assigned shape can not be empty.")
        self.__name = value

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Shape:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True
        return NotImplemented
