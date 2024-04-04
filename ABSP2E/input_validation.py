"""
@File         : input_validation.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-14 13:30:43
@Email        : cuixuanstephen@gmail.com
@Description  : 输入验证
"""

import pyinputplus as pyip

response = pyip.inputNum()

response = input("Enter a number: ")
response = pyip.inputInt(prompt="Enter a number: ")

response = pyip.inputNum("Enter Num: ", min=4)
response = pyip.inputNum("Enter Num: ", greaterThan=4)
response = pyip.inputNum("Enter Num: ", min=4, lessThan=6)


response = pyip.inputNum("Enter Num: ")
response = pyip.inputNum("Enter Num: ", blank=True)

response = pyip.inputNum(limit=2)
response = pyip.inputNum(timeout=10)
response = pyip.inputNum(limit=2, default=0)

response = pyip.inputNum(allowRegexes=[r"(I|V|X|L|C|D|M)+", r"zero"])
response = pyip.inputNum(blockRegexes=[r"[02468]$"])
response = pyip.inputStr(
    allowRegexes=[r"caterpillar", "category"], blockRegexes=[r"cat"]
)


def adds_uo_to_ten(numbers):
    numbers_lst = list(numbers)
    for i, digit in enumerate(numbers_lst):
        numbers_lst[i] = int(digit)
    if sum(numbers_lst) != 10:
        raise Exception(f"The digits must add up to 10, not {sum(numbers_lst)}.'")
    return int(numbers)


response = pyip.inputCustom(adds_uo_to_ten)
