"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-11 22:22:36
@Description: 
"""
import enum

# For more control over the values associated with members, the names string can be replaced
# with a sequence of two-part tuples or a dictionary mapping names to values.

BugStatus = enum.Enum(value="BugStatus",  # value 参数是枚举名，用于构建成员的标识
                      names=[
                          ('new', 7),
                          ('incomplete', 6),
                          ('invalid', 5),
                          ('wont_fix', 4),
                          ('in_progress', 3),
                          ('fix_committed', 2),
                          ('fix_released', 1),
                      ],
                      )

print("Member: {}".format(BugStatus.new))
print("\nAll members:")
for status in BugStatus:
    print("{:15} = {}".format(status.name, status.value))
