#!/usr/bin/python3
""""Module contains function that appends to file"""


def append_write(filename="", text=""):
    """"Function appends text to a given file

    Args:
        filename(str): name of file to append to
        text(str): text to append
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        f.write(text)
    return len(text)
