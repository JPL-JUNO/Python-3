"""
@Title: 方片问题 diamond problem
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-14 21:38:21
@Description: 
"""
from commerce_v3 import AddressHolder
from commerce_v1 import Contact


class Friend(Contact, AddressHolder):
    def __init__(self, name: str, email: str,
                 phone: str, street: str, city: str, state: str, code: str) -> None:
        Contact.__init__(self, name, email)
        AddressHolder.__init__(self, street, city, state, code)
        self.phone = phone


# 这里是展示多重继承的问题
class BaseClass:
    num_base_calls = 0

    def call_me(self) -> None:
        print("Calling method on BaseClass")
        self.num_base_calls += 1


class LeftSubclass(BaseClass):
    num_left_calls = 0

    def call_me(self) -> None:
        BaseClass.call_me(self)
        print("Calling method on LeftSubclass")
        self.num_left_calls += 1


class RightSubclass(BaseClass):
    num_right_calls = 0

    def call_me(self) -> None:
        BaseClass.call_me(self)
        print("Calling method on RightSubclass")
        self.num_right_calls += 1


class SubClass(LeftSubclass, RightSubclass):
    num_sub_calls = 0

    def call_me(self) -> None:
        LeftSubclass.call_me(self)
        RightSubclass.call_me(self)
        print("Calling method on SubClass")
        self.num_sub_calls += 1


# Python's Method Resolution Order
# (MRO) algorithm transforms the diamond
# into a flat, linear tuple.


class BaseClass_S:
    num_base_calls = 0

    def call_me(self) -> None:
        print("Calling method on BaseClass_S")
        self.num_base_calls += 1


class LeftSubclass_S(BaseClass_S):
    num_left_calls = 0

    def call_me(self) -> None:
        super().call_me()
        print("Calling method on LeftSubclass_S")
        self.num_left_calls += 1


class RightSubclass_S(BaseClass_S):
    num_right_calls = 0

    def call_me(self) -> None:
        super().call_me()
        print("Calling method on RightSubclass_S")
        self.num_right_calls += 1


class SubClass_S(LeftSubclass_S, RightSubclass_S):
    num_sub_calls = 0

    def call_me(self) -> None:
        super().call_me()
        print("Calling method on SubClass_S")
        self.num_sub_calls += 1


if __name__ == "__main__":
    s = SubClass()
    s.call_me()
    assert s.num_sub_calls == 1
    assert s.num_right_calls == 1
    assert s.num_left_calls == 1
    # 如果说一个存款，可能导致存两边
    assert s.num_base_calls == 2
    print()
    print("===== super() =====")
    s_S = SubClass_S()
    s_S.call_me()
    assert s_S.num_base_calls == 1
    assert s_S.num_right_calls == 1
    assert s_S.num_left_calls == 1
    assert s_S.num_base_calls == 1

    from pprint import pprint
    pprint(SubClass_S.__mro__)
    # (<class '__main__.SubClass_S'>,
    # <class '__main__.LeftSubclass_S'>,
    # <class '__main__.RightSubclass_S'>,
    # <class '__main__.BaseClass_S'>,
    # <class 'object'>)


# Let's look at the output from back to front to see who is calling what:
# 1. We start with the Subclass_S.call_me() method. This evaluates
# super().call_me(). The MRO shows LeftSubclass_S as next.
# 2. We begin evaluation of the LeftSubclass_S.call_me() method. This
# evaluates super().call_me(). The MRO puts RightSubclass_S as next. This
# is not a superclass; it's adjacent in the class diamond.
# 3. The evaluation of the RightSubclass_S.call_me() method, super().call_me().
# This leads to BaseClass.
# 4. The BaseClass.call_me() method finishes its processing: printing
# a message and setting an instance variable, self.num_base_calls, to
# BaseClass.num_base_calls + 1.
# 5. Then, the RightSubclass_S.call_me() method can finish, printing a message
# and setting an instance variable, self.num_right_calls.
# 6. Then, the LeftSubclass_S.call_me() method will finish by printing a
# message and setting an instance variable, self.num_left_calls.
# 7. This serves to set the stage for Subclass_S to finish its call_me() method
# processing. It writes a message, sets an instance variable, and rests, happy
# and successful.
