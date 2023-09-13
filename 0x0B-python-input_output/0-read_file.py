#!/usr/bin/python3
"""defines a readline function"""


def read_file(filename=""):
    """prints utf-8 tf to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
