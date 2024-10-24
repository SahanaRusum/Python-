import pandas
import pandas as pd

Student = {"Name" : ['sahana','rusum','akshara','sangu','deepa'],
           "English":[70,60,45,38,40],
           "Maths":[23,40,73,89,40],
           "science": [39, 94, 31, 80, 39],
           }
stud = pd.DataFrame(Student)
print(stud)

stud = pd.DataFrame(Student,index=[1,2,3,4,5])
print(stud)

print(stud.loc[2])