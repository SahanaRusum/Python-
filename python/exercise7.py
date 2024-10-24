""" from random import randint
l=[randint(1,10) for i in range(1000)]
avg=sum(l)/len(l)
print('avg is',avg)
"""
from random import randint

user_num=[]
count=0
for i in range(6):
     random_num=randint(1,10)
     user_num+=[random_num]
     user_num.sort()

for j in range(1000):
     picked=[]
     for k in range(6):
          pick_num=randint(1,10)
          picked+=[pick_num]
          picked.sort()
     if picked==user_num:
          count+=1
print("the avg darwing is: ",count, count/1000)