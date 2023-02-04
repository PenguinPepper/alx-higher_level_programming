#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new_list = list(a_dictionary)
    if key not in new_list:
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value
    return a_dictionary
