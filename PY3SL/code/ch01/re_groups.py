"""
@Title: 用组解析匹配 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-12 21:12:44
@Description: 
"""

from re_test_patterns import test_patterns

test_patterns(
    "abbaaabbbbaaaaa",
    # 可以用圆括号包围模式来定义组
    [("a(ab)", "a followed by literal ab"),
     ("a(a*b*)", "a followed by 0-n a and 0-n b"),
     ("a(ab)*", "a followed by 0-n ab"),
     ("a(ab)+", "a followed by 1-n ab")]
)
