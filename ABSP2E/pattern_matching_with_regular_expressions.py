"""
@File         : pattern_matching_with_regular_expressions.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-13 13:31:00
@Email        : cuixuanstephen@gmail.com
@Description  : 模式匹配与正则表达式
"""

import re

phone_num_regex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
mo = phone_num_regex.search("My number is 415-555-4242. 456-555-4242")
mo.group(1)
mo.group(2)
mo.group(0)

mo.groups()
mo.group()

area_code, main_number = mo.groups()
print(area_code)
print(main_number)

phone_num_regex = re.compile(r"(\(\d\d\d\))-(\d\d\d-\d\d\d\d)")
mo = phone_num_regex.search("My number is (415)-555-4242")
mo.group(1)
mo.group(2)

# re.compile(r"(\(Parentheses\)")

hero_regex = re.compile(r"Batman|Tina Fey")
mo1 = hero_regex.search("Batman and Tina Fey")
mo1.group()
mo2 = hero_regex.search("Tina Fey and Batman")
mo2.group()

bat_regex = re.compile(r"Bat(man|mobile|copter|bat)")
mo = bat_regex.search("Batmobile lost a wheel")
mo.group()
mo.group(1)

bat_regex = re.compile(r"Bat(wo)?man")
mo1 = bat_regex.search("The Adventures of Batman")
mo1.group()

mo2 = bat_regex.search("The Adventures of Batwoman")
mo2.group()

bat_regex = re.compile(r"Bat(wo)*man")
mo1 = bat_regex.search("The Adventures of Batman")
mo1.group()
mo2 = bat_regex.search("The Adventures of Batwoman")
mo2.group()
mo3 = bat_regex.search("The Adventures of Batwowowowoman")
mo3.group()

bat_regex = re.compile(r"Bat(wo)+man")
mo1 = bat_regex.search("The Adventure of Batwoman")
mo1.group()

mo2 = bat_regex.search("The Adventures of Batwowowowoman")
mo2.group()

mo3 = bat_regex.search("The Adventure of Batman")
mo3 == None

ha_regex = re.compile(r"(Ha){3}")
mo1 = ha_regex.search("HaHaHa")
mo1.group()
mo2 = ha_regex.search("Ha")
mo2 == None


greedy_ha_regex = re.compile(r"(Ha){3,5}")
mo1 = greedy_ha_regex.search("HaHaHaHaHa")
mo1.group()
non_greedy_ha_regex = re.compile(r"(Ha){3,5}?")
mo2 = non_greedy_ha_regex.search("HaHaHaHaHa")
mo2.group()

phone_num_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
mo = phone_num_regex.search('Cell" 415-555-9999 Work: 212-555-0000')
mo.group()

phone_num_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")  # has no groups
phone_num_regex.findall('Cell" 415-555-9999 Work: 212-555-0000')

phone_num_regex = re.compile(r"(\d\d\d)-(\d\d\d)-(\d\d\d\d)")  # has groups
phone_num_regex.findall('Cell" 415-555-9999 Work: 212-555-0000')

xmas_regex = re.compile(r"\d+\s\w+")
xmas_regex.findall("12 drummers,8 maids, 7 swans, 6 geese")

vowel_regex = re.compile(r"[aeiouAEIOU]")
vowel_regex.findall("RoboCop eats")

constant_regex = re.compile(r"[^aeiouAEIOU]")
constant_regex.findall("RoboCop eats")

begins_with_hello = re.compile(r"^Hello")
begins_with_hello.search("Hello, world!")
begins_with_hello.search("He said hello.") == None

end_with_number = re.compile(r"\d$")
end_with_number.search("Your number is 42")
end_with_number.search("Your number is forty two.") == None

whole_string_num = re.compile(r"^\d+$")
whole_string_num.search("1234567890")
whole_string_num.search("12345xyz67890") == None
whole_string_num.search("12 2345678") == None


at_regex = re.compile(r".at")
at_regex.findall("The cat in the hat sat on the flat mat.")

name_regex = re.compile(r"First Name: (.*) Last Name: (.*)")
mo = name_regex.search("First Name: Al Last Name: Sweigart")
mo.group(1)
mo.group(2)

non_greedy_regex = re.compile(r"<.*?>")
mo = non_greedy_regex.search("<To serve man> for dinner.>")
mo.group()

greedy_regex = re.compile(r"<.*>")
mo = greedy_regex.search("<To serve man> for dinner.>")
mo.group()


no_new_line_regex = re.compile(".*")
mo = no_new_line_regex.search("Serve the public trust.\nProtect the innocent\n")
mo.group()

new_line_regex = re.compile(".*", re.DOTALL)
mo = new_line_regex.search("Serve the public trust.\nProtect the innocent\n")
mo.group()

robocop = re.compile(r"robocop", re.I)
robocop.search("RoboCop is part man, part machine, all cop.").group()
robocop.search("ROBOCOP protects the innocent.").group()
robocop.search("Al, why does your programming book talk about robocop so much?").group()

names_regex = re.compile(r"Agent \w+")
names_regex.sub("CENSORED", "Agent Alice gave the secret documents to Agent Bob.")

agent_names_regex = re.compile(r"Agent (\w)\w+")
agent_names_regex.sub(r"\1****", "Agent Alice gave the secret documents to Agent Bob.")


phone_regex = re.compile(
    r"((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)"
)

phone_regex = re.compile(
    r"""(
    (\d{3}|\(\d{3}\))?# area code
    (\s|-|\.)?# separator
    \d{3}# first 3 digits
    (\s|-|\.)?# separator
    \d{4} # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})? # extension
    )""",
    re.VERBOSE,
)

some_regex_value = re.compile(r"foo", re.IGNORECASE | re.DOTALL)
some_regex_value = re.compile(r"foo", re.IGNORECASE | re.DOTALL | re.VERBOSE)
