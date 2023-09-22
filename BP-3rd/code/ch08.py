# 1 / 0  # ZeroDivisionError: division by zero

# raise Exception  # Exception:
# raise Exception("hyperdrive overload")  # Exception: hyperdrive overload


from warnings import warn
from warnings import filterwarnings
filterwarnings('error')
warn('This function is really old...', DeprecationWarning)
# DeprecationWarning: This function is really old...

filterwarnings('ignore', category=DeprecationWarning)
warn('Another deprecation warning', DeprecationWarning)
warn('Something else')  # UserWarning: Something else


class SomeCustomException(Exception):
    pass


# try:
#     x = int(input('Enter the first number: '))
#     y = int(input('Enter the second number: '))
#     print(x / y)
# except ZeroDivisionError:
#     print("The second number can't be zero.")


class MuffledCalculator:
    muffled = False

    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print('Division by zero is illegal')
            else:
                raise


calculator = MuffledCalculator()
calculator.calc('10 / 2')  # 5.0
# calculator.calc('10 / 0')  # ZeroDivisionError: division by zero
calculator.muffled = True
calculator.calc('10 / 0')  # Division by zero is illegal
ret = calculator.calc('10 / 0')
print(ret)  # None

# try:
#     1/0
# except ZeroDivisionError:
#     raise ValueError from Exception

# try:
#     x = int(input('Enter the first number: '))
#     y = int(input('Enter the second number: '))
# except:
#     print('Something wrong happened...')

try:
    print('A simple example')
except:
    print('What? Something went wrong ... ')
else:
    print('Ah ... It went as planned.')
# A simple example
# Ah ... It went as planned.

# while True:
#     try:
#         x = int(input('Enter the first number: '))
#         y = int(input('Enter the second number: '))
#         value = x / y
#         print('x / y is', value)
#     except Exception as e:
#         print('Invalid input.', e)
#         print('Please try again.')
#     else:
#         break
# Invalid input. division by zero
# Please try again.
# Invalid input. invalid literal for int() with base 10: 'a'
# Please try again.
# x / y is 0.5

try:
    1 / 0
except ZeroDivisionError:
    print('Unknown variable')
else:
    print('That went well!')
finally:
    print('Cleaning up...')


def faulty():
    raise Exception('Something went wrong!')


def ignore_exception():
    faulty()


def handle_exception():
    try:
        faulty()
    except:
        print('Exception handled.')


# faulty()  # Exception: Something went wrong!
# handle_exception()  # Exception handled.

def describe_person(person):
    print('Description of', person['name'])
    print('Age: ', person['age'])
    if 'occupation' in person:
        print('Occupation: ', person['occupation'])


person = {'name': 'John', 'age': 42}
describe_person(person)
# Description of John
# Age:  42


def describe_person(person):
    print('Description of', person['name'])
    print('Age: ', person['age'])
    try:
        print('Occupation: ', person['occupation'])
    except:
        pass


describe_person(person)
# try:
#     obj.write
# except AttributeError:
#     print('The object is not writeable')
# else:
#     print('The object is writeable')

# warn("I've got a bad feeling about this.")
# UserWarning: I've got a bad feeling about this.
