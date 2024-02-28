>>> import glob
>>> 
>>> glob.glob("person*")
['person-composite.py', 'person-department.py', 'person-department.rst', 'person.py', 'person_db.bak', 'person_db.dat', 'person_db.dir']
>>> print(open("person_db.dir").read())
'Bob Smith', (0, 74)
'Sue Jones', (512, 82)
'Tom Jones', (1024, 81)

>>> print(open("person_db.dat", "rb").read()) 
b'\x80\x04\x95?\x00\x00\x00\x00
...more omitted...

>>> import shelve
>>> 
>>> db = shelve.open("person_db")  # Reopen the shelve
>>> len(db)  # Three 'records' stored
3
>>> list(db.keys())
['Bob Smith', 'Sue Jones', 'Tom Jones']
>>> bob = db["Bob Smith"]  # Fetch bob by key
>>> bob  # Runs __repr__ from AttrDisplay
[Person: job=None, name=Bob Smith, pay=0]
>>> bob.last_name()  # Runs last_name from Person
'Smith'
>>> for key in db:
...     print(key, "->", db[key])
... 
Bob Smith -> [Person: job=None, name=Bob Smith, pay=0]
Sue Jones -> [Person: job=dev, name=Sue Jones, pay=100000]
Tom Jones -> [Manager: job=mgr, name=Tom Jones, pay=50000]
>>> for key in sorted(db):
...     print(key, "->", db[key])
...
Bob Smith -> [Person: job=None, name=Bob Smith, pay=0]
Sue Jones -> [Person: job=dev, name=Sue Jones, pay=100000]
Tom Jones -> [Manager: job=mgr, name=Tom Jones, pay=50000]
>>>

D:\code>python update_db.py
Bob Smith       -> [Person: job=None, name=Bob Smith, pay=0]
Sue Jones       -> [Person: job=dev, name=Sue Jones, pay=100000]
Tom Jones       -> [Manager: job=mgr, name=Tom Jones, pay=50000]

D:\code>python update_db.py
Bob Smith       -> [Person: job=None, name=Bob Smith, pay=0]
Sue Jones       -> [Person: job=dev, name=Sue Jones, pay=110000]
Tom Jones       -> [Manager: job=mgr, name=Tom Jones, pay=50000]

D:\code>python update_db.py
Bob Smith       -> [Person: job=None, name=Bob Smith, pay=0]
Sue Jones       -> [Person: job=dev, name=Sue Jones, pay=121000]
Tom Jones       -> [Manager: job=mgr, name=Tom Jones, pay=50000]

D:\code>python update_db.py
Bob Smith       -> [Person: job=None, name=Bob Smith, pay=0]
Sue Jones       -> [Person: job=dev, name=Sue Jones, pay=133100]
Tom Jones       -> [Manager: job=mgr, name=Tom Jones, pay=50000]

>>> import shelve
>>> db = shelve.open('person_db')  
>>> rec = db['Sue Jones']
>>> rec
[Person: job=dev, name=Sue Jones, pay=146410]
>>> rec.last_name()
'Jones'
>>> rec.pay
146410
>>>