"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-28 13:26:17
@Description: Extend the `track` function to monitor execution time.
"""

import functools
import time
from datetime import datetime


def track(function=None, label=None):
    if label and not function:
        return functools.partial(track, label=label)
    print(f"Initializing {label}")

    @functools.wraps(function)
    def _track(*args, **kwargs):
        print(f"calling {label}")
        start = datetime.now()
        result = function(*args, **kwargs)
        end = datetime.now()
        print(f"called {label} in {end- start}")
        return result
    return _track


@track(label="outer")
@track(label="inner")
def func():
    print("func")


@track(label="Slow function")
def slower_func():
    print("slower_func")
    time.sleep(.5)


if __name__ == "__main__":
    func()
    slower_func()
