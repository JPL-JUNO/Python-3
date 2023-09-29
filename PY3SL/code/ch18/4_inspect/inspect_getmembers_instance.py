"""
@Title: inspect_getmembers_instance.py
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-29 10:48:47
@Description: 检查实例的方法与检查其他对象相同
"""
import inspect
from pprint import pprint
import example

a = example.A(name="inspect_getmembers")
pprint(inspect.getmembers(a, inspect.ismethod))

# ismethod() 找出实例 a 中 A 的两个绑定方法
