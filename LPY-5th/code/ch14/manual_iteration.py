"""
@File         : Manual iteration.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-01-24 18:35:42
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

L = [1, 2, 3]

for X in L:
    print(X**2, end=" ")
print()

I = iter(L)  # Manual iteration: what for loops usually do
while True:
    try:
        # try statement catches exceptions
        # Or call I.__next__ in 3.X
        X = next(I)
    except StopIteration:
        break
    print(X**2, end=" ")
