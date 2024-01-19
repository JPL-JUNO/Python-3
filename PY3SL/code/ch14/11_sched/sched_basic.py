"""
@File         : sched_basic.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-01-19 20:37:11
@Email        : stephencuixuan@gmail.com
@Description  : 
"""

import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)


def print_event(name, start):
    now = time.time()

    elapsed = int(now - start)

    print(f"Event: {time.ctime(now)} elapsed={elapsed} name={name}")


start = time.time()
print("Start:", time.ctime(start))
scheduler.enter(2, 1, print_event, ("first", start))
scheduler.enter(3, 1, print_event, ("second", start))

scheduler.run()
