#!/usr/bin/python3
"""Module contains a function that writes a file"""


def write_file(filename="", text=""):
    """"Function writes to a file

    Args:
        filename(str): name of file to be opened
        text(str): text to be written to the file
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(text)
    return(len(text))
