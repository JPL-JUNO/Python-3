"""
@Title: A basic example
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-07 21:53:46
@Description: 
"""


def generator():
    value = yield 'value from generator'
    print('Generator received:', value)
    yield f'Previous value: {value!r}'


g = generator()
print('Result from generator:', next(g))

# The function is frozen until the send method is called,
# at which point it will process up to the next yield statement.
print(g.send('value from caller'))

# 缺点：协程不能自己唤醒自己
