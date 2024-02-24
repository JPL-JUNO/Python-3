>>> import pprint
>>>
>>> cats = [{"name": "Zophie", "desc": "chubby"}, {"name": "Pooka", "desc": "fluffy"}]
>>> pprint.pformat(cats)
"[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]"
>>> file_obj = open("my_cats.py", "w")
>>> file_obj.write("cats = " + pprint.pformat(cats) + "\n")
83
>>> file_obj.close()
>>>
>>> import my_cats
>>>
>>> my_cats.cats
[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]
>>> my_cats.cats[0]
{'desc': 'chubby', 'name': 'Zophie'}
>>> my_cats.cats[0]["name"]
'Zophie'
>>> 