from abc import ABC, abstractmethod
1 + 2  # 3
'Fish ' + 'license'  # 'Fish license'


def length_message(x):
    print('The length of', repr(x), 'is', len(x))


length_message('Hello, world!')  # The length of 'Hello, world!' is 13
length_message([1, 2, 3])  # The length of [1, 2, 3] is 3


class Person():
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def greet(self):
        print("Hello, world! I'm {}.".format(self.name))


foo = Person()
bar = Person()
foo.set_name('Luke Skywalker')
bar.set_name('Anakin Skywalker')
foo.greet()  # Hello, world! I'm Luke Skywalker.
bar.greet()  # Hello, world! I'm Anakin Skywalker.


class Class:
    def method(self):
        print("I have a self!")


def function():
    print("I don't...")


instance = Class()
instance.method()  # I have a self!
instance.method = function
instance.method()  # I don't...


class Bird():
    song = 'Squaawk!'

    def sing(self):
        print(self.song)


bird = Bird()
bird.sing()  # Squaawk!
birdsong = bird.sing
birdsong()  # Squaawk!


class Secretive():
    def __inaccessible(self):
        print("Bet you can't see me...")

    def accessible(self):
        self.__inaccessible()


s = Secretive()
# s.__inaccessible  # 'Secretive' object has no attribute '__inaccessible'
s.accessible()  # Bet you can't see me...

s._Secretive__inaccessible()  # Bet you can't see me...


class MemberCounter:
    members = 0

    def init(self):
        MemberCounter.members += 1


m1 = MemberCounter()
m1.init()
MemberCounter.members  # 1
m2 = MemberCounter()
m2.init()
MemberCounter.members  # 2


m1.members = "Two"
m1.members  # 'Two'
m2.members  # 2


class Filter():
    def init(self):
        self.blocked = []

    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]


class SPAMFilter(Filter):  # SPAMFilter is a subclass of Filter
    def init(self):  # Overrides init method from Filter superclass
        self.blocked = ['SPAM']


f = Filter()
f.init()
f.filter([1, 2, 3])  # [1, 2, 3]

s = SPAMFilter()
s.init()
s.filter(["SPAM", "SPAM", "bacon", "SPAM", "SPAM", "Eggs"])
# ['bacon', 'Eggs']


issubclass(SPAMFilter, Filter)  # True
issubclass(Filter, SPAMFilter)  # False

SPAMFilter.__bases__  # (__main__.Filter,)
Filter.__bases__  # (object,)

s = SPAMFilter()
isinstance(s, SPAMFilter)  # True
isinstance(s, Filter)  # True
isinstance(s, str)  # False


class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)


class Talker:
    def talk(self):
        print('Hi, my value is', self.value)


class TalkingCalculator(Calculator, Talker):
    pass


tc = TalkingCalculator()
tc.calculate('1 + 2 * 3')
tc.talk()  # Hi, my value is 7


hasattr(tc, 'talk')  # True
hasattr(tc, 'fnord')  # False

callable(getattr(tc, 'talk', None))  # True
callable(getattr(tc, 'fnord', None))  # False

setattr(tc, 'name', 'Mr. Gumby')
tc.name  # 'Mr. Gumby'


class Talker(ABC):
    @abstractmethod
    def talk(self):
        pass


# Talker()  # TypeError: Can't instantiate abstract class Talker with abstract method talk


class Knigget(Talker):
    def talk(self):
        print("Ni!")


k = Knigget()
isinstance(k, Talker)  # True
k.talk()  # Ni!


class Herring:
    def talk(self):
        print('Blub.')


h = Herring()
isinstance(h, Talker)  # False

Talker.register(Herring)  # __main__.Herring
isinstance(h, Talker)  # True
issubclass(Herring, Talker)  # True


class Clam:
    pass


Talker.register(Clam)  # __main__.Clam
issubclass(Clam, Talker)  # True
c = Clam()
isinstance(c, Talker)  # True
c.talk()  # AttributeError: 'Clam' object has no attribute 'talk'
