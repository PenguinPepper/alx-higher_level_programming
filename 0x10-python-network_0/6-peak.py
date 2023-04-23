#!/usr/bin/python3
"""
Function that finds a peak in an unsorted list
"""


def find_peak(list_of_integers):
    """
    Function that finds the peak in an unsorted array
    """
    maxi = 0
    for i in range(len(list_of_integers)):
        if list_of_integers[i] > maxi:
            maxi = list_of_integers[i]
    if maxi == 0:
        return None
    return maxi
