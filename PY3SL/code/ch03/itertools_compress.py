"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-20 16:57:39
@Description: 
"""

from itertools import compress, cycle

every_third = cycle([False, False, True])
data = range(1, 10)
for i in compress(data, every_third):
    print(i, end=" ")
print()

# 第一个参数是要处理的数据迭代器，第二个参数是一个选择器迭代器，这个迭代器会生成
# 布尔值指示从数据输入中取哪些元素
