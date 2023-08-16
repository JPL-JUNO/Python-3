from copy import deepcopy
phonebook = {"Alice": '2341', "Neth": '9012', "Cecil": '3258'}

items = [("name", "Gumby"), ("age", 42)]
d = dict(items)
d  # {'name': 'Gumby', 'age': 42}
d['name']  # 'Gumby'

d = dict(name="Gumby", age=42)
d  # {'name': 'Gumby', 'age': 42}

phonebook = {"Alice": '2341', "Neth": '9012', "Cecil": '3258'}
"Cecil's phone number is {Cecil}.".format_map(phonebook)
# "Cecil's phone number is 3258."

template = '''<html>
<head><title>{title}</title></head>
<body>
<h1>{title}</h1>
<p>{text}</p>
</body>
'''

d = {}
d['name'] = 'Gumby'
d['age'] = 42
d  # {'name': 'Gumby', 'age': 42}
return_value = d.clear()
# print(return_value)  # None

x = {}
y = x
x['key'] = 'value'
y  # {'key': 'value'}
x.clear()
y  # {}

x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
y = x.copy()
y['username'] = 'mhl'
y['machines'] = 'bar'
y  # {'username': 'mhl', 'machines': 'bar'}
x  # {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}

d = {'names': ['Alfred', 'Bertrand']}
c = d.copy()
dc = deepcopy(d)
d['names'].append('Clive')
c  # {'names': ['Alfred', 'Bertrand', 'Clive']}
dc  # {'names': ['Alfred', 'Bertrand']}

{}.fromkeys(['name', 'age'])  # {'name': None, 'age': None}
dict.fromkeys(['name', 'age'])  # {'name': None, 'age': None}

dict.fromkeys(['name', 'age'], '(unknown)')
# {'name': '(unknown)', 'age': '(unknown)'}

d = {}
# print(d['name'])  # KeyError: 'name'
# print(d.get('name'))  # None

d.get('name', 'NA')  # 'NA'

d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
d.items()
# dict_items([('title', 'Python Web Site'), ('url', 'http://www.python.org'), ('spam', 0)])
it = d.items()
len(it)  # 3
('spam', 0) in it  # True
d['spam'] = 1
('spam', 0) in it  # False
d['spam'] = 0
('spam', 0) in it  # True

d = {'x': 1, 'y': 2}
ret = d.pop('x')
ret, d  # (1, {'y': 2})

d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
ret = d.popitem()
ret, d
# (('spam', 0), {'title': 'Python Web Site', 'url': 'http://www.python.org'})

d = {}
d.setdefault('name', 'NA')  # 'NA'
d  # {'name': 'NA'}
d['name'] = 'Gumby'
d.setdefault('name', 'NA')  # 'Gumby'
d  # {'name': 'Gumby'}

d = {
    'title': 'Python Web Site',
    'url': 'http://www.python.org',
    'changed': 'Mar 14 22:09:15 MET 2016'
}
x = {'title': 'Python Language Website', 'Others': 'Others'}
d.update(x)
d
# {'title': 'Python Language Website',
#  'url': 'http://www.python.org',
#  'changed': 'Mar 14 22:09:15 MET 2016',
#  'Others': 'Others'}

d = {1: 1, 2: 2, 3: 3, 4: 1}
d.values()
# dict_values([1, 2, 3, 1])
