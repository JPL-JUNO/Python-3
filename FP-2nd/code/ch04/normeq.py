"""

"""

"""
@Description: 比较规范化 Unicode 字符串，准确比较
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-10 13:06:30

比较规范化 Unicode 字符串，准确比较
使用 NFC 规范化形式，区分大小写：

>>> s1 = 'café'
>>> s2 = 'cafe\u0301'
>>> s1 == s2
False
>>> nfc_equal(s1, s2)
True
>>> nfc_equal("A", 'a')
False

使用 NFC 规范化形式，大小写同一化：

>>> s3 = 'Straße'
>>> s4 = 'strasse'
>>> s3 == s4
False
>>> nfc_equal(s3, 
False
>>> fold_equal(s3, s4)
True
>>> fold_equal(s1, s2)
True
>>> fold_equal("A", "a")
True
"""

from unicodedata import normalize


def nfc_equal(str1, str2):
    return normalize('NFC', str1) == normalize('NFC', str2)


def fold_equal(str1, str2):
    return (normalize('NFC', str1).casefold() == normalize('NFC', str2).casefold())


if __name__ == '__main__':
    s1 = 'café'
    s2 = 'cafe\u0301'
    print(s1 == s2)
    assert nfc_equal(s1, s2)
    print(nfc_equal("A", 'a'))

    s3 = 'Straße'
    s4 = 'strasse'
    print(s3 == s4)
    print(nfc_equal(s3, s4))
    assert fold_equal(s3, s4)
    assert fold_equal(s1, s2)
    assert fold_equal("A", "a")
