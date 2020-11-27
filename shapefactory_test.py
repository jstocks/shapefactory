"""
Test methods in the shapefactory class. By testing shapefactory, the shape, circle, rectangle, square, and triangle
classes and methods that belong to those classes are all tested as well.
"""

import unittest
from shapefactory import ShapeFactory
from math import pi


class ShapeFactoryTest(unittest.TestCase):
    """
    Tests all four shapes; Circle, Rectangle, Square, and Triangle.
    Tests that shapes can be created with: ints and floats as parameters and return proper area and perimeter
    Tests that getter name property allows retrieval of proper name; circle:"Circle", rectangle:"Rectangle",
    square:"Square", triangle:"Triangle"
    Tests that shapes cannot be created with: no input, strings, negative numbers, missing parameters
    Tests the __lt__, __eq__, and __gt__ methods can all be used to compare shapes (area and perimeter), and raise
    proper errors when invalid parameters are passed
    """

    def test_circle_init(self):
        # Test circle can be created with radius >= 0
        circle_to_test = ShapeFactory.create_circle(0)
        self.assertEqual(circle_to_test.area(), 0, "Area should be 0")
        self.assertEqual(circle_to_test.perimeter(), 0, "Perimeter should be 0")
        # Create circle with radius 1
        circle_to_test = ShapeFactory.create_circle(1)
        self.assertEqual(circle_to_test.area(), pi, "Area should be 3.1415926")
        self.assertEqual(circle_to_test.perimeter(), 6.283185307179586, "Perimeter should be 6.283185307179586")
        # Create circle with radius 2.5
        circle_to_test = ShapeFactory.create_circle(2.5)
        self.assertEqual(circle_to_test.perimeter(), 15.707963267948966, "Area should be 15.707963267948966")

    def test_create_circle_with_negative_int_radius(self):
        # Test inputting a negative int as the radius raises a ValueError
        self.assertRaises(ValueError, ShapeFactory.create_circle, -1)

    def test_create_circle_with_negative_float_radius(self):
        # Test inputting a negative float as the radius raises a ValueError
        self.assertRaises(ValueError, ShapeFactory.create_circle, -3.7)

    def test_create_circle_radius_string_type(self):
        # Test inputting with string value so the radius raises a TypeError
        self.assertRaises(TypeError, ShapeFactory.create_circle, "i")
        self.assertRaises(TypeError, ShapeFactory.create_circle, "\n")

    def test_create_circle_missing_parameter(self):
        # Tests that a circle cannot be created with no parameter
        try:
            ShapeFactory.create_circle()
            self.assertEqual(True, False, "should not have got here, created circle with no radius parameter")
        except TypeError as type_error:
            self.assertEqual(True, True)

    def test_circle_object_name(self):
        # Test AssertionError is thrown when the name of a circle object is not "Circle"
        circle_to_test_2 = ShapeFactory.create_circle(0)
        try:
            self.assertEqual(circle_to_test_2.name(), "notCircle")
        except AssertionError:
            self.assertRaises(AssertionError)
        # Test name of the circle object is "Circle"
        self.assertEqual(circle_to_test_2.name(), "Circle", "Somehow managed to create circle object with name \n"
                                                            "not 'Circle'")

    def test_rectangle_init(self):
        # Test circle can be created with radius >= 0
        rectangle_to_test = ShapeFactory.create_rectangle(0, 0)
        self.assertEqual(rectangle_to_test.area(), 0, "Area of rectangle is not 0")
        self.assertEqual(rectangle_to_test.perimeter(), 0, "Perimeter of rectangle in not 0")
        # Create rectangle with width 1 and length 2
        rectangle_to_test = ShapeFactory.create_rectangle(1, 2)
        self.assertEqual(rectangle_to_test.area(), 2, "Area of rectangle in not 2")
        self.assertEqual(rectangle_to_test.perimeter(), 6, "Perimeter of rectangle in not 6")
        # Create rectangle with radius width of type float
        rectangle_to_test = ShapeFactory.create_rectangle(2.5, 1.5)
        self.assertEqual(rectangle_to_test.perimeter(), 8, "Perimeter of rectangle is not 8")
        self.assertEqual(rectangle_to_test.area(), 3.75, "Area of rectangle is not 3.75")

    def test_create_rectangle_with_negative_int_length_and_width(self):
        # Test inputting a negative int as the length and width raises a ValueError
        self.assertRaises(ValueError, ShapeFactory.create_rectangle, -1, 1)
        self.assertRaises(ValueError, ShapeFactory.create_rectangle, 1, -1)
        self.assertRaises(ValueError, ShapeFactory.create_rectangle, -1, -1)

    def test_create_rectangle_with_negative_float_length_and_width(self):
        # Test inputting a negative float as the length and width raises a ValueError
        self.assertRaises(ValueError, ShapeFactory.create_rectangle, -1.0, 1)
        self.assertRaises(ValueError, ShapeFactory.create_rectangle, 1, -1.0)
        self.assertRaises(ValueError, ShapeFactory.create_rectangle, -1.0, -1.0)

    def test_rectangle_length_and_width_string_type(self):
        # Test inputting with string value so the radius raises a TypeError
        self.assertRaises(ValueError, ShapeFactory.create_rectangle, "i", 1)
        self.assertRaises(ValueError, ShapeFactory.create_rectangle, 1, "\n")
        self.assertRaises(ValueError, ShapeFactory.create_rectangle, "", 1)
        # Tests that a circle cannot be created with no parameter
        try:
            ShapeFactory.create_rectangle()
            self.assertEqual(True, False, "should not have got here, created rectangle with no length or width")
        except TypeError as type_error:
            self.assertEqual(True, True)

    def test_create_rectangle_missing_parameter(self):
        # Test attempting to create a rectangle without enough parameters
        try:
            ShapeFactory.create_rectangle(1)
            self.assertEqual(True, False, "should not have got here, created rectangle with missing length parameter")
        except TypeError as type_error:
            self.assertEqual(True, True)

    def test_rectangle_object_name(self):
        # Test AssertionError is thrown when the name of a rectangle object is not "Rectangle"
        rectangle_to_test_2 = ShapeFactory.create_rectangle(1, 1)
        try:
            self.assertEqual(rectangle_to_test_2.name(), "notRectangle")
        except AssertionError:
            self.assertRaises(AssertionError)
        # Test name of the rectangle object is "Rectangle"
        self.assertEqual(rectangle_to_test_2.name(), "Rectangle", "Somehow managed to create circle object with name\n "
                                                                  "not 'Rectangle'")

    def test_square_init(self):
        # Test square can be created with length >= 0
        square_to_test = ShapeFactory.create_square(0)
        self.assertEqual(square_to_test.area(), 0, "Area should be 0")
        self.assertEqual(square_to_test.perimeter(), 0, "Perimeter should be 0")
        # Create circle with radius 1
        square_to_test = ShapeFactory.create_square(1)
        self.assertEqual(square_to_test.area(), 1, "Area should be 1")
        self.assertEqual(square_to_test.perimeter(), 4, "Perimeter should be 4")
        # Create square with slide length 2.5
        square_to_test = ShapeFactory.create_square(2.5)
        self.assertEqual(square_to_test.perimeter(), 10, "Area should be 10")

    def test__create_square_with_negative_int_length(self):
        # Test inputting a negative int as the radius raises a ValueError
        self.assertRaises(ValueError, ShapeFactory.create_square, -1)

    def test__create_square_with_negative_float_length(self):
        # Test inputting a negative float as the radius raises a ValueError
        self.assertRaises(ValueError, ShapeFactory.create_square, -3.7)

    def test_square_length_string_type(self):
        # Test inputting with string value so the length raises a TypeError
        self.assertRaises(ValueError, ShapeFactory.create_square, "i")
        self.assertRaises(ValueError, ShapeFactory.create_square, "\n")
        # Tests that a square cannot be created with no parameter
        try:
            ShapeFactory.create_square()
            self.assertEqual(True, False, "should not have got here, created square with no length parameter")
        except TypeError as type_error:
            self.assertEqual(True, True)

    def test_square_object_name(self):
        # Test AssertionError is thrown when the name of a square object is not "Square"
        square_to_test_2 = ShapeFactory.create_square(0)
        try:
            self.assertEqual(square_to_test_2.name(), "notSquare")
        except AssertionError:
            self.assertRaises(AssertionError)
        # Test name of the square object is "Square"
        self.assertEqual(square_to_test_2.name(), "Square", "Somehow managed to create square object with name \n"
                                                            "not 'Square'")

    def test_triangle_init(self):
        # Test triangle can be created with lengths, height, and base >= 0
        triangle_to_test = ShapeFactory.create_triangle(0, 0, 0, 0)
        self.assertEqual(triangle_to_test.area(), 0, "Area should be 0")
        self.assertEqual(triangle_to_test.perimeter(), 0, "Perimeter should be 0")
        # Create triangle with lengths of 1
        triangle_to_test = ShapeFactory.create_triangle(1, 1, 1, 1)
        self.assertEqual(triangle_to_test.area(), .5, "Area should be .5")
        self.assertEqual(triangle_to_test.perimeter(), 3, "Perimeter should be 3")
        # Create triangle with lengths 2.5
        circle_to_test = ShapeFactory.create_triangle(2.5, 2.6, 2.7, 2.7)
        self.assertEqual(circle_to_test.perimeter(), 7.9, "Area should be 7.9")

    def test_create_triangle_with_negative_int_length(self):
        # Test inputting a negative int as the length raises a ValueError
        self.assertRaises(ValueError, ShapeFactory.create_triangle, -1, 1, 1, 1)
        self.assertRaises(ValueError, ShapeFactory.create_triangle, 1, -1, 1, 1)
        self.assertRaises(ValueError, ShapeFactory.create_triangle, 1, 1, -1, 1)
        self.assertRaises(ValueError, ShapeFactory.create_triangle, 1, 1, 1, -1)

    def test_create_triangle_with_negative_float_length(self):
        # Test inputting a negative float as the length raises a ValueError
        self.assertRaises(ValueError, ShapeFactory.create_triangle, -1.0, 1, 1, 1)
        self.assertRaises(ValueError, ShapeFactory.create_triangle, 1, -1.0, 1, 1)
        self.assertRaises(ValueError, ShapeFactory.create_triangle, 1, 1, -1.0, 1)
        self.assertRaises(ValueError, ShapeFactory.create_triangle, 1, 1, 1, -1.0)

    def test_triangle_length_string_type(self):
        # Test inputting with string value so the length raises a TypeError
        self.assertRaises(TypeError, ShapeFactory.create_triangle, "i")
        self.assertRaises(TypeError, ShapeFactory.create_triangle, "\n")

    def test_create_triangle_missing_all_parameters(self):
        # Tests that a triangle cannot be created with no parameters
        try:
            ShapeFactory.create_triangle()
            self.assertEqual(True, False, "should not have got here, created triangle with no length parameters")
        except TypeError as type_error:
            self.assertEqual(True, True)

    def test_create_triangle_missing_3_parameters(self):
        # Test attempting to create a triangle with three missing parameters
        try:
            ShapeFactory.create_triangle(1)
            self.assertEqual(True, False, "should not have got here, created triangle with missing length parameters")
        except TypeError as type_error:
            self.assertEqual(True, True)

    def test_create_triangle_missing_2_parameters(self):
        # Test attempting to create a triangle with two missing parameters
        try:
            ShapeFactory.create_triangle(1, 2)
            self.assertEqual(True, False, "should not have got here, created triangle with missing length parameters")
        except TypeError as type_error:
            self.assertEqual(True, True)

    def test_create_triangle_missing_1_parameter(self):
        # Test attempting to create a triangle with one missing parameter
        try:
            ShapeFactory.create_triangle(1, 2, 3)
            self.assertEqual(True, False, "should not have got here, created triangle with missing length parameters")
        except TypeError as type_error:
            self.assertEqual(True, True)

    def test_triangle_object_name(self):
        # Test AssertionError is thrown when the name of a triangle object is not "Triangle"
        triangle_to_test = ShapeFactory.create_triangle(1, 1, 1, 1)
        try:
            self.assertEqual(triangle_to_test.name(), "notTriangle")
        except AssertionError:
            self.assertRaises(AssertionError)
        # Test name of the rectangle object is "Rectangle"
        self.assertEqual(triangle_to_test.name(), "Triangle", "Somehow managed to create triangle object with name\n "
                                                              "not 'Triangle'")

    def test_circle_str(self):
        # Test shape can be created and returns proper formatting as string
        # Create Circle and print string
        circle_to_test = ShapeFactory.create_circle(1)
        self.assertEqual("(Circle, 3.141593, 6.283185)", circle_to_test.__str__(),
                         "circle_to_test should be (Circle, 3.141593, 6.283185) but it not")

    def test_rectangle_str(self):
        # Test shape can be created and returns proper formatting as string
        # Create Rectangle and print string
        rectangle_to_test = ShapeFactory.create_rectangle(1, 2)
        self.assertEqual("(Rectangle, 2.000000, 6.000000)", rectangle_to_test.__str__(),
                         "rectangle_to_test should be (Rectangle, 2.000000, 6.000000) but it not")

    def test_square_str(self):
        # Test shape can be created and returns proper formatting as string
        # Create Square and print string
        square_to_test = ShapeFactory.create_square(1)
        self.assertEqual("(Square, 1.000000, 4.000000)", square_to_test.__str__(),
                         "square_to_test should be (Square, 1.000000, 4.000000)empty but it not")

    def test_triangle_str(self):
        # Test shape can be created and returns proper formatting as string
        # Create Triangle and print string
        triangle_to_test = ShapeFactory.create_triangle(1, 2, 1, 2)
        self.assertEqual("(Triangle, 1.000000, 4.000000)", triangle_to_test.__str__(),
                         "triangle_to_test should be (Triangle, 2.000000, 6.000000) but it not")

    def test_circle_draw(self):
        # Test shape can be "drawn" and returns proper formatting as string output
        # Create Circle and return string
        circle_to_test = ShapeFactory.create_circle(1)
        self.assertEqual("Circle, area: 3.141593, perimeter: 6.283185", circle_to_test.draw(),
                         "circle_to_test.draw() should return 'Circle, area: 3.141593, perimeter: 6.283185' "
                         "but it is not")

    def test_rectangle_draw(self):
        # Test shape can be "drawn" and returns proper formatting as string output
        # Create Rectangle and return string
        rectangle_to_test = ShapeFactory.create_rectangle(1, 3)
        self.assertEqual("Rectangle, area: 3.000000, perimeter: 8.000000", rectangle_to_test.draw(),
                         "rectangle_to_test.draw() should return 'Rectangle, area: 3.000000, perimeter: 8.000000' "
                         "but it is not")

    def test_square_draw(self):
        # Test shape can be "drawn" and returns proper formatting as string output
        # Create Square and return string
        square_to_test = ShapeFactory.create_square(2)
        self.assertEqual("Square, area: 4.000000, perimeter: 8.000000", square_to_test.draw(),
                         "square_to_test.draw() should return 'Square, area: 4.000000, perimeter: 8.000000' "
                         "but it is not")

    def test_triangle_draw(self):
        # Test shape can be "drawn" and returns proper formatting as string output
        # Create Triangle and return string
        triangle_to_test = ShapeFactory.create_triangle(2, 4, 2, 5)
        self.assertEqual("Triangle, area: 4.000000, perimeter: 9.000000", triangle_to_test.draw(),
                         "triangle_to_test.draw() should return 'Triangle, area: 4.000000, perimeter: 8.000000' "
                         "but it is not")

    def test_eq_circles_equal(self):
        # Test equal method on two shapes with same value
        # Test Circles
        circle1 = ShapeFactory.create_circle(.5)
        circle2 = ShapeFactory.create_circle(0.5000)
        self.assertEqual(circle1, circle2, "circles are not equal but they should be")

    def test_eq_rectangles_equal(self):
        # Test equal method on two shapes with same value
        # Test Rectangles
        rectangle1 = ShapeFactory.create_rectangle(.5, 1)
        rectangle2 = ShapeFactory.create_rectangle(0.5000, 1.0)
        self.assertEqual(rectangle1, rectangle2, "rectangles are not equal but they should be")

    def test_eq_squares_equal(self):
        # Test equal method on two shapes with same value
        # Test Squares
        square1 = ShapeFactory.create_square(.3)
        square2 = ShapeFactory.create_square(0.3000)
        self.assertEqual(square1, square2, "squares are not equal but they should be")

    def test_eq_triangles_equal(self):
        # Test equal method on two shapes with same value
        # Test Triangles
        triangle1 = ShapeFactory.create_triangle(.5, 1, 2, 3)
        triangle2 = ShapeFactory.create_triangle(0.5000, 1, 2.0, 3.00000)
        self.assertEqual(triangle1, triangle2, "triangles are not equal but they should be")

    def test_eq_circles_not_equal(self):
        # Test equal method on two shapes that are not equal
        # Test Circles
        circle1 = ShapeFactory.create_circle(1)
        circle2 = ShapeFactory.create_circle(0.5000)
        self.assertNotEqual(circle1, circle2, "circles are equal but they should not be")

    def test_eq_rectangles_not_equal(self):
        # Test equal method on two shapes that are not equal
        # Test Rectangles
        rectangle1 = ShapeFactory.create_rectangle(.4, 1)
        rectangle2 = ShapeFactory.create_rectangle(0.5000, 17.0)
        self.assertNotEqual(rectangle1, rectangle2, "rectangles are equal but they should not be")

    def test_eq_squares_not_equal(self):
        # Test equal method on two shapes that are not equal
        # Test Squares
        square1 = ShapeFactory.create_square(.8)
        square2 = ShapeFactory.create_square(8)
        self.assertNotEqual(square1, square2, "squares are equal but they should not be")

    def test_eq_triangles_not_equal(self):
        # Test equal method on two shapes that are not equal
        # Test Triangles
        triangle1 = ShapeFactory.create_triangle(6, 1.000, 2, 3)
        triangle2 = ShapeFactory.create_triangle(0.5000, 1, 2.0, 3.00000)
        self.assertNotEqual(triangle1, triangle2, "triangles are equal but they should not be")

    def test_eq_circle_wrong_type(self):
        """Test eq with something other than a Shape which should raise a TypeError"""
        # Test circle with radius 1
        circle = ShapeFactory.create_circle(1)
        try:
            if circle == 37:
                self.assertEqual(True, False, "somehow got past circle == 37")
        except TypeError as type_error:
            self.assertEqual(True, True)

    def test_eq_rectangle_wrong_type(self):
        """Test eq with something other than a Shape which should raise a TypeError"""
        # Test rectangle with lengths 1, 5
        rectangle = ShapeFactory.create_rectangle(1, 5)
        try:
            if rectangle == 38:
                self.assertEqual(True, False, "somehow got past rectangle == 38")
        except TypeError as type_error:
            self.assertEqual(True, True)

    def test_eq_square_wrong_type(self):
        """Test eq with something other than a Shape which should raise a TypeError"""
        # Test square with length = 5
        square = ShapeFactory.create_square(5)
        try:
            if square == 39:
                self.assertEqual(True, False, "somehow got past square == 39")
        except TypeError as type_error:
            self.assertEqual(True, True)

    def test_eq_triangle_wrong_type(self):
        """Test eq with something other than a Shape which should raise a TypeError"""
        # Test triangle with lengths 10
        triangle = ShapeFactory.create_triangle(10, 10, 10, 10)
        try:
            if triangle == 40:
                self.assertEqual(True, False, "somehow got past triangle == 40")
        except TypeError as type_error:
            self.assertEqual(True, True)

    def test_lt_first_less_than_second_circle_area(self):
        """Basic test of lt (the < operator) where Shape1 area is less than Shape2 area"""
        # Test circle area
        circle1 = ShapeFactory.create_circle(0.5)
        circle2 = ShapeFactory.create_circle(1)
        self.assertLess(circle1.area(), circle2.area(), "0.7853981633974483 should be "
                                                        "less than 3.141592653589793")

    def test_lt_first_less_than_second_rectangle_area(self):
        """Basic test of lt (the < operator) where Shape1 area is less than Shape2 area"""
        # Test rectangle area
        rectangle1 = ShapeFactory.create_rectangle(0.5, 1)
        rectangle2 = ShapeFactory.create_rectangle(1, 1)
        self.assertLess(rectangle1.area(), rectangle2.area(), "0.5 should be less than 1.0")

    def test_lt_first_less_than_second_square_area(self):
        """Basic test of lt (the < operator) where Shape1 area is less than Shape2 area"""
        # Test square area
        square1 = ShapeFactory.create_square(0.5)
        square2 = ShapeFactory.create_square(1)
        self.assertLess(square1.area(), square2.area(), "0.25 should be less than 1.0")

    def test_lt_first_less_than_second_triangle_area(self):
        """Basic test of lt (the < operator) where Shape1 area is less than Shape2 area"""
        # Test triangle area
        triangle1 = ShapeFactory.create_triangle(0.5, 1, 1, 1)
        triangle2 = ShapeFactory.create_triangle(1, 1, 1, 1)
        self.assertLess(triangle1.area(), triangle2.area(), "0.25 should be less than .5")

    def test_lt_first_less_than_second_circle_perimeter(self):
        """Basic test of lt (the < operator) where Shape1 perimeter is less than Shape2 perimeter"""
        # Test circle perimeter
        circle1 = ShapeFactory.create_circle(0.5)
        circle2 = ShapeFactory.create_circle(1)
        self.assertLess(circle1.perimeter(), circle2.perimeter(), "3.141592653589793 should be "
                                                                  "less than 6.283185307179586")

    def test_lt_first_less_than_second_rectangle_perimeter(self):
        """Basic test of lt (the < operator) where Shape1 perimeter is less than Shape2 perimeter"""
        # Test rectangle perimeter
        rectangle1 = ShapeFactory.create_rectangle(0.5, 1)
        rectangle2 = ShapeFactory.create_rectangle(1, 1)
        self.assertLess(rectangle1.perimeter(), rectangle2.perimeter(), "3.0 should be less than 4.0")

    def test_lt_first_less_than_second_square_perimeter(self):
        """Basic test of lt (the < operator) where Shape1 perimeter is less than Shape2 perimeter"""
        # Test square perimeter
        square1 = ShapeFactory.create_square(0.5)
        square2 = ShapeFactory.create_square(1)
        self.assertLess(square1.perimeter(), square2.perimeter(), "2.0 should be less than 4.0")

    def test_lt_first_less_than_second_triangle_perimeter(self):
        """Basic test of lt (the < operator) where Shape1 perimeter is less than Shape2 perimeter"""
        # Test triangle perimeter
        triangle1 = ShapeFactory.create_triangle(0.5, 1, 1, 1)
        triangle2 = ShapeFactory.create_triangle(1, 1, 1, 1)
        self.assertLess(triangle1.perimeter(), triangle2.perimeter(), "2.5 should be less than 3.0")

    def test_lt_first_same_second_circle(self):
        """Test where shapes are same so < should return a False"""
        # Test circle
        circle1 = ShapeFactory.create_circle(10)
        circle2 = ShapeFactory.create_circle(10)
        self.assertEqual(False, circle1 < circle2, "Circles are the same, somehow returned circle1 < circle2")

    def test_lt_first_same_second_rectangle(self):
        """Test where shapes are same so < should return a False"""
        # Test rectangle
        rectangle1 = ShapeFactory.create_rectangle(10, 10)
        rectangle2 = ShapeFactory.create_rectangle(10, 10)
        self.assertEqual(False, rectangle1 < rectangle2, "Rectangles are the same, somehow returned "
                                                         "rectangle1 < rectangle2")

    def test_lt_first_same_second_square(self):
        """Test where shapes are same so < should return a False"""
        # Test square
        square1 = ShapeFactory.create_square(10)
        square2 = ShapeFactory.create_square(10)
        self.assertEqual(False, square1 < square2, "Squares are the same, somehow returned square1 < square2")

    def test_lt_first_same_second_triangle(self):
        """Test where shapes are same so < should return a False"""
        # Test triangle
        triangle1 = ShapeFactory.create_triangle(10, 10, 10, 10)
        triangle2 = ShapeFactory.create_triangle(10, 10, 10, 10)
        self.assertEqual(False, triangle1 < triangle2, "Triangles are the same, somehow returned triangle1 < triangle2")

    def test_lt_wrong_type_circle(self):
        """Use something other than a Shape with <, which should raise a TypeError"""
        # Test with circle
        circle1 = ShapeFactory.create_circle(10)
        try:
            if circle1 < 37:
                self.assertEqual(True, False, "somehow got past circle1 < 37")
        except TypeError as type_error:
            self.assertEqual(True, True)

    def test_lt_wrong_type_rectangle(self):
        """Use something other than a Shape with <, which should raise a TypeError"""
        # Test with rectangle
        rectangle1 = ShapeFactory.create_rectangle(10, 11)
        try:
            if rectangle1 < 37:
                self.assertEqual(True, False, "somehow got past rectangle1 < 37")
        except TypeError as type_error:
            self.assertEqual(True, True)

    def test_lt_wrong_type_square(self):
        """Use something other than a Shape with <, which should raise a TypeError"""
        # Test with square
        square1 = ShapeFactory.create_square(12)
        try:
            if square1 < 37:
                self.assertEqual(True, False, "somehow got past square1 < 37")
        except TypeError as type_error:
            self.assertEqual(True, True)

    def test_lt_wrong_type_triangle(self):
        """Use something other than a Shape with <, which should raise a TypeError"""
        # Test with triangle
        triangle1 = ShapeFactory.create_triangle(10, 20, 30, 40)
        try:
            if triangle1 < 37:
                self.assertEqual(True, False, "somehow got past triangle1 < 37")
        except TypeError as type_error:
            self.assertEqual(True, True)







    def test_gt_first_greater_than_second_area(self):
        """Basic test of gt (the > operator) where Shape1 area is greater than Shape2 area"""
        # Test circle area
        circle1 = ShapeFactory.create_circle(1)
        circle2 = ShapeFactory.create_circle(.5)
        self.assertGreater(circle1.area(), circle2.area(), "3.141592653589793 should be "
                                                           "greater than 0.7853981633974483")
        # Test rectangle area
        rectangle1 = ShapeFactory.create_rectangle(1, 1)
        rectangle2 = ShapeFactory.create_rectangle(.5, 1)
        self.assertGreater(rectangle1.area(), rectangle2.area(), "1.0 should be greater than 0.5")
        # Test square area
        square1 = ShapeFactory.create_square(1)
        square2 = ShapeFactory.create_square(0.5)
        self.assertGreater(square1.area(), square2.area(), "1.0 should be greater than 0.25")
        # Test triangle area
        triangle1 = ShapeFactory.create_triangle(1, 1, 1, 1)
        triangle2 = ShapeFactory.create_triangle(0.5, 1, 1, 1)
        self.assertGreater(triangle1.area(), triangle2.area(), "0.5 should be greater than .25")

    def test_gt_first_greater_than_second_perimeter(self):
        """Basic test of gt (the > operator) where Shape1 perimeter is greater than Shape2 perimeter"""
        # Test circle perimeter
        circle1 = ShapeFactory.create_circle(1)
        circle2 = ShapeFactory.create_circle(0.5)
        self.assertGreater(circle1.perimeter(), circle2.perimeter(), "6.283185307179586 should be "
                                                                     "greater than 3.141592653589793")
        # Test rectangle perimeter
        rectangle1 = ShapeFactory.create_rectangle(1, 1)
        rectangle2 = ShapeFactory.create_rectangle(0.5, 1)
        self.assertGreater(rectangle1.perimeter(), rectangle2.perimeter(), "4.0 should be greater than 3.0")
        # Test square perimeter
        square1 = ShapeFactory.create_square(1)
        square2 = ShapeFactory.create_square(0.5)
        self.assertGreater(square1.perimeter(), square2.perimeter(), "4.0 should be less than 2.0")
        # Test triangle perimeter
        triangle1 = ShapeFactory.create_triangle(1, 1, 1, 1)
        triangle2 = ShapeFactory.create_triangle(0.5, 1, 1, 1)
        self.assertGreater(triangle1.perimeter(), triangle2.perimeter(), "3.0 should be greater than 2.5")

    def test_gt_first_same_second(self):
        """Test where shapes are same so > should return a False"""
        # Test circle
        circle1 = ShapeFactory.create_circle(10)
        circle2 = ShapeFactory.create_circle(10)
        self.assertEqual(False, circle1 > circle2, "Circles are the same, somehow returned circle1 > circle2")
        # Test rectangle
        rectangle1 = ShapeFactory.create_rectangle(10, 10)
        rectangle2 = ShapeFactory.create_rectangle(10, 10)
        self.assertEqual(False, rectangle1 > rectangle2, "Rectangles are the same, somehow returned "
                                                         "rectangle1 > rectangle2")
        # Test square
        square1 = ShapeFactory.create_square(10)
        square2 = ShapeFactory.create_square(10)
        self.assertEqual(False, square1 > square2, "Squares are the same, somehow returned square1 > square2")
        # Test triangle
        triangle1 = ShapeFactory.create_triangle(10, 10, 10, 10)
        triangle2 = ShapeFactory.create_triangle(10, 10, 10, 10)
        self.assertEqual(False, rectangle1 > rectangle2, "Triangles are the same, somehow returned "
                                                         "triangle1 > triangle2")

    def test_gt_wrong_type(self):
        """Use something other than a Shape with >, which should raise a TypeError"""
        # Test with circle
        circle1 = ShapeFactory.create_circle(10)
        try:
            if circle1 > 37:
                self.assertEqual(True, False, "somehow got past circle1 > 37")
        except TypeError as type_error:
            self.assertEqual(True, True)
        # Test with rectangle
        rectangle1 = ShapeFactory.create_rectangle(10, 11)
        try:
            if rectangle1 > 37:
                self.assertEqual(True, False, "somehow got past rectangle1 > 37")
        except TypeError as type_error:
            self.assertEqual(True, True)
        # Test with square
        square1 = ShapeFactory.create_square(12)
        try:
            if square1 > 37:
                self.assertEqual(True, False, "somehow got past square1 > 37")
        except TypeError as type_error:
            self.assertEqual(True, True)
        # Test with triangle
        triangle1 = ShapeFactory.create_triangle(10, 20, 30, 40)
        try:
            if triangle1 > 37:
                self.assertEqual(True, False, "somehow got past triangle1 > 37")
        except TypeError as type_error:
            self.assertEqual(True, True)

    """
    NOT SURE HOW TO TEST:
    @classmethod
    def __subclasshook__(cls, C):
        if cls is Shape:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True
        return NotImplemented
        """

if __name__ == '__main__':
    unittest.main()
