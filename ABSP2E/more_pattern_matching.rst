>>> import re
>>>
>>> phone_num_regex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
>>> mo = phone_num_regex.search("My number is 415-555-4242.")
>>> mo.group(1)
'415'
>>> mo.group(2)
'555-4242'
>>> mo.group(0)
'415-555-4242'
>>> mo.groups()
('415', '555-4242')
>>> mo.group()
'415-555-4242'
>>>

>>> area_code, main_number = mo.groups()
>>> print(area_code)
415
>>> print(main_number)
555-4242
>>>

>>> phone_num_regex = re.compile(r"(\(\d\d\d\))-(\d\d\d-\d\d\d\d)")
>>> mo = phone_num_regex.search("My number is (415)-555-4242")
>>> mo.group(1)
'(415)'
>>> mo.group(2)
'555-4242'
>>>

>>> re.compile(r"(\(Parentheses\)")
Traceback (most recent call last):
--snip--
re.error: missing ), unterminated subpattern at position 0
>>>

>>> hero_regex = re.compile(r"Batman|Tina Fey")
>>> mo1 = hero_regex.search("Batman and Tina Fey")
>>> mo1.group()
'Batman'
>>> mo2 = hero_regex.search("Tina Fey and Batman")
>>> mo2.group()
'Tina Fey'
>>>

可以使用管道来匹配多个模式中的一个，作为正则表达式的一部分。

>>> bat_regex = re.compile(r"Bat(man|mobile|copter|bat)")
>>> mo = bat_regex.search("Batmobile lost a wheel")
>>> mo.group()
'Batmobile'
>>> mo.group(1)
'mobile'
>>>

字符 ? 表明它前面的分组在这个模式中是可选的。

>>> bat_regex = re.compile(r"Bat(wo)?man")
>>> mo1 = bat_regex.search("The Adventures of Batman")
>>> mo1.group()
'Batman'
>>>
>>> mo2 = bat_regex.search("The Adventures of Batwoman")
>>> mo2.group()
'Batwoman'
>>>

*（称为星号）意味着“匹配零次或多次”，即星号之前的分组，可以在文本中出现任意次。它可以完全不存在，或一次又一次地重复。

>>> bat_regex = re.compile(r"Bat(wo)*man")
>>> mo1 = bat_regex.search("The Adventures of Batman")
>>> mo1.group()
'Batman'
>>> mo2 = bat_regex.search("The Adventures of Batwoman")
>>> mo2.group()
'Batwoman'
>>> mo3 = bat_regex.search("The Adventures of Batwowowowoman")
>>> mo3.group()
'Batwowowowoman'
>>>

>>> bat_regex = re.compile(r"Bat(wo)+man")
>>> mo1 = bat_regex.search("The Adventure of Batwoman")
>>> mo1.group()
'Batwoman'
>>> mo2 = bat_regex.search("The Adventures of Batwowowowoman")
>>> mo2.group()
'Batwowowowoman'
>>> mo3 = bat_regex.search("The Adventure of Batman")
>>> mo3 == None
True

>>> ha_regex = re.compile(r"(Ha){3}")
>>> mo1 = ha_regex.search("HaHaHa")
>>> mo1.group()
'HaHaHa'
>>> mo2 = ha_regex.search("Ha")
>>> mo2 == None
True
>>>

================
贪心和非贪心匹配
================

>>> greedy_ha_regex = re.compile(r"(Ha){3,5}")
>>> mo1 = greedy_ha_regex.search("HaHaHaHaHa")
>>> mo1.group()
'HaHaHaHaHa'
>>> non_greedy_ha_regex = re.compile(r"(Ha){3,5}?")
>>> mo2 = non_greedy_ha_regex.search("HaHaHaHaHa")
>>> mo2.group()
'HaHaHa'
>>>