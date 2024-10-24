#1 Its childrens day and the class teacher wanted to share chocolates with the 
# entire class the details are as follows,The number of chocolates with the teacher are = 327 
# Number of kids in the class are = 78. Write a program to perform modulus division using (%)
#  modulus operator and find out how many chocolates are remaining with the teacher after 
# equally distributing 327 chocolates to 78 students.

totalchoclates= 327
kids=78
remaining= totalchoclates%kids
print('the remaining chocolates are:', remaining)

#2 It's Domino's 25th Anniversary and is planning for a big give away and in order to choose the lucky draw winner
#  Domino's first needs to collect all of its customer details. On collecting the customer details Domino's even 
# wants to thank each and every customer for visiting as soon as they entered their details.Write a program to 
# accept customer details like customer name, customer mobile number, customer age, customer email Id.
# On successfully receiving all the customer information write a print() to thank the customer by using his name 
# for example"Hi", customerName,"!! Thanks for visiting our restaurant and registering for our lucky draw
#  competition on our 25th Anniversary.""Once the lucky draw results are announced you will receive a message 
# on your mobile number :",customerMobileNumber"An detailed description of your gift on your
#  email Id :",customerEmailId"Thank you for being a valued customer",customerName,"!!""Dominos"

name=input('Enter your name:''\n')
phoneno=int(input('Enter your phone number:''\n'))
customerage=int(input('enter your age:''\n'))
emailid=input('Enter your emailid:''\n')
print('Hi,', name, '!!\n'
      'Thanks for visiting our restaurant and registering for our lucky draw competition on our 25th Anniversary.\n'
      'Once the lucky draw results are announced you will receive a message on your mobile number:', phoneno, '\n'
      'A detailed description of your gift on your email Id:', emailid, '\n'
      'Thank you for being a valued customer', name, '!!\n'
      'Dominos')


#3Teacher wants to conduct a quiz activity in her class. For that she is planning to group 4 students 
# for each team among 60 students. She wants to know how many teams she can create among 60 students.
# Write a program to find the total number of teams that can be created among students by dividing total 
# number of students to the number of students per team.Total number of student = 60 Number of students per team =4

total=60
m=4
print('The total number of students in each team would be: ', total/m)
print('\n')

#4 Nidhi loves to travel to different countries. She is now in a country where the temperature is 
# measured in Fahrenheit and she is not able to understand it in a better way. To help her in this situation, 
# write program to convert temperature from Fahrenheit to celsius. ● Hint: (0°C × 9/5) + 32 = 32°F

temp=eval(input('enter temperature in fahrenheit: ''\n'))
conv=(temp-32)*(5/9)
print('The temperture in celcius is: ',conv)
