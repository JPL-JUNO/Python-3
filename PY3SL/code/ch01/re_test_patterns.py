"""
@Title: 模式语法
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-12 10:00:17
@Description: 
"""

import re


def test_patterns(text: str, patterns: list[tuple[str, str]]) -> None:
    for pattern, desc in patterns:
        print("'{}' ({})\n".format(pattern, desc))
        print("  '{}'".format(text))
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            substr = text[s:e]
            n_backslashes = text[:s].count('\\')
            prefix = "." * (s + n_backslashes)
            print("  {}'{}'".format(prefix, substr))
        print()
    return


if __name__ == "__main__":
    test_patterns("abbaaabbbaaaaa",
                  [("ab", "'a' followed by 'b'")])
