"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-12 16:03:37
@Description: 
"""
from re_test_patterns import test_patterns
# re 在匹配模式时通常会尽可能多地消费输入，这种所谓的贪心行为可能会导致单个匹配减少，
# 或者匹配结果可能包含比预想更多的输入文本
# 可以在重复指令后加 ? 来关闭这种贪心行为
test_patterns(
    'abbaabbba',
    [("ab*?", 'a followed by zero or more b'),  # 对于允许 b 出现 0 次的模式
     # 如果消费输入时金庸贪心行为，那么这意味着匹配的子串不会包含任何 b 字符
     ("ab+?", "a followed by one or more b"),
     ("ab??", "a followed by zero or one b"),
     ("ab{3}?", "a followed by three b"),
     ("ab{2,3}?", "a followed by two to three b")]
)
