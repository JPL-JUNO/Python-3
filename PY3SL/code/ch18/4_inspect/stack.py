"""
@Title: stack.py
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-29 15:25:48
@Description: 
"""

import inspect
import pprint


def show_stack():
    for level in inspect.stack():
        print("{}[{}]\n  ->  {}".format(
            level.frame.f_code.co_filename,
            level.lineno,
            level.code_context[level.index].strip(),
        ))

        pprint.pprint(level.frame.f_locals)
        print()


def recurse(limit):
    local_variable = "." * limit
    if limit <= 0:
        show_stack()
        return
    recurse(limit - 1)
    return local_variable


if __name__ == "__main__":
    recurse(2)
