"""
@Description: 海龟画图
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-19 11:47:54
"""

import math
import turtle


def draw_circle_turtle(x, y, r):
    # 调用 up()。这告诉 Python 提笔。换句话说，让笔离开虚拟的纸，这样移动海龟也
    # 不会画图。开始绘图之前，先定位海龟。
    turtle.up()
    # 将海龟的位置设置为横轴上的第一个点：(x + r, y)
    turtle.setpos(x + r, y)
    # 调用 down()，放下笔
    turtle.down()

    for i in range(0, 365, 5):
        a = math.radians(i)
        turtle.setpos(x + r * math.cos(a), y + r * math.sin(a))


draw_circle_turtle(100, 100, 50)
# 调用 mainloop()，它保持 tkinter
# 窗口打开，让你可以欣赏你画的圆（Tkinter 是 Python 默认的 GUI 库）
turtle.mainloop()
