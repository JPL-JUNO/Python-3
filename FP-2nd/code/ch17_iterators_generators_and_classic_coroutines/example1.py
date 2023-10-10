"""
@Title: 运行时打印消息的生成器函数
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-10 07:25:55
@Description: 
"""


def gen_AB():
    # 在 for 循环中，第一次隐式调用 next() 函数打印 'start'，然后停在第 1 个 yield 语句处，生成值 'A'
    print('start')
    yield 'A'
    print('continue')
    yield 'B'  # 第二次调用 next()
    print('end.')  # 第 3 次调用 next() 函数打印 'end.'，然后到达函数主体的末尾，导致生成器对象抛出 StopIteration 异常


for c in gen_AB():  # for 机制的作用与 g = iter(gen_AB()) 一样，用于获取生成器对象，并在每次迭代时调用 next()
    print('-->', c)
