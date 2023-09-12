"""
@Title: 迭代
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-11 21:53:27
@Description: 
"""
import enum


class BugStatus(enum.Enum):
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1


for status in BugStatus:
    # 迭代处理 enum 类会生成枚举的各个成员
    # 这些成员按它们在类定义中声明的顺序生成
    # 不会用名和值来对它们排序
    print("{:15} = {}".format(status.name, status.value))
