"""
@File         : coding_class_trees.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-08 23:59:50
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""


class C2:  # Make class objects (ovals)
    pass


class C3:
    pass


class C1(C2, C3):  # Linked to superclasses (in this order)
    def __init__(self) -> None:
        super().__init__()

    def set_name(self, who):
        self.name = who


I1 = C1()  # Make instance objects (rectangles)
I2 = C1()  # Linked to their classes
I1.set_name("bob")
I2.set_name("sue1")
print(I1.name)
