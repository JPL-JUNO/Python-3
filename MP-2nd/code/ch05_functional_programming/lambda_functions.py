"""
@Description: lambda functions
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-03 23:29:46
"""

values = dict(one=1, two=2, three=3)
# 按照键进行排序
print(sorted(values.items()))

# 按照值进行排序
print(sorted(values.items(), key=lambda item: item[1]))

import operator
get_value = operator.itemgetter(1)
print(sorted(values.items(), key=get_value))
# shows an alternative option using operator.itemgetter to generate a function that gets a specific item.


# key = lambda item: item[1]
# 不符合 PEP 8 的写法
def key(item):
    return item[1]
