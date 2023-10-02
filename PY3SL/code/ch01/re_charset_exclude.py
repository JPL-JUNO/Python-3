"""
@Title: 尖字符^意味着要查找不在这个尖字符后面的集合中的字符
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-12 16:48:03
@Description: 
"""

from re_test_patterns import test_patterns

test_patterns(
    "This is some text -- with punctuation",
    [('[^-. ]+', "sequences without -, ., or space")]
)
