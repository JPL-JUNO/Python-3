>>> import shelve
>>>
>>> shelf_file = shelve.open("my_data")
>>> cats = ["Zophie", "Pooka", "Simon"]
>>> shelf_file["cats"] = cats
>>> shelf_file.close()
>>>

>>> shelf_file = shelve.open("my_data")
>>> type(shelf_file)
<class 'shelve.DbfilenameShelf'>
>>> shelf_file["cats"]
['Zophie', 'Pooka', 'Simon']
>>> shelf_file.close()
>>> 

>>> shelf_file = shelve.open("my_data")
>>> list(shelf_file.keys())
['cats']
>>> list(shelf_file.values())
[['Zophie', 'Pooka', 'Simon']]
>>> shelf_file.close()
>>>