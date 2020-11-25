"""
This is a drawing program that can draw
circle, square, rectangle and triangle
"""
from drawingprogramiterator import DrawingProgramIterator
from shapefactory import ShapeFactory


class DrawingProgram:

    # Class constructor
    # parameter: shapes[]
    def __init__(self, shapes=None):
        if shapes is None:
            shapes = []
        self.__shapes = shapes

    # Provide a way to access the elements of a Drawing Program
    # Return: self
    def __iter__(self):
        return DrawingProgramIterator(self.__shapes)

    # Add a shape to the drawing program
    # Parameter: a shape to add to the drawing program
    def add_shape(self, shape):
        self.__shapes.append(shape)

    # Remove a shape from the drawing program
    # Parameter: a shape to remove from the drawing program
    def remove_shape(self, shape_to_remove):
        original_len = len(self.__shapes)
        if original_len > 0:
            self.__shapes = [shape for shape in self.__shapes if shape.name() !=
                             shape_to_remove]
            original_len -= len(self.__shapes)
            print("Removed " + str(original_len) + " " + str(shape_to_remove) + "(s).")
            return original_len
        else:
            raise ValueError("No shape to remove")

    # Print shape
    # Parameter: shape_to_print
    def print_shape(self, shape_to_print):
        # Prints all shapes from drawing program list with specified shape name
        # Parameter: a shape to print from the drawing program: Circle, Square, Rectangle, or Triangle
        if len(shape_to_print) > 0:
            if shape_to_print == "Circle" or \
                    shape_to_print == "Square" or \
                    shape_to_print == "Rectangle" or \
                    shape_to_print == "Triangle":
                for shape in self.__shapes:
                    if shape.name() == shape_to_print:
                        print(shape)
        else:
            raise ValueError("Must specify which shape to print: Circle, Square, Rectangle, or Triangle")

    # Sort shape in ascending order
    def sort_shapes(self):
        if len(self.__shapes) > 0:
            self.__merge_sort__(self.__shapes)

    # Merge sort
    def __merge_sort__(self, shape_array):
        size = len(shape_array)
        """base condition; return the array for size equal to or less than 1"""
        if size <= 1:
            return shape_array
        if size > 1:
            """split the array in half"""
            middle = size // 2
            left_arr = shape_array[:middle]
            right_arr = shape_array[middle:]
            """sort the two halves independently and recursively"""
            self.__merge_sort__(left_arr)
            self.__merge_sort__(right_arr)
            a = b = c = 0
            left_size = len(left_arr)
            right_size = len(right_arr)
            """copy data to temporary arrays left and right"""
            while a < left_size and b < right_size:
                if left_arr[a] < right_arr[b]:
                    shape_array[c] = left_arr[a]
                    a += 1
                else:
                    shape_array[c] = right_arr[b]
                    b += 1
                c += 1
            """check if any element remains in left or right array"""
            while a < left_size:
                shape_array[c] = left_arr[a]
                a += 1
                c += 1
            while b < right_size:
                shape_array[c] = right_arr[b]
                b += 1
                c += 1

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
        my_string = my_string.rstrip()
        return my_string



