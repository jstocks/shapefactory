from drawingprogram import DrawingProgram
from shapefactory import ShapeFactory


#Create a DrawingProgram?
dp = DrawingProgram()

#Create shapes & add to list
"""creating one shape of each kind"""
dp.add_shape(ShapeFactory.create_triangle(2, 3, 4, 5))
dp.add_shape(ShapeFactory.create_square(2))
dp.add_shape(ShapeFactory.create_rectangle(5, 4))
dp.add_shape(ShapeFactory.create_circle(4))
print(dp)
#
# #Sort shapes
# """sorting the shapes in the list by alphabetical and then area"""
# dp.sort_shapes()
# print(dp)
#
# #Add more shapes to list
# """adding additional shapes to the list"""
# dp.add_shape(ShapeFactory.create_triangle(3, 5, 7, 9))
# dp.add_shape(ShapeFactory.create_square(4))
# dp.add_shape(ShapeFactory.create_rectangle(3,7))
# dp.add_shape(ShapeFactory.create_circle(3))
# print(dp)
#
# #Sort shapes
# """sorting the shapes in the list by alphabetical and then area"""
# dp.sort_shapes()
# print(dp)

#Get the index of some shapes
"""returns the string of the shape at specified index"""
# print(dp.get_shape(0))
# print(dp.get_shape(1))
# print(dp.get_shape(2))
# print(dp.get_shape(3))

#Replace some shapes
"""calls an index and replaces that shape with a newly created shape"""
# dp.set_shape((ShapeFactory.create_circle(1)), 0)
# print(dp)

# #Sort list again
# """sort the list again with updated shapes / locations"""
# dp.sort_shapes()
# print(dp)