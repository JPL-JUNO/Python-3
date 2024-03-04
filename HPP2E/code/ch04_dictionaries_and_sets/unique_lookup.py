"""
@File         : unique_lookup.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-03-04 20:10:57
@Email        : cuixuanstephen@gmail.com
@Description  : 用列表和集合查询不同的名字
"""

import random, string, timeit


def list_unique_names(phone_book):
    unique_names = []
    for name, _ in phone_book:
        # 仅使用第一个空格进行分割
        first_name, _ = name.split(" ", 1)
        for unique in unique_names:
            if unique == first_name:
                break
        else:
            unique_names.append(first_name)
    return len(unique_names)


def set_unique_names(phone_book):
    unique_names = set()
    for name, _ in phone_book:
        first_name, _ = name.split(" ", 1)
        unique_names.add(first_name)
    return len(unique_names)


def random_name():
    first_name = "".join(random.sample(string.ascii_letters, 8))
    last_name = "".join(random.sample(string.ascii_letters, 8))
    return f"{first_name} {last_name}"


if __name__ == "__main__":
    phone_book = [("John Doe", "555-555-5555"), ("Albert Einstein", "212-555-5555")]

    print("Number of unique names from set method:", set_unique_names(phone_book))
    print("Number of unique names from list method:", list_unique_names(phone_book))
    setup = (
        "from __main__ import (large_phone_book, set_unique_names, list_unique_names)"
    )
    iterations = 50
    large_phone_book = [(random_name(), "132-1234-1232") for _ in range(1000)]
    t = timeit.timeit(
        stmt="list_unique_names(large_phone_book)", setup=setup, number=iterations
    )
    print(
        f"Finding unique names in a phone book of length {len(large_phone_book)} "
        f"using lists took: {t/iterations:.2e} seconds"
    )
    t = timeit.timeit(
        stmt="set_unique_names(large_phone_book)", setup=setup, number=iterations
    )
    print(
        f"Finding unique names in a phone book of length {len(large_phone_book)} "
        f"using sets took: {t / iterations:2e} seconds"
    )
