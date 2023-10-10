"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-10 21:18:39
@Description: 先在列表推导中使用 gen_AB 生成器函数，然后在生成器表达式中使用
"""


def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end.')


# 列表推导式会及早迭代 gen_AB() 函数返回的生成器对象产出的项
res1 = [x*3 for x in gen_AB()]
for i in res1:
    print('-->', i)

print()

# 生成器表达式返回一个生成器对象，该生成器在这里没有使用
res2 = (x*3 for x in gen_AB())
for i in res2:  # 仅当 for 循环迭代 res2 时，这个生成器才从 gen_AB 中获取项。
    # for 循环每迭代一次就隐式调用一次 next(res2)，
    # 而它又在 gen_AB() 返回的生成器对象上调用 next()
    # 提前执行到下一个 yield 语句
    print('-->', i)
