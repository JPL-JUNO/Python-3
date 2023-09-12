"""
@Title: 匹配转移字符
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-12 17:26:46
@Description: 
"""

from re_test_patterns import test_patterns

test_patterns(
    r"\d+ \D+ \s+",
    [(r"\\.\+", "escape code")]
)
# \\ 表示匹配 \
# \+ 表示匹配 +
