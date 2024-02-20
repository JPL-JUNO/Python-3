"""
@File         : functions_and_functional_programming.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-20 20:26:52
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

import streamlit as st

st.set_page_config(layout="wide")
tabs = st.tabs(
    [
        "函数",
        "参数传递与返回值",
        "作用域规则",
        "作为对象与闭包的函数",
        "装饰器",
        "生成器与 yield",
        "协程与 yield 表达式",
        "使用生成器与协程",
        "列表推导",
        "生成器表达式",
        "声明式编程",
        "lambda 运算符",
        "递归",
        "文档字符串",
        "函数属性",
        "eval() 、exec() 和 compile() 函数",
    ]
)
with tabs[0]:
    st.markdown(
        """
        使用 `def` 语句可定义函数。函数体就是在调用函数时所执行的一系列语句。调用函数的方法是在函数名称后面加上函数参数的元组。参数的顺序和数量必须与函数定义匹配，否则会引发 `TypeError` 异常。函数的参数可以拥有默认值，做法是在函数定义中为参数赋值。如果函数定义中存在带有默认值的参数，该参数及其所有后续参数都是可选的。如果未给函数定义中的所有可选参数赋值，就会引发 `SyntaxError` 异常。
        
        默认参数值总是被设为函数定义时作为值传入的对象。另外，使用可变对象作为默认值可能导致意料之外的结果：
        
        ```python
        def foo(x, items=[]):
            items.append(x)
            print(items)
        foo(1) # [1]
        foo(2) # [1, 2]
        foo(3) # [1, 2, 3]
        ```
        注意，默认参数保留了前面调用时进行的修改。为了防止出现这种情况，最好使用 `None` 值，并在后面加上检查代码。
        
        如果给最后一个参数名加上星号（*），函数就可以接受任意数量的参数。
        
        提供函数参数还有一种方式，即显式地命名每个参数并为其指定一值，这称为关键字参数。使用关键字参数时，参数的顺序无关紧要。但除非提供了默认值，否则必须显式地命名所有必需的函数参数。位置参数和关键字参数可以出现在同一次函数调用中，前提是所有位置参数必须先出现，给所有非可选参数提供值，并且不能多次定义参数值。
        
        如果函数定义的最后一个参数以 ** 开头，所有额外的关键字参数（与任意其他参数名称都不匹配的参数）都可以放入一个字典中，并把这个字典传递给函数。
        
        ```python
        def make_table(date, **kwargs):
            fg_color = kwargs.pop("fg_color", "black")
            bg_color = kwargs.pop("bg_color", "white")
            width = kwargs.pop("width", None)
            if kwargs:
                raise TypeError(f"Unsupported configuration options {list(kwargs)}")
        ```
        
        关键字参数和可变长度参数列表可以一起使用，只要 ** 参数出现在最后即可。`*args` 和 `**kwargs` 通常用来为其他函数编写包装器和代理。
        """
    )
with tabs[1]:
    st.markdown(
        """
        调用函数时，函数参数仅仅是指代传入对象的名称。参数传递的基本语义和其他编程语言中已知的方式不完全相同，如“按值传递”或“按引用传递”。例如，如果传递不可变的值，参数看起来实际是按值传递的。但如果传递可变对象（如列表或字典）给函数，然后再修改此可变对象，这些改动将反映在原始对象中。
        
        ```python
        a = [1, 2, 3, 4, 5]
        def square(items):
            for i, x in enumerate(items):
                items[i] = x * x
        square(a)  # a = [1, 4, 9, 16, 25]
        ```
        
        **像这样悄悄修改其输入值或者程序其他部分的函数被认为具有副作用。一般来说，最好避免使用这种编程风格，因为随着程序的规模和复杂程度不断增加，这类函数会成为各种奇怪编程错误的根源**（例如，如果函数具有副作用，只看函数调用是无法明显发现的）。在涉及线程和并发的程序中，这类函数的交互能力很差，因为通常需要使用锁定来防止副作用的影响。

        `return` 语句从函数返回一个值。如果没有指定任何值或者省略 `return` 语句，就会返回 `None` 对象。
        """
    )

with tabs[2]:
    st.markdown(
        """
        系统每次执行一个函数时，就会创建新的局部命名空间。该命名空间代表一个局部环境，其中包含函数参数的名称和在函数体内赋值的变量名称。解析这些名称时，解释器将首先搜索局部命名空间。如果没有找到匹配的名称，它就会搜索全局命名空间。函数的全局命名空间始终是定义该函数的模块。如果解释器在全局命名空间中也找不到匹配值，最终会检查内置命名空间。如果仍然找不到，就会引发 `NameError` 异常。
        
        ```python
        a = 42
        def foo():
            a = 13
        foo()
        assert a == 42
        ```
        
        当变量在函数中被赋值时，这些变量始终被绑定到该函数的局部命名空间中，因此函数体中的变量 `a` 引用的是一个包含值 13 的全新对象，而不是外面的变量。使用 `global` 语句可以改变这种行为。`global` 语句明确地将变量名称声明为属于全局命名空间，只有在需要修改全局变量时才必须使用它。这条语句可以放在函数体中的任意位置，并可重复使用。
        
        Python 支持嵌套的函数定义。嵌套函数中的变量是由静态作用域 （lexical scoping）限定的。也就是说，解释器在解析名称时首先检查局部作用域，然后由内而外一层层检查外部嵌套函数定义的作用域。如果找不到匹配，那么和之前一样，将搜索全局命名空间和内置命名空间。**内部函数不能给定义在外部函数中的局部变量重新赋值**。下面这段代码是无效的：
        
        ```
        def count_down(start):
            n = start
            def display():
                print(f"T-minus {n:d}")
            def decrement():
                n -=1
            while n >0:
                display()
                decrement()
        ```
        在 Python 3 中，可以把 `n` 声明为 `nonlocal`。`nonlocal` 声明不会把名称绑定到当前调用栈下方的任意函数中定义的局部变量，即动态作用域 （dynamic scope）中。
        
        如果使用局部变量时还没给它赋值，就会引发 `UnboundLocalError` 异常。（可以引用，但是不是赋值）
        
        ```
        i = 0
        def foo():
            i = i + 1 # UnboundLocalError
            print(i)
        ```
        """
    )
st.markdown(
    """
    函数在 Python 中是头等对象。也就是说可以把它们当作参数传递给其他函数，放在数据结构中，以及作为函数的返回结果。
    
    将组成函数的语句和这些语句的执行环境打包在一起时，得到的对象称为闭包 。事实上所有函数都拥有一个指向了定义该函数的全局命名空间的 `__globals__` 属性。
    
    使用嵌套函数时，闭包将捕捉内部函数执行所需的整个环境。如果要编写惰性求值（lazy evaluation）或延迟求值的代码，闭包和嵌套函数特别有用。
    
    ```python
    def call_func(func):
        return func()

    def bar():
        x = 13
        def hello_world():
            return f"Hello World. x is {x:d}"
        return call_func(hello_world) # 'Hello World. x is 13'
    ```
    
    ```python
    from urllib.request import urlopen
    def page(url):
        def get():
            return urlopen(url).read()
        return get
        
    python = page("http://www.python.org")
    jython = page("http://www.jython.org")
    jython, python
    # (<function page.<locals>.get at 0x000001DD2A084180>, <function page.<locals>.get at 0x000001DD2A084400>)
    py_data = python()
    jy_data = jython()
    ```
    
    在这个例子中，`page` 函数实际上并不执行任何有意义的计算。相反，它只会创建和返回函数 `get`，调用该函数时会获取 `url` 页面的内容。因此，`get` 函数中执行的计算实际上延迟到了程序后面对 `get` 求值的时候。
    ```python
    python.__closure__ # (<cell at 0x000001DD2A0815D0: str object at 0x000001DD2A07C490>,)
    python.__closure__[0].cell_contents # http://www.jython.org
    ```
    如果需要在一系列函数调用中保持某个状态，使用闭包是一种非常高效的方式。
    """
)


from urllib.request import urlopen


def page(url):
    def get():
        return urlopen(url).read()

    return get
