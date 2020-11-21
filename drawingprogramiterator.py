"""
Drawing program iterator will provides the ability to iterate across
the collection of shapes in DrawingProgram using a for loop
"""


class DrawingProgramIterator:

    # Class constructor
    # parameter: shapes[]
    def __init__(self, shapes):
        self.__shapes = shapes
        self.__index = 0

    # This method will go through the shape one by one and increase an index
    # return: shape
    def __next__(self):
        if self.__index == len(self.__shapes):
            raise StopIteration()
        shape = self.__shapes[self.__index]
        self.__index += 1
        return shape
