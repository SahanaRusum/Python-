#pallindrome
a=input('enter pet name :\n')
if a[:]==a[::-1]:
    print('true')
else:
    print('false')
#secret code:
a=input('enter the word:\n')
b=a[1::2]
c=a[0::2]
print('secret code:', b+c,'\n')
original=['']*(len(b)+len(c))
original[1::2]=b
original[0::2]=c
original=''.join(original)
print('original string:',original,'\n')

#phoneno:
phoneno = input('Enter your phone number:\n')
if len(phoneno) == 10:
    if phoneno.isnumeric():
        if phoneno[0] == '9' or phoneno[0] == '8' or phoneno[0] == '7':
            print('Valid')
        else:
            print('Invalid: Phone number should start with 9, 8, or 7.')
    else:
        print('Invalid: Phone number should contain only digits.')
else:
    print('Invalid: Phone number should be exactly 10 digits long.')

   


