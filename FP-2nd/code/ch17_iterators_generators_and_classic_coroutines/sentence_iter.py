"""
@Title: Sentence implemented using the Iterator pattern
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-09 21:50:51
@Description: 
"""

import re
import reprlib
RE_WORD = re.compile(r'\w+')


class Sentence:
    """可迭代的类"""

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return f'Sentence({reprlib.repr(self.text)})'

    def __iter__(self):
        """根据迭代协议，__iter__ 方法实例化并返回一个迭代器"""
        return SentenceIterator(self.words)


class SentenceIterator:
    """标准的迭代器"""

    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word

    def __iter__(self):
        """以便在预期可迭代对象的地方使用迭代器"""
        return self
