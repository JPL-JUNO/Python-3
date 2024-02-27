"""
@File         : sched_cancel.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-01-19 21:29:31
@Email        : stephencuixuan@gmail.com
@Description  : 
"""

import sched, threading, time

scheduler = sched.scheduler(time.time, time.sleep)

counter = 0


def increment_counter(name):
    global counter
    print("Event:", time.ctime(time.time()), name)
    counter += 1
    print("Now:", counter)


print("Start:", time.ctime(time.time()))
e1 = scheduler.enter(2, 1, increment_counter, ("E1",))
e2 = scheduler.enter(3, 1, increment_counter, ("E2",))

# Start a thread to run the events.
t = threading.Thread(target=scheduler.run)
t.start()

# Back in the main thread, cancel the first scheduled event.
scheduler.cancel(e1)

# Wait for the scheduler to finish running in the thread.
t.join()
print("Final:", counter)
