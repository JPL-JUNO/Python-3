
>>> from collections import namedtuple 
>>> City = namedtuple("City", "name country population coordinates")
>>> tokyo = City("Tokyo", "JP", 36.933, (35.689722, 139.691667))
>>> tokyo
City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722, 139.691667))
>>> tokyo.population
36.933
>>> tokyo.coordinates
(35.689722, 139.691667)
>>> tokyo[1]
'JP'
>>>

>>> City._fields
('name', 'country', 'population', 'coordinates')
>>> Coordinate = namedtuple("Coordinate", "lat lon")
>>> delhi_data = ("Delhi NCR", 'IN', 21.935, Coordinate(28.613889, 77.208889)) 
>>> delhi = City._make(delhi_data)
>>> delhi._asdict()
{'name': 'Delhi NCR', 'country': 'IN', 'population': 21.935, 'coordinates': Coordinate(lat=28.613889, lon=77.208889)}
>>> import json
>>> json.dumps(delhi._asdict())
'{"name": "Delhi NCR", "country": "IN", "population": 21.935, "coordinates": [28.613889, 77.208889]}'
>>>

Since Python 3.7, namedtuple accepts the defaults keyword-only argument providing an iterable of N default values for each of the N rightmost fields of the class.

>>> from collections import namedtuple
>>> Coordinate = namedtuple("Coordinate", "lat lon reference", defaults=["WGS84"])
>>> Coordinate(0, 0)
Coordinate(lat=0, lon=0, reference='WGS84')
>>> Coordinate._field_defaults
{'reference': 'WGS84'}
>>> 