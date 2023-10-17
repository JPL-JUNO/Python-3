"""
@Title: Item 21: Know How Closures Interact with Variable Scope
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-17 21:35:30
@Description: 了解闭包如何与变量作用域交互
"""


def sort_priority(values, group):
    # python 支持闭包，这就意味着 helper 可以引用其定义范围内的变量
    def helper(x):
        # python 序列的特殊比较方法，即先比较 index 0 ，然后在比较 index 1，以此类推
        if x in group:
            return (0, x)
        return (1, x)
    # python 的函数是头等对象（见《流畅的 python》），因此可以赋值给变量
    values.sort(key=helper)


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
sort_priority(numbers, group)
print(numbers)


def sort_priority2(numbers, group) -> bool:
    found_mask = False  # Scope: 'sort_priority2'

    def helper(x):
        if x in group:
            # 当在表达式中引用变量时，Python 的解释器遍历以下范围以顺序来解析引用：
            # 1. 当前函数的范围内；
            # 2. 任何闭包范围内；
            # 3. 包含代码的模块的范围内（全局）
            # 4. 内置作用域
            # 但是给一个变量赋值却完全不同，
            # 如果一个变量已经存在于当前作用域内，那么就会赋一个新的值给它，
            # 如果这个变量不存在，那么 Python 就把这个赋值作为一个变量的定义

            # 这种赋值方式是合理的，阻止了对包含它的模块的污染，
            # 否则每个赋值语句都可以向全局丢一个垃圾变量
            found_mask = True  # Scope: 'helper' -- Bad!
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found_mask


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
found_mask = sort_priority2(numbers, group)
# 排序是对的，但是 found_mask 没有改变，它指示的值不对
assert not found_mask
print(numbers)


def sort_priority3(numbers, group) -> bool:
    found_mask = False

    def helper(x):
        # The nonlocal statement is used to indicate
        # that scope traversal should happen upon assignment for
        # a specific variable name. The only limit is
        # that nonlocal won’t traverse up to the module-level scope
        # (to avoid polluting globals).
        # 是对 global 语句的补充，其可以直接到模块作用域
        nonlocal found_mask
        # 就像 global 变量一样反模式，不要将非局部用于简单函数之外的任何内容
        if x in group:
            found_mask = True  #
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found_mask


class Sorter:
    def __init__(self, group):
        self.group = group
        self.found_mask = False

    def __call__(self, x):
        if x in self.group:
            self.found_mask = True
            return (0, x)
        return (1, x)


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
sorter = Sorter(group)
# Sorter 实现了 __call__ 方法，因此是可以调用的对象
numbers.sort(key=sorter)
assert sorter.found_mask is True


# 闭包函数可以引用定义它们的任何作用域中的变量。
# 默认情况下，闭包不能通过分配变量来影响封闭范围。
# 使用 nonlocal 语句来指示闭包何时可以修改其封闭范围内的变量。
# 避免对简单函数之外的任何内容使用非局部语句。
