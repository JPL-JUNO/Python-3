"""
@File         : 2_2 Using List Comprehensions on Files.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-01-24 19:23:02
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""
f = open("./script2.py")
lines = f.readlines()
print(lines)

lines = [line.rstrip() for line in lines]

lines = [line.rstrip() for line in open("./script2.py")]
print(lines)

import sys, os

sys.path.append(os.path.join("../"))
from funcs import info

info("列表推导的表现力也很强")
[line.upper() for line in open("./script2.py")]
[line.upper().rstrip() for line in open("./script2.py")]
[line.replace(" ", "!") for line in open("./script2.py")]

[("sys" in line, line[:5]) for line in open("./script2.py")]
