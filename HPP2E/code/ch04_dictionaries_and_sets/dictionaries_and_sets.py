"""
@File         : dictionaries_and_sets.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-03-04 19:56:34
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""


def find_phone_number(phone_book, name):
    for n, p in phone_book:
        if n == name:
            return p
    return None


phone_book = [
    ("John Doe", "555-555-5555"),
    ("Albert Einstein", "212-555-5555"),
]
print(f"John Doe's phone number is {find_phone_number(phone_book, 'John Doe')}")

phone_book = {
    "John Doe": "555-555-5555",
    "Albert Einstein": "212-555-5555",
}
print(f"John Doe's phone number is {phone_book['John Doe']}")
