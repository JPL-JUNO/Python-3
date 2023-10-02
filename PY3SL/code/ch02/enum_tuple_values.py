"""
@Title: 非整数成员值
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-11 22:25:47
@Description: 
"""

# 任何类型的对象都可以与成员关联
# 如果值是一个元组，那么成员会作为单个参数传递到 __init__()

import enum


class BugStatus(enum.Enum):
    # 每个成员值分别是一个元组
    # 包括数值 ID 和从当前状态迁移的一个合法变迁列表
    new = (7, ["incomplete", "invalid", "wont_fix", "in_progress"])
    incomplete = (6, ["new", "wont_fix"])
    invalid = (5, ['new'])
    wont_fix = (4, ['new'])
    in_progress = (3, ['new', 'fix_committed'])
    fix_committed = (2, ['in_progress', 'fix_released'])
    fix_released = (1, ['new'])

    def __init__(self, num, transitions):
        self.num = num
        self.transitions = transitions

    def can_transition(self, new_state):
        return new_state.name in self.transitions


print("Name:", BugStatus.in_progress)
print("Value:", BugStatus.in_progress.value)
print("Custom attribute:", BugStatus.in_progress.transitions)
print("Using attribute:", BugStatus.in_progress.can_transition(BugStatus.new))
