#creating base class
class Operation:
    def calculate(self, a, b):
        pass
#drived classes
class Addition(Operation):
    def calculate(self, a, b):
        return a + b

class Subtraction(Operation):
    def calculate(self, a, b):
        return a - b

class Multiplication(Operation):
    def calculate(self, a, b):
        return a * b

#Define a function that uses polymorphism
def perform_operation(operation, a, b):
    return operation.calculate(a, b)

# Creating instances of different operations
add = Addition()
subtract = Subtraction()
multiply = Multiplication()

# Performing using the function
print(perform_operation(add, 10, 5))        # Output: 15 (Addition)
print(perform_operation(subtract, 10, 5))   # Output: 5  (Subtraction)
print(perform_operation(multiply, 10, 5))   # Output: 50 (Multiplication)
