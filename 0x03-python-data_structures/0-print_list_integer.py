#!/usr/bin/python3
def print_list_integer(my_list=[]):
    list_last = len(my_list) + 1
    for i in range(1, list_last):
        print("{:d}".format(i))
