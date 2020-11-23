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
    def remove_shape(self, shape):
        if len(self.__shapes) > 0:
            self.__shapes.remove(shape)
        else:
            raise ValueError("No shape to remove")

    # Print each shape in the drawing program
    # def print_shape(self):
    #     for shapes in self.__shapes:
    #         print(self.__shapes.name_of_shape)

    def print_shape(self, shape_to_print):
        # Prints all shapes from drawing program list with specified shape name
        # Parameter: a shape to print from the drawing program: Circle, Square, Rectangle, or Triangle
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
        self.merge_sort(self.__shapes)
        """
        first = 0
        last = len(self.__shapes) - 1
        DrawingProgram.quick_sort(self, first, last)
        """
    # Merge sort
    def merge_sort(self, shape_array):
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
            self.merge_sort(left_arr)
            self.merge_sort(right_arr)
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
        # def __str__(self):
        #     my_string = ""
        #     if len(self.__shapes) >= 0:
        #         for shape in self.__shapes:
        #             my_string = my_string + shape.__str__() + "\n"
        #     return my_string


tri1 = ShapeFactory.create_triangle(3, 4.5, 4, 5)
circle1 = ShapeFactory.create_circle(3)
rect1 = ShapeFactory.create_rectangle(2, 3)
circle2 = ShapeFactory.create_circle(2)
square1 = ShapeFactory.create_square(3)

# my_shapes = [tri1, circle1, rect1, circle2]
dp = DrawingProgram()
dp.add_shape(tri1)
dp.add_shape(circle1)
dp.add_shape(rect1)
dp.add_shape(circle2)
dp.add_shape(square1)
for i in dp:
    print(i)
print("----------------------------")
dp.sort_shapes()

for i in dp:
    print(i)
print("----------------------------")
# dp.remove_shape(tri1)
# for i in dp:
#     print(i)
# #dp.print_shape("Circle")
# print("----------------------------")
# dp.add_shape(squre1)
# for i in dp:
#     print(i)
# print("----------------------------")
# print(dp.get_shape(1))
# print("----------------------------")
# dp.set_shape(tri1, 0)
#
# for i in dp:
#     print(i)
# print("----------------------------")
# dp.sort_shapes()

"""

dp.remove_shape(my_shapes[4])
print("----------------------------")
for i in dp:
    print(i)


print("----------------------------")
print(dp.get_shape(2))
print("----------------------------")
dp.set_shape("Dee", 2)
for i in dp:
    print(i)

# print("----------------------------")
# dp.print_shape()

"""