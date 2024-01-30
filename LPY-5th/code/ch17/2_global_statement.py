"""
@File         : 2_global_statement.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-01-28 13:32:03
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""
X = 88


def func():
    global X
    X = 99


func()
assert X == 99

y, z = 1, 2


def all_global():
    # x 在函数运行前的外围模块中甚至并不存在
    # 如果这样的话，
    # 函数内的第一条赋值语句将自动在模块中创建 x 这个变量
    global x
    x = y + z


all_global()
assert x == 3
