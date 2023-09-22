"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-20 12:49:59
@Description: 
"""

from itertools import repeat

for i in repeat("over-and-over", 5):
    print(i)
print()
# 如果既要包含来自其他迭代器的值，也要包含一些不便的值
# 那么可以结合使用 repeat() 以及 zip() 或 map()

from itertools import repeat, count
for i, s in zip(count(), repeat("over-and-over", 5)):
    print(i, s)
print()

# repeat() 迭代器不需要被显式限制，因为任何一个输入迭代器结束时 map() 就会停止处理，而且 range() 只返回 5 个元素
for i in map(lambda x, y: (x, y, x * y), repeat(2), range(5)):
    print("{:d} * {:d} = {:d}".format(*i))
