"""
@File         : item20.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-04-20 22:04:43
@Email        : cuixuanstephen@gmail.com
@Description  : 遇到意外情况时应该抛出异常，不要返回 None
"""


def careful_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


x, y = 1, 0
result = careful_divide(x, y)
if result is None:
    print("Invalid inputs")

x, y = 0, 5
result = careful_divide(x, y)
if not result:
    print("Invalid inputs")


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
    print("Invalid inputs")


def careful_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("Invalid inputs")


x, y = 5, 2
try:
    result = careful_divide(x, y)
except ValueError:
    print("Invalid inputs")
else:
    print(f"Result is {result:.1f}")


def careful_divide(a: float, b: float) -> float:
    """Divides a by b.

    Raises
    ------
    `ValueError`
        When the inputs cannot be divided.
    """
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("Invalid inputs")
