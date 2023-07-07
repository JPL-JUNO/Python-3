"""
@Description: Default dictionary values using defaultdict
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-07-07 09:24:14
"""
nodes = [
    ('a', 'b'), ('a', 'c'),
    ('b', 'a'), ('b', 'd'),
    ('c', 'a'), ('d', 'a'),
    ('d', 'b'), ('d', 'c'),
]

graph = dict()
for from_, to in nodes:
    if from_ not in graph:
        graph[from_] = []
    graph[from_].append(to)

import pprint
pprint.pprint(graph)

from collections import defaultdict

graph = defaultdict(list)
for from_, to in nodes:
    graph[from_].append(to)
pprint.pprint(graph)

counter = defaultdict(int)
counter['spam'] += 5
print(counter)


def tree():
    return defaultdict(tree)


import json

colors = tree()
colors['other']['black'] = 0x000000
colors['other']['white'] = 0xFFFFFF
colors['primary']['red'] = 0x00FF00
colors['primary']['green'] = 0x00FF00
colors['primary']['blue'] = 0x0000FF
colors['secondary']['yellow'] = 0xFFFF00
colors['secondary']['aqua'] = 0x00FFFF
colors['secondary']['fuchsia'] = 0xFF00FF

print(json.dumps(colors, sort_keys=True, indent=4))
