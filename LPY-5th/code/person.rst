D:\code>python person.py
Bob Smith 0
Sue Jones 100000

D:\code>python
Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import person 
>>>

>>> class Person:
...     # def __init__(self, name, job, pay) -> None:
...     #     self.name = name
...     #     self.job = job
...     #     self.pay = pay
...     def __init__(self, name, job=None, pay=0) -> None:
...         self.name = name
...         self.job = job
...         self.pay = pay
...     def last_name(self):
...         return self.name.split()[-1]
...     def give_raise(self, percent):
...         self.pay = int(self.pay * (1 + percent))
...
>>>
>>> if __name__ == "__main__":
...     bob = Person("Bob Smith")
...     sue = Person("Sue Jones", job="dev", pay=100_000)
...     print(bob.name, bob.pay)
...     print(sue.name, sue.pay)
...     # print(bob.name.split()[-1])
...     # sue.pay *= 1.10
...     # print(f"{sue.pay:.2f}")
...     print(bob.last_name(), sue.last_name())
...     sue.give_raise(0.1)
...     print(sue.pay)
...
Bob Smith 0
Sue Jones 100000
Smith Jones
110000
>>>