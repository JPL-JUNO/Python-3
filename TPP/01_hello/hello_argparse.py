#!/cygdrive/d/Python3.11.1/python
# Purpose: Say hello

import argparse

parser = argparse.ArgumentParser(description="Say Hello")
parser.add_argument("name", help="Name to greet")
args = parser.parse_args()  # We ask the parser to parse any arguments to the program.

print(f"Hello, {args.name}!")
