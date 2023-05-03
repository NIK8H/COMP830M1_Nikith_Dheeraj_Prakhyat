import os
import csv
from atm import ATM
from account import Account


# Load accounts from database.csv
def load_accounts():
    accounts = {}
    with open("database.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row["name"]
            pin = int(row["pin"])
            balance = float(row["balance"])
            account = Account(name, pin, balance)
            accounts[name] = account
    return accounts


# Save accounts to database.csv
def save_accounts(accounts):
    with open("database.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        for account in accounts:
            name = account.name
            balance = account.balance
            pin = account.pin
            writer.writerow([name, pin, balance])


# Create ATM instance
atm = ATM()

# Load accounts from database.csv
accounts_data = load_accounts()

# Create Account instances for each account in accounts_data
for account_name, account_data in accounts_data.items():
    account = Account(account_name, account_data.pin, account_data.balance)
    atm.add_account(account)

# ATM menu
while True:
    print("******************************")
    print("Welcome to the ATM Stimulator!")
    print("******************************")
    print("Please select an option:")
    print("1. Create Account")
    print("2. Remove Account")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Check Balance")
    print("6. Print Transactions")
    print("7. Exit")

    choice = input("> ")

    if choice == "1":
        check = int(input("Enter the Admin Password:"))
        if check == 123456:
            name = input("Enter account name: ")
            balance = float(input("Enter starting balance: "))
            pin = int(input("Create a 4 digit PIN: "))
            pin1 = int(input("Confirm PIN again:"))
            if pin == pin1:
                account = Account(name, pin, balance)
                atm.add_account(account)
                print(f"Account created: {account}")
                save_accounts(atm.get_accounts())
            else:
                print("PIN not matched try again")
        else:
            print("Incorrect Admin Password, Try Again")
    elif choice == "2":
        check = int(input("Enter the Admin Password:"))
        if check == 123456:
            name = input("Enter account name: ")
            atm.remove_account(name)
            print(f"Account removed: {name}")
            save_accounts(atm.get_accounts())
        else:
            print("Incorrect Admin Password, Try Again")
    elif choice == "3":
        name = input("Enter account name: ")
        pin = int(input("Enter PIN: "))
        if atm.check_pin(name, pin):
            amount = float(input("Enter amount to deposit: "))
            atm.deposit(name, pin, amount)
            print(f"Deposit successful. New balance: "
                  f"{atm.check_balance(name, pin)}")
            save_accounts(atm.get_accounts())
        else:
            print("Incorrect PIN")
    elif choice == "4":
        name = input("Enter account name: ")
        pin = input("Enter PIN: ")
        if atm.check_pin(name, pin):
            amount = float(input("Enter amount to withdraw: "))
            atm.withdraw(name, pin, amount)
            print(f"Withdrawal successful. New balance: "
                  f"{atm.check_balance(name, pin)}")
            save_accounts(atm.get_accounts())
        else:
            print("Incorrect PIN")
    elif choice == "5":
        name = input("Enter account name: ")
        pin = input("Enter PIN: ")
        if atm.check_pin(name, pin):
            balance = atm.check_balance(name, pin)
            print(f"Current balance: {balance}")
        else:
            print("Incorrect PIN")
    elif choice == "6":
        atm.print_transactions()
    elif choice == "7":
        print("Thanks for using ATM Stimulator!")
        break
    else:
        print("Invalid choice. Please try again.")
