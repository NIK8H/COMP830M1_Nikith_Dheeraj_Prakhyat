import unittest
from src.atm import ATM
from src.bank_account import BankAccount


class TestATM(unittest.TestCase):

    def setUp(self):
        self.atm = ATM()
        self.account = BankAccount(1234567890, 1234, 1000)

    def test_create_account(self):
        self.atm.add_account(self.account)
        self.assertIn(self.account, self.atm.accounts)

    def test_check_balance(self):
        balance = self.atm.check_balance(self.account, 1234)
        self.assertEqual(balance, 1000)

    def test_deposit_funds(self):
        self.atm.deposit(self.account, 1234, 500)
        self.assertEqual(self.account.balance, 1500)
        self.assertEqual(len(self.account.transaction_history), 1)

    def test_withdraw_funds(self):
        self.atm.withdraw(self.account, 1234, 500)
        self.assertEqual(self.account.balance, 500)
        self.assertEqual(len(self.account.transaction_history), 1)

    def test_incorrect_pin(self):
        with self.assertRaises(ValueError):
            self.atm.check_balance(self.account, 4321)


if __name__ == '__main__':
    unittest.main()
