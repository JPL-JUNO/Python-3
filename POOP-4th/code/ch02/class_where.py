"""
@Title: 类可以定义在任何地方
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-31 20:27:23
@Description: 
"""

from typing import Optional


class Formatter:
    def format(self, string: str) -> str:
        pass


def format_string(string: str, formatter: Optional[Formatter] = None) -> str:
    """
    Format a string using the formatter object, which
    is expected to have a format() method that accepts
    a string.
    """
    class DefaultFormatter(Formatter):
        """Format a string in title case."""

        def format(self, string: str) -> str:
            return str(string).title()
    if not formatter:
        formatter = DefaultFormatter()
    return formatter.format(string)
