#!/cygdrive/d/Python3.11.1/python
"""
@File         : hello.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-09-06 21:36:53
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""
import argparse

parser = argparse.ArgumentParser(description="Say hello")
parser.add_argument(
    "-n", "--name", metavar="name", default="World", help="Name to greet"
)
args = parser.parse_args()
print(f"Hello, {args.name}!")
