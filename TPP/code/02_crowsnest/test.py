#!/usr/bin/env python3
"""
@Title:
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-23 10:00:23
@Description:
"""

import os
from subprocess import getoutput, getstatusoutput

prg = './crowsnest.py'

consonant_words = [
    "brigantine", "clipper", "dreadnought", "frigate", "gallon", "haddock",
    "junk", "ketch", "longboat", "mullet", "narwhal", "porpoise", "quay",
    "regatta", "submarine", "tanker", "vessel", "whale", "xebec", "yatch", "zebrafish"
]

vowel_words = ["aviso", "eel", "iceberg", "octopus", "upbound"]
template = "Ahoy, Caption, {} {} off the larboard bow!"


def test_exists():
    """测试文件是否存在"""
    assert os.path.exists(prg)


def test_usage():
    """"""
    for flag in ["-h", "--help"]:
        rv, out = getstatusoutput(f"python {prg} {flag}")
        assert rv == 0
        print(out)
        assert out.lower().startswith("usage")


def test_consonant():
    """brigantine -> a brigantine"""
    for word in consonant_words:
        # 程序运行的结果将会被返回至 out 变量
        # The output from running the program will go into the out variable, which
        # will be used to see if the program created the correct output for a given word.
        out = getoutput(f"python {prg} {word}")
        # The line starting with the plus sign (+) is what the test expected
        assert out.strip() == template.format("a", word)


def test_consonant_upper():
    """brigantine -> a Brigantine"""
    for word in consonant_words:
        out = getoutput(f"python {prg} {word.title()}")
        assert out.strip() == template.format("a", word.title())


def test_vowel():
    """octopus -> an octopus"""
    for word in vowel_words:
        out = getoutput(f"python {prg} {word}")
        assert out.strip() == template.format("an", word)


def test_vowel_upper():
    """octopus -> an Octopus"""
    for word in vowel_words:
        out = getoutput(f"python {prg} {word.upper()}")
        assert out.strip() == template.format("an", word.upper())
