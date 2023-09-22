"""
@Title: itemgetter
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-21 16:28:25
@Description: 
"""

from operator import itemgetter

l = [dict(val=-1 * i) for i in range(4)]
print("Dictionaries:")
print("  Original:", l)

g = itemgetter("val")
vals = [g(i) for i in l]
print("  values  :", vals)
print("  sorted  :", sorted(l, key=g))

l = [(i, i * -2) for i in range(4)]
print("\nTuples:")
print("  original:", l)
g = itemgetter(1)
# g 是一个函数，接受一个对象（或者是可调用的对象）
vals = [g(i) for i in l]
print("  values  :", vals)
print("  sorted  :", sorted(l, key=g))
