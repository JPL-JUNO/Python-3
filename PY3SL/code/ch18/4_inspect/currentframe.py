"""
@Title: 栈与帧
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-29 15:07:52
@Description: 
"""

import inspect
import pprint


def recurse(limit, keyword="default", *, kwonly="must be named"):
    local_variable = '.' * limit
    keyword = "change value of argument"
    frame = inspect.currentframe()
    print("line {} of {}".format(frame.f_lineno,
                                 frame.f_code.co_filename))
    print("locals:")
    # recurse() 的参数值被包含在帧的局部变量字典中
    pprint.pprint(frame.f_locals)
    print()
    if limit <= 0:
        return
    recurse(limit - 1)
    return local_variable


if __name__ == "__main__":
    recurse(2)
