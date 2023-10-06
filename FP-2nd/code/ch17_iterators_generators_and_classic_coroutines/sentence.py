"""
@Title: a Sentence as a sequence of words
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-03 23:04:17
@Description: 所有的序列都可以迭代，不过现在要具体说明为什么
"""

import re
import reprlib

# \w 表示字母数字（转义码），+ 表示至少出现一次（重复）
RE_WORD = re.compile(r'\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        # 为了完善序列协议，实现了该方法，不过，为了让对象可以迭代，没必要实现这个方法
        return len(self.words)

    def __repr__(self):
        # reprlib.repr is a utility function to generate abbreviated string representations
        # of data structures that can be very large.
        return 'Sentence(%s)' % reprlib.repr(self.text)


s = Sentence('"The time has come," the Walrus said,')
print(s)
for word in s:
    # 表明可以支持迭代，稍后说明原因
    print(word)
