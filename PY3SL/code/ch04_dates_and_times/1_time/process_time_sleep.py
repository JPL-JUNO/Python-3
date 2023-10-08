"""
@Title: 处理器时间
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-08 22:09:21
@Description: 一般情况下，如果程序什么也没有做，则处理器时钟不会 “滴答”（tick）
"""

import time
template = '{} - {:.2f} - {:.2f}'

print(template.format(
    time.ctime(), time.time(), time.process_time()
))

for i in range(3, 0, -1):
    print('Sleeping', i)
    time.sleep(i)
    print(template.format(
        time.ctime(), time.time(), time.process_time()
    ))

# 本例中，循环几乎不做什么，每次迭代后都会睡眠，
# 应用睡眠时，time() 值会增加，而 process_time() 的值不会增加

# 调用 sleep() 会从当前线程交出控制，并要求这个线程等待系统再次将其唤醒。
# 如果程序只有一个线程，则这个函数实际上会阻塞应用，使它不做任何工作
