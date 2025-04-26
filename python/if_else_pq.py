"""question 1:  Write a program that asks the user to enter a length in centimeters. If the user enters a negative
 length, the program should tell the user that the entry is invalid. Otherwise, the program
 should convert the length to inches and print out the result. There are 2.54 centimeters in an
 inch """
cm=int(input('Enter your length in centimeter: '))
if cm<0:
    print('Invalid Entry, the length is in negative')
else:
    inch=cm/2.54
    print(inch)
""" question 2:  Askthe user for a temperature. Then ask them what units, Celsius or Fahrenheit, the temperature is in.
 Your program should convert the temperature to the other unit. The conversions are F = 9/5*C +32 and C = 5/9(F-32)
"""
temp=eval(input('Enter your temperature: '))
char=input('enter C for Celsius and F for Fahrenheit: ').lower()
if char=='c':
    fahrenheit=((9/5)*temp)+32
    print('the temp in Fahrenheit would be: ', fahrenheit)
elif char=='f':
    celsius=((5/9)*(temp-32))
    print('the temp in Celsius would be: ', celsius)

""" question 3: Ask the user to enter a temperature in Celsius. The program should print a message based
 on the temperature:
 • If the temperature is less than-273.15, print that the temperature is invalid because it is
 below absolute zero.
 • If it is exactly-273.15, print that the temperature is absolute 0.
 • If the temperature is between-273.15 and 0, print that the temperature is below freezing.
 • If it is 0, print that the temperature is at the freezing point.
 • If it is between 0 and 100, print that the temperature is in the normal range.
 • If it is 100, print that the temperature is at the boiling point.
 • If it is above 100, print that the temperature is above the boiling point.
"""

temp1=eval(input('Enter your temp: '))
if temp1 < -273.15:
    print('temperature is invalid because it is below absolute zero')
elif temp1 == -273.15:
    print('temperature is absolute 0')
elif -273.15 < temp1 < 0:
    print('temperature is below freezing')
elif temp1 == 0:
    print('temperature is at the freezing point')
elif 0 < temp1 < 100:
    print('temperature is in the normal range')
elif temp1 == 100:
    print('temperature is at the boiling point')
else:
    print('temperature is above the boiling point')


""" question 4: Write a program that asks the user how many credits they have taken. If they have taken 23
 or less, print that the student is a freshman. If they have taken between 24 and 53, print that
 they are a sophomore. The range for juniors is 54 to 83, and for seniors it is 84 and over
"""

credits=int(input('Enter your credits'))
if credits<=23:
    print('freshman')
elif credits >=24 and credits <=53:
    print('sophomore')
elif credits >=54 and credits <=83:
    print('juniors')
else:
    print('seniors')

""" question 5:  Generate a random number between 1 and 10. Ask the user to guess the number and print a
 message based on whether they get it right or not
"""
import random

num=random.randint(1,10)
guess=int(input('Enter a number between 1 and 10: '))
if num==guess:
    print('right')
else:
    print('wrong')

""" question 6:  A store charges $12 per item if you buy less than 10 items. If you buy between 10 and 99
 items, the cost is $10 per item. If you buy 100 or more items, the cost is $7 per item. Write a
 program that asks the user how many items they are buying and prints the total cost.
"""
no_of_products=int(input('Enter number of products: '))
if no_of_products<10:
    cost=no_of_products*12
    print('The cost is, ' , cost)
elif no_of_products>=10 and no_of_products<=99:
    cost=no_of_products*10
    print('the cost would be, ', cost)
else: 
    cost=no_of_products*7
    print('the cost would be, ', cost)

""" question 7: Write a program that asks the user for two numbers and prints Close if the numbers are
 within .001 of each other and Not close otherwise
"""
num1=float(input('Enter ypur first number: '))
num2=float(input('Enter your second number: '))
if abs(num2-num1)<0.001:
    print('close')
else:
    print('not close')

""" question 8: Ayear is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years
 unless they are also divisible by 400. Write a program that asks the user for a year and prints
 out whether it is a leap year or not
"""
year=int(input('Enter your year: '))
if (year%4==0) and (year%100!=0):
    print('it is a leap year')
elif  (year %400==0 )and (year%100==0):
    print('it is a leap year')
else:
    print('it is not a leap year')


""" question 9:  Write a program that asks the user to enter a number and prints out all the divisors of that
 number.
"""
number=int(input('enter your number:'))
for i in range(1,number+1):
    if number%i==0:
        print(i)

""" question 10: Write a multiplication game program for kids. The program should give the player ten ran
domly generated multiplication questions to do. After each, the program should tell them
 whether they got it right or wrong and what the correct answer is.
"""
for i in range(10):
    first_no=random.randint(1,10)
    second_no=random.randint(1,10)
    product=first_no*second_no
    print(first_no,'*',second_no, ': ')
    ans=int(input('Enter your answer: '))
    if ans==product:
        print('correct ans')
    else:
        print('correct ans is,', product)

""" question 11:  Write a program that asks the user for an hour between 1 and 12, asks them to enter am or pm,
 and asks them how manyhours into the future they want to go. Print out what the hour will
 be that many hours into the future, printing am or pm as appropriate. An example is shown
 below.
 Enter hour: 8
 am (1) or pm (2)? 1
 How many hours ahead? 5
 New hour: 1 pm
"""
a = eval(input('Enter your time from 1 to 12: '))
b = eval(input('Choose AM(1) or PM(2): '))
y = eval(input('How many hours ahead: '))

z = (a + y) % 12
if z == 0:
    z = 12

if b == 1:
    print('New hour:', z, 'am')
elif b == 2:
    print('New hour:', z, 'pm')


""" question 12: A jar of Halloween candy contains an unknown amount of candy and if you can guess exactly
 how much candy is in the bowl, then you win all the candy. You ask the person in charge the
 following: If the candy is divided evenly among 5 people, how many pieces would be left
 over? The answer is 2 pieces. You then ask about dividing the candy evenly among 6 people,
 and the amount left over is 3 pieces. Finally, you ask about dividing the candy evenly among
 7 people, and the amount left over is 2 pieces. By looking at the bowl, you can tell that there
 are less than 200 pieces. Write a program to determine how many pieces are in the bowl.

"""
 
for i in range(1,200):
    if i%5==2  and i%6==3 and i%7==2:
        print('no_of_candies_are: ', i)

""" question 13:  Write a program that lets the user play Rock-Paper-Scissors against the computer. There
 should be five rounds, and after those five rounds, your program should print out who won
 and lost or that there is a tie.

"""
user_score = 0
computer_score = 0

for i in range(5):
    user_choice = input('Enter rock, paper, or scissors: ').lower()
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    print('Computer chose:', computer_choice)

    if user_choice == computer_choice:
        print('It is a tie!')
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print('You win this round!')
        user_score += 1
    else:
        print('Computer wins this round!')
        computer_score += 1
    print()

if user_score > computer_score:
    print('You won the game!')
elif computer_score > user_score:
    print('Computer won the game!')
else:
    print('The game is a tie!')

