"""
@File         : simplest_python_class.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-17 23:03:20
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""


class rec:
    pass


rec.name = "Bob"
rec.age = 40

print(rec.name)

x = rec()
y = rec()

x.name, y.name
x.name = "Sue"
rec.name, x.name, y.name
list(rec.__dict__.keys())
list(name for name in rec.__dict__ if not name.startswith("__"))
list(x.__dict__.keys())
list(y.__dict__.keys())

#
x.name, x.__dict__["name"]
x.age
x.__dict__["age"]
x.__class__
rec.__base__


def upper_name(obj):
    return obj.name.upper()


upper_name(x)
rec.method = upper_name
x.method()
y.method()
rec.method(x)

rec = ("Bob", 40.5, ["dev", "mgr"])  # Tuple-based record
print(rec[0])
rec = {}
rec["name"] = "Bob"  # Dictionary-based record
rec["age"] = 40.5
rec["jobs"] = ["dev", "mgr"]


class rec:
    pass


rec.name = "Bob"  # Class-based record
rec.age = 40.5
rec.jobs = ["dev", "mgr"]
print(rec.name)


class rec:
    pass


pers1 = rec()
pers1.name = "Bob"
pers1.jobs = ["dev", "mgr"]
pers1.age = 40.5

pers2 = rec()
pers2.name = "Sue"
pers2.jobs = ["dev", "cto"]
pers1.name, pers2.name


class Person:
    def __init__(self, name, jobs, age=None):
        self.name = name
        self.jobs = jobs
        self.age = age

    def info(self):
        return (self.name, self.jobs)


rec1 = Person("Bob", ["dev", "mgr"], 40.5)
rec2 = Person("Sue", ["dev", "cto"])
rec1.jobs, rec2.info()
rec = dict(name="Bob", age=40.5, jobs=["dev", "mgr"])
rec = {"name": "Bob", "age": 40.5, "jobs": ["dev", "mgr"]}
rec = Person("Bob", 40.5, ["dev", "mgr"])
