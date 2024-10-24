a=input('enter your word')
odd=''
even=''
for i in range(len(a)):
    if i%2==0:
        even=even+a[i]
    else:
        odd=odd+a[i]

secret_Code=odd+even
print('the secret code is:', secret_Code,'\n')

original=['']*len(a)
index_odd=''
index_even=''
for i in range(len(a)):
    if i%2==0:
        original[i]=even[index_even]
        index_even+=1
    else:
         original[i]=odd[index_odd]
         index_odd+=1

original=''.join(original)
print('the original word:',original,'\n')
