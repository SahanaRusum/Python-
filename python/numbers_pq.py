# question 1: Write a program that generates and prints 50 random integers, each between 3 and 6
from random import randint
import random
import math
for _ in range(50):
    x=randint(3,6)
    print(x)

#question 2:  Write a program that generates a random number, x, between 1 and 50, a random number y between 2 and 5, and computes x^y.

x1=randint(1,50)
y1=randint(2,5)
print('the product is,', x1**y1)

#question 3: Write a program that generates a random number between 1 and 10 and prints your name that many times.
name=input('Enter your name: ')
for _ in range(randint(1,10)):
    print(name)

#question 4: Write a program that generates a random decimal number between 1 and 10 with two decimal places of accuracy. Examples are 1.23, 3.45, 9.80, and 5.00
random_decimal = round(random.uniform(1.00, 10.00), 2)
print(random_decimal)

#question 5: Write a program that generates 50 random numbers such that the first number is between 1 and 2, the second is between 1 and 3, the third is between 1 and 4, ..., and the last is between 1 and 51.
for i in range(1,51):
    print(randint(1,i+1))

#question 6: Write a program that asks the user to enter two numbers, x and y, and computes |x-y|/ x+y.
num1=int(input('Enter first number : '))
num2=int(input('Enter second number : '))
a=abs(num1-num2)
b=num1+num2
result=a/b
print('the result is',result)

""" question 7:  Write a program that asks the user to enter an angle between 180 and 180. Using an
 expression with the modulo operator, convert the angle to its equivalent between 0 and
 360.
"""
m=eval(input('Enter an angle between -180 to 180:'))
n=(m+360)%360
print(n)

"""question 8: Write aprogramthataskstheuserforanumberofsecondsandprintsouthowmanyminutes
 and seconds that is. For instance, 200 seconds is 3 minutes and 20 seconds. """

number=int(input('Enter your sonds: '))
minute=number//60
seconds=number%60
print ('the time is ', minute ,'minute', seconds, 'seconds')

""" question 9:  Write a program that asks the user for an hour between 1 and 12 and for how many hours in
 the future they want to go. Print out what the hour will be that many hours into the future.
"""
hours=int(input('Enter your hour: '))
hours_ahead=int(input('Enter how many hours ahead: '))
time=(hours+hours_ahead)%12
print('time is ', time)

""" question 10 : (a) One way to find out the last digit of a number is to mod the number by 10. Write a
 program that asks the user to enter a power. Then find the last digit of 2 raised to that
 power.
 (b) One way to find out the last two digits of a number is to mod the number by 100. Write
 a program that asks the user to enter a power. Then find the last two digits of 2 raised to
 that power.
 (c) Write a program that asks the user to enter a power and how many digits they want.
 Find the last that many digits of 2 raised to the power the user entered.
"""
power=int(input('Enter your power: '))
n1=2**power
ld=n1%10
print('the last digit is ',ld)

power1=int(input('Enter your power: '))
n2=2**power1
ld1=n2%100
print('the last two digit are ',ld1)

power2=int(input('Enter your power: '))
n3=2**power2
ld2=int(input('Enter how many digits you want'))
last_digits = n3 % (10 ** ld2)
print('The last', ld2, 'digits are', last_digits) 

"""
question 11: Write a program that asks the user to enter a weight in kilograms. The program should
 convert it to pounds, printing the answer rounded to the nearest tenth of a pound
"""
weight=int(input('Enter your weight in kg :'))
pounds=weight*2.2
nearest_tenth=round(pounds,1)
print('Nearest tenth is :', nearest_tenth)

"""question 12:Write a program that asks the user for a number and prints out the factorial of that number.

"""
num3=int(input('Enter your number: '))
print('The factorial is, ', math.factorial(num3))

""" question 13:  Write a program that asks the user for a number and then prints out the sine, cosine, and
 tangent of that number.
"""
angle=eval(input('Enter your angle in randian :'))
sine=math.sin(angle)
cosine=math.cos(angle)
tan=math.tan(angle)
print('sine', sine , 'cosine', cosine, 'tan', tan)

""" question 14: Write a program that asks the user to enter an angle in degrees and prints out the sine of that
 angle.
"""
degree=eval(input('Enter a number in angle:'))
radian=math.radians(degree)
print('The sin of that angle would be:',math.sin(radian))

""" question 15:  Write a program that prints out the sine and cosine of the angles ranging from 0 to 345 in
 15 increments. Each result should be rounded to 4 decimal places. Sample output is shown
 below:
 0--- 0.0 1.0
 15--- 0.2588 0.9659
 30--- 0.5 0.866
 ...
 345----0.2588 0.9659

"""
for i in range(0,346,15):
    angle1=math.radians(i)
    sine1=math.sin(angle1)
    cosine1=math.cos(angle1)
    sine1_round=round(sine1,4)
    cosine1_round=round(cosine1,4)
    print(i,'---', sine1_round, cosine1_round)


""" question 16: year is a leap year if it is divisible by 4,except that years divisible by 100 are not leap 
years unless they  also divisible by 400. Ask the user to enter a year, determine how many leap years there have been between 1600 and that year.
 """
leap_year=0
year=int(input('Enter your year :'))
for i in range(1600,year+1):
    if (i%4==0 and i%100!=0) or (i%400==0):
        leap_year=leap_year+1
print('the number of leap year is, ', leap_year)

""" question 17: Write a program that given an amount of change less than $1.00 will print out exactly how
 many quarters, dimes, nickels, and pennies will be needed to efficiently make that change.
"""
amount=float(input('enter your amount less than $1.00'))
cents=int(round(amount*100))
quarters = cents // 25
cents=cents%25

dimes=cents//10
cents=cents%10

nickels=cents//5
cents=cents%5

pennies=cents

print('the quarters are, ' ,quarters)
print('the dimes are, ' ,dimes)
print('the nickels are, ' ,nickels)
print('the pennies are, ' ,pennies)

""" question 18: 
Writeaprogramthatdraws“modularrectangles”liketheonesbelow.Theuserspecifiesthe
 widthandheightoftherectangle,andtheentriesstartat0andincreasetypewriterfashion
 fromlefttorightandtoptobottom,butarealldonemod10.Belowareexamplesofa3 5
 rectangleanda4 8.
 01234
 56789
 01234
 
 01234567
 89012345
 67890123
 45678901

"""
count=0
height=int(input('Enter the height: '))
width=int(input('Enter the width '))
for i in range(height):
    for j in range(width):
        print(count%10, end="")
        count=count+1
    print()
