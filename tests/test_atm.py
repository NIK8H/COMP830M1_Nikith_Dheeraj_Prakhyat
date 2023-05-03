# file: test_atm.py

import unittest
from src.account import Account
from src.atm import ATM


class TestATM(unittest.TestCase):
    def setUp(self):
        self.atm = ATM()
        self.account = Account("test", 1234, 100)
        self.atm.add_account(self.account)

    def tearDown(self):
        self.atm.remove_account("test")

    def test_get_account(self):
        result = self.atm.get_account("test")
        self.assertEqual(result, self.account)

    def test_get_accounts(self):
        result = self.atm.get_accounts()
        self.assertEqual(result, [self.account])

    def test_deposit(self):
        self.atm.deposit("test", 1234, 50)
        self.assertEqual(self.account.balance, 150)

    def test_withdraw(self):
        result = self.atm.withdraw("test", 1234, 50)
        self.assertEqual(result, "Transaction successful")
        self.assertEqual(self.account.balance, 50)

    def test_check_balance(self):
        result = self.atm.check_balance("test", 1234)
        self.assertEqual(result, 100)

    def test_check_pin(self):
        result = self.atm.check_pin("test", 1234)
        self.assertTrue(result)
        result = self.atm.check_pin("test", 5678)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
