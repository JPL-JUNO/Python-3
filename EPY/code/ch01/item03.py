"""
@Title        : 了解 bytes 和 str 的区别
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2023-12-31 23:44:04
@Description  : 
"""

a = b"h\x65llo"
print(list(a))
print(a)

a = "a\u0300 propos"
print(list(a))
print(a)


def to_str(bytes_to_str):
    if isinstance(bytes_to_str, bytes):
        value = bytes_to_str.decode("utf-8")
    else:
        value = bytes_to_str
    return value


print(repr(to_str(b"foo")))
print(repr(to_str("bar")))


def to_bytes(bytes_to_str):
    if isinstance(bytes_to_str, str):
        value = bytes_to_str.encode("utf-8")
    else:
        value = bytes_to_str
    return value


print(repr(to_bytes(b"foo")))
print(repr(to_bytes("bar")))

print(b"one" + b"two")
print("one" + "two")

try:
    b"one" + "two"
except TypeError as e:
    print(e)

try:
    "one" + b"two"
except TypeError as e:
    print(e)


assert b"red" > b"blue"
assert "red" > "blue"

try:
    assert "red" > b"blue"
except TypeError as e:
    print(e)

try:
    assert b"blue" < "red"
except TypeError as e:
    print(e)


print(b"foo" == "foo")

print(b"red %s" % b"blue")
print("red %s" % "blue")

try:
    print(b"red %s" % "blue")
except TypeError as e:
    print(e)

# 会让系统在 bytes 实例上面调用 __repr__ 方法
print("red %s" % b"blue")
