"""
@Title: 保存最后 N 个元素
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-01 10:06:41
@Description: 
"""
from collections import deque


def search(lines, pattern, history: int = 5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


# TOREAD
if __name__ == '__main__':
    with open("somefile.txt") as f:
        for line, pre_lines in search(f, "Python", 5):
            for p_line in pre_lines:
                print(p_line, end='')
            print(line, end='')
            print("-" * 20)
