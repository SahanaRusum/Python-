word = input('Enter a word:\n')
count_upper = 0
count_lower = 0
count_digit=0
count_special=0

for i in word:
    if i.isupper():
        count_upper += 1
    elif i.islower():
        count_lower +=1
    elif i.isdigit():
        count_digit +=1
    elif not i.isalnum():
        count_special +=1

print('The total number of uppercase letters are:', count_upper)
print('The total number of lowercase letters are:', count_lower)
print('The total number of digit are  are:', count_digit)
print('The total number of special character are:', count_special)

month = int(input('Enter your month: '))
year = int(input('Enter the year: '))

if month != 2:
    for i in range(1, 32): 
        if (month in [4, 6, 9, 11] and i <= 30) or (month not in [4, 6, 9, 11] and i <= 31):
            print('The possible dates are', i, '/', month, '/', year)
else:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        for i in range(1, 30):  
            print('The possible dates are', i, '/', month, '/', year)
    else:
        for i in range(1, 29):  
            print('The possible dates are', i, '/', month, '/', year)


               
term = int(input("Enter the term number of the Fibonacci series you want to find: "))

if term <= 0:
    print("Invalid input. Please enter a positive integer.")
elif term == 1:
    print("The 1st term of the Fibonacci series is: 0")
elif term == 2:
    print("The 2nd term of the Fibonacci series is: 1")
else:
    a = 0
    b = 1
    for _ in range(3, term + 1):
        c = a + b
        a = b
        b = c
    print("The" ,term,"th term of the Fibonacci series is:", b)

