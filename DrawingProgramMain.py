from drawingprogram import DrawingProgram
from shapefactory import ShapeFactory


#Create a DrawingProgram?
shape_list = []

#Create shapes & add to list
"""creating one shape of each kind"""
tri1 = ShapeFactory.create_triangle(2, 3, 4, 5)
sq1 = ShapeFactory.create_square(2)
rect1 = ShapeFactory.create_rectangle(5, 4)
circ1 = ShapeFactory.create_circle(4)

#Add shapes to list
"""adding shapes from above to the list"""
shape_list.append(str(tri1))
shape_list.append(str(sq1))
shape_list.append(str(rect1))
shape_list.append(str(circ1))
print(shape_list)

#Sort shapes
"""sorting the shapes in the list by alphabetical and then area"""
DrawingProgram.sort_shape(shape_list)
print(shape_list)

#Add more shapes to list
"""adding additional shapes to the list"""
tri2 = ShapeFactory.create_triangle(3, 5, 7, 9)
sq2 = ShapeFactory.create_square(4)
rect2 = ShapeFactory.create_rectangle(3,7)
circ2 = ShapeFactory.create_circle(3)
shape_list.append(str(tri2))
shape_list.append(str(sq2))
shape_list.append(str(rect2))
shape_list.append(str(circ2))
print(shape_list)

#Get the index of some shapes
"""returns the string of the shape at specified index"""
DrawingProgram.get_shape(0)
DrawingProgram.get_shape(2)
DrawingProgram.get_shape(4)
DrawingProgram.get_shape(6)

#Replace some shapes
"""calls an index and replaces that shape with a newly created shape"""
DrawingProgram.set_shape((ShapeFactory.create_circle(1)), 6)
print(shape_list)

#Sort list again
"""sort the list again with updated shapes / locations"""
DrawingProgram.sort_shape(shape_list)
print(shape_list)