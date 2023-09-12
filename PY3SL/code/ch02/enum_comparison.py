"""
@Title: 比较 Enum
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-11 21:57:00
@Description: 
"""
import enum
# 由于枚举成员是无须的，所以它们只支持按同一性 identity 和相等性 equality 进行比较


class BugStatus(enum.Enum):
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1


actual_state = BugStatus.wont_fix
desired_state = BugStatus.fix_released

print("Equality:",
      actual_state == desired_state,
      actual_state == BugStatus.wont_fix)
print("Identity:",
      actual_state is desired_state,
      actual_state is BugStatus.wont_fix)

# 大小比较会产生 TypeError 异常
try:
    print("\n".join(' ' + s.name for s in sorted(BugStatus)))
except TypeError as err:
    print(" Cannot sort: {}".format(err))

# 有些枚举中的成员要表现得更像数字，例如，要支持比较，对于这些枚举要使用 IntEnum
