from datetime import datetime

class Transaction:
    def __init__(self, account_name, amount, transaction_type):
        self.account_name = account_name
        self.amount = float(amount)
        self.transaction_type = transaction_type
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"{self.timestamp} - {self.account_name} - " \
               f"{self.transaction_type} - {self.amount}"