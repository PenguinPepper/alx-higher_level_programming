#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    key_list = list(a_dictionary)
    new_dict = {}
    for i in key_list:
        new_dict[i] = a_dictionary.get(i) * 2
    return new_dict
