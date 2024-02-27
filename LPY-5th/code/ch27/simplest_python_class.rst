>>> class rec:
...     pass
... 
>>> 
>>> rec.name = "Bob"
>>> rec.age = 40
>>> 
>>> print(rec.name)
Bob
>>> 
>>> x = rec()
>>> y = rec()
>>> 
>>> x.name, y.name
('Bob', 'Bob')
>>> x.name = "Sue"
>>> rec.name, x.name, y.name
('Bob', 'Sue', 'Bob')
>>> list(rec.__dict__.keys())
['__module__', '__dict__', '__weakref__', '__doc__', 'name', 'age']
>>> list(name for name in rec.__dict__ if not name.startswith("__"))
['name', 'age']
>>> list(x.__dict__.keys())
['name']
>>> list(y.__dict__.keys())
[]

一个属性通常既可以通过字典索引又可以通过属性记号访问，当时仅当其出现在所需的对象上。属性记号启动了继承搜索，但是索引只在单独的该对象中查看。

>>> x.name, x.__dict__["name"]
('Sue', 'Sue')
>>> x.age
40
>>> x.__dict__["age"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'age'
>>> x.__class__
<class '__main__.rec'>
<class 'object'>

>>> def upper_name(obj):
...     return obj.name.upper()
...
>>>
>>> upper_name(x)
'SUE'
>>> rec.method = upper_name
>>> x.method()
'SUE'
>>> y.method()
'BOB'
>>> rec.method(x)
'SUE'
>>>

====================
重访记录：类 VS 字典
====================

>>> rec = ("Bob", 40.5, ["dev", "mgr"])  # Tuple-based record
>>> print(rec[0])
Bob
>>> rec = {}
>>> rec["name"] = "Bob"  # Dictionary-based record
>>> rec["age"] = 40.5
>>> rec["jobs"] = ["dev", "mgr"]
>>> 
>>>
>>> class rec:
...     pass
...
>>>
>>> rec.name = "Bob"  # Class-based record
>>> rec.age = 40.5
>>> rec.jobs = ["dev", "mgr"]
>>> print(rec.name)
Bob
>>>
>>>
>>> class rec:
...     pass
... 
>>>
>>> pers1 = rec()
>>> pers1.name = "Bob"
>>> pers1.jobs = ["dev", "mgr"]
>>> pers1.age = 40.5
>>> 
>>> pers2 = rec()
>>> pers2.name = "Sue"
>>> pers2.jobs = ["dev", "cto"]
>>>
>>> pers1.name, pers2.name
('Bob', 'Sue')
>>> 

>>> class Person:
...     def __init__(self, name, jobs, age=None):
...         self.name = name
...         self.jobs = jobs
...         self.age = age
...     def info(self):
...         return (self.name, self.jobs)
...
>>> rec1 = Person("Bob", ["dev", "mgr"], 40.5)
>>> rec2 = Person("Sue", ["dev", "cto"])
>>> rec1.jobs, rec2.info()
(['dev', 'mgr'], ('Sue', ['dev', 'cto']))
>>> rec = dict(name="Bob", age=40.5, jobs=["dev", "mgr"])
>>> rec = {"name": "Bob", "age": 40.5, "jobs": ["dev", "mgr"]}
>>> rec = Person("Bob", 40.5, ["dev", "mgr"])
>>>