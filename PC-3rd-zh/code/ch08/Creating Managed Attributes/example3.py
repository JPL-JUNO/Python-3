"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-31 13:58:42
@Description: 有时候 Java 程序员会觉得所有的访问都需要通过 getter 和 setter 来处理
"""


class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

# 如果 property 并不会完成任何额外的处理任务，就不要把代码写成上面这个样子。
# 第一，这么做会使得代码变得更加啰嗦，对其他人来说也比较困惑。
# 第二，这么做会让程序变慢很多。
# 最后，这么做不会给设计带来真正的好处。
