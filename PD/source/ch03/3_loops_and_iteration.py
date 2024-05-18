"""
@File         : 3_loops_and_iteration.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-05-17 22:59:10
@Email        : cuixuanstephen@gmail.com
@Description  : 循环和迭代
"""

s = [(1, 2, 3), (4, 5, 6)]
for x, y, z in s:
    pass

s = [(1, 2), (3, 4, 5), (6, 7, 8, 9)]
for x, y, *extra in s:
    pass

for i, x in enumerate(s):
    pass

with open("foo.txt") as file:
    for line in file:
        stripped = line.strip()
        if not stripped:
            break  # A blank line, stop reading
        # process the stripped line
        pass

with open("foo.txt") as file:
    for line in file:
        stripped = line.strip()
        if not stripped:
            continue  # Skip the blank line
        # process the stripped line
        pass


with open("foo.txt") as file:
    for line in file:
        stripped = line.strip()
        if not stripped:
            break
        # process the stripped line
        pass
    else:
        raise RuntimeError("Missing section separator")

found_separator = False
with open("foo.txt") as file:
    for line in file:
        stripped = line.strip()
        if not stripped:
            found_separator = True
            break
    if not found_separator:
        raise RuntimeError("Missing section separator")
