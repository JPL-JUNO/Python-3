"""
@Title: 一个文本块生成器
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-05 15:01:23
@Description: 
"""


def lines(file):
    """
    成器 lines 是个简单的工具，在文件末尾添加一个空行
    """
    for line in file:
        yield line
    yield '\n'


def blocks(file):
    """
    生成文本块时，将其包含的所有行合并，并将两端多余的空白（如列表项缩进和换行符）
    删除，得到一个表示文本块的字符串    
    """
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            # 用空字符将 block 连接起来
            yield ''.join(block)
            block = []
