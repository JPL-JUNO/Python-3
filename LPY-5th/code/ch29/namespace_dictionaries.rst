>>> class Super:
...     def hello(self):
...         self.data1 = "spam"
... 
>>> 
>>> class Sub(Super):
...     def hola(self):
...         self.data2 = "eggs"
...
>>>
>>> X = Sub()
>>> X.__dict__
{}
>>> X.__class__
<class '__main__.Sub'>
>>> Sub.__base__
<class '__main__.Super'>
>>> Super.__base__
<class 'object'>
>>>

当类为 `self` 属性赋值时，会填入实例对象。也就是说，属性最后会位于实例的属性命名空间字典内，而不是类的。实例对象的命名空间保存了数据，会随实例的不同而不同，而 `self` 正是进入其命名空间的钩子。

>>> Y = Sub()
>>> X.hello()
>>> X.__dict__
{'data1': 'spam'}
>>> X.hola()
>>> X.__dict__
{'data1': 'spam', 'data2': 'eggs'}
>>> Sub.__dict__.keys()
dict_keys(['__module__', 'hola', '__doc__'])
>>> Super.__dict__.keys()
dict_keys(['__module__', 'hello', '__dict__', '__weakref__', '__doc__'])
>>> Y.__dict__
{}
>>>

因为属性实际上是 Python 的字典键，所以其实有两种方式可以读取并对其进行赋值：通过点号运算或者通过键索引运算。

>>> X.data1, X.__dict__["data1"]
('spam', 'spam')
>>> X.data3 = "toast"
>>> X.__dict__
{'data1': 'spam', 'data2': 'eggs', 'data3': 'toast'}
>>> X.__dict__["data3"] = "ham"
>>>

不过，这种等效关系只适用于实际中附加在实例上的属性。因为属性点号运算也会执行继承搜索，所以可以存取命名空间字典索引运算无法读取的属性。例如，继承的属性 `X.hello` 无法由 `X.__dict__['hello']` 读取。