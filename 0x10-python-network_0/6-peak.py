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
    """
    mid= len(list_of_integers) // 2
    my_list = list_of_integers
    if not my_list:
        return None
    if my_list[mid] > my_list[mid + 1] and my_list[mid] > my_list[mid - 1]:
        return list_of_integers[mid]
    elif my_list[mid] < my_list[mid + 1] and my_list[mid] > my_list[mid - 1]:
        return my_list[mid + 1]
    elif my_list[mid] > my_list[mid + 1] and my_list[mid] < my_list[mid - 1]:
        return my_list[mid- 1]
    else:
        return max(my_list)
    """
