Methods:

[('__eq__', <function MyObject.__eq__ at 0x00000261E1340680>),
 ('__ge__', <function _ge_from_gt at 0x00000261E1061D00>),
 ('__gt__', <function MyObject.__gt__ at 0x00000261E1340720>),
 ('__init__', <function MyObject.__init__ at 0x00000261E12A34C0>),
 ('__le__', <function _le_from_gt at 0x00000261E1061120>),
 ('__lt__', <function _lt_from_gt at 0x00000261E1061800>)]

Comparisons:

a < b :
  testing __gt__(1, 2)
  testing __eq__(1, 2)
  result of a < b: True

a <= b:
  testing __gt__(1, 2)
  result of a <= b: True

a == b:
  testing __eq__(1, 2)
  result of a == b: False

a >= b:
  testing __gt__(1, 2)
  testing __eq__(1, 2)
  result of a >= b: False

a > b :
  testing __gt__(1, 2)
  result of a > b: False
