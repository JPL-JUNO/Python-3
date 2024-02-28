>>> class SharedData:
...     spam = 42  # Generates a class data attribute
... 
>>> 
>>> x = SharedData()  # Make two instances
>>> y = SharedData()
>>> x.spam, y.spam  # They inherit and share 'spam' (a.k.a. SharedData.spam)
(42, 42)
>>> SharedData.spam = 99
>>> x.spam, y.spam, SharedData.spam
(99, 99, 99)

对实例的属性进行赋值运算会在该实例内创建或修改变量名，而不是在共享的类中。通常的情况下，继承搜索只会在属性引用时发生，而不是在赋值运算时发生：对对象属性进行赋值总是会修改该对象，除此之外没有其他的影响。

>>> x.spam = 88
>>> x.spam, y.spam, SharedData.spam
(88, 99, 99)
>>>

>>> class MixedNames:
...     data = "spam"
...     def __init__(self, value) -> None:
...         self.data = value
...     def display(self):
...         print(self.data, MixedNames.data)
...
>>> x = MixedNames(1)
>>> y = MixedNames(2)
>>> x.display()
1 spam
>>> y.display()
2 spam
>>>