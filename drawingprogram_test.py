"""
This is the class to test methods in a drawingprogram class
"""

import unittest
from drawingprogram import DrawingProgram
from shapefactory import ShapeFactory


class MyDrawingProgramTest(unittest.TestCase):
    def test_init(self):
        drawing_program = DrawingProgram()
        self.assertEqual("", drawing_program.__str__(), "DrawingProgram should be empty but it not")

    # Test set_shape method with valid index
    def test_set_shape_valid_index(self):
        shapes = [ShapeFactory.create_triangle(3, 4.5, 4, 5), ShapeFactory.create_circle(3), ShapeFactory.create_circle(2), ShapeFactory.create_square(3)]
        drawing_program = DrawingProgram(shapes)
        drawing_program.set_shape(ShapeFactory.create_triangle(1, 1.5, 2, 3), 1)
        self.assertEqual('Triangle', shapes[1].name())

    # Test set_shape method with negative index
    def test_set_shape_negative_index(self):
        drawing_program = DrawingProgram()
        try:
            shapes = [ShapeFactory.create_triangle(3, 4.5, 4, 5)]
            drawing_program.set_shape(shapes[0], -1)
            self.assertEqual(True, False, "should not have got here, set_shape took a negative index")
        except ValueError as value_error:
            self.assertEqual(True, True)

    # Test get_shape method with valid index
    def test_get_shape_valid_index(self):
        drawing_program = DrawingProgram()
        try:
            drawing_program.add_shape(ShapeFactory.create_triangle(3, 4.5, 4, 5))
        except ValueError as value_error:
            self.assertEqual(True, True)

    # Test get_shape method with negative index
    def test_get_shape_negative_index(self):
        shapes = [ShapeFactory.create_triangle(3, 4.5, 4, 5), ShapeFactory.create_circle(3)]
        drawing_program = DrawingProgram(shapes)
        try:
            index = drawing_program.get_shape(-1)
            self.assertEqual(True, False, "should not have got here, set_shape took a negative index")
        except ValueError as value_error:
            self.assertEqual(True, True)

    # Test get_shape method with index too large
    def test_get_shape_index_too_large(self):
        drawing_program = DrawingProgram()
        try:
            index = drawing_program.get_shape(5)
            self.assertEqual(True, False, "should not have got here, get_shape took an index beyond size -- no shapes")
        except ValueError as value_error:
            self.assertEqual(True, True)

    # Test add_shape method with one shape
    def test_add_shape_one_shape(self):
        drawing_program = DrawingProgram()
        drawing_program.add_shape(ShapeFactory.create_triangle(3, 4.5, 4, 5))
        self.assertEqual('Triangle', drawing_program.get_shape(0).name())

    # Test add_shape method with four shapes
    def test_add_shape_four_shape(self):
        shapes = [ShapeFactory.create_triangle(3, 4.5, 4, 5),
                  ShapeFactory.create_circle(3),
                  ShapeFactory.create_rectangle(2, 3),
                  ShapeFactory.create_square(3)]
        drawing_program = DrawingProgram()
        count = 0
        for shape in shapes:
            drawing_program.add_shape(shape)
            count += 1
        self.assertEqual(4, count, "4 shapes not added properly ")

    # Test remove_shape method
    def test_remove_no_shape(self):
        try:
            drawing_program = DrawingProgram()
            drawing_program.remove_shape("Circle")
        except ValueError as value_error:
            self.assertEqual(True, True)

    # Test remove_shape method with remove all
    def test_remove_shape_all_shape(self):
        shapes = [ShapeFactory.create_triangle(3, 4.5, 4, 5),
                  ShapeFactory.create_circle(3),
                  ShapeFactory.create_rectangle(2, 3),
                  ShapeFactory.create_square(3)]
        drawing_program = DrawingProgram(shapes)
        try:
            count = drawing_program.remove_shape('Circle')
        except ValueError as value_error:
            self.assertEqual(True, True)

    # Test remove_shape method with one shape
    def test_remove_shape_one_shape(self):
        shapes = [ShapeFactory.create_triangle(3, 4.5, 4, 5),
                  ShapeFactory.create_circle(3),
                  ShapeFactory.create_rectangle(2, 3),
                  ShapeFactory.create_square(3)]
        drawing_program = DrawingProgram(shapes)
        try:
            drawing_program.remove_shape('Circle')
            drawing_program.print_shape('Circle')
        except ValueError as value_error:
            self.assertEqual(True, True)

    # Test print_shape method with no shape
    def test_print_no_shape(self):
        drawing_program = DrawingProgram()
        try:
            drawing_program.print_shape("")
        except ValueError as value_error:
            self.assertEqual(True, True)

    # Test print_shape method with selected shape
    def test_print_shape_selected_shape(self):
        drawing_program = DrawingProgram()
        try:
            drawing_program.print_shape("Triangle")
        except ValueError as value_error:
            self.assertEqual(True, True)

    # Test print_shape method with all shapes
    def test_print_all_shape(self):
        shapes = [ShapeFactory.create_triangle(3, 4.5, 4, 5),
                  ShapeFactory.create_circle(3),
                  ShapeFactory.create_rectangle(2, 3),
                  ShapeFactory.create_square(3)]
        drawing_program = DrawingProgram(shapes)
        shape_name = ['Triangle', 'Circle', 'Rectangle', 'Square']
        try:
            for i in shape_name:
                drawing_program.print_shape(i)
        except ValueError as value_error:
            self.assertEqual(True, True)

    # Test sort_shape method with no shape
    def test_sort_no_shapes(self):
        drawing_program = DrawingProgram()
        drawing_program.sort_shapes()
        self.assertEqual("", drawing_program.__str__(), "should be empty string for drawing program")

    # Test sort_shape method with one shape
    def test_sort_one_shape(self):
        drawing_program = DrawingProgram()
        drawing_program.add_shape(ShapeFactory.create_square(3))
        try:
            drawing_program.sort_shapes()
        except ValueError as value_error:
            self.assertEqual(True, True)

    # Test sort_shape method with four shapes
    def test_sort_four_shapes_ascending(self):
        shapes = [ShapeFactory.create_triangle(3, 4.5, 4, 5),
                  ShapeFactory.create_circle(3),
                  ShapeFactory.create_rectangle(2, 3),
                  ShapeFactory.create_square(3)]
        drawing_program = DrawingProgram(shapes)
        sorted_shapes = ['Circle', 'Rectangle', 'Square', 'Triangle']
        try:
            drawing_program.sort_shapes()
            if drawing_program.get_shape(0).name() == sorted_shapes[0] \
               and drawing_program.get_shape(1).name() == sorted_shapes[1] \
               and drawing_program.get_shape(2).name() == sorted_shapes[2] \
               and drawing_program.get_shape(3).name() == sorted_shapes[3]:

                print("Shapes are sorted correctly")
        except ValueError as value_error:
            self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
