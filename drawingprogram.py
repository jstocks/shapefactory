"""
This is a drawing program that can draw
circle, square, rectangle and triangle
"""


class DrawingProgram:

    # Class constructor
    # parameter: shapes[]
    def __init__(self, shapes=None):
        self.__shapes = shapes

    # Provide a way to access the elements of a Drawing Program
    # Return: self
    def __iter__(self):
        return self

    # Add a shape to the drawing program
    # Parameter: a shape to add to the drawing program
    def add_shape(self, shapes):
        if len(shapes) > 0:
            for shape in shapes:
                self.__shapes.append(shape)
        else:
            raise ValueError("No shape to add")

    # Remove a shape from the drawing program
    # Parameter: a shape to remove from the drawing program
    def remove_shape(self, shape):
        if len(self.__shapes) > 0:
            self.__shapes.remove(shape)
        else:
            raise ValueError("No shape to remove")

    # Print each shape in the drawing program
    def print_shape(self):
        for shapes in self.__shapes:
            print(self.__shapes.name_of_shape)

    # Sort shape in ascending order
    def sort_shapes(self):
        first = 0
        last = len(self.__shapes) - 1
        DrawingProgram.quick_sort(self, first, last)

    # Using Quick Sort to sort shape
    # Parameter: First location of index, Last location of index
    def quick_sort(self, first, last):
        if last - first > 0:
            partition_point = DrawingProgram.partition(self, first, last)
            DrawingProgram.quick_sort(self, first, partition_point-1)
            DrawingProgram.quick_sort(self, partition_point+1, last)

    # Partition the list
    # Parameter: First index location, Last index location
    # Return: Index of the last element
    def partition(self, first_index, last_index):
        pivot = self.__shapes[first_index]
        pivot_index = first_index
        index_of_the_last_element = last_index

        less_than_pivot_index = index_of_the_last_element
        greater_than_pivot_index = first_index + 1

        while True:
            temp = ""

            # While next value < pivot && index of next value != the last index.
            while self.__shapes[greater_than_pivot_index] < pivot and greater_than_pivot_index < last_index:
                greater_than_pivot_index += 1

            # While the last value > pivot && the last value index >= to first index
            while self.__shapes[less_than_pivot_index] > pivot and less_than_pivot_index >= first_index:
                less_than_pivot_index -= 1

            # if current index < the last index
            if greater_than_pivot_index < less_than_pivot_index:
                temp = self.__shapes[greater_than_pivot_index]
                self.__shapes[greater_than_pivot_index] = self.__shapes[less_than_pivot_index]
                self.__shapes[less_than_pivot_index] = temp
            else:
                break

        # Swap the places
        self.__shapes[pivot_index] = self.__shapes[less_than_pivot_index]
        self.__shapes[less_than_pivot_index] = pivot

        return less_than_pivot_index

    # Get the shape in the list of shape
    # Parameter: Index
    # Return: Value of shape in the index or Raise error when the index is out of range
    def get_shape(self, index):
        if (index >= 0) and (index < len(self.__shapes)):
            return self.__shapes[index]
        else:
            raise ValueError("Error: index out of range. You entered: " + str(index))

    # Put shape in the index location
    # Parameter: A shape to put in the list of shape
    #            A index where you want to put the shape
    def set_shape(self, a_shape, index):
        if index >= 0 and (index < len(self.__shapes)):
            self.__shapes[index] = a_shape
        else:
            raise ValueError("ERROR: the value you entered is out of range. You entered :" + str(index))

        # Provide a name of each shape in the list of shapes
        def __str__(self):
            my_string = ""
            if len(self.__shapes) >= 0:
                for shape in self.__shapes:
                    my_string = my_string + shape.__str__() + "\n"
            return my_string


