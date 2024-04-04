"""
@File         : sched_overlap.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-01-19 21:06:41
@Email        : stephencuixuan@gmail.com
@Description  : 
"""

import sched, time

scheduler = sched.scheduler(time.time, time.sleep)


def long_event(name):
    print(f"Begin event :", time.ctime(time.time()), name)
    time.sleep(5)
    print("Finish event :", time.ctime(time.time()), name)


print("Start:", time.ctime(time.time()))
scheduler.enter(2, 1, long_event, ("first",))
scheduler.enter(3, 1, long_event, ("second",))

scheduler.run()
