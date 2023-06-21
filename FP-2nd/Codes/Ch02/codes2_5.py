"""
@Description: Unpacking Sequences and Iterables
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-06-20 14:01:13
"""
lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates
assert latitude == 33.9425
assert longitude == -118.408056

longitude, latitude = latitude, longitude

assert divmod(20, 8) == (2, 4)
t = (20, 8)
assert divmod(*t) == (2, 4)
quotient, remainder = divmod(*t)

assert quotient == 2
assert remainder == 4


import os
_, filename = os.path.split('/FP-2nd/Codes/Ch02/codes2_5.py')
assert filename == 'codes2_5.py'

a, b, *rest = range(5)
a, b, *rest = range(3)
a, b, *rest = range(2)

a, *body, c, d = range(5)
*head, b, c, d = range(5)


def fun(a, b, c, d, *rest):
    return a, b, c, d, rest


fun(*[1, 2], 3, *range(4, 7))

*range(4), 4
[*range(4), 4]
{*range(4), 4, *(5, 6, 7)}

# nested unpacking
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.69722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]


def main():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    for name, _, _, (lat, lon) in metro_areas:
        if lon <= 0:
            print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')


if __name__ == '__main__':
    main()
