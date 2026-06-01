import random
class Bank:
    def __init__(self, account_name, balance):
        self.account_name = account_name
        self.balance = balance
        self.account_number = "".join(str(random.randint(0, 9)) for i in range(16))

    def deposit(self, amount):
        if amount > 100:
            self.balance += amount
            print('-'*35)
            print(f'Rs.{amount} has been deposited to your account A/C. {self.account_number}.')
            print('-'*35)
        else:
            print('-'*35)
            print(f'Deposit amount must be more than Rs.100.')
            print('-'*35)

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            print('-'*35)
            print(f'Rs.{amount} has been withdrawn from your account A/C. {self.account_number}.')
            print('-'*35)
        else:
            print('-'*35)
            print(f'Withraw amount must be less than your balance amount.')
            print('-'*35)

    def user_details(self):
        print('-'*35)
        print(f'Account Name: {self.account_name}')
        print(f'Account Balance: Rs.{self.balance}')
        print(f'Account Number: {self.account_number}')
        print('-'*35)