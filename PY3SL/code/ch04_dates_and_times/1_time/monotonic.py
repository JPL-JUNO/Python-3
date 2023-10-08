"""
@Title: 单调时钟
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-08 21:59:58
@Description: 反复调用 time() 所产生的值可能向前或向后
"""

import time

start = time.monotonic()
time.sleep(.1)
end = time.monotonic()

print('start :{:>9.2f}'.format(start))
print('end   :{:>9.2f}'.format(end))
print('span  :{:>9.2f}'.format(end - start))
# 单调时钟的起始值没有被定义
# 所以返回值只是在于其他时钟值完成计算时有用
