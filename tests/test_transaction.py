import unittest
from datetime import datetime
from src.transaction import Transaction


class TestTransaction(unittest.TestCase):
    def test_init(self):
        now = datetime.now()
        transaction = Transaction('deposit', 500, now)
        self.assertEqual(transaction.transaction_type, 'deposit')
        self.assertEqual(transaction.amount, 500)
        self.assertEqual(transaction.timestamp, now)


if __name__ == '__main__':
    unittest.main()
