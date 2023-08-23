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
    """"""
    assert os.path.exists(prg)
