>>> from step4 import Person
>>>
>>> bob = Person("Bob Smith")
>>> bob  # Show bob's __repr__ (not __str__)
[Person: Bob Smith, 0]
>>> print(bob)  # Ditto: print => __str__ or __repr__
[Person: Bob Smith, 0]
>>> bob.__class__  # Show bob's class and its name
<class 'step4.Person'>
>>> bob.__class__.__name__
'Person'
>>> list(bob.__dict__.keys())  # Attributes are really dict keys
['name', 'job', 'pay']
>>> for key in bob.__dict__:  # Index manually
...     print(key, " => ", bob.__dict__[key])
...
name  =>  Bob Smith
job  =>  None
pay  =>  0
>>> for key in bob.__dict__:  # obj.attr, but attr is a var
...     print(key, " => ", getattr(bob, key))
...
name  =>  Bob Smith
job  =>  None
pay  =>  0
>>>