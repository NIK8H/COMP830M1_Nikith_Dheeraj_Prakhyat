from datetime import datetime


class Bank:
    def __init__(self, name, amount, transaction_type):
        self.name = name
        self.amount = amount
        self.transaction_type = transaction_type
        self.timestamp = datetime.now()

    def validate_card(self, card_number, pin):
        # Code to validate card number and pin
        return True

    def validate_account(self, card_number, account_number):
        # Code to validate account number against card number
        return True

    def get_balance(self, account_number):
        account = self.get_account(account_number)
        return account.check_balance()

    def deposit(self, account_number, amount):
        account = self.get_account(account_number)
        account.deposit(amount)
        return account.check_balance()

    def withdraw(self, account_number, amount):
        account = self.get_account(account_number)
        return account.withdraw(amount)

    def get_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

