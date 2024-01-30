"""
@File         : scope_details.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-01-27 23:18:26
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

# 全局 x
x = [10, 11]


def outer():
    # x 是 outer 作用域下的
    x = [999, 998]

    def inner():
        # x 是 inner 作用域下的
        x = [-999, -998]
        return x

    inner()
    return x


outer()
assert x == [10, 11]

X = [1, 2, 3, 4]


def in_place_changes():
    # in-place changes to objects do not classify names as locals;
    # only actual name assignments do.
    X.append(5)
    # 有预感，这种写法会导致很大的 bug


in_place_changes()
assert X == [1, 2, 3, 4, 5]
