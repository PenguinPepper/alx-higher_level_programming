#!/usr/bin/python3
def print_list_integer(my_list=[]):
    list_last = len(my_list) + 1
    for i in range(list_last):
        if i == 0:
            continue
        print("{:d}".format(i))
