"""
@Description: 大小写统一化
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-10 13:00:23
"""

# 大小写折叠其实就是把所有文本变成小写，再做些其他转换。这个功能由 str.casefold()
# 方法（Python 3.3 新增）支持。
# 对于只包含 latin1 字符的字符串 s，s.casefold() 得到的结果与 s.lower() 一样，唯有两
# 个例外：微符号 'µ' 会变成小写的希腊字母“μ”（在多数字体中二者看起来一样）；德语
# Eszett（“sharp s”，ß）会变成“ss”。


from unicodedata import name
micro = 'µ'
print(name(micro))
micro_cf = micro.casefold()
print(name(micro_cf))
print((micro, micro_cf))

eszett = 'ß'
print(name(eszett))
eszett_cf = eszett.casefold()
print(eszett_cf)
print((eszett, eszett_cf))
