# """
# @Title:
# @Author(s): Stephen CUI
# @LastEditor(s): Stephen CUI
# @CreatedTime: 2023-09-04 16:28:42
# @Description:
# """


def square(x):
    """
    计算平方并返回结果
    >>> square(2)
    4
    >>> square(3)
    9
    """
    return x * x


if __name__ == "__main__":
    import doctest
    import my_math
    # doctest.testmod读取模块中所有文档字符串，查找看起来像是从交互式解释其中摘取的示例，
    # 再检查这些示例是否反映了实际情况
    doctest.testmod(my_math)
