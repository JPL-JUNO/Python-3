"""
@Description: 去掉全部组合记号的函数
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-10 13:28:37
"""

import unicodedata
import string


def shave_marks(txt):
    """
    shave_marks 函数使用起来没问题，但是也许做得太多了。通常，去掉
    变音符号是为了把拉丁文本变成纯粹的 ASCII，但是 shave_marks 函数还会修改非拉丁字
    符（如希腊字母），而只去掉重音符并不能把它们变成 ASCII 字符。因此，我们应该分析
    各个基字符，仅当字符在拉丁字母表中时才删除附加的记号
    """
    # 把所有字符分解成基字符和组合记号
    norm_txt = unicodedata.normalize('NFD', txt)
    # 过滤所有组合记号
    shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c))
    # 重组所有字符
    return unicodedata.normalize('NFC', shaved)


def shave_marks_latin(txt):
    # 把所有字符分解成基字符和组合记号。
    norm_txt = unicodedata.normalize('NFD', txt)
    latin_base = False
    preserve = []
    for c in norm_txt:
        if unicodedata.combining(c) and latin_base:
            continue  # 忽略拉丁基字符上的变音符号
        preserve.append(c)
        # 如果不是组合字符，那就是新的基字符/
        if not unicodedata.combining(c):
            latin_base = c in string.ascii_letters
    shaved = ''.join(preserve)
    return unicodedata.normalize('NFC', shaved)


if __name__ == '__main__':
    order = '“Herr Voß: • ½ cup of Œtker™ caffè latte • bowl of açaí.”'
    # Only the letters “è”, “ç”, and “í” were replaced.
    print(shave_marks(order))
    Greek = 'Ζέφυρος, Zéfiro'
    print(shave_marks(Greek))  # Both “έ” and “é” were replaced.
