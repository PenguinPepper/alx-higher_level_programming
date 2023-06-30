#!/usr/bin/python3
""""Module contains function that opens a file"""

def read_file(filename=""):
    """Function opens a file

    Args:
        filename(str): file to be opened
    """
    with open(filename, encoding="utf-8", newline=None) as f:
        text = f.read()
    print(text, end="")
