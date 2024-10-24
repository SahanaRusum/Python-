#1 printing name
name="Arvind"
print(name)
name1="sahana"
age=24
print(name1,age, sep=" ")
#2 printing symbols
print('|')
print('-')
print('/')
print("\\")
#3 printing four name
print("sahana\nakshara\nsangjukta\ndevika\nxyz")
#4making para
name2=input('enter your name?')
age1=int(input('enter ypur age?'))
add=input('enter your address')
amb=input('enter your ambition?')
hobbies=input('enter your hobbies')

#two line para
print('hello, i am ', name2, 'my age is', age1, 'i live here', add)
print('my ambition is', amb, 'my hobbies are', hobbies)
#chatbot:
print('hi i am chatbot','\n')
askname=input('enter your name:''\n')
print('>>'+askname,'\n')
print('oh',askname,'what grade are you in','\n')
askgrade=input('enter your grade:''\n')
print('>>'+'i am in',askgrade,'\n')
print('can i ask you a question?','\n','please say yes or no')
answer=input('>>')
if answer == 'yes':
    print("Tell me 1024 + 98 = ?")
    answer1 = input(">> ")
    
    if answer1 == '1122':
        print("Good! Your answer is correct. Bye")
    else:
        print("Sorry, that's not correct. The correct answer is 1122. Bye")
else:
    print("Okay, maybe next time. Bye")

print(">> bye")

#5 cost of book  
bookcost=int(input('enter the amount of book brought'))
totalcost=int(bookcost * 2) #dollar 2
print('the total amount for the books are dollars:', totalcost)
#6 maths 
a=int(input('enter one number:'))
b=int(input('enter second number:'))
print('addition=''\n', a+b)

print('subtraction=''\n', a-b)

print('multiplication=''\n', a*b)

print('division=''\n', a/b)


#6 age 
currentage=int(input('enter the year you were born:'))
print('the current age is : ''\n', 2024-currentage  )



