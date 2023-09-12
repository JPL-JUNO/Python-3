"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-12 22:06:45
@Description: 
"""
import re


def test_patterns(text, patterns):
    for pattern, desc in patterns:
        print("{!r} ({})\n".format(pattern, desc))
        print("  {!r}".format(text))

        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            prefix = " " * (s)
            print(
                "  {}{!r}{} ".format(prefix, text[s:e],
                                     " " * (len(text) - e)),
                end=' '
            )
            # 组本身是一个完整的正则表达式，
            # 可以嵌套在其他组中来创建更复杂的表达式
            # 这个 groups 里面放的是啥
            # () 圆括号里面的匹配
            # group(0)是全部，group(1)是第一组，因此这里的结果使用重复串的
            print(match.groups())
            if match.groupdict():
                print("{}{}".format(
                    " " * (len(text) - s),
                    match.groupdict()
                ))
        print()
    return


test_patterns(
    'abbaabbba',
    # (a*) 匹配一个空串
    [(r'a((a*)(b*))', 'a followed by 0-n a and 0-n b')],
)
