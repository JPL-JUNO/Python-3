"""
classtree.py: Climb inheritance trees using namespace links,
displaying higher superclasses with indentation for height
"""


def class_tree(cls, indent):
    print("." * indent + cls.__name__)  # Print class name here
    for super_cls in cls.__bases__:  # Recur to all superclasses
        class_tree(super_cls, indent + 3)  # May visit super > once


def instance_tree(inst):
    print(f"Tree of {inst}")  # Show instance
    class_tree(inst.__class__, 3)  # Climb to its class


def self_test():
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B, C):
        pass

    class E:
        pass

    class F(D, E):
        pass

    instance_tree(B())
    instance_tree(F())


if __name__ == "__main__":
    self_test()
