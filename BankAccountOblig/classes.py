# Imports from the Programming Project pdf.
from time import perf_counter, strftime # This lets us check time and log system time to user
from functools import wraps # This lets the function keep its name through the decorators

# Decorators
def bal_check(func): # -> Handles checking if you can withdraw amount from account
    @wraps(func)
    def inner(self, amount):
        if (self.bal - amount) < 0:
            raise ValueError("Your account balance cannot go under zero.")
        return func(self, amount)
    return inner

# Takes the time of functions
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
        self.is_closed = False
        self.bal = bal
        self.account = account
        self.history = []

    # Decorators in proper order to check everything needed
    @check_status
    @time_elapsed
    def deposit(self, amount):
        self.bal += amount
        deposit_history = {"Type": "deposit","Amount": amount, "Time": strftime("%Y-%m-%d %H:%M")}
        self.history.append(deposit_history)
        return self.bal

    # Decorators in proper order to check everything needed
    @check_status
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


# Test
acc = BankAccount(100, 123321)
acc.deposit(20000)
acc.withdraw(100)
acc.account_summary()

