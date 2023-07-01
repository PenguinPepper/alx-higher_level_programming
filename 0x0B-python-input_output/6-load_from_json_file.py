#!/usr/bin/python3
"""Module contains a function that creates a object from a JSON file"""


import json


def load_from_json_file(filename):
    """Function creates an object from a JSON file

    Args:
        filename(file): file to deserealise
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        json.load(f)
