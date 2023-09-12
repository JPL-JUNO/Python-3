"""
@Title: 锚定
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-12 20:25:22
@Description: 
"""

from re_test_patterns import test_patterns

test_patterns(
    "This is some text -- with punctuation",
    [
        (r"^\w+", "word at start of string, excluding alphanumeric"),
        (r"\A\w+", "word at start of sting"),
        (r"\w+\S*$", "word near end of string"),
        (r"\w+\S*\Z", "word near end of string"),
        (r"\w*t\w*", "word containing t"),
        (r"\bt\w+", "t at start fo word"),
        (r"\w+t\b", "t an end of word"),
        (r"\Bt\B", "t, not start or end of word"),
    ]
)
