"""
@File         : Generator Expressions.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-05-02 14:27:45
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

nums = [1, 2, 3, 4]
squares = (x * x for x in nums)
squares

next(squares)
next(squares)

for n in squares:
    print(n)

for n in squares:
    print(n)

f = open("data.txt")  # Open a file
lines = (t.strip() for t in f)  # Read lines, strip trailing/leading whitespace
comments = (t for t in lines if t[0] == "#")  # All comments
for c in comments:
    print(c)

clist = list(comments)
