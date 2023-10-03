"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-03 18:41:11
@Description: 
"""
from collections.abc import Iterable
from typing import TypeAlias
FromTo = tuple[str, str]
# 从 3.10 之后的首选方式
# FromTo: TypeAlias = tuple[str, str]


def zip_replace(text: str, changes: Iterable[FromTo]) -> str:
    for from_, to in changes:
        text = text.replace(from_, to)
    return text


l33t = [('a', '4'), ('e', '3'), ('i', '1'), ('o', '0')]
text = 'mad skilled noob powned leet'
zip_replace(text, l33t)
