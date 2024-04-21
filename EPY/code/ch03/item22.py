"""
@File         : item22.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-04-21 13:16:18
@Email        : cuixuanstephen@gmail.com
@Description  : 用数量可变的位置参数给函数涉及清晰的参数列表
"""


def log(message, values):
    if not values:
        print(message)
    else:
        values_str = ", ".join(str(x) for x in values)
        print(f"{message}: {values_str}")


log("My numbers are", [1, 2])
log("Hi there", [])


def log(message, *values):  # The only difference
    if not values:
        print(message)
    else:
        values_str = ", ".join(str(x) for x in values)
        print(f"{message}: {values_str}")


log("My numbers are", [1, 2])
log("Hi there")

favorites = [7, 33, 99]
log("Favorite colors", *favorites)


def my_generator():
    for i in range(10):
        yield i


def my_func(*args):
    print(args)


it = my_generator()
my_func(*it)  # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

log("Favorite numbers", 7, 33)  # Old usage breaks


def log(sequence, message, *values):
    if not values:
        print(f"{sequence} - {message}")
    else:
        values_str = ", ".join(str(x) for x in values)
        print(f"{sequence} - {message}: {values_str}")


log(1, "Favorites", 7, 33)  # New with *args OK
log(1, "Hi there")  # New message only OK
log("Favorite numbers", 7, 33)  # Old usage breaks
