"""
@Title: 用生成器创建新的迭代模式
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-03 17:39:49
@Description: 
"""

# 如果想实现一种新的迭代模式，可使用生成器函数来定义。


def my_range(start, stop, step):
    x = start
    while x < stop:
        yield x
        x += step


for n in my_range(0, 4, .5):
    print(n)

list(my_range(0, 1, 0.125))

# 函数中只要出现了 yield 语句就会将其转变成一个生成器。与普通函数不同，生成器只
# 会在响应迭代操作时才运行。


def count_down(n):
    print("Starting to count from", n)
    while n > 0:
        yield n
        n -= 1
    print("Done")
