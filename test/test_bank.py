import unittest
import os

from src.bank_account import BankAccount


class BankAccountTests(unittest.TestCase):

    def setUp(self) -> None:
        self.account = BankAccount(balance=1000,
                                   log_file="transaction_log.txt")

    def tearDown(self) -> None:
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)

    def _count_lines(self, filename):
        with open(filename, "r") as f:
            return len(f.readlines())

    def test_deposit(self):
        new_balance = self.account.deposit(500)
        self.assertEqual(new_balance, 1500, "El balance no igual")

    def test_withdraw(self):
        new_balance = self.account.withdraw(200)
        self.assertEqual(new_balance, 800, "El balance no igual")

    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 1000)

    def test_transfer(self):
        target_account = BankAccount(balance=500)
        new_balance = self.account.transfer(500, target_account)
        assert new_balance == 500
        assert target_account.balance == 1000

    def test_transfer_not_enough_balance(self):
        target_account = BankAccount(balance=500)
        with self.assertRaises(ValueError):
            self.account.transfer(1500, target_account)

    def test_transaction_log(self):
        self.account.deposit(500)
        self.assertTrue(os.path.exists("transaction_log.txt"))

    def test_count_transactions(self):
        assert self._count_lines(self.account.log_file) == 1
        self.account.deposit(500)
        assert self._count_lines(self.account.log_file) == 2
