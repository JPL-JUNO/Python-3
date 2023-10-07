"""
@Title: Closing and throwing exceptions
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-07 22:46:35
@Description: 
"""
from coroutine_decorator import coroutine


@coroutine
def simple_coroutine():
    print('Setting up the coroutine')
    try:
        while True:
            item = yield
            print('Got item:', item)
    except GeneratorExit:
        print('Normal exit')
    except Exception as e:
        print('Exception exit:', e)
        raise
    finally:
        print('Any exit')


active_coroutine = simple_coroutine()
active_coroutine.send('from caller')

active_coroutine.close()

active_coroutine = simple_coroutine()
try:
    active_coroutine.throw(RuntimeError, 'caller sent an error')
except RuntimeError as err:
    print(err)
