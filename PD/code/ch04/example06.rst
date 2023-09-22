Python 中的所有对象都被认为是头等对象。这意味着所有可以被赋值给一个名称的对象也可以被视为数据。

作为数据，对象可以被当作当作变量存储、作为参数传递、从函数返回、与其他对象进行比较等。

>>> items = {
...     "number": 42,
...     "text": "Hello, World"
... }
>>> items["func"] = abs             # 添加一个函数
>>> import math                     
>>> items["mod"] = math             # 添加一个模块
>>> items["error"] = ValueError     # 添加一个异常类型
>>> nums = [1, 2, 3, 4]
>>> items["append"] = nums.append   # 添加另一个对象的方法

>>> items["func"](-45)              # 执行 abs(-45)   
45
>>> items["mod"].sqrt(4)            # 执行 math.sqrt(4)
2.0
>>> try:
...     x = int('a lot')
... except items["error"] as e:     # 等同于 except ValueError as e
...     print("Couldn't convert")
...
Couldn't convert
>>> items["append"](100)            # 执行 nums.append(100)
>>> nums
[1, 2, 3, 4, 100]
>>>

>>> line = "ACME, 100, 490.10"
>>> column_types = [str, int, float]
>>> parts = line.split(", ")
>>> row = [ty(val) for val, ty in zip(parts, column_types)]
>>> print(row)
['ACME', 100, 490.1]