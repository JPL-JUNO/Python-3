"""
@File         : exception_details.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-11 18:44:28
@Email        : cuixuanstephen@gmail.com
@Description  : 异常的详细信息
"""

import traceback, sys


def grail(x):
    raise TypeError("already got one")


try:
    grail("arthur")
except:
    exc_info = sys.exc_info()
    print(exc_info[0])
    print(exc_info[1])
    traceback.print_tb(exc_info[2])
