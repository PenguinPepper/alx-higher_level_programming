#!/usr/bin/python3
"""Module contains a function that writes JSON objects to a file"""


import json


def save_to_json_file(my_obj, filename):
    """Funtion writes an object to a text file in JSON form

    Args:
        my_obj(obj): object to be written to file
        filename(file): file to write to
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)
