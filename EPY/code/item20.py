"""
@Title: Item 20: Prefer Raising Exceptions to Returning None
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-17 20:48:28
@Description: 
"""


def careful_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


x, y = 1, 0
result = careful_divide(x, y)
if result is None:
    # 这样是可以的没问题的，但是有些时候直接来判断
    # if not result
    # 会出现大的问题
    print("Invalid inputs")

x, y = 0, 5
result = careful_divide(x, y)
if not result:
    # 这样是可以运行的，但是它是不正确的
    # 它只是返回的结果为 0，但是
    print(
        "如果使用 not result 来判断会导致一些不必要的问题（应该 0, '', [], None 都会判定为 False）"
    )

# 改进的方法


def careful_divide(a, b):
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None


success, result = careful_divide(x, y)
if not success:
    print("Invalid inputs")

_, result = careful_divide(x, y)
if not result:
    print("改进方法一缺点：如果调用者使用 _ 拆解返回的值，那么同样会产生难以察觉的错误")


def careful_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError("Invalid inputs")


x, y = 5, 2
try:
    result = careful_divide(x, y)
except ValueError:
    print("Invalid inputs")
else:
    print("Result is %.1f" % result)


def careful_divide(a: float, b: float) -> float:
    """Divides a by b.

    Parameters
    ----------
    a : float
        _description_
    b : float
        _description_

    Returns
    -------
    float
        _description_

    Raises
    ------
    ValueError
        如果分母为 0，那么将会 raise
    """
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError("Invalid inputs")


# Functions that return None to indicate special meaning are error prone
# because None and other values (e.g., zero, the empty string)
# all evaluate to False in conditional expressions.

# Raise exceptions to indicate special situations instead of returning None.
# Expect the calling code to handle exceptions properly when they’re documented.

# Type annotations can be used to make it clear that
# a function will never return the value None, even in special situations.
