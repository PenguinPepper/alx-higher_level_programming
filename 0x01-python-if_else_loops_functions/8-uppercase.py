#!/usr/bin/python3
def uppercase(string):
    empt_str = ""
    for i in string:
        values = i.capitalize()
        empt_str += values
    print("{}".format(empt_str))
