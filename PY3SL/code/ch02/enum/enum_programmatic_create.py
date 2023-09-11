"""
@Title: 通过编程创建枚举
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-11 22:16:17
@Description: 
"""

import enum

BugStatus = enum.Enum(value="BugStatus",  # value 参数是枚举名，用于构建成员的标识
                      names=('fixed_released fix_committed in_progress \
                             wont_fix invalid incomplete new')  # names 参数会列出枚举的成员。传递单个字符串时，会按空白符和逗号拆分
                      #   所得到的 token 会被用作成员名，这些成员还没自动赋值，从 1 开始
                      )

print("Member: {}".format(BugStatus.new))
print("\nAll members:")
for status in BugStatus:
    print("{:15} = {}".format(status.name, status.value))
