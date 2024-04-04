"""
@File         : sched_priority.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-01-19 21:17:22
@Email        : stephencuixuan@gmail.com
@Description  : 
"""

import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)


def print_event(name):
    print("Event:", time.ctime(time.time()), name)


now = time.time()
print("Start:", time.ctime(now))
scheduler.enterabs(now + 2, 2, print_event, ("first",))
scheduler.enterabs(now + 2, 1, print_event, ("second",))
scheduler.run()
