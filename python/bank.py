userid = 'abc123'
password = '1234'

while True:
    user = input('Enter userid:\n')
    pin = input('Enter your pin:\n')
    if userid == user and password == pin:
        print('Welcome')
        break
    else:
        print('Invalid userid or pin. Please try again.')

bank_balance = 50000

while True:
    money = int(input('Enter an amount: '))
    print('Select an option:')
    print('1 for Withdraw')
    print('2 for Deposit')
    print('3 for Balance Enquiry')
    print('4 for Fast Cash')
    
    select = input()
    
    if select == '1':
        if money % 1000 != 0:
            print('Please enter in multiples of 1000')
        elif money > bank_balance:
            print('Insufficient balance')
        else:
            bank_balance -= money
            print('Withdrawn:',money, 'Remaining balance:', bank_balance)
    elif select == '2':
        bank_balance += money
        print('Deposited,' ,money, 'New balance:', bank_balance)
    elif select == '3':
        print('Your current balance is:', bank_balance)
    elif select == '4':
        print('Fast cash options: 1000, 2000, 5000, 10000')
        fast_cash = int(input('Enter the fast cash amount: '))
        if fast_cash % 1000 != 0:
            print('Please enter in multiples of 1000')
        elif fast_cash > bank_balance:
            print('Insufficient balance for fast cash')
        else:
            bank_balance -= fast_cash
            print('Withdrawn:', fast_cash, 'Remaining balance:',bank_balance)
    else:
        print('Invalid selection. Please try again.')
