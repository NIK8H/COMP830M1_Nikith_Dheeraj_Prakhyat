from bank_account import BankAccount
from atm import ATM
from transaction import Bank

if __name__ == "__main__":
    atm = ATM()
    account1 = BankAccount("Dheeraj", 1000)
    account2 = BankAccount("Nikith", 1500)
    atm.add_account(account1)
    atm.add_account(account2)

    # Using ATM Stimulator
    while True:
        print("Welcome to ATM Stimulator")
        print("1. Make a Deposit")
        print("2. Withdraw Money")
        print("3. Check balance")
        print("4. Print transactions")
        print("5. Add account")
        print("6. Remove account")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter account name: ")
            amount = int(input("Enter amount: "))
            atm.deposit(name, amount)
            transaction = Bank(name, amount, "deposited")
            print(f"Transaction logged: {transaction}")
        elif choice == "2":
            name = input("Enter account name: ")
            amount = int(input("Enter amount: "))
            atm.withdraw(name, amount)
            transaction = Bank(name, amount, "withdrawn")
            print(f"Transaction logged: {transaction}")
        elif choice == "3":
            name = input("Enter account name: ")
            balance = atm.check_balance(name)
            if balance:
                print(f"Balance for account {name}: {balance}")
        elif choice == "4":
            atm.print_transactions()
        elif choice == "5":
            name = input("Enter account name: ")
            balance = int(input("Enter account balance: "))
            account = BankAccount(name, balance)
            atm.add_account(account)
            print(f"Account {name} added successfully")
        elif choice == "6":
            name = input("Enter account name: ")
            atm.remove_account(name)
            print(f"Account {name} removed successfully")
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")
