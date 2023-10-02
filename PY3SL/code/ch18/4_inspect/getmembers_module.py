"""
@Title: getmembers_module
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-29 10:26:24
@Description: 打印 example 模块的成员
"""

import inspect
import example

for name, data in inspect.getmembers(example):
    if name.startswith("__"):
        # 忽略一组 __builtins__ 的成员
        # 这不能算模块真正的一部分，而且这个列表很长
        continue
    print("{} : {!r}".format(name, data))
