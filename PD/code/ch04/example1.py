"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-01 21:38:52
@Description: 
"""


def compare(a, b):
    # is 和 is not 比较两个对象的标识
    if a is b:
        print("same object")
    if a == b:
        print("same value")
    # type 返回对象的类型
    if type(a) == type(b):
        print("same type")


items = list()
item: list = None
if isinstance(item, list):
    items.append(item)


def remove_all(items: list, item) -> list:
    return [i for i in items if i != item]

# 子类型(subtype)


class my_list(list):
    def remove_all(self, val):
        return [i for i in self if i != val]


items = my_list([4, 5, 2, 3])
x = items.remove_all(2)
print(x)  # [4, 5, 3]


if isinstance(items, (list, tuple)):
    max_val = max(items)
# 缺点：
# 1. 过多的检查会影响性能
# 2. 程序定义的对象并不是总是能很好的适应类型层次结构
