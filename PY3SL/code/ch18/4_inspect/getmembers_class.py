"""
@Title: getmembers_class.py
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-29 10:33:45
@Description: 检查类
"""

import inspect
import example

from pprint import pprint

pprint(inspect.getmembers(example.A), width=65)
# 将显示属性、方法、槽以及类的其他成员

# 要查找一个类的成员，可以使用谓词 isfunction()
# ismethod() 谓词只识别实例绑定的方法
pprint(inspect.getmembers(example.A, inspect.isfunction))

# 从 A 继承的方法会被识别为 B 的方法
pprint(inspect.getmembers(example.B, inspect.isfunction))
