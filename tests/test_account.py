import unittest
from src.account import Account


class TestAccount(unittest.TestCase):
    def test_deposit(self):
        account = Account("test", 1234, 0)
        account.deposit(100)
        self.assertEqual(account.balance, 100)

    def test_withdraw(self):
        account = Account("test", 1234, 100)
        result = account.withdraw(50, 1234)
        self.assertTrue(result)
        self.assertEqual(account.balance, 50)

    def test_check_pin(self):
        account = Account("test", 1234, 0)
        self.assertTrue(account.check_pin(1234))
        self.assertFalse(account.check_pin(5678))


if __name__ == '__main__':
    unittest.main()