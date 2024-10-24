students=[]
num_students=int(input('enter the number of students: '))
for i in range(num_students):
    name=input('Enter the name of student')
    students.append(name)
students.sort()
for i in range(len(students)):
    roll_no=i+1
    print('the roll no are',roll_no,students)