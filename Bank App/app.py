from BankClass import Bank
from Storage import all_accounts
from BankFunctions import findAccountNumber, signup, login

def bankApp():
    while True:
        print('\nWelcome to Bank Application')
        print('Signup to Access Bank Application')
        
        signup()
        
        email = input('Enter your email: ')
        password = input('Enter your password: ')
        
        user_login = login(email, password)
        
        if user_login:
            print('\nWelcome to Bank Application')
            print('-'*35)
            print('1. Create Account')
            print('2. Deposit Amount')
            print('3. Withdraw Amount')
            print('4. Show Details')
            print('5. Exit')

            choice = int(input('Enter your choice: '))

            if choice == 1:
                print('Create New Account')
                print('-'*35)
                yes_no = input('Do you really want to create new account? (y or n): ')
                if yes_no == 'y':
                    name = input('Enter your name: ')
                    balance = int(input('Enter your initial balance: '))
                    if balance >= 100:
                        b = Bank(name, balance)
                        all_accounts.append(b)
                        print('-'*55)
                        print(f'Account Created with A/C no. {b.account_number} with initial balance of Rs.{balance}')
                        print('-'*55)
                    else:
                        print('-'*55)
                        print('Initial Balance must be more than Rs.100.')
                        print('-'*55)
                else:
                    print('-'*55)
                    print('Continue on your transaction.')
                    print('-'*55)
            elif choice == 2:
                print('Deposit Amount')
                print('-'*35)
                yes_no = input('Do you really want to deposit amount? (y or n): ')
                if yes_no == 'y':
                    acc_number = input('Enter your acccount number: ')
                    find_acc = findAccountNumber(acc_number)
                    if find_acc:
                        balance = int(input('Enter your deposit amount: '))
                        find_acc.deposit(balance)
                    else:
                        print('Account Number doesnot match. Try Again.')
                else:
                    print('Continue with your transaction!!')
            elif choice == 3:
                print('Withdraw Amount')
                print('-'*35)
                yes_no = input('Do you really want to withdraw amount? (y or n):')
                if yes_no == 'y':
                    acc_number = input('Enter your account number: ')
                    find_acc = findAccountNumber(acc_number)
                    if find_acc:
                        balance = int(input('Enter your withdraw amount: '))
                        find_acc.withdraw(balance)
                    else:
                        print('Account Number doesnot match. Try Again.')
                else:
                    print('Continue with your transaction.')
            elif choice == 4:
                print('Show Details')
                print('-'*35)
                yes_no = input('Do you really want to show your details? (y or n):')
                if yes_no == 'y':
                    acc_number = input('Enter your account number: ')
                    find_acc = findAccountNumber(acc_number)
                    if find_acc:
                        find_acc.user_details()
                    else:
                        print('Account Number doesnot match. Try Again.')
                else:
                    print('Continue with your transaction.')
            elif choice == 5:
                print('Thank you for choosing us.')
                break
        else:
            print('Username and password incorrect.')