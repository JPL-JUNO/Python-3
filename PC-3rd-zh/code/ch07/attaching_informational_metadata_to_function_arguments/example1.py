"""
@Title: 将元数据信息附加到函数参数上
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-07 11:00:43
@Description: 
"""


def add(x: int, y: int) -> int:
    """
    >>> add.__annotations__
    {'x': <class 'int'>, 'y': <class 'int'>, 'return': <class 'int'>}
    >>> help(add)
    Help on function add in module __main__:

    add(x: int, y: int) -> int

    >>>
    """
    return x + y
