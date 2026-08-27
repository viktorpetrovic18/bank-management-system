import random
from sqlalchemy import create_engine

class Account:
    def __init__(self, account_number, name, pin, balance, transaction_history):
        self.account_number = account_number
        self.name = name
        self.pin = pin
        self.balance = balance
        self.transaction_history = transaction_history

    def display_account(self):
        print(f"Account number: {self.account_number}\n"
        f"Owner: {self.name}\n"
        f"Pin: {self.pin}\n"
        f"Balance: {self.balance}\n"
        f"Transactions: {self.transaction_history}")

    def deposit(self):
        amount = float(input("How much do you want to deposit? "))
        self.balance += amount
        print(f"New balance is: ${self.balance}")
    
    def withdraw(self):
        acc_inp = int(input("Enter your account number to access your account: "))
        if acc_inp == self.account_number:
            chck_pin = int(input("Enter your pin: "))
            if chck_pin == self.pin:
                if self.balance > 0:
                    withdraww = int(input("How much do you want to withdraw? "))
                    if withdraww > self.balance:
                        print("Insufficient funds.")
                    else:
                        self.balance -= withdraww
                        print(f"Your new balance is ${self.balance}")
    def transfer(self):
        user = int(input("Enter your account number: "))
        if self.account_number == user:
            user1 = int(input("Enter your pin: "))
            if self.pin == user1:
                trans_user = int(input("Enter the account number you want to transfer the funds to: "))
                for account in accounts_list:
                    if trans_user == account.account_number:
                        print("We have found a match.")

accounts_list = []

def create_account():
    account_number = random.randint(100_000_000, 999_999_999)
    name = input("Please enter your name: ")
    pin = int(input("Enter your four digit pin: "))
    balance = 0
    transaction_history = 0

    account = Account(
        account_number,
        name,
        pin,
        0,
        0
    )

    accounts_list.append(account)
    print("---Account created succesfully and appended to the list--- ".upper())
    return account


account2 = Account(
    12345,
    "Milos",
    1234,
    0,
    0
)

account = create_account()
account.display_account()
account.transfer()




