"""
@Title: 支持函数式编程的包
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-02 22:21:34
@Description: 
"""


def example7_11():
    from functools import reduce

    def factorial(n):
        """不使用递归计算阶乘。求和可以使用 sum 函数，但是求积则没有这样的函数。"""
        return reduce(lambda a, b: a * b, range(1, n + 1))

    from operator import mul

    def fact(n):
        """
        operator 模块为多个算术运算符提供了对应的函数，从而避免编写 lambda a, b: a*b 这种
        平凡的匿名函数。使用算术运算符函数
        """
        return reduce(mul, range(1, n + 1))


def example7_13():
    """Another group of one-trick lambdas that operator replaces are functions to pick
    items from sequences or read attributes from objects: itemgetter and attrgetter
    are factories that build custom functions to do that.
    """
    metro_data = [
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
        ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
        ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
    ]

    from operator import itemgetter
    for city in sorted(metro_data, key=itemgetter(1)):
        print(city)

    # If you pass multiple index arguments to itemgetter, the function it builds will return
    # tuples with the extracted values, which is useful for sorting on multiple keys:
    cc_name = itemgetter(1, 0)
    for city in metro_data:
        print(cc_name(city))
    # itemgetter 使用 [] 运算符，因此它不仅支持序列，
    # 还支持映射和任何实现 __getitem__ 方法的类。

    # attrgetter 与 itemgetter 作用类似，它创建的函数根据名称提取对象的属性。如果把
    # 多个属性名传给 attrgetter，它也会返回提取的值构成的元组。此外，如果参数名中包
    # 含 .（点号），attrgetter 会深入嵌套对象，获取指定的属性。

    from collections import namedtuple
    LatLon = namedtuple('LatLon', "lat lon")
    Metropolis = namedtuple('Metropolis', 'name cc pop coord')

    metro_areas = [Metropolis(name, cc, pop, LatLon(lat, lon))
                   for name, cc, pop, (lat, lon) in metro_data]
    print(metro_areas[0])
    print(metro_areas[0].coord.lat)

    from operator import attrgetter

    name_lat = attrgetter("name", "coord.lat")

    for city in sorted(metro_areas, key=attrgetter("coord.lat")):
        """按照经度排序，但是打印名称和对应的经度"""
        print(name_lat(city))

    import operator
    # 以 i 开头、后面是另一个运算符的那些名称（如
    # iadd、iand 等），对应的是增量赋值运算符（如 +=、&= 等）。如果第一个参数是可变的，那
    # 么这些运算符函数会就地修改它；否则，作用与不带 i 的函数一样，直接返回运算结果。
    print([name for name in dir(operator) if not name.startswith('_')])


def example7_15():
    from operator import methodcaller
    s = "The time has come"
    upcase = methodcaller("upper")
    print(upcase(s))
    # methodcaller 还可以冻结某些参数，也就是部分应用
    # （partial application），这与 functools.partial 函数的作用类似。
    # 相当于给 replace 传递了两个参数
    hiphenate = methodcaller("replace", " ", "_")
    print(hiphenate(s))


def example7_16():
    from operator import mul
    from functools import partial
    triple = partial(mul, 3)

    assert triple(7) == 21
    print(list(map(triple, range(1, 10))))


def example7_17():
    import unicodedata
    import functools
    nfc = functools.partial(unicodedata.normalize, "NFC")
    s1 = "café"
    s2 = "cafe\u0301"
    print(s1, s2)
    assert not s1 == s2
    assert nfc(s1) == nfc(s2)


def example7_18():
    from tagger import tag
    from functools import partial

    picture = partial(tag, "img", class_="pic-frame")
    picture(src="hello.jpeg")
    print(picture)
    print(picture.func)
    print(picture.args)
    print(picture.keywords)


if __name__ == "__main__":
    example7_18()
