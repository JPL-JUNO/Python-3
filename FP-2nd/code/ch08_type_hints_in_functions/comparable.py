"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-03 21:17:13
@Description: 
"""
from typing import Protocol, Any


class SupportsLessThan(Protocol):
    def __lt__(self, other: Any) -> bool:
        ...
