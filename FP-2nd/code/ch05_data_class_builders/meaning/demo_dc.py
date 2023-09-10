"""
@Title: 一个使用 @dataclass 装饰的类 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-10 19:53:37
@Description: 
"""

from dataclasses import dataclass


@dataclass
class DemoDataClass:
    a: int
    b: float = 1.1
    c = "spam"
