#!/usr/bin/python3
def print_last_digit(number):
    if (number > 0):
        the_last = number % 10
    else:
        the_last = abs(number) % 10
    return (the_last)
