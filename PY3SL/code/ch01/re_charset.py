"""
@Title: 字符集
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-12 16:42:50
@Description: 
"""

from re_test_patterns import test_patterns

test_patterns(
    "abbaabbba",
    [
        ("[ab]", "either a or b"),
        # a[ab]+ 会消费整个字符串，因为第一个字母是 a，而且后学的各个字符要么是 a 要么是 b
        ("a[ab]+", "a followed by 1 or more a or b"),
        ("a[ab]+?", "a followed by 1 or more a or b, not greedy"),
    ]
)
