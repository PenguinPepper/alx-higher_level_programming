#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        new_num = number * -1
        the_last = (-1) * (new_num % 10)
        the_last = the_last * -1
    else:
        the_last = number % 10
    print("{:d}".format(the_last), end='')
    return (the_last)
