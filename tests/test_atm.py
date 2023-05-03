import unittest
from src.bank_account import BankAccount
from src.atm import ATM


class TestATM(unittest.TestCase):

    def setUp(self):
        self.atm = ATM()
        self.account1 = BankAccount("Alice", "1234")
        self.account2 = BankAccount("Bob", "5678")
        self.atm.add_account(self.account1)
        self.atm.add_account(self.account2)

    def test_add_account(self):
        account3 = BankAccount("Charlie", "9012")
        self.atm.add_account(account3)
        self.assertEqual(len(self.atm.accounts), 3)

    def test_remove_account(self):
        self.atm.remove_account("Bob")
        self.assertEqual(len(self.atm.accounts), 1)

    def test_get_account(self):
        account = self.atm.get_account("Alice")
        self.assertEqual(account.name, "Alice")
        self.assertEqual(account.pin, "1234")

    def test_deposit(self):
        self.atm.deposit("Alice", 100)
        self.assertEqual(self.account1.balance, 100)

    def test_withdraw(self):
        self.atm.withdraw("Bob", 50)
        self.assertEqual(self.account2.balance, 50)

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.atm.withdraw("Alice", 100)

    def test_check_balance(self):
        balance = self.atm.check_balance("Alice")
        self.assertEqual(balance, 0)

    def test_print_transactions(self):
        self.atm.deposit("Alice", 100)
        self.atm.withdraw("Bob", 50)
        self.atm.deposit("Charlie", 200)
        transactions = self.atm.print_transactions()
        self.assertEqual(len(transactions), 3)


if __name__ == '__main__':
    unittest.main()
