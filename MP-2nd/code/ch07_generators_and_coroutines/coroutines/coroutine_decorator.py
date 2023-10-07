"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-07 22:47:07
@Description: 
"""

import functools


def coroutine(function):
    @functools.wraps(function)
    def _coroutine(*args, **kwargs):
        active_coroutine = function(*args, **kwargs)

        # 率先 or 事先告知
        # prime the coroutine and make sure we get no values
        # 因为 active_coroutine() 没有任何的生成值，生成为 None，
        # 直到调用 send 方法
        # 类似于将第一个 生成手动放掉等待 send 方法
        assert not next(active_coroutine)
        return active_coroutine
    return _coroutine
