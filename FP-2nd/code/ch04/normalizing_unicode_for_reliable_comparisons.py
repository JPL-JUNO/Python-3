"""
@Description: Normalizing Unicode for Reliable Comparisons
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-09 13:20:46
"""

s1 = 'café'
s2 = 'cafe\N{COMBINING ACUTE ACCENT}'
print(s1, s2)
assert len(s1) == 4
assert len(s2) == 5
assert not s1 == s2
# U+0301 是 COMBINING ACUTE ACCENT，加在“e”后面得到“é”。在 Unicode 标准中，'é' 和
# 'e\u0301' 这样的序列叫“标准等价物”（canonical equivalent），应用程序应该把它们视作
# 相同的字符。但是，Python 看到的是不同的码位序列，因此判定二者不相等。


# NFC（Normalization Form C）使用最少的码位构成等价的字符串，而 NFD 把组合字符分
# 解成基字符和单独的组合字符。这两种规范化方式都能让比较行为符合预期
from unicodedata import normalize
assert len(normalize('NFC', s1)) == 4
assert len(normalize('NFC', s2)) == 4

assert len(normalize('NFD', s1)) == 5
assert len(normalize('NFD', s2)) == 5

assert normalize('NFC', s1) == normalize('NFC', s2)
assert normalize('NFD', s1) == normalize('NFD', s2)

# 不过，安全起见，保存文本之前，最好使用 normalize('NFC', user_text) 规范化字符串
# 使用 NFC 时，有些单字符会被规范成另一个单字符
from unicodedata import name
ohm = '\u2126'
print(name(ohm))
ohm_c = normalize("NFC", ohm)
print(name(ohm_c))
assert not ohm == ohm_c
assert normalize("NFC", ohm) == normalize("NFC", ohm_c)

half = '\N{VULGAR FRACTION ONE HALF}'
print(half)
print(normalize('NFKC', half))
for char in normalize("NFKC", half):
    print(char, name(char), sep='\t')
four_squared = '4²'
print(normalize('NFKC', four_squared))
micro = 'µ'
micro_kc = normalize('NFKC', micro)
print(micro, micro_kc)
print((name(micro), name(micro_kc)))
