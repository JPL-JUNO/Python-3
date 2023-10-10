"""
@Title: 惰性生成器
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-10 21:07:04
@Description: 之前的版本因为提前将 words 作为属性，及早构成了文本中的单词列表
"""

# 本版本主要是依靠 re 模块来实现惰性，即利用 re.finditer 替代 re.findall

import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence:
    def __init__(self, text):
        self.text = text  # 不再需要 words 列表

    def __repr__(self):
        return f'Sentence({reprlib.repr(self.text)})'

    def __iter__(self):
        # RE_WORD.finditer() 返回一个 MatchObject 实例
        for match in RE_WORD.finditer(self.text):
            yield match.group()  # 从 MatchObject 实例中提取匹配的文本
