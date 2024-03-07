# 当索引行不通时

## 创建和使用字典

### 函数 `dict`

### 基本的字典操作

### 将字符串格式设置功能用于字典

### 字典方法

与其他内置类型一样，字典也有方法。字典的方法很有用，但其使用频率可能没有列表和字符串的方法那样高。

#### `clear`

方法 `clear` 删除所有的字典项，这种操作是就地执行的（就像 `list.sort` 一样），因此什么都不返回（或者说返回 `None`）。

```python
>>> d = {}
>>> d["name"] = "Gumby"
>>> d["age"] = 42
>>> d
{'name': 'Gumby', 'age': 42}
>>> returned_value = d.clear()
>>> d
{}
>>> assert returned_value is None
>>>
```

```python
>>> x = {}
>>> y = x
>>> x["key"] = "value"
>>> y
{'key': 'value'}
>>> x
{'key': 'value'}
>>> x = {}
>>> y
{'key': 'value'}
>>>
```

`x` 和 `y` 最初都指向同一个字典。在第一个场景中，通过将一个空字典赋给 `x` 来“清空”它。这对 `y` 没有任何影响，它依然指向原来的字典。但要删除原来字典的所有元素，必须使用 `clear`。如果这样做，`y` 也将是空的。

```python
>>> x = {}
>>> y = x
>>> x["key"] = "value"
>>> y
{'key': 'value'}
>>> x.clear()
>>> y 
{}
>>>
```

#### `copy`

方法 `copy` 返回一个新字典，其包含的键-值对与原来的字典相同（这个方法执行的是浅复制，因为值本身是原件，而非副本）。

```python
>>> x = {"user_name": "admin", "machines": ["foo", "bar", "baz"]}
>>> y = x.copy()
>>> y["user_name"] = "mlh"
>>> y["machines"].remove("bar")
>>> y
{'user_name': 'mlh', 'machines': ['foo', 'baz']}
>>> x
{'user_name': 'admin', 'machines': ['foo', 'baz']}
>>>
```

当替换副本中的值时，原件不受影响。然而，如果修改副本中的值（就地修改而不是替换），原件也将发生变化，因为原件指向的也是被修改的值（如这个示例中的 `'machines'` 列表所示）。

为避免这种问题，一种办法是执行深复制，即同时复制值及其包含的所有值，等等。为此，可使用模块 `copy` 中的函数 `deepcopy`。

```python
>>> from copy import deepcopy
>>> 
>>> d = {}
>>> d["names"] = ["Alfred", "Bertrand"]
>>> c = d.copy()
>>> dc = deepcopy(d)
>>> d["names"].append("Clive")
>>> c
{'names': ['Alfred', 'Bertrand', 'Clive']}
>>> dc
{'names': ['Alfred', 'Bertrand']}
>>>
```

#### `fromkeys`

方法 `fromkeys` 创建一个新字典，其中包含指定的键，且每个键对应的值都是 `None`。如果你不想使用默认值`None`，可提供特定的值。

```python
>>> {}.fromkeys(["name", "age"])
{'name': None, 'age': None}
>>> {}.fromkeys(["name", "age"], "NAN")
{'name': 'NAN', 'age': 'NAN'}
>>>
```

首先创建了一个空字典，再调用方法 `fromkeys` 来创建另一个字典，这显得有点多余。可以不这样做，而是直接对 `dict` 调用方法 `fromkeys`。

```python
>>> dict.fromkeys(["name", "age"])
{'name': None, 'age': None}
>>>
```

#### `get`

方法 `get` 为访问字典项提供了宽松的环境。通常，如果你试图访问字典中没有的项，将引发错误。而使用 `get` 不会这样。使用 get 来访问不存在的键时，没有引发异常，而是返回 `None`。你可指定“默认”值，这样将返回你指定的值而不是 `None`。如果字典包含指定的键，`get` 的作用将与普通字典查找相同。

```python
>>> d = {}
>>> d["name"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'name'
>>> d.get("name")
>>> d.get("name", "NAN")
'NAN'
>>> d["name"] = "Python"
>>> d.get("name")
'Python'
>>>
```

#### `items`

方法 `items` 返回一个包含所有字典项的列表，其中每个元素都为 `(key, value)` 的形式。字典项在列表中的排列顺序不确定。返回值属于一种名为**字典视图**的特殊类型。字典视图可用于迭代。另外，你还可确定其长度以及对其执行成员资格检查。

```python
>>> d = {"Language": "Python", "url": "http://www.python.org", "others": "R"}
>>> d.items()
dict_items([('Language', 'Python'), ('url', 'http://www.python.org'), ('others', 'R')])
>>> it = d.items()
>>> len(it)
3
>>> assert ("others", "R") in it
>>>
```

视图的一个优点是不复制，它们始终是底层字典的反映，即便你修改了底层字典亦如此。如果想要动态的访问，这是不错的方法，但是小心代码某处不注意的修改。

```python
>>> d["others"] = "ggplot2"
>>> assert ("others", "R") not in it
>>> d["others"] = 0
>>> assert ("others", 0) in it
>>>
```

#### `keys`

方法 `keys` 返回一个字典视图，其中包含指定字典中的键。

#### `pop`

方法 `pop` 可用于获取与指定键相关联的值，并将该键-值对从字典中删除。如果没有的键将报错

```python
>>> d = {"x": 1, "language": "Python"}
>>> d.pop("x")
1
>>> d
{'language': 'Python'}
>>> d.pop("R")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'R'
>>>
```

#### `popitem`

#### `setdefault`

#### `update`

#### `values`

方法 `values` 返回一个由字典中的值组成的字典视图。不同于方法 `keys`，方法 `values` 返回的视图可能包含重复的值。
