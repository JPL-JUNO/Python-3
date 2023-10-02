"""
@Title: chain()
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-20 10:15:48
@Description: chain() 函数取多个迭代器作为参数，最后返回一个迭代器，它会生成所有输入迭代器的内容
"""

from itertools import chain

for i in chain([1, 2, 3], ['a', 'b', 'c']):
    print(i, end=' ')
print()
StopIteration
