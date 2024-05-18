# 异常

异常表示错误并破坏了程序的正常控制流程。使用 raise 语句引发异常。 raise 语句的一般格式是 raise Exception([value])，其中 Exception 是异常类型，value 是可选值，提供有关异常的具体详细信息。

要捕获异常，请使用 try 和 except 语句。

当异常发生时，解释器停止执行 try 块中的语句，并寻找与发生的异常类型相匹配的 except 子句。如果找到，控制权将传递给 except 子句中的第一个语句。执行 except 子句后，控制继续执行整个 try‑except 块之后出现的第一条语句。

try 语句没有必要匹配所有可能发生的异常。如果找不到匹配的 except 子句，异常将继续传播，并可能被另一个 try‑except 块捕获，而该块实际上可以在其他地方处理异常。从编程风格上讲，您应该只捕获代码可以实际恢复的异常。如果无法恢复，通常最好让异常传播。

如果异常在没有被捕获的情况下一直到达程序的顶层，则解释器将中止并显示错误消息。

如果 raise 语句单独使用，则最后生成的异常将再次引发。这仅在处理先前引发的异常时才起作用：

```python
try:
    file = open("foo.txt", "rt")
except FileNotFoundError:
    print("Well, that didn't work")
    raise
```

每个 except 子句都可以与 as var 修饰符一起使用，该修饰符给出变量的名称，如果发生异常，则将异常类型的实例放入该变量中。异常处理程序可以检查此值以了解有关异常原因的更多信息。例如，可以使用 isinstance() 检查异常类型。

异常具有一些标准属性，这些属性在需要执行进一步操作以响应错误的代码中可能会有用

- `e.args`: 引发异常时提供的参数元组。在大多数情况下，这是一个包含描述错误的字符串的单项元组。对于 `OSError` 异常，值是一个 2 元组或 3 元组，包含整数错误号、字符串错误消息和可选文件名。
- `e.__cause__`: 如果 B 异常时为了相应处理 A 异常而特意抛出的，则值为 A 异常。
- `e.__context__`: 如果在处理 A 异常抛出了 B 异常，则值为 A 异常
- `e.__traceback__`: 与异常关联的堆栈回溯对象。

用于保存异常值的变量只能在关联的内部访问除了块。一旦控制离开块，变量就变得未定义。

```python
try:
    int("N/A")  # Raises ValueError
except ValueError as e:
    print("Failed:", e)

print(e)  # Fails -> NameError. 'e' not defined.
```

可以使用多个except子句指定多个异常处理块：

```python
try:
    pass
except TypeError as e:
    pass
except ValueError as e:
    pass
```

单个处理程序子句可以捕获多个异常类型，如下所示：

```python
try:
    pass
except (TypeError, ValueError) as e:
    pass
```

要忽略异常，请使用 `pass` 语句。

要捕获除与程序退出相关的异常之外的所有异常，请像这样使用 `Exception`：

```python
try:
    pass
except Exception as e:
    print(f"An error occurred : {e!r}")
```

try 语句还支持 else 子句，该子句必须跟在最后一个 except 子句后面。如果 try 块中的代码未引发异常，则执行此代码：

```python
try:
    file = open("foo.txt", "rt")
except FileNotFoundError as e:
    print(f"Unable to open foo : {e}")
    data = ""
else:
    data = file.read()
    file.close()
```

finally 语句定义了一个清理操作，无论 try‑except 块中发生什么，该操作都必须执行。

```python
file = open("foo.txt", "rt")
try:
    # Do some stuff
    pass
finally:
    # File closed regardless of what happened
    file.close()
```

finally 子句不用于捕获错误。相反，它用于必须始终执行的代码。无论是否发生错误都会执行。如果没有引发异常，则 finally 子句中的代码将在 try 块中的代码之后立即执行。如果发生异常，则首先执行匹配的 except 块（如果有），然后将控制权传递给 finally 子句的第一个语句。如果执行此代码后，异常仍处于待处理状态，则该异常将重新引发以由另一个异常处理程序捕获。

## 异常层次

处理异常的一大挑战是管理程序中可能发生的大量异常。例如，仅内置异常就有 60 多个。如果再加上标准库的其余部分，则可能出现数百种异常。此外，通常没有办法提前轻松确定代码的任何部分可能引发哪种异常。异常不会记录为函数调用签名的一部分，也没有任何类型的编译器来验证代码中的异常处理是否正确。因此，异常处理有时会显得杂乱无章。

认识到异常是通过继承组织成层次结构的，会很有帮助。与针对特定错误相比，关注更一般的错误类别可能更容易。

```python
try:
    item = items[index]
except IndexError:  # Raised if items is a sequence
    pass
except KeyError:  # Raised if items is a mapping
    pass
```

与其编写代码来处理两个高度特定的异常，不如这样做可能更容易：

```python
try:
    item = items[index]
except LookupError:
    pass
```

`LookupError` 是一个代表更高级别异常分组的类。`IndexError` 和 `KeyError` 都继承自 `LookupError`，因此这个 except 子句将捕获其中之一。然而，`LookupError` 并不宽泛到包含与查找无关的错误。
异常类型|描述
---|---
`BaseException`|所有异常的根类
`Exception`|所有与程序相关的错误的基类
`ArithmeticError`|所有与数学相关的错误的基类
`ImportError`|所有与导入相关的错误的基类
`LookupError`|所有与容器查找相关的错误的基类
`OSError`|所有与系统相关的错误的基类，`IOError` 和 `EnvironmentError` 是别名
`ValueError`|与值相关的错误的基类，包括 Unicode
`UnicodeError`|与 Unicode 字符串编码相关的错误的基类

`BaseException` 类很少直接用于异常处理，因为它匹配所有可能的异常。这包括影响控制流的特殊异常，例如 `SystemExit`、`KeyboardInterrupt` 和 `StopIteration`。抓住这些很少是你想要的。相反，所有与程序相关的正常错误都继承自 `Exception`。`ArithmeticError` 是所有与数学相关的错误（例如 `ZeroDivisionError`、`FloatingPointError` 和 `OverflowError`）的基础。`ImportError` 是所有与导入相关的错误的基础。`LookupError` 是所有与容器查找相关的错误的基础。`OSError` 是源自操作系统和环境的所有错误的基础。`OSError` 包含与文件、网络连接、权限、管道、超时等相关的各种异常。当向操作提供错误的输入值时，通常会引发 `ValueError` 异常。`UnicodeError` 是 `ValueError` 的一个子类，它归类了所有与 Unicode 相关的编码和解码错误。

异常类|描述
---|---
`AssertionError`|失败的断言语句
`AttributeError`|错误地查找对象的属性
`EOFError`|文件结束错误
`MemoryError`|内存不足的错误
`NameError`|在本地或全局命名空间中找不到名称
`NotImplementedError`|未实现的功能
`RuntimeError`|通用的“something bad happened”错误
`TypeError`|应用于错误类型的对象的操作
`UnboundLocalError`|在赋值之前使用局部变量

## 异常和控制流

通常，异常是为处理错误而保留的。但是，也有一些例外，用于改变控制流。这些异常，直接继承自接 `BaseException`。
异常类|描述
---|---
`SystemExit`|抛出以指示程序退出
`KeyboardInterrupt`|当程序通过 Control‑C 中断时抛出
`StopIteration`|抛出以表示迭代结束

`SystemExit` 异常用于使程序有意终止。作为参数，可以提供整数退出代码或字符串消息。如果给出了一个字符串，它将被打印到 `sys.stderr` 并且程序以退出代码 1 终止。

```python
import sys

if len(sys.argv) != 2:
    raise SystemExit(f"Usage: {sys.argv[0]} filename")
filename = sys.argv[1]
```

当程序收到 `SIGINT` 信号（通常是在终端中按 Control‑C 键）时，会引发 `KeyboardInterrupt` 异常。此异常有点不寻常，因为它是异步的。这意味着它几乎可以在任何时间和程序中的任何语句中发生。当发生这种情况时，Python 的默认行为是简单地终止。

如果要控制 `SIGINT` 的传递，可以使用 signal 模块。

`StopIteration` 异常是迭代协议的一部分，表示迭代结束迭代。
