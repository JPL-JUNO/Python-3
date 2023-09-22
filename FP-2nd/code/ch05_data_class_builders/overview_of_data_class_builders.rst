namedtuple—a factory function that builds a subclass of tuple with the name and fields you specify:

>>> from collections import namedtuple
>>> Coordinate = namedtuple("Coordinate", "lat lon")
>>> issubclass(Coordinate, tuple)
True
>>> moscow = Coordinate(55.756, 37.617)
>>> moscow
Coordinate(lat=55.756, lon=37.617)
>>> moscow == Coordinate(55.756, 37.617)
True
>>>

The newer typing.NamedTuple provides the same functionality, adding a type annotation to each field:

>>> import typing
>>> Coordinate = typing.NamedTuple("Coordinate", [('lat', float), ('lon', float)])
>>> issubclass(Coordinate, tuple)
True
>>> typing.get_type_hints(Coordinate)
{'lat': <class 'float'>, 'lon': <class 'float'>}
>>>

A typed named tuple can also be constructed with the fields given as keyword arguments, like this:

>>> Coordinate = typing.NamedTuple("Coordinate", lat=float, lon=float)
>>>

