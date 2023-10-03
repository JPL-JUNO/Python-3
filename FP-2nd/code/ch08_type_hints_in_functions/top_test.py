"""
@Title: partial listing of the test suite for top
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-03 21:25:30
@Description: 
"""

from collections.abc import Iterator
# 这个常量在运行时始终为 False
# 不过类型检查工具在做类型检查时会假装值为 True
from typing import TYPE_CHECKING

import pytest

from top import top

# several lines omitted


def test_top_tuples() -> None:
    fruit = 'mango pear apple kiwi banana'.split()
    # 显示声明类型，不显示声明的话，mypy也可以推导出来，与显示声明的类型是相容的
    series: Iterator[tuple[int, str]] = (
        (len(s), s) for s in fruit
    )
    length = 3
    expected = [(6, 'banana'), (5, 'mango'), (5, 'apple')]
    result = top(series, length)
    if TYPE_CHECKING:
        # reveal_type() 不能在运行时调用，因为它不是常规函数
        # 而是 mypy 提供的调试设施，因此无须使用 import 导入
        # mypy 每遇到一个伪函数调用 reveal_type 就输出一个调试信息，显示参数的推导类型
        reveal_type(series)
        reveal_type(expected)
        reveal_type(result)
    assert result == expected

# intentional type error


def test_top_objects_error() -> None:
    series = [object() for _ in range(4)]
    if TYPE_CHECKING:
        reveal_type(series)
    with pytest.raises(TypeError) as excinfo:
        top(series, 3)
    assert "'<' not supported" in str(excinfo.value)
