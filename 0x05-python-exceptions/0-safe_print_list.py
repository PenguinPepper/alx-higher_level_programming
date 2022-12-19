#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    # print the elements specified by x
    try:
        for x in my_list[:x]:
            print("{}".format(x), end="")

    # if x is out of range do not stop the excution
    except IndexError:
        pass

    # Prints a new line
    print('')
    return x
