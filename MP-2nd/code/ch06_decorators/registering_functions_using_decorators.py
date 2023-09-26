"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-25 22:34:22
@Description: 
"""

import collections


class EventRegistry:
    def __init__(self):
        self.registry = collections.defaultdict(list)

    def on(self, *events):
        def _on(function):
            for event in events:
                self.registry[event].append(function)
            return function
        return _on

    def fire(self, event, *args, **kwargs):
        for function in self.registry[event]:
            function(*args, **kwargs)


events = EventRegistry()


@events.on("success", "error")
def teardown(value):
    print(f"Tearing down got: {value}")
# 相当于这样嘛？
# def teardown(value):
#     print(f"Tearing down got: {value}")
# teardown = events.on("success", "error")(teardown)


@events.on("success")
def success(value):
    print(f"Successfully executed: {value}")


# 因为 events.registry 不存在这个 non-existing 这个键
events.fire("non-existing", "nothing to see here")
events.fire("error", "Oops, some error here")
events.fire("success", "Everything is fine")
