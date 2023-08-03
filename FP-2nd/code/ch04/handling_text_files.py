"""
@Description: 处理文本文件
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-03 13:23:08
"""
# open('cafe.txt', 'w', encoding='utf_8').write('café')
# print(open('cafe.txt').read())

fp = open('cafe.txt', 'w', encoding='utf_8')
print(fp)

assert fp.write('café') == 4
fp.close()

import os
assert os.stat('cafe.txt').st_size == 5

fp2 = open('cafe.txt')
print(fp2)
print(fp2.encoding)
print(fp2.read())

fp3 = open('cafe.txt', encoding='utf_8')
print(fp3)
print(fp3.read())

# 'rb' 标志指明以二进制模式读取文件
fp4 = open('cafe.txt', 'rb')
print(fp4)
print(fp4.read())
# 除非想判断编码，否则不要在二进制模式中打开文本文件；即便如此，也应
# 该使用 Chardet，而不是重新发明轮子。常规代码只应该使
# 用二进制模式打开二进制文件，如光栅图像。
