from bank_account import BankAccount
from transaction import Bank


class ATM:
    def __init__(self):
        self.accounts = {}
        self.transactions = []

    def add_account(self, account):
        self.accounts[account.name] = account

    def remove_account(self, name):
        del self.accounts[name]

    def get_account(self, name):
        return self.accounts[name]

    def deposit(self, name, amount):
        account = self.get_account(name)
        if account:
            account.deposit(amount)
            transaction = Bank(name, amount, "deposited")
            self.transactions.append(transaction)
        else:
            print("Account not found")

    def withdraw(self, name, amount):
        account = self.get_account(name)
        if account:
            if account.withdraw(amount):
                transaction = Bank(name, amount, "withdrawn")
                self.transactions.append(transaction)
            else:
                print("Insufficient balance")
        else:
            print("Account not found")

    def check_balance(self, name):
        account = self.get_account(name)
        if account:
            return account.check_balance()
        else:
            print("Account not found")

    def print_transactions(self):
        for transaction in self.transactions:
            print(transaction)
