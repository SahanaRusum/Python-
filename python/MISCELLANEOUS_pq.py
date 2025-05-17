# question 1:  Write a program that counts how many of the squares of the numbers from 1 to 100 end in a 1.
count=0
for i in range(1,101):
    if (i**2)%10==1:
        count=count+1
print('the no of squares are ',count )

#question 2:  Write a program that counts how many of the squares of the numbers from 1 to 100 end
#  in a 4 and how many end in a 9
  
count1=0
for i in range(1,101):
    if (i**2)%10==4 or (i**2)%10==9:
        count1+=1
print('the number of squares are, ', count1)

# question 3 : Write a program that asks the user to enter a value n, and then computes (1+ 1/2 + 1/3 + + 1/n)
 #-ln(n). The ln function is log in the math module.
import math
count2=0
n=int(input('Enter your number: '))
for i in range(1,n+1):
  count2=count2+1/i
a=math.log(n)
result=count2-a
print('the result is, ' ,result)

# question 4 : Write a program to compute the sum 1-2+3-4+-+1999-2000
total = 0
for i in range(1, 2001):
    if i % 2 == 0:
        total -= i
    else:
        total += i
print(total)

#question 5: Write a program that asks the user to enter a number and prints the sum of the divisors of
 # that number. The sum of the divisors of a number is an important function in number theory.
number=int(input('Enter your number: '))
sum1=0
for i in range(1,number+1):
   if number%i==0:
      sum1=sum1+i
print('the sum of the divisors are : ', sum1)

"""question 6:  Anumberis called a perfect number if it is equal to the sum of all of its divisors,
 not including the number itself. For instance, 6 is a perfect number because the divisors of 6 
 are 1, 2, 3, 6 and 6=1+2+3. Asanother example, 28 is a perfect number because its divisors are 1, 2, 4,
 7, 14, 28 and 28 =1+2+4+7+14. However,15is not a perfect number because its divisors
 are 1, 3, 5, 15 and 15= 1+3+5. Write a program that finds all four of the perfect numbers
 that are less than 10000
"""
for num in range(1,10000):
   sum_of_divisors=0
   for i in range(1,num):
      if num%i==0:
         sum_of_divisors+=i
        
   if sum_of_divisors==num:
      print('perfect numbers: ,', num)

""" queation 7:An integer is called squarefree if it is not divisible by any perfect squares other than 1. For
 instance, 42 is squarefree because its divisors are 1, 2, 3, 6, 7, 21, and 42, and none of those
 numbers (except 1) is a perfect square. On the other hand, 45 is not squarefree because it is
 divisible by 9, which is a perfect square. Write a program that asks the user for an integer and
 tells them if it is squarefree or not.
"""
import math
num = int(input('Enter your number: '))
is_squarefree = True
for i in range(2, int(math.sqrt(num)) + 1):
    if num % (i * i) == 0:
        is_squarefree = False
        break
if is_squarefree:
    print(num, 'is squarefree')
else:
    print(num, 'is not squarefree')

""" question 8:  Write a program that swaps the values of three variables x, y, and z, so that x gets the value
 of y, y gets the value of z, and z gets the value of x.
"""
x=int(input('Enter your first number: '))
y=int(input('enter your second number: '))
z=int(input('enter your third number: '))

print('Original values:')
print('x =', x)
print('y =', y)
print('z =', z)

x,y,z=y,z,x

print('Swapped values:')
print('x =', x)
print('y =', y)
print('z =', z)

# question  9: Write a program to count how many integers from 1 to 1000 are not perfect squares, perfect 
# cubes, or perfect fifth powers
count3=0
for i in range(1, 1001):
    if (round(i**(1/2))**2 != i) and (round(i**(1/3))**3 != i) and (round(i**(1/5))**5 != i):
        count3 += 1
print("Count:", count3)


#question 10:  Write a program that computes the factorial of a number. The factorial, n!, of a number n isthe
 #product of all the integers between 1 and n, including n. For instance, 5! = 1 2 3 4 5=120
multiply = 1
num = int(input('Enter your number: '))
for i in range(1, num + 1):
    multiply *= i
print('The factorial is:', multiply)


""" question 11: Write a programthat asks the user to guess a randomnumberbetween1and10. Iftheyguess
 right, they get 10 points added to their score, and they lose 1 point for anincorrect guess. Give
 the user five numbers to guess and print their score after all the guessing is done.
"""
import random
score=0
for i in range(5):
 number2=int(input('Enter your number: '))
 number3=random.randint(1,10)
 if number2==number3:
   score=score+10
 else:
   score=score-1
print('The total score is : ', score)

""" question 12:   In the last chapter there was an exercise that asked you to create a multiplication game for
 kids. Improve your program from that exercise to keep track of the number of right and
 wrong answers. At the end of the program, print a message that varies depending on how
 many questions the player got right
"""
right=0
wrong=0
for _ in range(5):
   a=random.randint(1,10)
   b=random.randint(1,10)
   ans=int(input('What is ',a,'*',b ,':'))
   if ans==a*b:
      print('correct')
      right+=1
   else:
      print('incorrect')
      wrong+=1
print("You got", right, "right and", wrong, "wrong.")

if right == 5:
    print("Excellent work!")
elif right >= 3:
    print("Good job!")
else:
    print("Keep practicing!")