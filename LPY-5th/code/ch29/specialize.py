class Super:
    def method(self):
        print("in Super.method")

    def delegate(self):  # Expected to be defined
        # 具体的实现交给子类去实现
        self.action()

    def action(self):
        assert False, "action must be defined"
        # raise NotImplemented('action must be defined')


class Inheritor(Super):  # Inherit method verbatim
    pass


class Replacer(Super):  # Replace method completely
    def method(self):
        print("in Replacer.method")


class Extender(Super):
    def method(self):  # Extend method behavior
        print("starting Extender.method")
        Super.method(self)
        print("ending Expender.method")


class Provider(Super):  # Fill in a required method
    def action(self):
        print("in Provider.action")


if __name__ == "__main__":
    for klass in (Inheritor, Replacer, Extender):
        print("\n" + klass.__name__ + "...")
        klass().method()
    print("\nProvider")
    x = Provider()
    x.delegate()
