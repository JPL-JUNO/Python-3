"""
@Title: ArithmeticProgression 类
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-10 22:18:53
@Description: 
"""


class ArithmeticProgression:
    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end  # None -> 无穷数列

    def __iter__(self):
        # 获取 self.begin + self.step 的数据类型
        result_type = type(self.begin+self.step)
        result = result_type(self.begin)
        forever = self.end is None  # 是否是无穷数列
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin+self.step*index
