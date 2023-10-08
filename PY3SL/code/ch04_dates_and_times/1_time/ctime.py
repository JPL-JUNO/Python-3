"""
@Title: 墙上时钟时间
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-08 21:55:50
@Description: 要记录或打印时间 ctime() 可能是更好的选择
"""

# 浮点是表示对于存储或比较日期很有用，但是对于生成人类可读的表示就有点差强人意了

import time
print('The time is     :', time.ctime())
later = time.time() + 15
# 格式化一个时间值
print('15 sec from now :', time.ctime(later))
