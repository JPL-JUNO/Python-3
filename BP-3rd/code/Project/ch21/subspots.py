"""
@Title: 最终的太阳黑子程序
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-06 10:45:44
@Description:
"""

from urllib.request import urlopen
from reportlab.lib import colors
from reportlab.graphics.shapes import String, Drawing
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics import renderPDF

URL = "https://services.swpc.noaa.gov/json/solar-cycle/predicted-solar-cycle.json"
COMMENT_CHARS = '#:'

import json

# 在线读取
# for data in urlopen(URL).readlines():
#     data = json.loads(data.decode())


# 读取本地
with open("./predicted-solar-cycle.json") as f:
    for line in f.readlines():
        data = json.loads(line)

data = [[int(row["time-tag"][:4]), int(row["time-tag"][-2:]), row["predicted_ssn"], row["high_ssn"], row["low_ssn"]]
        for row in data]

pred = [row[2] for row in data]
high = [row[3] for row in data]
low = [row[4] for row in data]
times = [row[0] + row[1] / 12.0 for row in data]
lp = LinePlot()
lp.x = 50
lp.y = 50
lp.height = 125
lp.width = 300
lp.data = [list(zip(times, pred)),
           list(zip(times, high)),
           list(zip(times, low)),]
lp.lines[0].strokeColor = colors.blue
lp.lines[1].strokeColor = colors.red
lp.lines[2].strokeColor = colors.green

drawing = Drawing()
drawing.add(lp)
drawing.add(String(250, 150, "Sunspots",
                   fontSize=14, fillColor=colors.red))
renderPDF.drawToFile(drawing, "report2.pdf", "Sunspots")
