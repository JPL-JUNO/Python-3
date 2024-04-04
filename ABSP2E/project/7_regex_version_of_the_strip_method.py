"""
@File         : 7_regex_version_of_the_strip_method.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-13 22:46:21
@Email        : cuixuanstephen@gmail.com
@Description  : strip() 的正则表达式版本
"""

import re


def strip_regex(text, rm_str=None):
    begin_blank_regex = re.compile(r"(^\s*)")
    end_blank_regex = re.compile(r"(\s*$)")
    start_removed = begin_blank_regex.sub("", text)
    end_removed = end_blank_regex.sub("", start_removed)
    if rm_str is None:
        return end_removed
    else:
        rm_str_regex = re.compile(rm_str)
        return rm_str_regex.sub("", end_removed)


if __name__ == "__main__":
    print(strip_regex("  abcdef  "))
    print("  abcdef  ")
    print(strip_regex("  abcdef  ", "a"))
    print(strip_regex("  abcdef  ", "c"))
