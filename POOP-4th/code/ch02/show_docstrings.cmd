@REM 在命令行运行
python -i point_docstrings.py
@REM 进入交互式命令窗口，输入 help(Point)
Help on class Point in module __main__:

@REM class Point(builtins.object)
@REM  |  Point(x: float = 0, y: float = 0) -> None
@REM  |
@REM  |  Represents a point in two-dimensional geometric coordinates
@REM  |
@REM  |  >>> p_0 = Point()
@REM  |  >>> p_1 = Point(3, 4)
@REM  |  >>> p_0.calculate_distance(p_1)
@REM  |  5.0
@REM  |
@REM  |  Methods defined here:
@REM  |
@REM  |  __init__(self, x: float = 0, y: float = 0) -> None
@REM  |      Initialize the position of a new point. The x and y coordinates
@REM  |      can be specified. If they are not, the point defaults to the origin
@REM  |
@REM  |      Parameters
@REM  |      ----------
@REM  |      x : float, optional
@REM  |          x-coordinate, by default 0
@REM  |      y : float, optional
@REM  |          y-coordinate, by default 0
@REM  |
@REM  |  calculate_distance(self, other: 'Point') -> float
@REM  |      Calculate the Euclidean distance from this point
@REM  |      to a second point passed as a parameter
@REM  |
@REM  |      Parameters
@REM  |      ----------
@REM  |      other : Point
@REM  |          instance
@REM  |
@REM  |      Returns
@REM  |      -------
@REM  |      float
@REM  |          distance
@REM  |
@REM  |  move(self, x: float, y: float) -> None
@REM  |      Move the point to a new location in 2D space
@REM  |
@REM  |      Parameters
@REM  |      ----------
@REM  |          x-coordinate
@REM  |      y : float
@REM  |          y-coordinate
@REM  |
@REM  |  reset(self) -> None
@REM  |      Reset the point back to the geometric origin: 0, 0
@REM  |
@REM  |  ----------------------------------------------------------------------
@REM  |  Data descriptors defined here:
@REM  |
@REM  |  __dict__
@REM  |      dictionary for instance variables (if defined)
@REM  |
@REM  |  __weakref__
@REM  |      list of weak references to the object (if defined)

@REM 可以测试文档
python -m doctest point_docstrings.py
@REM python -m doctest point_docstrings.py -v
@REM v 是 Verbose的缩写吗
@REM 不知道是不是这一行命令更好（或者不同在哪里）

@REM 对文件夹下的全部 python 文件测试类型提示和返回值
mypy --strict folder_name