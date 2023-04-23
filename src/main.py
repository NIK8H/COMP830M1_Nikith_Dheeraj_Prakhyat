from bank_account import BankAccount
from atm import ATM
from transaction import Bank


if __name__ == "__main__":
    # Create bank accounts
    account1 = BankAccount("123456", 1000)
    account2 = BankAccount("789012", 500)

    # Create bank and ATM
    bank = Bank([account1, account2])
    atm = ATM(bank)

    # Use ATM
    account_number = input("Please enter your Account Number:")
    if account_number == 123456 or 789012:
        pin = int(input("Please enter you pin number:"))
        if pin == 1234:
            account_number = "123456"
            atm.insert_card(account_number, pin)
            atm.select_account(account_number)
            print(atm.check_balance())  # Returns 1000
            atm.deposit(500)
            print(atm.check_balance())  # Returns 1500
            print(atm.withdraw(200))  # Returns 200
            print(atm.check_balance())  # Returns 1300
        else:
            print("Incorrect pin number")
    else:
        print("Invalid Account Number")
