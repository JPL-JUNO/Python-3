"""
@File         : ex7.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-13 18:48:55
@Email        : cuixuanstephen@gmail.com
@Description  : 习题
"""

import re

# T18
num_regex = re.compile(r"\d+")
num_regex.sub("X", "12 drummers, 11 pipers, five rings, 3 hens")

# T20
thousand_regex = re.compile(r"^(\d{1,3})(,\d{3})*$")
thousand_regex.search("1,234")
thousand_regex.search("1,234,456")
thousand_regex.search("12,34") == None
thousand_regex.search("1234") == None

# T21
name_regex = re.compile(r"([A-Z]\w*\s)Nakamoto")
name_regex.search("Satoshi Nakamoto")
# re.compile(r"[A-Z][a-z]*\sNakamoto")
name_regex.search("Alice Nakamoto")
name_regex.search("RoboCop Nakamoto")
name_regex.search("haruto Nakamoto") == None
name_regex.search("Mr. Nakamoto") == None
name_regex.search("Nakamoto") == None

# T22
sentence_regex = re.compile(
    r"(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.",
    re.IGNORECASE,
)
sentence_regex.search("Alice eats apples.")
sentence_regex.search("Bob pets cats.")
sentence_regex.search("Carol throws baseballs.")
sentence_regex.search("BOB EATS CATS.")
sentence_regex.search("RoboCop eats apples.") == None
sentence_regex.search("ALICE THROWS FOOTBALLS.") == None
sentence_regex.search("Carol eats 7 cats.") == None
