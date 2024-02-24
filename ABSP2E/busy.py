"""
@File         : busy.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-14 15:09:31
@Email        : cuixuanstephen@gmail.com
@Description  : 项目：如何让人忙几小时
"""

import pyinputplus as pyip

while True:
    prompt = "Want to know how to keep a person busy for hours?\n"
    response = pyip.inputYesNo(prompt)
    if response == "no":
        break
print("Thank you. Have a nice day.")
