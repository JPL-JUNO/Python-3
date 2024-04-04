"""
@Title        : 用支持插值的 f-string 取代 C 风格的格式字符串与 str.format 方法
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-01-01 11:26:14
@Description  : 
"""

a = 0b10111011
b = 0xC5F
print("Binary is %d, hex is %d" % (a, b))

key = "my_var"
value = 1.234
formatted = "%-10s = %.2f" % (key, value)
print(formatted)

try:
    reordered_tuple = "%-10s = %.2f" % (value, key)
except TypeError as e:
    print(e)

pantry = [("avocados", 1.25), ("bananas", 2.5), ("cherries", 15)]

print(
    "缺点 2：在填充模板之前，经常要先对准备填写进去的这个值稍微做一些处理，\n但这样一来，整个表达式可能就会写的很长，让人觉得比较混乱"
)
for i, (item, count) in enumerate(pantry):
    print("#%d: %-10s = %.2f" % (i, item, count))

print()

for i, (item, count) in enumerate(pantry):
    print("#%d: %-10s = %d" % (i + 1, item.title(), round(count)))

print("缺点 3：")
template = "%s loves food. See %s cook."
name = "Max"
formatted = template % (name, name)
print(formatted)

key = "my_var"
value = 1.234
old_way = "%-10s = %.2f" % (key, value)

# %(key)s 这个说明符，意思就是用字符串（s）来表示 dict 里面名为 key 的那个键所保存的值
new_way = "%(key)-10s = %(value).2f" % {"key": key, "value": value}

reordered = "%(key)-10s = %(value).2f" % {"value": value, "key": key}

assert old_way == new_way == reordered


name = "Max"
template = "%s loves food. See %s cook."
before = template % (name, name)

template = "%(name)s loves food. See %(name)s cook."
after = template % {"name": name}

# 更加明显的缺点
for i, (item, count) in enumerate(pantry):
    before = "#%s: %-10s = %d" % (i + 1, item.title(), round(count))

    after = "#%(loop)d: %(item)-10s = %(count)d" % {
        "loop": i + 1,
        "item": item.title(),
        "count": round(count),
    }

    assert before == after


soup = "lentil"
formatted = "Today's soup is %(soup)s" % {"soup": soup}
print(formatted)

menu = {"soup": "lentil", "oyster": "kumamoto", "special": "schnitzel"}

template = (
    "Today's soup is %(soup)s, "
    "buy one get two %(oyster)s oysters, "
    "and out special entree is %(special)s."
)
formatted = template % menu
print(formatted)


print()
print("内置的 format 函数与 str 类的 format 方法")
a = 1234.5678
formatted = format(a, ",.2f")
print(formatted)

b = "my string"
formatted = format(b, "^20s")
print("*", formatted, "*")

key = "my_var"
value = 1.234

formatted = "{} = {}".format(key, value)
print(formatted)

formatted = "{:<10} = {:.2f}".format(key, value)
print(formatted)

# 转义输出 % 与 {}
print("%.2f%%" % 12.5)
print("{} replaces {{}}".format(1.23))

formatted = "{1} = {0}".format(key, value)
print(formatted)

formatted = "{0} loves food. See {0} cook".format(name)
print(formatted)

for i, (item, count) in enumerate(pantry):
    old_style = "#%d: %-10s = %d" % (i + 1, item.title(), round(count))
    new_style = "#{}: {:<10s} = {}".format(i + 1, item.title(), round(count))
    assert old_style == new_style


formatted = "First letter us {menu[oyster][0]!r}".format(menu=menu)
print(formatted)


old_template = (
    "Today's soup is %(soup)s, "
    "buy one get two %(oyster)s oysters, "
    "and out special entree is %(special)s."
)
old_formatted = old_template % {
    "soup": "lentil",
    "oyster": "kumamoto",
    "special": "schnitzel",
}
new_template = (
    "Today's soup is %(soup)s, "
    "buy one get two %(oyster)s oysters, "
    "and out special entree is %(special)s."
)
new_formatted = new_template.format(
    soup="lentil", oyster="kumamoto", special="schnitzel"
)

print("插值格式字符串")

key = "my_var"
value = 1.234
formatted = f"{key} = {value}"
print(formatted)

formatted = f"{key!r:<10} = {value:.2f}"
print(formatted)

f_string = f"{key:<10} = {value:.2f}"
c_tuple = "%-10s = %.2f" % (key, value)
str_args = "{:<10} = {:.2f}".format(key, value)
str_kw = "{key:<10} = {value:.2f}".format(key=key, value=value)
c_dict = "%(key)-10s = %(value).2f" % {"key": key, "value": value}

assert c_tuple == c_dict == f_string
assert str_args == str_kw == f_string

for i, (item, count) in enumerate(pantry):
    old_style = "#%d: %-10s = %d" % (i + 1, item.title(), round(count))

    new_style = "#{}: {:<10s} = {}".format(i + 1, item.title(), round(count))

    f_string = f"#{i+1}: {item.title():<10s} = {round(count)}"

    assert old_style == new_style == f_string

for i, (item, count) in enumerate(pantry):
    print(f"#{i+1} " f"{item.title():<10s} = " f"{round(count)}")

places = 3
number = 1.23456
print(f"My number is {number:.{places}f}. 这样比硬代码更灵活")
