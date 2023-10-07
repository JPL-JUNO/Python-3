"""
@Title: Priming
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-07 22:04:53
@Description: 
"""

from coroutine_decorator import coroutine


@coroutine
def our_coroutine():
    while True:
        print("Waiting for yield...")
        value = yield
        print('our coroutine received:', value)


generator = our_coroutine()
generator.send('a')
