"""
@Description: 创建 GUI 示例应用程序
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-17 10:07:16
"""

import tkinter as tk
# 要创建GUI，可创建一个将充当主窗口的顶级组件（控件）
top = tk.Tk()
btn = tk.Button()
# 现在这个按钮是不可见的——你需要使用布局管理器（也叫几何体管理器）来告诉 Tkinter
# 将它放在什么地方。
btn.pack()
# 控件包含各种属性，我们可以使用它们来修改控件的外观和行为。可像访问字典项一样访问
# 属性，因此要给按钮指定一些文本，只需使用一条赋值语句即可。
btn['text'] = "Click me!"


def clicked():
    print("I was clicked!")


btn['command'] = clicked
# 可以不分别给属性赋值，而使用方法config同时设置多个属性。
btn.config(text="Click me!", command=clicked)
# 还可使用控件的构造函数来配置控件。
tk.Button(text="Click me!", command=clicked).pack()
tk.Label(text="I'm in the first window!").pack()
second = tk.Toplevel()
tk.Label(second, text="I'm in the second window!").pack()
# 在常规程序中，我们将调用函数mainloop以进入Tkinter主事件循环，
# 而不是直接退出程序。

# 没有提供任何参数时，pack 从窗口顶部开始将控件堆叠成一列，并让它们在窗口中水平居中。
# 幸可调整控件的位置和拉伸方式。要指定将控件停靠在哪一条边上，可将参数 side 设置为
# LEFT、RIGHT、TOP或 BOTTOM。要让控件在 x 或 y 方向上填满分配给它的空间，可将参数 fill 设置为 X、
# Y 或 BOTH。要让控件随父控件（这里是窗口）一起增大，可将参数 expand 设置为 True。
for i in range(10):
    tk.Button(text=i).pack()
# help(Pack.config)
# help(Grid.configure)
# help(Place.config)

# 事件处理
top = tk.Tk()

# 可通过设置属性command给按钮指定动作（action）


def callback(event):
    print(event.x, event.y)


# <Button-1>是使用鼠标左按钮（按钮1）单击的事件名称。我们将这种事件关联到函数
# callback
top.bind("<Button-1>", callback)


tk.mainloop()
