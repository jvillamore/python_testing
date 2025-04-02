import unittest

from src.bank_account import BankAccount


class BankAccountTests(unittest.TestCase):

    def setUp(self) -> None:
        self.account = BankAccount(balance=1000)

    def test_deposit(self):
        new_balance = self.account.deposit(500)
        assert new_balance == 1500

    def test_withdraw(self):
        new_balance = self.account.withdraw(200)
        assert new_balance == 800

    def test_get_balance(self):
        assert self.account.get_balance() == 1000

    def test_transfer(self):
        target_account = BankAccount(balance=500)
        self.account.balance = 1000
        new_balance = self.account.transfer(500, target_account)
        assert new_balance == 500
        assert target_account.balance == 1000

    def test_transfer_not_enough_balance(self):
        target_account = BankAccount(balance=500)
        with self.assertRaises(ValueError):
            self.account.transfer(1500, target_account)
