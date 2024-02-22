"""
@File         : functions_and_functional_programming.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-20 20:26:52
@Email        : cuixuanstephen@gmail.com
@Description  : 函数与函数式编程
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
with tabs[3]:
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

        在这个例子中，`page` 函数实际上并不执行任何有意义的计算。相反，它只会创建和返回函数 `get`，调用该函数时会获取 `url` 页面的内容。    因此，`get` 函数中执行的计算实际上延迟到了程序后面对 `get` 求值的时候。
        ```python
        python.__closure__ # (<cell at 0x000001DD2A0815D0: str object at 0x000001DD2A07C490>,)
        python.__closure__[0].cell_contents # http://www.jython.org
        ```
        如果需要在一系列函数调用中保持某个状态，使用闭包是一种非常高效的方式。

        ```python
        def count_down(n):
            def next_one():
                nonlocal n
                r = n
                n -= 1
                return r

            return next_one


        next_one = count_down(10)
        while True:
            v = next_one()
            if not v:
                break
        ```
        在这段代码中，闭包用于保存内部计数器的值 `n`。每次调用内部函数 `next_one` 时，它都更新并返回这个计数器变量的前一个值。
        """
    )

with tabs[4]:
    st.write(
        "装饰器是一个函数，其主要用途是包装另一个函数或类。这种包装的首要目的是光明正大地修改或增强被包装对象的行为。语法上使用 特殊符号 @ 表示装饰器。使用装饰器时，它们必须出现在函数或类定义之前的单独行上。可以同时使用多个装饰器。装饰器将按照它们出现的先后顺序应用。"
    )
    st.markdown(
        """
        ```python
        enable_tracing = True
        if enable_tracing:
            debug_log = open("debug.log", "w")


        def trace(func):
            if enable_tracing:

                def call_func(*args, **kwargs):
                    debug_log.write(f"Calling {func.__name__}: {args}, {kwargs}\\n")
                    r = func(*args, **kwargs)
                    debug_log.write(f"{func.__name__} returned {r}\\n")
                    return r

                return call_func
            else:
                return func


        @trace
        def square(x):
            return x * x


        square(3)
        # square = trace(square)
        debug_log.close()
        """
    )
    st.write(
        """
        `trace` 创建了一个包装器函数，它会写入一些调试输出，然后调用原始函数对象。因此如果调用 `square` 函数，看到的将是包装器中 `write` 方法的输出。trace` 函数返回的函数 `call_func` 是一个闭包，用于替换原始的函数。
        """
    )
    st.markdown(
        """
        装饰器也可以接受参数。
        
        ```python
        event_handlers = {}


        def event_handler(event):
            def register_function(f):
                event_handlers[event] = f
                return f

            return register_function


        @event_handler("Button")
        def handle_button(msg):
            pass
        # temp = event_handler('Button')
        # handle_button =  temp(handle_button)


        @event_handler("Reset")
        def handle_reset(msg):
            pass
        ```
        
        装饰器也可以应用于类定义。对于类装饰器，应该让装饰器函数始终返回类对象作为结果。需要使用原始类定义的代码可能要直接引用类成员。
        """
    )
with tabs[5]:
    st.write(
        """
        函数使用 `yield` 关键字可以定义生成器 对象。生成器是一个函数，它生成一个值的序列，以便在迭代中使用。
        """
    )
    st.code(
        """
        >>> def count_down(n):
        ...     print(f"Counting down from {n:d}")
        ...     while n > 0:
        ...         yield n
        ...         n -= 1
        ...     return
        ... 
        >>> c = count_down(10)
        >>> c
        <generator object count_down at 0x000001DD29E60F20>
        """
    )
    st.markdown(
        """
        如果调用该函数，就会发现其中的代码不会开始执行，相反它会返回一个生成器对象。
        ```python
        >>> next(c)
        Counting down from 10
        10
        >>> next(c)
        9
        >>>
        ```
        
        生成器对象就会在 `next()` 被调用（在 Python 3 中是 `__next__()` ）时执行函数。调用 `next()` 时，生成器函数将开始执行语句，直至遇到 `yield` 语句为止。`yield` 语句在函数执行停止的地方生成一个结果，直到再次调用 `next()` 。然后继续执行 `yield` 之后的语句。

        通常不会在生成器上直接调用 `next()` 方法，而是通过 `for` 语句、`sum()` 或一些消耗序列的其他操作使用生成器，即不会手动去迭代。
        
        生成器函数完成的标志是返回或引发 `StopIteration` 异常，这标志着迭代的结束。如果生成器在完成时返回 `None` 之外的值，都是不合法的。(:orange[我觉得是可以返回其他值的])
        
        生成器使用时存在一个棘手的问题，即生成器函数仅被部分消耗。例如：
        
        ```python
        for n in count_down(10):
            if n == 2: 
                break
            pass
        ```
        
        为了处理这种情况，生成器对象提供方法 `close()` 标识关闭。不再使用或删除生成器时，就会调用 `close()` 方法。通常不必手动调用 `close()` 方法，但也可以这么做。
        
        ```python
        >>> c = count_down(10)
        >>> c.__next__()
        Counting down from 10
        10
        >>> c.__next__()
        9
        >>> c.close()
        >>> c.__next__()
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        StopIteration
        >>>
        ```
        
        在生成器函数内部，在 `yield` 语句上出现 `GeneratorExit` 异常时就会调用 `close()` 方法。也可以选择捕捉这个异常，以便执行清理操作。虽然可以捕捉 `GeneratorExit` 异常，但对于生成器函数而言，使用 `yield` 语句处理异常并生成另一个输出值是不合法的。另外，如果程序当前正在对生成器进行迭代，不应通过另一个的执行线程或从信号处理程序异步调用该生成器上的 `close()` 方法。
        
        ```python
        >>> def count_down(n):
        ...     print(f"Counting down from {n:d}")
        ...     try:
        ...         while n > 0:
        ...             yield n
        ...             n -= 1
        ...     except GeneratorExit:
        ...         print(f"Only made it to {n:d}")
        ...
        >>> c = count_down(5)
        >>> next(c)
        Counting down from 5
        5
        >>> next(c)
        4
        >>> c.close()
        Only made it to 4
        >>>
        ```
        """
    )
with tabs[6]:
    st.markdown(
        """
        在函数内，`yield` 语句还可以作为表达式使用，出现在赋值运算符的右边。以这种方式使用 `yield` 语句的函数称为**协程** ，向函数发送值时函数将执行。
        
        ```python
        >>> def receiver():
        ...     print("Ready to receive")
        ...     while True:
        ...         n = yield
        ...         print(f"Got {n}")
        ...
        >>> r = receiver()
        >>> next(r)
        Ready to receive
        >>> r.send(1)
        Got 1
        >>> r.send(2)
        Got 2
        >>> r.send("Hello")
        Got Hello
        >>>
        ```
        
        在这个例子中，一开始调用 `next()` 是必不可少的，这样协程才能执行第一个 `yield` 表达式之前的语句。这时，协程会挂起，等待相关生成器对象 `r` 的 `send()` 方法给它发送一个值。传递给 `send()` 的值由协程中的 `(yield)` 表达式返回。接收到值后，协程就会执行语句，直至遇到下一条 `yield` 语句。

        在协程中需要首先调用 `next()` 这件事情很容易被忽略，这经常成为错误出现的原因。因此，建议使用一个能自动完成该步骤的装饰器来包装协程。
        ```python
        >>> def coroutine(func):
        ...     def start(*args, **kwargs):
        ...         g = func(*args, **kwargs)
        ...         next(g)
        ...         return g
        ...     return start
        ...
        >>> 
        >>> @coroutine
        ... def receiver():
        ...     print("Ready to receive")
        ...     while True:
        ...         n = yield
        ...         print(f"Got {n}")
        ...
        >>>
        ```
        协程一般会不断地执行下去，除非被显式关闭或者自己退出。关闭后，如果继续给协程发送值，就会引发 `StopIteration` 异常。`close()` 操作将在协程内部引发 `GeneratorExit` 异常。
        ```python
        >>> r.close()
        >>> r.send(4)
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        StopIteration
        >>>
        ```
        
        可以使用 `throw(exctype[, value [, tb]])` 方法在协程内部引发异常，其中 `exctype` 是指异常类型， `value` 是指异常的值，而 `tb` 是指跟踪对象。
        
        ```python
        >>> r.throw(RuntimeError, "You're hosed!") 
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        RuntimeError: You're hosed!
        >>>
        ```
        以这种方式引发的异常将在协程中当前执行的 `yield` 语句处出现。协程可以选择捕捉异常并以正确方式处理它们。使用 `throw()` 方法作为给协程的异步信号并不安全——永远都不应该通过单独的执行线程或信号处理程序调用这个方法。
        
        如果 `yield` 表达式中提供了值，协程可以使用 `yield` 语句同时接收和发出返回值。
        
        ```python
        >>> def line_splitter(delimiter=None):
        ...     print("Ready to split")
        ...     result = None
        ...     while True:
        ...         line = yield result
        ...         result = line.split(delimiter)
        ...
        >>> s = line_splitter(",")
        >>> next(s)
        Ready to split
        >>> s.send("A,B,C")
        ['A', 'B', 'C']
        >>> s.send("100,200,300")
        ['100', '200', '300']
        >>>
        ```
        
        理解这个例子中的先后顺序至关重要。首个 `next()` 调用让协程向前执行到(`yield result`) ，这将返回 `result` 的初始值 `None` 。在接下来的 `send()` 调用中，接收到的值被放在 `line` 中并拆分到 `result` 中。`send()` 方法的返回值就是传递给下一条 `yield` 语句的值。换句话说，`send()` 方法的返回值来自下一个 `yield` 表达式，而不是接收 `send()` 传递的值的 `yield` 表达式。
        
        如果协程返回值，需要小心处理使用 `throw()` 引发的异常。如果使用 `throw()` 在协程中引发一个异常，传递给协程中下一条 `yield` 语句的值将作为 `throw()` 方法的结果返回。如果需要这个值却又忘记保存它，它就会消失不见。
        """
    )
