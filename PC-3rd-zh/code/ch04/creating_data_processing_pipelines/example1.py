"""
@Title: 生成器函数是一种实现管道机制的好方法
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-07 09:28:26
@Description: 我们想以流水线式的形式对数据进行迭代处理
"""

import os
import fnmatch
import gzip
import bz2
import re


def gen_find(filepat, top):
    """
    Find all filenames in a directory tree that match a shell wildcard pattern
    """
    for path, _, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path, name)


def gen_opener(filenames):
    """
    Open a sequence of filenames one at a time producing a file object.
    The file is closed immediately when proceeding to the next iteration.
    """
    for filename in filenames:
        if filename.endswith(".gz"):
            f = gzip.open(filename, 'rt')
        elif filename.endswith(".bz2"):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt')
        yield f
        # 迭代完关闭文件
        f.close()


def gen_concatenate(iterators):
    """Chain a sequence of iterators together into a single sequence."""
    for it in iterators:
        yield from it


def gen_grep(pattern, lines):
    """Look for a regex pattern in a sequence of lines"""
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line

# http://www.dabeaz.com/generators
