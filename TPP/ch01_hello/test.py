#!/usr/bin/env python3

import os
from subprocess import getstatusoutput, getoutput

prg = "./hello.py"


def test_exists():
    assert os.path.isfile(prg)


def test_runnable():
    out = getoutput(f"python {prg}")
    assert out.strip() == "Hello, World!"


def test_executable():

    out = getoutput(prg)
    assert out.strip() == ""


def test_usage():

    for flag in ["-h", "--help"]:
        rv, out = getstatusoutput(f"python {prg} {flag}")

        assert rv == 0
        assert out.lower().startswith("usage")


getstatusoutput("hello.py --help")
