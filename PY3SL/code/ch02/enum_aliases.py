"""
@Title: 唯一枚举值
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-11 22:06:47
@Description: 
"""
import enum
# 有相同值得 Enum 成员会被处理为同一个成员对象的别名引用
# 别名可以避免 Enum 迭代器中出现重复的值

# 一个成员的规范名是与这个值关联的第一个名字


class BugStatus(enum.Enum):
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1

    by_design = 4
    closed = 1


for status in BugStatus:
    print("{:15} = {}".format(status.name, status.value))
print("\nSame: by_design is wont_fix: ",
      BugStatus.by_design is BugStatus.wont_fix)
print("Same: closed is fix_released: ",
      BugStatus.closed is BugStatus.fix_released)
