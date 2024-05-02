# Set 操作

Set 是唯一值的无序集合。下表的操作可以在 Set 上执行：

|Operation|Description
|---|---
|`s \| t`|s 和 t 的并集
|`s & t`|s 和 t 的交集
|`s – t`|s 和 t 的差集
|`s ^ t`|对称差(并集-交集)
|`len(s)`|集合中的项数
|`item in s`, `item not in s`|成员检查
|`s.add(item)`|添加一个项
|`s.remove(item)`|如果存在项，则移除，否则报错
|`s.discard(item)`|删除一个存在的项

```python
>>> a = {"a", "b", "c"}
>>> b = {"c", "d"}
>>> a | b
{'a', 'b', 'c', 'd'}
>>> a & b
{'c'}
>>> a - b
{'a', 'b'}
>>> b - a
{'d'}
>>> a ^ b
{'a', 'b', 'd'}
>>>
```

集合操作也适用于字典的键视图和项目视图对象。例如，为了要找出两个字典有哪些共同的键，请执行以下操作：

```python
>>> a = {"x": 1, "y": 2, "z": 3}
>>> b = {"z": 3, "w": 4, "q": 5}
>>> a.keys() & b.keys()
{'z'}
>>>
```
