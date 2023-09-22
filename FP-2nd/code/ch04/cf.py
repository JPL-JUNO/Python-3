#!/usr/bin/env python3
"""
@Description: 字符查找使用脚本
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-11 13:41:14
"""
import sys
import unicodedata

START, END = ord(' '), sys.maxunicode + 1


def find(*query_words, start=START, end=END):
    query = {w.upper() for w in query_words}
    for code in range(start, end):
        char = chr(code)  # 获取 code 对应的 Unicode 字符
        name = unicodedata.name(char, None)  # 获取字符的名称。如果码点不对应任何字集，则返回 None
        if name and query.issubset(name.split()):
            print(f'U+{code:04X}\t{char}\t{name}')


def main(words):
    if words:
        find(*words)
    else:
        print('Please provide words to find')


if __name__ == '__main__':
    main(sys.argv[1:])
