"""
@File         : make_db.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-27 22:10:39
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

from person import Person, Manager

bob = Person("Bob Smith")  # Re-create objects to be stored
sue = Person("Sue Jones", job="dev", pay=100_000)
tom = Manager("Tom Jones", 50_000)
import shelve

db = shelve.open("person_db")  # Filename where objects are stored
for obj in (bob, sue, tom):  # Use object's name attr as key
    db[obj.name] = obj  # Store object on shelve by key
db.close()  # Close after making changes
