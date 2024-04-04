"""
@File  : item08.py
@Author: Stephen CUI
@Time  : 2024-04-03 16:31:11
"""

names = ["Cecilia", "Lise", "Marie"]
counts = [len(n) for n in names]
print(counts)

longest_name = None
max_count = 0
for i in range(len(names)):
    count = counts[i]
    if count > max_count:
        longest_name = names[i]
        max_count = count

print(longest_name)

for i, name in enumerate(names):
    count = counts[i]
    if count > max_count:
        longest_name = name
        max_count = count

for name, count in zip(names, counts):
    if count > max_count:
        longest_name = name
        max_count = count

names.append("Rosalind")
for name, count in zip(names, counts):
    print(name)

import itertools

for name, count in itertools.zip_longest(names, counts, fillvalue=None):
    print(f"{name}: {count}")
