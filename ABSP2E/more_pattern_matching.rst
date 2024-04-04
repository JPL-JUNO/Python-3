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

>>> phone_num_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
>>> mo = phone_num_regex.search('Cell" 415-555-9999 Work: 212-555-0000')
>>> mo.group()
'415-555-9999'
>>>

>>> phone_num_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")  # has no groups
>>> phone_num_regex.findall('Cell" 415-555-9999 Work: 212-555-0000')
['415-555-9999', '212-555-0000']
>>> 

>>> phone_num_regex = re.compile(r"(\d\d\d)-(\d\d\d)-(\d\d\d\d)")  # has groups
>>> phone_num_regex.findall('Cell" 415-555-9999 Work: 212-555-0000')
[('415', '555', '9999'), ('212', '555', '0000')]
>>> 

>>> xmas_regex = re.compile(r"\d+\s\w+")
>>> xmas_regex.findall("12 drummers,8 maids, 7 swans, 6 geese")
['12 drummers', '8 maids', '7 swans', '6 geese']
>>> 

>>> vowel_regex = re.compile(r"[aeiouAEIOU]")
>>> vowel_regex.findall("RoboCop eats")
['o', 'o', 'o', 'e', 'a']
>>> 

>>> constant_regex = re.compile(r"[^aeiouAEIOU]")
>>> constant_regex.findall("RoboCop eats")
['R', 'b', 'C', 'p', ' ', 't', 's']
>>> 

>>> begins_with_hello = re.compile(r"^Hello")
>>> begins_with_hello.search("Hello, world!")
<re.Match object; span=(0, 5), match='Hello'>
>>> begins_with_hello.search("He said hello.") == None
True
>>> 


>>> end_with_number = re.compile(r"\d$")
>>> end_with_number.search("Your number is 42")
<re.Match object; span=(16, 17), match='2'>
>>> end_with_number.search("Your number is forty two.") == None
True
>>>

>>> whole_string_num = re.compile(r"^\d+$")
>>> whole_string_num.search("1234567890")
<re.Match object; span=(0, 10), match='1234567890'>
>>> whole_string_num.search("12345xyz67890") == None
True
>>> whole_string_num.search("12 2345678") == None
True
>>>

>>> at_regex = re.compile(r".at")
>>> at_regex.findall("The cat in the hat sat on the flat mat.")
['cat', 'hat', 'sat', 'lat', 'mat']

>>> name_regex = re.compile(r"First Name: (.*) Last Name: (.*)")
>>> mo = name_regex.search("First Name: Al Last Name: Sweigart")
>>> mo.group(1)
'Al'
>>> mo.group(2)
'Sweigart'
>>>

>>> greedy_regex = re.compile(r"<.*>")
>>> mo = greedy_regex.search("<To serve man> for dinner.>")
>>> mo.group()
'<To serve man> for dinner.>'
>>>

>>> no_new_line_regex = re.compile(".*")
>>> mo = no_new_line_regex.search("Serve the public trust.\nProtect the innocent\n")
>>> mo.group()
'Serve the public trust.'
>>>
>>> new_line_regex = re.compile(".*", re.DOTALL)
>>> mo = new_line_regex.search("Serve the public trust.\nProtect the innocent\n")
>>> mo.group()
'Serve the public trust.\nProtect the innocent\n'
>>>

>>> robocop = re.compile(r"robocop", re.I)
>>> robocop.search("RoboCop is part man, part machine, all cop.").group()
'RoboCop'
>>> robocop.search("ROBOCOP protects the innocent.").group()
'ROBOCOP'
>>> robocop.search("Al, why does your programming book talk about robocop so much?").group()
'robocop'
>>>

>>> names_regex = re.compile(r"Agent \w+")
>>> names_regex.sub("CENSORED", "Agent Alice gave the secret documents to Agent Bob.")
'CENSORED gave the secret documents to CENSORED.'
>>>

>>> agent_names_regex = re.compile(r"Agent (\w)\w+")
>>> agent_names_regex.sub(r"\1****", "Agent Alice gave the secret documents to Agent Bob.")
'A**** gave the secret documents to B****.'
>>> 

>>> phone_regex = re.compile(
...     r"((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)"
... )
>>>
>>> phone_regex = re.compile(
...     r"""(
...     (\d{3}|\(\d{3}\))?# area code
...     (\s|-|\.)?# separator
...     \d{3}# first 3 digits
...     (\s|-|\.)?# separator
...     \d{4} # last 4 digits
...     (\s*(ext|x|ext.)\s*\d{2,5})? # extension
...     )""",
...     re.VERBOSE,
... )
>>>

>>> some_regex_value = re.compile(r"foo", re.IGNORECASE | re.DOTALL)
>>> some_regex_value = re.compile(r"foo", re.IGNORECASE | re.DOTALL | re.VERBOSE)
>>>