"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-10 14:00:24
@Description: 
"""

import typing


class DemoNTClass(typing.NamedTuple):
    a: int
    b: float = 1.1
    c = "spam"
