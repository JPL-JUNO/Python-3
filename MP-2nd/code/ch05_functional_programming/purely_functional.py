"""
@Description: Purely functional
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-01 22:09:47
"""
# Purely functional programming expects functions to have no side effects.
# That means that arguments given to the function should not be mutated,
# and neither should any other external states.


def add_value_functional(items, value):
    # returns a new value purely based on the input, without any other side effects.
    return items + [value]


items = [1, 2, 3]
add_value_functional(items, 5)
print(items)


def add_value_regular(items, value):
    # modifies the given input or even variables outside of its scope
    items.append(value)
    return items


add_value_regular(items, 5)
print(items)
