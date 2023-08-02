"""
@Description: Augmented Assignment with Sequences
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-06-26 12:46:29
"""

l = [1, 2, 3]
print(id(l))
l *= 2
print(l)
print(id(l))

t = (1, 2, 3)
print(id(t))
t *= 2
print(t)
print(id(t))

t = (1, 2, [30, 40])
try:
    t[2] += [50, 60]
except TypeError as e:
    print(repr(e))
print(t)

import dis
dis.dis('s[a] += b')
