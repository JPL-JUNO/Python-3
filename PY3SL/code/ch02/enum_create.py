"""
@Title: 创建枚举
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-11 21:47:31
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


print("\nMember name: {}".format(BugStatus.wont_fix.name))
print("Member value: {}".format(BugStatus.wont_fix.value))

# 解析这个类时， Enum 的成员会被转化为实例，每个实例有一个对应成员名的 name 属性
# 另外有一个 value 属性，对应为类定义中的名所赋的值
