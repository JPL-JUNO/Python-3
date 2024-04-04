"""
@File         : string_method_basics.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-10 23:53:39
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

my_string = "xxxSPAMxxx"
assert my_string.find("SPAM") == 3
my_string = "xxaaxxaa"
my_string.replace("aa", "SPAM")

my_string = "xxxSPAMxxx"
assert "SPAM" in my_string
assert "Ni" not in my_string

assert my_string.find("Ni") == -1  # when not found

my_string = "\t Ni\n"
assert my_string.strip() == "Ni"  # remove whitespace
assert my_string.rstrip() == "\t Ni"  # same, but just on right side

my_string = "STEPHEN"
assert my_string.lower() == "stephen"

assert my_string.isalpha()  # content tests
assert not my_string.isdigit()

import string

assert string.ascii_lowercase == "abcdefghijklmnopqrstuvwxyz"
assert string.whitespace == " \t\n\r\x0b\x0c"

my_string = "aaa,bbb,ccc"
assert my_string.split(",") == ["aaa", "bbb", "ccc"]  # 分割为子字符串组成的列表

my_string = "a b\nc\nd"
assert my_string.split() == ["a", "b", "c", "d"]  # 默认分隔符：泛空格符

delim = "NI"
assert delim.join(["aaa", "bbb", "ccc"]) == "aaaNIbbbNIccc"

assert " ".join(["A", "dead", "parrot"]) == "A dead parrot"

chars = list("Lorreta")
chars.append("!")
assert "".join(chars) == "Lorreta!"
