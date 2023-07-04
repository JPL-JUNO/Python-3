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
    pass
