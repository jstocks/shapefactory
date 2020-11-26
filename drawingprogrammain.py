from drawingprogram import DrawingProgram
from shapefactory import ShapeFactory
from shape import Shape


#Create a DrawingProgram?
dp = DrawingProgram()

# Create shapes & add to list
# creating one shape of each kind
print("------------ Add Shape ---------------")
dp.add_shape(ShapeFactory.create_triangle(2, 3, 4, 5))
dp.add_shape(ShapeFactory.create_square(2))
dp.add_shape(ShapeFactory.create_rectangle(5, 4))
dp.add_shape(ShapeFactory.create_circle(4))
print(dp)

# Sort shapes
# Sorting the shapes in the list by alphabetical and then area
print("------------ Sort Shape ---------------")
dp.sort_shapes()
print(dp)

# Add more shapes to list
# adding additional shapes to the list
print("------------ Add more shape ---------------")
dp.add_shape(ShapeFactory.create_triangle(3, 5, 7, 9))
dp.add_shape(ShapeFactory.create_square(4))
dp.add_shape(ShapeFactory.create_rectangle(3,7))
dp.add_shape(ShapeFactory.create_circle(3))
print(dp)

# Sort shapes
# sorting the shapes in the list by alphabetical and then area
print("------------ Sort Shape ---------------")
dp.sort_shapes()
print(dp)

# Get the index of some shapes
# returns the string of the shape at specified index
print("------------ Get Shape ---------------")
print("Get shape at index 0: ", dp.get_shape(0))
print("Get shape at index 2: ", dp.get_shape(2))
print("Get shape at index 4: ", dp.get_shape(4))
print("Get shape at index 6: ", dp.get_shape(6))

# Replace some shapes
# calls an index and replaces that shape with a newly created shape
print("------------ Set/Replace Shape ---------------")
dp.set_shape((ShapeFactory.create_circle(1)), 5)
print("Replace shape at index 5 from Square to Circle")
print(dp)

# Print shape
# print shape in the drawing program
print("------------ Print Shape ---------------")
print("Print all 'Triangle' in drawing program")
dp.print_shape('Triangle')

# Remove shape
# removes ALL shapes that match the one passed as a parameter
print("------------ Remove Shape ---------------")
dp.remove_shape('Circle')
print(dp)

# Iterator
# print all shape in the drawing program
print("------------ Iterator ---------------")
for shape in dp:
    print(shape)

# Draw shape
# draw shapes in the drawing program
print("------------ Draw Shape ---------------")
print("Use draw() method to draw 3 Shapes")
print(Shape.draw(ShapeFactory.create_triangle(3, 5, 7, 9)))
print(Shape.draw(ShapeFactory.create_square(4)))
print(Shape.draw(ShapeFactory.create_rectangle(3, 7)))
print(Shape.draw(ShapeFactory.create_circle(3)))
