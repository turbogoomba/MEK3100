import time
from functools import wraps

def time_transaction_decorator(fn):
    @wraps(fn)
    def inner(self, amount):
        if amount <= 0:
            print("negative or zero amounts is not allowed")
        else:
            t = time.strftime("%Y-%m-%d %H:%M:%S")
            self.transactions.append({"type":f"{fn.__name__}", "amount":amount, "timestamp": t})
            fn(self, amount)
    return inner

def enough_in_balance(fn):
    @wraps(fn)
    def inner(self, amount):
        if (self.balance - amount) < 0:
            print("withdrawing amounts larger than your balance is not allowed")
        else:
            fn(self, amount)
    return inner

account_created = False

def is_created(skip_print = False):
    if not account_created:
        if not skip_print:
            print("There is no account")
        return False
    return True

class BankAccount:
    def __init__(self,):
        self.balance = 0
        self.transactions = []

    @time_transaction_decorator
    def deposit(self, amount): #deposit amount into the balance
        self.balance += amount
    
    @enough_in_balance
    @time_transaction_decorator
    def withdraw(self, amount): #withdraw amount from the balance
        self.balance -= amount

    def balance_inquiry(self):
        return print(f"current balance is {self.balance} kr")
    def transaction_history(self):
        if self.transactions:
            for i in range(len(self.transactions)):
                type = self.transactions[i].get("type")
                amount = self.transactions[i].get("amount")
                timestamp = self.transactions[i].get("timestamp")
                print(f"at {timestamp} you made a {type} of {amount} kr")
        else:
            print("there is no history")

    def retrive_transactions(self):
        if self.transactions:
            for i in self.transactions:
                print(i)
        else:
            print("there is no history")
    def account_statement(self):
        pass
    def account_summary(self):
        pass
    def account_clousure(self):
        pass
    def is_account_closed(self):
        pass


while True:
    print("~"*100) #shows the menu and allows input
    menu = input("""
what do you want to do?:
0: quit                     6: retrive transactions
1: create account           7: see account statement
2: deposit                  8: see account summary
3: withdraw                 9: close account
4: inquire balance          10: check if account is closed
5: see transaction history
Type a number """)
    print("\n")
    match menu:
        case "0": #Stops the programm
            quit()
        case "1": #Creates an account
                if is_created(skip_print = True):
                    print("Account already exists")
                else:
                    account = BankAccount() #makes the account again and resets the balance aswell as the history
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
                account.balance_inquiry()
        case "5": #Check the transaction history
            if is_created():
                account.transaction_history()
        case "6": #Retrives the past transactions
            if is_created():
                account.retrive_transactions()
        case "7": #Checks the account statement
            if is_created():
                account.account_statement()
        case "8": # Checks the account summary
            if is_created():
                account.account_summary()
        case "9": # Closes the account
            if is_created():
                account.account_clousure()
                print("account is closed")
                account_created = False
        case "10": # checks if the account is closed
            if is_created():
                print("account still exists")
        case _:
            print("That is NOT a valid choice")