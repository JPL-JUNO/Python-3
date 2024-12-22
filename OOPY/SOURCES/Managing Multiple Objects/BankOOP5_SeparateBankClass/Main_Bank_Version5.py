"""
@File         : Main_Bank_Version5.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-12-22 22:09:57
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

from Bank import Bank

oBank = Bank()
# Main code
# Create two test accounts
joesAccountNumber = oBank.createAccount("Joe", 100, "JoesPassword")
print("Joe's account number is:", joesAccountNumber)
marysAccountNumber = oBank.createAccount("Mary", 12345, "MarysPassword")
print("Mary's account number is:", marysAccountNumber)
while True:
    print()
    print("To get an account balance, press b")
    print("To close an account, press c")
    print("To make a deposit, press d")
    print("To open a new account, press o")
    print("To quit, press q")
    print("To show all accounts, press s")
    print("To make a withdrawal, press w ")
    print()

    action = input("What do you want to do? ")
    action = action.lower()
    action = action[0]  # grab the first letter
    print()
    if action == "b":
        oBank.balance()
    elif action == "c":
        oBank.closeAccount()
    elif action == "d":
        oBank.deposit()
    elif action == "o":
        oBank.openAccount()
    elif action == "s":
        oBank.show()
    elif action == "q":
        break
    elif action == "w":
        oBank.withdraw()
    else:
        print("Sorry, that was not a valid action. Please try again.")
print("Done")
