"""
@File         : 4_a_second_example.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-01-26 22:42:03
@Email        : cuixuanstephen@gmail.com
@Description  : Intersecting Sequences
"""


def intersect(seq1, seq2):
    # our intersect function is fairly slow (it executes nested loops)
    # 而且不是真正的交集
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res


s1 = "SPAM"
s2 = "SCAM"
# [x for x in s1 if x not in s2]
intersect(s1, s2)

x = intersect([1, 2, 3], (1, 4))
