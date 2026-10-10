from classes import BankAccount
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
    print(f'='*40)

while True:
    interface()
    choice = int(input("What would you like to do: "))
    match choice:
        case 1:
            print("You picket option 1")
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

