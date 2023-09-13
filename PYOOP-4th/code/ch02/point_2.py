"""
@Title: Type hints and defaults
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-30 09:52:29
@Description: 类型提示与默认值
"""


class Point:
    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.move(x, y)

    # 如果参数太长，也可以这样写
    # def __init__(self,
    #              x: float = 0,
    #              y: float = 0) -> None:
    #     self.move(x, y)

    def move(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
