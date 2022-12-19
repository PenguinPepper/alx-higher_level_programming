#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        for x in my_list[:x]:
            try:
                print("{:d}".format(x), end="")
            except (ValueError, TypeError):
                continue
                x += 1
        print('')
        return x
    except (TypeError, ValueError):
        pass
    print('')
    return x
