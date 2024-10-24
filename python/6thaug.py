#1 Adding of two numbers:
def adding(func):
    def wraper(a,b):
        result=func(a,b)
        return result
    return wraper
@adding
def add_number(a,b):
    return a+b
a=int(input('Enter first number: '))
b=int(input('Enter second number: '))
print(add_number(a,b))
#2 printing hello thrice:
def hello_thrice(func):
    def wrapper():
        ans = func() * 3
        return ans
    return wrapper

@hello_thrice
def printing_hi():
    return 'hi'

print(printing_hi())
#3 Factorial
import math

def factorial_decorator(func):
    def wrapper(n):
        result = func(n)
        return math.factorial(result)
    return wrapper

@factorial_decorator
def get_number(n):
    return n


number = int(input('Enter a number: '))
print(get_number(number))


 
    