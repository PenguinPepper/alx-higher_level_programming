#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        new_list = []
        for list_length in my_list_1[:list_length]:
            for list_length in my_list_2[:list_length]:
                pass
            result = list_length / list_length
            new_list.append(result)

    except ZeroDivisionError:
        print("division by 0".format())
    except (TypeError, ValueError):
        print("wrong type".format())
        result = 0
        new_list.append(result)
    except IndexError:
        print("out of range".format())
    return (new_list)
