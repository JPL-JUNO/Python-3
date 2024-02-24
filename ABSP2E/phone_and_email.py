"""
@File         : phone_and_email.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-13 18:09:24
@Email        : cuixuanstephen@gmail.com
@Description  : 项目：电话号码和 E-mail 地址提取程序
"""

import pyperclip, re

# BUG 98769-1234 会被识别为 769-1234，其实不是 phone num
phone_regex = re.compile(
    r"""(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # separator
    (\d{3})                         # first 3 digits
    (\s|-|\.)?                      # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    )
    """,
    re.VERBOSE,
)

email_regex = re.compile(
    # 用户名部分是一个或多个字符，字符可以包括：小写和大写字
    # 母、数字、句点、下划线、百分号、加号或短横。
    # 域名允许的字符分类要少一些，只允许字母、数字、句点和短横
    r"""(
        [a-zA-Z0-9._%+-]+   # username
        @                   # @ symbol
        [a-zA-Z0-9.-]+      # domain name
        (\.[a-zA-Z]{2,4})   # dot-something
    )

    """,
    re.VERBOSE,
)

if __name__ == "__main__":
    text = str(pyperclip.paste())
    matches = []
    for groups in phone_regex.findall(text):
        if groups[1]:
            phone_num = "-".join([groups[1], groups[3], groups[5]])
        else:
            phone_num = "-".join([groups[3], groups[5]])
        if groups[8]:
            phone_num += " x" + groups[8]
        matches.append(phone_num)

    for groups in email_regex.findall(text):
        matches.append(groups[0])
    # matches.extend(email_regex.findall(text))

    if matches:
        pyperclip.copy("\n".join(matches))
        print("Copied to clipboard:")
        print("\n".join(matches))
    else:
        print("No phone numbers or email addresses found.")
