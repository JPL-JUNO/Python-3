重新定义继承变量名的概念引出了各种专有化技术。例如，子类可以完全取代继承的属性，提供超类可以找到的属性，并且通过已覆盖的方法回调超类来扩展超类的方法。我们已经看到过实际中取代的做法。 
>>> class Super:
...     def method(self):
...         print("in Super.method")
...
>>> 
>>> class Sub(Super):
...     def method(self):  # Override method
...         print("starting Sub.method")  # Add actions here
...         Super.method(self)  # Run default action
...         print("ending Sub.method")
...
>>>
>>> x = Super()  # Make a Super instance
>>> x.method()  # Runs Super.method
in Super.method
>>> x = Sub()  # Make a Sub instance
>>> x.method()  # Runs Sub.method, calls Super.method
starting Sub.method
in Super.method
ending Sub.method
>>>