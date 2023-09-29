"""
@Title: getdoc.py
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-29 10:53:36
@Description: 
"""

import inspect
import example

print("B.__doc__:")
print(example.B.__doc__)
print()
print("getdoc(B):")
print(inspect.getdoc(example.B))

print()
# inspect.getcomments() 函数会查看对象的源文件
# 并查找实现代码前面的注释
# 返回的行中包括注释前缀，这里会去除空白符前缀
print(inspect.getcomments(example.B.do_something))


# 将模块传入 inspect.getcomments()，返回值总是模块中的第一个注释
# 邻接的行会作为一个注释，不过一旦出现一个空行，注释就会停止
print(inspect.getcomments(example))
