"""
@File         : 8_sandwich_maker.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-14 18:25:48
@Email        : cuixuanstephen@gmail.com
@Description  : 三明治机
"""

import pyinputplus as pyip

bread = pyip.inputMenu(choices=["wheat", "white", "sourdough"])
protein = pyip.inputMenu(choices=["chicken", "turkey", "ham", "tofu"])
is_cheese = pyip.inputYesNo(prompt="cheese or not\n")
cheese = ""
if is_cheese == "yes":
    cheese = pyip.inputMenu(choices=["cheddar", "Swiss", "mozzarella"])
others = pyip.inputMenu(choices=["mayo", "mustard", "lettuce", "tomato"])
quantity = pyip.inputInt(greaterThan=1, prompt="How many sandwiches you want?\n")

prices = {bread: 1, protein: 3, cheese: 1, others: 1}
fee = 0
for component, price in prices.items():
    if component:
        print(component, ":", price)
        fee += price * quantity
print("quantity:", quantity)
print("Total:", fee)
