from account import Account
from transaction import Transaction
import csv


class ATM:
    def __init__(self):
        self.accounts = {}
        self.transactions = []
        self.load_accounts()

    def add_account(self, account):
        self.accounts[account.name] = account

    def remove_account(self, name):
        del self.accounts[name]

    def get_account(self, name):
        return self.accounts[name] if name in self.accounts else None

    def get_accounts(self, name=None):
        if name:
            return [self.get_account(name)]
        else:
            return list(self.accounts.values())

    def deposit(self, name, pin, amount):
        account = self.get_account(name)
        if account and account.check_pin(pin):
            account.deposit(amount)
            transaction = Transaction(name, amount, "deposited")
            self.transactions.append(transaction)
            self.save_accounts()
        else:
            print("Account not found or incorrect PIN")

    def withdraw(self, name, pin, amount):
        account = self.get_account(name)
        if not account:
            return "Account not found"
        if not account.check_pin(pin):
            return "Invalid PIN"
        if account.balance < amount:
            return "Insufficient balance"
        if account.withdraw(amount, pin):
            transaction = Transaction(name, -amount, "withdrawn")
            self.transactions.append(transaction)
            self.save_accounts()
            return "Transaction successful"
        else:
            return "Check"

    def check_balance(self, name, pin):
        account = self.get_account(name)
        if account and account.check_pin(pin):
            return account.check_balance()
        else:
            print("Account not found or incorrect PIN")

    def print_transactions(self):
        for transaction in self.transactions:
            print(f"{transaction.account_name}: {transaction.amount} "
                  f"({transaction.transaction_type})")

    def save_accounts(self):
        with open("database.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            for account in self.get_accounts():
                writer.writerow([account.name, account.pin, account.balance])

    def load_accounts(self):
        try:
            with open("database.csv") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if "balance" in row:
                        self.add_account(
                            Account(row["name"], int(row["pin"]),
                                    float(row["balance"])))
                    else:
                        self.add_account(Account(row["name"], row))
        except FileNotFoundError:
            print("File not found.")
        except ValueError:
            print("Error loading accounts from file.")

    def check_pin(self, name, pin):
        account = self.get_account(name)
        if account and account.check_pin(pin):
            return True
        else:
            return False
