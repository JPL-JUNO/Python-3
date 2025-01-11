"""
@File         : recipe_03.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2025-01-11 21:57:42
@Email        : cuixuanstephen@gmail.com
@Description  : Using super flexible keyword parameters
"""

import warnings


def rtd_outline():

    if distance is None:
        distance = rate * time

    elif rate is None:
        rate = distance / time

    elif time is None:
        time = distance / rate

    else:
        warnings.warning("Nothing to solve for")

    return dict(distance=distance, rate=rate, time=time)


def rtd(
    distance: float | None = None, rate: float | None = None, time: float | None = None
) -> dict[str, float | None]:
    if distance is None and rate is not None and time is not None:
        distance = rate * time
    elif rate is None and time is not None and distance is not None:
        rate = distance / time
    elif time is None and distance is not None and rate is not None:
        time = distance / rate
    else:
        warnings.warn("Nothing to solve for")

    return dict(distance=distance, rate=rate, time=time)


def rtd2(**kwargs: float) -> dict[str, float | None]:
    rate = kwargs.get("rate")
    time = kwargs.get("time")
    distance = kwargs.get("distance")

    if distance is None and rate is not None and time is not None:
        distance = rate * time
    elif rate is None and time is not None and distance is not None:
        rate = distance / time
    elif time is None and distance is not None and rate is not None:
        time = distance / rate
    else:
        warnings.warn("Nothing to solve for")

    return dict(distance=distance, rate=rate, time=time)


def rtd3(**kwargs: float) -> dict[str, float | None]:
    rate = kwargs.pop("rate", None)
    time = kwargs.pop("time", None)
    distance = kwargs.pop("distance", None)

    if kwargs:
        raise TypeError(f"Invalid keyword parameter(s): {''.join(kwargs.keys())}")

    if distance is None and rate is not None and time is not None:
        distance = rate * time
    elif rate is None and time is not None and distance is not None:
        rate = distance / time
    elif time is None and distance is not None and rate is not None:
        time = distance / rate
    else:
        warnings.warn("Nothing to solve for")

    return dict(distance=distance, rate=rate, time=time)


test_error = """
>>> import warnings
>>> warnings.simplefilter('error')
>>> rtd(distance=31.2, rate=6, time=10)
Traceback (most recent call last):
...
UserWarning: Nothing to solve for

"""


__test__ = {name: code for name, code in locals().items() if name.startswith("test_")}
