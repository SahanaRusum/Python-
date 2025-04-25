""" for loop- is a type of loop used in python. It's an entry based loop.
The basic syntax is: for variable in sequence:
    # Block of code to be executed
range() is often used with a for loop to create a sequence of numbers.
Syntax: range(start, stop, step), where:
start: The starting value (default is 0).
stop: The ending value (exclusive).
step: The difference between each number (default is 1).
This folder contents some question based on for loop. 
"""
# question 1: Print Numbers from 1 to 10

for i in range(1,11):
    print(i)

#question2 :  Find Even Numbers from 1 to 20

for i in range(1,21):
    if i%2==0:
      print(i)

#question3 : Find Odd Numbers from 1 to 20

for i in range(1,21):
   if i%2!=0:
      print(i)

#question4 : Write a program of squares for numbers from 1 to 5 using a for loop.

for i in range(1,6):
   print(i**2)

#question5 : Write a program that outputs 100 lines, numbered 1 to 100, each with your name on it. 

name=input('Enter your name: ')
for i in range(1,101):
   print(i,"",name)

#question6:  Write a program that uses a for loop to print the numbers 8, 11, 14, 17, 20, ..., 83, 86, 89

for i in range(8,90,3):
   print(i, end=",")

#question 7: Write a program that uses a for loop to print the numbers 100, 98, 96, ..., 4, 2

for i in range(100,2,-2):
   print(i,end=",")

#question8: Write a program that asks the user for their name and how many times to print it.
# The program should print out the user’s name the specified number of times.
num=int(input('Enter a number:'))
name=input('Enter your name: ')
for _ in range(num):
   print(name)

#question9: Use a for loop to print a box with astricks.
height=int(input('Enter height: '))
width=int(input('Enter width:'))
for i in range(height):
   print('*'*width)

#question10: The Fibonacci numbers are the sequence below, where the first two numbers are 1, and each
#number thereafter is the sum of the two preceding numbers. Write a program that asks the
#user how manyFibonacci numbers to print and then prints that many. 1,1,2,3,5,8,13,21,34,55,89...

number=int(input('Enter your number: '))
a=0
b=1
if number<=0:
   print(0)
else:
   print(a,b,end=" ")
   for i in range(2,number):
      c=a+b
      print(c,end=" ")
      a=b
      b=c

"""question11:  Use a for loop to print a triangle like the one below. 
Allow the user to specify how high the
 triangle should be.
 *
 **
 ***
 **** """
length=int(input('Enter height: '))
for i in range(length):
   print('*'*(i+1))
""" quesion12: Use a for loop to print an upside down triangle like the one below. 
Allow the user to specify
 howhigh the triangle should be.
 ****
 ***
 **
 *
"""
length1=int(input('Enter height: '))
for i in range(length1):
   print('*'*(length1-i))

""" question13:   Use a for loop to print a box like the one below. Allow the user to specify how wide and how
 high the box should be.
 *******************
 *                 *
 *                 *
 *******************
"""
height1=int(input('Enter height: '))
width1=int(input('Enter width:'))
print('*'*width1)
for _ in range(height1-2):
   print('*' + " "*(width1-2)+"*")
print('*'*width1)

# question14: Find all prime numbers between 1 and 50
for num in range(2, 51):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)
# question15: Find Sum of Numbers from 1 to 100
total=0
for i in range(1,101):
   total=i+total
print(total)

#question 16: Print numbers divisible by 3 or 5 from 1 to 20 using a for loop
for i in range (1,21):
   if (i%3)==0 or (i%5)==0:
      print(i)

#question 17: Print numbers from 1 to 5, except 3 using a for loop and continue statement
for i in range(1,6):
   if i==3:
      continue
   print(i)

"""question 18: Print numbers from 1 to 10. If a number is 
divisible by 4, stop the loop using a for loop and break statement:
"""
for i in range(1,11):
 print(i)
 if i%4==0:
      break
  
"""  Use for loops to print a diamond like the one below. Allow the user to specify how high the
 diamond should be.
     *
    ***
   *****
  *******
   *****
    ***
     *

"""

height3 = int(input("Enter the height of the diamond (half height): "))

# Upper half of the diamond (including the middle row)
for i in range(height3):
    spaces = height3 - i - 1
    stars = 2 * i + 1
    print(" " * spaces + "*" * stars)

# Lower half of the diamond
for i in range(height3 - 2, -1, -1):
    spaces = height3 - i - 1
    stars = 2 * i + 1
    print(" " * spaces + "*" * stars)
