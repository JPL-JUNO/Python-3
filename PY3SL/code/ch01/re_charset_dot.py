"""
@Title: 元点符号（.）指示模式应当匹配该位置的单个字符
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-12 17:11:27
@Description: 
"""

from re_test_patterns import test_patterns
test_patterns(
    "abbaabbba",
    [('a.', 'a followed by any one character'),
     ('b.', 'b followed by any one character'),
     ('a.*b', 'a followed by anything, ending in b'),
     ('a.*?b', 'a followed by anything, ending in b, not greedy')]
)
