"""
@Title: 从定位参数到仅限关键字参数
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-02 21:55:31
@Description: 
"""


def tag(name, *content, class_=None, **attrs):
    if class_ is not None:
        attrs['class'] = class_
    attr_pairs = (f' {attr}="{value}' for attr, value in sorted(attrs.items()))

    attr_str = "".join(attr_pairs)

    if content:
        elements = (f"<{name}{attr_str}>{c}</{name}>"
                    for c in content)
        return "\n".join(elements)
    else:
        return f"<{name}{attr_str} />"


def example7_10():
    print(tag('br'))

    # 第一个参数后面的任意个参数会被 *content 捕获，存入一个元组。
    print(tag("p", "hello"))
    print(tag('p', 'hello', 'world'))

    # tag 函数签名中没有明确指定名称的关键字参数会被 **attrs 捕获，存入一个字典。
    print(tag('p', 'hello', id=33))

    # class_ 参数只能作为关键字参数传入。
    print(tag('p', 'hello', 'world', class_='sidebar'))

    # 调用 tag 函数时，即便第一个定位参数也能作为关键字参数传入。
    # content 虽然和形参同名，但是也只能作为关键字参数传入
    print(tag(content='testing', name="img"))

    # 在 my_tag 前面加上 **，字典中的所有元素作为单个参数传入，同名键会绑定到对应的
    # 具名参数上，余下的则被 **attrs 捕获。
    my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
              'src': 'sunset.jpg', 'class': 'framed'}
    print(tag(**my_tag))


def f(*, a, b, c):
    """仅限关键字参数"""
    pass


def f2(a, *, b):
    """确定数量的位置参数，同时也支持仅限关键字参数"""
    pass


f(a=1, b=2, c=3)
f2(1, b=1)


def divmod(a, b, /, c=1):
    """仅限位置参数

    All arguments to the left of the / are positional-only. 
    After the /, you may specify other arguments, which work as usual.
    """
    return (a // b, a % b)


# 不能使用关键字传入，只能使用位置
# divmod(a=10, b=4) 是错误的
assert divmod(10, 4) == (2, 2)
assert divmod(10, 4, c=100) == (2, 2)
