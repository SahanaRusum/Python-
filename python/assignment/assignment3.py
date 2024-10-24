Uerid='abc123'
password='1234'
user=eval(input('enter userid'))
pin=eval(input('enter your pin'))
if Uerid==user and password==pin:
    print('welcome')
else:
    print('try again')

bankbalane=50000
money=eval(input('eneter an amount:'))
select=eval(input('select 1 for withdraw\n ', 'select 2 for deposit\n', 'select 3 for balance enquire\n','select 4 for fast cash\n'))
if select=='1':
    if (money%2!=0):
        print('please enter in multiples of 1000')