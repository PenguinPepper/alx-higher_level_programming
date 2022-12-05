#!/usr/bin/python3
def print_list_integer(my_list=[]):
    list_length = len(my_list) + 1
    for i in range(list_length):
        print("{:d}".format(i))
