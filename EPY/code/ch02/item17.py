"""
@File         : item17.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-04-10 22:26:31
@Email        : cuixuanstephen@gmail.com
@Description  : 用 defaultdict 处理内部状态中缺失的元素，而不要使用 setdefault
"""

visits = {
    "Mexico": {"Tulum", "Puerto Vallarta"},
    "Japan": {"Hakone"},
}
visits.setdefault("France", set()).add("Arles")  # short

if (japan := visits.get("Japan")) is None:  # Long
    visits["Japan"] = japan = set()
japan.add("Kyoto")
print(visits)


class Visits:
    def __init__(self) -> None:
        self.data = {}

    def add(self, country, city):
        # the implementation isn’t efficient because it
        # constructs a new set instance on every call, regardless of whether the
        # given country was already present in the data dictionary.
        city_set = self.data.setdefault(country, set())
        city_set.add(city)


visits = Visits()
visits.add("Russia", "Yekaterinburg")
visits.add("Tanzania", "Zanzibar")
print(visits.data)

from collections import defaultdict


class Visits:
    def __init__(self) -> None:
        self.data = defaultdict(set)

    def add(self, country, city):
        # the implementation of add is short and simple.
        self.data[country].add(city)


visits = Visits()
visits.add("England", "Bath")
visits.add("England", "London")
print(visits.data)
