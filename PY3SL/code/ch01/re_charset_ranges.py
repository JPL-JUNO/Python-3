"""
@Title: 字符集
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-12 17:06:50
@Description: 
"""
from re_test_patterns import test_patterns

test_patterns(
    "This is some text -- with punctuation.",
    [("[a-z]+", "sequences of lowercase letters"),
     ("[A-Z]+", "sequences of lowercase letters"),
     ("[a-zA-Z]+", "sequences of lower- or uppercase letters"),
     ("[A-Z][a-z]+", "one uppercase followed by lowercase")]
)
