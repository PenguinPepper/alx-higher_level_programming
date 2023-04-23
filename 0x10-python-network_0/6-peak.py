#!/usr/bin/python3
"""
Function that finds a peak in an unsorted list
"""


def find_peak(list_of_integers):
    """
    Function that finds the peak in an unsorted array

    maxi = 0
    for i in range(len(list_of_integers)):
        if list_of_integers[i] > maxi:
            maxi = list_of_integers[i]
    if maxi == 0:
        return None
    return maxi
    """
    mid= len(list_of_integers) // 2
    if not list_of_integers:
        return None
    if list_of_integers[mid] > list_of_integers[mid + 1] and list_of_integers[mid] > list_of_integers[mid - 1]:
        return list_of_integers[mid]
    elif list_of_integers[mid] < list_of_integers[mid + 1] and list_of_integers[mid] > list_of_integers[mid - 1]:
        return list_of_integers[mid + 1]
    else:
        return max(list_of_integers)
