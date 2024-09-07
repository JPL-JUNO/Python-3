#!/cygdrive/d/Python3.11.1/python

import os
from subprocess import getstatusoutput, getoutput

prg = "./hello.py"


def test_exists():
    assert os.path.isfile(prg)


def test_runnable():
    out = getoutput(f"python {prg}")
    assert out.strip() == "Hello, World!"


def test_executable():
    """这个有点难测试"""
    out = getoutput(f"bash -c {prg}")
    assert out.strip() == "Hello, World!"


def test_usage():

    for flag in ["-h", "--help"]:
        rv, out = getstatusoutput(f"python {prg} {flag}")

        assert rv == 0
        assert out.lower().startswith("usage")


def test_input():
    for val in ["Universe", "Multiverse"]:
        for option in ["-n", "--name"]:
            rv, out = getstatusoutput(f"python {prg} {option} {val}")
            assert rv == 0
            assert out.strip() == f"Hello, {val}!"
