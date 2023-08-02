"""
@Description: 字节概要
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-02 12:56:08
"""

cafe = bytes('café', encoding='utf-8')
print(cafe)

# bytes 或 bytearray 对象的各个元素是介于 0~255（含）之间的整数
assert cafe[0] == 99
assert cafe[:1] == b'c'

cafe_arr = bytearray(cafe)

print(cafe_arr)
# bytearray 对象没有字面量句法，而是以 bytearray() 和字节序列字面量参数的形式显示
print(cafe_arr[-1:])


# 二进制序列有个类方法是 str 没有的，名为 fromhex，
# 它的作用是解析十六进制数字对
# （数字对之间的空格是可选的），构建二进制序列：
print(bytes.fromhex('31 4B CE A9'))

import array
# 指定类型代码 h, 创建一个短整数（16位）数组
numbers = array.array('h', [02, -1, 0, 1, 2])
octets = bytes(numbers)
# 使用缓冲类对象创建 bytes 或 bytearray 对象时，始终复制源对象中的字节序列。
print(octets)

