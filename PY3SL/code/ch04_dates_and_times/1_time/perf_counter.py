"""
@Title: 性能计数器
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-08 22:40:50
@Description: 
"""

import hashlib
import time

data = open(__file__, 'rb').read()

loop_start = time.perf_counter()

for i in range(5):
    iter_start = time.perf_counter()
    h = hashlib.sha1()
    for i in range(300_000):
        h.update(data)
    cksum = h.digest()
    now = time.perf_counter()
    loop_elapsed = now - loop_start
    iter_elapsed = now - iter_start

    print(time.ctime(), ': {:.3f}'.format(
        iter_elapsed, loop_elapsed
    ))
