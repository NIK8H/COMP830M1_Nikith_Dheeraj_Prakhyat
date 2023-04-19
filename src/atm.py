class ATM:
    def __init__(self, bank):
        self.bank = bank

    def insert_card(self, card_number, pin):
        self.card_number = card_number
        self.pin = pin
        if self.bank.validate_card(self.card_number, self.pin):
            return True
        else:
            return False

    def select_account(self, account_number):
        if self.bank.validate_account(self.card_number, account_number):
            self.account_number = account_number
            return True
        else:
            return False

    def check_balance(self):
        return self.bank.get_balance(self.account_number)

    def deposit(self, amount):
        return self.bank.deposit(self.account_number, amount)

    def withdraw(self, amount):
        return self.bank.withdraw(self.account_number, amount)
