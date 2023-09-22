"""
@Title: count()
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-20 11:04:09
@Description: 
"""

from itertools import count

for i in zip(count(1), ['a', 'b', 'c']):
    print(i)
print()

# count() 的开始位置和步长参数可以是可相加的任意的数字值
import fractions
start = fractions.Fraction(1, 3)
step = fractions.Fraction(1, 3)
for i in zip(count(start, step), ['a', 'b', 'c']):
    print("{}: {}".format(*i))
