"""
@Title: 几种类型提示
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-14 21:32:16
@Description: 
"""

# 1. Generic collections: set, list, dict
# set[int]
# list[int]
# dict[str, int]

# 2. The typing.NamedTuple definition lets us define new kinds of immutable
# tuples and provide useful names for the members.
from typing import NamedTuple

# 3. Python has type hints for file-related I/O objects.
from typing import TextIO, BinaryIO

# 4. create new types of strings by extending
from typing import Text

# 5. New numeric types often start with the numbers module as a source for built-
# in numeric functionality.
# import numbers
from numbers import Number
