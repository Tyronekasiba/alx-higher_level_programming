#!/usr/bin/python3
"""
function that writes a string to a text file in utf-8 and returns the number of charactors written.
"""


def write_file(filename="", text=""):
    """
    writes a text file in utf-8 and returns number of charactors in stdout
    """
    with open(filename, 'w', encoding='utf-8') as f :
        return f.write(text)
