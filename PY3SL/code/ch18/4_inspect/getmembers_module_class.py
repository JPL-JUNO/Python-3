"""
@Title: getmembers_module_class.py
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-29 10:31:13
@Description: 
"""

import inspect
import example

for name, data in inspect.getmembers(example, inspect.isclass):
    # 使用谓词函数过滤返回对象的类型
    print("{} : {!r}".format(name, data))
