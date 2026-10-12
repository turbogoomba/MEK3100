# Imports from the Programming Project pdf.
from time import perf_counter, strftime # This lets us check time and log system time to user
from functools import wraps # This lets the function keep its name through the decorators
account_dict = {} # -> Overview over all accounts

# Decorators
def bal_check(func): # -> Handles checking if you can withdraw amount from account
    @wraps(func)
    def inner(self, amount):
        if (self.bal - amount) < 0:
            raise ValueError("Your account balance cannot go under zero.")
        return func(self, amount)
    return inner

# Checks if amount is acceptble amount for methods
def under_zero(func):
    @wraps(func)
    def inner(self,amount):
        if amount <= 0:
            raise ValueError("Cannot take value equal or under zero")
        return func(self, amount)
    return inner

#  Takes the time of functions
def time_elapsed(func):
    @wraps(func)
    def inner(self, amount):
        start = perf_counter()
        result = func(self, amount)
        end = perf_counter()
        time_elapsed = end - start
        print(f"{func.__name__} account took {time_elapsed * 1e06:.2f}µs")
        return result
    return inner

# Checks if the account is closed or not
def check_status(func):
    @wraps(func)
    def inner(self, amount):
        if self.is_closed:
            raise RuntimeError("This account is closed") # Raises RuntimeError if the account is closed
        else:
            return func(self, amount)
    return inner

# Main class
class BankAccount:
    def __init__(self, bal, account):
        if bal < 0:
            raise ValueError("Start balance cannot be zero")
        self.is_closed = False
        self.bal = bal
        self.account = account
        self.history = []

    # Decorators in proper order to check everything needed
    @check_status
    @under_zero
    @time_elapsed
    def deposit(self, amount):
        self.bal += amount
        deposit_history = {"Type": "deposit","Amount": amount, "Time": strftime("%Y-%m-%d %H:%M")}
        self.history.append(deposit_history)
        return self.bal

    # Decorators in proper order to check everything needed
    @check_status
    @under_zero
    @bal_check
    @time_elapsed
    def withdraw(self, amount):
        self.bal -= amount
        withdraw_history = {"Type": "withdraw","Amount": amount, "Time": strftime("%Y-%m-%d %H:%M")}
        self.history.append(withdraw_history)
        return self.bal

    def bal_inc(self): # Method to display balance to user
        return self.bal

    def transaction_history(self):
        history = list(self.history) # Gives a copy of history, so that it cannot be modified and manipulate self.history
        return history

    def account_statement(self): # Gives the user an account statement
        print(f"{'Type':<12} {'Amount':>5} {'Time':>20}")
        print("="*40)
        for transaction in self.history:
            print(f"{transaction['Type']:<12} {transaction['Amount']:>5} {transaction['Time']:>21}")
        print("="*40)
        print(f"balance: {self.bal:>31}")

    def account_summary(self):
        # This makes it so that we can auto align the box based on length of summary
        summary = f"| Account: {self.account} | Balance: {self.bal} | Transactions: {len(self.history)} |"
        print("="*len(summary))
        print(summary)
        print("="*len(summary))

    def close_account(self):
        self.is_closed = True
        self.bal = 0
        self.history = []

    def is_account_closed(self):
        return self.is_closed
def num_check(number):
    try:
        number = float(number)
        return number
    except ValueError:
        raise ValueError("Number not valid")


def find_account():
    account_num = input("Account number: ")
    if account_num in account_dict:
        return account_dict[account_num]
    else:
        raise ValueError("Account not found!")

# Interface - What the user will see.
def interface():
    opts = ["Make Account", "Deposit", "Withdraw",
           "Get Balance", "Retrieve Transactions", "Account Statement",
           "Account Closure", "Check If Closed", "Quit"]

    print("Bank Account Management System (BAMS)")
    print('='*40)
    for i, opt in enumerate(opts):
        print(i + 1, opt)
    print('='*40)

# Loop for the options
while True:
    interface()
    choice = input("What would you like to do: ")
    try:
        num_choice = int(choice)
    except ValueError:
        print("Please enter valid option")
        continue

    try:
        match num_choice:
            case 1: # Make account
                acc_number = input("Account number: ")
                # Checks if acc_number is in the account dictionary
                if acc_number in account_dict:
                    print("This account number is taken")
                    continue
                bal = input("Balance: ") # i chose to put it here so that the program doesnt ask for bal if accnumber is taken
                # Checks if bal is valid number
                number = num_check(bal)
                # Creates the class if all checks are good
                account = BankAccount(number, acc_number)
                # Adds the class and acc_number to the account dictionary
                account_dict[acc_number] = account

                print(f"You made an account!")

            case 2: # Deposit
                account = find_account()
                depo = input("Deposit: ")
                number = num_check(depo)
                account.deposit(number)
                print(f"Deposited {number} $")

            case 3: # Withdraw
                account = find_account()
                withdraw = input("Withdraw: ")
                number = num_check(withdraw)
                account.withdraw(number)
                print(f"Withdrew {number} $")

            case 4: # Get balance
                account = find_account()
                balance = account.bal_inc()
                print(f"Your balance is {balance} $")

            case 5: # Retrive transactions
                account = find_account()
                transactions = account.transaction_history()
                for transaction in transactions:
                    print(transaction)

            case 6: # Account statement
                account = find_account()
                account.account_statement()

            case 7: # Account closure
                account = find_account()
                account.close_account()

            case 8: # Check if closed
                account = find_account()
                status = account.is_account_closed()
                if status:
                    print("Account is closed!")
                    continue
                else:
                    print("Account is open!")
                    continue

            case 9: # Quit
                break
            case _:
                print("Please enter valid number")

    # This makes it so that we can handle both ValueError and RuntimeError, proivded from the decorators
    except (ValueError, RuntimeError) as e:
        print(e)
