"""
@File         : Account.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-12-21 15:51:13
@Email        : cuixuanstephen@gmail.com
@Description  : 第一个 Python 类文件
"""


class Account:
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = balance
        self.password = password

    def deposit(self, amountToDeposit, password):
        if password != self.password:
            print("Sorry, incorrect password")
            return None
        if amountToDeposit < 0:
            print("You cannot deposit a negative amount")
            return None
        self.balance += amountToDeposit
        return self.balance

    def withdraw(self, amountToWithdraw, password):
        if password != self.password:
            print("Incorrect password for this account")
            return None
        if amountToWithdraw < 0:
            print("You cannot withdraw a negative amount")
            return None
        if amountToWithdraw > self.balance:
            print("You cannot withdraw more than you have in your account")
            return None
        self.balance = self.balance - amountToWithdraw
        return self.balance

    def getBalance(self, password):
        if password != self.password:
            print("Sorry, incorrect password")
            return None
        return self.balance

    def show(self):
        print("    Name:", self.name)
        print("    Balance:", self.balance)
        print("    Password:", self.password)
