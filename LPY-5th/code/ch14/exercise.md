# 迭代和推导

## 本章习题

1. for 循环和可迭代对象之间有什么关系？
2. for 循环和列表推导直接有什么关系？
3. 举出 Python 中的 4 种迭代上下文。
4. 目前逐行读取一个文本文件的最佳方式是什么？

## 习题解答

1. The for loop uses the iteration protocol to step through items in the iterable object across which it is iterating. It first fetches an iterator from the iterable by passing the object to iter, and then calls this iterator object’s `__next__` method in 3.X on each iteration and catches the `StopIteration` exception to determine when to stop looping. The method is named `next` in 2.X, and is run by the `next` built-in function in both 3.x and 2.X. Any object that supports this model works in a for loop and in all other iteration contexts. For some objects that are their own iterator, the initial iter call is extraneous but harmless.
2. Both are iteration tools and contexts. List comprehensions are a concise and often efficient way to perform a common for loop task: collecting the results of applying an expression to all items in an iterable object. It’s always possible to translate a list comprehension to a for loop, and part of the list comprehension expression looks like the header of a for loop syntactically.
3. Iteration contexts in Python include the for loop; list comprehensions; the map built-in function; the `in` membership test expression; and the built-in functions `sorted`, `sum`, `any`, and `all`. This category also includes the `list` and `tuple` built-ins, string `join` methods, and sequence assignments, all of which use the iteration protocol (see answer #1) to step across iterable objects one item at a time.
4. The best way to read lines from a text file today is to not read it explicitly at all: instead, open the file within an iteration context tool such as a for loop or list comprehension, and let the iteration tool automatically scan one line at a time by running the file’s next handler method on each iteration. This approach is generally best in terms of coding simplicity, memory space, and possibly execution speed requirements.

```python
for line in open("./script2.py"):
    print(line.upper(), end="")
```
