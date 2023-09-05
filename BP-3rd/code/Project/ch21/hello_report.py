"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-05 22:48:14
@Description: 
"""

from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics import renderPDF

d = Drawing(100, 100)
# 构造函数String的主要参数包括x坐标和y坐标以及文本。另外，你还可指定各种属性，如
# 字号、颜色等。在这里，我设置了参数textAnchor，它指定要将字符串的哪部分放在坐标指定
# 的位置。
s = String(50, 50, "Hello, world!", textAnchor="middle")
d.add(s)

renderPDF.drawToFile(d, "hello.pdf", "A simple PDF file")
