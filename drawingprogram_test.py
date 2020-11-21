import unittest
from drawingprogram import DrawingProgram


class MyDrawingProgramTest(unittest.TestCase):
    def test_init(self):
        drawing_program = DrawingProgram()
        self.assertEqual("", drawing_program.__str__(), "DrawingProgram should be empty but it not")

    def test_set_shape_valid_index(self):
        shapes = ["circle"]
        drawing_program = DrawingProgram()
        drawing_program.add_shape(shapes)
        drawing_program.set_shape(shapes[0], 0)
        self.assertEqual("circle\n", drawing_program.__str__())

    def test_set_shape_negative_index(self):
        drawing_program = DrawingProgram()
        try:
            shapes = ["circle"]
            drawing_program.set_shape(shapes[0], -1)
            self.assertEqual(True, False, "should not have got here, set_shape took a negative index")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_get_shape_valid_index(self):
        shapes = ["circle"]
        drawing_program = DrawingProgram()
        drawing_program.add_shape(shapes)
        shape = drawing_program.get_shape(0)
        self.assertEqual("circle\n", shape.__str__(), "correct shape not return")

    def test_get_shape_negative_index(self):
        shapes = ["circle"]
        drawing_program = DrawingProgram()
        drawing_program.add_shape(shapes)
        try:
            index = drawing_program.get_shape(-1)
            self.assertEqual(True, False, "should not have got here, get_shape took a negative index")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_get_shape_index_too_large(self):
        drawing_program = DrawingProgram()
        try:
            index = drawing_program.get_shape(0)
            self.assertEqual(True, False, "should not have got here, get_shape took an index beyond size -- no shapes")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_add_shape_one_shape(self):
        shapes = ["circle"]
        drawing_program = DrawingProgram()
        drawing_program.add_shape(shapes)
        self.assertEqual("circle\n", drawing_program.__str__(), "one shape not added to shapes properly")

    def test_add_shape_four_shape(self):
        shapes = ["circle", "square", "rectangle", "triangle"]
        drawing_program = DrawingProgram()
        drawing_program.add_shape(shapes)
        self.assertEqual("circle\nsquare\nrectangle\ntriangle", shapes.__str__(),"4 shapes not added properly ")

    def test_remove_no_shape(self):
        print("not done")

    def test_remove_shape_four_shape(self):
        print("not done")

    def test_remove_shape_one_shape(self):
        print("not done")

    def test_print_no_shape(self):
        print("print one")

    def test_print_shape_one_shape(self):
        print("print one")

    def test_print_shape_four_shape(self):
        print("print four")

    def test_sort_no_shapes(self):
        drawing_program = DrawingProgram()
        drawing_program.sort_shapes()
        self.assertEqual("", drawing_program.__str__(), "should be empty string for drawing program")

    def test_sort_one_shape(self):
        drawing_program = DrawingProgram()
        shapes = ["circle"]
        drawing_program.add_shape(shapes)
        drawing_program.sort_shapes()
        self.assertEqual("circle\n", drawing_program.__str__(),  "should be one shape: circle")

    def test_sort_four_shapes_ascending(self):
        drawing_program = DrawingProgram()
        shapes = ["circle", "square", "rectangle", "triangle"]
        drawing_program.sort_shapes()
        self.assertEqual("circle", "square", "rectangle", "triangle")

if __name__ == '__main__':
    unittest.main()
