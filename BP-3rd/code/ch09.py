class FooBar():
    def __init__(self, value=42):
        self.somevar = value


f = FooBar("This is constructor argument")
f.somevar  # 'This is constructor argument'


class A:
    def hello(self):
        print("Hello, I'm A.")


class B(A):
    def hello(self):
        print("Hello, I'm B")


a = A()
b = B()
a.hello()  # Hello, I'm A.
b.hello()  # Hello, I'm B.


class Bird:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('Aaaah....')
            self.hungry = False
        else:
            print('No, thanks!')


b = Bird()
b.eat()  # Aaaah....
b.eat()  # No, thanks!


class SongBird(Bird):
    def __init__(self):
        super().__init__()
        self.song = 'Squawk!'

    def sing(self):
        print(self.song)


sb = SongBird()
sb.sing()  # Squawk!

sb.eat()  # Aaaah....
sb.eat()  # No, thanks!


def check_index(key):
    """

    """
    if not isinstance(key, int):
        raise TypeError
    if key < 0:
        raise ValueError


class ArithmeticsSequence:
    def __init__(self, start=0, step=1):
        """
        """
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self, key):
        """
        """
        check_index(key)
        try:
            return self.changed[key]
        except KeyError:
            return self.start + key * self.step

    def __setitem__(self, key, value):
        """
        """
        check_index(key)
        self.changed[key] = value


s = ArithmeticsSequence(1, 2)
s[4]  # 9
s[4] = 2
s[4]  # 2

s[3]


class CounterList(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.counter = 0

    def __getitem__(self, index):
        self.counter += 1
        return super(CounterList, self).__getitem__(index)
        # return super().__getitem__(index)


cl = CounterList(range(10))
cl  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
cl.reverse()
cl  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
cl.counter  # 0

cl[4] + cl[2] + cl[3]
cl.counter  # 3


class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def set_size(self, size):
        self.width, self.height = size

    def get_size(self):
        return self.width, self.height

    size = property(get_size, set_size)


r = Rectangle()
r.width = 10
r.height = 5
r.get_size()  # (10, 5)
r.set_size((150, 100))
r.height  # 100


class MyClass:
    def smeth():
        print('This is a static method')
    smeth = staticmethod(smeth)

    def cmeth(cls):
        print('This is a class method of', cls)
    cmeth = classmethod(cmeth)


class MyClass:
    @staticmethod
    def smeth():
        print('This is a static method')

    @classmethod
    def cmeth(cls):
        print('This is a class method of', cls)


MyClass.smeth()  # This is a static method
MyClass.cmeth()  # This is a class method of <class '__main__.MyClass'>


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __setattr__(self, name, value):
        if name == 'size':
            self.width, self.height = value
        else:
            self.__dict__[name] = value

    def __getattr__(self, name):
        if name == 'size':
            return self.width, self.height
        else:
            raise AttributeError()


class Fibs():
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self


fibs = Fibs()
for i in fibs:
    if i > 1000:
        print(i)  # 1597
        break

it = iter([1, 2, 3])
next(it)  # 1
next(it)  # 2


class TestIterator:
    value = 0

    def __next__(self):
        self.value += 1
        if self.value > 10:
            raise StopIteration
        return self.value

    def __iter__(self):
        return self


ti = TestIterator()
list(ti)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element


nested = [[2, 2,], [4, 0], [5]]
for num in flatten(nested):
    print(num)
# or
list(flatten(nested))  # [2, 2, 4, 0, 5]

g = ((i + 2) ** 2 for i in range(2, 27))
next(g)  # 16
next(g)  # 25

sum(i ** 2 for i in range(10))


def flatten(nested):
    try:
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested


list(flatten([[[1, 2, 2], 1, [1, 2, 1], 1], 1, [1, 1, 1]]))
# [1, 2, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1]


def flatten(nested):
    try:
        try:
            nested + ''
        except TypeError:
            pass
        else:
            raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested


list(flatten(['foo', ['bar', ['baz']]]))
# ['foo', 'bar', 'baz']


def simple_generator():
    yield 1


simple_generator
# <function __main__.simple_generator()>
simple_generator()
# <generator object simple_generator at 0x000001BEF4C3D380>


def repeater(value):
    while True:
        new = (yield value)
        if new is not None:
            value = new


r = repeater(42)
next(r)  # 42
r.send('Hello, world')  # Hello, world


def flatten(nested):
    result = []
    try:
        try:
            nested + ''
        except TypeError:
            pass
        else:
            raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                result.append(element)
    except TypeError:
        result.append(nested)
    return result
