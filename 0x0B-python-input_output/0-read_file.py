#!/usr/bin/python3
"""
function that reads a text file and prints it in stdout
"""


def read_file(filename=""):
    """ reads a text file in (UTF8) and prints it in stdout """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
