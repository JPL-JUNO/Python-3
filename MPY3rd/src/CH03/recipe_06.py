"""
@File         : recipe_06.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2025-01-12 14:17:37
@Email        : cuixuanstephen@gmail.com
@Description  : Picking an order for parameters based on partial functions
"""

from math import radians, sin, cos, sqrt, asin

MI = 3959
NM = 3440
KM = 6372


def haversine(
    lat_1: float, lon_1: float, lat_2: float, lon_2: float, R: float
) -> float:
    Δ_lat = radians(lat_2) - radians(lat_1)
    Δ_lon = radians(lon_2) - radians(lon_1)

    lat_1 = radians(lat_1)
    lat_2 = radians(lat_2)

    a = sqrt(sin(Δ_lat / 2) ** 2 + cos(lat_1) * cos(lat_2) * sin(Δ_lon / 2) ** 2)

    return R * 2 * asin(a)


# Solution 1: Wrap the function in a new function that provides the default value.
def haversine_k(
    lat_1: float, lon_1: float, lat_2: float, lon_2: float, *, R: float
) -> float: ...


def nm_haversine_1(*args: float) -> float:
    return haversine_k(*args, R=NM)


from functools import partial

nm_haversine_3 = partial(haversine_k, R=NM)


def p_haversine(
    R: float, lat_1: float, lon_1: float, lat_2: float, lon_2: float
) -> float: ...


from functools import partial

nm_haversine_4 = partial(p_haversine, NM)

nm_haversine_L = lambda *args: haversine_k(*args, R=NM)
# A lambda object is a function that’s been stripped of its name and body.
# The function definition is reduced to just two essentials:
# • The parameter list, *args, in this example.
# • A single expression, which is the result, haversine_k(*args, R=NM). A lambda cannot have any statements.
# The lambda approach makes it difficult to create type hints. This limits its utility.
# Further,
# the PEP-8 recommendations suggest assigning a lambda to a variable should never be done.
