>>> import pyinputplus as pyip
>>> response = pyip.inputNum()
response
'response' is not a number.
five
'five' is not a number.
5
>>> response
5
>>> 

>>> response = input('Enter a number: ')
Enter a number: 42
>>> response
'42'
>>> response = pyip.inputInt(prompt="Enter a number: ")
Enter a number: cat
'cat' is not an integer.
Enter a number: 42
>>> response
42
>>>

>>> response = pyip.inputNum('Enter Num: ', min=4)
Enter Num: 2
Number must be at minimum 4.
Enter Num: 4
>>> response
4
>>> response = pyip.inputNum("Enter Num: ", greaterThan=4)
Enter Num: 4
Number must be greater than 4.
Enter Num: 10
>>> response
10
>>> response = pyip.inputNum("Enter Num: ", min=4, lessThan=6)
Enter Num: 7
Number must be less than 6.
Enter Num: 3
Number must be at minimum 4.
Enter Num: 5
>>> response
5
>>>

>>> response = pyip.inputNum("Enter Num: ")
Enter Num: 42
>>> response
42
>>> response = pyip.inputNum("Enter Num: ", blank=True) 
Enter Num:
>>> response
''
>>>

>>> response = pyip.inputNum(limit=2)
cat
'cat' is not a number.
number
'number' is not a number.
Traceback (most recent call last):
--snip--
pyinputplus.RetryLimitException
>>>

如果十秒时候才键入 enter，那么就会 raise TimeoutException

>>> response = pyip.inputNum(timeout=10)
56
Traceback (most recent call last):
--snip--
pyinputplus.TimeoutException
>>>

>>> response = pyip.inputNum(limit=2, default=0)
hello
'hello' is not a number.
Stephen
'Stephen' is not a number.
>>> response
0
>>>

这个正则是额外允许的，本身你也可以输入 Num 类型数字

>>> response = pyip.inputNum(allowRegexes=[r"(I|V|X|L|C|D|M)+", r"zero"])
XLII
>>> response
'XLII'
>>>

>>> response = pyip.inputNum(blockRegexes=[r"[02468]$"])
42
This response is invalid.
38
This response is invalid.
43
>>>

>>> response = pyip.inputStr(
...     allowRegexes=[r"caterpillar", "category"], blockRegexes=[r"cat"]
... )
category
>>> response
'category'
>>>

>>> def adds_uo_to_ten(numbers):
...     numbers_lst = list(numbers)
...     for i, digit in enumerate(numbers_lst):
...         numbers_lst[i] = int(digit)
...     if sum(numbers_lst) != 10:
...         raise Exception(f"The digits must add up to 10, not {sum(numbers_lst)}.'")
...     return int(numbers)
...
>>>
>>> response = pyip.inputCustom(adds_uo_to_ten)
123
The digits must add up to 10, not 6.'
123456
The digits must add up to 10, not 21.'
1234
>>> response
1234
>>>