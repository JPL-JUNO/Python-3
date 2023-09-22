"""
@Title: 编写可接受任意数量参数的函数
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-07 10:36:38
@Description: 
"""


def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))
# rest 是一个元组，它包含了其他所有传递过来的位置参数


assert avg(1, 2) == 1.5
assert avg(1, 2, 3, 4) == 2.5


import html


def make_element(name, value, **attrs):
    key_vals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = "".join(key_vals)
    element = "<{name}{attrs}>{value}</{name}>".format(name=name,
                                                       attrs=attr_str,
                                                       value=html.escape(value))
    return element


assert make_element("item", "Albatross", size="large",
                    quantity=6) == '<item size="large" quantity="6">Albatross</item>'
assert make_element("p", "<spam>") == '<p>&lt;spam&gt;</p>'
# attrs 是一个字典，它包含了所有传递过来的关键字参数
