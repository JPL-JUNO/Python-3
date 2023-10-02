"""
@Title: getsource_class.py
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-29 11:04:13
@Description: 
"""

import inspect
import example

# 传入一个类时，输出中会包含这个类的所有方法
print(inspect.getsource(example.A))


# 获取一个方法的源代码，可以将这个方法引用传入 inspect.getsource()
print(inspect.getsource(example.A.get_name))

# inspect.getsourcelines() 获取源代码中的代码行，并将其分解为单独的字符串

import pprint
# The return value from getsourcelines() is a tuple containing a list of strings (the lines
# from the source file) plus the line number in the file where the source begins.
pprint.pprint(inspect.getsourcelines(example.A.get_name))

# If the source file is not available, getsource() and getsourcelines() raise an IOError.
