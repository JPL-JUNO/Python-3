"""
@File         : 2_3_thismod.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-01-28 13:57:02
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

var = 99


def local():
    var = 0  # Change local var


def glob1():
    global var  # Declare global (normal)
    var += 1  # Change global var


def glob2():
    var = 0  # Change local var
    import thismod  # Import myself

    thismod.var += 1  # Change global var


def glob3():
    var = 0  # Change local var
    import sys  # Import system table

    glob = sys.modules["thismod"]  # Get module object (or use __name__)
    glob.var += 1  # Change global var


def test():
    print(var)  # 99
    local()
    glob1()  # 100
    glob2()  # 101
    glob3()  # 102
    print(var)


if __name__ == "__main__":
    import thismod

    thismod.test()
    assert thismod.var == 102
