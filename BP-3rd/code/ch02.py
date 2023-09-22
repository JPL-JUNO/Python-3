# months = ["January", "February", "March", "April", "May", "June",
#           "July", "August", "September", "October", "November", "December"]
# endings = ["st", "nd", "rd"] + 17 * ["th"] \
#     + ["st", "nd", "rd"] + 7 * ["th"]\
#     + ["st"]
# year = input("Year: ")
# month = input("Month: ")
# day = input("Day: ")

# month_number = int(month)
# day_number = int(day)
# month_name = months[month_number-1]
# ordinal = day + endings[day_number-1]

# print(month_name + " "+ordinal + ', ' + year)

tag = "<a href='http://www.python.org'>Python web site</a>"
tag[9:30]  # 'http://www.python.org'

tag[32:-4]  # 'Python web site'

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers[3:6]  # [4, 5, 6]
numbers[0:1]  # [1]

numbers[7:10]

numbers[-3:-1]
numbers[-3:0]

# url = input("Please enter the URL: ")
# domain = url[11:-4]
# print("Domain name: " + domain)

numbers[0:10:1]
numbers[0:10:2]  # [1, 3, 5, 7, 9]

numbers[3:6:3]  # [4]

numbers[8:3:-1]  # [9, 8, 7, 6, 5]
numbers[10:0:-1]  # [10, 9, 8, 7, 6, 5, 4, 3, 2]
numbers[:5:-2]  # [10, 8]
numbers[5::-2]  # [10, 8]

[1, 2, 3] + [4, 5, 6]  # [1, 2, 3, 4, 5, 6]
"Hello, " + "Python!"  # 'Hello, Python!'
# TypeError: can only concatenate list (not "str") to list
# [1, 2, 3] + "Python!"

"Python" * 5  # 'PythonPythonPythonPythonPython'
[42] * 10  # [42, 42, 42, 42, 42, 42, 42, 42, 42, 42]

sequence = [None] * 10
# print(sequence)  # [None, None, None, None, None, None, None, None, None, None]


permissions = "rw"
"w" in permissions  # True
"x" in permissions  # False
user = ["mlh", "foo", "bar"]
# input("Enter your user name: ") in user
subject = '$$ Get rich now !!!'
"$$" in subject  # True

# database = [
#     ['albert', '1234'],
#     ['dilbert', '4242'],
#     ['smith', '7523'],
#     ['jones', '9753']
# ]
# username = input('User name: ')
# pin = input("PIN code: ")
# if [username, pin] in database:
#     print("Access Granted")

numbers = [100, 34, 678]
len(numbers)  # 3
max(numbers)  # 678
min(numbers)  # 34

max(2, 3)  # 3
min(9, 3, 2, 5)  # 2

list("Hello")  # ['H', 'e', 'l', 'l', 'o']
list(["Hello"])
list(("Hello", "World", "Python"))  # ['Hello', 'World', 'Python']

x = [1] * 3
x[1] = 2
x  # [1, 2, 1]

names = ["Alice", "Beth", "Cecil", "Dee-Dee", "Earl"]
del names[2]
names  # ['Alice', 'Beth', 'Dee-Dee', 'Earl']

name = list("Perl")
name  # ['P', 'e', 'r', 'l']
name[2:] = list("ar")
name  # ['P', 'e', 'a', 'r']

name = list("Perl")
name[1:] = list("ython")
name  # ['P', 'y', 't', 'h', 'o', 'n']

numbers = [1, 5]
numbers[1:1] = [2, 3, 4]
numbers  # [1, 2, 3, 4, 5]

numbers[1:4] = []
numbers  # [1, 5]

lst = [1, 2, 3]
lst.append(4)
lst  # [1, 2, 3, 4]

lst = [1, 2, 3]
ret = lst.append(4)
# print(ret)  # None

lst = [1, 2, 3]
lst.clear()
lst  # []

a = [1, 2, 3]
b = a
b[1] = 4
a  # [1, 4, 3]

a = [1, 2, 3]
b = a.copy()
b[1] = 4
a  # [1, 2, 3]

a = [1, 2, 3]
b = a[:]
b[1] = 4
a  # [1, 2, 3]

a = [1, 2, 3]
b = list(a)
b[1] = 4
a  # [1, 2, 3]

a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
a  # [1, 2, 3, 4, 5, 6]

a = [1, 2, 3]
a + b
a  # [1, 2, 3]

a = [1, 2, 3]
b = [4, 5, 6]
a[len(a):] = b
a  # [1, 2, 3, 4, 5, 6]

knights = ['We', 'are', 'the', 'knights', 'who', 'say', 'ni']
knights.index('who')  # 4
# knights.index('Stephen')  # ValueError: 'Stephen' is not in list

['to', 'be', 'or', 'not', 'to', 'be'].count('to')  # 2
x = [[1, 2], 1, 1, [2, 1, [1, 2]]]
x.count(1)  # 2
x.count([1, 2])  # 1

numbers = [1, 2, 3, 5, 6, 7]
numbers.insert(3, 'four')
numbers  # [1, 2, 3, 'four', 5, 6, 7]

numbers = [1, 2, 3, 5, 6, 7]
numbers[3:3] = ['four']
numbers  # [1, 2, 3, 'four', 5, 6, 7]

x = [1, 2, 3]
x.pop()  # 3
x  # [1, 2]
x.pop(0)
x  # [2]

x = [1, 2, 4]
x.append(x.pop())
x  # [1, 2, 4]

# x = ['to', 'be', 'or', 'not', 'to', 'be']
# x.remove('be')
# x  # ['to', 'or', 'not', 'to', 'be']
# x.remove('bee')  # list.remove(x): x not in list

x = [7, 9, 3]
x.reverse()
x  # [3, 9, 7]

x = [4, 6, 2, 1, 7, 9]
y = x.sort()
x  # [1, 2, 4, 6, 7, 9]
# print(y)  # None

x = ['aardvark', 'abalone', 'acme', 'add', 'aerate']
x.sort(key=len)
x  # ['add', 'acme', 'aerate', 'abalone', 'aardvark']

x = ['aardvark', 'abalone', 'acme', 'add', 'aerate']
x.sort(key=len, reverse=True)
x  # ['aardvark', 'abalone', 'aerate', 'acme', 'add']

1, 2, 3  # (1, 2, 3)
(1, 2, 3)  # (1, 2, 3)
()  # ()
42,  # (42,)

tuple([1, 2, 4])  # (1, 2, 4)
tuple('abc')  # ('a', 'b', 'c')
tuple((1, 2, 3))  # (1, 2, 3)
