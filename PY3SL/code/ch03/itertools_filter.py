"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-20 16:39:04
@Description: 
"""


def check_item(x) -> bool:
    print("Testing:", x)
    return x < 1


for i in filter(check_item, [-1, 0, 1, 2, -2]):
    print("Yielding:", i)

# filter() 在返回之前测试每一个元素
