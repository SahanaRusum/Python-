#1
class triangle:
    def __init__(self,height,a,b,c):
        self.b=b
        self.height=height
        self.a=a
        self.b=b
        self.c=c
    def area(self):
        return 0.5*(self.height)*(self.b)
    def perimeter(self):
        return self.a+self.b+self.c    
    
#here b is same as base of the triangle which is also the second side of the triangle  
b=float(input('Enter the base of the triangle: '))
height=float(input('Enter the height of the triangle: '))
a=float(input('Enter the side 1: '))
c=float(input('Enter the side 3: '))
object=triangle(a,b,c,height)
print('The perimeter of the the triangle is: ', object.perimeter())
print('The area of the the triangle is: ', object.area())

#2
class Sum:
    def __init__(self):
        self.total = sum(range(1, 1001))
    
    def get_sum(self):
        return self.total
object1 = Sum()
print(object1.get_sum())

#3
from math import factorial
class fac:
    def __init__(self,n):
        self.n=n
        self.fact=factorial(n)
    def fact1(self):
        return self.fact
n=int(input('Enter a number:'))
object2=fac(n)
print('the factorial of the number is:', object2.fact1())

#4
class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.series = self.generate_series()
    
    def generate_series(self):
        fib_series = [0, 1]
        while len(fib_series) < self.n:
            fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series[:self.n]
    
    def get_series(self):
        return self.series

n = int(input('Enter the number of terms in the Fibonacci series: '))
object3 = Fibonacci(n)
print('Fibonacci series:', object3.get_series())

