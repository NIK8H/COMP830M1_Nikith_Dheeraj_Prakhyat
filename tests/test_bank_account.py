import unittest
#from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(1234567890, 1234, 1000)
    def test_init(self):
        self.assertEqual(self.account.account_number, 1234567890)
        self.assertEqual(self.account.pin, 1234)
        self.assertEqual(self.account.balance, 1000)
        self.assertEqual(len(self.account.transaction_history), 0)
    def test_check_balance(self):
        balance = self.account.check_balance()
        self.assertEqual(balance, 1000)
    def test_deposit_funds(self):
        self.account.deposit_funds(500)
        self.assertEqual(self.account.balance, 1500)
        self.assertEqual(len(self.account.transaction_history), 1)
    def test_withdraw_funds(self):
        self.account.withdraw_funds(500)
        self.assertEqual(self.account.balance, 500)
        self.assertEqual(len(self.account.transaction_history), 1)
if __name__ == '__main__':
    unittest.main()