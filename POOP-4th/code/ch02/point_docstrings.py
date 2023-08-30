"""
@Title: Explaining yourself with docstrings
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-30 10:16:22
@Description: 
"""
import math


class Point:
    """
    Represents a point in two-dimensional geometric coordinates

    >>> p_0 = Point()
    >>> p_1 = Point(3, 4)
    >>> p_0.calculate_distance(p_1)
    5.0
    """

    def __init__(self, x: float = 0, y: float = 0) -> None:
        """
        Initialize the position of a new point. The x and y coordinates
        can be specified. If they are not, the point defaults to the origin

        Parameters
        ----------
        x : float, optional
            x-coordinate, by default 0
        y : float, optional
            y-coordinate, by default 0
        """
        self.move(x, y)

    def move(self, x: float, y: float) -> None:
        """
        Move the point to a new location in 2D space

        Parameters
        ----------
        x : float
            x-coordinate
        y : float
            y-coordinate
        """
        self.x = x
        self.y = y

    def reset(self) -> None:
        """
        Reset the point back to the geometric origin: 0, 0
        """
        self.move(0, 0)

    def calculate_distance(self, other: "Point") -> float:
        """
        Calculate the Euclidean distance from this point
        to a second point passed as a parameter

        Parameters
        ----------
        other : Point
            instance

        Returns
        -------
        float
            distance
        """
        return math.hypot(self.x - other.x, self.y - other.y)
