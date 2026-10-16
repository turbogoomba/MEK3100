import time
from functools import wraps
import random

def time_transaction_decorator(fn): 
    @wraps(fn) 
    def inner(self, amount):
        if amount <= 0: #checking if the amount deposited or withdrawn is less than 0 so it doesnt get logged in the history
            print("negative or zero amounts is not allowed")
        else: #checks the timestamp and appends it into the transactions list in the BankAccount class
            t = time.strftime("%Y-%m-%d %H:%M:%S")
            self.transactions.append({"type":f"{fn.__name__}", "amount":amount, "timestamp": t})
            fn(self, amount)
    return inner

def enough_in_balance(fn):
    @wraps(fn)
    def inner(self, amount):
        if (self.balance - amount) < 0: # checks if the amount withdrawn makes the balance go bellow 0
            print("\nwithdrawing amounts larger than your balance is not allowed")
        else: #runs the function if the amount withdrawn is less than the current balance balance
            fn(self, amount)
    return inner

#This variable is to check if they made an account the first time they entered the program.
#doesnt make sense to check if a bank account that hasnt been made before is closed. you cant close something thats never been opened
made_first_time = False 

#checks if the account is created at all any time during the program. Unlike made_first_time which only checks for the first time.
account_created = False

# checks if the account is created and prints that there is no account.
# made this cause its a pain to copy paste print on ALL the cases when there isnt an account + i can use it in other places.
def is_created(skip_print = False):
    if not account_created:
        if not skip_print: #skip_print does exactly what it says. it lets the function return False without printing "there is no account"
            print("There is no account")
        return False
    return True

class BankAccount:
    def __init__(self, acc_num):
        self.balance = 0
        self.transactions = [] #transaction history
        self.account_number = acc_num #the number assigned to the account when its first made

    @time_transaction_decorator
    def deposit(self, amount): #deposit amount into the balance
        self.balance += amount
        print(f"\nyou have deposited {amount} kr")
    
    @enough_in_balance
    @time_transaction_decorator
    def withdraw(self, amount): #withdraw amount from the balance
        self.balance -= amount
        print(f"\nyou have withdrawn {amount} kr")
        

    def balance_inquiry(self):#formats the balance into a readable string telling you how much you have
        return print(f"current balance is {self.balance} kr")
    
    def transaction_history(self):
        if self.transactions: #checks if there are any elements in the list
            for i in range(len(self.transactions)): # takes the amount of elements in the dictionary and loops through them
                type = self.transactions[i].get("type") #find the type of element i
                amount = self.transactions[i].get("amount") #find the amount of element i
                timestamp = self.transactions[i].get("timestamp") #find the timestamp of element i
                print(f"at {timestamp} you made a {type} of {amount} kr") #prints it so its nice and readable
        else:
            print("there is no history") #if there is no elements in the transactions list it prints this

    def retrive_transactions(self): #kind of like the transactions_history method but this time its more for programmers
        if self.transactions: #checks if there are any elements in the list
            for i in self.transactions: #it prints each dictionary in the list directly
                print(i)
        else:
            print("there is no history") #if there is no elements in the transactions list it prints this

    def account_statement(self): #formates and prints out the history and the balance inquiry so its readable
        print("_"*100)
        print("your account statement:")
        print("_ "*50)
        self.transaction_history()
        print("_ "*50)
        self.balance_inquiry()

    def account_summary(self): #formats and prints out the account number, current balance and total transactions done
        print("_"*100)
        print("your account summary:")
        print("_ "*50)
        print(f"your account number is {self.account_number}")
        self.balance_inquiry()
        print(f"you have made {len(self.transactions)} transactions in total")

    def account_clousure(self): #closes the account by setting everything to 0 and emptying the list
        self.balance = 0
        self.transactions = []

    def is_account_closed(self): # checks if the account_created variable is True or False to see if the account is closed or not
        if not (account_created):
            print("the account is closed")
        else:
            print("the account is still open")


while True:
    print("~"*100)
    #shows the menu and allows input
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
    match menu: #chooses what it will run based on the users input
        case "0":
            print("you have quit the program")
            quit()
        case "1": #Creates an account
            made_first_time = True
            if is_created(skip_print = True):
                print("Account already exists")
            else:
                account_number = random.randint(1,100000) # generates a random account number for the user when account it created
                account = BankAccount(account_number) #makes the account again and resets the balance aswell as the history
                print("your account has succesfully been created")
                account_created = True #sets account_create to True so the is_account_closed method can use it to check later
                
        case "2": #Deposits an amount into the account
            if is_created():
                amount = float(input("how much do you want to deposit? "))
                account.deposit(amount)
        case "3": #Withdraws an amount from the account
            if is_created():
                amount = float(input("how much do you want to withdraw? "))
                account.withdraw(amount)
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
                account_created = False #sets account_create to false so the is_account_closed method can use it to check later
        case "10": # checks if the account is closed
            if made_first_time:
                account.is_account_closed()
            else:
                print("you havent made an account. you can therefore not have closed one")
                
        case _: #Stops the programm
            print("That is NOT valid, pick a number from 0-10")

