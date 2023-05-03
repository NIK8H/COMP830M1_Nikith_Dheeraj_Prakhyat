from transaction import Transaction


class Account:
    """Code for Account module."""
    def __init__(self, name, pin, balance):
        self.name = name
        self.pin = int(pin)
        self.balance = float(balance)
        self.transactions = []

    def check_pin(self, entered_pin):
        return self.pin == int(entered_pin)

    def deposit(self, amount):
        self.balance += amount
        self.add_transaction(amount, "deposited")

    def withdraw(self, amount, pin):
        if self.pin == pin:
            if amount <= self.balance:
                self.balance = self.balance-amount
                self.add_transaction(-amount, "withdrawn")
                return True
            else:
                return False
        else:
            return "Invalid PIN"

    def check_balance(self):
        return self.balance

    def get_details(self):
        return {"name": self.name, "pin": self.pin, "balance": self.balance}

    def add_transaction(self, amount, transaction_type):
        transaction = Transaction(self.name, amount, transaction_type)
        self.transactions.append(transaction)

    def __str__(self):
        return f"{self.name} account balance: {self.balance}"
