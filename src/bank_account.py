import datetime


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(("deposit", amount, datetime.datetime.now()))

    def withdraw(self, amount):
        if self.balance < amount:
            return "Insufficient balance"
        self.balance -= amount
        self.transactions.append(
            ("withdrawal", amount, datetime.datetime.now()))
        return amount
