"""
@File         : 1_3_scope_example.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-01-27 23:42:56
@Email        : cuixuanstephen@gmail.com
@Description  : 作用域实例
"""
# Global scope
X = 99  # X and func assigned in module: global


def func(Y):  # Y and Z assigned in function: locals
    Z = X + Y  # X is a global
    return Z


assert func(1) == 100
