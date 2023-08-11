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


"""
@Description: 把一些西文印刷字符转换成 ASCII 字符集
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-11 13:04:53
"""

# 构建字符到字符的替换映射
single_map = str.maketrans("""‚ƒ„ˆ‹‘’“”•–—˜›""",
                           """'f"^<''""---~>""")

# 构建字符到字符串的替换映射表
multi_map = str.maketrans({
    '€': 'EUR',
    '…': '...',
    'Æ': 'AE',
    'æ': 'ae',
    'Œ': 'OE',
    'œ': 'oe',
    '™': '(TM)',
    '‰': '<per mille>',
    '†': '**',
    '‡': '***',
})

# 合并两种映射表
multi_map.update(single_map)
# print(multi_map)


def dewinize(txt):
    """把cp1252符号替换为ASCII字符或字符序列"""
    return txt.translate(multi_map)


def asciize(txt):
    """"""
    no_marks = shave_marks_latin(dewinize(txt))  # 调用 dewinize 函数，再去掉变音符
    no_marks = no_marks.replace('ß', 'ss')
    return unicodedata.normalize('NFKC', no_marks)


if __name__ == '__main__':
    order = '“Herr Voß: • ½ cup of Œtker™ caffè latte • bowl of açaí.”'
    # Only the letters “è”, “ç”, and “í” were replaced.
    print(shave_marks(order))
    Greek = 'Ζέφυρος, Zéfiro'
    print(shave_marks(Greek))  # Both “έ” and “é” were replaced.
    print(dewinize(order))
    print(asciize(order))
