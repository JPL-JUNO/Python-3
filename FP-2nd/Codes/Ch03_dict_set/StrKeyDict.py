"""
@Description: 子类应继承UserDict而不是dict
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-07-04 13:36:43
"""
# It’s better to create a new mapping type
# by extending collections.UserDict rather than dict.

import collections


class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        # UserDict没有继承dict，使用的是组合模式
        # data是dict的实例，存放具体的项
        return str(key) in self.data

    def __setitem__(self, key, item) -> None:
        self.data[str(key)] = item
