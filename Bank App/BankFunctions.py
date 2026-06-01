from Storage import all_accounts, users
from UserClass import User

def findAccountNumber(accNumber):
    for data in all_accounts:
        if accNumber == data.account_number:
            return data
    return None


def signup():
    username = input('Enter your username: ')
    email = input('Enter your email: ')
    phone = input('Enter your phone: ')
    password = input('Enter your password: ')
    confirm_password = input('Enter your confirm password: ')
    u = User(username, email, phone, password, confirm_password)
    users.append(u)

def login(email, password):
    for each_user in users:
        if each_user.email == email and each_user.password == password:
            return each_user
    return None