#!usr/bin/python3
"""Module contains function that returns an object"""


import json


def from_json_string(my_str):
    """"Function returns a python object from a json string

    Args:
        my_str(json): json object to be convereted

    Returns:
        my_obj(obj): python object conversion
    """
    my_obj = json.loads(my_str)
    return my_obj
