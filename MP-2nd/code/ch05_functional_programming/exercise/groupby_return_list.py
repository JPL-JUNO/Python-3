"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-23 18:30:35
@Description: 
"""

# Write a groupby function that returns lists of results instead of
# generators.

import pprint


def groupby(iterable, key=None):
    if key is None:
        def key(x): return x
    groups = {}
    for item in iterable:
        groups.setdefault(key(item), []).append(item)
    return groups


def main():
    pprint.pprint(groupby("AAAABBBCCDAABBB"))
    pprint.pprint(groupby("AAAABBBCCD"))


if __name__ == "__main__":
    main()
