class MathOperations:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

math_op = MathOperations()
print(math_op.add(5, 10))     
"""Output: 15 (would use the first method in a
language that supports overloading"""

print(math_op.add(5, 10, 15)) 
# Output: 30 (would use the second method)
class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * (self.radius ** 2)

# Creating instances of the shapes
rectangle = Rectangle(5, 10)
circle = Circle(7)

# Using run-time polymorphism 
print(f"Rectangle Area: {rectangle.area()}")  # Output: Rectangle Area: 50
print(f"Circle Area: {circle.area()}")        # Output: Circle Area: 153.86






