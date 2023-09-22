"""
@Description: BOM: 有用的鬼符
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-02 13:51:49
"""

u16 = 'El Niño'.encode('utf_16')
print(u16)
# b'\xff\xfe'
# 这是 BOM，即字节序标记（byte-order mark），指明编码时使用
# Intel CPU 的小字节序

print(list(u16))

# 显式指明使用小端序
u16le = 'El Niño'.encode('utf_16le')
# 显式指明使用大端序
u16be = 'El Niño'.encode('utf_16be')
print(list(u16le))
print(list(u16be))
