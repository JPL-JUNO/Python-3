"""
@File         : File Iterators.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-01-23 22:08:40
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""
import os
import sys

sys.path.append(os.path.dirname("../"))
from funcs import info

print(open("./script2.py").read())

open("./script2.py").read()

f = open("./script2.py")
f.readline()
f.readline()
f.readline()
f.readline()
f.readline()
f.readline()

# 文件也有一个方法，名为__next__，差不多有相同的效果：每次调
# 用时，就会返回文件中的下一行。唯一值得注意的区别在于，到达文件末尾
# 时，__next__会引发内置的StopIteration异常，而不是返回空字符串。
f = open("./script2.py")
f.__next__()
f.__next__()
f.__next__()
f.__next__()
f.__next__()
try:
    f.__next__()
except StopIteration as e:
    print(e)

info("读取文本文件的最佳方式")
for line in open("./script2.py"):
    print(line.upper(), end="")
# 这里的 print 使用 end='' 来抑制添加一个 \n，因为行字符串已经有
# 了一个（如果没有这点，我们的输出将会变成两行隔开）

f = open("./script2.py")
while True:
    line = f.readline()
    if not line:
        break
    print(line.upper(), end="")
