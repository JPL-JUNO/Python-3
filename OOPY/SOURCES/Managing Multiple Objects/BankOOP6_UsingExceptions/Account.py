"""
@File         : Account.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-12-24 22:00:15
@Email        : cuixuanstephen@gmail.com
@Description  : 在 Bank 程序中使用异常
"""


class AbortTransaction(Exception):
    pass


class Account:
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = self.validateAmount(balance)
        self.password = password

    def validateAmount(self, amount):
        try:
            amount = int(amount)
        except ValueError:
            raise AbortTransaction("Amount must be an integer")
        if amount <= 0:
            raise AbortTransaction("Amount must be positive")
        return amount

    def checkPasswordMatch(self, password):
        if password != self.password:
            raise AbortTransaction("Incorrect password for this account")

    def deposit(self, amountToDeposit):
        amountToDeposit = self.validateAmount(amountToDeposit)
        self.balance += amountToDeposit
        return self.balance

    def getBalance(self):
        return self.balance

    def withdraw(self, amountToWithdraw):
        amountToWithdraw = self.validateAmount(amountToWithdraw)
        if amountToWithdraw > self.balance:
            raise AbortTransaction(
                "You cannot withdraw more than you have in your account"
            )
        self.balance = self.balance - amountToWithdraw
        return self.balance

    # Added for debugging
    def show(self):
        print("    Name:", self.name)
        print("    Balance:", self.balance)
        print("    Password:", self.password)
