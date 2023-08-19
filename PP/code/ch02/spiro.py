"""
@Description: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-19 13:29:16
"""
import turtle
import math
from fractions import gcd


class Spiro:
    # 构造函数
    def __init__(self, xc, yc, col, R, r, l):
        # 创建一个新的 turtle 对象，这将有助于我们同时绘制多条螺线
        self.t = turtle.Turtle()
        # 将光标的形状设置为海龟
        self.t.shape("turtle")

        # 将参数绘图角度的增量设置为 5 度
        self.step = 5
        # 设置了一个标志，将在动画中使用它，它会产生一组螺线。
        self.drawing_complete = False
        self.setparams(xc, yc, col, R, r, l)
        self.restart()

    def setparams(self, xc, yc, col, R, r, l):
        # 设置函数
        self.xc = xc
        self.yc = yc
        # R, r分别是万花尺模型中的大圆半径和小圆半径
        self.R = int(R)
        self.r = int(r)
        # l 是 线段 PC 与小圆半径 r 的比值
        self.l = l
        self.col = col
        # 计算 GCD 值，即 r/R 中分子分母的最大公约数
        gcd_val = gcd(self.r, self.R)
        # 确定曲线的周期性
        self.n_rot = self.r // gcd_val
        # 半径比
        self.k = r / float(R)
        self.t.color(*col)
        # 保存当前的角度
        self.a = 0

    def restart(self):
        """重置 Spiro 对象的绘制参数"""
        # 确定绘图是否已经完成
        self.drawing_complete = False
        # 显示海龟光标，以防它被隐藏
        self.t.showturtle()
        # 行提起笔，这样就可以在移动到第一个位置而不画线
        self.t.up()
        # 前往第一个点
        R, k, l = self.R, self.k, self.l
        a = 0.0
        x = R * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k))
        y = R * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k))
        self.t.setpos(self.xc + x, self.yc + y)
        self.t.down()

    def draw(self):
        """用连续的线段绘制该曲线"""
        R, k, l = self.R, self.k, self.l
        # 360 乘以 n_rot
        for i in range(0, 360 * self.n_rot + 1, self.step):
            # 计算参数 i 的每个值对应的 X 和 Y 坐标
            a = math.radians(i)
            x = R * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k))
            y = R * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k))
            self.t.setpos(self.xc + x, self.yc + y)
        # 隐藏光标，因为我们已完成绘制
        self.t.hideturtle()

    def update(self):
        """展示了一段一段绘制曲线来创建动画时所使用的绘图方法"""
        # 检查是否完成标志
        if self.drawing_complete:
            return
        # 增加当前的角度
        self.a += self.step

        R, k, l = self.R, self.k, self.l
        a = math.radians(self.a)
        x = self.R * ((1 - k) * math.cos(a) + l *
                      k * math.cos((1 - k) * a / k))
        y = self.R * ((1 - k) * math.sin(a) + l *
                      k * math.sin((1 - k) * a / k))
        self.t.setpos(self.xc + x, self.yc + y)
        # 在一定的角度后，万花尺的图案开始重复。在行，检查角度是否达这条特定曲线计算的完整范围。如果是这样，
        # 就设置 drawing_complete 标志，因为绘图完成了。
        if self.a >= 360 * self.n_rot:
            self.drawing_complete = True
            self.t.hideturtle()
