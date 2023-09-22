import os
from subprocess import getstatusoutput, getoutput
prg = './hello.py'


def test_exists():
    """"""
    assert os.path.exists(prg)


def test_runnable():
    out = getoutput(f'python {prg}')
    assert out.strip() == 'Hello, World!'

# 没有办法执行Windows
# def test_executable():
#     out = getoutput(prg)
#     assert out.strip() == 'Hello, World!'
