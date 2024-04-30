# 生成器

## 引言

生成器函数是 Python 最有趣、最强大的功能之一。生成器通常被认为是定义新型迭代模式的便捷方法。然而，它们还有更多的意义：生成器还可以从根本上改变函数的整个执行模型。

## 生成器与 `yield`

如果函数使用 `yield` 关键字，它就会定义一个称为生成器的对象。生成器的主要用途是生成用于迭代的值。

```python
def countdown(n):
    print("Counting down from", n)
    while n > 0:
        yield n
        n -= 1
```

这样定义的函数是一个生成器，如果你调用它，就会发现它不会执行。

```python
>>> c = countdown(10)
>>> c
<generator object countdown at 0x000001CC3BE3F1D0>
>>>
```

生成器对象仅在开始迭代时才执行该函数。 一种方法是调用 `next()` ：

```python
>>> next(c)
Counting down from 10
10
>>> next(c)
9
>>>
```

当 `next()` 被调用时，生成器函数执行语句，直到到达 `yield` 语句。`yield` 语句返回一个结果，此时函数的执行将暂停，直到再次调用 `next()`。当它被挂起时，该函数保留其所有局部变量和执行环境。当恢复时，继续执行 `yield` 后面的语句。

`next()` 是在生成器上调用 `__next__()` 方法的简写。

```python
>>> c.__next__()
8
>>> c.__next__()
7
>>>
```

通常不会直接在生成器上调用 `next()`，而是使用 `for` 语句或其他消费这些项目的操作。

生成器函数会生成项，直到返回为止（通过到达函数末尾或使用 `return` 语句）。这会引发 `StopIteration` 异常，终止 `for` 循环。如果生成器函数返回非 `None` 值，则会附加 `StopIteration` 异常。

```python
>>> def func():
...     yield 37
...     return 42
...
>>> f = func()
>>> next(f)
37
>>> next(f)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration: 42
>>>
```

要收集这个值，需要显式捕获 `StopIteration` 并提取该值：

```python
>>> try:
...     next(f)
... except StopIteration as e:
...     value = e.value
...
>>> value
42
>>>
```

通常，生成器函数不返回值。生成器几乎总是被 `for` 循环消耗，无法获取异常值。这意味着获取该值的唯一实用方法是通过显式的 `next()` 调用手动迭代生成器。

生成器的一个微妙问题是生成器函数只被部分使用。比如说在 `for` 循环中提前 `break`，那么生成器永远不会运行到完全完成。如果你的生成器函数执行某种清理操作很重要，请确保使用 `try-finally` 或上下文管理器。

```python
for n in countdown(10):
    if n == 2:
        break
    pass
def countdown(n):
    print("Counting down from", n)
    try:
        while n > 0:
            yield n
            n = n - 1
    finally:
        print("Only made it to", n)
```

即使生成器没有完全消耗，生成器也保证执行 `finally` 块代码——当废弃的生成器被垃圾收集时，它将执行。类似地，任何涉及上下文管理器的清理代码也保证在生成器终止时执行。

```python
def func(filename):
    # 伪代码
    pass
    with open(filename) as file:
        yield data
    pass
```

正确清理资源是一个棘手的问题。只要你使用诸如 `try-finally` 或上下文管理器之类的构造，即使生成器提前终止，也可以保证它们做正确的事情。

## 可重新启动的生成器

通常一个生成器函数只执行一次：

```python
>>> def countdown(n):
...     print("Counting down from", n)
...     while n > 0:
...         yield n
...         n -= 1
...
>>>
>>> c = countdown(3)
>>> for i in c:
...     print("T-minus", i)
...
Counting down from 3
T-minus 3
T-minus 2
T-minus 1
>>> for n in c:
...     print("T-minus", i)
...
>>>
```

如果你想要一个允许重复迭代的对象，请将其定义为类并将 `__iter__()` 方法定义为生成器。

```python
class countdown:
    def __init__(self, start) -> None:
        self.start = start
​
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1
```

这样，每次迭代时，`__iter__()` 都会创建一个新的生成器。

## 生成器委托

生成器的一个基本特征是，涉及 `yield` 的函数永远不会自行执行——它总是必须由其他代码使用 `for` 循环或显式的 `next()` 调用来驱动。这使得编写涉及 `yield` 的库函数变得有些困难，因为调用生成器函数不足以使其执行。为了解决这个问题，可以使用 `yield from` 语句。`yield from` 有效地将迭代过程委托给外部迭代。

```python
def countup(stop):
    n = 1
    while n <= stop:
        yield n
        n += 1
​
​
def countdown(start):
    n = start
    while n > 0:
        yield n
        n -= 1
​
​
def up_and_down(n):
    `yield from` countup(n)
    `yield from` countdown(n)
​
​
for i in up_and_down(5):
    print(i, end=" ")
```

`yield from` 主要使你不必自己驱动迭代。如果没有此功能，你将不得不编写如下 `up_and_down(n)` ：

```python
def up_and_down(n):
    for x in countup(n):
        yield x
    for x in countdown(n):
        yield x
```

在编写必须递归迭代嵌套可迭代对象的代码时，`yield from` 特别有用。例如，此代码展平嵌套列表：

```python
def flatten(items):
    for i in items:
        if isinstance(i, list):
            yield from flatten(i)
        else:
            yield i
​
​
a = [1, 2, [3, [4, 5], 6, 7], 8]
for x in flatten(a):
    print(x, end=" ")

# 1 2 3 4 5 6 7 8
```

## 生成器实践

生成器在构建与管道和工作流程相关的各种数据处理问题方面特别有效。生成器的一个有用应用是作为重构由深度嵌套的 `for` 循环和条件组成的代码的工具。

```python
import pathlib, re
​
for path in pathlib.Path(".").rglob("*.py"):
    if path.exists():
        with path.open("rt", encoding="utf-8") as file:
            for line in file:
                # 匹配注释
                m = re.match(".*(#.*)$", line)
                if m:
                    # 获取注释
                    comment = m.group(1)
                    if "spam" in comment:
                        print(comment)
```

这段代码嵌套的层数看起来很多，考虑使用生成器重构：

```python
def get_paths(top_dir, pattern):
    for path in pathlib.Path(top_dir).rglob(pattern):
        if path.exists():
            yield path
​
​
def get_files(paths):
    for path in paths:
        with path.open("rt", encoding="utf-8") as file:
            yield file
​
​
def get_lines(files):
    # file 本身是个迭代器
    for file in files:
        `yield from` file
​
​
def get_comments(lines):
    for line in lines:
        m = re.match(".*(#.*)$", line)
        if m:
            yield m.group(1)
​
​
def print_matching(lines, substring):
    for line in lines:
        if substring in line:
            print(line)
​
​
paths = get_paths(".", "*.py")
files = get_files(paths)
lines = get_lines(files)
comments = get_comments(lines)
print_matching(comments, "spam")
```

将功能细化成小且独立的组件，每个组件只关注其自身的特定任务，那么这可以提供代码的复用性。较小的任务也更容易进行推理、调试和测试。

生成器对于改变函数应用的正常评估规则也很有用。通常，当你应用函数时，它会立即执行并产生结果。生成器不这样做。 当应用生成器函数时，它的执行会被延迟，直到其他代码位调用它的 `next()` （显式地或通过 `for` 循环）。

考虑前面的 `flatten()` 函数，由于 Python 递归的限制，不能处理生成的嵌套结构。这可以通过使用栈以不同的方式驱动迭代来解决。

```python
def flatten_stack(items):
    stack = [iter(items)]
    while stack:
        try:
            item = next(stack[-1])
            if isinstance(item, list):
                stack.append(iter(item))
            else:
                yield item
        except StopIteration:
            stack.pop()
```

此实现构建了一个内部迭代器堆栈。它不受 Python 递归限制，因为它将数据放在内部列表上，而不是在内部解释器堆栈上构建帧。

这些示例是否意味着你应该使用狂野的生成器模式重写所有代码？ 不。主要的一点是，生成器的延迟评估允许你改变正常函数评估的时空维度。在各种现实场景中，这些技术都可以发挥作用并以意想不到的方式应用。

## 增强型生成器和 `yield` 表达式

在生成器函数内部，`yield` 语句也可以用作出现在赋值运算符右侧的表达式。

```python
def receiver():
    print("Ready to receive")
    while True:
        n = yield
        print("Got", n)
```

以这种方式使用 `yield` 的函数有时被称为“增强型生成器”或“基于生成器的协程”。遗憾的是，这个术语有点不精确，而且更加令人困惑，因为“协程”最近与异步函数相关联。为了避免这种混淆，我们将使用术语“增强型生成器”来明确我们仍在讨论使用 `yield` 的标准函数。

使用 `yield` 作为表达式的函数仍然是生成器，但其用法不同。它不产生值，而是响应发送给它的值并执行。

```python
>>> r = receiver()
>>> r.send(None)  # 将执行流程定位到生成器中 yield 第一次执行的位置
Ready to receive
>>> r.send(1)
Got 1
>>> r.send(2)
Got 2
>>> r.send("Hello, yield")
Got Hello, yield
>>>
```
