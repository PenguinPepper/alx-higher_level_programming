#!/usr/bin/python3
"""Module contains function that jsonifies a given object"""


import json


def to_json_string(my_obj):
    """"Function jsoinifies an object

    Args:
        my_obj(obj): object to be jsonified
    """
    return json.dumps(my_obj)
