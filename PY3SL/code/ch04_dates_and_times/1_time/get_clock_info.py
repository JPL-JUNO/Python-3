"""
@Title: 比较时钟
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-08 21:41:52
@Description: 可以使用 get_clock_info() 获取当前实现的基本信息，包括时钟的分辨率
"""

import textwrap
import time

available_clocks = [
    # 被弃用了
    # ('clock', time.clock)
    ('process_time', time.process_time),
    ('monotonic', time.monotonic),
    ('perf_counter', time.perf_counter),
    ('process_time', time.process_time),
    ('time', time.time)
]

for clock_name, func in available_clocks:
    print(textwrap.dedent('''\
        {name}:
            adjustable    :{info.adjustable}
            implementation:{info.implementation}
            monotonic     : {info.monotonic}
            resolution    : {info.resolution}
            current       : {current}
        '''
                          ).format(name=clock_name,
                                   info=time.get_clock_info(clock_name),
                                   current=func())
          )
