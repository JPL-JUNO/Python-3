"""
@Title: 定义带有额外状态的生成器函数
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-03 21:08:08
@Description: 
"""
from collections import deque


class LineHistory:
    def __init__(self, lines, hist_line: int = 3) -> None:
        self.lines = lines
        self.history = deque(maxlen=hist_line)

    def __iter__(self):
        for line_no, line in enumerate(self.lines, 1):
            self.history.append((line_no, line))
            yield line

    def clear(self):
        self.history.clear()


with open('example1.txt') as f:
    lines = LineHistory(f)
    for line in lines:
        if "python" in line:
            for line_no, h_line in lines.history:
                print("{}:{}".format(line_no, h_line), end="")
