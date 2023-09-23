"""
@Title: Selecting items using a function
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-23 15:07:08
@Description: 
"""

import itertools

# 用途：比如说等待一个函数返回满足条件的结果
assert list(itertools.dropwhile(
    lambda x: x <= 3, [1, 3, 5, 4, 2])) == [5, 4, 2]


# the takewhile function is the reverse of this. 
# It will simply return all rows until the predicate turns false:

assert list(itertools.takewhile(lambda x: x <= 3, [1, 3, 5, 4, 2])) == [1, 3]