"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-03 18:25:19
@Description: 
"""

import sys
import re
import unicodedata
from collections.abc import Iterable

RE_WORD = re.compile(r'\w+')
STOP_CODE = sys.maxunicode + 1


def tokenize(text: str) -> Iterable[str]:
    """return iterable of upper cased words"""
    for match in RE_WORD.finditer(text):
        yield match.group().upper()


def name_index(start: int = 32, end: int = STOP_CODE) -> dict[str, set[str]]:
    index: dict[str, set[str]] = {}

    for char in (chr(i) for i in range(start, end)):
        if name := unicodedata.name(char, ''):
            # assigns the result of the unicodedata.name() call to name,
            # and the whole expression evaluates to that result.
            for word in tokenize(name):
                index.setdefault(word, set()).add(char)
    return index
