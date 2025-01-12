"""
@File         : recipe_07.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2025-01-12 21:33:24
@Email        : cuixuanstephen@gmail.com
@Description  : Writing clear documentation strings with RST markup
"""


def T_wc_1(T, V):
    """Computes the wind chill temperature"""
    ...


def T_wc_2(T, V):
    """Computes the wind chill temperature
    Th wind-chill, :math:`T_{wc}`,
    is based on air temperature, T, and wind speed, V.
    """
    ...


def T_wc_3(T: float, V: float):
    """Computes the wind chill temperature
    Th wind-chill, :math:`T_{wc}`,
    is based on air temperature, T, and wind speed, V.

    :param T: Temperature in ℃
    :param V: Wind Speed in KPH
    """
    ...


def T_wc_3(T: float, V: float) -> float:
    """Computes the wind chill temperature
    Th wind-chill, :math:`T_{wc}`,
    is based on air temperature, T, and wind speed, V.

    :param T: Temperature in ℃
    :param V: Wind Speed in KPH
    """
    ...


def T_wc_4(T: float, V: float) -> float:
    """Computes the wind chill temperature
    Th wind-chill, :math:`T_{wc}`,
    is based on air temperature, T, and wind speed, V.

    :param T: Temperature in ℃
    :param V: Wind Speed in KPH

    :returns: Wind-Chill temperature in ℃
    """
    ...


def T_wc_5(T: float, V: float) -> float:
    """Computes the wind chill temperature
    Th wind-chill, :math:`T_{wc}`,
    is based on air temperature, T, and wind speed, V.

    :param T: Temperature in ℃
    :param V: Wind Speed in KPH

    :returns: Wind-Chill temperature in ℃

    :raises ValueError: for wind speeds under 4.8 kph or T above 10 ℃
    """
    ...


def T_wc(T: float, V: float) -> float:
    """Computes the wind chill temperature
    Th wind-chill, :math:`T_{wc}`,
    is based on air temperature, T, and wind speed, V.

    :param T: Temperature in ℃
    :param V: Wind Speed in KPH

    :returns: Wind-Chill temperature in ℃

    :raises ValueError: for wind speeds under 4.8 kph or T above 10 ℃

    See https://en.wikipedia.org/wiki/Wind_chill
    .. math::

        T_{wc}(T_a, V) = 13.2 + 0.6215 T_a - 11.37 V ^ {0.16} + 0.3965 T_a V ^ {0.16}

    >>> round(T_wc(-10, 25), 1)
    -18.8
    """

    ...


def wind_chill_table() -> None:
    """Uses :func:`T_wc` to produce a wind-chill table for temperatures from -30℃ to 10℃ and
    wind speeds from 5kph to 50kph
    """
