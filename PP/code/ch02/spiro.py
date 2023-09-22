"""
@Description: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-19 13:29:16
"""
import turtle
import math
# fractions.gcd(a, b) has been moved to the math module in Python 3.9.
# from fractions import gcd
from math import gcd
import random
from datetime import datetime
from PIL import Image
import argparse


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
        self.set_params(xc, yc, col, R, r, l)
        self.restart()

    def set_params(self, xc, yc, col, R, r, l):
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

    def clear(self):
        # clear everything
        self.t.clear()


class SpiroAnimator:
    """我们同时绘制随机的螺线。该类使用一个计时器，每次绘制
    曲线的一段。这种技术定期更新图像，并允许程序处理事件，如按键、鼠标点击，等等。
    """

    def __init__(self, N):
        # 以毫秒为单位的时间间隔，将用于定时器
        self.delta_t = 10
        # 保存海龟窗口的尺寸
        self.width = turtle.window_width()
        self.height = turtle.window_height()
        self.spiros = []
        for _ in range(N):
            # 一个元组，需要传入到 Spiro 构造函数
            r_params = self.gen_random_params()
            # 创建一个新的 Spiro 对象，并将它添加到 Spiro 对象的列表中。
            # 用 Python 的*运算符将元组转换为参数列表
            spiro = Spiro(*r_params)
            self.spiros.append(spiro)
            # 设置 turtle.ontimer()方法每隔 DeltaT 毫秒调用 update()
            turtle.ontimer(self.update, self.delta_t)

    def gen_random_params(self):
        """"""
        width, height = self.width, self.height
        # 将 R 设置为 50 至窗口短边一半长度的随机整数
        R = random.randint(50, min(width, height) // 2)
        r = random.randint(10, 9 * R // 10)
        l = random.uniform(.1, .9)

        # 在屏幕边界内随机选择 x 和 y 坐标，选择屏幕上的一个随机点作为螺线的中心。
        xc = random.randint(-width // 3, width // 3)
        yc = random.randint(-height // 3, height // 3)

        # 设置为红、绿和蓝颜色的成分，为曲线指定随机的颜色。
        col = (random.random(), random.random(), random.random())
        return (xc, yc, col, R, r, l)

    def restart(self):
        for spiro in self.spiros:
            spiro.clear()
            r_params = self.gen_random_params()

            spiro.set_params(*r_params)
            spiro.restart()

    def update(self):
        """它由定时器调用，以动画的形式更新所有的 Spiro 对象"""
        # 使用一个计数器 n_complete 来记录已画的 Spiro 对象的数目
        n_complete = 0
        for spiro in self.spiros:
            spiro.update()
            if spiro.drawing_complete:
                n_complete += 1
        if n_complete == len(self.spiros):
            # 检查计数器，看看是否所有对象都已画完。如果已画完，调
            # 用 restart()方法重新开始新的螺线动画。
            self.restart()
        # 调用计时器方法，
        # 它在 delta_t 毫秒后再次调用 update()
        turtle.ontimer(self.update, self.delta_t)

    def toggle_turtles(self):
        """打开或关闭海龟光标。这可以让绘图更快。"""
        for spiro in self.spiros:
            if spiro.t.isvisible():
                spiro.t.hideturtle()
            else:
                self.t.showturtle()


def save_drawing():
    # 隐藏海龟光标，这样就不会在最后的图形中看到它
    turtle.hideturtle()
    # 利用当前时间和日期（以“日—月—年—时—分—秒”的格式），以生成图像文件的唯一名称
    data_str = (datetime.now()).strftime("%d%b%Y-%H%M%S")
    # 生成文件名
    file_name = "spiro-" + data_str
    print("Saving Drawing to %s.eps/png" % file_name)

    # 利用 tkinter的 canvas 对象，将窗口保存为嵌入式 PostScript（EPS）文件格式。由于 EPS 是矢
    # 量格式，你可以用高分辨率打印它
    canvas = turtle.getcanvas()
    canvas.postscript(file=file_name + '.eps')

    # PNG 用途更广，所以用 Pillow 打开
    # EPS 文件，并在行将它保存为 PNG 文件
    img = Image.open(file_name + '.eps')
    img.save(file_name + ".png", "png")
    # 取消隐藏海龟光标
    turtle.showturtle()


def main():
    print("Generating spirograph...")
    desc_str = """This program draws spirographs using the Turtle module
    When run with no arguments, this program draws random spirographs
    
    Terminology:
    
    R: radius of outer circle
    r: radius of inner circle
    l: ratio of hole distance to r
    """
    parser = argparse.ArgumentParser(description=desc_str)
    parser.add_argument("--s_params", nargs=3, dest="s_params", required=False,
                        help="The three arguments in s_params: R, r, l.")

    args = parser.parse_args()
    # 用 setup() 将绘图窗口的宽度设置为 80％的屏幕宽度
    # 设置光标形状为海龟
    turtle.setup(width=.8)
    turtle.shape("turtle")
    # 设置程序窗口的标题为 Spirographs
    turtle.title("Spirographs")
    # 利用 onkey()和 saveDrawing，在按下 S 时保存图画
    turtle.onkey(save_drawing, 's')
    # 调用 listen()让窗口监听用户事件
    turtle.listen()
    turtle.hideturtle()

    if args.s_params:
        # 检查是否有参数赋给 --s_params
        params = [float(x) for x in args.s_params]
        col = (.0, .0, .0)
        spiro = Spiro(0, 0, col, *params)
        spiro.draw()
    else:
        spiro_anim = SpiroAnimator(4)
        # 利用 onkey() 来捕捉按键 T，这样就可以用它来切换海龟光标（toggleTurtles）
        turtle.onkey(spiro_anim.toggle_turtles, 't')
        # 处理空格键（space），这样就可以用它在任何时候重新启动动画
        turtle.onkey(spiro_anim.restart, "space")

    turtle.mainloop()


if __name__ == '__main__':
    main()
