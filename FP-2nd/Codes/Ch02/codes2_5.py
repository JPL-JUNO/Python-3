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
