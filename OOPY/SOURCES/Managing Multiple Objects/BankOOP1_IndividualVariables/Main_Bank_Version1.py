"""
@File         : Main_Bank_Version1.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-12-22 20:51:52
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

from Account import *

oJoesAccount = Account("Joe", 100, "JoesPassword")
print("Created an account for Joe")
oMarysAccount = Account("Mary", 12345, "MarysPassword")

print("Created an account for Mary")
oJoesAccount.show()
oMarysAccount.show()
print()

# Call some methods on the different accounts
print("Calling methods of the two accounts ...")
oJoesAccount.deposit(50, "JoesPassword")
oMarysAccount.withdraw(345, "MarysPassword")
oMarysAccount.deposit(100, "MarysPassword")

oJoesAccount.show()
oMarysAccount.show()
