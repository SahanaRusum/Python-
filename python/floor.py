"""x=5
y=3
z=x//y
z1=x**y
print(z)
print(z1)
z+=1
print(z)

"""
class Sum:
    def __init__(self):
        self.total = sum(range(1, 1001))
    
    def get_sum(self):
        return self.total
object1 = Sum()
print(object1.get_sum())

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
