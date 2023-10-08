"""
@Title: 处理器时钟时间
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-08 22:04:47
@Description: 
@注意：clock() 已被弃用，采用 process_time() 替代
"""
import time
import hashlib

data = open(__file__, 'rb').read()
for i in range(5):
    h = hashlib.sha1()
    print(time.ctime(), ': {:0.3f} {:0.3f}'.format(
        time.time(), time.process_time()
    ))
    for i in range(300_000):
        h.update(data)
    cksum = h.digest()
