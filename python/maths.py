import calculator

x = int(input('Enter a number: '))
y = int(input('Enter another number: '))
operator = input('Enter the operation (+, -, *, /, %,^): ')

result = calculator.calculator(x, y, operator)
print("Result:", result)
