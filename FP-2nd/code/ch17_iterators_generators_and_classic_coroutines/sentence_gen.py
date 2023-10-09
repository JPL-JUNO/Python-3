"""
@Title: Sentence implemented using a generator
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-09 22:27:02
@Description: 
"""

import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        """本例中，迭代器其实是生成器对象，每次调用 __iter__ 方法都会自动创建，
        因为这里的 __iter__ 方法是生成器函数"""
        # 迭代 self.words
        for word in self.words:
            # 产出当前的 word
            yield word
        return
    # 这个 return 语句不是必要的；这个函数可以直接“落空”，自动返回。
    # 不管有没有return 语句，生成器函数都不会抛出 StopIteration 异常，
    # 而是在生成完全部值之后会直接退出。
