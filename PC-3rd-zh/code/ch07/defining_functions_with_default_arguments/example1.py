"""
@Title: 定义带有默认参数的函数
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-07 11:05:32
@Description: 
"""


def spam(a, b=42):
    print(a, b)


def spam_1(a, b=None):
    if b is None:
        b = []


_no_value = object()


def spam_2(a, b=_no_value):
    """
    请仔细区分不传递任何值和传递 None 之间的区别
    >>> spam(1)
    No b value supplied
    >>> spam(1, 2)
    >>> spam(1, None)
    """
    if b is _no_value:
        print("No b value supplied")
# 在函数中检测是否对可选参数提供了某个特定值
# （可以是任意值）。这里最为棘手的地方在于我们不能用 None、0 或者 False 当做默认值
# 来检测用户是否提供了参数（因为所有这些值都是完全合法的参数，用户极有可能将
# 它们当做参数）。因此，需要用其他的办法来检测。
# 参数 b 可以有值，比如说 0 或者 None
