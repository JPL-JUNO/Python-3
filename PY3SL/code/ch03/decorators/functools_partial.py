"""
@Title: 修饰符
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-21 16:57:43
@Description: 
"""

from functools import partial


def my_func(a, b=2):
    "Docstring for my_func()."
    print("  called my_func with:", (a, b))


def show_details(name, f, is_partial: bool = False):
    """Show details of a callable object."""
    print("{}:".format(name))
    print("  object:", f)
    if not is_partial:
        print("  __name__:", f.__name__)
    if is_partial:
        print("  func:", f.func)
        print("  args:", f.args)
        print("  keywords:", f.keywords)
    return


show_details("my_func", my_func)
my_func("a", 3)
print()

# Set a different default value for 'b',
# but require the caller to provide 'a'.
p1 = partial(my_func, b=4)
show_details("partial with named default", p1, True)
p1("passing a")
p1("override b", b=5)
print()


p2 = partial(my_func, "default a", b=99)
show_details("partial with default", p2, True)
p2()
p2(b="override b")
print()


print("Insufficient arguments:")
# the first partial created is invoked without passing a value
# for a, causing an exception.
p1()  # ❌
