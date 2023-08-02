"""
@Description: 处理 UnicodeEncodeError
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-02 13:21:39
"""
city = 'São Paulo'
city.encode('utf_8')

city.encode('utf_16')

city.encode('iso8859_1')

try:
    city.encode('cp437')
except UnicodeEncodeError:
    print("'cp437' 无法编码 'ã'（带波形符的'a'）。默认的错误处理方式 'strict' 抛出 UnicodeEncodeError。")

# error='ignore' 处理方式悄无声息地跳过无法编码的字符；这样做通常很是不妥。
city.encode('cp437', errors='ignore')
# 编码时指定 error='replace'，把无法编码的字符替换成 '?'；
# 数据损坏了，但是用户知道出了问题。
city.encode('cp437', errors='replace')
# 把无法编码的字符替换成 XML 实体，如果你无法使用 UTF，而且不想丢失数据，那么这就是唯一的选择
city.encode('cp437', errors='xmlcharrefreplace')
