from time import perf_counter, strftime
from functools import wraps

# Decorators
def bal_check(func): # -> Handles checking if you can withdraw amount from account
    @wraps(func)
    def inner(self, amount):
        if (self.bal - amount) < 0:
            raise ValueError("Your account balance cannot go under zero.")
        return func(self, amount)
    return inner

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



# Main class for project
class BankAccount:
    def __init__(self, bal, account):
        self.bal = bal
        self.account = account
        self.history = []

    @time_elapsed
    def deposit(self, amount):
        self.bal += amount
        deposit_history = {"Type": "deposit","Amount": amount, "Time": strftime("%Y-%m-%d %H:%M")}
        self.history.append(deposit_history)
        return self.bal

    @bal_check
    @time_elapsed
    def withdraw(self, amount):
        self.bal -= amount
        withdraw_history = {"Type": "withdraw","Amount": amount, "Time": strftime("%Y-%m-%d %H:%M")}
        self.history.append(withdraw_history)
        return self.bal


    def bal_inc(self): # -> Lets you chec the current balance of the account
        return self.bal

    def transaction_history(self):
        history = list(self.history)
        return history

    def account_statement(self):
        print(f"{'Type':<12} {'Amount':>5} {'Time':>20}")
        print(f"="*40)
        for transaction in self.history:
            print(f"{transaction['Type']:<12} {transaction['Amount']:>5} {transaction['Time']:>21}")
        print(f"="*40)
        print(f"balance: {self.bal:>31}")

    # Account summary(--- || ---)

    def close_account(self): # Close the account
        pass

    def check_status(self): # Method for checkin if account is closed
        pass

acc = BankAccount(100, 123321)
acc.deposit(20000)
acc.withdraw(100)
acc.account_statement()

