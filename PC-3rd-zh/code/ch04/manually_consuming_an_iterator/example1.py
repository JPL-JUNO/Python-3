"""
@Title: 手动访问迭代器中的元素
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-03 17:23:40
@Description: 
"""

with open("example1.txt") as f:
    try:
        while True:
            line = next(f)
            print(line, end="")
    except StopIteration:
        pass

# 一般来说，StopIteration 异常是用来通知我们迭代结束的。但是，如果是手动使用 next()，也可以命令它返回一个结束值，比如说 None。
with open("example1.txt") as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end="")
