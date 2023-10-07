"""
@Title: Mixing generators and coroutines
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-07 22:57:58
@Description: 
"""

from coroutine_decorator import coroutine

lines = 'some old text', 'really really old', 'old old old'


@coroutine
def replace(search, replace):
    while True:
        item = yield
        # 为什么是打印，而不是生成
        print(item.replace(search, replace))


old_replace = replace('old', 'new')
for line in lines:
    old_replace.send(line)
