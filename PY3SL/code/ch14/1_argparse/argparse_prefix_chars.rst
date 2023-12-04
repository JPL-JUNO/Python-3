D:\DS_Works\Python-3\PY3SL\code\ch14\1_argparse>python argparse_prefix_chars.py
Namespace(a=None, noarg=False)

D:\DS_Works\Python-3\PY3SL\code\ch14\1_argparse>python argparse_prefix_chars.py -h
usage: argparse_prefix_chars.py [-h] [-a] [+a] [//noarg]

Change the option prefix characters

options:
  -h, --help        show this help message and exit
  -a                Turn A off
  +a                Turn A on
  //noarg, ++noarg

D:\DS_Works\Python-3\PY3SL\code\ch14\1_argparse>python argparse_prefix_chars.py +a
Namespace(a=True, noarg=False)

D:\DS_Works\Python-3\PY3SL\code\ch14\1_argparse>python argparse_prefix_chars.py -a
Namespace(a=False, noarg=False)

D:\DS_Works\Python-3\PY3SL\code\ch14\1_argparse>python argparse_prefix_chars.py ++noarg
Namespace(a=None, noarg=True)

D:\DS_Works\Python-3\PY3SL\code\ch14\1_argparse>python argparse_prefix_chars.py //noarg
Namespace(a=None, noarg=True)

D:\DS_Works\Python-3\PY3SL\code\ch14\1_argparse>python argparse_prefix_chars.py --noarg 
usage: argparse_prefix_chars.py [-h] [-a] [+a] [//noarg]
argparse_prefix_chars.py: error: unrecognized arguments: --noarg