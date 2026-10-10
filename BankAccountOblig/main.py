from classes import BankAccount
account_dict = {} # -> Overview over all accounts

# Interface - Temp (jeg vet ikke hva jeg vil det skal se ut som enda)
def interface():
    print("Bank Account Management System (BAMS)")
    print(f'='*40)
    print(f"{'Create account':<38} 1")
    print(f"{'Deposit':<38} 2")
    print(f"{'Withdraw':<38} 3" )
    print(f"{'Get balance':<38} 4")
    print(f"{'Transaction history':<38} 5")
    print(f"{'Account Info':<38} 6")
    print(f"{'Quit':<38} 7")
    print(f'='*40)

# Loop for the options
while True:
    interface()
    choice = input("What would you like to do: ")
    try:
        num_choice = int(choice)
    except ValueError:
        print("Please enter valid option")
        continue

    match num_choice:
        case 1:
            acc_number = input("Account number: ")

            # Checks if acc_number is in the account dictionary
            if acc_number in account_dict:
                print("This account number is taken")
                continue

            bal = input("Balance: ") # i chose to put it here so that the program doesnt ask for bal if accnumber is taken

            # Checks if bal is valid number
            try:
                number = float(bal)
            except ValueError:
                print("Please enter a valid balance")
                continue
            # Creates the class if all checks are good
            account = BankAccount(number, acc_number)
            # Adds the class and acc_number to the account dictionary
            account_dict[acc_number] = account

            print(f"You made an account!")

        case 2:
            print("You picket option 2")
        case 3:
            print("You picket option 3")
        case 4:
            print("You picket option 4")
        case 5:
            print("You picket option 5")
        case 6:
            print("You picket option 6")
        case 7:
            break
        case _:
            print("Please enter valid number")


