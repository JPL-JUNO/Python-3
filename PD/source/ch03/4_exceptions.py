"""
@File         : 4_exceptions.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-05-18 14:24:36
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

try:
    file = open("foo.txt", "rt")
except FileNotFoundError:
    print("Well, that didn't work")
    raise

try:
    int("N/A")  # Raises ValueError
except ValueError as e:
    print("Failed:", e)

print(e)  # Fails -> NameError. 'e' not defined.

try:
    pass
except TypeError as e:
    pass
except ValueError as e:
    pass

try:
    pass
except (TypeError, ValueError) as e:
    pass

try:
    pass
except Exception as e:
    print(f"An error occurred : {e!r}")

try:
    file = open("foo.txt", "rt")
except FileNotFoundError as e:
    print(f"Unable to open foo : {e}")
    data = ""
else:
    data = file.read()
    file.close()

file = open("foo.txt", "rt")
try:
    # Do some stuff
    pass
finally:
    # File closed regardless of what happened
    file.close()

try:
    item = items[index]
except IndexError:  # Raised if items is a sequence
    pass
except KeyError:  # Raised if items is a mapping
    pass

try:
    item = items[index]
except LookupError:
    pass

import sys

if len(sys.argv) != 2:
    raise SystemExit(f"Usage: {sys.argv[0]} filename")
filename = sys.argv[1]
