from datetime import datetime
from functools import wraps

def time_decorator(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        return datetime.now()
    return inner

def enough_in_balance(fn):
    @wraps(fn)
    def inner(self, amount):
        if amount <= 0 or (self.balance - amount) < 0:
            print("Withdrawing negative, zero or amounts larger than your balance is not allowed")
    return inner

def is_created(skip_print = False):
    if not account_created:
        if not skip_print:
            print("There is no account")
        return False
    return True

account_created = False



class BankAccount:
    def __init__(self,):
        self.balance = 0
        self.transactions = []
    def deposit(self, amount): #deposit amount into the balance
        if amount <= 0:
            print("depositing negative amounts")
        else:
            self.balance += amount

    @enough_in_balance
    def withdraw(self, amount): #withdraw amount from the balance
        self.balance -= amount

    def balance_inquiry(self):
        pass
    def transaction_history(self):
        pass
    def retrive_transactions(self):
        pass
    def account_statement(self):
        pass
    def account_summary(self):
        pass
    def account_clousure(self):
        pass
    def is_account_closed(self):
        pass





while True:
    print("~"*100)
    menu = input("""
what do you want to do?:
0: quit
1: create account
2: deposit
3: withdraw
4: inquire balance
5: see transaction history
6: retrive transactions
7: see account statement
8: see account summary
9: close account
10: check if account is closed
Type a number """)
    print("\n")
    match menu:
        case "0": #Stops the programm
            quit()
        case "1": #Creates an account
                if is_created(skip_print = True):
                    print("Account already exists")
                else:
                    account = BankAccount()
                    print("your account has succesfully been created")
                    account_created = True
                
        case "2": #Deposits an amount into the account
            if is_created():
                amount = float(input("how much do you want to deposit? "))
                account.deposit(amount)
        case "3": #Withdraws an amount from the account
            if is_created():
                amount = float(input("how much do you want to withdraw? "))
                account.withdraw(amount)
            else:
                print("")
        case "4": #checks the balance
            if is_created():
                account.balance_inquiry
        case "5": #Check the transaction history
            if is_created():
                account.transaction_history
        case "6": #Retrives the past transactions
            if is_created():
                account.retrive_transactions
        case "7": #Checks the account statement
            if is_created():
                account.account_statement
        case "8": # Checks the account summary
            if is_created():
                account.account_summary
        case "9": # Closes the account
            if is_created():
                account.account_clousure
                print("account is closed")
                account_created = False
        case "10": # checks if the account is closed
            if is_created():
                print("account still exists")
        case _:
            raise ValueError("That is NOT a valid choice")