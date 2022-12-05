#!/usr/bin/python3
def print_list_integer(my_list=[]):
    list_length = len(my_list)
    for i in range(0, list_length):
        print("{:d}".format(i))
