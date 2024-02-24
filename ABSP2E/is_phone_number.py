"""
@File         : is_phone_number.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-12 14:06:08
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""


def is_phone_number(text: str) -> bool:
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    for pos in (3, 7):
        if text[pos] != "-":
            return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


if __name__ == "__main__":
    print("Is 415-555-4242 a phone number?")
    print(is_phone_number("415-555-4242"))
    print("Is Moshi moshi a phone number?")
    print(is_phone_number("Moshi moshi"))

    message = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office."
    for i, _ in enumerate(message):
        chunk = message[i : i + 12]
        if is_phone_number(chunk):
            print("Phone number found: " + chunk)
    print("Done")
