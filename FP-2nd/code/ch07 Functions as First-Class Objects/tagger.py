"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-03 11:07:13
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
