#!/cygdrive/d/Python3.11.1/python
# Purpose: Say hello

import argparse

parser = argparse.ArgumentParser(description="Say hello")
parser.add_argument(
    "-n", "--name", metavar="name", default="World", help="Name to greet"
)
args = parser.parse_args()
print(f"Hello, {args.name}!")
