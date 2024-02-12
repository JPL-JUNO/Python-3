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
