"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-31 14:25:43
@Description: 
"""


from typing import Any


class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, name):
        return getattr(self._obj, name)

    def __setattr__(self, name: str, value: Any) -> None:
        if name.startswith("_"):
            # Call original __setattr__
            # super()即使在没有显式列出基类的情况下也是可以工作的。
            super().__setattr__(name, value)
        else:
            setattr(self._obj, name, value)
