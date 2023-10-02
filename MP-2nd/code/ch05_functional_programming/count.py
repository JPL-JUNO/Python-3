"""
@Title: Infinite range with decimal steps
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-23 17:56:22
@Description: 与 range 类似，但是是无限的而且可以使用浮点
"""

import itertools
list(itertools.islice(itertools.count(), 10))

list(itertools.islice(itertools.count(), 5, 10, 2))

list(itertools.islice(itertools.count(10, 2.5), 5))
